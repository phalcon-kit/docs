
This class provides functionality to recursively replace specific patterns in strings
within a nested array structure using a key/value map of replacements.

***

* Full name: `\PhalconKit\Support\Helper\Arr\RecursiveStrReplace`

## Methods

### __invoke

```php
public __invoke(array $collection, array $replaces): array
```

**Parameters:**

| Parameter     | Type      | Description |
|---------------|-----------|-------------|
| `$collection` | **array** |             |
| `$replaces`   | **array** |             |

***

### process

Processes the given collection recursively, replacing specific key patterns in strings
with their corresponding values from the replaces array.

```php
public static process(array $collection, array $replaces): array|null
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                                              |
|---------------|-----------|----------------------------------------------------------------------------------------------------------|
| `$collection` | **array** | The input array to be processed. It can contain nested arrays and/or strings.                            |
| `$replaces`   | **array** | An associative array where keys are the patterns to be replaced, and values are the replacement strings. |

**Return Value:**

Returns the processed array with replaced values, or null if processing fails.

***
