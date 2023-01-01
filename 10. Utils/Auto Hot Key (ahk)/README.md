# Auto Hot Key 관련 폴더
### Alt + `
* 음악 일시정지 / 재생

### Alt + 1
* 카카오톡 보이기

### Alt + 2
* 카카오톡 숨기기

## 시작 폴더 접근 명령어
* `shell:startup`
* `shell:common startup`

# Run as `System` rights
Start command below as administrator rights
```powershell
./psexec.exe -s -i -d  "C:\Program Files\AutoHotkey\AutoHotkey.exe" "C:\Users\yalle\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\All.ahk"
```