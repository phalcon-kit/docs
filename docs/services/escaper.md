# Escaper Service

The `escaper` service uses the [Phalcon Escaper Component](https://docs.phalcon.io/latest/html-escaper/){:target="_blank"}

## Configurations

```ini
# no ini configuration available yet
```

### Escaper Service Provider

```ini
PROVIDER_ESCAPER=\Zemit\Provider\Escaper\ServiceProvider
```

### Escaper Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Escaper\ServiceProvider::class => Env::get('PROVIDER_ESCAPER', \Zemit\Provider\Escaper\ServiceProvider::class),
    ],
    'escapers' => [
        // add your own escapers here
    ],
]);
```

## Escaper Service (`escaper`)

!!! info "Escaper Service Provider"
    Escaper Service Provider (`escaper`):
    [`\Zemit\Provider\Escaper\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Escaper/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$escaper = $this->escaper;

// Retrieving the service from the DI
$escaper = $this->di->get('escaper');

// Retrieving the service from the getDI()
$escaper = $this->getDI()->get('escaper');

// Retrieving the service from anywhere
$escaper = Di::getDefault()->get('escaper');
```
