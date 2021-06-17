# 윈도우 ISO - WIM 파일 내에서 필요 없는 윈도우 버전 날려버리기
* https://superuser.com/questions/1065108/remove-editions-of-windows-7-iso
* 윈도우 7이지만 방법은 동일.
* `Dism /Get-WimInfo /WimFile:DVDDRIVELETTER:\sources\install.wim` 이거로 해당 WIM파일이 가지고 있는 버전을 확인한다.
* `Dism /Export-Image /SourceImageFile:DVDDRIVELETTER:\sources\install.wim /SourceIndex:4 /DestinationImageFile:C:\Win7Ultimate\sources\install.wim /DestinationName:"Windows 7 Ultimate"` 이거로 새로운 WIM을 제작한다.
