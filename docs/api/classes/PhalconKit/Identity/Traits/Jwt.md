
Resolves identity claims from JWTs, bearer authorization, or session fallback.

Access and refresh tokens both carry the same claim payload, but use
different token ids so the validator can distinguish normal and refresh
flows. The claim `key` is also used by the session identity trait as the
server-side lookup key for the small `userId`/`asUserId` payload, unless
`identity.stateless` stores that payload directly in the token subject.

***

* Full name: `\PhalconKit\Identity\Traits\Jwt`

## Properties

### claim

Cached claim payload for the current manager instance.

```php
public array<string,mixed> $claim
```

***

## Methods

### getJwt

Generate access and refresh tokens for the current claim.

```php
public getJwt(bool $refresh = false): array{jwt: string, refreshToken: string, refreshed: bool}
```

When no claim key exists, a new UUID key is created. During refresh with
session-backed identity storage, the existing identity payload is copied
from the old key to the new key after the old storage entry is removed,
which invalidates tokens tied to the old key while keeping the user
logged in. In stateless identity mode, the payload is preserved directly
in the claim so clients can carry it without PHP session storage; old
signed JWTs remain valid until expiration or an application-level
revocation strategy rejects them.

**Parameters:**

| Parameter  | Type     | Description                                          |
|------------|----------|------------------------------------------------------|
| `$refresh` | **bool** | Rotate the claim key and invalidate previous tokens. |

**Throws:**

When token key generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When JWT validation fails.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### getClaim

Resolve the current claim from request and session sources.

```php
public getClaim(bool $refresh = false, bool $force = false): array<string,mixed>
```

Resolution order is refresh token, JWT request value, authorization
header, then optional session fallback. The fallback is intentionally
disabled by default because it couples token authentication to server-side
session state, and is always skipped when `identity.stateless` is enabled.

**Parameters:**

| Parameter  | Type     | Description                                        |
|------------|----------|----------------------------------------------------|
| `$refresh` | **bool** | Prefer the refresh-token source.                   |
| `$force`   | **bool** | Ignore the cached claim for this manager instance. |

**Return Value:**

Claim payload or an empty array when no
supported credential is present.

***
### setClaim

Replace the cached claim for this manager instance.

```php
public setClaim(array<string,mixed> $claim): void
```

**Parameters:**

| Parameter | Type                    | Description    |
|-----------|-------------------------|----------------|
| `$claim`  | **array<string,mixed>** | Claim payload. |

***
### getJwtToken

Build a signed JWT with Phalcon's JWT service.

```php
public getJwtToken(string $id, array<string,mixed> $data = [], array<string,mixed> $options = []): string
```

Missing issuer and audience values default to the current request URI.
Missing token id defaults to `$id`, and the subject defaults to the JSON
encoded claim data.

**Parameters:**

| Parameter  | Type                    | Description                       |
|------------|-------------------------|-----------------------------------|
| `$id`      | **string**              | Expected token id.                |
| `$data`    | **array<string,mixed>** | Claim payload encoded into `sub`. |
| `$options` | **array<string,mixed>** | Additional JWT builder options.   |

**Return Value:**

Encoded JWT.

**Throws:**

When the JWT builder rejects the options.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### getClaimFromToken

Validate a JWT and return its decoded subject payload.

```php
public getClaimFromToken(string $token, string|null $claim = null): array<string,mixed>
```

The token must match the current request URI as issuer and audience. When
`$claim` is provided, it is used as the expected token id so access and
refresh tokens cannot be exchanged.

**Parameters:**

| Parameter | Type             | Description        |
|-----------|------------------|--------------------|
| `$token`  | **string**       | Encoded JWT.       |
| `$claim`  | **string\|null** | Expected token id. |

**Return Value:**

Decoded `sub` payload or an empty array when
the subject is missing/non-array.

***
### getClaimFromAuthorization

Resolve a claim from a bearer authorization header.

```php
public getClaimFromAuthorization(array<int,string> $authorization): array<string,mixed>
```

**Parameters:**

| Parameter        | Type                  | Description                              |
|------------------|-----------------------|------------------------------------------|
| `$authorization` | **array<int,string>** | Header parts, usually
`[Bearer, token]`. |

**Return Value:**

Claim payload or an empty array when the
header is not a bearer token.

***
### getJsonRawBody

Return the request JSON body as an object.

```php
private getJsonRawBody(): \stdClass
```

Phalcon throws for invalid JSON; identity credential lookup treats that
as an empty body so malformed optional JSON does not prevent header/query
credentials from being evaluated.

**Return Value:**

Parsed body or an empty object.

***
