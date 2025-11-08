
***

* Full name: `\PhalconKit\Identity\Traits\Role`

## Methods

### hasRole

Determines if the current user has the specified roles.

```php
public hasRole(array|null $roles = null, bool $or = false, bool $inherit = true): bool
```

**Parameters:**

| Parameter  | Type            | Description                                                                                            |
|------------|-----------------|--------------------------------------------------------------------------------------------------------|
| `$roles`   | **array\|null** | List of roles to check against.                                                                        |
| `$or`      | **bool**        | If true, checks if the user has at least one of the roles. If false, checks if the user has all roles. |
| `$inherit` | **bool**        | If true, includes inherited roles in the check.                                                        |

**Return Value:**

True if the user satisfies the role conditions, false otherwise.

***
### has

Check if the needles meet the haystack using nested arrays
Reversing ANDs and ORs within each nested subarray

```php
public has(array|string|null $needles = null, array $haystack = [], bool $or = false): bool
```

$this->has(['dev', 'admin'], $this->getUser()->getRoles(), true); // 'dev' OR 'admin'
$this->has(['dev', 'admin'], $this->getUser()->getRoles(), false); // 'dev' AND 'admin'

$this->has(['dev', 'admin'], $this->getUser()->getRoles()); // 'dev' AND 'admin'
$this->has([['dev', 'admin']], $this->getUser()->getRoles()); // 'dev' OR 'admin'
$this->has([[['dev', 'admin']]], $this->getUser()->getRoles()); // 'dev' AND 'admin'

**Parameters:**

| Parameter   | Type                    | Description                                              |
|-------------|-------------------------|----------------------------------------------------------|
| `$needles`  | **array\|string\|null** | Needles to match and meet the rules                      |
| `$haystack` | **array**               | Haystack array to search into                            |
| `$or`       | **bool**                | True to force with "OR" , false to force "AND" condition |

**Return Value:**

Return true or false if the needles rules are being met

***
### getInheritedRoleList

Retrieves a list of inherited roles based on the provided role indices.

```php
public getInheritedRoleList(array $roleIndexList = []): array
```

The method processes the given role indices, determines their inherited roles
recursively, and returns a unique and flattened list of all inherited roles.

**Parameters:**

| Parameter        | Type      | Description                                                                      |
|------------------|-----------|----------------------------------------------------------------------------------|
| `$roleIndexList` | **array** | The list of role indices to process for inheritance. Defaults to an empty array. |

**Return Value:**

An array containing the unique list of all inherited roles.

***
