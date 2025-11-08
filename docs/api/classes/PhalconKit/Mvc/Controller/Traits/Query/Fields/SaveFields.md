
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\SaveFields`

## Properties

### saveFields

```php
protected ?\Phalcon\Support\Collection $saveFields
```

***

## Methods

### initializeSaveFields

Initializes the save fields.

```php
public initializeSaveFields(): void
```

This method is responsible for initializing the necessary save fields for the model

***
### setSaveFields

Sets the fields for saving data.

```php
public setSaveFields(\Phalcon\Support\Collection|null $saveFields): void
```

**Parameters:**

| Parameter     | Type                                  | Description                                                     |
|---------------|---------------------------------------|-----------------------------------------------------------------|
| `$saveFields` | **\Phalcon\Support\Collection\|null** | The array of save fields.
Pass null to allow saving all fields. |

***
### getSaveFields

Returns the save fields.

```php
public getSaveFields(): \Phalcon\Support\Collection|null
```

This method retrieves the save fields for the model.
If save fields have been set, it returns the collection of save fields.
If no save fields have been set, it returns null.

Note: The save fields are the fields that are allowed to be saved in the database for the model.

**Return Value:**

The collection of save fields or null if no save fields have been set.

***
### hasSaveFields

Checks if the save fields are set.

```php
public hasSaveFields(): bool
```

This method determines whether the save fields have been initialized.

**Return Value:**

True if save fields are set, otherwise false.

***
