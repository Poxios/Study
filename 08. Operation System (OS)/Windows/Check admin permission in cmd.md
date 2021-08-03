# cmd 창에서 관리자 권한 있는지 확인
```bat
@echo off
goto check_Permissions

:check_Permissions
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Success: Administrative permissions confirmed.
    ) else (
        echo Failure: Current permissions inadequate.
    )

    pause >nul
```
* https://stackoverflow.com/questions/4051883/batch-script-how-to-check-for-admin-rights
