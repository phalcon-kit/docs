
Public contract for the default PhalconKit identity manager.

The manager is intentionally composed from smaller identity capability
contracts so applications can reason about ACL, impersonation, JWT, OAuth2,
role, session, and user behavior independently. Concrete implementations
should preserve the same session identity keys, user model expectations, and
anti-enumeration behavior as

- **See:** \PhalconKit\Identity\Manager unless they clearly document a
different application-specific policy.

***

* Full name: `\PhalconKit\Identity\ManagerInterface`
* Parent interfaces:
  [`\PhalconKit\Identity\Traits\Interfaces\AclInterface`](./Traits/Interfaces/AclInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\ImpersonationInterface`](./Traits/Interfaces/ImpersonationInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\JwtInterface`](./Traits/Interfaces/JwtInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\Oauth2Interface`](./Traits/Interfaces/Oauth2Interface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\RoleInterface`](./Traits/Interfaces/RoleInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\SessionInterface`](./Traits/Interfaces/SessionInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\UserInterface`](./Traits/Interfaces/UserInterface.md)

**See Also:**

* \PhalconKit\Identity\Manager - Default implementation used by the core service providers.

## Inherited methods

### getUser

Return the effective user or original impersonating user.

```php
public getUser(bool $as = false, bool|null $force = null): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type           | Description                                                      |
|-----------|----------------|------------------------------------------------------------------|
| `$as`     | **bool**       | Return the original user during impersonation.                   |
| `$force`  | **bool\|null** | Force a fresh model lookup instead of using the
cached instance. |

***

### setUser

Cache the effective user for the current manager instance.

```php
public setUser(?\PhalconKit\Models\Interfaces\UserInterface $user): void
```

**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***

### getUserAs

Return the original user when the session is impersonating another user.

```php
public getUserAs(): ?\PhalconKit\Models\Interfaces\UserInterface
```

***

### setUserAs

Cache the original impersonating user for the current manager instance.

```php
public setUserAs(?\PhalconKit\Models\Interfaces\UserInterface $user): void
```

**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***

### getUserId

Return the effective or original user's id.

```php
public getUserId(bool $as = false): ?int
```

**Parameters:**

| Parameter | Type     | Description                                |
|-----------|----------|--------------------------------------------|
| `$as`     | **bool** | Return the original impersonating user id. |

***

### getUserAsId

Return the original user's id during impersonation.

```php
public getUserAsId(): ?int
```

***

### getRoleList

Return identity roles keyed by their stable role key.

```php
public getRoleList(): array<string,object>
```

***

### getGroupList

Return identity groups keyed by their stable group key.

```php
public getGroupList(): array<string,object>
```

***

### getTypeList

Return identity types keyed by their stable type key.

```php
public getTypeList(): array<string,object>
```

***

### isLoggedIn

Check whether the effective or original user is logged in.

```php
public isLoggedIn(bool $as = false, bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description                            |
|-----------|----------|----------------------------------------|
| `$as`     | **bool** | Check the original impersonating user. |
| `$force`  | **bool** | Force a fresh model lookup.            |

***

### isLoggedInAs

Check whether the session is currently impersonating another user.

```php
public isLoggedInAs(bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$force`  | **bool** |             |

***

### findUserById

Find a user by primary key using the configured user model.

```php
public findUserById(int $id): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$id`     | **int** |             |

***

### findUserByEmail

Find a user by email using the configured user model.

```php
public findUserByEmail(string $string): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$string` | **string** |             |

***

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

### hasRole

Check whether the current identity matches requested roles.

```php
public hasRole(array<int,string>|null $roles = null, bool $or = false, bool $inherit = true): bool
```

The legacy `$or` parameter name is misleading: `false` checks whether any
requested role matches, while `true` requires every requested role to
match. The parameter is kept for compatibility.

**Parameters:**

| Parameter  | Type                        | Description                                                                             |
|------------|-----------------------------|-----------------------------------------------------------------------------------------|
| `$roles`   | **array<int,string>\|null** | Role names to test.                                                                     |
| `$or`      | **bool**                    | Legacy mode flag; `false` means any-match, `true` means
all-match at the current level. |
| `$inherit` | **bool**                    | Include configured inherited roles.                                                     |

***

### has

Match one or more values against a haystack.

```php
public has(array<int,mixed>|string|null $needles = null, array<int,string> $haystack = [], bool $or = false): bool
```

Nested arrays flip the current matching mode, allowing callers to express
alternating any/all groups without a separate expression object.

**Parameters:**

| Parameter   | Type                               | Description                                                                             |
|-------------|------------------------------------|-----------------------------------------------------------------------------------------|
| `$needles`  | **array<int,mixed>\|string\|null** | Values or nested groups to
match.                                                       |
| `$haystack` | **array<int,string>**              | Available values.                                                                       |
| `$or`       | **bool**                           | Legacy mode flag; `false` means any-match, `true` means
all-match at the current level. |

***

### getInheritedRoleList

Resolve configured inherited roles for the provided base roles.

```php
public getInheritedRoleList(array<int,string> $roleIndexList = []): array<int,string>
```

**Parameters:**

| Parameter        | Type                  | Description      |
|------------------|-----------------------|------------------|
| `$roleIndexList` | **array<int,string>** | Base role names. |

***

### oauth2

Create or update an OAuth2 identity and log in the linked local user.

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, string|null $refreshToken = null, array<string,mixed>|null $meta = []): array<string,mixed>
```

**Parameters:**

| Parameter       | Type                          | Description                                |
|-----------------|-------------------------------|--------------------------------------------|
| `$provider`     | **string**                    | Provider key such as `google` or `github`. |
| `$providerUuid` | **string**                    | Stable provider-side user identifier.      |
| `$accessToken`  | **string**                    | Current provider access token.             |
| `$refreshToken` | **string\|null**              | Optional provider refresh token.           |
| `$meta`         | **array<string,mixed>\|null** | Optional provider profile data.            |

**Return Value:**

Save state, login state, validation
messages, and optional JWT values when stateless identity mode
changes the token payload.

***

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

### loginAs

Impersonate another user while preserving the original user id.

```php
public loginAs(array<string,mixed> $params = []): array<string,mixed>
```

**Parameters:**

| Parameter | Type                    | Description                                |
|-----------|-------------------------|--------------------------------------------|
| `$params` | **array<string,mixed>** | Parameters containing the target
`userId`. |

**Return Value:**

Login state, validation messages, and
optional JWT values when stateless identity mode changes the token
payload.

***

### logoutAs

Restore the original user stored in the impersonation session payload.

```php
public logoutAs(): array{loggedIn: bool, loggedInAs: bool, jwt?: string, refreshToken?: string, refreshed?: bool}
```

***

### getAclRoles

Return ACL role objects keyed by role name.

```php
public getAclRoles(array<int,string>|null $roleList = null): array<string,\Phalcon\Acl\Role>
```

Implementations should include contextual roles such as `everyone`,
execution-context roles, identity roles, guest fallback, and inherited
roles according to the identity manager policy.

**Parameters:**

| Parameter   | Type                        | Description                                                                          |
|-------------|-----------------------------|--------------------------------------------------------------------------------------|
| `$roleList` | **array<int,string>\|null** | Optional base role names to use
instead of deriving roles from the current identity. |

***
