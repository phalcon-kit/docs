
Provides model-level access to the current PhalconKit identity service.

The trait is used by attribution behaviors and application models that need
the current user or delegated user while handling model lifecycle events. It
resolves the identity manager from the model DI so tests and applications can
replace the identity service through normal container configuration.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Identity`

## Methods

### getIdentityService

Resolve the current identity manager from the model DI.

```php
public getIdentityService(): \PhalconKit\Identity\ManagerInterface
```

The service must implement `PhalconKit\Identity\ManagerInterface`; this
allows applications to provide custom identity managers without extending
the concrete core manager class.

**Return Value:**

Current identity manager service.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### isLoggedIn

Check whether the current identity is logged in.

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                                                          |
|-----------|----------|--------------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, checks delegated/impersonated identity state
instead of the primary user. |

**Return Value:**

True when the requested identity state is authenticated.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### isLoggedInAs

Check whether the current identity is acting as another user.

```php
public isLoggedInAs(): bool
```

**Return Value:**

True when a delegated/impersonated user is active.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getCurrentUser

Return the current user model from the identity service.

```php
public getCurrentUser(bool $as = false): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type     | Description                                                                     |
|-----------|----------|---------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user
instead of the primary user. |

**Return Value:**

Current user, delegated user, or null when no
matching identity is available.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getCurrentUserAs

Return the delegated user model from the identity service.

```php
public getCurrentUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

Delegated/impersonated user, or null when no
delegated identity is active.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getCurrentUserId

Return the integer ID of the current or delegated user.

```php
public getCurrentUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                                                           |
|-----------|----------|---------------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user ID
instead of the primary user ID. |

**Return Value:**

User ID cast to int, or null when no user is available
or the user does not expose an ID.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getCurrentUserIdCallback

Build a callback that returns the current or delegated user ID.

```php
public getCurrentUserIdCallback(bool $as = false): callable
```

Behaviors can store this closure and evaluate it later during lifecycle
events, ensuring they use the identity state at execution time rather
than initialization time.

**Parameters:**

| Parameter | Type     | Description                                             |
|-----------|----------|---------------------------------------------------------|
| `$as`     | **bool** | When true, the callback resolves the delegated user ID. |

**Return Value:**

Callback returning the requested user ID or null.

***
