
Declares role matching methods required by ACL and impersonation helpers.

The role API keeps its legacy `$or` parameter for compatibility even though
the current behavior treats `false` as any-match and `true` as all-match at
the current nesting level.

***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractRole`

## Methods

### hasRole

```php
public hasRole(array<int,string>|null $roles = null, bool $or = false, bool $inherit = true): bool
```

* This method is **abstract**.
**Parameters:**

| Parameter  | Type                        | Description |
|------------|-----------------------------|-------------|
| `$roles`   | **array<int,string>\|null** |             |
| `$or`      | **bool**                    |             |
| `$inherit` | **bool**                    |             |

***
### has

```php
public has(array<int,mixed>|string|null $needles = null, array<int,string> $haystack = [], bool $or = false): bool
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type                               | Description |
|-------------|------------------------------------|-------------|
| `$needles`  | **array<int,mixed>\|string\|null** |             |
| `$haystack` | **array<int,string>**              |             |
| `$or`       | **bool**                           |             |

***
### getInheritedRoleList

```php
public getInheritedRoleList(array<int,string> $roleIndexList = []): array<int,string>
```

* This method is **abstract**.
**Parameters:**

| Parameter        | Type                  | Description |
|------------------|-----------------------|-------------|
| `$roleIndexList` | **array<int,string>** |             |

***
