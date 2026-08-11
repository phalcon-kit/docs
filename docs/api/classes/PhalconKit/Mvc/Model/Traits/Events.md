
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
### ensureTraversableResultset

```php
private static ensureTraversableResultset(\Phalcon\Mvc\Model\ResultsetInterface $resultset): \Phalcon\Mvc\Model\ResultsetInterface&\Traversable
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                                      | Description |
|--------------|-------------------------------------------|-------------|
| `$resultset` | **\Phalcon\Mvc\Model\ResultsetInterface** |             |

***
### find

Retrieves records from the database that match the specified conditions.

```php
public static find(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface&\Traversable
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                                                                                                                                              |
|---------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Optional native Phalcon find parameters. The
public signature stays broad to match PhalconKit's patched Phalcon
model stubs, while callers normally pass an array, string, integer
primary key, or null. |

**Return Value:**

Returns the result set, or an empty result set if the operation is canceled.

**See Also:**

* \Phalcon\Mvc\Model::find()

***
### findFirst

Finds the first record that matches the given parameters.

```php
public static findFirst(mixed $parameters = null): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|false|null
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                                                                                                                                                    |
|---------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Optional native Phalcon find-first parameters.
The public signature stays broad to match PhalconKit's patched
Phalcon model stubs, while callers normally pass an array, string,
integer primary key, or null. |

**Return Value:**

The first matching record, or null if no record is found or false if the operation is canceled.

**See Also:**

* \Phalcon\Mvc\Model::findFirst()

***
### count

Counts the number of records that match the given parameters.

```php
public static count(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|int
```

This method wraps the core static `count` model call with beforeCount/afterCount cancellable events.
The "beforeCount" event can cancel the operation. Since Phalcon 5.16's
native contract cannot return false for count(), cancellation returns 0.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                               |
|---------------|-----------|-------------------------------------------|
| `$parameters` | **mixed** | Optional native Phalcon count parameters. |

**Return Value:**

The count result or a ResultsetInterface, depending on the implementation.

**See Also:**

* \Phalcon\Mvc\Model::count()

***
### sum

Executes a sum operation on the underlying data with optional parameters.

```php
public static sum(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|float
```

This method supports cancellable events triggered before and after execution.
If the "beforeSum" event cancels the operation, this method returns 0.0
to satisfy Phalcon 5.16's native return contract.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                             |
|---------------|-----------|-----------------------------------------|
| `$parameters` | **mixed** | Optional native Phalcon sum parameters. |

**Return Value:**

Returns the sum result as a float or a result set interface.

**See Also:**

* \Phalcon\Mvc\Model::sum()

***
### average

Calculates the average of results based on the provided parameters. It wraps the method execution
with before/after cancellable events.

```php
public static average(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float
```

Example events triggered:
- beforeAverage()
- afterAverage()

If the "beforeAverage" event cancels the operation, 0.0 is returned to
satisfy Phalcon 5.16's native return contract.

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
public static minimum(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                                           |
|---------------|-----------|-------------------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon parameters to customize the query,
such as conditions, column selection, or groupings. |

**Return Value:**

Returns the minimum value as a float, a ResultsetInterface object, or false if no matching records are found or the operation fails.

***
### maximum

Calculates the maximum value of a specified column in the database based on the given conditions.

```php
public static maximum(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                                           |
|---------------|-----------|-------------------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon parameters to customize the query,
such as conditions, column selection, or groupings. |

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

Returns false if the "beforeX" event cancels the operation. Callers
whose native Phalcon contracts cannot return false must normalize this
sentinel before returning.

* This method is **static**.
**Parameters:**

| Parameter   | Type         | Description |
|-------------|--------------|-------------|
| `$method`   | **string**   |             |
| `$callable` | **callable** |             |

***
