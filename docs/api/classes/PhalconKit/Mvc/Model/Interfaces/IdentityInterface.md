
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\IdentityInterface`

## Methods

### getIdentityService

Resolve the identity manager used by model identity helpers.

```php
public getIdentityService(): \PhalconKit\Identity\ManagerInterface
```

Implementations should resolve the service from the model DI and surface
missing or incompatible services as a PhalconKit service exception.

**Return Value:**

Identity manager used by the model helpers.

**Throws:**

When the service cannot be
resolved or does not implement the expected contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### isLoggedIn

Check whether the primary or delegated identity is authenticated.

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                                                              |
|-----------|----------|------------------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, checks delegated/impersonated identity state
instead of the primary identity. |

**Return Value:**

True when the selected identity is logged in.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### isLoggedInAs

Check whether a delegated/impersonated identity is active.

```php
public isLoggedInAs(): bool
```

**Return Value:**

True when the current identity is acting as another user.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### getCurrentUser

Return the current primary or delegated user.

```php
public getCurrentUser(bool $as = false): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type     | Description                                         |
|-----------|----------|-----------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user. |

**Return Value:**

Matching user model, or null when unavailable.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### getCurrentUserAs

Return the delegated/impersonated user model.

```php
public getCurrentUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

Delegated user, or null when no delegated
identity is active.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### getCurrentUserId

Return the current primary or delegated user ID.

```php
public getCurrentUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                            |
|-----------|----------|--------------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user ID. |

**Return Value:**

User ID, or null when no matching user is available.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### getCurrentUserIdCallback

Build a deferred callback for resolving the current user ID.

```php
public getCurrentUserIdCallback(bool $as = false): callable
```

Behaviors use this to evaluate identity state during model lifecycle
events instead of capturing a stale ID at initialization time.

**Parameters:**

| Parameter | Type     | Description                                             |
|-----------|----------|---------------------------------------------------------|
| `$as`     | **bool** | When true, the callback resolves the delegated user ID. |

**Return Value:**

Callback returning the selected user ID.

***
