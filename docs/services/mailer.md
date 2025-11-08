# Mailer Service



## Mailer Configurations

```ini
MAILER_DRIVER=sendmail
MAILER_SENDMAIL=/usr/sbin/sendmail -bs
MAILER_SMTP_HOST=localhost
MAILER_SMTP_PORT=25
MAILER_SMTP_ENCRYPTION=
MAILER_SMTP_USERNAME=
MAILER_SMTP_PASSWORD=
MAILER_CHARSET=utf-8
MAILER_VIEWS_DIR=./app/Modules/Frontend/Views/
MAILER_BASE_URI=
MAILER_FROM_EMAIL=no-reply@localhost
MAILER_FROM_NAME=Phalcon Kit
MAILER_TO_EMAIL=
MAILER_CC_EMAIL=
MAILER_BCC_EMAIL=
```

### Mailer Service Provider

```ini
PROVIDER_MAILER=\Zemit\Provider\Mailer\ServiceProvider
```

### Mailer Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Mailer\ServiceProvider::class => Env::get('PROVIDER_MAILER', \Zemit\Provider\Mailer\ServiceProvider::class),
    ],
    'mailer' => [
        'driver' => Env::get('MAILER_DRIVER', 'sendmail'),
        'drivers' => [
            'mail' => [
                'driver' => 'mail',
            ],
            'sendmail' => [
                'driver' => 'sendmail',
                'sendmail' => Env::get('MAILER_SENDMAIL', '/usr/sbin/sendmail -bs'),
            ],
            'smtp' => [
                'driver' => 'smtp',
                'host' => Env::get('MAILER_SMTP_HOST', 'localhost'),
                'port' => Env::get('MAILER_SMTP_PORT', 25),
                'encryption' => Env::get('MAILER_SMTP_ENCRYPTION', ''),
                'username' => Env::get('MAILER_SMTP_USERNAME', ''),
                'password' => Env::get('MAILER_SMTP_PASSWORD', ''),
            ],
        ],
        'default' => [
            'charset' => Env::get('MAILER_CHARSET', 'utf-8'),
            'viewsDir' => Env::get('MAILER_VIEWS_DIR', APP_PATH . '/Modules/Frontend/Views/'),
            'baseUri' => Env::get('MAILER_BASE_URI', null),
        ],
        'from' => [
            'email' => Env::get('MAILER_FROM_EMAIL', 'no-reply@localhost'),
            'name' => Env::get('MAILER_FROM_NAME', 'Phalcon Kit'),
        ],
        'to' => [...explode(',', Env::get('MAILER_TO_EMAIL', ''))],
        'cc' => [...explode(',', Env::get('MAILER_CC_EMAIL', ''))],
        'bcc' => [...explode(',', Env::get('MAILER_BCC_EMAIL', ''))],
    ],
]);
```

## Mailer Service (`mailer`)

!!! info "Mailer Service Provider"
    Mailer Service Provider (`mailer`):
    [`\Zemit\Provider\Mailer\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Mailer/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$mailer = $this->mailer;

// Retrieving the service from the DI
$mailer = $this->di->get('mailer');

// Retrieving the service from the getDI()
$mailer = $this->getDI()->get('mailer');

// Retrieving the service from anywhere
$mailer = Di::getDefault()->get('mailer');
```
