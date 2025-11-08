
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Joins`

## Properties

### joins

```php
protected ?\Phalcon\Support\Collection $joins
```

***

## Methods

### initializeJoins

Initializes the joins.

```php
public initializeJoins(): void
```

This method is responsible for initializing the joins.

***
### setJoins

Sets the joins for the find criteria.

```php
public setJoins(\Phalcon\Support\Collection|null $joins): void
```

**Parameters:**

| Parameter | Type                                  | Description                                          |
|-----------|---------------------------------------|------------------------------------------------------|
| `$joins`  | **\Phalcon\Support\Collection\|null** | The collection of joins.
Pass null to disable joins. |

***
### getJoins

Returns the joins collection.

```php
public getJoins(): \Phalcon\Support\Collection|null
```

This method retrieves the joins for the find criteria.
If joins fields have been set, it returns the collection of joins.
If no joins have been set, it returns null.

Note: The joins are used to add conditions during the find query and are not added to the result.

**Return Value:**

The collection of joins or null everything is allowed.

***
