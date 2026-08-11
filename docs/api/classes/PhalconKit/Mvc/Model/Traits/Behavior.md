
Adds named behavior registration helpers to PhalconKit models.

Phalcon's native behavior stack is event oriented and does not expose a
first-class named registry. PhalconKit's models manager adds that registry
so model traits can install and later retrieve behaviors such as `uuid`,
`softDelete`, or `blameable` without duplicating storage on each model.

The model must be managed by `PhalconKit\Mvc\Model\ManagerInterface`; native
Phalcon-only managers cannot provide the named behavior methods and are
rejected by the shared helper in `AbstractModelsManager`.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Behavior`

## Methods

### getBehavior

Retrieve a named behavior registered for the current model.

```php
public getBehavior(string $behaviorName): \Phalcon\Mvc\Model\BehaviorInterface|null
```

This method returns null when no behavior is registered under the given
name. It does not inspect Phalcon's native event manager; it reads the
PhalconKit models-manager registry.

**Parameters:**

| Parameter       | Type       | Description                                               |
|-----------------|------------|-----------------------------------------------------------|
| `$behaviorName` | **string** | Registry key such as `uuid`, `security`, or
`softDelete`. |

**Return Value:**

Registered behavior, or null when the name
is not present.

**Throws:**

When the current models
manager does not implement the PhalconKit manager contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getTypedBehavior

Retrieve a named behavior and require the expected behavior class.

```php
protected getTypedBehavior(string $behaviorName, class-string<\PhalconKit\Mvc\Model\Traits\TBehavior> $expectedClass): \PhalconKit\Mvc\Model\Traits\TBehavior
```

The named behavior registry returns the generic Phalcon behavior
interface. Public model helper methods usually promise a concrete
behavior type, so this helper centralizes the runtime check and produces
a stable framework exception when an initializer was skipped or a behavior
name was reused with the wrong implementation.

**Parameters:**

| Parameter        | Type                                                     | Description                                  |
|------------------|----------------------------------------------------------|----------------------------------------------|
| `$behaviorName`  | **string**                                               | Registry key such as `uuid` or `softDelete`. |
| `$expectedClass` | **class-string<\PhalconKit\Mvc\Model\Traits\TBehavior>** | Expected behavior class.                     |

**Return Value:**

Registered behavior narrowed to the expected class.

**Throws:**

When the behavior is missing or has the wrong
type.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### setBehavior

Register or replace a named behavior for the current model.

```php
public setBehavior(string $behaviorName, \Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

The behavior remains associated with this model class in the PhalconKit
models manager. Callers that also need native Phalcon event notification
should continue to attach the behavior through the normal model behavior
APIs used by the specific trait.

**Parameters:**

| Parameter       | Type                                     | Description                                       |
|-----------------|------------------------------------------|---------------------------------------------------|
| `$behaviorName` | **string**                               | Registry key used to retrieve the behavior
later. |
| `$behavior`     | **\Phalcon\Mvc\Model\BehaviorInterface** | Behavior instance to register.                    |

**Throws:**

When the current models
manager does not implement the PhalconKit manager contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### hasBehavior

Determine whether a named behavior is registered for the current model.

```php
public hasBehavior(string $behaviorName): bool
```

This is a lightweight registry check and does not instantiate or resolve
behavior services.

**Parameters:**

| Parameter       | Type       | Description              |
|-----------------|------------|--------------------------|
| `$behaviorName` | **string** | Registry key to inspect. |

**Return Value:**

True when the behavior name exists for this model.

**Throws:**

When the current models
manager does not implement the PhalconKit manager contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### removeBehavior

Remove a named behavior from the current model registry.

```php
public removeBehavior(string $behaviorName): void
```

Removing a missing behavior is treated as a no-op by the models manager.
This method updates the PhalconKit registry only; it does not detach
arbitrary listeners from a native Phalcon events manager.

**Parameters:**

| Parameter       | Type       | Description             |
|-----------------|------------|-------------------------|
| `$behaviorName` | **string** | Registry key to remove. |

**Throws:**

When the current models
manager does not implement the PhalconKit manager contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getBehaviorModel

Require the trait host to be a Phalcon model instance.

```php
private getBehaviorModel(): \Phalcon\Mvc\ModelInterface
```

Model behavior registry APIs key entries by model class. If this trait is
accidentally composed into a non-model class, failing here gives
extension authors a deterministic PhalconKit exception even when PHP
assertions are disabled.

**Throws:**

When the trait host is not a Phalcon model.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
