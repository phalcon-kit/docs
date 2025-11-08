
This trait provides convenient methods for managing user identity and authentication within a model.

It encapsulates the logic related to user authentication and session management,
making it easier to reuse and maintain in different models.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Identity`

## Methods

### getIdentityService

Get the current identity service from the DI

```php
public getIdentityService(): \PhalconKit\Identity\Manager
```

***
### isLoggedIn

Check if a user is logged in

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                               |
|-----------|----------|-----------------------------------------------------------|
| `$as`     | **bool** | Optional parameter to specify the identity state to check |

**Return Value:**

Returns true if the user is logged in, false otherwise

***
### isLoggedInAs

Check if the user is logged in as another user.

```php
public isLoggedInAs(): bool
```

**Return Value:**

True if the user is logged in as another user, false otherwise.

***
### getCurrentUser

Get the current user.

```php
public getCurrentUser(bool $as = false): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type     | Description                                                 |
|-----------|----------|-------------------------------------------------------------|
| `$as`     | **bool** | If true, return the UserInterface object. Default is false. |

**Return Value:**

Returns the current user as a UserInterface object if $as is true.
Returns null if there is no current user or the user is not found.

***
### getCurrentUserAs

Get the current delegated UserInterface object

```php
public getCurrentUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

The current user as UserInterface if available, null otherwise

***
### getCurrentUserId

Retrieves the ID of the currently logged-in user.

```php
public getCurrentUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                                                                                                                                                             |
|-----------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Optional flag indicating whether to retrieve the user as well.
If set to true, the complete user object will be returned.
If set to false (default), only the user ID will be returned. |

**Return Value:**

If $as is true, it returns the ID of the currently logged-in user as an integer.
If $as is false, it returns null if there is no logged-in user or
the ID of the currently logged-in user as an integer.

***
### getCurrentUserIdCallback

Retrieves a callback function that returns the ID of the currently logged-in user.

```php
public getCurrentUserIdCallback(bool $as = false): \Closure
```

**Parameters:**

| Parameter | Type     | Description                                                                                                                                                                             |
|-----------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Optional flag indicating whether to retrieve the user as well.
If set to true, the complete user object will be returned.
If set to false (default), only the user ID will be returned. |

**Return Value:**

A callback function that, when invoked, returns the ID of the currently logged-in user.
The returned ID will be null if there is no logged-in user or an integer if the user is logged in.

***
