# Tag Service

The `tag` service uses the [Phalcon Tag Component](https://docs.phalcon.io/latest/api/phalcon_tag){:target="_blank"}

## Configurations

```ini
# no ini configuration available yet
```

### Tag Service Provider

```ini
PROVIDER_TAG=\PhalconKit\Provider\Tag\ServiceProvider
```

### Tag Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Tag\ServiceProvider::class => Env::get('PROVIDER_TAG', \PhalconKit\Provider\Tag\ServiceProvider::class),
    ],
]);
```

## Tag Service (`tag`)

!!! info "Tag Service Provider"
    Tag Service Provider (`tag`):
    [`\PhalconKit\Provider\Tag\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Tag/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$tag = $this->tag;

// Retrieving the service from the DI
$tag = $this->di->get('tag');

// Retrieving the service from the getDI()
$tag = $this->getDI()->get('tag');

// Retrieving the service from anywhere
$tag = Di::getDefault()->get('tag');
```
