
Shared typed accessor for the model cache service.

Model traits use this helper when they are invoked through native Phalcon
model lifecycle hooks and only have access to the model's DI container. It
centralizes the PhalconKit DI contract check for the `modelsCache` service.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Abstracts\AbstractModelsCache`

## Methods

### getModelsCache

Resolve the shared model cache service from the current model DI.

```php
public getModelsCache(): \Phalcon\Cache\Cache
```

**Return Value:**

Cache service used by model cache invalidation helpers.

**Throws:**

When the modelsCache service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../../Exception/ServiceException.md)

***
