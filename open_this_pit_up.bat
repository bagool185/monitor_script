set env=python.exe

@ECHO OFF
:loop
  start python open_this_pit_up.py
  timeout /t 60
 goto loop

