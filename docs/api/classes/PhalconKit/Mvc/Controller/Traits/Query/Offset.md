
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

Initializes the offset value.

```php
public initializeOffset(): void
```

Sets the offset value using the provided parameter's value, after filtering it
through the specified filter, or sets it to the default offset value if no
offset parameter is provided.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
- [`Exception`](../../../../../Exception.md)

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
- [`Exception`](../../../../../Exception.md)

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
