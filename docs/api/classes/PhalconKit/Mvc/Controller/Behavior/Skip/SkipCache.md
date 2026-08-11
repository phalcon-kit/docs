
Behavior flag that disables REST query cache-option initialization.

Attach this to actions that must bypass controller-level cache configuration
and let the model query run without generated cache options.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipCache`

## Methods

### getCache

Tell the REST controller to skip cache configuration initialization.

```php
public getCache(): false
```

**Return Value:**

Always disables cache options for the action.

***
