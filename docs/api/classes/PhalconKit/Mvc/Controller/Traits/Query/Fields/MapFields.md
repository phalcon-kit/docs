
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\MapFields`

## Properties

### mapFields

```php
protected ?\Phalcon\Support\Collection $mapFields
```

***

## Methods

### initializeMapFields

Initializes the map fields.

```php
public initializeMapFields(): void
```

This method is responsible for initializing the necessary map fields for the model

***
### setMapFields

Sets the fields for mapping data.

```php
public setMapFields(\Phalcon\Support\Collection|null $mapFields): void
```

**Parameters:**

| Parameter    | Type                                  | Description                                                 |
|--------------|---------------------------------------|-------------------------------------------------------------|
| `$mapFields` | **\Phalcon\Support\Collection\|null** | The array of map fields.
Pass null to disable the mappings. |

***
### getMapFields

Returns the map fields.

```php
public getMapFields(): \Phalcon\Support\Collection|null
```

This method retrieves the map fields for the model.
If map fields have been set, it returns the collection of map fields.
If no map fields have been set, it returns null.

Note: The map fields are the fields that are mapped during the data assignation (save).

**Return Value:**

The collection of map fields or null if no map fields have been set.

***
### hasMapFields

Determines if map fields are set.

```php
public hasMapFields(): bool
```

This method checks whether the map fields have been initialized and are not null.

**Return Value:**

True if map fields are set, otherwise false.

***
