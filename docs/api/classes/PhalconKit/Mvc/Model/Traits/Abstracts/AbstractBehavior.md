
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Abstracts\AbstractBehavior`

## Methods

### addBehavior

```php
public addBehavior(\Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type                                     | Description |
|-------------|------------------------------------------|-------------|
| `$behavior` | **\Phalcon\Mvc\Model\BehaviorInterface** |             |

***
### getBehavior

```php
public getBehavior(string $behaviorName): ?\Phalcon\Mvc\Model\BehaviorInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***
### setBehavior

```php
public setBehavior(string $behaviorName, \Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

* This method is **abstract**.
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

* This method is **abstract**.
**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***
### removeBehavior

```php
public removeBehavior(string $behaviorName): void
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***
