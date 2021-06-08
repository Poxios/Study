#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

!`::
sendInput {Media_Play_Pause}
return

; 카카오톡 창 띄우고 Focus
!1::
WinShow, 카카오톡
WinActivate, 카카오톡
return

; 카카오톡 창 숨기기
!2::
WinHide, 카카오톡
return

!3::
Run %A_AppData%\..\Local\Programs\Notion\Notion.exe
return

!4::
WinShow, ahk_exe Chrome.exe
WinActivate, ahk_exe Chrome.exe
return

!5::
WinShow, ahk_exe Discord.exe
WinActivate, ahk_exe Discord.exe
return