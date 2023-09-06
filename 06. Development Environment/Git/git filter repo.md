### Remove file with commit history
* https://github.com/newren/git-filter-repo/blob/main/INSTALL.md#simple-installation
```bash
git filter-repo --invert-paths --path PATH_TO_FILE_OR_DIR
```

### Move root files to subdir
```bash
git filter-repo --to-subdirectory-filter "$REPO_NAME"
```

### Move files/folders with history
```bash
git filter-repo --path-rename OLD_PATH:TARGET_PATH
```

### Move a repo to another repo's subdir
* https://medium.com/@ayushya/move-directory-from-one-repository-to-another-preserving-git-history-d210fa049d4b
* Use this url with git filter-repo
