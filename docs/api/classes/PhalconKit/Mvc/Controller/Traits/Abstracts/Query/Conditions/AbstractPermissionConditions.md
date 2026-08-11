
Abstract contract for permission-based query conditions.

This trait defines the minimum API required for any
permission condition provider participating in the
query compilation pipeline.

CONDITION CONTRACT
------------------
All permission condition builders MUST return:

 - null        → no restriction applied
 - array       → [sql, bindValues, bindTypes]

Any other return shape is considered invalid and
may break the query compiler.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions\AbstractPermissionConditions`

## Methods

### initializePermissionConditions

Initialize permission conditions.

```php
public initializePermissionConditions(): void
```

Called during controller / query bootstrap.

* This method is **abstract**.
***
### setPermissionConditions

Replace the permission condition collection.

```php
public setPermissionConditions(array|\Phalcon\Support\Collection|null $permissionConditions): void
```

* This method is **abstract**.
**Parameters:**

| Parameter               | Type                                         | Description |
|-------------------------|----------------------------------------------|-------------|
| `$permissionConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getPermissionConditions

Retrieve the registered permission conditions.

```php
public getPermissionConditions(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### buildDefaultPermissionCondition

Build the default permission condition.

```php
public buildDefaultPermissionCondition(): array|null
```

This method MUST be deterministic and side-effect free.

* This method is **abstract**.
**Return Value:**

Condition payload or null if unrestricted

***
### getCreatedByColumns

Return the list of ownership columns used to restrict access.

```php
public getCreatedByColumns(): array
```

Example:
- ['createdBy']
- ['ownerId', 'assignedTo']

* This method is **abstract**.
***
### getSuperRoles

Return the list of roles exempt from permission constraints.

```php
public getSuperRoles(): array
```

* This method is **abstract**.
***
