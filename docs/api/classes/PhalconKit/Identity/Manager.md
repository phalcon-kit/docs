
Coordinates authentication state for PhalconKit applications.

The manager exposes a compact identity API on top of several lower-level
traits: user lookup, session-backed identity storage, JWT claim handling,
OAuth2 account linking, role inheritance, ACL role construction, and
impersonation. It expects the application DI to provide the standard
PhalconKit services used by those traits, including config, models, request,
security, session, JWT, and bootstrap services.

Identity state is stored as a small payload keyed by the active JWT claim
key. The payload normally lives in the session service; when
`identity.stateless` is enabled it lives directly in the JWT claim so API
clients can avoid server-side identity persistence. The primary payload keys
are `userId` for the effective user and `asUserId` for the original user
during impersonation. Login and password reset responses deliberately avoid
exposing whether an email address exists unless validation has already
failed, so downstream code should preserve that behavior when overriding the
manager.

***

* Full name: `\PhalconKit\Identity\Manager`
* Parent class: [`\PhalconKit\Di\Injectable`](../Di/Injectable.md)
* This class implements:
  [`\PhalconKit\Identity\ManagerInterface`](./ManagerInterface.md),
  [`\PhalconKit\Support\Options\OptionsInterface`](../Support/Options/OptionsInterface.md)

## Methods

### get

Return the current identity payload.

```php
public get(array|null $userExpose = null): array<string,mixed>
```

This method is the short public entry point used by controllers and API
responses. It delegates to

- **See:** \PhalconKit\Identity\getIdentity() so subclasses only need
to customize the detailed identity payload in one place.

**Parameters:**

| Parameter     | Type            | Description                                                                               |
|---------------|-----------------|-------------------------------------------------------------------------------------------|
| `$userExpose` | **array\|null** | Optional expose definition passed to user
models before they are returned in the payload. |

**Return Value:**

Identity payload for the current request.

***

### getIdentity

Build the current identity payload.

```php
public getIdentity(array|null $userExpose = null): array{loggedInAs: bool, userAs: mixed, loggedIn: bool, user: mixed, roleList: array<string,object>, typeList: array<string,object>, groupList: array<string,object>}
```

The payload includes both the effective user and the original user when
impersonating. Related role, type, and group lists are normalized into
maps keyed by each related entity's `getKey()` value so ACL checks and
API consumers can use stable identifiers without inspecting model
relation internals.

**Parameters:**

| Parameter     | Type            | Description                                                                           |
|---------------|-----------------|---------------------------------------------------------------------------------------|
| `$userExpose` | **array\|null** | Optional expose definition passed to
`expose()` on user models before returning them. |

**Throws:**

When a related role/type/group entity cannot
provide a stable key.
- [`LogicException`](../Exception/LogicException.md)

***

### login

Validate credentials and establish the session identity.

```php
public login(array<string,mixed> $params = []): array{loggedIn: bool, loggedInAs: bool, messages: \Phalcon\Messages\Messages, jwt?: string, refreshToken?: string, refreshed?: bool}
```

The login flow accepts an email address and password, validates both
fields, checks the configured user model, and stores the authenticated
`userId` in the identity payload. Missing users, disabled passwords, and
invalid passwords all return the same generic login-failed message so the
response does not reveal whether an account exists. Deleted users are
rejected with a forbidden message after password verification succeeds.
When stateless identity is enabled, successful responses also include a
freshly signed JWT/refresh-token pair containing the new identity payload.

Successful login also refreshes the global model security roles from the
effective ACL roles, allowing model behaviors to evaluate the newly
authenticated identity immediately.

**Parameters:**

| Parameter | Type                    | Description                                              |
|-----------|-------------------------|----------------------------------------------------------|
| `$params` | **array<string,mixed>** | Login fields. Supported keys are
`email` and `password`. |

**Throws:**

When stateless token key generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### logout

Remove the current identity payload.

```php
public logout(): array{loggedIn: bool, loggedInAs: bool, jwt?: string, refreshToken?: string, refreshed?: bool}
```

Logout clears the identity stored under the current claim key. It does not
clear unrelated session data. Stateless clients receive a refreshed
anonymous token response and must replace/discard any older authenticated
token client-side; JWTs are not server-revoked without an application
revocation strategy.

**Return Value:**

Login state after
the identity has been removed.

**Throws:**

When stateless token key generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### reset

Start or complete a password reset flow.

```php
public reset(array<string,mixed>|null $params = null): array<string,mixed>
```

When only `email` is provided, the manager creates a random reset token,
stores its hash on the user record, and returns an empty response on
success. When `resetToken` and `password` are provided, the token is
verified against the stored hash before the password is updated and the
reset token is cleared.

To prevent user enumeration, a valid request for a missing email returns
the same empty response shape as a successful request. Validation failures
and persistence failures still return messages because those are
actionable by the caller. Notification delivery is intentionally left to
application code until the framework has a mailer/event contract for this
flow.

**Parameters:**

| Parameter | Type                          | Description                                                                                              |
|-----------|-------------------------------|----------------------------------------------------------------------------------------------------------|
| `$params` | **array<string,mixed>\|null** | Reset fields. Supported keys are
`email`, optional `resetToken`, and `password` when completing a
reset. |

**Return Value:**

Empty on successful or intentionally opaque
outcomes, or `messages` when validation/persistence fails.

**Throws:**

When token generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### collectList

Normalize a related model list into a key-indexed map.

```php
private collectList(\PhalconKit\Mvc\ModelInterface|null $model, string $property, string $keyMethod = 'getKey'): array<string,object>
```

Identity payloads need stable role, type, and group keys regardless of
whether relations were eager-loaded, staged as dirty related records, or
assigned to public fixture properties in tests. This helper checks those
sources in order and ignores missing or non-iterable values.

**Parameters:**

| Parameter    | Type                                     | Description                                                    |
|--------------|------------------------------------------|----------------------------------------------------------------|
| `$model`     | **\PhalconKit\Mvc\ModelInterface\|null** | Model that may expose the relation.                            |
| `$property`  | **string**                               | Relation alias or property name to read.                       |
| `$keyMethod` | **string**                               | Method each related entity must expose to
provide the map key. |

**Return Value:**

Related entities keyed by their stable key.

**Throws:**

When a related entity is not an object or does not
implement the required key method.
- [`LogicException`](../Exception/LogicException.md)

***

## Inherited methods

### getUser

Return the effective user or original impersonating user.

```php
public getUser(bool $as = false, bool|null $force = null): \PhalconKit\Models\Interfaces\UserInterface|null
```

Unless `$force` is set, the method returns the cached instance for the
requested slot. A fresh lookup reads `userId` or `asUserId` from the
session identity payload and eager-loads role, group, and type relations
through the configured user model.

**Parameters:**

| Parameter | Type           | Description                                                           |
|-----------|----------------|-----------------------------------------------------------------------|
| `$as`     | **bool**       | Return the original impersonating user instead of the
effective user. |
| `$force`  | **bool\|null** | Force a fresh lookup instead of using the cached
model instance.      |

**Return Value:**

User model or null when no identity is stored.

***

### requireIdentityUser

Require the configured user model query to return the identity contract.

```php
protected requireIdentityUser(mixed $user): \PhalconKit\Models\Interfaces\UserInterface
```

The identity manager can resolve the user model from application
configuration, so the query result is a framework integration boundary.
This helper keeps `getUser()` focused on session/user selection while
failing clearly if the configured model does not implement the expected
PhalconKit user interface.

**Parameters:**

| Parameter | Type      | Description                                   |
|-----------|-----------|-----------------------------------------------|
| `$user`   | **mixed** | User record returned by the configured model. |

**Throws:**

When the configured user model does not return
the PhalconKit identity user contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### setUser

Cache the effective user for this manager instance.

```php
public setUser(\PhalconKit\Models\Interfaces\UserInterface|null $user): void
```

**Parameters:**

| Parameter | Type                                                  | Description                            |
|-----------|-------------------------------------------------------|----------------------------------------|
| `$user`   | **\PhalconKit\Models\Interfaces\UserInterface\|null** | User model or null to clear the cache. |

***

### getUserAs

Return the original user during impersonation.

```php
public getUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

Original user or null when not impersonating.

***

### setUserAs

Cache the original user for this manager instance.

```php
public setUserAs(\PhalconKit\Models\Interfaces\UserInterface|null $user): void
```

**Parameters:**

| Parameter | Type                                                  | Description                            |
|-----------|-------------------------------------------------------|----------------------------------------|
| `$user`   | **\PhalconKit\Models\Interfaces\UserInterface\|null** | User model or null to clear the cache. |

***

### getUserId

Return the effective or original user's id.

```php
public getUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                |
|-----------|----------|--------------------------------------------|
| `$as`     | **bool** | Return the original impersonating user id. |

**Return Value:**

User id or null when no matching user is logged in.

***

### getUserAsId

Return the original user's id during impersonation.

```php
public getUserAsId(): int|null
```

**Return Value:**

Original user id or null when not impersonating.

***

### getRoleList

Return roles associated with the current effective identity.

```php
public getRoleList(): array<string,object>
```

**Return Value:**

Role entities keyed by their stable key.

***

### getGroupList

Return groups associated with the current effective identity.

```php
public getGroupList(): array<string,object>
```

**Return Value:**

Group entities keyed by their stable key.

***

### getTypeList

Return types associated with the current effective identity.

```php
public getTypeList(): array<string,object>
```

**Return Value:**

Type entities keyed by their stable key.

***

### isLoggedIn

Check whether the effective or original user is logged in.

```php
public isLoggedIn(bool $as = false, bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                         |
|-----------|----------|-----------------------------------------------------|
| `$as`     | **bool** | Check the original impersonating user.              |
| `$force`  | **bool** | Force a fresh lookup instead of using cached users. |

**Return Value:**

True when a matching user model can be resolved.

***

### isLoggedInAs

Check whether the current session is impersonating another user.

```php
public isLoggedInAs(bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                |
|-----------|----------|--------------------------------------------|
| `$force`  | **bool** | Force a fresh lookup of the original user. |

**Return Value:**

True when `asUserId` resolves to a user.

***

### findUserById

Find a user by primary key through the configured user model.

```php
public findUserById(int $id): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$id`     | **int** | User id.    |

**Return Value:**

Matching user or null.

***

### findUserByEmail

Find a user by email through the configured user model.

```php
public findUserByEmail(string $string): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type       | Description    |
|-----------|------------|----------------|
| `$string` | **string** | Email address. |

**Return Value:**

Matching user or null.

***

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

### hasRole

Check whether the current identity has the requested roles.

```php
public hasRole(array<int,string>|null $roles = null, bool $or = false, bool $inherit = true): bool
```

When inheritance is enabled, configured parent roles are added to the
current role list before matching. With the legacy `$or` flag left at its
default, the method returns true when any requested role matches. Passing
`true` requires every requested role to match at the current level.

**Parameters:**

| Parameter  | Type                        | Description                                                           |
|------------|-----------------------------|-----------------------------------------------------------------------|
| `$roles`   | **array<int,string>\|null** | Role names to check.                                                  |
| `$or`      | **bool**                    | Legacy mode flag; `false` means any-match and `true`
means all-match. |
| `$inherit` | **bool**                    | Include roles inherited through configuration.                        |

**Return Value:**

True if the user satisfies the role conditions, false otherwise.

***

### has

Match one or more values against a haystack.

```php
public has(array<int,mixed>|string|null $needles = null, array<int,string> $haystack = [], bool $or = false): bool
```

At the current level, the legacy `$or` flag behaves as follows:
`false` returns true when any needle matches, and `true` returns true only
when every needle matches. Each nested array flips the mode for that
nested group, enabling expressions such as "all of these groups, where
each group may contain any of these roles".

Examples:

$this->has(['dev', 'admin'], $roles); // 'dev' OR 'admin'
$this->has(['dev', 'admin'], $roles, true); // 'dev' AND 'admin'
$this->has([['dev', 'admin']], $roles, true); // ('dev' OR 'admin')

**Parameters:**

| Parameter   | Type                               | Description                                                                                |
|-------------|------------------------------------|--------------------------------------------------------------------------------------------|
| `$needles`  | **array<int,mixed>\|string\|null** | Values or nested groups to
match.                                                          |
| `$haystack` | **array<int,string>**              | Values available to match against.                                                         |
| `$or`       | **bool**                           | Legacy mode flag; `false` means any-match and `true`
means all-match at the current level. |

**Return Value:**

True when the expression matches the haystack.

***

### getInheritedRoleList

Resolve inherited roles from the permissions configuration.

```php
public getInheritedRoleList(array<int,string> $roleIndexList = []): array<int,string>
```

The method walks `permissions.roles.<role>.inherit` recursively, avoids
re-processing roles it has already inspected, and returns a de-duplicated
list. When no base or inherited role is present, `guest` is added. The
universal `everyone` role is always included.

**Parameters:**

| Parameter        | Type                  | Description                 |
|------------------|-----------------------|-----------------------------|
| `$roleIndexList` | **array<int,string>** | Base role names to resolve. |

**Return Value:**

Unique inherited role names.

***

### oauth2

Create/update an OAuth2 identity and log in its linked local user.

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, string|null $refreshToken = null, array<string,mixed>|null $meta = []): array{saved: bool, loggedIn: bool, loggedInAs: bool, messages: \Phalcon\Messages\Messages, jwt?: string, refreshToken?: string, refreshed?: bool}
```

If the provider identity is not linked yet and a local user is already
logged in, the provider identity is attached to that user. Otherwise the
saved provider identity must already contain a user id before login can
succeed.

**Parameters:**

| Parameter       | Type                          | Description                           |
|-----------------|-------------------------------|---------------------------------------|
| `$provider`     | **string**                    | Provider key.                         |
| `$providerUuid` | **string**                    | Stable provider-side user identifier. |
| `$accessToken`  | **string**                    | Provider access token.                |
| `$refreshToken` | **string\|null**              | Optional provider refresh token.      |
| `$meta`         | **array<string,mixed>\|null** | Optional provider profile data.       |

**Throws:**

When OAuth provider fields cannot be sanitized.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless token key
generation fails after a successful OAuth2 login.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails after a successful OAuth2 login.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

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

### loginAs

Switch the current session to another user.

```php
public loginAs(array<string,mixed> $params = []): array{messages?: \Phalcon\Messages\Messages, loggedIn: bool, loggedInAs: bool, jwt?: string, refreshToken?: string, refreshed?: bool}
```

The target `userId` must be present, numeric, and resolvable through the
configured user model. If the target id equals the current `asUserId`, the
method treats the request as a return-to-self action and restores the
original session.

**Parameters:**

| Parameter | Type                    | Description                     |
|-----------|-------------------------|---------------------------------|
| `$params` | **array<string,mixed>** | Parameters containing `userId`. |

**Throws:**

When stateless token key
generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### logoutAs

Restore the original user from an impersonated session.

```php
public logoutAs(): array{loggedIn: bool, loggedInAs: bool, jwt?: string, refreshToken?: string, refreshed?: bool}
```

If both `userId` and `asUserId` are present, the original id becomes the
effective `userId` and the impersonation marker is removed.

**Return Value:**

Login state after
the restore attempt.

**Throws:**

When stateless token key
generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### hasAclRole

Check whether the current identity has at least one (or all) of the given ACL roles.

```php
public hasAclRole(array|null $roles = null, bool $or = false): bool
```

This method evaluates the provided role names against the **effective ACL role set**
returned by

- **See:** \PhalconKit\Identity\Traits\getAclRoles(), not just the raw identity roles. As a result:

- Contextual roles such as `ws`, `cli`, and `everyone` are implicitly considered.
- The `guest` role may be present when no explicit identity roles exist.
- Inherited roles are already resolved and included.

Internally, this delegates to
- **See:** \PhalconKit\Identity\Traits\has(), comparing:
- the requested roles (`$roles`)
- against the keys of the computed ACL role map

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$roles`  | **array\|null** | List of role identifiers to test.
- `null` typically implies a truthy check against defaults,
  depending on {@see \PhalconKit\Identity\Traits\has()} semantics.      |
| `$or`     | **bool**        | Legacy matching mode passed to {@see \PhalconKit\Identity\Traits\has()}:
- `false` (default): at least one role must be present.
- `true`: all roles must be present. |

**Return Value:**

True if the role condition is satisfied, false otherwise.

***

### getAclRoles

Build and return the effective ACL role set for the current identity.

```php
public getAclRoles(array|null $roleList = null): array<string,\Phalcon\Acl\Role>
```

This method computes the **final, authoritative list of ACL roles** used by
permission checks. The resulting role set is not a direct reflection of the
identity’s stored roles; it is a **context-aware, normalized, and expanded**
role map that accounts for execution context and role inheritance.

Resolution rules, applied in order:

1. **Execution-context roles**
   - `ws` is added when running under a WebSocket bootstrap.
   - `cli` is added when running under a console/CLI bootstrap.

2. **Global role**
   - `everyone` is always added, regardless of identity state.

3. **Identity roles**
   - If `$roleList` is provided, it is treated as the authoritative base role list.
   - Otherwise, roles are derived from the current identity via `getRoleList()`.

4. **Guest fallback**
   - If no base roles are resolved, `guest` is added as the sole identity role.

5. **Inherited roles**
   - All roles implied by inheritance rules are automatically added.

The returned array is keyed by role name and contains instantiated ACL `Role`
objects, ensuring uniqueness and preventing duplicate role registration.

**Parameters:**

| Parameter   | Type            | Description                                                                                                                                           |
|-------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$roleList` | **array\|null** | Optional explicit list of base role identifiers.
When provided, it overrides identity-derived roles
but still participates in inheritance resolution. |

**Return Value:**

Map of role name to ACL Role instance representing
the complete effective ACL role set.

***

### __construct

Construct the object and initialize its options.

```php
public __construct(array<string,mixed>|null $options = null): mixed
```

**Parameters:**

| Parameter  | Type                          | Description                    |
|------------|-------------------------------|--------------------------------|
| `$options` | **array<string,mixed>\|null** | Defaults to capture and apply. |

***

### initializeOptions

Capture defaults, apply the current options, and run initialize().

```php
public initializeOptions(array<string,mixed>|null $options = null): void
```

**Parameters:**

| Parameter  | Type                          | Description                    |
|------------|-------------------------------|--------------------------------|
| `$options` | **array<string,mixed>\|null** | Defaults to capture and apply. |

***

### initialize

Optional hook called after options are initialized.

```php
public initialize(): void
```

Override this in classes that need to derive internal state from options
during construction.

***

### setOptions

Replace or merge the current option set.

```php
public setOptions(array<string,mixed> $options, bool $merge = false): void
```

Options intentionally use PHP's null-coalescing read semantics: a key
stored with a null value remains present in the raw option array, but


- **See:** \PhalconKit\Support\Options\getOption() returns the caller default and
- **See:** \PhalconKit\Support\Options\hasOption()
reports false for that key.

**Parameters:**

| Parameter  | Type                    | Description                                                       |
|------------|-------------------------|-------------------------------------------------------------------|
| `$options` | **array<string,mixed>** | Options to apply.                                                 |
| `$merge`   | **bool**                | Whether to merge into existing options instead of
replacing them. |

***

### getOptions

Return the current option set.

```php
public getOptions(): array<string,mixed>
```

***

### setOption

Store or replace one option value.

```php
public setOption(string $key, mixed $value = null, bool $merge = false): void
```

Passing null stores the key in the raw option array, but the key still
reads as missing through

- **See:** \PhalconKit\Support\Options\getOption() and
- **See:** \PhalconKit\Support\Options\hasOption(). This
preserves the historical contract where null means "fall back to the
caller default" while still allowing callers to inspect raw options.

**Parameters:**

| Parameter | Type       | Description                                                         |
|-----------|------------|---------------------------------------------------------------------|
| `$key`    | **string** |                                                                     |
| `$value`  | **mixed**  |                                                                     |
| `$merge`  | **bool**   | Whether to merge the key/value pair into the existing
option array. |

***

### getOption

Return one option value or a default when it is missing or null.

```php
public getOption(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description                                  |
|------------|------------|----------------------------------------------|
| `$key`     | **string** |                                              |
| `$default` | **mixed**  | Default returned when the option is not set. |

***

### hasOption

Return true when an option is present and not null.

```php
public hasOption(string $key): bool
```

This intentionally mirrors

- **See:** \PhalconKit\Support\Options\getOption() rather than
`array_key_exists()`: null-valued options are stored in the raw option
array but are treated as absent by the public lookup helpers.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### removeOption

Remove one option key when it exists in the raw option array.

```php
public removeOption(string $key): void
```

Removal uses `array_key_exists()` instead of `isset()` so callers can
delete a key even when it currently stores null.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### resetOptions

Restore current options to the initialized defaults.

```php
public resetOptions(): void
```

***

### clearOptions

Remove all current option values.

```php
public clearOptions(): void
```

***
