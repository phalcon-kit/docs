
Declares JWT claim methods required by session and identity helpers.

The identity session layer uses the active claim key to read and write the
session payload, so any class using this abstract trait must provide the JWT
claim lifecycle from

- **See:** \PhalconKit\Identity\Traits\Interfaces\JwtInterface.

***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractJwt`

## Methods

### getJwt

```php
public getJwt(bool $refresh = false): array{jwt: string, refreshToken: string, refreshed: bool}
```

* This method is **abstract**.
**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***
### getClaim

```php
public getClaim(bool $refresh = false, bool $force = false): array<string,mixed>
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
public setClaim(array<string,mixed> $claim): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                    | Description |
|-----------|-------------------------|-------------|
| `$claim`  | **array<string,mixed>** |             |

***
### getJwtToken

```php
public getJwtToken(string $id, array<string,mixed> $data = [], array<string,mixed> $options = []): string
```

* This method is **abstract**.
**Parameters:**

| Parameter  | Type                    | Description |
|------------|-------------------------|-------------|
| `$id`      | **string**              |             |
| `$data`    | **array<string,mixed>** |             |
| `$options` | **array<string,mixed>** |             |

***
### getClaimFromToken

```php
public getClaimFromToken(string $token, ?string $claim = null): array<string,mixed>
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
public getClaimFromAuthorization(array<int,string> $authorization): array<string,mixed>
```

* This method is **abstract**.
**Parameters:**

| Parameter        | Type                  | Description |
|------------------|-----------------------|-------------|
| `$authorization` | **array<int,string>** |             |

***
