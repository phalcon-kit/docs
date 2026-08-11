
Registers the mode-specific router service.

Router creation follows the active bootstrap mode. MVC receives the
config-aware PhalconKit MVC router, CLI receives the CLI router, and
WebSocket receives the WebSocket router that inherits CLI-style route
matching. All variants implement the shared PhalconKit router contract so
downstream code can use typed DI lookups without branching on the runtime
mode.

***

* Full name: `\PhalconKit\Provider\Router\ServiceProvider`
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

Register the shared `router` service and apply configured defaults.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

The provider respects an already-created bootstrap router when one exists,
otherwise it creates the router for the current mode. MVC routers receive
the events manager, config service, base routes, hostname routes, and
registered application module routes; CLI and WebSocket routers only need
their configured defaults and DI reference.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

**Throws:**

When the bootstrap mode is not supported by
the router provider.
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
