## Settings for windows ssh (permission)
* https://superuser.com/questions/1342411/setting-ssh-keys-on-windows-10-openssh-server

> Note that if you are setting up keys for an administrator user, putting the public key to `%USERPROFILE%/.ssh/authorized_keys` will not work. `You must append the public key to %PROGRAMDATA%/ssh/administrators_authorized_keys` instead.

* Run this script with adminstrator powershell _this is chmod 600 in other os_
```ps1
$acl = Get-Acl C:\ProgramData\ssh\administrators_authorized_keys
$acl.SetAccessRuleProtection($true, $false)
$administratorsRule = New-Object system.security.accesscontrol.filesystemaccessrule("Administrators","FullControl","Allow")
$systemRule = New-Object system.security.accesscontrol.filesystemaccessrule("SYSTEM","FullControl","Allow")
$acl.SetAccessRule($administratorsRule)
$acl.SetAccessRule($systemRule)
$acl | Set-Acl
```