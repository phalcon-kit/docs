
This trait provides methods for managing search conditions.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\SearchConditions`

## Properties

### searchConditions

```php
protected ?\Phalcon\Support\Collection $searchConditions
```

***

## Methods

### initializeSearchConditions

Initializes the search conditions.

```php
public initializeSearchConditions(): void
```

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### setSearchConditions

Set the search conditions for this object.

```php
public setSearchConditions(\Phalcon\Support\Collection|null $searchConditions): void
```

**Parameters:**

| Parameter           | Type                                  | Description                      |
|---------------------|---------------------------------------|----------------------------------|
| `$searchConditions` | **\Phalcon\Support\Collection\|null** | The search conditions to be set. |

***
### getSearchConditions

Returns the search conditions.

```php
public getSearchConditions(): \Phalcon\Support\Collection|null
```

**Return Value:**

The search conditions, represented as a collection.

***
### defaultSearchCondition

Generates the default search condition for the method.

```php
public defaultSearchCondition(): array|string|null
```

**Return Value:**

The default search condition, represented as an array containing the query, bind parameters, and bind types.

**Throws:**

If an error occurs while filtering the search parameter.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### generateSearchSubQuery

Generates a sub-query for searching within the specified fields.

```php
public generateSearchSubQuery(string $searchTerm, array $searchFields, array& $bind, array& $bindTypes): array
```

**Parameters:**

| Parameter       | Type       | Description                                                                   |
|-----------------|------------|-------------------------------------------------------------------------------|
| `$searchTerm`   | **string** | The term to search for.                                                       |
| `$searchFields` | **array**  | The fields to search within. Can be nested arrays representing relationships. |
| `$bind`         | **array**  | The reference array to hold values for the search bind parameters.            |
| `$bindTypes`    | **array**  | The reference array to hold the bind types for the search parameters.         |

**Return Value:**

The generated sub-query as an array of conditional statements.

***
