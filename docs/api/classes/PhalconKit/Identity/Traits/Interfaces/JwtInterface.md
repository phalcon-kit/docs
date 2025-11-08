
***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\JwtInterface`

## Methods

### getJwt

```php
public getJwt(bool $refresh = false): array
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***

### getClaim

```php
public getClaim(bool $refresh = false, bool $force = false): array
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |
| `$force`   | **bool** |             |

***

### setClaim

```php
public setClaim(array $claim): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$claim`  | **array** |             |

***

### getJwtToken

```php
public getJwtToken(string $id, array $data = [], array $options = []): string
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$id`      | **string** |             |
| `$data`    | **array**  |             |
| `$options` | **array**  |             |

***

### getClaimFromToken

```php
public getClaimFromToken(string $token, ?string $claim = null): array
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$token`  | **string**  |             |
| `$claim`  | **?string** |             |

***

### getClaimFromAuthorization

```php
public getClaimFromAuthorization(array $authorization): array
```

**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$authorization` | **array** |             |

***
