
This class is responsible for transforming a Model object into an array representation.

***

* Full name: `\PhalconKit\Fractal\ModelTransformer`
* Parent class: [`TransformerAbstract`](https://fractal.thephpleague.com/){:target="_blank"}
* This class implements:
  `InjectionAwareInterface`

## Methods

### transform

```php
public transform(\Phalcon\Mvc\Model $model): array
```

**Parameters:**

| Parameter | Type                   | Description |
|-----------|------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\Model** |             |

***

## Inherited methods

### getDI

Returns the Dependency Injection (DI) container used by this object.

```php
public getDI(): \Phalcon\Di\DiInterface
```

**Return Value:**

The DI container instance.

***

### setDI

Sets the dependency injection container.

```php
public setDI(\Phalcon\Di\DiInterface $container): void
```

**Parameters:**

| Parameter    | Type                        | Description                         |
|--------------|-----------------------------|-------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface** | The dependency injection container. |

***

### __isset

Checks if a property is set.

```php
public __isset(string $name): bool
```

**Parameters:**

| Parameter | Type       | Description                        |
|-----------|------------|------------------------------------|
| `$name`   | **string** | The name of the property to check. |

**Return Value:**

True if the property is set, false otherwise.

***

### __get

Magic method __get.

```php
public __get(string $name): mixed
```

Retrieves the value of a non-existent or inaccessible property.

**Parameters:**

| Parameter | Type       | Description               |
|-----------|------------|---------------------------|
| `$name`   | **string** | The name of the property. |

**Return Value:**

The value of the property if it exists, or null if the property is undefined.

***
