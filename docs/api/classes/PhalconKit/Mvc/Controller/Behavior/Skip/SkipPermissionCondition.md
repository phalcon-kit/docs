
Behavior flag that disables permission condition initialization.

Attach this only when an action intentionally bypasses permission-derived
query predicates and enforces access through another explicit mechanism.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipPermissionCondition`

## Methods

### getPermissionConditions

Tell the REST controller to skip permission condition initialization.

```php
public getPermissionConditions(): false
```

**Return Value:**

Always disables permission conditions for the action.

***
