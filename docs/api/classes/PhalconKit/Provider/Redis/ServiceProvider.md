
Registers the native Redis client service.

Connection settings come from the `redis` config section. The provider
handles connection, optional authentication, and optional database selection
before returning the client, wrapping extension failures in
`ServiceException` so framework consumers can catch a stable exception type.

***

* Full name: `\PhalconKit\Provider\Redis\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

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

### register

Register the shared Redis client service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

The provider reads the `redis` configuration path, applies conservative
connection defaults, and returns a native `Redis` instance from the DI
container. Native Redis extension failures are wrapped in
`ServiceException` so callers can catch a stable PhalconKit service
boundary instead of depending on extension-specific exception behavior.

**Parameters:**

| Parameter | Type                           | Description                                                                                                 |
|-----------|--------------------------------|-------------------------------------------------------------------------------------------------------------|
| `$di`     | **\PhalconKit\Di\DiInterface** | The PhalconKit container that supplies the config
service and receives the shared Redis service definition. |

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
