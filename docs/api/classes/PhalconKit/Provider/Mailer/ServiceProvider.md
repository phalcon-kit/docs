
Registers the mailer manager service.

Mailer configuration is resolved from `mailer.driver`, `mailer.default`,
and `mailer.drivers.<driver>`. Driver options are merged over defaults before
constructing Phalcon Incubator's mailer manager, then the DI container and
shared events manager are attached when available.

***

* Full name: `\PhalconKit\Provider\Mailer\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

## Constants

| Constant            | Visibility | Type  | Value                                                                                                       |
|---------------------|------------|-------|-------------------------------------------------------------------------------------------------------------|
| `SUPPORTED_DRIVERS` | private    | array | ['sendmail', 'smtp']                                                                                        |
| `SMTP_ENCRYPTIONS`  | private    | array | ['', \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_SMTPS, \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS] |

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

Register the shared `mailer` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

SMTP encryption is normalized case-insensitively and validated before the
mailer is created so bad config fails before network I/O. The SMTP driver
also enables PHPMailer authentication explicitly because SMTP credentials
in the merged options imply authenticated transport.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

**Throws:**

When the selected driver, option shape, or
SMTP encryption value is invalid.
- [`ConfigurationException`](../../Exception/ConfigurationException.md)

***

### normalizeOptions

Normalize and validate the options passed to the incubator mailer.

```php
private static normalizeOptions(array $options, string $driver): array
```

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **array**  |             |
| `$driver`  | **string** |             |

**Throws:**

When SMTP encryption is unsupported.
- [`ConfigurationException`](../../Exception/ConfigurationException.md)

***

### resolveDefaultOptions

Return validated defaults from the canonical key or legacy alias.

```php
private static resolveDefaultOptions(array $mailerConfig): array
```

* This method is **static**.
**Parameters:**

| Parameter       | Type      | Description |
|-----------------|-----------|-------------|
| `$mailerConfig` | **array** |             |

***

### normalizeDrivers

Normalize and validate driver option groups keyed by driver name.

```php
private static normalizeDrivers(mixed $drivers): array<string,array>
```

* This method is **static**.
**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$drivers` | **mixed** |             |

***

### normalizeOptionArray

Validate a mailer option group.

```php
private static normalizeOptionArray(mixed $options, string $path): array
```

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **mixed**  |             |
| `$path`    | **string** |             |

***

### assertSupportedDriver

Validate the selected driver against the providers this class can create.

```php
private static assertSupportedDriver(string $driver): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$driver` | **string** |             |

***

### normalizeMailerToken

Normalize ASCII mailer config tokens such as driver and encryption names.

```php
private static normalizeMailerToken(mixed $value, string $path): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$value`  | **mixed**  |             |
| `$path`   | **string** |             |

***

### normalizeOptionalMailerToken

Normalize optional mailer config tokens that may intentionally be empty.

```php
private static normalizeOptionalMailerToken(string $value): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$value`  | **string** |             |

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
