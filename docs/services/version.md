# Version Service

## Configurations

```ini
APP_VERSION=1.0.0
```

### Version Service Provider

```ini
PROVIDER_VERSION=\PhalconKit\Provider\Version\ServiceProvider
```

### Version Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Version\ServiceProvider::class => Env::get('PROVIDER_VERSION', \PhalconKit\Provider\Version\ServiceProvider::class),
    ],
]);
```

## Version Service (`version`)

!!! info "Version Service Provider"
    Version Service Provider (`version`):
    [`\PhalconKit\Provider\Version\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Version/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$version = $this->version;

// Retrieving the service from the DI
$version = $this->di->get('version');

// Retrieving the service from the getDI()
$version = $this->getDI()->get('version');

// Retrieving the service from anywhere
$version = Di::getDefault()->get('version');
```
