
Shared typed service resolver for static helpers and native Phalcon bridges.

Normal PhalconKit code should prefer calling `$di->getTyped()` or
`$di->getConfig()` directly. This resolver exists for places that do not own
a typed `DiInterface` property yet, such as static helper APIs, native
Phalcon extension points, or compatibility code that receives a native
`Phalcon\Di\DiInterface` and needs to enforce the PhalconKit container
boundary before resolving a service.

***

* Full name: `\PhalconKit\Di\ServiceResolver`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Methods

### __construct

```php
private __construct(): mixed
```

***

### requirePhalconKitContainer

Require a native Phalcon container to expose PhalconKit typed helpers.

```php
public static requirePhalconKitContainer(\Phalcon\Di\DiInterface $di, string $operationDescription, string $containerDescription = 'the provided DI'): \PhalconKit\Di\DiInterface
```

Use this helper at framework boundaries that receive Phalcon's native
DI contract but still need PhalconKit's stricter service APIs. The
returned value is narrowed to `PhalconKit\Di\DiInterface`, so callers can
immediately use `getTyped()` and `getConfig()` without repeating
instanceof checks or leaking native Phalcon errors.

* This method is **static**.
**Parameters:**

| Parameter               | Type                        | Description                                                                                                                                 |
|-------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `$di`                   | **\Phalcon\Di\DiInterface** | Container to validate.                                                                                                                      |
| `$operationDescription` | **string**                  | Human-readable operation used in the
exception message, such as `create MVC application` or
`resolve DI service "view" for provider setup`. |
| `$containerDescription` | **string**                  | Human-readable container label used
in the exception message, such as `the application DI`.                                                 |

**Throws:**

When the container does not implement
PhalconKit's DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### fromContainer

Resolve a typed service from an explicit DI container.

```php
public static fromContainer(\Phalcon\Di\DiInterface $di, string $name, class-string<\PhalconKit\Di\T> $expectedType, mixed $parameters = null, string|null $context = null): \PhalconKit\Di\T
```

Use this method when the caller has obtained a DI container from a native
Phalcon API and needs to verify that it is actually a PhalconKit
container before using typed lookups. Missing services fail before
resolution so the optional context can identify the public API that needed
the service.

* This method is **static**.
**Parameters:**

| Parameter       | Type                               | Description                                                                             |
|-----------------|------------------------------------|-----------------------------------------------------------------------------------------|
| `$di`           | **\Phalcon\Di\DiInterface**        | Container to resolve from.                                                              |
| `$name`         | **string**                         | DI service name to resolve.                                                             |
| `$expectedType` | **class-string<\PhalconKit\Di\T>** | Required runtime service contract.                                                      |
| `$parameters`   | **mixed**                          | Optional parameters forwarded to `getTyped()`.                                          |
| `$context`      | **string\|null**                   | Human-readable caller context for exception
messages, such as `PhalconKit tag helpers`. |

**Throws:**

When the container is not a PhalconKit DI, the
service is missing, or the service does not match the expected type.
- [`ServiceException`](../Exception/ServiceException.md)

***

### fromContainerOrDefault

Resolve a typed service from a container or create a typed default.

```php
public static fromContainerOrDefault(\Phalcon\Di\DiInterface $di, string $name, class-string<\PhalconKit\Di\T> $expectedType, callable $defaultFactory, mixed $parameters = null, string|null $context = null): \PhalconKit\Di\T
```

Use this when a framework component supports optional DI replacement but
also has a local default implementation. The container is still required
to be a PhalconKit DI because a caller-provided container participates in
the framework boundary even when the specific service is absent.

* This method is **static**.
**Parameters:**

| Parameter         | Type                               | Description                                                                          |
|-------------------|------------------------------------|--------------------------------------------------------------------------------------|
| `$di`             | **\Phalcon\Di\DiInterface**        | Container to resolve from.                                                           |
| `$name`           | **string**                         | DI service name to resolve when registered.                                          |
| `$expectedType`   | **class-string<\PhalconKit\Di\T>** | Required runtime service contract.                                                   |
| `$defaultFactory` | **callable**                       | Factory used when the service is
not registered in the container.                    |
| `$parameters`     | **mixed**                          | Optional parameters forwarded to `getTyped()`.                                       |
| `$context`        | **string\|null**                   | Human-readable caller context for exception
messages, such as `MVC module services`. |

**Throws:**

When the container is not a PhalconKit DI, the
registered service or default factory output does not match the
expected type, or service resolution fails.
- [`ServiceException`](../Exception/ServiceException.md)

***

### fromDefault

Resolve a typed service from Phalcon's default DI container.

```php
public static fromDefault(string $name, class-string<\PhalconKit\Di\T> $expectedType, mixed $parameters = null, string|null $context = null): \PhalconKit\Di\T
```

Use this method only for static helpers or native Phalcon APIs that
already depend on the default container. Framework and application code
that already has a `DiInterface` should call `fromContainer()` or
`$di->getTyped()` instead.

* This method is **static**.
**Parameters:**

| Parameter       | Type                               | Description                                                                             |
|-----------------|------------------------------------|-----------------------------------------------------------------------------------------|
| `$name`         | **string**                         | DI service name to resolve.                                                             |
| `$expectedType` | **class-string<\PhalconKit\Di\T>** | Required runtime service contract.                                                      |
| `$parameters`   | **mixed**                          | Optional parameters forwarded to `getTyped()`.                                          |
| `$context`      | **string\|null**                   | Human-readable caller context for exception
messages, such as `PhalconKit tag helpers`. |

**Throws:**

When no default DI exists, the default container
is not a PhalconKit DI, the service is missing, or the service does
not match the expected type.
- [`ServiceException`](../Exception/ServiceException.md)

***

### fromPhalconKitContainer

Resolve from a container after enforcing the PhalconKit DI boundary.

```php
private static fromPhalconKitContainer(\Phalcon\Di\DiInterface $di, string $name, class-string<\PhalconKit\Di\T> $expectedType, mixed $parameters, ?string $context, string $containerDescription): \PhalconKit\Di\T
```

* This method is **static**.
**Parameters:**

| Parameter               | Type                               | Description                        |
|-------------------------|------------------------------------|------------------------------------|
| `$di`                   | **\Phalcon\Di\DiInterface**        | Container to inspect.              |
| `$name`                 | **string**                         |                                    |
| `$expectedType`         | **class-string<\PhalconKit\Di\T>** | Required runtime service contract. |
| `$parameters`           | **mixed**                          |                                    |
| `$context`              | **?string**                        |                                    |
| `$containerDescription` | **string**                         |                                    |

***

### contextSuffix

Formats optional caller context for human-readable exception messages.

```php
private static contextSuffix(?string $context): string
```

* This method is **static**.
**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$context` | **?string** |             |

***
