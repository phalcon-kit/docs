
***

* Full name: `\PhalconKit\Mvc\Model\EagerLoading\Loader`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Constants

| Constant              | Visibility | Type | Value                                                                                                                      |
|-----------------------|------------|------|----------------------------------------------------------------------------------------------------------------------------|
| `E_INVALID_SUBJECT`   | private    |      | 'Expected value of `subject` to be either a ModelInterface object, a Simple object or an array of ModelInterface objects.' |
| `E_INVALID_CLASSNAME` | private    |      | 'Expected value of `className` to be either an existing class name.'                                                       |

## Properties

### subject

```php
public ?array $subject
```

***

### className

```php
public string $className
```

***

### eagerLoads

```php
public array $eagerLoads
```

***

### singleModel

```php
public bool $singleModel
```

***

### options

```php
public array $options
```

***

## Methods

### __construct

Constructs a new instance of the class.

```php
public __construct(mixed $from, array $arguments): mixed
```

**Parameters:**

| Parameter    | Type      | Description                                                                                                         |
|--------------|-----------|---------------------------------------------------------------------------------------------------------------------|
| `$from`      | **mixed** | The data source from which to load the data. Can be an instance of ModelInterface,
Simple, array, null, or boolean. |
| `$arguments` | **array** | Optional arguments for eager loading. Each argument should be an array
specifying the relationships to eager load.  |

**Throws:**

If the supplied data source is invalid.
- [`InvalidArgumentException`](../../../../InvalidArgumentException.md)

***

### setOptions

Sets the options for the current object instance.

```php
public setOptions(array $options = []): $this
```

**Parameters:**

| Parameter  | Type      | Description                                 |
|------------|-----------|---------------------------------------------|
| `$options` | **array** | An array of options for the current object. |

**Return Value:**

The current object instance after setting the options.

***

### setSubject

Sets the subject of the object.

```php
public setSubject(array|null $subject): $this
```

**Parameters:**

| Parameter  | Type            | Description                                          |
|------------|-----------------|------------------------------------------------------|
| `$subject` | **array\|null** | The subject data array or null to clear the subject. |

**Return Value:**

The current object instance with the subject set.

***

### getSubject

Gets the subject

```php
public getSubject(): \Phalcon\Mvc\ModelInterface[]|null
```

**Return Value:**

The subject, or null if it has not been set.

***

### getFirstSubject

Retrieves the first element from the subject array and returns it.

```php
public getFirstSubject(): \Phalcon\Mvc\ModelInterface|null
```

**Return Value:**

The first element from the subject array, or null if the array is empty.

***

### from

Creates an instance of the current object from various input types and returns it.

```php
public static from(mixed $subject, mixed $arguments): array|\Phalcon\Mvc\ModelInterface|null
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description                                                      |
|--------------|-----------|------------------------------------------------------------------|
| `$subject`   | **mixed** | The input object or array to create the instance from.           |
| `$arguments` | **mixed** | Additional arguments that can be passed to the creation process. |

**Return Value:**

The current object instance created from the input.

***

### fromModel

Create and get from a Model

```php
public static fromModel(\Phalcon\Mvc\ModelInterface $subject, mixed $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                            | Description |
|--------------|---------------------------------|-------------|
| `$subject`   | **\Phalcon\Mvc\ModelInterface** |             |
| `$arguments` | **mixed**                       |             |

***

### fromArray

Create and get from an array

```php
public static fromArray(\Phalcon\Mvc\ModelInterface[] $subject, mixed $arguments): array
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                              | Description |
|--------------|-----------------------------------|-------------|
| `$subject`   | **\Phalcon\Mvc\ModelInterface[]** |             |
| `$arguments` | **mixed**                         |             |

***

### fromModelWithoutSoftDelete

Create and get from a Model without soft deleted records

```php
public static fromModelWithoutSoftDelete(\Phalcon\Mvc\ModelInterface $subject, mixed $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                            | Description |
|--------------|---------------------------------|-------------|
| `$subject`   | **\Phalcon\Mvc\ModelInterface** |             |
| `$arguments` | **mixed**                       |             |

***

### fromArrayWithoutSoftDelete

Create and get from an array without soft deleted records

```php
public static fromArrayWithoutSoftDelete(\Phalcon\Mvc\ModelInterface[] $subject, mixed $arguments): array
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                              | Description |
|--------------|-----------------------------------|-------------|
| `$subject`   | **\Phalcon\Mvc\ModelInterface[]** |             |
| `$arguments` | **mixed**                         |             |

***

### fromResultset

Create and get from a Resultset

```php
public static fromResultset(\Phalcon\Mvc\Model\ResultsetInterface $subject, mixed $arguments): array
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                                      | Description |
|--------------|-------------------------------------------|-------------|
| `$subject`   | **\Phalcon\Mvc\Model\ResultsetInterface** |             |
| `$arguments` | **mixed**                                 |             |

***

### parseArguments

Parses the arguments that will be resolved to Relation instances

```php
private static parseArguments(array $arguments): array
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

**Throws:**

- [`InvalidArgumentException`](../../../../InvalidArgumentException.md)

***

### addEagerLoad

Adds an eager load for a given relation alias and optional constraints and returns an instance of the current object.

```php
public addEagerLoad(string $relationAlias, callable|null $constraints = null): $this
```

**Parameters:**

| Parameter        | Type               | Description                                                                                             |
|------------------|--------------------|---------------------------------------------------------------------------------------------------------|
| `$relationAlias` | **string**         | The alias of the relation to be eagerly loaded.                                                         |
| `$constraints`   | **callable\|null** | Optional. The callback function that applies constraints on the eager loaded relation. Default is null. |

**Return Value:**

The current object instance after adding the eager load.

***

### buildTree

Resolves the relations

```php
private buildTree(): \PhalconKit\Mvc\Model\EagerLoading\EagerLoad[]
```

**Throws:**

- [`RuntimeException`](../../../../RuntimeException.md)

***

### execute

Execute the eager loading of related models.

```php
public execute(): self
```

This method iterates through the result of the buildTree method and loads the related models
using the load method of each eager load instance.

**Return Value:**

The instance of the class executing the method.

***

### load

Loads the data from a data source and returns an instance of the current object.

```php
public load(): self
```

**Return Value:**

The current object instance after loading the data.

***
