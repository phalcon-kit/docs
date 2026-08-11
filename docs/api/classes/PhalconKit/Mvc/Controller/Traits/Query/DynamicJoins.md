
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\DynamicJoins`

## Properties

### dynamicJoinsMapping

```php
protected array $dynamicJoinsMapping
```

***
### dynamicJoinsBuild

```php
protected ?array $dynamicJoinsBuild
```

***
### dynamicJoins

```php
protected ?\Phalcon\Support\Collection $dynamicJoins
```

***

## Methods

### initializeDynamicJoins

Initializes the dynamic joins.

```php
public initializeDynamicJoins(): void
```

This method is responsible for initializing the dynamic joins.

***
### setDynamicJoins

Sets the dynamic joins for the find criteria.

```php
public setDynamicJoins(array|\Phalcon\Support\Collection|null $dynamicJoins): void
```

**Parameters:**

| Parameter       | Type                                         | Description                                                          |
|-----------------|----------------------------------------------|----------------------------------------------------------------------|
| `$dynamicJoins` | **array\|\Phalcon\Support\Collection\|null** | The collection of dynamic joins.
Pass null to disable dynamic joins. |

***
### getDynamicJoins

Returns the dynamic joins collection.

```php
public getDynamicJoins(): \Phalcon\Support\Collection|null
```

This method retrieves the dynamic joins for the find criteria.
If joins fields have been set, it returns the collection of dynamic joins.
If no dynamic joins have been set, it returns null.

Note: The dynamic joins are used to add conditions during the find query and are not added to the result.

**Return Value:**

The collection of dynamic joins or null everything is allowed.

***
### mergeDynamicJoins

Merges the provided dynamicJoins collection with the current dynamicJoins property.

```php
public mergeDynamicJoins(array|\Phalcon\Support\Collection $dynamicJoins): void
```

**Parameters:**

| Parameter       | Type                                   | Description                                                        |
|-----------------|----------------------------------------|--------------------------------------------------------------------|
| `$dynamicJoins` | **array\|\Phalcon\Support\Collection** | The collection of dynamicJoins to merge with the current property. |

***
### getDynamicJoinsFromFilters

Extract dynamic join definitions required by the current filter tree.

```php
public getDynamicJoinsFromFilters(array|null $filters = null): array
```

Relationship filters can ask the controller to materialize joins lazily.
This method walks nested filters, validates that every requested dynamic
alias is configured, builds generated SQL aliases, and returns the join
definitions that should be merged into the current find query.

**Parameters:**

| Parameter  | Type            | Description                                                                                   |
|------------|-----------------|-----------------------------------------------------------------------------------------------|
| `$filters` | **array\|null** | Optional filter tree. When null, the request
`filters` parameter is read from the controller. |

**Return Value:**

Dynamic join definitions keyed by generated join alias.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When a filter references an undefined dynamic join
alias.
- [`HttpException`](../../../../Exception/HttpException.md)
When a configured dynamic join definition is
malformed.
- [`LogicException`](../../../../Exception/LogicException.md)

***
### normalizeDynamicJoinDefinition

Normalizes dynamic join definitions to [model, condition, alias?, type?].

```php
protected normalizeDynamicJoinDefinition(string $alias, mixed $definition): array
```

Dynamic joins generate their concrete SQL alias at runtime, so only the model and
join condition are required. The legacy [Model::class => condition] form is kept
for older application controllers.

**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$alias`      | **string** |             |
| `$definition` | **mixed**  |             |

***
### getJoinsDefinitionFromField

Retrieves the join definitions for a given field by analyzing its relationship parts.

```php
public getJoinsDefinitionFromField(string $field): array
```

**Parameters:**

| Parameter | Type       | Description                                                                                 |
|-----------|------------|---------------------------------------------------------------------------------------------|
| `$field`  | **string** | The field for which to retrieve the join definitions, including its relationship hierarchy. |

**Return Value:**

An array containing the join definitions for the specified field, ordered in a manner suitable for processing.

***
