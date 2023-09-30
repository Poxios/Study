# 7zip
## Compress
```
7zz a -p123 -mhe=on -mx9 -v4500k "DEST_ZIP_FILE_NAME" "SOURCE_FILE_TO_ARCHIVE"
```
* password 123 `-p123`, encrypt file name (with aes option `-mhe=on`)

## Unarchive
```
7zz x "SOURCE_7Z_PATH" -o"DEST_FOLDER_PATH" -pPASSWORD
```