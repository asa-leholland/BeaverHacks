import ctypes


def confirm(message, title, style):
    return ctypes.windll.user32.MessageBox(0, message, title, style)