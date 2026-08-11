
Registers the session manager service.

Session configuration is resolved from `session.driver`,
`session.default`, `session.drivers`, and optional `session.ini` values. The
default driver is Phalcon's stream adapter with a temporary-directory save
path, which keeps legacy MVC applications session-capable without extra
configuration.

This provider intentionally starts the session before returning it. Identity
flows that need stateless JWT-only behavior should use `identity.stateless`
so flash messages, OAuth2 state, locale persistence, and other PHP-session
consumers can keep working normally.

***

* Full name: `\PhalconKit\Provider\Session\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

**See Also:**

* https://docs.phalcon.io/5.18/session/

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

Register the shared `session` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

Adapter classes using Phalcon's stream/noop constructor are instantiated
directly. Other adapters are created with a storage adapter factory and
must implement `SessionHandlerInterface` before being attached to the
manager.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

**Throws:**

When a factory-backed adapter does not
implement PHP's session handler interface.
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
