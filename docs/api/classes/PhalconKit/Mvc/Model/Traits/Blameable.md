
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Blameable`

## Methods

### initializeBlameable

Initialize Blameable

```php
public initializeBlameable(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                       |
|------------|-----------------|-----------------------------------|
| `$options` | **array\|null** | Options for the BlameableBehavior |

***
### setBlameableBehavior

Set Blameable Behavior.

```php
public setBlameableBehavior(\PhalconKit\Mvc\Model\Behavior\Blameable $blameableBehavior): void
```

**Parameters:**

| Parameter            | Type                                         | Description                              |
|----------------------|----------------------------------------------|------------------------------------------|
| `$blameableBehavior` | **\PhalconKit\Mvc\Model\Behavior\Blameable** | The `BlameableBehavior` instance to set. |

***
### getBlameableBehavior

Retrieves the BlameableBehavior instance associated with the current object.

```php
public getBlameableBehavior(): \PhalconKit\Mvc\Model\Behavior\Blameable
```

**Return Value:**

The BlameableBehavior instance.

***
### addUserRelationship

Adds a relationship between the current object and a user entity.

```php
public addUserRelationship(string $field = 'userId', string $alias = 'UserEntity', array $params = [], string $ref = 'id', string $type = 'belongsTo', string|null $class = null): \Phalcon\Mvc\Model\Relation|null
```

**Parameters:**

| Parameter | Type             | Description                                                                                                    |
|-----------|------------------|----------------------------------------------------------------------------------------------------------------|
| `$field`  | **string**       | The field name to create the relationship on. Default is 'userId'.                                             |
| `$alias`  | **string**       | The alias name for the user entity. Default is 'UserEntity'.                                                   |
| `$params` | **array**        | Additional parameters for the relationship. Default is an empty array.                                         |
| `$ref`    | **string**       | The reference field in the user entity. Default is 'id'.                                                       |
| `$type`   | **string**       | The type of relationship to create. Default is 'belongsTo'.                                                    |
| `$class`  | **string\|null** | The class name of the user entity. If null, it will be obtained from the identity or the global configuration. |

**Return Value:**

The created relationship object, or null if the specified field does not exist in the current object.

***
