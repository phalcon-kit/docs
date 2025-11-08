# Loggers Service

## Configurations

```ini
// @todo
```

### Loggers Service Provider

```ini
PROVIDER_LOGGERS=\PhalconKit\Provider\Loggers\ServiceProvider
```

### Loggers Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Loggers\ServiceProvider::class => Env::get('PROVIDER_LOGGERS', \PhalconKit\Provider\Loggers\ServiceProvider::class),
    ],
    'loggers' => [
        'error' => [
            'enable' => Env::get('LOGGER_ERROR_ENABLE', Env::get('LOGGER_ERROR', false)),
            'driver' => Env::get('LOGGER_ERROR_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_ERROR_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_ERROR_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_ERROR_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_ERROR_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_ERROR_FILENAME', 'error.log'),
        ],
        
        'database' => [
            'enable' => Env::get('LOGGER_DATABASE_ENABLE', Env::get('LOGGER_DATABASE', false)),
            'driver' => Env::get('LOGGER_DATABASE_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_DATABASE_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_DATABASE_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_DATABASE_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_DATABASE_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_DATABASE_FILENAME', 'database.log'),
        ],
        
        'request' => [
            'enable' => Env::get('LOGGER_REQUEST_ENABLE', Env::get('LOGGER_REQUEST', false)),
            'driver' => Env::get('LOGGER_REQUEST_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_REQUEST_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_REQUEST_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_REQUEST_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_REQUEST_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_REQUEST_FILENAME', 'request.log'),
        ],
        
        'dispatcher' => [
            'enable' => Env::get('LOGGER_DISPATCHER_ENABLE', Env::get('LOGGER_DISPATCHER', false)),
            'driver' => Env::get('LOGGER_DISPATCHER_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_DISPATCHER_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_DISPATCHER_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_DISPATCHER_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_DISPATCHER_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_DISPATCHER_FILENAME', 'dispatcher.log'),
        ],
        
        'profiler' => [
            'enable' => Env::get('LOGGER_PROFILER_ENABLE', Env::get('LOGGER_PROFILER', false)),
            'driver' => Env::get('LOGGER_PROFILER_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_PROFILER_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_PROFILER_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_PROFILER_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_PROFILER_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_PROFILER_FILENAME', 'profiler.log'),
        ],
        
        'mailer' => [
            'enable' => Env::get('LOGGER_MAILER_ENABLE', Env::get('LOGGER_MAILER', false)),
            'driver' => Env::get('LOGGER_MAILER_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_MAILER_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_MAILER_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_MAILER_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_MAILER_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_MAILER_FILENAME', 'mailer.log'),
        ],
        
        'cron' => [
            'enable' => Env::get('LOGGER_CRON_ENABLE', Env::get('LOGGER_CRON', false)),
            'driver' => Env::get('LOGGER_CRON_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_CRON_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_CRON_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_CRON_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_CRON_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_CRON_FILENAME', 'cron.log'),
        ],
        
        'auth' => [
            'enable' => Env::get('LOGGER_AUTH_ENABLE', Env::get('LOGGER_AUTH', false)),
            'driver' => Env::get('LOGGER_AUTH_DRIVER', Env::get('LOGGER_DRIVER', 'stream')),
            'formatter' => Env::get('LOGGER_AUTH_FORMATTER', Env::get('LOGGER_FORMATTER', 'line')),
            'format' => Env::get('LOGGER_AUTH_FORMAT', Env::get('LOGGER_FORMAT', '[%date%][%type%] %message%')),
            'date' => Env::get('LOGGER_AUTH_DATE', Env::get('LOGGER_DATE', 'Y-m-d H:i:s')),
            'path' => Env::get('LOGGER_AUTH_PATH', Env::get('LOGGER_PATH', STORAGE_PATH . '/log/')),
            'filename' => Env::get('LOGGER_AUTH_FILENAME', 'auth.log'),
        ],
    ],
]);
```

## Loggers Service (`loggers`)

!!! info "Loggers Service Provider"
    Loggers Service Provider (`loggers`):
    [`\PhalconKit\Provider\Loggers\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Loggers/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$loggers = $this->loggers;

// Retrieving the service from the DI
$loggers = $this->di->get('loggers');

// Retrieving the service from the getDI()
$loggers = $this->getDI()->get('loggers');

// Retrieving the service from anywhere
$loggers = Di::getDefault()->get('loggers');
```
