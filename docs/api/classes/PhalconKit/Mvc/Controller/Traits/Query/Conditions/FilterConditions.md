
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\FilterConditions`

## Properties

### filterConditions

```php
protected ?\Phalcon\Support\Collection $filterConditions
```

***

## Methods

### initializeFilterConditions

```php
public initializeFilterConditions(): void
```

***
### setFilterConditions

```php
public setFilterConditions(?\Phalcon\Support\Collection $filterConditions): void
```

**Parameters:**

| Parameter           | Type                             | Description |
|---------------------|----------------------------------|-------------|
| `$filterConditions` | **?\Phalcon\Support\Collection** |             |

***
### getFilterConditions

```php
public getFilterConditions(): ?\Phalcon\Support\Collection
```

***
### defaultFilterCondition

Retrieves the filter condition based on the specified filters, allowed filters, and logical operator.

```php
public defaultFilterCondition(array|null $filters = null, array|null $allowedFilters = null, bool $or = false): array|string|null
```

**Parameters:**

| Parameter         | Type            | Description                                                                   |
|-------------------|-----------------|-------------------------------------------------------------------------------|
| `$filters`        | **array\|null** | An array of filters.                                                          |
| `$allowedFilters` | **array\|null** | An array of allowed filters.                                                  |
| `$or`             | **bool**        | The logical operator to use for combining multiple filters. Default is false. |

**Return Value:**

The filter condition with the specified filters, or null if no filters are provided.

**Throws:**

if a filter field property or filter operator property is empty, or if a filter field is not allowed.
- [`Exception`](../../../../../../Exception.md)

***
### getFilterOperator

Retrieves the equivalent filter operator for the specified alias or operator.

```php
public getFilterOperator(string $operator): string
```

**Parameters:**

| Parameter   | Type       | Description                           |
|-------------|------------|---------------------------------------|
| `$operator` | **string** | The alias or operator for the filter. |

**Return Value:**

The equivalent filter operator, or an empty string if the operator is not allowed.

***
### getBindTypeFromRawValue

Retrieves the bind type based on the raw value.

```php
public getBindTypeFromRawValue(mixed|null $rawValue = null): int
```

**Parameters:**

| Parameter   | Type            | Description                                   |
|-------------|-----------------|-----------------------------------------------|
| `$rawValue` | **mixed\|null** | The raw value to determine the bind type for. |

**Return Value:**

The bind type based on the raw value. Possible values are:
- Column::BIND_PARAM_STR: If the raw value is a string or an array.
- Column::BIND_PARAM_INT: If the raw value is an integer.
- Column::BIND_PARAM_BOOL: If the raw value is a boolean.
- Column::BIND_PARAM_DECIMAL: If the raw value is a float or a double.
- Column::BIND_PARAM_NULL: If the raw value is null or its type is not recognized.

***
### isFilterAllowed

Determines if the specified field is allowed as a filter based on the provided allowed filters.

```php
public isFilterAllowed(string $field, array|null $allowedFilters): bool
```

**Parameters:**

| Parameter         | Type            | Description                                                      |
|-------------------|-----------------|------------------------------------------------------------------|
| `$field`          | **string**      | The field name to check against the allowed filters.             |
| `$allowedFilters` | **array\|null** | The array of allowed filters or null if no filters are provided. |

**Return Value:**

True if the field is allowed as a filter, false otherwise.

***
### hasFiltersFieldsParams

Check whether the current request filters contain one or more of the specified fields.

```php
public hasFiltersFieldsParams(array|string|null $fields = null, bool $or = false): bool
```

Supports nested AND/OR logic - each nested array inverts the operator.

Examples:
  hasFiltersParams('status')                      // checks if "status" filter exists
  hasFiltersParams(['status', 'type'], true)      // "status" OR "type"
  hasFiltersParams(['status', 'type'])            // "status" AND "type"
  hasFiltersParams([['status', 'type']])          // "status" OR "type"
  hasFiltersParams([[['status', 'type']]])        // "status" AND "type"

**Parameters:**

| Parameter | Type                    | Description                                                                 |
|-----------|-------------------------|-----------------------------------------------------------------------------|
| `$fields` | **array\|string\|null** | List of fields to check against. If null, checks if "filters" param exists. |
| `$or`     | **bool**                | If true, matches at least one (OR). If false, matches all (AND).            |

**Return Value:**

True if the filters satisfy the condition, false otherwise.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
