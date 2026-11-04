
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

Initializes the limit from the request, or from `defaultLimit()`.

```php
public initializeLimit(): void
```

A missing, null, or empty-string `limit` parameter uses `defaultLimit()`.
A provided value must be a non-negative integer (an int or a decimal
digit string such as `"25"`); anything else, including `-1`, is rejected
with HTTP 400 instead of being coerced. The `-1` "no limit" sentinel is
reserved for server code through `setLimit(-1)` or `defaultLimit()`;
clients must page through results with `limit` and `offset`.

**Throws:**

When Phalcon rejects parameter filtering.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the requested limit is not a non-negative
integer or exceeds the maximum limit.
- [`HttpException`](../../../../Exception/HttpException.md)

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

If the provided limit is less than -1 or exceeds
the maximum limit.
- [`HttpException`](../../../../Exception/HttpException.md)

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
else it returns a default value of 10.

**Return Value:**

The default limit.

***
### defaultMaxLimit

Returns the default maximum limit.

```php
public defaultMaxLimit(): int|null
```

If the maximum limit is set, then it returns that value,
else it returns a default value of 100.

**Return Value:**

The default maximum limit.

***
