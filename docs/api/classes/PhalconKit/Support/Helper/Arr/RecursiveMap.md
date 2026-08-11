
Apply a callback to every scalar value in a nested array.

Array keys and nesting are preserved. Only non-array leaf values are passed
to the callback, which makes the helper useful for normalizing config values
without changing the shape expected by providers or policy builders.

***

* Full name: `\PhalconKit\Support\Helper\Arr\RecursiveMap`

## Methods

### __invoke

Invoke the helper for a nested array.

```php
public __invoke(array<string|int,mixed> $collection, callable $callback): array<string|int,mixed>
```

**Parameters:**

| Parameter     | Type                         | Description                               |
|---------------|------------------------------|-------------------------------------------|
| `$collection` | **array<string\|int,mixed>** | Input array.                              |
| `$callback`   | **callable**                 | Callback applied to each non-array value. |

***

### process

Apply a callback to each non-array value and preserve array structure.

```php
public static process(array<string|int,mixed> $collection, callable $callback): array<string|int,mixed>
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                         | Description                              |
|---------------|------------------------------|------------------------------------------|
| `$collection` | **array<string\|int,mixed>** | The array to process.                    |
| `$callback`   | **callable**                 | Callback receiving each non-array value. |

***
