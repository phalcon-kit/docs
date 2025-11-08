
This class extends the TransformerAbstract class and implements the InjectionAwareInterface.

It also uses the InjectableTrait.

***

* Full name: `\PhalconKit\Modules\Api\Transformers\RecordTransformer`
* Parent class: [`\PhalconKit\Fractal\Transformer`](../../../Fractal/Transformer.md)

## Methods

### transform

```php
public transform(?\PhalconKit\Models\Record $record): array
```

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$record` | **?\PhalconKit\Models\Record** |             |

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
