# Logger Service

The `logger` service uses the [Phalcon Logger Component](https://docs.phalcon.io/latest/logger/){:target="_blank"}

## Configurations

```ini
LOGGER_ENABLE=false

LOGGER_DRIVER_NOOP=\Phalcon\Logger\Adapter\Noop
LOGGER_DRIVER_STREAM=\Phalcon\Logger\Adapter\Stream
LOGGER_DRIVER_SYSLOG=\Phalcon\Logger\Adapter\Syslog

LOGGER_FORMATTER_JSON=\Phalcon\Logger\Formatter\Json
LOGGER_FORMATTER_LINE=\Phalcon\Logger\Formatter\Line

LOGGER_DRIVER=stream

LOGGER_FORMATTER=line
LOGGER_FORMAT="[%date%][%type%] %message%"
LOGGER_DATE="Y-m-d H:i:s"

LOGGER_PATH=./storage/log/
LOGGER_FILENAME=default
```

### Logger Service Provider

```ini
PROVIDER_LOGGER=\PhalconKit\Provider\Logger\ServiceProvider
```

### Logger Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Logger\ServiceProvider::class => Env::get('PROVIDER_LOGGER', \PhalconKit\Provider\Logger\ServiceProvider::class),
    ],
    'logger' => [
        'enable' => Env::get('LOGGER_ENABLE', Env::get('LOGGER', false)),
        
        'drivers' => [
            'noop' => Env::get('LOGGER_DRIVER_NOOP', \Phalcon\Logger\Adapter\Noop::class),
            'stream' => Env::get('LOGGER_DRIVER_STREAM', \Phalcon\Logger\Adapter\Stream::class),
            'syslog' => Env::get('LOGGER_DRIVER_SYSLOG', \Phalcon\Logger\Adapter\Syslog::class),
        ],
        'formatters' => [
            'json' => Env::get('LOGGER_FORMATTER_JSON', \Phalcon\Logger\Formatter\Json::class),
            'line' => Env::get('LOGGER_FORMATTER_LINE', \Phalcon\Logger\Formatter\Line::class),
        ],
        'default' => [
            'driver' => Env::get('LOGGER_DRIVER', 'stream'),
            'formatter' => Env::get('LOGGER_FORMATTER', 'line'),
            'format' => Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%'),
            'date' => Env::get('LOGGER_DATE', 'Y-m-d H:i:s'),
            'path' => Env::get('LOGGER_PATH', STORAGE_PATH . '/log/'),
            'filename' => Env::get('LOGGER_FILENAME', 'default'),
        ],
    ],
]);
```

## Logger Service (`logger`)

!!! info "Logger Service Provider"
    Logger Service Provider (`logger`):
    [`\PhalconKit\Provider\Logger\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Logger/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$logger = $this->logger;

// Retrieving the service from the DI
$logger = $this->di->get('logger');

// Retrieving the service from the getDI()
$logger = $this->getDI()->get('logger');

// Retrieving the service from anywhere
$logger = Di::getDefault()->get('logger');
```
