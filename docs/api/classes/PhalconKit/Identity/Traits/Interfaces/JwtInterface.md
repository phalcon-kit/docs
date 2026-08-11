
Contract for JWT-backed identity claims and token generation.

***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\JwtInterface`

## Methods

### getJwt

Build access and refresh tokens for the current claim.

```php
public getJwt(bool $refresh = false): array{jwt: string, refreshToken: string, refreshed: bool}
```

In stateless identity mode the claim also carries the identity payload,
so callers should replace their stored token after any login/logout or
impersonation change that returns new JWT values. Replacing the client
token does not revoke older signed JWTs by itself; applications that need
immediate revocation need a denylist, token-version check, short access
token lifetime, or similar strategy.

**Parameters:**

| Parameter  | Type     | Description                                                                         |
|------------|----------|-------------------------------------------------------------------------------------|
| `$refresh` | **bool** | Rotate the claim key and preserve session identity
under the new key when possible. |

***

### getClaim

Resolve the current claim from request tokens, authorization headers, or
the optional session fallback.

```php
public getClaim(bool $refresh = false, bool $force = false): array<string,mixed>
```

**Parameters:**

| Parameter  | Type     | Description                                                        |
|------------|----------|--------------------------------------------------------------------|
| `$refresh` | **bool** | Prefer the refresh token source.                                   |
| `$force`   | **bool** | Ignore any cached claim and inspect request/session
sources again. |

***

### setClaim

Replace the in-memory claim for this manager instance.

```php
public setClaim(array<string,mixed> $claim): void
```

**Parameters:**

| Parameter | Type                    | Description    |
|-----------|-------------------------|----------------|
| `$claim`  | **array<string,mixed>** | Claim payload. |

***

### getJwtToken

Create a signed JWT for the given token id and payload.

```php
public getJwtToken(string $id, array<string,mixed> $data = [], array<string,mixed> $options = []): string
```

**Parameters:**

| Parameter  | Type                    | Description                         |
|------------|-------------------------|-------------------------------------|
| `$id`      | **string**              | Token id used by the JWT validator. |
| `$data`    | **array<string,mixed>** | Subject payload to encode.          |
| `$options` | **array<string,mixed>** | JWT builder options.                |

***

### getClaimFromToken

Validate a JWT and extract its subject claim payload.

```php
public getClaimFromToken(string $token, string|null $claim = null): array<string,mixed>
```

**Parameters:**

| Parameter | Type             | Description      |
|-----------|------------------|------------------|
| `$token`  | **string**       | Encoded JWT.     |
| `$claim`  | **string\|null** | Expected JWT id. |

***

### getClaimFromAuthorization

Extract a bearer token from an authorization header split into parts.

```php
public getClaimFromAuthorization(array<int,string> $authorization): array<string,mixed>
```

**Parameters:**

| Parameter        | Type                  | Description                              |
|------------------|-----------------------|------------------------------------------|
| `$authorization` | **array<int,string>** | Header parts, usually
`[Bearer, token]`. |

***
