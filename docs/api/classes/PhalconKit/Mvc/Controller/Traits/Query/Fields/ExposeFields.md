
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\ExposeFields`

## Properties

### exposeFields

```php
protected ?\Phalcon\Support\Collection $exposeFields
```

***

## Methods

### initializeExposeFields

Initializes the expose fields.

```php
public initializeExposeFields(): void
```

This method is responsible for initializing the necessary expose fields for the model

***
### setExposeFields

Sets the fields for exposing data.

```php
public setExposeFields(\Phalcon\Support\Collection|null $exposeFields): void
```

**Parameters:**

| Parameter       | Type                                  | Description                                                         |
|-----------------|---------------------------------------|---------------------------------------------------------------------|
| `$exposeFields` | **\Phalcon\Support\Collection\|null** | The array of expose fields.
Pass null to allow exposing all fields. |

***
### getExposeFields

Returns the expose fields.

```php
public getExposeFields(): \Phalcon\Support\Collection|null
```

This method retrieves the expose fields for the model.
If expose fields have been set, it returns the collection of expose fields.
If no expose fields have been set, it returns null.

Note: The expose fields are the fields that are exposed with the response.

**Return Value:**

The collection of expose fields or null if no expose fields have been set.

***
### hasExposeFields

Determines if the exposeFields property is set to a non-null value.

```php
public hasExposeFields(): bool
```

**Return Value:**

True if exposeFields is not null, false otherwise.

***
