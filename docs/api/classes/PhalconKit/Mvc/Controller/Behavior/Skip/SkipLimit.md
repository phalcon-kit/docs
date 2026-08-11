
Behavior flag that disables limit initialization.

Use this when an action should not receive controller/request pagination
limits before it prepares its final query.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipLimit`

## Methods

### getLimit

Tell the REST controller to skip limit initialization.

```php
public getLimit(): false
```

**Return Value:**

Always disables limit query state for the action.

***
