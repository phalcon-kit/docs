
Registers the mode-specific dispatcher and core dispatch listeners.

The dispatcher service is selected from the active bootstrap mode: MVC
receives the HTTP dispatcher, CLI receives the task dispatcher, and WebSocket
receives the task-style WebSocket dispatcher. Shared listeners such as
preflight, ACL security, maintenance checks, logging, and module bootstrapping
are attached before the concrete dispatcher is returned.

MVC-only listeners are attached only for HTTP dispatching. CLI and WebSocket
dispatchers keep the common listeners but avoid MVC error/rest behavior that
depends on controllers and HTTP responses.

***

* Full name: `\PhalconKit\Provider\Dispatcher\ServiceProvider`
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

Register the shared `dispatcher` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

The returned dispatcher is configured with the shared events manager, the
PhalconKit DI container, and the default namespace from
`router.defaults.namespace` when that config value exists.

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
