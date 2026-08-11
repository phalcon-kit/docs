
Behavior flag that disables identity-scope condition initialization.

Attach this only for actions that deliberately bypass authenticated identity
scoping, such as public resources or framework-maintained internal queries.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipIdentityCondition`

## Methods

### getIdentityCondition

Tell the REST controller to skip identity condition initialization.

```php
public getIdentityCondition(): false
```

**Return Value:**

Always disables identity-scope conditions for the action.

***
