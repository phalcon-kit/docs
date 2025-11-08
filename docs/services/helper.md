# Helper Service

The `helper` service uses the [Phalcon Helper Component](https://docs.phalcon.io/latest/support-helper){:target="_blank"}

## Configurations

```ini
# no ini configuration available yet
```

### Helper Service Provider

```ini
PROVIDER_HELPER=\PhalconKit\Provider\Helper\ServiceProvider
```

### Helper Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Helper\ServiceProvider::class => Env::get('PROVIDER_HELPER', \PhalconKit\Provider\Helper\ServiceProvider::class),
    ],
    'helpers' => [
        // add your own helpers here
    ],
]);
```

## Helper Service (`helper`)

!!! info "Helper Service Provider"
    Helper Service Provider (`helper`):
    [`\PhalconKit\Provider\Helper\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Helper/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$helper = $this->helper;

// Retrieving the service from the DI
$helper = $this->di->get('helper');

// Retrieving the service from the getDI()
$helper = $this->getDI()->get('helper');

// Retrieving the service from anywhere
$helper = Di::getDefault()->get('helper');
```
