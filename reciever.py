from pynput import keyboard
import webbrowser
import subprocess


buffer = ""
prefix = "#!_-"
def on_type(key):
    global buffer
    try:
        buffer += key.char
        if prefix + "OPEN_GMAIL" in buffer:
            webbrowser.open("https://mail.google.com/mail/u/0")
            buffer = ""
        if prefix + "OPEN_VS_CODE" in buffer:
            subprocess.Popen(['code'])
            buffer = ""
        if prefix + "OPEN_YOUTUBE_MUSIC" in buffer:
            webbrowser.open("https://www.youtube.com/watch?v=RlPNh_PBZb4&list=RDMM")
            buffer = ""
        if prefix + "OPEN_TERMINAL" in buffer:
            subprocess.Popen(['ptyxis'])
            buffer = ""
    except AttributeError:
        pass


with keyboard.Listener(on_press=on_type) as listener:
    listener.join()
