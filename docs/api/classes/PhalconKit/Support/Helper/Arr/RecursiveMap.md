
Class RecursiveMap

This class provides a way to recursively process the elements of an array using a callback function.

***

* Full name: `\PhalconKit\Support\Helper\Arr\RecursiveMap`

## Methods

### __invoke

```php
public __invoke(array $collection, callable $callback): array
```

**Parameters:**

| Parameter     | Type         | Description |
|---------------|--------------|-------------|
| `$collection` | **array**    |             |
| `$callback`   | **callable** |             |

***

### process

Applies a callback function to each element of the given array recursively and returns a new array.

```php
public static process(array $collection, callable $callback): array
```

* This method is **static**.
**Parameters:**

| Parameter     | Type         | Description                                                                                                                                                                                        |
|---------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$collection` | **array**    | The array to be processed.                                                                                                                                                                         |
| `$callback`   | **callable** | The callback function to be applied to each array element.
The callback function should accept one argument, which is the current array element,
and can return a modified value for that element. |

**Return Value:**

The processed array with the callback function applied to each element.

***
