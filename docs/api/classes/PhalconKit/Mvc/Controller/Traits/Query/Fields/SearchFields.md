
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\SearchFields`

## Properties

### searchFields

Controller-owned search-field policy.

```php
protected ?\Phalcon\Support\Collection $searchFields
```

Null means the search condition builder has no configured field list and
will not add a search predicate. A non-null collection defines the fields
considered by the public `search` request parameter.

***

## Methods

### initializeSearchFields

Initialize the full-text-like search field list.

```php
public initializeSearchFields(): void
```

Concrete controllers should override this method and call


- **See:** \PhalconKit\Mvc\Controller\Traits\Query\Fields\setSearchFields() when a resource supports request-driven search.
The default is null so search stays disabled unless a controller defines
an explicit set of searchable fields.

***
### setSearchFields

Replace the fields used by the REST `search` parameter.

```php
public setSearchFields(array|\Phalcon\Support\Collection|null $searchFields): void
```

Passing null disables search field configuration. Passing an empty
collection keeps the policy explicit but gives the search builder no
fields to compile.

**Parameters:**

| Parameter       | Type                                         | Description |
|-----------------|----------------------------------------------|-------------|
| `$searchFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getSearchFields

Return the configured search-field policy.

```php
public getSearchFields(): ?\Phalcon\Support\Collection
```

A null return value means no search fields have been configured. A
non-null collection is flattened by the search condition builder so nested
field definitions can participate in the generated predicate.

***
### hasSearchFields

Check whether search-field configuration is present.

```php
public hasSearchFields(): bool
```

This reports policy presence only. An empty collection still means the
controller made an explicit search-field decision.

***
### mergeSearchFields

Merge additional search-field entries into the current policy.

```php
public mergeSearchFields(array|\Phalcon\Support\Collection $searchFields): void
```

Merge semantics are centralized in

- **See:** \PhalconKit\Support\CollectionPolicy: null starts
from the incoming collection, empty incoming collections leave an existing
policy unchanged, and associative keys can override previous entries.

**Parameters:**

| Parameter       | Type                                   | Description |
|-----------------|----------------------------------------|-------------|
| `$searchFields` | **array\|\Phalcon\Support\Collection** |             |

***
