
PhalconKit dependency injection contract.

This interface extends Phalcon's native DI contract with typed lookup helpers
used by the PhalconKit bootstrap, service providers, and downstream
applications. Code that participates in the PhalconKit provider/bootstrap
boundary should type against this interface instead of native
`Phalcon\Di\DiInterface` so `getTyped()` and `getConfig()` are available.

***

* Full name: `\PhalconKit\Di\DiInterface`
* Parent interfaces:
  `DiInterface`

**See Also:**

* https://docs.phalcon.io/latest/di/

## Methods

### getTyped

Resolve a DI service and enforce its runtime type.

```php
public getTyped(string $name, class-string<\PhalconKit\Di\T> $expectedType, mixed $parameters = null): \PhalconKit\Di\T
```

Use this helper when the caller knows the expected service contract. It
keeps provider and framework code concise while still failing with a
clear framework exception when a service is missing or misconfigured.

**Parameters:**

| Parameter       | Type                               | Description                                                              |
|-----------------|------------------------------------|--------------------------------------------------------------------------|
| `$name`         | **string**                         | DI service name to resolve.                                              |
| `$expectedType` | **class-string<\PhalconKit\Di\T>** |                                                                          |
| `$parameters`   | **mixed**                          | Optional parameters forwarded to the underlying
Phalcon DI `get()` call. |

**Throws:**

When the service cannot be
resolved or does not implement the expected type.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getConfig

Resolve a config service and enforce the PhalconKit config contract.

```php
public getConfig(string $name = 'config'): \PhalconKit\Config\ConfigInterface
```

The default service name is `config`, but tests and specialized
bootstraps may pass a different service name when they intentionally
register more than one config object.

**Parameters:**

| Parameter | Type       | Description                                   |
|-----------|------------|-----------------------------------------------|
| `$name`   | **string** | DI service name containing the config object. |

**Throws:**

When the service cannot be
resolved or is not a ConfigInterface instance.
- [`ServiceException`](../Exception/ServiceException.md)

***
