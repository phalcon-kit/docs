
Stores the lightweight identity payload for the active manager.

By default the payload is written under the active JWT claim key in the
configured session service. This allows JWT refreshes to rotate the storage
key and invalidate older tokens while preserving the small `userId` and
`asUserId` payload.

When `identity.stateless` is enabled, the same payload is stored directly in
the JWT claim instead. That mode is intended for API clients that want the
identity layer to avoid PHP session persistence while the rest of the
application can still use sessions for unrelated features such as flash
messages, OAuth2 state, or locale persistence.

***

* Full name: `\PhalconKit\Identity\Traits\Session`

## Constants

| Constant           | Visibility | Type   | Value                  |
|--------------------|------------|--------|------------------------|
| `SESSION_KEY`      | public     | string | 'phalcon-kit-identity' |
| `REFRESH_SUFFIX`   | public     | string | '-refresh'             |
| `TOKEN_CLAIM_KEYS` | private    | array  | ['key' => true]        |

## Methods

### getSessionKey

Return the configured identity session namespace.

```php
public getSessionKey(bool $refresh = false): string
```

**Parameters:**

| Parameter  | Type     | Description                                                                            |
|------------|----------|----------------------------------------------------------------------------------------|
| `$refresh` | **bool** | Append {@see \PhalconKit\Identity\Traits\REFRESH_SUFFIX} for refresh-token
operations. |

**Return Value:**

Configured session key with the optional refresh suffix.

***
### removeSessionIdentity

Remove the identity payload stored under the active claim key.

```php
public removeSessionIdentity(): void
```

If no claim key is available, there is no addressable identity payload
and the method intentionally becomes a no-op.

***
### setSessionIdentity

Store the identity payload under the active claim key.

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

Return the identity payload stored under the active claim key.

```php
public getSessionIdentity(): array<string,mixed>
```

**Return Value:**

Empty when no key or payload exists.

***
### hasSessionIdentity

Check whether an identity payload exists for the active claim key.

```php
public hasSessionIdentity(): bool
```

**Return Value:**

True when both a claim key and matching session payload are
present.

***
### getKey

Return the active claim key used to address session identity storage.

```php
public getKey(): string|null
```

**Return Value:**

Claim key or null when no usable claim has been
resolved.

***
### isStatelessIdentity

Check whether identity state should be carried only in JWT claims.

```php
protected isStatelessIdentity(): bool
```

This setting does not disable the framework session service globally. It
only changes where the identity payload is persisted, which keeps
unrelated session consumers available for applications that still need
them.

***
### getJwtForStatelessIdentity

Return fresh JWT values after an identity state change when needed.

```php
protected getJwtForStatelessIdentity(): array{jwt?: string, refreshToken?: string, refreshed?: bool}
```

Stateless clients must replace their token after login, logout, OAuth2
login, and impersonation changes because the identity payload lives in
the token subject. Stateful clients keep receiving the legacy response
shape because the session-backed payload has already changed server-side.

***
