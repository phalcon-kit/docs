
This trait provides methods for managing permission conditions for the query.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\PermissionConditions`

## Properties

### permissionConditions

Holds the permission conditions collection.

```php
protected \Phalcon\Support\Collection|null $permissionConditions
```

This variable stores the permission conditions in an associative array format. Each key represents a permission,
and the corresponding value represents the conditions associated with that permission. The conditions can be
nested within sub-arrays to handle complex permission structures.

***

## Methods

### initializePermissionConditions

Initializes the permission conditions for the object.

```php
public initializePermissionConditions(): void
```

Sets the permission conditions using a new instance of Collection class.
The default permission condition is set using the defaultPermissionCondition method.

***
### setPermissionConditions

Sets the permission conditions for the current user's identity and role.

```php
public setPermissionConditions(\Phalcon\Support\Collection|null $permissionConditions): void
```

**Parameters:**

| Parameter               | Type                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$permissionConditions` | **\Phalcon\Support\Collection\|null** | The permission conditions to be set. Pass null if no conditions are required.
A Collection object that contains the permission conditions.
Each permission condition is expected to be an array with the following elements:
- The condition string formed by joining the columns with 'or' operators.
- An array of bind values for the condition.
- An array of bind types for the condition.
Example: [
    'column1 = :value1:',
    ['value1' => 'some value'],
    ['value1' => Column::BIND_PARAM_STR],
] |

***
### getPermissionConditions

Retrieves the collection of permission conditions.

```php
public getPermissionConditions(): \Phalcon\Support\Collection|null
```

**Return Value:**

Returns the collection of permission conditions, or null if it is not set.

***
### defaultPermissionCondition

Builds the permission condition based on the current user's identity and role.

```php
public defaultPermissionCondition(): array|string|null
```

**Return Value:**

Returns an array with the following elements:
- If permission columns are empty, returns null.
- If no permission is found, returns ['false'].
- If the current user role is a super admin, returns ['true'].
- If permission conditions are found, returns an array with the following elements:
  - The condition string formed by joining the columns with 'or' operators.
  - An array of bind values for the condition.
  - An array of bind types for the condition.

***
### getCreatedByColumns

Retrieves the owner id columns of the current model.

```php
public getCreatedByColumns(): array
```

**Return Value:**

Returns an array of strings representing the column names containing the "created by" information.

***
### getSuperRoles

Retrieves the list of super admins roles.

```php
public getSuperRoles(): array
```

These roles are authorized through the Permission Conditions

**Return Value:**

The list of super roles, which by default includes 'dev' and 'admin'.

***
