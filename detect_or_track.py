import argparse
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn
from PyQt5.QtWidgets import QLabel
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, \
                check_imshow, non_max_suppression, apply_classifier, \
                scale_coords, xyxy2xywh, strip_optimizer, set_logging, \
                increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from sort import *


"""Function to Draw Bounding boxes"""
def draw_boxes(img, bbox, identities=None, categories=None, confidences = None, names=None, colors = None):
    # print('x')
    for i, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(i) for i in box]
        tl = round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness

        cat = int(categories[i]) if categories is not None else 0
        id = int(identities[i]) if identities is not None else 0
        # conf = confidences[i] if confidences is not None else 0

        color = colors[cat]

        # if not opt.nobbox:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, tl)

        # if not opt.nolabel:
        label = str(id) + ":"+ names[cat] if identities is not None else  f'{names[cat]} {confidences[i]:.2f}'
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = x1 + t_size[0], y1 - t_size[1] - 3
        cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (x1, y1 - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    return img


class detect(QThread):
    signal = pyqtSignal(QImage, QLabel)

    def __init__(self, cam_link, label, width, height):
        self.cam_link = cam_link
        self.label = label
        self.width = width
        self.height = height
        super(detect, self).__init__()

    def run(self):
        self.hilo_corriendo = True
        sort_tracker = Sort(max_age=5,
                           min_hits=2,
                           iou_threshold=0.2)
        source, weights, imgsz = str(self.cam_link), 'yolov7.pt', 640
        print(source, type(source))
        webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
            ('rtsp://', 'rtmp://', 'http://', 'https://'))
        print(webcam)

        # Initialize
        set_logging()
        device = select_device('')
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(weights, map_location=device)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        imgsz = check_img_size(imgsz, s=stride)  # check img_size

        if half:
            model.half()  # to FP16

        vid_path, vid_writer = None, None
        if webcam:
        # if source.isnumeric() == False:
            view_img = check_imshow()
            cudnn.benchmark = True  # set True to speed up constant image size inference
            dataset = LoadStreams(source, img_size=imgsz, stride=stride)
        else:
            dataset = LoadImages(source, img_size=imgsz, stride=stride)

        # Get names and colors
        names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

        # Run inference
        if device.type != 'cpu':
            model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
        old_img_w = old_img_h = imgsz
        old_img_b = 1

        t0 = time.time()
        ###################################
        startTime = 0
        ###################################
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Warmup
            if device.type != 'cpu' and (old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
                old_img_b = img.shape[0]
                old_img_h = img.shape[2]
                old_img_w = img.shape[3]
                for i in range(3):
                    model(img)[0]

            # Inference
            t1 = time_synchronized()
            pred = model(img)[0]
            t2 = time_synchronized()

            # Apply NMS
            pred = non_max_suppression(pred, 0.25, 0.45, classes=0)
            t3 = time_synchronized()

            for i, det in enumerate(pred):  # detections per image
                if webcam:  # batch_size >= 1
                    p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
                else:
                    p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                    dets_to_sort = np.empty((0,6))
                    # NOTE: We send in detected object class too
                    for x1,y1,x2,y2,conf,detclass in det.cpu().detach().numpy():
                        dets_to_sort = np.vstack((dets_to_sort,
                                    np.array([x1, y1, x2, y2, conf, detclass])))

                    # if opt.track:

                    tracked_dets = sort_tracker.update(dets_to_sort)
                    tracks =sort_tracker.getTrackers()

                    # draw boxes for visualization
                    if len(tracked_dets)>0:
                        bbox_xyxy = tracked_dets[:,:4]
                        identities = tracked_dets[:, 8]
                        categories = tracked_dets[:, 4]
                        confidences = None

                        im0 = draw_boxes(im0, bbox_xyxy, identities, categories, confidences, names, colors)
                rgb_image = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pic = convert_to_Qt_format.scaled(self.width, self.height, Qt.KeepAspectRatio)

                # Image = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
                # flip = cv2.flip(Image, 1)
                # convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                # pic = convertir_QT.scaled(1024, 800, Qt.KeepAspectRatio)
                self.signal.emit(pic, self.label)

                # Print time (inference + NMS)
                print(f'{s}Done. ({(1E3 * (t2 - t1)):.1f}ms) Inference, ({(1E3 * (t3 - t2)):.1f}ms) NMS')

                # Stream results
                ######################################################
                if dataset.mode != 'image': # and opt.show_fps:
                    currentTime = time.time()

                    fps = 1/(currentTime - startTime)
                    startTime = currentTime
                    cv2.putText(im0, "FPS: " + str(int(fps)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0),2)

                #######################################################
                # if view_img:
                #     cv2.imshow(str(p), im0)
                #     cv2.waitKey(1)  # 1 millisecond

        print(f'Done. ({time.time() - t0:.3f}s)')

    def stop(self):
        self.hilo_corriendo = False
        self.quit()

# with torch.no_grad():
#     detect()
#     strip_optimizer('yolov7.pt')
