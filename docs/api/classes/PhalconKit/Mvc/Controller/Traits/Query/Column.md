
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Column`

## Properties

### column

```php
protected ?\Phalcon\Support\Collection $column
```

***

## Methods

### initializeColumn

Initializes the column by setting it to null.

```php
public initializeColumn(): void
```

***
### setColumn

Sets the column collection.

```php
public setColumn(array|\Phalcon\Support\Collection|null $column): void
```

**Parameters:**

| Parameter | Type                                         | Description                                                    |
|-----------|----------------------------------------------|----------------------------------------------------------------|
| `$column` | **array\|\Phalcon\Support\Collection\|null** | The collection to set, or null to unset the column collection. |

***
### getColumn

Retrieves the column collection.

```php
public getColumn(): \Phalcon\Support\Collection|null
```

**Return Value:**

Returns a collection of column collection, or null if no collection is available.

***
### mergeColumn

Merges the provided column collection with the current column property.

```php
public mergeColumn(array|\Phalcon\Support\Collection $column): void
```

**Parameters:**

| Parameter | Type                                   | Description                                                   |
|-----------|----------------------------------------|---------------------------------------------------------------|
| `$column` | **array\|\Phalcon\Support\Collection** | The collection of columns to merge with the current property. |

***
