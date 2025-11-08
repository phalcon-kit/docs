
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\DynamicJoins`

## Properties

### dynamicJoinsAllowed

```php
protected array $dynamicJoinsAllowed
```

***
### dynamicJoins

```php
protected ?array $dynamicJoins
```

***
### dynamicJoinsMapping

```php
protected array $dynamicJoinsMapping
```

***

## Methods

### getJoins

```php
public getJoins(): mixed
```

***
### getDynamicJoins

```php
public getDynamicJoins(): array
```

***
### getDynamicJoinsFromFilters

```php
public getDynamicJoinsFromFilters(?array $filters = null): array
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$filters` | **?array** |             |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

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
### setDynamicNestedJoin

```php
public setDynamicNestedJoin(string& $field, string|array $startWith, array $joins): bool
```

**Parameters:**

| Parameter    | Type              | Description |
|--------------|-------------------|-------------|
| `$field`     | **string**        |             |
| `$startWith` | **string\|array** |             |
| `$joins`     | **array**         |             |

***
### setDynamicJoin

Sets a dynamic join for a field that matches a specified prefix and updates its configuration.

```php
public setDynamicJoin(string& $field, string $class, array|string $startWith, string|array $condition, string $type = 'left'): bool
```

**Parameters:**

| Parameter    | Type              | Description                                                              |
|--------------|-------------------|--------------------------------------------------------------------------|
| `$field`     | **string**        | The field that needs to be updated with the join alias.                  |
| `$class`     | **string**        | The class or table name to be used in the join condition.                |
| `$startWith` | **array\|string** | The prefix that the field must start with to trigger a dynamic join.     |
| `$condition` | **string\|array** | The joins condition to apply for the dynamic joins.                      |
| `$type`      | **string**        | The type of join to apply (e.g., 'outer left'). Default is 'outer left'. |

**Return Value:**

Returns true if a dynamic join is successfully applied, otherwise false.

***
