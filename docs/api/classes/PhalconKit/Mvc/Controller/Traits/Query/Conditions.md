
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions`

## Properties

### conditions

```php
protected ?\Phalcon\Support\Collection $conditions
```

***

## Methods

### initializeConditions

Initializes and sets up various conditions required for the system.

```php
public initializeConditions(): void
```

- Permission Conditions
- Soft Delete Conditions
- Identity Conditions
- Filter Conditions
- Search Conditions

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When filter conditions contain invalid fields or
operators.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### setConditions

Sets the conditions.

```php
public setConditions(array|\Phalcon\Support\Collection|null $conditions): void
```

**Parameters:**

| Parameter     | Type                                         | Description                                                 |
|---------------|----------------------------------------------|-------------------------------------------------------------|
| `$conditions` | **array\|\Phalcon\Support\Collection\|null** | A collection of conditions or null to unset the conditions. |

***
### getConditions

Retrieves the conditions.

```php
public getConditions(): \Phalcon\Support\Collection|null
```

**Return Value:**

A collection of conditions or null if none are set.

***
### mergeConditions

Merges the provided conditions collection with the current conditions property.

```php
public mergeConditions(array|\Phalcon\Support\Collection $conditions): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                      |
|---------------|----------------------------------------|------------------------------------------------------------------|
| `$conditions` | **array\|\Phalcon\Support\Collection** | The collection of conditions to merge with the current property. |

***
