# Imap Service

The `imap` service uses the [PHP Imap](https://github.com/barbushin/php-imap){:target="_blank"} library.
You can manage mailboxes, filter/get/delete emails in PHP (supports IMAP/POP3/NNTP)

PHP IMAP Mailbox is a powerful and open source library to connect to a mailbox by POP3, IMAP and NNTP using the PHP IMAP
extension. This library allows you to fetch emails from your email server. Extend the functionality or create powerful
web applications to handle your incoming emails.

## Configurations

```ini
# IMAP server and mailbox folder
IMAP_PATH=

# Username for the before configured mailbox
IMAP_LOGIN=

# Password for the before configured username
IMAP_PASSWORD=

# Directory, where attachments will be saved (optional)
IMAP_ATTACHMENTS_DIR=

# Server encoding (optional)
IMAP_SERVER_ENCODING=UTF-8

# Trim leading/ending whitespaces of IMAP path
IMAP_TRIM_IMAP_PATH=true

# Attachment filename mode (optional; false = random filename; true = original filename)
IMAP_ATTACHMENT_FILENAME_MODE=false
```

### Imap Service Provider

```ini
PROVIDER_IMAP = \Zemit\Provider\Imap\ServiceProvider
```

### Imap Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Imap\ServiceProvider::class => Env::get('PROVIDER_IMAP', \Zemit\Provider\Imap\ServiceProvider::class),
    ],
    'imap' => [
        'path' => Env::get('IMAP_PATH'), // IMAP server and mailbox folder
        'login' => Env::get('IMAP_LOGIN'), // Username for the before configured mailbox
        'password' => Env::get('IMAP_PASSWORD'), // Password for the before configured username
        'attachmentsDir' => Env::get('IMAP_ATTACHMENTS_DIR'), // Server encoding (optional)
        'serverEncoding' => Env::get('IMAP_SERVER_ENCODING', 'UTF-8'), // Directory, where attachments will be saved (optional)
        'trimImapPath' => Env::get('IMAP_TRIM_IMAP_PATH', true),   // Trim leading/ending whitespaces of IMAP path (optional)
        'attachmentFilenameMode' => Env::get('IMAP_ATTACHMENT_FILENAME_MODE', false), // Attachment filename mode (optional; false = random filename; true = original filename)
    ],
]);
```

## Imap Service (`imap`)

!!! info "Imap Service Provider"
    Imap Service Provider (`imap`):
    [`\Zemit\Provider\Imap\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Imap/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$imap = $this->imap;

// Retrieving the service from the DI
$imap = $this->di->get('imap');

// Retrieving the service from the getDI()
$imap = $this->getDI()->get('imap');

// Retrieving the service from anywhere
$imap = Di::getDefault()->get('imap');
```
