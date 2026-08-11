
Registers the dynamic-model database connection service.

This provider reuses the base database provider but forces the configured
`dynamic` driver and exposes it as `dbd`. Dynamic models and generated
record controllers can use this service when their storage should be isolated
from the primary application database.

***

* Full name: `\PhalconKit\Provider\DatabaseDynamic\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\Database\ServiceProvider`](../Database/ServiceProvider.md)

## Properties

### driverName

Optional configured driver name forced by a specialized provider.

```php
protected ?string $driverName
```

Null means the provider uses `database.default`. Subclasses such as the
read-only and dynamic database providers set this value to select a named
driver while reusing the base connection-building logic.

***

### serviceName

Stable DI service name managed by this provider.

```php
protected string $serviceName
```

This value is part of the provider contract because controllers, tasks,
other injectables, and replacement providers resolve services by name.
Concrete providers must set it to a non-empty value.

***

## Inherited methods

### __construct

Stores the DI container and prepares the provider for registration.

```php
public __construct(\PhalconKit\Di\DiInterface $di): mixed
```

The constructor intentionally requires `PhalconKit\Di\DiInterface` so
providers can rely on typed service helpers during configuration and
registration.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

**Throws:**

When a concrete provider does not define a
non-empty service name.
- [`LogicException`](../../Exception/LogicException.md)

***

### getName

Returns the DI service name managed by this provider.

```php
public getName(): string
```

***

### boot

Optional post-registration hook.

```php
public boot(): void
```

The base implementation is intentionally empty. Custom bootstraps or
application code may call this method for provider-specific startup work
after all services have been registered.

***

### configure

Optional provider-local configuration hook.

```php
public configure(): void
```

This runs during construction after DI has been stored and before
`register()` is called. Use it to normalize provider options or prepare
lightweight state; service creation belongs in `register()`.

***

### register

Register the shared database service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

Supported driver options include `adapter`, `dialectClass`, connection
descriptor values accepted by the selected adapter, and control keys such
as `extends`/`enable` that are removed before adapter construction.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

**Throws:**

When driver options are invalid, adapter or
dialect classes do not exist, or the adapter does not extend Phalcon's
PDO adapter base class.
- [`ConfigurationException`](../../Exception/ConfigurationException.md)

***
