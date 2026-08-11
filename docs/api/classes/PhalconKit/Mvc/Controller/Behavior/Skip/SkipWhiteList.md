
Behavior flag that disables whitelist initialization.

Attach this when an action must not apply the controller's configured field
whitelist while normalizing request data or query state.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipWhiteList`

## Methods

### getWhiteList

Tell the REST controller to skip whitelist initialization.

```php
public getWhiteList(): false
```

**Return Value:**

Always disables whitelist state for the action.

***
