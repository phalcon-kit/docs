
Registers the debug helper service.

Debug mode is enabled when either `app.debug` or `debug.enable` is truthy.
When enabled in MVC mode, the provider attaches Phalcon's debug listener and
applies display options from the `debug` config section. CLI and WebSocket
modes still receive a debug service instance, but do not attach the MVC debug
listener.

***

* Full name: `\PhalconKit\Provider\Debug\ServiceProvider`
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

Register the shared `debug` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

The provider also toggles PHP debug display behavior through
`PhalconKit\Support\Php::debug()`, keeping PHP runtime debug flags aligned
with the framework debug service.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

***

### causeCyclicError

Detect an old Phalcon/PHP combination that cannot safely attach debug.

```php
public causeCyclicError(): bool
```

Phalcon versions before 5 can trigger cyclic debug errors on PHP 8+. The
provider keeps the guard isolated so tests can assert the compatibility
decision and future Phalcon upgrades can remove or revise it cleanly.

**Return Value:**

True when the runtime should skip debug listener attachment.

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
