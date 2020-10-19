import win32api, win32gui
from win10toast import ToastNotifier
import pyperclip
import time

def get_pixel_colour(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x'

if __name__ == '__main__':
    time.sleep(2)
    x, y = win32api.GetCursorPos()
    color = rgb_to_hex(get_pixel_colour(x*2, y*2)).upper()
    pyperclip.copy(color)
    toaster = ToastNotifier()
    toaster.show_toast("Color grabbed !", color + " is now in your clipboard.", icon_path="./icon.ico", duration=3)
    