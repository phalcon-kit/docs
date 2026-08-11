
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
### getTypedBehavior

Retrieve a named behavior and require a specific behavior implementation.

```php
protected getTypedBehavior(string $behaviorName, class-string<\PhalconKit\Mvc\Model\Traits\Abstracts\TBehavior> $expectedClass): \PhalconKit\Mvc\Model\Traits\Abstracts\TBehavior
```

Model feature traits use this helper for public getters such as
`getUuidBehavior()` and `getSoftDeleteBehavior()`. The concrete
implementation lives in the shared behavior trait so each feature trait
can return a stable PhalconKit exception when a behavior was not
initialized, instead of relying on PHP assertions or late return-type
errors.

* This method is **abstract**.
**Parameters:**

| Parameter        | Type                                                               | Description                           |
|------------------|--------------------------------------------------------------------|---------------------------------------|
| `$behaviorName`  | **string**                                                         | Registry key used by the initializer. |
| `$expectedClass` | **class-string<\PhalconKit\Mvc\Model\Traits\Abstracts\TBehavior>** | Expected behavior class.              |

**Return Value:**

Registered behavior narrowed to the expected type.

**Throws:**

When the behavior is
missing or does not match the expected class.
- [`ServiceException`](../../../../Exception/ServiceException.md)

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
