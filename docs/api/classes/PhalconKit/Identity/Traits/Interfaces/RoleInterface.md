
Contract for role matching and configured role inheritance.

***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\RoleInterface`

## Methods

### hasRole

Check whether the current identity matches requested roles.

```php
public hasRole(array<int,string>|null $roles = null, bool $or = false, bool $inherit = true): bool
```

The legacy `$or` parameter name is misleading: `false` checks whether any
requested role matches, while `true` requires every requested role to
match. The parameter is kept for compatibility.

**Parameters:**

| Parameter  | Type                        | Description                                                                             |
|------------|-----------------------------|-----------------------------------------------------------------------------------------|
| `$roles`   | **array<int,string>\|null** | Role names to test.                                                                     |
| `$or`      | **bool**                    | Legacy mode flag; `false` means any-match, `true` means
all-match at the current level. |
| `$inherit` | **bool**                    | Include configured inherited roles.                                                     |

***

### has

Match one or more values against a haystack.

```php
public has(array<int,mixed>|string|null $needles = null, array<int,string> $haystack = [], bool $or = false): bool
```

Nested arrays flip the current matching mode, allowing callers to express
alternating any/all groups without a separate expression object.

**Parameters:**

| Parameter   | Type                               | Description                                                                             |
|-------------|------------------------------------|-----------------------------------------------------------------------------------------|
| `$needles`  | **array<int,mixed>\|string\|null** | Values or nested groups to
match.                                                       |
| `$haystack` | **array<int,string>**              | Available values.                                                                       |
| `$or`       | **bool**                           | Legacy mode flag; `false` means any-match, `true` means
all-match at the current level. |

***

### getInheritedRoleList

Resolve configured inherited roles for the provided base roles.

```php
public getInheritedRoleList(array<int,string> $roleIndexList = []): array<int,string>
```

**Parameters:**

| Parameter        | Type                  | Description      |
|------------------|-----------------------|------------------|
| `$roleIndexList` | **array<int,string>** | Base role names. |

***
