# Flash Service

The `flash` service uses the [Phalcon Flash Component](https://docs.phalcon.io/latest/html-flash/){:target="_blank"}

## Configurations

```ini
FLASH_DRIVER=direct
FLASH_DRIVER_DIRECT=\Phalcon\Flash\Direct
FLASH_DRIVER_SESSION=\Phalcon\Flash\Session

FLASH_AUTOMATIC_HTML=true
FLASH_AUTO_ESCAPE=false
FLASH_IMPLICIT_FLUSH=true

# CSS Classes
FLASH_CSS_CLASS_ERROR=
FLASH_CSS_CLASS_SUCCESS=
FLASH_CSS_CLASS_NOTICE=
FLASH_CSS_CLASS_WARNING=

# Icons Classes
FLASH_CSS_ICON_CLASS_ERROR=
FLASH_CSS_ICON_CLASS_SUCCESS=
FLASH_CSS_ICON_CLASS_NOTICE=
FLASH_CSS_ICON_CLASS_WARNING=
```

### Flash Service Provider

```ini
PROVIDER_FLASH=\PhalconKit\Provider\Flash\ServiceProvider
```

### Flash Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Flash\ServiceProvider::class => Env::get('PROVIDER_FLASH', \PhalconKit\Provider\Flash\ServiceProvider::class),
    ],
    'flash' => [
        'driver' => Env::get('FLASH_DRIVER', 'direct'),
        'drivers' => [
            'direct' => Env::get('FLASH_DRIVER_DIRECT', \Phalcon\Flash\Direct::class),
            'session' => Env::get('FLASH_DRIVER_SESSION', \Phalcon\Flash\Session::class),
        ],
        'automaticHtml' => Env::get('FLASH_AUTOMATIC_HTML', true),
        'autoEscape' => Env::get('FLASH_AUTO_ESCAPE', false),
        'implicitFlush' => Env::get('FLASH_IMPLICIT_FLUSH', true),
        'cssClasses' => [
            'error' => Env::get('FLASH_CSS_CLASS_ERROR', 'alert alert-danger fade in'),
            'success' => Env::get('FLASH_CSS_CLASS_SUCCESS', 'alert alert-success fade in'),
            'notice' => Env::get('FLASH_CSS_CLASS_NOTICE', 'alert alert-info fade in'),
            'warning' => Env::get('FLASH_CSS_CLASS_WARNING', 'alert alert-warning fade in'),
        ],
        'cssIconsClasses' => [
            'error' => Env::get('FLASH_CSS_ICON_CLASS_ERROR'),
            'success' => Env::get('FLASH_CSS_ICON_CLASS_SUCCESS'),
            'notice' => Env::get('FLASH_CSS_ICON_CLASS_NOTICE'),
            'warning' => Env::get('FLASH_CSS_ICON_CLASS_WARNING'),
        ],
    ],
]);
```

## Flash Service (`flash`)

!!! info "Flash Service Provider"
    Flash Service Provider (`flash`):
    [`\PhalconKit\Provider\Flash\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Flash/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$flash = $this->flash;

// Retrieving the service from the DI
$flash = $this->di->get('flash');

// Retrieving the service from the getDI()
$flash = $this->getDI()->get('flash');

// Retrieving the service from anywhere
$flash = Di::getDefault()->get('flash');
```
