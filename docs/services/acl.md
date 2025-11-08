# Acl Service

## Configurations

### Acl Configurations

```ini
```

### Acl Service Provider

```ini
PROVIDER_ACL=\Zemit\Provider\Acl\ServiceProvider
```

### Acl Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Acl\ServiceProvider::class => Env::get('PROVIDER_ACL', \Zemit\Provider\Acl\ServiceProvider::class),
    ],
    'acl' => [
    ],
    'permissions' => [
    ],
]);
```

## Acl Service (`acl`)

!!! info "Acl Service Provider"
    Acl Service Provider (`acl`):
    [`\Zemit\Provider\Acl\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Acl/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$acl = $this->acl;

// Retrieving the service from the DI
$acl = $this->di->get('acl');

// Retrieving the service from the getDI()
$acl = $this->getDI()->get('acl');

// Retrieving the service from anywhere
$acl = Di::getDefault()->get('acl');
```
