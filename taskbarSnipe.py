import pyautogui
import win32gui

def get_taskbar_rect():
    taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    rect = win32gui.GetWindowRect(taskbar)
    return rect

def is_cursor_over_taskbar():
    taskbar_rect = get_taskbar_rect()
    cursor_position = pyautogui.position()
    return cursor_position[1] >= taskbar_rect[1]

def hide_taskbar():
    taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    win32gui.ShowWindow(taskbar, 0)

def show_taskbar():
    taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    win32gui.ShowWindow(taskbar, 5)

while True:
    if is_cursor_over_taskbar():
        show_taskbar()
    else:
        hide_taskbar()
