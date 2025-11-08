
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\BlameableInterface`
* Parent interfaces:
  [`\PhalconKit\Mvc\Model\Interfaces\Blameable\BlameAtInterface`](./Blameable/BlameAtInterface.md),
  [`\PhalconKit\Mvc\Model\Interfaces\Blameable\CreatedInterface`](./Blameable/CreatedInterface.md),
  [`\PhalconKit\Mvc\Model\Interfaces\Blameable\DeletedInterface`](./Blameable/DeletedInterface.md),
  [`\PhalconKit\Mvc\Model\Interfaces\Blameable\RestoredInterface`](./Blameable/RestoredInterface.md),
  [`\PhalconKit\Mvc\Model\Interfaces\Blameable\UpdatedInterface`](./Blameable/UpdatedInterface.md)

## Methods

### initializeBlameable

```php
public initializeBlameable(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setBlameableBehavior

```php
public setBlameableBehavior(\PhalconKit\Mvc\Model\Behavior\Blameable $blameableBehavior): void
```

**Parameters:**

| Parameter            | Type                                         | Description |
|----------------------|----------------------------------------------|-------------|
| `$blameableBehavior` | **\PhalconKit\Mvc\Model\Behavior\Blameable** |             |

***

### getBlameableBehavior

```php
public getBlameableBehavior(): \PhalconKit\Mvc\Model\Behavior\Blameable
```

***

### addUserRelationship

```php
public addUserRelationship(string $field = 'userId', string $alias = 'UserEntity', array $params = [], string $ref = 'id', string $type = 'belongsTo', ?string $class = null): ?\Phalcon\Mvc\Model\Relation
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$field`  | **string**  |             |
| `$alias`  | **string**  |             |
| `$params` | **array**   |             |
| `$ref`    | **string**  |             |
| `$type`   | **string**  |             |
| `$class`  | **?string** |             |

***

## Inherited methods

### initializeUpdated

```php
public initializeUpdated(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setUpdatedBehavior

```php
public setUpdatedBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $updatedBehavior): void
```

**Parameters:**

| Parameter          | Type                                             | Description |
|--------------------|--------------------------------------------------|-------------|
| `$updatedBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getUpdatedBehavior

```php
public getUpdatedBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### initializeRestored

```php
public initializeRestored(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setRestoredBehavior

```php
public setRestoredBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $restoredBehavior): void
```

**Parameters:**

| Parameter           | Type                                             | Description |
|---------------------|--------------------------------------------------|-------------|
| `$restoredBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getRestoredBehavior

```php
public getRestoredBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### initializeDeleted

```php
public initializeDeleted(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setDeletedBehavior

```php
public setDeletedBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $deletedBehavior): void
```

**Parameters:**

| Parameter          | Type                                             | Description |
|--------------------|--------------------------------------------------|-------------|
| `$deletedBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getDeletedBehavior

```php
public getDeletedBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### initializeCreated

```php
public initializeCreated(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setCreatedBehavior

```php
public setCreatedBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $createdBehavior): void
```

**Parameters:**

| Parameter          | Type                                             | Description |
|--------------------|--------------------------------------------------|-------------|
| `$createdBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getCreatedBehavior

```php
public getCreatedBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### getDateCallback

```php
public getDateCallback(string $format, ?int $timestamp = null): \Closure
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$format`    | **string** |             |
| `$timestamp` | **?int**   |             |

***
