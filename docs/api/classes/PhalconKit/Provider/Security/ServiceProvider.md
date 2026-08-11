
Registers the password hashing and token security service.

PhalconKit uses its `Encryption\Security` wrapper so hashing helpers can read
framework config while preserving Phalcon's security API. Defaults favor
Argon2id with a moderate work factor; applications can override both under
`security.workFactor` and `security.hash`.

***

* Full name: `\PhalconKit\Provider\Security\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

**See Also:**

* https://docs.phalcon.io/latest/encryption-security/

## Properties

### defaultWorkFactor

Default password hashing work factor used when config does not override.

```php
public int $defaultWorkFactor
```

***

### defaultHash

Default Phalcon password hash algorithm used when config does not
override.

```php
public int $defaultHash
```

***

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

Register the shared `security` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

The service receives DI before hash defaults are applied so downstream
hashing helpers can resolve config-backed Argon options safely.

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
