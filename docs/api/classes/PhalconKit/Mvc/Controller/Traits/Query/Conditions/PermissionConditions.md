
Permission-based query condition provider.

This trait is responsible for producing **row-level access constraints**
based on the current authenticated identity.

Design contract:
 - Returning `null` means: *no restriction applied*
 - Returning an array means: *AND-applicable condition payload*

Condition payload shape:
 [
     0 => string  $conditionSql,
     1 => array   $bindValues,
     2 => array   $bindTypes,
 ]

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\PermissionConditions`

## Properties

### permissionConditions

Registered permission condition sets.

```php
protected ?\Phalcon\Support\Collection $permissionConditions
```

Keys are symbolic names (e.g. "default", "custom"),
values are condition payloads or callables producing them.

***

## Methods

### initializePermissionConditions

Initialize permission conditions.

```php
public initializePermissionConditions(): void
```

Called during controller / query bootstrap.

***
### setPermissionConditions

Replace the permission condition collection.

```php
public setPermissionConditions(array|\Phalcon\Support\Collection|null $permissionConditions): void
```

**Parameters:**

| Parameter               | Type                                         | Description |
|-------------------------|----------------------------------------------|-------------|
| `$permissionConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getPermissionConditions

Retrieve the permission condition collection.

```php
public getPermissionConditions(): ?\Phalcon\Support\Collection
```

***
### buildDefaultPermissionCondition

Build the default permission condition.

```php
public buildDefaultPermissionCondition(): ?array
```

Rules:
- No identity → no restriction
- Super roles → no restriction
- No owner columns → no restriction
- Otherwise → owner-based OR condition

***
### buildOwnerCondition

Build an owner-based permission condition.

```php
public buildOwnerCondition(int $userId, array $columns): array|null
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$userId`  | **int**   |             |
| `$columns` | **array** |             |

***
### getCreatedByColumns

Columns used to assert record ownership.

```php
public getCreatedByColumns(): array
```

Override per-model when ownership differs.

***
### getSuperRoles

Roles exempt from permission constraints.

```php
public getSuperRoles(): array
```

***
