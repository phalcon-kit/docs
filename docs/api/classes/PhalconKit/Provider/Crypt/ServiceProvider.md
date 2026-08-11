
Registers the encryption service.

The provider validates cipher, signing, padding, and key configuration before
returning Phalcon's `Crypt` service. It defaults to AES-256-GCM and requires
a key of at least 32 bytes, either from `crypt.key` or `APP_CRYPT_KEY`.

AEAD ciphers such as GCM/CCM authenticate internally and must not also enable
Phalcon's signing path. Stream modes are rejected with signing enabled
because Phalcon's HMAC signing path is not compatible with those modes.

***

* Full name: `\PhalconKit\Provider\Crypt\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

**See Also:**

* https://docs.phalcon.io/latest/encryption-crypt/

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

Register the shared `crypt` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

Runtime arguments can override cipher and signing for a specific
resolution, but all other options are read from `crypt` config. Invalid
cryptographic configuration fails during service resolution so the
application does not start with unsafe encryption settings.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

**Throws:**

When the pad factory, encryption key,
cipher, or signing mode is invalid.
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
