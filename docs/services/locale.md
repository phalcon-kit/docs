# Locale Service

## Configurations

### Locale Configurations

```ini
LOCALE_DEFAULT=en
LOCALE_ALLOWED=en,fr
LOCALE_SESSION_KEY=phalcon-kit-locale
LOCALE_MODE=default
```

### Locale Service Provider

```ini
PROVIDER_LOCALE=\PhalconKit\Provider\Locale\ServiceProvider
```

### Locale Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Locale\ServiceProvider::class => Env::get('PROVIDER_LOCALE', \PhalconKit\Provider\Locale\ServiceProvider::class),
    ],
    'locale' => [
        'default' => Env::get('LOCALE_DEFAULT', 'en'),
        'allowed' => explode(',', Env::get('LOCALE_ALLOWED', 'en')),
        'sessionKey' => Env::get('LOCALE_SESSION_KEY', 'phalcon-kit-locale'),
        'mode' => Env::get('LOCALE_MODE', Locale::MODE_DEFAULT),
    ],
]);
```

## Locale Service (`locale`)

!!! info "Locale Service Provider"
    Locale Service Provider (`locale`):
    [`\PhalconKit\Provider\Locale\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Locale/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$locale = $this->locale;

// Retrieving the service from the DI
$locale = $this->di->get('locale');

// Retrieving the service from the getDI()
$locale = $this->getDI()->get('locale');

// Retrieving the service from anywhere
$locale = Di::getDefault()->get('locale');
```
