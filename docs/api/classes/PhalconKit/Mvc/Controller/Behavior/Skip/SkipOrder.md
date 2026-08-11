
Behavior flag that disables order-by initialization.

Use this for actions that need deterministic ordering outside the standard
REST order policy or must avoid request-driven sorting.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipOrder`

## Methods

### getOrder

Tell the REST controller to skip order collection initialization.

```php
public getOrder(): false
```

**Return Value:**

Always disables order-by query state for the action.

***
