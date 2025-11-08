# Dispatcher Service

## Configuration



### Changing the Dispatcher Service Provider

```ini
PROVIDER_DISPATCHER=\Zemit\Provider\Dispatcher\ServiceProvider
```

## Dispatcher Service (`dispatcher`)

!!! info "Dispatcher Service Provider"
    Dispatcher Service Provider (`dispatcher`):
    [`\Zemit\Provider\Dispatcher\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Dispatcher/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$dispatcher = $this->dispatcher;

// Retrieving the service from the DI
$dispatcher = $this->di->get('dispatcher');

// Retrieving the service from the getDI()
$dispatcher = $this->getDI()->get('dispatcher');

// Retrieving the service from anywhere
$dispatcher = Di::getDefault()->get('dispatcher');
```
