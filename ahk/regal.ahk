#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%

;富豪
X := 435
Y := 270
targetX := 328
targetY := 456

MouseMove, X, Y
Sleep, 50
Click, right
Sleep, 50

MouseMove, targetX, targetY
Sleep, 50
Click, left