# Env Service

## Configurations

### Env Service Provider

```ini
PROVIDER_ENV=\Zemit\Provider\Env\ServiceProvider
```

### Env Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Env\ServiceProvider::class => Env::get('PROVIDER_ENV', \Zemit\Provider\Env\ServiceProvider::class),
    ],
]);
```

## Env Service (`env`)

!!! info "Env Service Provider"
    Env Service Provider (`env`):
    [`\Zemit\Provider\Env\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Env/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$env = $this->env;

// Retrieving the service from the DI
$env = $this->di->get('env');

// Retrieving the service from the getDI()
$env = $this->getDI()->get('env');

// Retrieving the service from anywhere
$env = Di::getDefault()->get('env');
```
