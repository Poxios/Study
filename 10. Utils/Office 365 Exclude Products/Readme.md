# Office 365 Exclude Products on install
1. Get `Setup.exe` (Office installer exe file)
2. https://config.office.com/deploymentsettings <- Make custom settings and Export - `Office Open Xml`
3. If there is <AppSettings> section, remove it.
4. Change xml name to below.
5. Execute `Setup.exe /configure o365_custom_configuration.xml`