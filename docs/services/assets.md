# Assets Manager Service

The `assets` service uses the [Phalcon Assets Manager Component](https://docs.phalcon.io/latest/assets/){:target="_blank"}

## Configurations

### Assets Service Provider

```ini
PROVIDER_ASSETS=\PhalconKit\Provider\Assets\ServiceProvider
```

### Assets Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Assets\ServiceProvider::class => Env::get('PROVIDER_ASSETS', \PhalconKit\Provider\Assets\ServiceProvider::class),
    ],
]);
```

## Assets Service (`assets`)

!!! info "Assets Service Provider"
    Assets Service Provider (`assets`):
    [`\PhalconKit\Provider\Assets\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Assets/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$assets = $this->assets;

// Retrieving the service from the DI
$assets = $this->di->get('assets');

// Retrieving the service from the getDI()
$assets = $this->getDI()->get('assets');

// Retrieving the service from anywhere
$assets = Di::getDefault()->get('assets');
```
