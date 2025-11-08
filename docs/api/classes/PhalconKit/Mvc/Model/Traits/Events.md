
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Events`

## Methods

### fireEventCancel

```php
public fireEventCancel(string $eventName): bool
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$eventName` | **string** |             |

***
### find

Retrieves records from the database that match the specified conditions.

```php
public static find(array|int|null|string $parameters = null): \Phalcon\Mvc\Model\Resultset|array
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                         | Description                                                                                                  |
|---------------|------------------------------|--------------------------------------------------------------------------------------------------------------|
| `$parameters` | **array\|int\|null\|string** | Optional conditions to filter the retrieved records. Can include arrays, strings, or other query parameters. |

**Return Value:**

Returns the result set as an array, a Resultset object, or a Simple object depending on the query execution.

**See Also:**

* \Phalcon\Mvc\Model::find()

***
### findFirst

Finds the first record that matches the given parameters.

```php
public static findFirst(array|int|null|string $parameters = null): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|false|null
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                         | Description                              |
|---------------|------------------------------|------------------------------------------|
| `$parameters` | **array\|int\|null\|string** | Optional parameters to filter the query. |

**Return Value:**

The first matching record, or null if no record is found or false if the operation is canceled.

**See Also:**

* \Phalcon\Mvc\Model::findFirst()

***
### count

Counts the number of records that match the given parameters.

```php
public static count(array|null|string $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|int|false
```

This method wraps the core static `count` model call with beforeCount/afterCount cancellable events.
The "beforeCount" event can cancel the operation by returning false.

* This method is **static**.
**Parameters:**

| Parameter     | Type                    | Description                                        |
|---------------|-------------------------|----------------------------------------------------|
| `$parameters` | **array\|null\|string** | Optional parameters to filter the count operation. |

**Return Value:**

The count result or a ResultsetInterface, depending on the implementation.

**See Also:**

* \Phalcon\Mvc\Model::count()

***
### sum

Executes a sum operation on the underlying data with optional parameters.

```php
public static sum(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

This method supports cancellable events triggered before and after execution.
If the "beforeSum" event cancels the operation, this method returns false.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                         |
|---------------|-----------|-----------------------------------------------------|
| `$parameters` | **array** | Optional parameters to customize the sum operation. |

**Return Value:**

Returns the sum result as a float, a result set interface, or false if the operation is canceled.

**See Also:**

* \Phalcon\Mvc\Model::sum()

***
### average

Calculates the average of results based on the provided parameters. It wraps the method execution
with before/after cancellable events.

```php
public static average(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

Example events triggered:
- beforeAverage()
- afterAverage()

If the "beforeAverage" event cancels the operation, false is returned.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                    |
|---------------|-----------|----------------------------------------------------------------|
| `$parameters` | **array** | Parameters to define the criteria for calculating the average. |

**Return Value:**

The calculated average or a ResultsetInterface, depending on the implementation.

**See Also:**

* \Phalcon\Mvc\Model::average()

***
### minimum

Calculates the minimum value of a specified column in the database according to the given conditions.

```php
public static minimum(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                            |
|---------------|-----------|----------------------------------------------------------------------------------------|
| `$parameters` | **array** | Parameters to customize the query, such as conditions, column selection, or groupings. |

**Return Value:**

Returns the minimum value as a float, a ResultsetInterface object, or false if no matching records are found or the operation fails.

***
### maximum

Calculates the maximum value of a specified column in the database based on the given conditions.

```php
public static maximum(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                            |
|---------------|-----------|----------------------------------------------------------------------------------------|
| `$parameters` | **array** | Parameters to customize the query, such as conditions, column selection, or groupings. |

**Return Value:**

Returns the computed maximum value as a float, a ResultsetInterface object for detailed results, or false on failure.

***
### fireEventCancelCall

Wraps core static model calls (find, findFirst, count, sum, average, minimum, maximum)
 with beforeX/afterX cancellable events.

```php
public static fireEventCancelCall(string $method, callable $callable): mixed
```

Example (beforeX/afterX events):
- beforeAverage()
- beforeSum()
- beforeCount()
- beforeFind()
- beforeFindFirst()
- afterAverage()
- afterSum()
- afterCount()
- afterFind()
- afterFindFirst()

Returns false if the "beforeX" event cancels the operation.

* This method is **static**.
**Parameters:**

| Parameter   | Type         | Description |
|-------------|--------------|-------------|
| `$method`   | **string**   |             |
| `$callable` | **callable** |             |

***
