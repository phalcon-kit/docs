
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\JsonInterface`

## Methods

### jsonEncode

```php
public jsonEncode(mixed $value, int $flags = JSON_UNESCAPED_SLASHES, int $depth = 512): string|false
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |
| `$flags`  | **int**   |             |
| `$depth`  | **int**   |             |

***

### jsonDecode

```php
public jsonDecode(string $json, ?bool $associative = null, int $depth = 512, int $flags): mixed
```

**Parameters:**

| Parameter      | Type       | Description |
|----------------|------------|-------------|
| `$json`        | **string** |             |
| `$associative` | **?bool**  |             |
| `$depth`       | **int**    |             |
| `$flags`       | **int**    |             |

***
