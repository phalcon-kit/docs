
Abstract contract for search-based query conditions.

This trait defines the public API exposed by any
search condition provider.

CONDITION CONTRACT
------------------
All search condition builders MUST return:

 - null        → no search restriction applied
 - array       → [sql, bindValues, bindTypes]

AND / OR semantics are the responsibility of the
implementing trait.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions\AbstractSearchConditions`

## Methods

### initializeSearchConditions

Initialize search conditions.

```php
public initializeSearchConditions(): void
```

* This method is **abstract**.
***
### setSearchConditions

Replace the search condition collection.

```php
public setSearchConditions(array|\Phalcon\Support\Collection|null $searchConditions): void
```

* This method is **abstract**.
**Parameters:**

| Parameter           | Type                                         | Description |
|---------------------|----------------------------------------------|-------------|
| `$searchConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getSearchConditions

Retrieve the registered search conditions.

```php
public getSearchConditions(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### buildDefaultSearchCondition

Build the default search condition.

```php
public buildDefaultSearchCondition(): array|null
```

This method is expected to:
- Normalize user input
- Apply AND / OR grouping
- Return a compiler-safe payload

* This method is **abstract**.
**Return Value:**

Condition payload or null if no search applied

***
### extractSearchTerms

Extract normalized search terms from input.

```php
public extractSearchTerms(): string[]
```

Exposed publicly for reuse and testability.

* This method is **abstract**.
***
### buildSearchTermGroup

Build an OR-group for a single search term.

```php
public buildSearchTermGroup(string $term, array $searchFields, array& $bind, array& $bindTypes): string[]
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$term`         | **string** |             |
| `$searchFields` | **array**  |             |
| `$bind`         | **array**  |             |
| `$bindTypes`    | **array**  |             |

***
