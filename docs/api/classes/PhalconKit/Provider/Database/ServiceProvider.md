
Registers a configured PDO database connection.

The provider resolves the active driver from `database.default` or from a
subclass-specific `$driverName`. Driver definitions can extend one or more
other driver definitions through `extends`, allowing applications to keep
shared connection options in one place and override only the values that
differ per connection.

Core database logger and profiler listeners are attached to the shared events
manager before the connection is returned.

***

* Full name: `\PhalconKit\Provider\Database\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

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

### attachedEvents

Tracks whether database listeners were attached during this PHP process.

```php
protected static bool $attachedEvents
```

* This property is **static**.

***

## Methods

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
