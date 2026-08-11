
Abstract identity contract required by model traits that need user context.

Traits such as blameable timestamp/user attribution depend on the consuming
model exposing identity helpers. Keeping the contract here avoids coupling
those traits to a concrete model class.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Abstracts\AbstractIdentity`

## Methods

### getIdentityService

Resolve the identity manager used by blameable model helpers.

```php
public getIdentityService(): \PhalconKit\Identity\ManagerInterface
```

Implementing traits provide the concrete lookup and should fail with a
stable PhalconKit service exception when the DI service is unavailable or
does not implement the identity manager contract.

* This method is **abstract**.
**Return Value:**

Current identity manager service.

**Throws:**

When the identity service
cannot be resolved through the PhalconKit DI contract.
- [`ServiceException`](../../../../Exception/ServiceException.md)

***
