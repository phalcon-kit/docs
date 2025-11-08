# Lorem Ipsum Service

## Configuration

### Changing the Lorem Ipsum Service Provider

```ini
PROVIDER_LOREM_IPSUM=\Zemit\Provider\LoremIpsum\ServiceProvider
```

### LoremIpsum Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\LoremIpsum\ServiceProvider::class => Env::get('PROVIDER_LOREM_IPSUM', \Zemit\Provider\LoremIpsum\ServiceProvider::class),
    ],
]);
```

## Lorem Ipsum Service (`loremIpsum`)

!!! info "Lorem Service Provider"
    Lorem Service Provider (`loremIpsum`):
    [`\Zemit\Provider\Lorem\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/LoremIpsum/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$lorem = $this->loremIpsum;

// Retrieving the service from the DI
$lorem = $this->di->get('loremIpsum');

// Retrieving the service from the getDI()
$lorem = $this->getDI()->get('loremIpsum');

// Retrieving the service from anywhere
$lorem = Di::getDefault()->get('loremIpsum');
```
