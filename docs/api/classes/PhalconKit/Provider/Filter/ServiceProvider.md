
Registers the PhalconKit filter locator.

The provider starts from the package filter factory so the core sanitizer and
validator services are available, then applies any configured application
filters from `filters`. Applications can use that config path to add or
replace named filter services without replacing the provider itself.

***

* Full name: `\PhalconKit\Provider\Filter\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

**See Also:**

* https://docs.phalcon.io/5.18/filter/

## Properties

### serviceName

DI service name for the shared filter locator.

```php
protected string $serviceName
```

***

## Methods

### register

Register the configured filter locator.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

**Parameters:**

| Parameter | Type                           | Description                                                              |
|-----------|--------------------------------|--------------------------------------------------------------------------|
| `$di`     | **\PhalconKit\Di\DiInterface** | PhalconKit container used to read configured
filter service definitions. |

**Throws:**

When the factory does not return the expected
PhalconKit filter implementation.
- [`ServiceException`](../../Exception/ServiceException.md)

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
