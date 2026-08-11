
Provides role matching and configured role inheritance.

The public methods keep the historical `$or` parameter name for compatibility.
In practice the flag controls the current matching level: `false` performs an
any-match check and `true` performs an all-match check. Nested arrays flip
the mode, which lets callers express simple alternating role expressions
without introducing a separate parser.

***

* Full name: `\PhalconKit\Identity\Traits\Role`

## Methods

### hasRole

Check whether the current identity has the requested roles.

```php
public hasRole(array<int,string>|null $roles = null, bool $or = false, bool $inherit = true): bool
```

When inheritance is enabled, configured parent roles are added to the
current role list before matching. With the legacy `$or` flag left at its
default, the method returns true when any requested role matches. Passing
`true` requires every requested role to match at the current level.

**Parameters:**

| Parameter  | Type                        | Description                                                           |
|------------|-----------------------------|-----------------------------------------------------------------------|
| `$roles`   | **array<int,string>\|null** | Role names to check.                                                  |
| `$or`      | **bool**                    | Legacy mode flag; `false` means any-match and `true`
means all-match. |
| `$inherit` | **bool**                    | Include roles inherited through configuration.                        |

**Return Value:**

True if the user satisfies the role conditions, false otherwise.

***
### has

Match one or more values against a haystack.

```php
public has(array<int,mixed>|string|null $needles = null, array<int,string> $haystack = [], bool $or = false): bool
```

At the current level, the legacy `$or` flag behaves as follows:
`false` returns true when any needle matches, and `true` returns true only
when every needle matches. Each nested array flips the mode for that
nested group, enabling expressions such as "all of these groups, where
each group may contain any of these roles".

Examples:

$this->has(['dev', 'admin'], $roles); // 'dev' OR 'admin'
$this->has(['dev', 'admin'], $roles, true); // 'dev' AND 'admin'
$this->has([['dev', 'admin']], $roles, true); // ('dev' OR 'admin')

**Parameters:**

| Parameter   | Type                               | Description                                                                                |
|-------------|------------------------------------|--------------------------------------------------------------------------------------------|
| `$needles`  | **array<int,mixed>\|string\|null** | Values or nested groups to
match.                                                          |
| `$haystack` | **array<int,string>**              | Values available to match against.                                                         |
| `$or`       | **bool**                           | Legacy mode flag; `false` means any-match and `true`
means all-match at the current level. |

**Return Value:**

True when the expression matches the haystack.

***
### getInheritedRoleList

Resolve inherited roles from the permissions configuration.

```php
public getInheritedRoleList(array<int,string> $roleIndexList = []): array<int,string>
```

The method walks `permissions.roles.<role>.inherit` recursively, avoids
re-processing roles it has already inspected, and returns a de-duplicated
list. When no base or inherited role is present, `guest` is added. The
universal `everyone` role is always included.

**Parameters:**

| Parameter        | Type                  | Description                 |
|------------------|-----------------------|-----------------------------|
| `$roleIndexList` | **array<int,string>** | Base role names to resolve. |

**Return Value:**

Unique inherited role names.

***
