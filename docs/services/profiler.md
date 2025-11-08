# Profiler Service

The `profiler` service uses the [Phalcon Profiler Component](https://docs.phalcon.io/latest/db-layer/?h=profiler){:target="_blank"}

## Configurations

```ini
# no ini configuration available yet
```

### Profiler Service Provider

```ini
PROVIDER_PROFILER=\Zemit\Provider\Profiler\ServiceProvider
```

### Profiler Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Profiler\ServiceProvider::class => Env::get('PROVIDER_PROFILER', \Zemit\Provider\Profiler\ServiceProvider::class),
    ],
]);
```

## Profiler Service (`profiler`)

!!! info "Profiler Service Provider"
    Profiler Service Provider (`profiler`):
    [`\Zemit\Provider\Profiler\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Profiler/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$profiler = $this->profiler;

// Retrieving the service from the DI
$profiler = $this->di->get('profiler');

// Retrieving the service from the getDI()
$profiler = $this->getDI()->get('profiler');

// Retrieving the service from anywhere
$profiler = Di::getDefault()->get('profiler');
```
