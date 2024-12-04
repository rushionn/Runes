import time
from pynput import mouse, keyboard
import threading

# 用于保存事件的列表
events = []

def on_click(x, y, button, pressed):
    event = f"{time.time()}: {'Pressed' if pressed else 'Released'} {button} at ({x}, {y})"
    events.append(event)

def on_scroll(x, y, dx, dy):
    event = f"{time.time()}: Scrolled at ({x}, {y}) with delta ({dx}, {dy})"
    events.append(event)

def on_press(key):
    try:
        event = f"{time.time()}: Key {key.char} pressed."
    except AttributeError:
        event = f"{time.time()}: Special Key {key} pressed."
    events.append(event)

def on_release(key):
    event = f"{time.time()}: Key {key} released."
    events.append(event)
    if key == keyboard.Key.esc:  # 使用esc鍵結束錄製
        return False

def start_recording():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as k_listener, \
         mouse.Listener(on_click=on_click, on_scroll=on_scroll) as m_listener:
        k_listener.join()
        m_listener.join()

def save_events(filename):
    with open(filename, 'w') as f:
        for event in events:
            f.write(event + '\n')

if __name__ == "__main__":
    # 在这里可以添加初始化代码或者从其他模块导入
    pass