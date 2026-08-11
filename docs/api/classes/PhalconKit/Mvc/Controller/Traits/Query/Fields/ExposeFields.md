
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\ExposeFields`

## Properties

### exposeFields

Controller-owned response exposure policy.

```php
protected ?\Phalcon\Support\Collection $exposeFields
```

Null lets the exposer use its default behavior for the current item. A
non-null collection constrains the fields or nested relation paths that
standard REST responses expose to clients.

***

## Methods

### initializeExposeFields

Initialize the response exposure field list.

```php
public initializeExposeFields(): void
```

Concrete controllers can override this method and call


- **See:** \PhalconKit\Mvc\Controller\Traits\Query\Fields\setExposeFields() to define the public response shape for standard
REST actions. The default remains null for backward compatibility.

***
### setExposeFields

Replace the fields standard REST actions may expose.

```php
public setExposeFields(array|\Phalcon\Support\Collection|null $exposeFields): void
```

Passing null leaves exposure unrestricted/defaulted. Passing an empty
collection is a closed response policy and can be useful when a custom
transformer owns the complete payload.

**Parameters:**

| Parameter       | Type                                         | Description |
|-----------------|----------------------------------------------|-------------|
| `$exposeFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getExposeFields

Return the configured response exposure policy.

```php
public getExposeFields(): ?\Phalcon\Support\Collection
```

The expose trait converts this collection to an array when listing or
exposing records for standard REST responses.

***
### hasExposeFields

Check whether response exposure configuration is present.

```php
public hasExposeFields(): bool
```

This reports policy presence only. An empty collection still means the
controller explicitly configured exposure.

***
### mergeExposeFields

Merge additional response exposure entries into the current policy.

```php
public mergeExposeFields(array|\Phalcon\Support\Collection $exposeFields): void
```

Merge semantics are centralized in

- **See:** \PhalconKit\Support\CollectionPolicy: null starts
from the incoming collection, empty incoming collections leave an existing
policy unchanged, and associative keys can override previous entries.

**Parameters:**

| Parameter       | Type                                   | Description |
|-----------------|----------------------------------------|-------------|
| `$exposeFields` | **array\|\Phalcon\Support\Collection** |             |

***
