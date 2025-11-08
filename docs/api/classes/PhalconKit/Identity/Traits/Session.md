
***

* Full name: `\PhalconKit\Identity\Traits\Session`

## Constants

| Constant         | Visibility | Type | Value                  |
|------------------|------------|------|------------------------|
| `SESSION_KEY`    | public     |      | 'phalcon-kit-identity' |
| `REFRESH_SUFFIX` | public     |      | '-refresh'             |

## Methods

### getSessionKey

Retrieves the session key, optionally appending a refresh suffix.

```php
public getSessionKey(bool $refresh = false): string
```

**Parameters:**

| Parameter  | Type     | Description                                                           |
|------------|----------|-----------------------------------------------------------------------|
| `$refresh` | **bool** | Indicates whether to append the '-refresh' suffix to the session key. |

**Return Value:**

The retrieved session key, with or without the refresh suffix.

***
### removeSessionIdentity

Removes the session identity associated with the current instance, if a valid key exists.

```php
public removeSessionIdentity(): void
```

***
### setSessionIdentity

Sets the session identity by storing the provided identity data in the session.

```php
public setSessionIdentity(array $identity): void
```

**Parameters:**

| Parameter   | Type      | Description                                                                      |
|-------------|-----------|----------------------------------------------------------------------------------|
| `$identity` | **array** | An associative array representing the identity data to be stored in the session. |

***
### getSessionIdentity

Retrieves the session identity from the session storage.

```php
public getSessionIdentity(): array
```

**Return Value:**

An associative array representing the identity data retrieved from the session. Returns an empty array if no data is found.

***
### hasSessionIdentity

Checks if a session identity exists by verifying the presence of a valid key and its association in the session.

```php
public hasSessionIdentity(): bool
```

**Return Value:**

Returns true if a session identity exists; otherwise, false.

***
### getKey

Retrieves the 'key' value from the claim array if it exists, or returns null.

```php
public getKey(): string|null
```

**Return Value:**

The 'key' value from the claim array, or null if not found.

***
