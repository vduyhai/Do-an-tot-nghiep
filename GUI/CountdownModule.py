import threading
import time
import tkinter as tk
from win10toast import ToastNotifier

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('')
        self.root.title('Countdown Timer')

        self.time_entry = tk.Entry(self.root, font = ('Arial', 30))
        self.time_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.start_button = tk.Button(self.root, font=('Arial', 30), text='Start', command=self.start_thread)
        self.start_button.grid(row=8, column=20, padx=5, pady=5)

        self.stop_button = tk.Button(self.root, font=('Arial', 30), text='Stop', command=self.start_thread)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.root, font=('Arial', 30), text='Time: 00:00:00')
        self.time_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.stop_loop = False

        self.root.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        self.stop_loop= False

        hours, mins, secs = 0, 0, 0
        string_split = self.time_entry.get().split(':')
        if len(string_split) == 3:
            hours = int(string_split[0])
            mins = int(string_split[1])
            secs = int(string_split[2])
        elif len(string_split) == 2:
            mins = int(string_split[0])
            secs = int(string_split[1])
        elif len(string_split) == 1:
            secs = int(string_split[0])
        else:
            print('Invalid time format')
            return

        full_secs = hours*3600 + mins*60 + secs

        while int(full_secs) > 0 and not self.stop_loop:
            full_secs -= 1

            mins, secs = divmod(full_secs, 60)
            hours, mins = divmod(mins, 60)

            self.time_label.config(text=f'Time: {hours:02d}:{mins:02d}:{secs:02d}')
            self.root.update()
            time.sleep(1)
        if not self.stop_loop:
            toast = ToastNotifier()
            toast.show_toast('Countdown Timer', 'Time is up!', duration=10)

    def stop(self):
        self.stop_loop = True
        self.time_label.config(text='Text: 00:00:00')

CountdownTimer()