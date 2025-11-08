# Translate Service

## Configurations

### Translate Configurations

```ini
TRANSLATE_LOCALE=en_CA.UTF-8,fr_CA.UTF-8
TRANSLATE_DEFAULT_DOMAIN=messages
TRANSLATE_CATEGORY=5
TRANSLATE_DEFAULT_PATH=./resources/translations/
```

### Translate Service Provider

```ini
PROVIDER_TRANSLATE=\PhalconKit\Provider\Translate\ServiceProvider
```

### Translate Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Translate\ServiceProvider::class => Env::get('PROVIDER_TRANSLATE', \PhalconKit\Provider\Translate\ServiceProvider::class),
    ],
    'translate' => [
        'locale' => explode(',', Env::get('TRANSLATE_LOCALE', 'en_CA.UTF-8')),
        'defaultDomain' => Env::get('TRANSLATE_DEFAULT_DOMAIN', 'messages'),
        'category' => Env::get('TRANSLATE_CATEGORY', defined('LC_MESSAGES')? LC_MESSAGES : 5),
        'directory' => Env::get('TRANSLATE_DEFAULT_PATH', RESOURCES_PATH . 'translations'),
    ],
]);
```

## Translate Service (`translate`)

!!! info "Translate Service Provider"
    Translate Service Provider (`translate`):
    [`\PhalconKit\Provider\Translate\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Translate/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$translate = $this->translate;

// Retrieving the service from the DI
$translate = $this->di->get('translate');

// Retrieving the service from the getDI()
$translate = $this->getDI()->get('translate');

// Retrieving the service from anywhere
$translate = Di::getDefault()->get('translate');
```
