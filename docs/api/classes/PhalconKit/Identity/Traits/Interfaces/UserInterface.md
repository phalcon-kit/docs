
Contract for resolving the effective and impersonating identity users.

***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\UserInterface`

## Methods

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
