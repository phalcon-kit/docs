
Abstract contract for request-filter query conditions.

Implementations convert user-supplied filter trees into compiler-safe SQL,
bind values, and bind types. Filter conditions are distinct from permission
and identity conditions: they express client-requested narrowing only.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions\AbstractFilterConditions`

## Methods

### initializeFilterConditions

Initialize filter-condition definitions.

```php
public initializeFilterConditions(): void
```

* This method is **abstract**.
***
### setFilterConditions

Replace filter-condition definitions.

```php
public setFilterConditions(array|\Phalcon\Support\Collection|null $filterConditions): void
```

* This method is **abstract**.
**Parameters:**

| Parameter           | Type                                         | Description |
|---------------------|----------------------------------------------|-------------|
| `$filterConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getFilterConditions

Return filter-condition definitions.

```php
public getFilterConditions(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### defaultFilterCondition

Build the default request-filter condition.

```php
public defaultFilterCondition(array<string|int,mixed>|null $filters = null, array<string|int,mixed>|null $allowedFilters = null, string|null $aliasContext = null, bool $or = false, int $level = 0): array<string|int,mixed>|string|null
```

* This method is **abstract**.
**Parameters:**

| Parameter         | Type                               | Description                                                             |
|-------------------|------------------------------------|-------------------------------------------------------------------------|
| `$filters`        | **array<string\|int,mixed>\|null** | Filter tree. Null means
read request filters from the controller.       |
| `$allowedFilters` | **array<string\|int,mixed>\|null** | Allowed field map.
Null means use the controller's filter-field policy. |
| `$aliasContext`   | **string\|null**                   | Optional alias context for nested joins.                                |
| `$or`             | **bool**                           | Whether the current filter level uses OR semantics.                     |
| `$level`          | **int**                            | Current nesting level.                                                  |

**Return Value:**

Compiler-safe condition.

***
### normalizeFilterOperator

Normalize a filter operator alias to the compiler's canonical operator.

```php
public normalizeFilterOperator(string $operator): string
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$operator` | **string** |             |

***
### getBindTypeFromRawValue

Infer the Phalcon bind type for a raw filter value.

```php
public getBindTypeFromRawValue(mixed $rawValue = null): int
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type      | Description |
|-------------|-----------|-------------|
| `$rawValue` | **mixed** |             |

***
