# File System Service

## Configuration

```ini

```

### Changing the File System Service Provider

```ini
PROVIDER_FILE_SYSTEM=\PhalconKit\Provider\FileSystem\ServiceProvider
```

### FileSystem Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\FileSystem\ServiceProvider::class => Env::get('PROVIDER_FILE_SYSTEM', \PhalconKit\Provider\FileSystem\ServiceProvider::class),
    ],
    'fileSystem' => [
        'driver' => Env::get('FILE_SYSTEM_DRIVER', 'local'),
        'drivers' => [
            'local' => [
                'rootDirectory' => Env::get('FILE_SYSTEM_LOCAL_ROOT_DIRECTORY', ROOT_PATH)
            ],
            'ftp' => [
                'host' => Env::get('FILE_SYSTEM_FTP_HOST'), // required
                'root' => Env::get('FILE_SYSTEM_FTP_ROOT'), // required
                'username' => Env::get('FILE_SYSTEM_FTP_USERNAME'), // required
                'password' => Env::get('FILE_SYSTEM_FTP_PASSWORD'), // required
                'port' => Env::get('FILE_SYSTEM_FTP_PORT', 21),
                'ssl' => Env::get('FILE_SYSTEM_FTP_SSL', false),
                'timeout' => Env::get('FILE_SYSTEM_FTP_TIMEOUT', 10),
                'utf8' => Env::get('FILE_SYSTEM_FTP_UTF8', false),
                'passive' => Env::get('FILE_SYSTEM_FTP_PASSIVE', true),
                'transferMode' => Env::get('FILE_SYSTEM_FTP_TRANSFER_MODE', defined('FTP_BINARY')? FTP_BINARY : 2),
                'systemType' => Env::get('FILE_SYSTEM_FTP_SYSTEM_TYPE'), // windows or unix
                'ignorePassiveAddress' => Env::get('FILE_SYSTEM_FTP_SYSTEM_IGNORE_PASSIVE_ADDRESS'), // true or false
                'timestampsOnUnixListingsEnabled' => Env::get('FILE_SYSTEM_FTP_TIMESTAMPS_ON_UNIX_LISTING_ENABLED', false), // true or false
                'recurseManually' => Env::get('FILE_SYSTEM_FTP_RECURSE_MANUALLY', true), // true or false
            ],
            'sftp' => [
                'host' => Env::get('FILE_SYSTEM_SFTP_HOST'), // required
                'username' => Env::get('FILE_SYSTEM_SFTP_USERNAME'), // required
                'password' => Env::get('FILE_SYSTEM_SFTP_PASSWORD'), // set to null if privateKey is used
                'privateKey' => Env::get('FILE_SYSTEM_SFTP_STORAGE_KEY'), // can be used instead of password, set to null if password is set
                'passphrase' => Env::get('FILE_SYSTEM_SFTP_PASSPHRASE'), //  set to null if privateKey is not used or has no passphrase
                'port' => Env::get('FILE_SYSTEM_SFTP_PORT', 22),
                'useAgent' => Env::get('FILE_SYSTEM_SFTP_USE_AGENT', false),
                'timeout' => Env::get('FILE_SYSTEM_SFTP_TIMEOUT', 10),
                'maxTries' => Env::get('FILE_SYSTEM_SFTP_MAX_TRIES', 4),
                'hostFingerprint' => Env::get('FILE_SYSTEM_SFTP_HOST_FINGERPRINT'),
                'connectivityChecker' => Env::get('FILE_SYSTEM_SFTP_CONNECTIVITY_CHECKER'),
            ],
            'memory' => [
                // nothing
            ],
            'readOnly' => [
                // nothing
            ],
            'awsS3' => [
                'bucketName' => Env::get('FILE_SYSTEM_AWS_S3_BUCKET_NAME'),
                'pathPrefix' => Env::get('FILE_SYSTEM_AWS_S3_PATH_PREFIX')
            ],
            'googleCloudStorage' => [
                'bucketName' => Env::get('FILE_SYSTEM_GOOGLE_CLOUD_STORAGE_BUCKET_NAME'),
                'pathPrefix' => Env::get('FILE_SYSTEM_GOOGLE_CLOUD_STORAGE_PATH_PREFIX')
            ],
            'azureBlobStorage' => [
                'containerName' => Env::get('FILE_SYSTEM_AZURE_BLOB_STORAGE_CONTAINER_NAME'),
                'pathPrefix' => Env::get('FILE_SYSTEM_AZURE_BLOB_STORAGE_PATH_PREFIX')
            ],
            'webdav' => [
                'baseUri' => Env::get('FILE_SYSTEM_WEBDAV_BASE_URI'),
                'userName' => Env::get('FILE_SYSTEM_WEBDAV_USERNAME'),
                'password' => Env::get('FILE_SYSTEM_WEBDAV_PASSWORD'),
            ],
            'zipArchive' => [
                'path' => Env::get('FILE_SYSTEM_ZIP_ARCHIVE_PATH')
            ],
        ],
    ],
]);
```

## File System Service (`fileSystem`)

!!! info "File Service Provider"
    File Service Provider (`fileSystem`):
    [`\PhalconKit\Provider\File\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/FileSystem/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$file = $this->fileSystem;

// Retrieving the service from the DI
$file = $this->di->get('fileSystem');

// Retrieving the service from the getDI()
$file = $this->getDI()->get('fileSystem');

// Retrieving the service from anywhere
$file = Di::getDefault()->get('fileSystem');
```
