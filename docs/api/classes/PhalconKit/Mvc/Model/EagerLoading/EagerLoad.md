
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
