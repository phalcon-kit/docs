# Debug Service

The `debug` service uses the [Phalcon Debug Component](https://docs.phalcon.io/latest/support-debug/){:target="_blank"}

## Configurations

```ini
DEBUG_ENABLE=false
DEBUG_EXCEPTION=true
DEBUG_LOW_SEVERITY=false
DEBUG_SHOW_FILES=true
DEBUG_SHOW_BACKTRACE=true
DEBUG_SHOW_FRAGMENT=true
DEBUG_URI=
DEBUG_BLACKLIST=
```

### Debug Service Provider

```ini
PROVIDER_DEBUG=\PhalconKit\Provider\Debug\ServiceProvider
```

### Debug Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Debug\ServiceProvider::class => Env::get('PROVIDER_DEBUG', \PhalconKit\Provider\Debug\ServiceProvider::class),
    ],
    'debug' => [
        'enable' => Env::get('DEBUG_ENABLE', false),
        'exception' => Env::get('DEBUG_EXCEPTION', true),
        'lowSeverity' => Env::get('DEBUG_LOW_SEVERITY', false),
        'showFiles' => Env::get('DEBUG_SHOW_FILES', true),
        'showBackTrace' => Env::get('DEBUG_SHOW_BACKTRACE', true),
        'showFileFragment' => Env::get('DEBUG_SHOW_FRAGMENT', true),
        'uri' => Env::get('DEBUG_URI'),
        'blacklist' => [
            'server' => array_merge(explode(' ', Env::get('DEBUG_BLACKLIST', '')), [
                'PWD',
                'PASS',
                'PASSWD',
                'PASSWORD',
                'TOKEN',
                'HASH',
                'DB_PWD',
                'DB_PASS',
                'DB_PASSWD',
                'DB_PASSWORD',
                'DATABASE_PWD',
                'DATABASE_PASS',
                'DATABASE_PASSWD',
                'DATABASE_PASSWORD',
                'SECURITY_WORK_FACTOR',
                'SECURITY_SALT',
                'PASSPHRASE',
                'SECRET',
                'API_SECRET',
                'API_KEY',
            ]),
        ],
    ],
]);
```

## Debug Service (`debug`)

!!! info "Debug Service Provider"
    Debug Service Provider (`debug`):
    [`\PhalconKit\Provider\Debug\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Debug/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$debug = $this->debug;

// Retrieving the service from the DI
$debug = $this->di->get('debug');

// Retrieving the service from the getDI()
$debug = $this->getDI()->get('debug');

// Retrieving the service from anywhere
$debug = Di::getDefault()->get('debug');
```
