
Class Helper

This class is responsible for providing helper methods and functions.

Native methods

***

* Full name: `\PhalconKit\Support\Helper`

## Properties

### helperFactory

```php
public static ?\PhalconKit\Support\HelperFactory $helperFactory
```

* This property is **static**.

***

## Methods

### getHelperFactory

Returns the instance of the HelperFactory class.

```php
public static getHelperFactory(): \PhalconKit\Support\HelperFactory
```

This method is responsible for providing the HelperFactory instance.
If the instance is already set, it returns the existing instance.
If the instance is not set, it tries to retrieve it from the dependency injection container.
If the instance is not found in the container, it creates a new instance of HelperFactory.

* This method is **static**.
**Return Value:**

The instance of the HelperFactory class.

***

### __callStatic

Magic method __callStatic

```php
public static __callStatic(string $name, array $arguments): mixed
```

This method is a magic method that allows calling static methods dynamically.

* This method is **static**.
**Parameters:**

| Parameter    | Type       | Description                             |
|--------------|------------|-----------------------------------------|
| `$name`      | **string** | The name of the static method to call.  |
| `$arguments` | **array**  | Arguments to pass to the static method. |

**Return Value:**

The result of the static method call.

***
