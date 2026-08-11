
Represents a level in the relations tree to be eagerly loaded

***

* Full name: `\PhalconKit\Mvc\Model\EagerLoading\EagerLoad`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Properties

### relation

```php
private \Phalcon\Mvc\Model\RelationInterface $relation
```

***

### constraints

```php
private null|callable $constraints
```

***

### parent

```php
private \PhalconKit\Mvc\Model\EagerLoading\Loader|\PhalconKit\Mvc\Model\EagerLoading\EagerLoad $parent
```

***

### subject

```php
private null|\Phalcon\Mvc\ModelInterface[] $subject
```

***

## Methods

### __construct

```php
public __construct(\Phalcon\Mvc\Model\Relation $relation, null|callable $constraints, \PhalconKit\Mvc\Model\EagerLoading\Loader|\PhalconKit\Mvc\Model\EagerLoading\EagerLoad $parent): mixed
```

**Parameters:**

| Parameter      | Type                                                                                        | Description |
|----------------|---------------------------------------------------------------------------------------------|-------------|
| `$relation`    | **\Phalcon\Mvc\Model\Relation**                                                             |             |
| `$constraints` | **null\|callable**                                                                          |             |
| `$parent`      | **\PhalconKit\Mvc\Model\EagerLoading\Loader\|\PhalconKit\Mvc\Model\EagerLoading\EagerLoad** |             |

***

### getSubject

```php
public getSubject(): null|\Phalcon\Mvc\ModelInterface[]
```

***

### load

Executes each db query needed

```php
public load(): $this
```

Note: The {$alias} property is set two times because Phalcon Model ignores
empty arrays when overloading property set.

Also

- **See:** https://github.com/stibiumz/phalcon.eager-loading/issues/1

***

### assignMissingRelations

```php
private assignMissingRelations(array<int,\Phalcon\Mvc\ModelInterface> $records, string $alias, bool $isSingle): void
```

**Parameters:**

| Parameter   | Type                                       | Description |
|-------------|--------------------------------------------|-------------|
| `$records`  | **array<int,\Phalcon\Mvc\ModelInterface>** |             |
| `$alias`    | **string**                                 |             |
| `$isSingle` | **bool**                                   |             |

***

### getRelationKey

```php
private getRelationKey(\Phalcon\Mvc\EntityInterface $record, string $field): int|string|null
```

**Parameters:**

| Parameter | Type                             | Description |
|-----------|----------------------------------|-------------|
| `$record` | **\Phalcon\Mvc\EntityInterface** |             |
| `$field`  | **string**                       |             |

***

### requireEntity

Require the native entity contract at the model-subject boundary.

```php
private requireEntity(object $record): \Phalcon\Mvc\EntityInterface
```

Phalcon's ModelInterface does not extend EntityInterface even though the
native Model implements both. Eager-loading relation keys need the entity
attribute API, so validate that runtime contract deterministically instead
of relying on assertions that may be disabled.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$record` | **object** |             |

***

### isSingleRelation

```php
private isSingleRelation(\Phalcon\Mvc\Model\RelationInterface $relation, bool $isThrough): bool
```

**Parameters:**

| Parameter    | Type                                     | Description |
|--------------|------------------------------------------|-------------|
| `$relation`  | **\Phalcon\Mvc\Model\RelationInterface** |             |
| `$isThrough` | **bool**                                 |             |

***

### assignRelation

```php
private assignRelation(\Phalcon\Mvc\ModelInterface $record, string $alias, mixed $value): void
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$record` | **\Phalcon\Mvc\ModelInterface** |             |
| `$alias`  | **string**                      |             |
| `$value`  | **mixed**                       |             |

***
