
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Abstracts\AbstractInjectable`

## Methods

### setDI

```php
public setDI(\Phalcon\Di\DiInterface $di): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                        | Description |
|-----------|-----------------------------|-------------|
| `$di`     | **\Phalcon\Di\DiInterface** |             |

***
### getDI

```php
public getDI(): \Phalcon\Di\DiInterface
```

* This method is **abstract**.
***
### getTypedService

Resolve a typed service from the model's DI container.

```php
protected getTypedService(string $name, class-string<\PhalconKit\Mvc\Model\Traits\Abstracts\T> $expectedType, string|null $context = null): \PhalconKit\Mvc\Model\Traits\Abstracts\T
```

Model traits often run inside native Phalcon model lifecycle hooks, where
the inherited `getDI()` return type is only Phalcon's native DI contract.
This helper centralizes the PhalconKit DI boundary check and typed service
validation so individual traits do not need repetitive private wrappers
around `ServiceResolver::fromContainer()`.

**Parameters:**

| Parameter       | Type                                                       | Description                                                                         |
|-----------------|------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `$name`         | **string**                                                 | DI service name to resolve.                                                         |
| `$expectedType` | **class-string<\PhalconKit\Mvc\Model\Traits\Abstracts\T>** | Required runtime service contract.                                                  |
| `$context`      | **string\|null**                                           | Human-readable caller context for exception
messages, such as `model hash helpers`. |

**Throws:**

When the model DI is not a
PhalconKit DI, the service is missing, or the service does not match
the expected type.
- [`ServiceException`](../../../../Exception/ServiceException.md)

***
