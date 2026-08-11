
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\SaveFields`

## Properties

### saveFields

Controller-owned save-field policy.

```php
protected ?\Phalcon\Support\Collection $saveFields
```

Null delegates writable-field decisions to Phalcon's normal model assign
behavior. A non-null collection is passed to `ModelInterface::assign()`
so REST payloads can write only explicitly configured fields.

***

## Methods

### initializeSaveFields

Initialize the writable field list for REST save/create/update actions.

```php
public initializeSaveFields(): void
```

Concrete controllers should override this method and call


- **See:** \PhalconKit\Mvc\Controller\Traits\Query\Fields\setSaveFields() when a resource needs mass-assignment protection
at the controller layer. The default is null for backward compatibility.

***
### setSaveFields

Replace the fields clients may write through REST persistence actions.

```php
public setSaveFields(array|\Phalcon\Support\Collection|null $saveFields): void
```

Passing null leaves assign unrestricted. Passing an empty collection makes
the policy explicit but gives `assign()` no allowed fields, which is a
useful closed default for read-only resources.

**Parameters:**

| Parameter     | Type                                         | Description |
|---------------|----------------------------------------------|-------------|
| `$saveFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getSaveFields

Return the configured save-field policy.

```php
public getSaveFields(): ?\Phalcon\Support\Collection
```

The save query trait converts the collection to an array and passes it to
Phalcon's model assignment API together with the optional map-field
policy.

***
### hasSaveFields

Check whether save-field configuration is present.

```php
public hasSaveFields(): bool
```

This reports policy presence only. An empty collection still means the
controller intentionally configured a closed writable-field policy.

***
### mergeSaveFields

Merge additional save-field entries into the current policy.

```php
public mergeSaveFields(array|\Phalcon\Support\Collection $saveFields): void
```

Merge semantics are centralized in

- **See:** \PhalconKit\Support\CollectionPolicy: null starts
from the incoming collection, empty incoming collections leave an existing
policy unchanged, and associative keys can override previous entries.

**Parameters:**

| Parameter     | Type                                   | Description |
|---------------|----------------------------------------|-------------|
| `$saveFields` | **array\|\Phalcon\Support\Collection** |             |

***
