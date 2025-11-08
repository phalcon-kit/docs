# Utils Service


## Configurations

```ini
# no ini configuration available yet
```

### Utils Service Provider

```ini
PROVIDER_UTILS=\PhalconKit\Provider\Utils\ServiceProvider
```

### Utils Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Utils\ServiceProvider::class => Env::get('PROVIDER_UTILS', \PhalconKit\Provider\Utils\ServiceProvider::class),
    ],
]);
```

## Utils Service (`utils`)

!!! info "Utils Service Provider"
    Utils Service Provider (`utils`):
    [`\PhalconKit\Provider\Utils\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Utils/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$utils = $this->utils;

// Retrieving the service from the DI
$utils = $this->di->get('utils');

// Retrieving the service from the getDI()
$utils = $this->getDI()->get('utils');

// Retrieving the service from anywhere
$utils = Di::getDefault()->get('utils');
```
