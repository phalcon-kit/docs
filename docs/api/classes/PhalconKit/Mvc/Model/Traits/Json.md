
Trait Json

This trait provides methods for encoding and decoding JSON data.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Json`

## Methods

### jsonEncode

Encodes a value to JSON.

```php
public jsonEncode(mixed $value, int $flags = JSON_UNESCAPED_SLASHES, int $depth = 512): string|false
```

**Parameters:**

| Parameter | Type      | Description                                                                              |
|-----------|-----------|------------------------------------------------------------------------------------------|
| `$value`  | **mixed** | The value to be encoded.                                                                 |
| `$flags`  | **int**   | [Optional] Bitmask of JSON encode options.
Defaults to JSON_UNESCAPED_SLASHES.           |
| `$depth`  | **int**   | [Optional] The maximum depth of recursion when encoding nested objects.
Defaults to 512. |

**Return Value:**

The JSON encoded string on success, or `false` on failure.

***
### jsonDecode

Decodes a JSON string.

```php
public jsonDecode(string $json, bool|null $associative = null, int $depth = 512, int $flags): mixed
```

**Parameters:**

| Parameter      | Type           | Description                                                                                                                                                                                                              |
|----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$json`        | **string**     | The JSON string to be decoded.                                                                                                                                                                                           |
| `$associative` | **bool\|null** | [Optional] When `true`, returned objects will be converted into associative arrays.
When `false`, objects will be returned as generic objects. If `null`, objects
will be returned based on the JSON_NUMERIC_CHECK flag. |
| `$depth`       | **int**        | [Optional] The maximum depth of recursion when decoding nested objects.
Defaults to 512.                                                                                                                                 |
| `$flags`       | **int**        | [Optional] Bitmask of JSON decode options.
Defaults to 0.                                                                                                                                                                |

**Return Value:**

The decoded value on success, or the original JSON string on failure.

***
### validateJsonDepth

Validates that the provided depth is within the supported JSON recursion range.

```php
private validateJsonDepth(int $depth): int<1, 2147483647>
```

**Parameters:**

| Parameter | Type    | Description                      |
|-----------|---------|----------------------------------|
| `$depth`  | **int** | The recursion depth to validate. |

**Return Value:**

The validated depth.

**Throws:**

If depth is outside the valid range.
- [`InvalidArgumentException`](../../../../InvalidArgumentException.md)

***
