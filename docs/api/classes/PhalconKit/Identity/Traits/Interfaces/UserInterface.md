
***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\UserInterface`

## Methods

### getUser

```php
public getUser(bool $as = false, ?bool $force = null): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$as`     | **bool**  |             |
| `$force`  | **?bool** |             |

***

### setUser

```php
public setUser(?\PhalconKit\Models\Interfaces\UserInterface $user): void
```

**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***

### getUserAs

```php
public getUserAs(): ?\PhalconKit\Models\Interfaces\UserInterface
```

***

### setUserAs

```php
public setUserAs(?\PhalconKit\Models\Interfaces\UserInterface $user): void
```

**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***

### getUserId

```php
public getUserId(bool $as = false): ?int
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### getUserAsId

```php
public getUserAsId(): ?int
```

***

### getRoleList

```php
public getRoleList(): array
```

***

### getGroupList

```php
public getGroupList(): array
```

***

### getTypeList

```php
public getTypeList(): array
```

***

### isLoggedIn

```php
public isLoggedIn(bool $as = false, bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |
| `$force`  | **bool** |             |

***

### isLoggedInAs

```php
public isLoggedInAs(bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$force`  | **bool** |             |

***

### findUserById

```php
public findUserById(int $id): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$id`     | **int** |             |

***

### findUserByEmail

```php
public findUserByEmail(string $string): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$string` | **string** |             |

***
