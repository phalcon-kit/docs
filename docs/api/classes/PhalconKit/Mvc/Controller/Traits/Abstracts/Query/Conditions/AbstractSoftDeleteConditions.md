
Abstract contract for soft-delete query conditions.

Soft-delete conditions are responsible for excluding
logically deleted records from query results.

CONDITION CONTRACT
------------------
Implementations MUST return:

 - null        → no soft-delete constraint applied
 - array       → [sql, bindValues, bindTypes]

The query compiler depends on this behavior strictly.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions\AbstractSoftDeleteConditions`

## Methods

### initializeSoftDeleteConditions

Initialize soft-delete conditions.

```php
public initializeSoftDeleteConditions(): void
```

Called during controller / query bootstrap.

* This method is **abstract**.
***
### setSoftDeleteConditions

Replace the soft-delete condition collection.

```php
public setSoftDeleteConditions(array|\Phalcon\Support\Collection|null $softDeleteConditions): void
```

* This method is **abstract**.
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

* This method is **abstract**.
***
### buildDefaultSoftDeleteCondition

Build the default soft-delete condition.

```php
public buildDefaultSoftDeleteCondition(): array|null
```

* This method is **abstract**.
**Return Value:**

Soft-delete condition payload

***
### getSoftDeleteColumn

Return the column used to mark deleted records.

```php
public getSoftDeleteColumn(): ?string
```

Returning null MUST disable soft-delete filtering.

* This method is **abstract**.
***
### getSoftDeleteActiveValue

Return the value representing a non-deleted record.

```php
public getSoftDeleteActiveValue(): int
```

Example:
- 0 (boolean flag)
- null (nullable timestamp strategies may override logic)

* This method is **abstract**.
***
