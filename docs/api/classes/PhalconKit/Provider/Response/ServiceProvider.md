
Registers the HTTP response service.

The response service wraps Phalcon's native response with PhalconKit's HTTP
contract and applies globally configured headers from `response.headers`.
This keeps security, cache, and platform headers centralized in config
instead of scattering them across controllers.

***

* Full name: `\PhalconKit\Provider\Response\ServiceProvider`
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

Register the shared `response` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

Headers configured under `response.headers` are applied as soon as the
response is built. Applications that replace this provider should either
preserve that config behavior or document their own header strategy.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

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
