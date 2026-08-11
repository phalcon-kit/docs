
Soft-delete query condition provider.

PURPOSE
-------
This trait enforces soft-delete semantics at the query level
by excluding records marked as deleted.

It does NOT:
 - Perform delete operations
 - Decide whether soft-delete is enabled globally
 - Infer delete state implicitly

CONDITION CONTRACT
------------------
 - null  → no soft-delete constraint applied
 - array → [sql, bindValues, bindTypes]

The compiler relies on this contract strictly.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\SoftDeleteConditions`

## Properties

### softDeleteConditions

Registered soft-delete condition sets.

```php
protected ?\Phalcon\Support\Collection $softDeleteConditions
```

Allows consumers to:
- Disable soft delete
- Replace default behavior
- Introduce advanced delete semantics

***

## Methods

### initializeSoftDeleteConditions

Initialize soft-delete conditions.

```php
public initializeSoftDeleteConditions(): void
```

Called during controller / query bootstrap.
Always registers a `default` condition, which may resolve to null.

***
### setSoftDeleteConditions

Replace the soft-delete condition collection.

```php
public setSoftDeleteConditions(array|\Phalcon\Support\Collection|null $softDeleteConditions): void
```

**Parameters:**

| Parameter               | Type                                         | Description |
|-------------------------|----------------------------------------------|-------------|
| `$softDeleteConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getSoftDeleteConditions

Retrieve the registered soft-delete conditions.

```php
public getSoftDeleteConditions(): ?\Phalcon\Support\Collection
```

***
### buildDefaultSoftDeleteCondition

Build the default soft-delete condition.

```php
public buildDefaultSoftDeleteCondition(): array|null
```

DEFAULT STRATEGY
----------------
 - Column: `deleted`
 - Value:  0
 - Comparison: strict equality

This assumes:
 - 0 = not deleted
 - 1 = deleted

Override this method for:
 - nullable soft delete
 - timestamp-based delete
 - multi-state delete flags

**Return Value:**

Soft-delete condition payload

***
### getSoftDeleteColumn

Return the column used to mark deleted records.

```php
public getSoftDeleteColumn(): ?string
```

Returning null disables soft-delete constraints entirely.

***
### getSoftDeleteActiveValue

Return the value representing a non-deleted record.

```php
public getSoftDeleteActiveValue(): int
```

Default:
- 0 → active

***
