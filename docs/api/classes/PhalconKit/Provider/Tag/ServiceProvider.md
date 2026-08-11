
Registers the PhalconKit tag helper service.

Phalcon tag helpers are static, so the provider stores the active DI
container on `PhalconKit\Tag` and returns a shared helper instance for code
that still resolves `tag` from DI. This keeps static helpers and injected
helpers pointed at the same service container.

***

* Full name: `\PhalconKit\Provider\Tag\ServiceProvider`
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

Register the shared `tag` service and bind the static tag DI.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

Applications replacing this service should keep `Tag::setDI()` behavior
or static tag helpers will not be able to resolve assets, escaper, and
other DI-backed services.

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
