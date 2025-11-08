
***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\RoleInterface`

## Methods

### hasRole

```php
public hasRole(?array $roles = null, bool $or = false, bool $inherit = true): bool
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$roles`   | **?array** |             |
| `$or`      | **bool**   |             |
| `$inherit` | **bool**   |             |

***

### has

```php
public has(array|string|null $needles = null, array $haystack = [], bool $or = false): bool
```

**Parameters:**

| Parameter   | Type                    | Description |
|-------------|-------------------------|-------------|
| `$needles`  | **array\|string\|null** |             |
| `$haystack` | **array**               |             |
| `$or`       | **bool**                |             |

***

### getInheritedRoleList

```php
public getInheritedRoleList(array $roleIndexList = []): array
```

**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$roleIndexList` | **array** |             |

***
