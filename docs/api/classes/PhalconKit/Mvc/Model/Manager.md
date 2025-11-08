
***

* Full name: `\PhalconKit\Mvc\Model\Manager`
* Parent class: [`Manager`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Mvc\Model\ManagerInterface`](./ManagerInterface.md)

## Methods

### getBehaviors

Retrieve all behaviors.

```php
public getBehaviors(): array
```

***

### setBehaviors

Replaces the current behaviors with a new set of behaviors.

```php
public setBehaviors(array $behaviors): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$behaviors` | **array** |             |

***

### getBehavior

Get a behavior using the behavior name

```php
public getBehavior(\Phalcon\Mvc\ModelInterface $model, string $behaviorName): ?\Phalcon\Mvc\Model\BehaviorInterface
```

**Parameters:**

| Parameter       | Type                            | Description |
|-----------------|---------------------------------|-------------|
| `$model`        | **\Phalcon\Mvc\ModelInterface** |             |
| `$behaviorName` | **string**                      |             |

***

### setBehavior

Set a behavior using the behavior name

```php
public setBehavior(\Phalcon\Mvc\ModelInterface $model, string $behaviorName, \Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

**Parameters:**

| Parameter       | Type                                     | Description |
|-----------------|------------------------------------------|-------------|
| `$model`        | **\Phalcon\Mvc\ModelInterface**          |             |
| `$behaviorName` | **string**                               |             |
| `$behavior`     | **\Phalcon\Mvc\Model\BehaviorInterface** |             |

***

### hasBehavior

Return true if the behavior is set

```php
public hasBehavior(\Phalcon\Mvc\ModelInterface $model, string $behaviorName): bool
```

**Parameters:**

| Parameter       | Type                            | Description |
|-----------------|---------------------------------|-------------|
| `$model`        | **\Phalcon\Mvc\ModelInterface** |             |
| `$behaviorName` | **string**                      |             |

***

### removeBehavior

Removes a behavior associated with the given model and behavior name.

```php
public removeBehavior(\Phalcon\Mvc\ModelInterface $model, string $behaviorName): void
```

**Parameters:**

| Parameter       | Type                            | Description |
|-----------------|---------------------------------|-------------|
| `$model`        | **\Phalcon\Mvc\ModelInterface** |             |
| `$behaviorName` | **string**                      |             |

***
