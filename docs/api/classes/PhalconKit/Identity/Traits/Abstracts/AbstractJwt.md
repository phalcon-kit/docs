
***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractJwt`

## Methods

### getJwt

```php
public getJwt(bool $refresh = false): array
```

* This method is **abstract**.
**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***
### getClaim

```php
public getClaim(bool $refresh = false, bool $force = false): array
```

* This method is **abstract**.
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

* This method is **abstract**.
**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$claim`  | **array** |             |

***
### getJwtToken

```php
public getJwtToken(string $id, array $data = [], array $options = []): string
```

* This method is **abstract**.
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

* This method is **abstract**.
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

* This method is **abstract**.
**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$authorization` | **array** |             |

***
