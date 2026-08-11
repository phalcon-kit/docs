
Shared REST query builder for PhalconKit controllers.

The trait coordinates request-driven query state: filters, permissions,
joins, eager-loading, grouping, aggregate columns, pagination, ordering,
cache options, and save payload metadata. It compiles those collections into
Phalcon model `find()`/aggregate option arrays while keeping extension hooks
available through REST initialization events.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query`

**See Also:**

* https://docs.phalcon.io/5.18/db-models/
* https://docs.phalcon.io/5.18/db-models-relationships/

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

When request parameter filtering fails during
query initialization.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

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
public setFind(array|\Phalcon\Support\Collection|null $find): void
```

**Parameters:**

| Parameter | Type                                         | Description                            |
|-----------|----------------------------------------------|----------------------------------------|
| `$find`   | **array\|\Phalcon\Support\Collection\|null** | The new value for the `find` property. |

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
### prepareFindListToString

Converts find list options to their PHQL string form.

```php
protected prepareFindListToString(array $items): string
```

Collection-backed query options can be represented either as plain values
or as enabled field maps, for example ['id' => true]. Values remain the
default source, but true map entries use their string key as the selected
field instead of compiling to "1".

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$items`  | **array** |             |

***
### conditionsShouldBeHaving

Determines whether WHERE conditions must be promoted to HAVING.

```php
public conditionsShouldBeHaving(?string $conditions): bool
```

Currently disabled by design.

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$conditions` | **?string** |             |

***
### find

Find records in the database using the specified criteria.

```php
public find(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface&\Traversable
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
with the found records. Passing null uses the
controller's normalized default `with` graph.                      |
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation with loaded relationships.

**Throws:**

When the configured model does not support
PhalconKit eager-loading helpers.
- [`ServiceException`](../../../Exception/ServiceException.md)

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
Passing null uses the controller's normalized
default `with` graph.                                |
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation for the first record.

**Throws:**

When the configured model does not support
PhalconKit eager-loading helpers.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### requireEagerLoadModel

Require a loaded model that supports PhalconKit eager-loading helpers.

```php
protected requireEagerLoadModel(\Phalcon\Mvc\ModelInterface $model, string $method): \PhalconKit\Mvc\Model\Interfaces\EagerLoadInterface
```

Controller query helpers can load any Phalcon model, but `findWith()` and
`findFirstWith()` need the PhalconKit eager-loading contract. Keeping this
check in one helper keeps the public query methods readable while still
producing a stable service-resolution exception instead of a late static
method error when a controller is wired to the wrong model class.

**Parameters:**

| Parameter | Type                            | Description                                           |
|-----------|---------------------------------|-------------------------------------------------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** | Loaded model instance used for static query
dispatch. |
| `$method` | **string**                      | Query helper that requires eager loading.             |

**Return Value:**

The same model narrowed to the eager-loading
contract.

**Throws:**

When the configured model does not support
PhalconKit eager-loading helpers.
- [`ServiceException`](../../../Exception/ServiceException.md)

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

***
### prepareCountFind

Prepare count-specific options without overriding an explicit count column.

```php
protected prepareCountFind(array $find): array
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$find`   | **array** |             |

***
### getJoinedCountColumn

Joined count queries default to the root model identity for single-column primary keys.

```php
protected getJoinedCountColumn(array $find): ?string
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$find`   | **array** |             |

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
