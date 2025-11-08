
Class Query

This class provides methods for building and executing database queries.
It is used as a trait in other classes that need query building capabilities.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query`

## Properties

### find

```php
protected ?\Phalcon\Support\Collection $find
```

***

## Methods

### initializeQuery

Initializes the query builder with default values for various properties.

```php
public initializeQuery(): void
```

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
- [`Exception`](../../../../Exception.md)

***
### initializeFind

Initializes the `find` property with a new Collection object.

```php
public initializeFind(): void
```

The values of various properties are assigned to the corresponding keys of the Collection object.

***
### setFind

Sets the value of the `find` property.

```php
public setFind(\Phalcon\Support\Collection|null $find): void
```

**Parameters:**

| Parameter | Type                                  | Description                            |
|-----------|---------------------------------------|----------------------------------------|
| `$find`   | **\Phalcon\Support\Collection\|null** | The new value for the `find` property. |

***
### getFind

Retrieves the value of the `find` property.

```php
public getFind(): \Phalcon\Support\Collection|null
```

**Return Value:**

The value of the `find` property.

***
### prepareFind

Builds the `find` array for a query.

```php
public prepareFind(\Phalcon\Support\Collection|null $find = null, bool $ignoreKey = false): array
```

**Parameters:**

| Parameter    | Type                                  | Description                                                      |
|--------------|---------------------------------------|------------------------------------------------------------------|
| `$find`      | **\Phalcon\Support\Collection\|null** | The collection to build the find array from. Defaults to null.   |
| `$ignoreKey` | **bool**                              | Whether to ignore the keys in the collection. Defaults to false. |

**Return Value:**

The built find array.

***
### mergeConditions

Merges and reformats the multiple conditions array to work with Phalcon\Mvc\Model\Query\Builder

```php
public mergeConditions(array $ret): array
```

**Parameters:**

| Parameter | Type      | Description                                                         |
|-----------|-----------|---------------------------------------------------------------------|
| `$ret`    | **array** | The input array that may contain conditions and other related data. |

**Return Value:**

The modified array with merged and reformatted conditions.

***
### find

Find records in the database using the specified criteria.

```php
public find(array|null $find = null): \Phalcon\Mvc\Model\Resultset|array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                      |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation.

***
### findWith

Find records in the database using the specified criteria and include related records.

```php
public findWith(array|null $with = null, array|null $find = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                      |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$with`   | **array\|null** | Optional. An array of related models to include
with the found records. Defaults to `null`.                                                                      |
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation with loaded relationships.

***
### findFirst

Find the first record in the database using the specified criteria.

```php
public findFirst(array|null $find = null): \Phalcon\Mvc\ModelInterface|false|null
```

Note: We intentionally removed the Row from the return type to simplify usages.
If you need to access the Row, use a query builder instead.

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                                              |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional. An array of criteria to determine the record to find.
If not provided, the default criteria from `getFind()` method
will be used to find the first record. Defaults to `null`. |

**Return Value:**

The result of the find operation, which is the first record that matches the criteria.

***
### findFirstWith

Find the first record in the database using the specified criteria and relations.

```php
public findFirstWith(array|null $with = null, array|null $find = null): ?\Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                      |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$with`   | **array\|null** | Optional. An array of relations to eager load for the record.
If not provided, the default relations from `getWith()` method
will be used. Defaults to `null`.   |
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation for the first record.

***
### average

Calculates the average value based on a given set of criteria.

```php
public average(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                       |
|-----------|-----------------|---------------------------------------------------|
| `$find`   | **array\|null** | The criteria to filter the records by (optional). |

**Return Value:**

The average value or a result set containing the average value.

***
### count

Retrieves the total count of items based on the specified model name and find criteria.

```php
public count(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|int|false
```

Note: limit and offset are removed from the parameters in order to retrieve the total count

**Parameters:**

| Parameter | Type            | Description                                                                                     |
|-----------|-----------------|-------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | An array of find criteria to filter the results. If null, the default criteria will be applied. |

**Return Value:**

The total count of items that match the specified criteria.

**Throws:**

- [`Exception`](../../../../Exception.md)

***
### sum

Calculates the sum of values based on a given search criteria.

```php
public sum(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional: The criteria to find the maximum value from.
Default: null (will retrieve the `find` from $this->getFind()) |

**Return Value:**

The calculated sum of values.

***
### maximum

Retrieves the minimum value.

```php
public maximum(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional: The criteria to find the maximum value from.
Default: null (will retrieve the `find` from $this->getFind()) |

**Return Value:**

The maximum value from the dataset or a `ResultsetInterface` that represents the grouped maximum values.

***
### minimum

Retrieves the minimum value.

```php
public minimum(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional: The criteria to find the minimum value from.
Default: null (will retrieve the `find` from $this->getFind()) |

**Return Value:**

The minimum value from the dataset or a `ResultsetInterface` that represents the grouped minimum values.

***
### getCalculationFind

Prepares and retrieves the modified `find` array with optional adjustments.

```php
protected getCalculationFind(array|null $find = null, bool $removeLimitOffset = true): array
```

**Parameters:**

| Parameter            | Type            | Description                                                                                                         |
|----------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| `$find`              | **array\|null** | The initial `find` array to modify. If null, it defaults
to the result of `getFind()->toArray()` or an empty array. |
| `$removeLimitOffset` | **bool**        | Whether to remove `limit` and `offset` keys
from the `find` array. Defaults to true.                                |

**Return Value:**

The adjusted `find` array, filtered with any necessary modifications.

***
### generateBindKey

Generates a unique bind key with the given prefix.

```php
public generateBindKey(string $prefix): string
```

**Parameters:**

| Parameter | Type       | Description                            |
|-----------|------------|----------------------------------------|
| `$prefix` | **string** | The prefix to be used in the bind key. |

**Return Value:**

The generated bind key.

***
