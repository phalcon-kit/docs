
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\BehaviorInterface`

## Methods

### addBehavior

```php
public addBehavior(\Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

**Parameters:**

| Parameter   | Type                                     | Description |
|-------------|------------------------------------------|-------------|
| `$behavior` | **\Phalcon\Mvc\Model\BehaviorInterface** |             |

***

### getBehavior

```php
public getBehavior(string $behaviorName): ?\Phalcon\Mvc\Model\BehaviorInterface
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***

### setBehavior

```php
public setBehavior(string $behaviorName, \Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

**Parameters:**

| Parameter       | Type                                     | Description |
|-----------------|------------------------------------------|-------------|
| `$behaviorName` | **string**                               |             |
| `$behavior`     | **\Phalcon\Mvc\Model\BehaviorInterface** |             |

***

### hasBehavior

```php
public hasBehavior(string $behaviorName): bool
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***

### removeBehavior

```php
public removeBehavior(string $behaviorName): void
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***
