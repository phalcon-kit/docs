
***

* Full name: `\PhalconKit\Bootstrap\Permissions\ColumnConfig`
* Parent class: [`\PhalconKit\Config\Config`](../../Config/Config.md)

## Methods

### __construct

```php
public __construct(array $data = [], bool $insensitive = true): mixed
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$data`        | **array** |             |
| `$insensitive` | **bool**  |             |

***

## Inherited methods

### pathToArray

Retrieves a value from a path and converts it to an array.

```php
public pathToArray(string $path, array|null $defaultValue = null, string|null $delimiter = null): array|null
```

**Parameters:**

| Parameter       | Type             | Description                                             |
|-----------------|------------------|---------------------------------------------------------|
| `$path`         | **string**       | The path to retrieve the value from.                    |
| `$defaultValue` | **array\|null**  | The default value to return if the path does not exist. |
| `$delimiter`    | **string\|null** | The delimiter to use for splitting the path.            |

**Return Value:**

The value from the path as an array, or null if the value does not exist.

***

### merge

Merges the current configuration object with another set of data.

```php
public merge(array|\Phalcon\Config\ConfigInterface $toMerge, bool $append = false): \Phalcon\Config\ConfigInterface
```

**Parameters:**

| Parameter  | Type                                       | Description                                                                                                                                    |
|------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `$toMerge` | **array\|\Phalcon\Config\ConfigInterface** | The data to merge into the current configuration.
This can be an array or another configuration object that implements PhalconConfigInterface. |
| `$append`  | **bool**                                   | Whether to append the data during the merge or replace existing values.
Defaults to false, meaning values will be replaced during the merge.   |

**Return Value:**

Returns the updated configuration object after the merge operation.
The current instance is modified and returned.

**Throws:**

If the $toMerge parameter is not of a valid data type.
- [`Exception`](../../../Exception.md)

***

### internalMergeAppend

Merges two arrays recursively, appending values from the target array into the source array.

```php
final protected internalMergeAppend(array $source, array $target): array
```

Handles both associative and indexed arrays.

* This method is **final**.
**Parameters:**

| Parameter | Type      | Description                            |
|-----------|-----------|----------------------------------------|
| `$source` | **array** | The source array to merge values into. |
| `$target` | **array** | The target array to merge values from. |

**Return Value:**

The resulting array after the merge operation.

***

### getDateTime

Get a modified DateTime.

```php
public getDateTime(string $modifier, \DateTimeImmutable|null $dateTime = null): \DateTimeImmutable
```

Note: This is a helper to enhance strict typings and safely use DateTime within config

**Parameters:**

| Parameter   | Type                         | Description                                                                     |
|-------------|------------------------------|---------------------------------------------------------------------------------|
| `$modifier` | **string**                   | The modifier string to modify the DateTime.                                     |
| `$dateTime` | **\DateTimeImmutable\|null** | Optional. The DateTime to modify. Defaults to current DateTime if not provided. |

**Return Value:**

The modified DateTime object.

**Throws:**

If the modification of the DateTime fails.
- [`Exception`](../../../Exception.md)

***
