
Trait Behavior

This trait provides methods to manipulate behaviors for models.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Behavior`

## Methods

### getBehavior

Retrieves a behavior by its name.

```php
public getBehavior(string $behaviorName): ?\Phalcon\Mvc\Model\BehaviorInterface
```

**Parameters:**

| Parameter       | Type       | Description                           |
|-----------------|------------|---------------------------------------|
| `$behaviorName` | **string** | The name of the behavior to retrieve. |

**Return Value:**

The behavior instance.

***
### setBehavior

Sets a behavior for the model.

```php
public setBehavior(string $behaviorName, \Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

**Parameters:**

| Parameter       | Type                                     | Description                      |
|-----------------|------------------------------------------|----------------------------------|
| `$behaviorName` | **string**                               | The name of the behavior to set. |
| `$behavior`     | **\Phalcon\Mvc\Model\BehaviorInterface** | The behavior instance to set.    |

***
### hasBehavior

Checks if the model has a specific behavior.

```php
public hasBehavior(string $behaviorName): bool
```

**Parameters:**

| Parameter       | Type       | Description                            |
|-----------------|------------|----------------------------------------|
| `$behaviorName` | **string** | The name of the behavior to check for. |

**Return Value:**

Returns true if the model has the specified behavior, otherwise false.

***
### removeBehavior

Removes a behavior from the model.

```php
public removeBehavior(string $behaviorName): void
```

**Parameters:**

| Parameter       | Type       | Description                         |
|-----------------|------------|-------------------------------------|
| `$behaviorName` | **string** | The name of the behavior to remove. |

***
