
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\MapFields`

## Properties

### mapFields

Controller-owned public-to-model assignment map.

```php
protected ?\Phalcon\Support\Collection $mapFields
```

Null disables assignment mapping and leaves payload keys unchanged. A
non-null collection is passed to Phalcon's assign API so controllers can
expose stable public field names while assigning different model fields.

***

## Methods

### initializeMapFields

Initialize the REST assignment field map.

```php
public initializeMapFields(): void
```

Concrete controllers can override this method and call


- **See:** \PhalconKit\Mvc\Controller\Traits\Query\Fields\setMapFields() when public payload names differ from model
attribute names. The default is null so save behavior remains unchanged.

***
### setMapFields

Replace the field map used by REST persistence actions.

```php
public setMapFields(array|\Phalcon\Support\Collection|null $mapFields): void
```

Passing null disables field mapping. Passing an empty collection keeps the
decision explicit but maps no payload keys.

**Parameters:**

| Parameter    | Type                                         | Description |
|--------------|----------------------------------------------|-------------|
| `$mapFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getMapFields

Return the configured assignment field map.

```php
public getMapFields(): ?\Phalcon\Support\Collection
```

The save query trait converts this collection to an array and passes it to
Phalcon's model assignment API together with the optional save-field
policy.

***
### hasMapFields

Check whether assignment mapping is configured.

```php
public hasMapFields(): bool
```

This reports policy presence only. An empty collection still means the
controller intentionally configured no field mappings.

***
### mergeMapFields

Merge additional assignment mappings into the current policy.

```php
public mergeMapFields(array|\Phalcon\Support\Collection $mapFields): void
```

Merge semantics are centralized in

- **See:** \PhalconKit\Support\CollectionPolicy: null starts
from the incoming collection, empty incoming collections leave an existing
policy unchanged, and associative keys can override previous entries.

**Parameters:**

| Parameter    | Type                                   | Description |
|--------------|----------------------------------------|-------------|
| `$mapFields` | **array\|\Phalcon\Support\Collection** |             |

***
