
The MetaData trait provides methods for retrieving metadata information about a model or entity.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\MetaData`

## Methods

### getColumnMap

Get the column mapping of the model

```php
public getColumnMap(): array|null
```

**Return Value:**

The column mapping of the model, or null if no mapping is defined

***
### getPrimaryKeys

Retrieves the primary keys attributes of the model.

```php
public getPrimaryKeys(): array
```

**Return Value:**

Array containing the primary keys of the model.

***
### getPrimaryKeysValues

Retrieves the values of the primary keys attributes of the entity.

```php
public getPrimaryKeysValues(): array
```

**Return Value:**

Array containing the values of the primary keys attributes of the entity.

***
