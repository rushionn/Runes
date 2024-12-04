import tkinter as tk
from tkinter import messagebox
import recorder
import threading

def start_recording():
    record_thread = threading.Thread(target=recorder.start_recording)
    record_thread.start()
    messagebox.showinfo("Info", "Recording started. Press ESC to stop.")

def save_recording():
    recorder.save_events("recording.txt")
    messagebox.showinfo("Info", "Recording saved as recording.txt")

def create_ui():
    root = tk.Tk()
    root.title("Keyboard and Mouse Recorder")

    start_button = tk.Button(root, text="Start Recording", command=start_recording)
    start_button.pack(pady=20)

    save_button = tk.Button(root, text="Save Recording", command=save_recording)
    save_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()