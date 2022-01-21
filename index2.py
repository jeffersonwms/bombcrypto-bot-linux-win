import json
import os
import sys
import mss
import time
import sys
import yaml
import numpy as np
import pyautogui
import platform
import subprocess
import webbrowser
from sys import platform as sys_platform
from src.logger import logger, loggerMapClicked
from cv2 import cv2
from os import listdir, getcwd, path, environ, popen
from random import randint
from random import random

def run_command(command):
    try:
        result = subprocess.check_output(command).decode("utf-8")
    except:
        result = [os.popen(command[0]).read()]
    return result

def get_windows_with_title(title):
    # sudo apt-get install xdotool wmctrl
    windows_list = [w.split() for w in run_command(["wmctrl", "-lG"]).splitlines()]
    # check if the window is "normal" and / or minimized
    windows_with_title = [
        {"id": w[0], "is_minimized": all([
            "_NET_WM_STATE_HIDDEN" not in run_command(["xprop", "-id", w[0]]),
            "_NET_WM_WINDOW_TYPE_NORMAL" in run_command(["xprop", "-id", w[0]])]),
         "application": " ".join(w[-2:]).replace("–", "").lstrip(), "title": w[7]
         } for w in windows_list if title in w[7]]

    return windows_with_title

widonws = get_windows_with_title('Bombcrypto')

print(widonws)