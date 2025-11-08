
***

* Full name: `\PhalconKit\Mvc\Model\ManagerInterface`
* Parent interfaces:
  `ManagerInterface`

## Methods

### getBehaviors

```php
public getBehaviors(): array
```

***

### setBehaviors

```php
public setBehaviors(array $behaviors): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$behaviors` | **array** |             |

***

### getBehavior

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

```php
public removeBehavior(\Phalcon\Mvc\ModelInterface $model, string $behaviorName): void
```

**Parameters:**

| Parameter       | Type                            | Description |
|-----------------|---------------------------------|-------------|
| `$model`        | **\Phalcon\Mvc\ModelInterface** |             |
| `$behaviorName` | **string**                      |             |

***
