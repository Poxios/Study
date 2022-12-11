# Delete large folder faster than default windows gui remove animation
* Copy this text file to `c:\windows\quick_delete.bat` (or somewhere PATH)
```bat
@ECHO OFF
ECHO Delete Folder: %CD%?
PAUSE
SET FOLDER=%CD%
CD /
DEL /F/Q/S "%FOLDER%" > NUL
RMDIR /Q/S "%FOLDER%"
EXIT
```
1. Go to `HKEY_CLASSES_ROOT\Directory\shell\`
2. Create key `Quick Remove`
3. Create key `command` in `Quick Remove`
4. Change key `command`'s value to `cmd /c "cd %1 && quick_delete.bat"`
* https://pureinfotech.com/delete-large-folder-fast-windows-10/

### or just with cmd
```cmd
rmdir /s /q FOLDER_NAME
```
### or just with bash (linux)
```
rm -rf FOLDER_OR_FILE_NAME
```