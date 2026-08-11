
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Group`

## Properties

### group

```php
protected ?\Phalcon\Support\Collection $group
```

***

## Methods

### initializeGroup

Initializes the group by retrieving and processing input parameters.

```php
public initializeGroup(): void
```

This method retrieves the 'group' parameter, applies filters, and formats it as a collection.
If the parameter is not set, the group is set to null. Otherwise, the parameter is split
into an array (if not already an array) and processed into a `Collection` where keys and values
are appropriately trimmed and adjusted.

**Return Value:**

This method does not return a value but updates the group's state internally.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### getGroup

Retrieves the current group collection.

```php
public getGroup(): \Phalcon\Support\Collection|null
```

**Return Value:**

The current group collection or null if not set.

***
### setGroup

Sets the group collection.

```php
public setGroup(array|\Phalcon\Support\Collection|null $group): void
```

**Parameters:**

| Parameter | Type                                         | Description                                  |
|-----------|----------------------------------------------|----------------------------------------------|
| `$group`  | **array\|\Phalcon\Support\Collection\|null** | The group collection to be set. Can be null. |

***
### mergeGroup

Merges the provided group collection with the current group property.

```php
public mergeGroup(array|\Phalcon\Support\Collection $group): void
```

**Parameters:**

| Parameter | Type                                   | Description                                                 |
|-----------|----------------------------------------|-------------------------------------------------------------|
| `$group`  | **array\|\Phalcon\Support\Collection** | The collection of group to merge with the current property. |

***
### defaultGroup

Retrieves the default group based on defined joins.

```php
public defaultGroup(): array|string|null
```

**Return Value:**

The primary key attributes as an array or string if joins are defined and have elements; otherwise, null.

***
