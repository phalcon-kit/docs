
Resolves identity users from the configured user model.

The trait keeps separate cached instances for the effective user and the
original impersonating user. It reads only lightweight ids from the identity
session payload, then loads full user records with role, group, and type
relations for downstream ACL and API payloads.

***

* Full name: `\PhalconKit\Identity\Traits\User`

## Properties

### user

Effective user for the current request.

```php
protected ?\PhalconKit\Models\Interfaces\UserInterface $user
```

***
### userAs

Original user when the current request is impersonating another user.

```php
protected ?\PhalconKit\Models\Interfaces\UserInterface $userAs
```

***

## Methods

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
- [`ServiceException`](../../Exception/ServiceException.md)

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
