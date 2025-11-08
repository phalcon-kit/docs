# Filter Service

The `filter` service uses the [Phalcon Filter Component](https://docs.phalcon.io/latest/filter-filter/){:target="_blank"}

## Configurations

```ini
# no ini configuration available yet
```

### Filter Service Provider

```ini
PROVIDER_FILTER=\Zemit\Provider\Filter\ServiceProvider
```

### Filter Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Filter\ServiceProvider::class => Env::get('PROVIDER_FILTER', \Zemit\Provider\Filter\ServiceProvider::class),
    ],
    'filters' => [
        // add your own filters here
    ],
]);
```

## Filter Service (`filter`)

!!! info "Filter Service Provider"
    Filter Service Provider (`filter`):
    [`\Zemit\Provider\Filter\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Filter/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$filter = $this->filter;

// Retrieving the service from the DI
$filter = $this->di->get('filter');

// Retrieving the service from the getDI()
$filter = $this->getDI()->get('filter');

// Retrieving the service from anywhere
$filter = Di::getDefault()->get('filter');
```
