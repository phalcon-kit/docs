
The Limit trait provides methods to handle query limits.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Limit`

## Properties

### limit

```php
protected ?int $limit
```

***
### maxLimit

```php
protected ?int $maxLimit
```

***

## Methods

### initializeLimit

Initializes the limit for the current instance.

```php
public initializeLimit(): void
```

It sets the limit value to the result of calling the `getParam` method, passing
the 'limit' parameter as the first argument, an array of filters as the second argument,
and the result of calling the `defaultLimit` method as the third argument.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
- [`Exception`](../../../../../Exception.md)

***
### setLimit

Sets the limit for the query.

```php
public setLimit(int|null $limit): void
```

If the provided limit is less than -1, it throws an exception with an error message.
If the maximum limit is set and it's not -1, it checks if the provided limit is higher than the maximum limit, and throws an exception if it is.
After performing the necessary validations, it updates the limit property with the provided value.

**Parameters:**

| Parameter | Type          | Description          |
|-----------|---------------|----------------------|
| `$limit`  | **int\|null** | The limit to be set. |

**Throws:**

If the provided limit is less than -1 or exceeds the maximum limit.
- [`Exception`](../../../../../Exception.md)

***
### getLimit

Returns the limit.

```php
public getLimit(): int|null
```

If the limit is set to -1, then it returns null indicating that there is no limit,
else it returns the specified limit.

**Return Value:**

The limit value or null if there is no limit.

***
### setMaxLimit

Sets the maximum limit.

```php
public setMaxLimit(int|null $maxLimit): void
```

Sets the value of the maximum limit. If a value is provided,
it will be set as the new maximum limit. If a null value is provided,
the maximum limit will be unset.

**Parameters:**

| Parameter   | Type          | Description                      |
|-------------|---------------|----------------------------------|
| `$maxLimit` | **int\|null** | The new maximum limit to be set. |

***
### getMaxLimit

Returns the maximum limit.

```php
public getMaxLimit(): int|null
```

If the maximum limit is set, then it returns that value,
else it returns null.

**Return Value:**

The maximum limit, or null if not set.

***
### defaultLimit

Returns the default limit.

```php
public defaultLimit(): int|null
```

If the limit is set, then it returns that value,
else it returns a default value of 100.

**Return Value:**

The default limit.

***
### defaultMaxLimit

Returns the default maximum limit.

```php
public defaultMaxLimit(): int|null
```

If the maximum limit is set, then it returns that value,
else it returns a default value of 1000.

**Return Value:**

The default maximum limit.

***
