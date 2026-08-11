
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\FilterFields`

## Properties

### filterFields

Controller-owned filter-field policy.

```php
protected ?\Phalcon\Support\Collection $filterFields
```

Null means unrestricted filtering and preserves legacy controller
behavior. A non-null collection enables allow-list mode; an empty
collection is therefore a closed policy that rejects every client filter.

***

## Methods

### initializeFilterFields

Initialize the filter-field allow-list.

```php
public initializeFilterFields(): void
```

Concrete controllers can override this method and call


- **See:** \PhalconKit\Mvc\Controller\Traits\Query\Fields\setFilterFields() to define which fields the public `filter`
request parameter may target. The default is null so existing resources
keep accepting any normalized field until they opt in to restrictions.

***
### setFilterFields

Replace the fields clients may use in the REST `filter` parameter.

```php
public setFilterFields(array|\Phalcon\Support\Collection|null $filterFields): void
```

Supported collection shapes follow the filter compiler contract and may
include nested arrays for relation-aware filters. Passing null disables
allow-list enforcement; passing an empty collection keeps allow-list mode
active but allows no client-supplied filters.

**Parameters:**

| Parameter       | Type                                         | Description |
|-----------------|----------------------------------------------|-------------|
| `$filterFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getFilterFields

Return the configured filter-field policy.

```php
public getFilterFields(): ?\Phalcon\Support\Collection
```

A null return value means unrestricted filtering. A non-null collection is
consumed by the filter condition builder before client filters are
accepted.

***
### hasFilterFields

Check whether filter-field allow-list mode is configured.

```php
public hasFilterFields(): bool
```

This reports policy presence, not whether at least one field is enabled.
An empty collection still means filtering is intentionally closed.

***
### mergeFilterFields

Merge additional filter-field entries into the current policy.

```php
public mergeFilterFields(array|\Phalcon\Support\Collection $filterFields): void
```

Merge semantics are centralized in

- **See:** \PhalconKit\Support\CollectionPolicy: null starts
from the incoming collection, empty incoming collections leave an existing
policy unchanged, and associative keys can override previous entries.

**Parameters:**

| Parameter       | Type                                   | Description |
|-----------------|----------------------------------------|-------------|
| `$filterFields` | **array\|\Phalcon\Support\Collection** |             |

***
