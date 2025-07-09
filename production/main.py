# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Tap, Macros, Delay

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

prefix = "#!_-"

OPEN_GMAIL_STRING = prefix + "OPEN_GMAIL"
OPEN_GMAIL = KC.MACRO(OPEN_GMAIL_STRING, Delay(0.1), *[Tap(KC.BACKSPACE) for _ in range(len(OPEN_GMAIL_STRING))])

OPEN_VS_CODE_STRING = prefix + "OPEN_VS_CODE"
OPEN_VS_CODE = KC.MACRO(OPEN_VS_CODE_STRING, Delay(0.1), *[Tap(KC.BACKSPACE) for _ in range(len(OPEN_VS_CODE_STRING))])

OPEN_YOUTUBE_MUSIC_STRING = prefix + "OPEN_YOUTUBE_MUSIC"
OPEN_YOUTUBE_MUSIC = KC.MACRO(OPEN_YOUTUBE_MUSIC_STRING, Delay(0.1), *[Tap(KC.BACKSPACE) for _ in range(len(OPEN_YOUTUBE_MUSIC_STRING))])

OPEN_TERMINAL_STRING = prefix + "OPEN_TERMINAL"
OPEN_TERMINAL = KC.MACRO(OPEN_TERMINAL_STRING, Delay(0.1), *[Tap(KC.BACKSPACE) for _ in range(len(OPEN_TERMINAL_STRING))])

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [OPEN_GMAIL, OPEN_VS_CODE, OPEN_YOUTUBE_MUSIC, OPEN_TERMINAL]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()