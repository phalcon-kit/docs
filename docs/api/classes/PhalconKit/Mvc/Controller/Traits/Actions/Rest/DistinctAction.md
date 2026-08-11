
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\DistinctAction`

## Constants

| Constant                          | Visibility | Type   | Value   |
|-----------------------------------|------------|--------|---------|
| `DISTINCT_ACTION_FIELD_PARAMETER` | public     | string | 'field' |

## Properties

### distinctActionFields

Controller-owned fields that may be enumerated by {@see distinctAction()}.

```php
protected ?\Phalcon\Support\Collection $distinctActionFields
```

***

## Methods

### distinctAction

Return distinct values for one explicitly allowed field.

```php
public distinctAction(): \Phalcon\Http\ResponseInterface
```

The action is intended for facets, autocomplete controls, and dashboard
filters that need the list of possible values under the same filters,
joins, permissions, identity conditions, binds, pagination, and cache
options as the normal REST query. It deliberately does not expose
arbitrary client-selected columns: concrete controllers must opt into
fields through

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\initializeDistinctActionFields().

Successful responses expose:
- `data`: scalar distinct values returned by the database.
- `field`: the public field requested by the client.
- `count`: the number of returned values.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### initializeDistinctActionFields

Initialize the action-level distinct field allow-list.

```php
public initializeDistinctActionFields(): void
```

The default is intentionally closed. Concrete controllers can override
this method and call

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\setDistinctActionFields() with either a value
list (`['status']`) or a public-to-query map
(`['ownerEmail' => 'Owner.email']`). The map form lets applications keep
public API names stable while querying joined aliases internally.

***
### setDistinctActionFields

Replace the fields that {@see distinctAction()} may enumerate.

```php
public setDistinctActionFields(array|\Phalcon\Support\Collection|null $distinctActionFields): void
```

Passing null disables the action for every field. This is the safest
default for reusable framework controllers because exposing all
filterable columns could leak high-cardinality or sensitive values.

**Parameters:**

| Parameter               | Type                                         | Description |
|-------------------------|----------------------------------------------|-------------|
| `$distinctActionFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getDistinctActionFields

Return the configured distinct action field policy.

```php
public getDistinctActionFields(): ?\Phalcon\Support\Collection
```

***
### hasDistinctActionFields

Check whether any distinct action fields are currently enabled.

```php
public hasDistinctActionFields(): bool
```

***
### mergeDistinctActionFields

Merge additional distinct action fields with the current policy.

```php
public mergeDistinctActionFields(array|\Phalcon\Support\Collection $distinctActionFields): void
```

**Parameters:**

| Parameter               | Type                                   | Description                                                                                                                                                                                |
|-------------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$distinctActionFields` | **array\|\Phalcon\Support\Collection** | array or Collection containing public field
names, enabled maps, or public-to-query aliases accepted by
{@see \PhalconKit\Mvc\Controller\Traits\Actions\Rest\getDistinctActionFieldMap()}. |

***
### getDistinctActionRequestedField

Read the requested distinct field from request parameters.

```php
protected getDistinctActionRequestedField(): string|null
```

**Return Value:**

A non-empty public field name, or null when the client
did not provide one.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### resolveDistinctActionField

Resolve a public distinct field to the actual query field.

```php
protected resolveDistinctActionField(string $field): ?string
```

The returned value is intentionally still normalized by


- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\appendModelName() when the query is built. This method only applies
the controller allow-list; it does not format PHQL identifiers.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

***
### getDistinctActionFieldMap

Normalize the configured distinct field policy to public => query fields.

```php
protected getDistinctActionFieldMap(): array<string,string>
```

Supported collection shapes:
- `['status', 'type']` exposes the same public and query fields.
- `['status' => true]` enables a field map entry.
- `['ownerEmail' => 'Owner.email']` exposes a public alias that queries a
  joined model alias.
- false, null, and empty-string values are ignored so controllers can
  disable inherited entries through merge policy.

***
### getDistinctActionFind

Build the find options used to select distinct values.

```php
protected getDistinctActionFind(string $field): array<string|int,mixed>
```

The prepared query contributes conditions, joins, permissions, bind data,
pagination, and cache options. Selection-oriented keys are removed because
this action owns the selected column and should not inherit request
`column`, `columns`, `distinct`, `group`, or `having` state from list or
aggregate endpoints.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

***
### normalizeDistinctActionResult

Convert a distinct resultset into a scalar value list.

```php
protected normalizeDistinctActionResult(\Phalcon\Mvc\Model\ResultsetInterface $resultset): list
```

Phalcon usually hydrates `DISTINCT ... AS value` rows as arrays with a
`value` key. The fallback accepts one-column rows so custom hydration
modes and drivers can still produce the same public response shape.

**Parameters:**

| Parameter    | Type                                      | Description |
|--------------|-------------------------------------------|-------------|
| `$resultset` | **\Phalcon\Mvc\Model\ResultsetInterface** |             |

***
### getDistinctActionRowValue

Extract the selected value from one hydrated distinct row.

```php
protected getDistinctActionRowValue(mixed $row): mixed
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$row`    | **mixed** |             |

***
### setDistinctActionErrorResponse

Return a standard REST error response for distinct action validation.

```php
protected setDistinctActionErrorResponse(string $message): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$message` | **string** |             |

***
