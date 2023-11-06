import tkinter as tk
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            for i in range(5):  # Sound alert 5 times
                winsound.Beep(1000, 1000)  # Beep sound
            break

def stop_alarm():
    # You can add functionality here to stop the alarm
    pass

# Creating the main window with a medium size
root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("300x200")  # Width x Height

# Creating the labels and entry for alarm time
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Buttons to set and stop the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm)
stop_button.pack()

# Run the application
root.mainloop()
