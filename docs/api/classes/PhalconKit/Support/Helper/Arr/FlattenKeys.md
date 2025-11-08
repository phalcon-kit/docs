
This class provides methods to parse an array into a flatten array with key path separated by a delimiter.

***

* Full name: `\PhalconKit\Support\Helper\Arr\FlattenKeys`

## Methods

### __invoke

```php
public __invoke(array $collection = [], string $delimiter = '.', bool $lowerKey = true): array
```

**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$collection` | **array**  |             |
| `$delimiter`  | **string** |             |
| `$lowerKey`   | **bool**   |             |

***

### process

Here to parse the columns parameter into some kind of flatten array with
the key path separated by dot "my.path" and the value true, false or a callback function
including the ExposeBuilder object

```php
public static process(array $collection = [], string $delimiter = '.', bool $lowerKey = false, ?string $context = null): ?array
```

* This method is **static**.
**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$collection` | **array**   |             |
| `$delimiter`  | **string**  |             |
| `$lowerKey`   | **bool**    |             |
| `$context`    | **?string** |             |

***
