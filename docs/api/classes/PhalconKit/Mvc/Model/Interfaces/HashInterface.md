
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\HashInterface`

## Methods

### hash

```php
public hash(string $string, ?string $salt = null, ?string $workFactor = null): string
```

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$string`     | **string**  |             |
| `$salt`       | **?string** |             |
| `$workFactor` | **?string** |             |

***

### checkHash

```php
public checkHash(?string $hash = null, ?string $string = null, int $maxPassLength): bool
```

**Parameters:**

| Parameter        | Type        | Description |
|------------------|-------------|-------------|
| `$hash`          | **?string** |             |
| `$string`        | **?string** |             |
| `$maxPassLength` | **int**     |             |

***
