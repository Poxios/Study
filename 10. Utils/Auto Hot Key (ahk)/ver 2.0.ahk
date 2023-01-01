#Requires AutoHotkey v2.0
#SingleInstance Force
#WinActivateForce
; Key mapping for guacamole
$CapsLock::LWin ; capslock to win
$AppsKey::vk15 ; right context menu key to ime hangul

; 카카오톡 창 띄우고 Focus
!1::
{
  WinShow("카카오톡")
  WinActivate("카카오톡")
  return
}