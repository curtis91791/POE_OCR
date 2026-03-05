#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%

;增幅
X := 226
Y := 328
targetX := 328
targetY := 456

MouseMove, X, Y
Sleep, 50
Click, right
Sleep, 50

MouseMove, targetX, targetY
Sleep, 50
Click, left