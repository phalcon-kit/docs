# Volt Service

The `volt` service uses the [Phalcon Volt Template Engine](https://docs.phalcon.io/latest/volt/){:target="_blank"}

## Configurations

```ini
VOLT_AUTOESCAPE=false
VOLT_ALWAYS=false
VOLT_EXTENSION=.php
VOLT_SEPARATOR=%%
VOLT_PATH=./
VOLT_PREFIX=
VOLT_STAT=
```

### Volt Service Provider

```ini
PROVIDER_VOLT=\PhalconKit\Provider\Volt\ServiceProvider
```

### Volt Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Volt\ServiceProvider::class => Env::get('PROVIDER_VOLT', \PhalconKit\Provider\Volt\ServiceProvider::class),
    ],
   'volt' => [
        'autoescape' => Env::get('VOLT_AUTOESCAPE', false),
        'always' => Env::get('VOLT_ALWAYS', false),
        'extension' => Env::get('VOLT_EXTENSION', '.php'),
        'separator' => Env::get('VOLT_SEPARATOR', '%%'),
        'path' => Env::get('VOLT_PATH', './'),
        'prefix' => Env::get('VOLT_PREFIX', null),
        'stat' => Env::get('VOLT_STAT', true),
    ],
]);
```

## Volt Service (`volt`)

!!! info "Volt Service Provider"
    Volt Service Provider (`volt`):
    [`\PhalconKit\Provider\Volt\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Volt/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$volt = $this->volt;

// Retrieving the service from the DI
$volt = $this->di->get('volt');

// Retrieving the service from the getDI()
$volt = $this->getDI()->get('volt');

// Retrieving the service from anywhere
$volt = Di::getDefault()->get('volt');
```
