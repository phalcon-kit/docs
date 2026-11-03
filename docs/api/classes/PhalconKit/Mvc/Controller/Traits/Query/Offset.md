
This trait provides functionality to set and get an offset value for a query.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Offset`

## Properties

### offset

```php
protected ?int $offset
```

***

## Methods

### initializeOffset

Initializes the offset from the request, or from `defaultOffset()`.

```php
public initializeOffset(): void
```

A missing, null, or empty-string `offset` parameter uses
`defaultOffset()`. A provided value must be a non-negative integer (an
int or a decimal digit string such as `"20"`); anything else is rejected
with HTTP 400 instead of being coerced.

**Throws:**

When Phalcon rejects parameter filtering.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the requested offset is not a non-negative
integer.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### setOffset

Sets the offset value for the query.

```php
public setOffset(int|null $offset): void
```

**Parameters:**

| Parameter | Type          | Description                                                                                                               |
|-----------|---------------|---------------------------------------------------------------------------------------------------------------------------|
| `$offset` | **int\|null** | The offset value to set for the query. Specify an integer representing the offset value or null if no offset is required. |

**Throws:**

If the specified offset value is less than 0.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### getOffset

Returns the offset value.

```php
public getOffset(): int|null
```

**Return Value:**

The offset value. Returns either an integer representing the offset value or null if no offset is set.

***
### defaultOffset

Returns the default offset value.

```php
public defaultOffset(): int|null
```

**Return Value:**

The default offset value. Returns either an integer representing the offset value or null if no offset is set.

***
