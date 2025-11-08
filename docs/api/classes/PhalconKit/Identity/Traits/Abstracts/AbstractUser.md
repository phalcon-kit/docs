
***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractUser`

## Methods

### getUser

```php
public getUser(bool $as = false, ?bool $force = null): ?\PhalconKit\Models\Interfaces\UserInterface
```

* This method is **abstract**.
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

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***
### getUserAs

```php
public getUserAs(): ?\PhalconKit\Models\Interfaces\UserInterface
```

* This method is **abstract**.
***
### setUserAs

```php
public setUserAs(?\PhalconKit\Models\Interfaces\UserInterface $user): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***
### getUserId

```php
public getUserId(bool $as = false): ?int
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***
### getUserAsId

```php
public getUserAsId(): ?int
```

* This method is **abstract**.
***
### getRoleList

```php
public getRoleList(): array
```

* This method is **abstract**.
***
### getGroupList

```php
public getGroupList(): array
```

* This method is **abstract**.
***
### getTypeList

```php
public getTypeList(): array
```

* This method is **abstract**.
***
### isLoggedIn

```php
public isLoggedIn(bool $as = false, bool $force = false): bool
```

* This method is **abstract**.
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

* This method is **abstract**.
**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$force`  | **bool** |             |

***
### findUserById

```php
public findUserById(int $id): ?\PhalconKit\Models\Interfaces\UserInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$id`     | **int** |             |

***
### findUserByEmail

```php
public findUserByEmail(string $string): ?\PhalconKit\Models\Interfaces\UserInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$string` | **string** |             |

***
