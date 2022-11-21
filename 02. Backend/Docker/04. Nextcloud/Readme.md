### Android App Error - Strict mode: no http connection
* https://www.reddit.com/r/NextCloud/comments/qawc7e/android_app_strict_mode_no_http_connection/

```php
<?php
$CONFIG = array (
  'htaccess.RewriteBase' => '/',
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'apps_paths' => 
  array (
    0 => 
    array (
      'path' => '/var/www/html/apps',
      'url' => '/apps',
      'writable' => false,
    ),
    1 => 
    array (
      'path' => '/var/www/html/custom_apps',
      'url' => '/custom_apps',
      'writable' => true,
    ),
  ),
  'instanceid' => 'ID_HERE',
  'passwordsalt' => 'SALT_HERE',
  'secret' => 'SECRET_HERE',
  'trusted_domains' => 
  array (
    0 => '192.168.X.X:PORT#',
    1 => 'YOUR_DOMAIN.duckdns.org',
  ),
  'datadirectory' => '/var/www/html/data',
  'dbtype' => 'mysql',
  'version' => '25.0.0.18',
  'overwrite.cli.url' => 'http://192.168.X.X:PORT#',
  'overwriteprotocol' => 'https',
  'dbname' => 'nextcloud',
  'dbhost' => 'next_db',
  'dbport' => 'dbPORT#',
  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'nextcloud',
  'dbpassword' => 'PW_HERE',
  'installed' => true,
);
```