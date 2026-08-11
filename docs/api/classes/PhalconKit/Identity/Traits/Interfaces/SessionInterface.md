
Contract for storing identity payloads under the current claim key.

Implementations may persist the payload in the PHP session service or carry
it directly in JWT claims for stateless identity mode, but callers should use
this contract consistently instead of reading either storage location
directly.

***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\SessionInterface`

## Methods

### getSessionKey

Return the configured identity session key.

```php
public getSessionKey(bool $refresh = false): string
```

**Parameters:**

| Parameter  | Type     | Description                                |
|------------|----------|--------------------------------------------|
| `$refresh` | **bool** | Append the refresh-token suffix when true. |

***

### removeSessionIdentity

Remove the identity payload stored under the current claim key.

```php
public removeSessionIdentity(): void
```

***

### setSessionIdentity

Store the identity payload under the current claim key.

```php
public setSessionIdentity(array<string,mixed> $identity): void
```

**Parameters:**

| Parameter   | Type                    | Description                                                             |
|-------------|-------------------------|-------------------------------------------------------------------------|
| `$identity` | **array<string,mixed>** | Identity payload, usually including
`userId` and optionally `asUserId`. |

***

### getSessionIdentity

Return the identity payload stored under the current claim key.

```php
public getSessionIdentity(): array<string,mixed>
```

***

### hasSessionIdentity

Check whether an identity payload exists under the current claim key.

```php
public hasSessionIdentity(): bool
```

***

### getKey

Return the active claim key used to address identity session storage.

```php
public getKey(): ?string
```

***
