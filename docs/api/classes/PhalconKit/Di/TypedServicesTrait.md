
Implements typed service lookups for PhalconKit DI containers.

Classes using this trait must provide Phalcon's native `get()` method, which
is why the trait is only intended for DI container classes that extend native
Phalcon containers.

***

* Full name: `\PhalconKit\Di\TypedServicesTrait`

## Methods

### getTyped

Resolve a DI service and enforce its runtime type.

```php
public getTyped(string $name, class-string<\PhalconKit\Di\T> $expectedType, mixed $parameters = null): \PhalconKit\Di\T
```

Missing services and wrong service types are wrapped in ServiceException
so framework callers get stable PhalconKit failures instead of raw
Phalcon exceptions, PHP type errors, or disabled assertion behavior.

**Parameters:**

| Parameter       | Type                               | Description                                                              |
|-----------------|------------------------------------|--------------------------------------------------------------------------|
| `$name`         | **string**                         | DI service name to resolve.                                              |
| `$expectedType` | **class-string<\PhalconKit\Di\T>** |                                                                          |
| `$parameters`   | **mixed**                          | Optional parameters forwarded to the underlying
Phalcon DI `get()` call. |

**Throws:**

When the service cannot be resolved or does not
implement the expected type.
- [`ServiceException`](../Exception/ServiceException.md)

***
### getConfig

Resolve a config service as a PhalconKit ConfigInterface.

```php
public getConfig(string $name = 'config'): \PhalconKit\Config\ConfigInterface
```

This is the preferred path for providers and bootstraps that need config.
It delegates to getTyped() so missing or invalid config services fail with
the same explicit ServiceException behavior as other typed lookups.

**Parameters:**

| Parameter | Type       | Description                                   |
|-----------|------------|-----------------------------------------------|
| `$name`   | **string** | DI service name containing the config object. |

**Throws:**

When the service cannot be resolved or is not a
ConfigInterface instance.
- [`ServiceException`](../Exception/ServiceException.md)

***
