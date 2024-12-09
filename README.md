# Reverse_shell
```shell
pip install pyautogui
```
```shell
pip install pyinstaller
```
```shell
pyinstaller --onefile --add-data "cmds.txt;." --add-data "shellcode.txt;." --add-data "payload.txt;." reverse_shell.py
```
