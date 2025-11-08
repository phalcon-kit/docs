# Php Service

## Configurations

### Php Configurations

```ini
PHP_LOCALE_CATEGORY=6
PHP_LOCALE_REST=fr_CA.UTF-8,French_Canada.1252
PHP_DATE_TIMEZONE=America/Montreal
PHP_INI_ZEND_EXCEPTION_IGNORE_ARGS=On
```

### Php Service Provider

```ini
PROVIDER_PHP=\PhalconKit\Provider\Php\ServiceProvider
```

### Php Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Php\ServiceProvider::class => Env::get('PROVIDER_PHP', \PhalconKit\Provider\Php\ServiceProvider::class),
    ],
    'php' => [
        'locale' => [
            'category' => Env::get('PHP_LOCALE_CATEGORY', LC_ALL),
            'rest' => explode(',', Env::get('PHP_LOCALE_REST', 'fr_CA.UTF-8,French_Canada.1252')),
        ],
        'date' => [
            'timezone' => Env::get('PHP_DATE_TIMEZONE', 'America/Montreal'),
        ],
        'ini' => [
            'zend.exception_ignore_args' => Env::get('PHP_INI_ZEND_EXCEPTION_IGNORE_ARGS', 'On'),
        ],
    ],
]);
```

## Php Service (`php`)

!!! info "Php Service Provider"
    Php Service Provider (`php`):
    [`\PhalconKit\Provider\Php\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Php/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$php = $this->php;

// Retrieving the service from the DI
$php = $this->di->get('php');

// Retrieving the service from the getDI()
$php = $this->getDI()->get('php');

// Retrieving the service from anywhere
$php = Di::getDefault()->get('php');
```
