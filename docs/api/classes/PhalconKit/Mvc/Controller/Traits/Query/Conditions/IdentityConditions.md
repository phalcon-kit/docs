
IdentityConditions

Responsibility:
 - Generate *identity-scoped* WHERE conditions based on runtime parameters
 - Constrain queries to a model’s identity columns (usually primary keys)

Design constraints:
 - Stateless builder: no side effects beyond stored Collection
 - Null-safe: absence of identity data yields no condition
 - PDO-safe: all values bound with generated placeholders

Output contract:
 - null → no identity constraint
 - [string, bind[], types[]] → Phalcon-compatible condition payload

This trait intentionally does NOT:
 - Perform authorization decisions
 - Infer identity values implicitly
 - Throw when identity data is missing

Consumers decide how absence of identity affects query semantics.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\IdentityConditions`

## Properties

### identityConditions

array\|Collection of named identity conditions.

```php
protected ?\Phalcon\Support\Collection $identityConditions
```

Shape:
[
    'default' => array|string|null
]

***

## Methods

### initializeIdentityConditions

Initializes identity conditions.

```php
public initializeIdentityConditions(): void
```

Called during controller/query bootstrap.
Always registers a `default` condition, which may resolve to null.

***
### setIdentityConditions

Explicit setter.

```php
public setIdentityConditions(array|\Phalcon\Support\Collection|null $identityConditions): void
```

Allows higher-level components to override identity semantics.

**Parameters:**

| Parameter             | Type                                         | Description |
|-----------------------|----------------------------------------------|-------------|
| `$identityConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getIdentityConditions

Returns the registered identity conditions collection.

```php
public getIdentityConditions(): ?\Phalcon\Support\Collection
```

***
### defaultIdentityCondition

Resolves the default identity condition.

```php
public defaultIdentityCondition(): array|string|null
```

Uses request/query parameters as the identity source.

***
### buildIdentityConditionFromData

Builds an identity condition from arbitrary data.

```php
public buildIdentityConditionFromData(array $data, array|null $columns = null): array|null
```

Algorithm:
 1. Resolve identity columns (defaults to primary key attributes)
 2. For each column:
    - Skip if missing or null in input data
    - Generate a unique bind placeholder
    - Append strict equality predicate
 3. AND-coalesce predicates

Failure modes:
 - No identity columns → null
 - No matching data provided → null

**Parameters:**

| Parameter  | Type            | Description                           |
|------------|-----------------|---------------------------------------|
| `$data`    | **array**       | Input data (typically request params) |
| `$columns` | **array\|null** | Explicit identity columns override    |

**Return Value:**


[
    string $condition,
    array $bind,
    array $bindTypes
]

***
### getIdentityColumns

Returns the identity columns for the current model.

```php
public getIdentityColumns(): array
```

Default strategy:
 - Use primary key attributes

Override point:
 - Models with composite or non-PK identity semantics

***
