import win32gui
import win32con

def find_window_by_url(url):
    def enum_windows_callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if url.lower() in window_title.lower():
                windows.append(hwnd)

    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows

def set_always_on_top(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# Buscar la ventana de WhatsApp Web
whatsapp_windows = find_window_by_url("new chat")
if len(whatsapp_windows) > 0:
    whatsapp_window = whatsapp_windows[0]
    set_always_on_top(whatsapp_window)
else:
    print("No se encontró la ventana abierta.")
