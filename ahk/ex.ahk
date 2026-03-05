#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%

;崇高
X := 300
Y := 270
targetX := 328
targetY := 456

MouseMove, X, Y
Sleep, 100
Click, right
Sleep, 100

MouseMove, targetX, targetY
Sleep, 100
Click, left