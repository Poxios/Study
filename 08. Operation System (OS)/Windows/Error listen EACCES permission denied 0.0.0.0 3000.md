# Error: listen EACCES: permission denied 0.0.0.0:3000
## Solution
```cmd
net stop winnat
net start winnat
```
Type these on cmd.