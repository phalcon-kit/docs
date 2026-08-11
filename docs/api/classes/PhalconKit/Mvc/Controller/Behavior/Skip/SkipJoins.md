
Behavior flag that disables REST join initialization.

Attach this when an action should not inherit configured joins, dynamic
joins, or relation joins from the controller query policy.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipJoins`

## Methods

### getJoins

Tell the REST controller to skip join collection initialization.

```php
public getJoins(): false
```

**Return Value:**

Always disables join query state for the action.

***
