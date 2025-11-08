# Cookies Service

## Cookies Configuration

```ini
COOKIES_USE_ENCRYPTION=true
COOKIES_SIGN_KEY=
```

### Cookies Configuration Object

```php
<?php
new Config([
    'cookies' => [
        'useEncryption' => Env::get('COOKIES_USE_ENCRYPTION', true),
        'signKey' => Env::get('COOKIES_SIGN_KEY', ''),
    ],
]);
```

## Cookies Service (`cookies`)

!!! info "Cookies Service Provider"
    Cookies Service Provider (`cookies`):
    [`\Zemit\Provider\Cookies\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Cookies/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$cookies = $this->cookies;

// Retrieving the service from the DI
$cookies = $this->di->get('cookies');

// Retrieving the service from the getDI()
$cookies = $this->getDI()->get('cookies');

// Retrieving the service from anywhere
$cookies = Di::getDefault()->get('cookies');
```
