
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\IdentityInterface`

## Methods

### getIdentityService

```php
public getIdentityService(): \PhalconKit\Identity\Manager
```

***

### isLoggedIn

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### isLoggedInAs

```php
public isLoggedInAs(): bool
```

***

### getCurrentUser

```php
public getCurrentUser(bool $as = false): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### getCurrentUserAs

```php
public getCurrentUserAs(): ?\PhalconKit\Models\Interfaces\UserInterface
```

***

### getCurrentUserId

```php
public getCurrentUserId(bool $as = false): ?int
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### getCurrentUserIdCallback

```php
public getCurrentUserIdCallback(bool $as = false): \Closure
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***
