# Request Service

## Configuration



### Changing the Request Service Provider

```ini
PROVIDER_REQUEST=\Zemit\Provider\Request\ServiceProvider
```

## Request Service (`request`)

!!! info "Request Service Provider"
    Request Service Provider (`request`):
    [`\Zemit\Provider\Request\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Request/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$request = $this->request;

// Retrieving the service from the DI
$request = $this->di->get('request');

// Retrieving the service from the getDI()
$request = $this->getDI()->get('request');

// Retrieving the service from anywhere
$request = Di::getDefault()->get('request');
```
