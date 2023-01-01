* move root files to subdir
```bash
git filter-repo --to-subdirectory-filter "$REPO_NAME"
```

* Move files/folders with history
```
git filter-repo --path-rename OLD_NAME:TARGET_NAME
```

* Move a repo to another repo's subdir
* https://medium.com/@ayushya/move-directory-from-one-repository-to-another-preserving-git-history-d210fa049d4b
* Use this url with git filter-repo (above)
* 
### Remove file with commit history
1. Install `git-filter-repo`. [url](https://github.com/newren/git-filter-repo/blob/main/INSTALL.md#simple-installation)
### Windows
```cmd
git filter-repo --invert-paths --path <path to the file or directory>
```

### Other OS
```bash
python git-filter-repo.py --invert-paths --path <path to the file or directory>
```
