
Declares identity session methods required by JWT, OAuth2, and user helpers.

Implementations are expected to store only the small identity payload under
the active claim key; the full user model is resolved separately through the
configured model service.

***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractSession`

## Methods

### getSessionKey

```php
public getSessionKey(bool $refresh = false): string
```

* This method is **abstract**.
**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***
### removeSessionIdentity

```php
public removeSessionIdentity(): void
```

* This method is **abstract**.
***
### setSessionIdentity

```php
public setSessionIdentity(array<string,mixed> $identity): void
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type                    | Description |
|-------------|-------------------------|-------------|
| `$identity` | **array<string,mixed>** |             |

***
### getSessionIdentity

```php
public getSessionIdentity(): array<string,mixed>
```

* This method is **abstract**.
***
### hasSessionIdentity

```php
public hasSessionIdentity(): bool
```

* This method is **abstract**.
***
### getKey

```php
public getKey(): ?string
```

* This method is **abstract**.
***
### getJwtForStatelessIdentity

Return refreshed JWT values when the concrete identity storage is
stateless.

```php
protected getJwtForStatelessIdentity(): array{jwt?: string, refreshToken?: string, refreshed?: bool}
```

Stateful identity storage persists the payload server-side, so callers
should receive an empty array and preserve their legacy response shape.

* This method is **abstract**.
***
