
Installs audit/user attribution behavior and user relationships on models.

The trait wires the `Blameable` behavior with model classes resolved from
the shared `models` service, so consuming applications can override core
model classes through the normal model-map configuration. It also adds a
belongs-to relationship to the configured user model when the target field
exists on the model.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Blameable`

## Methods

### initializeBlameable

Initialize the blameable behavior and user relationship.

```php
public initializeBlameable(array<array-key,mixed>|null $options = null): void
```

When no options are provided, the trait reads `blameable` options from
the model options manager. Missing audit, audit-detail, and user classes
are filled from the PhalconKit `models` service so applications using
custom model classes keep one central mapping.

**Parameters:**

| Parameter  | Type                             | Description                                                                                                                                                                                                                                   |
|------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$options` | **array<array-key,mixed>\|null** | Behavior options. Common
keys include `auditClass`, `auditDetailClass`, `userClass`,
`userField`, `auditEnabled`, and `auditDetailEnabled`. Audit is
opt-in; set `auditEnabled` to `true` for applications that install
and use audit tables. |

**Throws:**

When the models service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### setBlameableBehavior

Register the blameable behavior under the standard behavior name.

```php
public setBlameableBehavior(\PhalconKit\Mvc\Model\Behavior\Blameable $blameableBehavior): void
```

The behavior is stored in the PhalconKit model behavior registry as
`blameable`, which lets other traits and application code retrieve the
same instance later.

**Parameters:**

| Parameter            | Type                                         | Description                   |
|----------------------|----------------------------------------------|-------------------------------|
| `$blameableBehavior` | **\PhalconKit\Mvc\Model\Behavior\Blameable** | Configured behavior instance. |

**Throws:**

When the current models manager does not expose
the PhalconKit behavior registry.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getBlameableBehavior

Retrieve the registered blameable behavior.

```php
public getBlameableBehavior(): \PhalconKit\Mvc\Model\Behavior\Blameable
```

**Throws:**

When the current models manager does not expose
the PhalconKit behavior registry.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### addUserRelationship

Add a user relationship when the configured attribution field exists.

```php
public addUserRelationship(string $field = 'userId', string $alias = 'UserEntity', array<array-key,mixed> $params = [], string $ref = 'id', string $type = 'belongsTo', string|null $class = null): \Phalcon\Mvc\Model\Relation|null
```

**Parameters:**

| Parameter | Type                       | Description                                                                              |
|-----------|----------------------------|------------------------------------------------------------------------------------------|
| `$field`  | **string**                 |                                                                                          |
| `$alias`  | **string**                 | The alias name for the user entity. Default is 'UserEntity'.                             |
| `$params` | **array<array-key,mixed>** | Additional relationship
parameters.                                                      |
| `$ref`    | **string**                 | The reference field in the user entity. Default is 'id'.                                 |
| `$type`   | **string**                 | Relationship method to call on the model, usually
`belongsTo`.                           |
| `$class`  | **string\|null**           | User model class. When null, the class is
resolved from the PhalconKit `models` service. |

**Return Value:**

Created relationship, or null when the model does
not expose the configured attribution field.

**Throws:**

When the models service cannot be resolved while
deriving the default user class.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
