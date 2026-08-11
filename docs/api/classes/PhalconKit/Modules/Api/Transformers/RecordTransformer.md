
Base transformer for Fractal resources backed by Phalcon models.

The transformer is DI-aware so concrete API transformers can resolve shared
services without introducing their own container plumbing. It also provides
helpers for exposing relationships only when they were already loaded by the
model layer, which avoids accidental lazy-loading and keeps response costs
predictable for REST endpoints.

Concrete transformers should call `includeCollectionIfLoaded()` and
`includeItemIfLoaded()` from Fractal include methods when an include should
reflect the model's loaded relationship state instead of forcing a query.

This convention keeps include behavior aligned with controller eager-loading:
the controller decides what relationships are loaded, and the transformer
serializes only that already-known state.

***

* Full name: `\PhalconKit\Modules\Api\Transformers\RecordTransformer`
* Parent class: [`\PhalconKit\Fractal\Transformer`](../../../Fractal/Transformer.md)

## Methods

### transform

```php
public transform(?\PhalconKit\Models\Record $record): array
```

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$record` | **?\PhalconKit\Models\Record** |             |

***

## Inherited methods

### getDI

Returns the Dependency Injection (DI) container used by this object.

```php
public getDI(): \Phalcon\Di\DiInterface
```

**Return Value:**

The DI container instance.

***

### setDI

Sets the dependency injection container.

```php
public setDI(\Phalcon\Di\DiInterface $container): void
```

**Parameters:**

| Parameter    | Type                        | Description                         |
|--------------|-----------------------------|-------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface** | The dependency injection container. |

***

### __isset

Checks if a property is set.

```php
public __isset(string $name): bool
```

**Parameters:**

| Parameter | Type       | Description                        |
|-----------|------------|------------------------------------|
| `$name`   | **string** | The name of the property to check. |

**Return Value:**

True if the property is set, false otherwise.

***

### __get

Magic method __get.

```php
public __get(string $name): mixed
```

Retrieves the value of a non-existent or inaccessible property.

**Parameters:**

| Parameter | Type       | Description               |
|-----------|------------|---------------------------|
| `$name`   | **string** | The name of the property. |

**Return Value:**

The value of the property if it exists, or null if the property is undefined.

***

### includeCollectionIfLoaded

Build a Fractal collection resource for a loaded relationship alias.

```php
protected includeCollectionIfLoaded(\Phalcon\Mvc\ModelInterface $entity, string $alias, \PhalconKit\Fractal\Transformer $transformer): \League\Fractal\Resource\Collection
```

If the alias is not available, or if the loaded value is not iterable, an
empty collection is returned. This keeps collection includes stable for
clients while still avoiding implicit database reads.

Returning an empty collection for missing/non-iterable values is
deliberate: this helper is for "many" relationships, and an absent loaded
relation should serialize as an empty include rather than trigger another
model query from inside a transformer.

**Parameters:**

| Parameter      | Type                                | Description                                                                                |
|----------------|-------------------------------------|--------------------------------------------------------------------------------------------|
| `$entity`      | **\Phalcon\Mvc\ModelInterface**     | Model that may expose loaded relationship
aliases through PhalconKit relationship helpers. |
| `$alias`       | **string**                          | Relationship alias requested by the transformer.                                           |
| `$transformer` | **\PhalconKit\Fractal\Transformer** | Transformer used for each related item.                                                    |

**Return Value:**

Fractal collection resource for the loaded relation.

***

### includeItemIfLoaded

Build a Fractal item resource for a loaded relationship alias.

```php
protected includeItemIfLoaded(\Phalcon\Mvc\ModelInterface $entity, string $alias, \PhalconKit\Fractal\Transformer $transformer): \League\Fractal\Resource\Item|null
```

Missing aliases, null values, and iterable values return null because
Fractal item includes are meant for one related model. Use
`includeCollectionIfLoaded()` when the relation may contain many records.

Returning null tells Fractal to omit the include instead of inventing a
placeholder object. This avoids confusing one-to-one response shapes when
the requested relation was not loaded by the controller/query layer.

**Parameters:**

| Parameter      | Type                                | Description                                                                                |
|----------------|-------------------------------------|--------------------------------------------------------------------------------------------|
| `$entity`      | **\Phalcon\Mvc\ModelInterface**     | Model that may expose loaded relationship
aliases through PhalconKit relationship helpers. |
| `$alias`       | **string**                          | Relationship alias requested by the transformer.                                           |
| `$transformer` | **\PhalconKit\Fractal\Transformer** | Transformer used for the related model.                                                    |

**Return Value:**

Fractal item resource when a single related model is
available, or null when the include should be omitted.

***

### isRelationAliasLoaded

Determine whether a relationship alias was already populated on a model.

```php
protected isRelationAliasLoaded(\Phalcon\Mvc\ModelInterface $entity, string $alias): bool
```

PhalconKit tracks both loaded aliases and dirty aliases. Both are treated
as explicitly available values because they represent state already known
to the model rather than a relation that must be queried.

**Parameters:**

| Parameter | Type                            | Description                                    |
|-----------|---------------------------------|------------------------------------------------|
| `$entity` | **\Phalcon\Mvc\ModelInterface** | Model being inspected.                         |
| `$alias`  | **string**                      | Relationship alias as used by the transformer. |

**Return Value:**

True when the alias has eager-loaded or dirty in-memory data.

***

### getLoadedRelationAlias

Return the loaded or dirty value for a relationship alias.

```php
protected getLoadedRelationAlias(\Phalcon\Mvc\ModelInterface $entity, string $alias): mixed
```

Loaded aliases take priority over dirty aliases so eager-loaded data wins
when both stores contain a value. Null is returned for models that do not
implement PhalconKit's relationship contract or for aliases that have not
been populated.

**Parameters:**

| Parameter | Type                            | Description                                    |
|-----------|---------------------------------|------------------------------------------------|
| `$entity` | **\Phalcon\Mvc\ModelInterface** | Model being inspected.                         |
| `$alias`  | **string**                      | Relationship alias as used by the transformer. |

**Return Value:**

Relationship value, commonly a model, iterable resultset, or
null when no explicit relation value exists.

***
