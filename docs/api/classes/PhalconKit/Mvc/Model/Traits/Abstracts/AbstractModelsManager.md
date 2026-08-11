
Shared models-manager contract helpers for model traits.

Phalcon model APIs expose the native manager interface, while PhalconKit
traits need the extended manager contract for named behavior storage. This
trait keeps that stricter check in one place and gives downstream consumers
a stable exception when a native-only manager is configured.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Abstracts\AbstractModelsManager`

## Methods

### getModelsManager

Return the native model manager assigned to the model.

```php
public getModelsManager(): \Phalcon\Mvc\Model\ManagerInterface
```

Implementations are supplied by Phalcon's model base class. The protected
helper below narrows this native contract to the PhalconKit manager when
framework-specific behavior registry APIs are required.

* This method is **abstract**.
***
### getPhalconKitModelsManager

Resolve the PhalconKit models manager extension from the current model.

```php
protected getPhalconKitModelsManager(): \PhalconKit\Mvc\Model\ManagerInterface
```

Native Phalcon exposes only `Phalcon\Mvc\Model\ManagerInterface`, but
several PhalconKit model traits need framework-specific behavior helpers
such as named behavior registration. This helper keeps that stricter
contract check in one place instead of repeating assertions in each
behavior helper.

**Return Value:**

Extended manager with PhalconKit
behavior-registry helpers.

**Throws:**

When the model manager does not expose the
PhalconKit model manager contract.
- [`ServiceException`](../../../../Exception/ServiceException.md)

***
