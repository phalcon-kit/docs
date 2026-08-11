
Registers the IMAP mailbox service.

Mailbox options are read from `imap` config and passed to
`PhpImap\Mailbox`. The service centralizes mailbox path, login credentials,
attachment directory, encoding, and attachment filename behavior for mail
ingestion workflows.

***

* Full name: `\PhalconKit\Provider\Imap\ServiceProvider`
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

Register the shared `imap` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

Runtime options may be supplied for tests or specialized bootstraps. Empty
defaults are preserved so the service can still be constructed in
environments where IMAP is configured later by the application.

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
