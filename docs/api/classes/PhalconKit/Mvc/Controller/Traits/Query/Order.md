
The Order trait sets and retrieves the order parameter for the query.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Order`

## Properties

### defaultOrder

```php
protected array|string|null $defaultOrder
```

***
### order

```php
protected ?\Phalcon\Support\Collection $order
```

***

## Methods

### initializeDefaultOrder

Initializes the default order for the instance.

```php
public initializeDefaultOrder(): void
```

***
### initializeOrder

Initializes the order parameter for the query.

```php
public initializeOrder(): void
```

This method processes and sets the order parameter based on the "order" input received.

**Throws:**

If the order parameter is invalid.
- [`Exception`](../../../../../Exception.md)

***
### setOrder

Sets the order for the query.

```php
public setOrder(\Phalcon\Support\Collection|null $order): void
```

The provided order will replace any existing order previously set.

**Parameters:**

| Parameter | Type                                  | Description                                                 |
|-----------|---------------------------------------|-------------------------------------------------------------|
| `$order`  | **\Phalcon\Support\Collection\|null** | The order to be set. It can be a Collection object or null. |

***
### getOrder

Retrieves the order assigned to the query.

```php
public getOrder(): \Phalcon\Support\Collection|null
```

If no order has been assigned, it will return null.

**Return Value:**

The order collection to assign to the query, or null if no order has been set.

***
### setDefaultOrder

Sets the default order for the query.

```php
public setDefaultOrder(array|string|null $defaultOrder): void
```

The default order will be used if no "order" parameter was provided

**Parameters:**

| Parameter       | Type                    | Description                                                         |
|-----------------|-------------------------|---------------------------------------------------------------------|
| `$defaultOrder` | **array\|string\|null** | The default order to be set. It can be an array, a string, or null. |

***
### getDefaultOrder

Retrieves the default order for the query.

```php
public getDefaultOrder(): array|string|null
```

**Return Value:**

The default order. It can be an array, a string, or null.

***
### getSide

Returns the side value based on the given input.

```php
protected getSide(string $side): string
```

**Parameters:**

| Parameter | Type       | Description                   |
|-----------|------------|-------------------------------|
| `$side`   | **string** | The side value to be checked. |

**Return Value:**

The side value. Returns 'desc' if the input is 'desc', otherwise returns 'asc'.

***
