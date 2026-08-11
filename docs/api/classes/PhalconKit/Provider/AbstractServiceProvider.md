
Base implementation for PhalconKit DI service providers.

Concrete providers define a stable `$serviceName` and implement
`register(DiInterface $di)` to bind their service into the container. The
constructor stores the PhalconKit DI container and runs `configure()` so
subclasses can prepare provider-local options before registration.

***

* Full name: `\PhalconKit\Provider\AbstractServiceProvider`
* Parent class: [`\PhalconKit\Di\Injectable`](../Di/Injectable.md)
* This class implements:
  [`\PhalconKit\Provider\ServiceProviderInterface`](./ServiceProviderInterface.md)
* This class is an **Abstract class**

## Properties

### serviceName

Stable DI service name managed by this provider.

```php
protected string $serviceName
```

This value is part of the provider contract because controllers, tasks,
other injectables, and replacement providers resolve services by name.
Concrete providers must set it to a non-empty value.

***

## Methods

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
- [`LogicException`](../Exception/LogicException.md)

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
