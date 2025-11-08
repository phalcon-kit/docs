
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\SearchFields`

## Properties

### searchFields

```php
protected ?\Phalcon\Support\Collection $searchFields
```

***

## Methods

### initializeSearchFields

Initializes the search fields.

```php
public initializeSearchFields(): void
```

This method is responsible for initializing the necessary search fields for the model

***
### setSearchFields

Sets the fields for searching data.

```php
public setSearchFields(\Phalcon\Support\Collection|null $searchFields): void
```

**Parameters:**

| Parameter       | Type                                  | Description                                                          |
|-----------------|---------------------------------------|----------------------------------------------------------------------|
| `$searchFields` | **\Phalcon\Support\Collection\|null** | The array of search fields.
Pass null to allow searching all fields. |

***
### getSearchFields

Returns the search fields.

```php
public getSearchFields(): \Phalcon\Support\Collection|null
```

This method retrieves the search fields for the model.
If search fields have been set, it returns the collection of search fields.
If no search fields have been set, it returns null.

Note: The search fields are the fields that are used with the search queries.

**Return Value:**

The collection of search fields or null if no search fields have been set.

***
### hasSearchFields

Determines if the search fields are defined.

```php
public hasSearchFields(): bool
```

This method checks whether the search fields for the model have been set.

**Return Value:**

True if search fields are defined, false otherwise.

***
