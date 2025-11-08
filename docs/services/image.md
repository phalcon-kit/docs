# Image Service

The `image` service uses the [Phalcon Image Component](https://docs.phalcon.io/latest/image){:target="_blank"}

## Configurations

```ini
# no ini configuration available yet
```

### Image Service Provider

```ini
PROVIDER_IMAGE=\Zemit\Provider\Image\ServiceProvider
```

### Image Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Image\ServiceProvider::class => Env::get('PROVIDER_IMAGE', \Zemit\Provider\Image\ServiceProvider::class),
    ],
]);
```

## Image Service (`image`)

!!! info "Image Service Provider"
    Image Service Provider (`image`):
    [`\Zemit\Provider\Image\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Image/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$image = $this->image;

// Retrieving the service from the DI
$image = $this->di->get('image');

// Retrieving the service from the getDI()
$image = $this->getDI()->get('image');

// Retrieving the service from anywhere
$image = Di::getDefault()->get('image');
```
