# View Service

The `view` service uses the [Phalcon View Component](https://docs.phalcon.io/latest/views/){:target="_blank"}

## Configurations

```ini
VIEW_MINIFY=false
```

### View Service Provider

```ini
PROVIDER_VIEW=\PhalconKit\Provider\View\ServiceProvider
```

### View Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\View\ServiceProvider::class => Env::get('PROVIDER_VIEW', \PhalconKit\Provider\View\ServiceProvider::class),
    ],
    'view' => [
        'minify' => Env::get('VIEW_MINIFY', false),
        'engines' => Env::get('VIEW_ENGINES', [
            '.phtml' => \Phalcon\Mvc\View\Engine\Php::class,
            '.volt' => \Phalcon\Mvc\View\Engine\Volt::class,
//            '.mhtml' => \Phalcon\Mvc\View\Engine\Mustache::class,
//            '.twig' => \Phalcon\Mvc\View\Engine\Twig::class,
//            '.tpl' => \Phalcon\Mvc\View\Engine\Smarty::class
        ]),
    ],
]);
```

## View Service (`view`)

!!! info "View Service Provider"
    View Service Provider (`view`):
    [`\PhalconKit\Provider\View\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/View/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$view = $this->view;

// Retrieving the service from the DI
$view = $this->di->get('view');

// Retrieving the service from the getDI()
$view = $this->getDI()->get('view');

// Retrieving the service from anywhere
$view = Di::getDefault()->get('view');
```
