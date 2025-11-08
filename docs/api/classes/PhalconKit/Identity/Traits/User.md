
***

* Full name: `\PhalconKit\Identity\Traits\User`

## Properties

### user

Current/impersonated user instance

```php
protected ?\PhalconKit\Models\Interfaces\UserInterface $user
```

***
### userAs

Original user instance when impersonating

```php
protected ?\PhalconKit\Models\Interfaces\UserInterface $userAs
```

***

## Methods

### getUser

Return the current user or impersonated user object based on the session

```php
public getUser(bool $as = false, bool|null $force = null): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type           | Description                                                        |
|-----------|----------------|--------------------------------------------------------------------|
| `$as`     | **bool**       | Flag to indicate whether to get the user as another user           |
| `$force`  | **bool\|null** | Flag to indicate whether to force the retrieval of the user object |

**Return Value:**

The user object or null if session is not available

***
### setUser

Set the current user or impersonated user instance.

```php
public setUser(\PhalconKit\Models\Interfaces\UserInterface|null $user): void
```

**Parameters:**

| Parameter | Type                                                  | Description                                                 |
|-----------|-------------------------------------------------------|-------------------------------------------------------------|
| `$user`   | **\PhalconKit\Models\Interfaces\UserInterface\|null** | The user instance to set or null to unset the current user. |

***
### getUserAs

Retrieve the original user when impersonating

```php
public getUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

The user instance or null if not available.

***
### setUserAs

Set the original user instance when impersonating

```php
public setUserAs(\PhalconKit\Models\Interfaces\UserInterface|null $user): void
```

**Parameters:**

| Parameter | Type                                                  | Description                                 |
|-----------|-------------------------------------------------------|---------------------------------------------|
| `$user`   | **\PhalconKit\Models\Interfaces\UserInterface\|null** | The user instance to set, or null to unset. |

***
### getUserId

Retrieves the current/impersonated user or the original user ID.

```php
public getUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                                                                      |
|-----------|----------|--------------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Determines whether to retrieve the original user (true) or the current/impersonated one (false). |

**Return Value:**

Returns the user ID as an integer if available, or null if the user is not set.

***
### getUserAsId

Retrieves the original user ID when impersonating.

```php
public getUserAsId(): int|null
```

**Return Value:**

Returns the user ID as an integer if available, or null otherwise.

***
### getRoleList

Retrieves the list of roles associated with the current identity.

```php
public getRoleList(): array
```

**Return Value:**

Returns an array of roles. If no roles are set, returns an empty array.

***
### getGroupList

Retrieves the list of groups associated with the current identity.

```php
public getGroupList(): array
```

**Return Value:**

Returns an array of group identifiers or an empty array if no groups are found.

***
### getTypeList

Retrieves the list of types associated with the current identity.

```php
public getTypeList(): array
```

**Return Value:**

Returns an array of types. If no types are found, returns an empty array.

***
### isLoggedIn

Checks if the user is currently logged in.

```php
public isLoggedIn(bool $as = false, bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                                                                   |
|-----------|----------|-----------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Determines whether to check the original user (true) or the current/impersonated one (false). |
| `$force`  | **bool** | Forces a fresh check ignoring cached user session data when set to true.                      |

**Return Value:**

Returns true if the user is logged in, false otherwise.

***
### isLoggedInAs

Checks if the user is logged in and impersonating another user.

```php
public isLoggedInAs(bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                           |
|-----------|----------|-------------------------------------------------------|
| `$force`  | **bool** | Determines whether to enforce a specific login check. |

**Return Value:**

Returns true if the user is logged in based on the condition, otherwise false.

***
### findUserById

Finds and retrieves a user by their unique identifier.

```php
public findUserById(int $id): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type    | Description                                        |
|-----------|---------|----------------------------------------------------|
| `$id`     | **int** | The unique identifier of the user to be retrieved. |

**Return Value:**

Returns the user instance if found, or null if no user exists with the specified identifier.

***
### findUserByEmail

Finds and retrieves a user by their email address.

```php
public findUserByEmail(string $string): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type       | Description                                  |
|-----------|------------|----------------------------------------------|
| `$string` | **string** | The email address of the user to search for. |

**Return Value:**

Returns a UserInterface instance if a user with the specified email is found, or null if no user matches the email.

***
