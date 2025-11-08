# Url Service

## Configurations

### Url Configurations

```ini
URL_STATIC_BASE_URI=
URL_BASE_URI=/
URL_BASE_PATH=/
```

### Url Service Provider

```ini
PROVIDER_URL=\Zemit\Provider\Url\ServiceProvider
```

### Url Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Url\ServiceProvider::class => Env::get('PROVIDER_URL', \Zemit\Provider\Url\ServiceProvider::class),
    ],
    'url' => [
        'staticBaseUri' => Env::get('URL_STATIC_BASE_URI', null),
        'baseUri' => Env::get('URL_BASE_URI', '/'),
        'basePath' => Env::get('URL_BASE_PATH', '/'),
    ],
]);
```

## Url Service (`url`)

!!! info "Url Service Provider"
    Url Service Provider (`url`):
    [`\Zemit\Provider\Url\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Url/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$url = $this->url;

// Retrieving the service from the DI
$url = $this->di->get('url');

// Retrieving the service from the getDI()
$url = $this->getDI()->get('url');

// Retrieving the service from anywhere
$url = Di::getDefault()->get('url');
```
