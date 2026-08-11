
Behavior flag that disables distinct-expression initialization.

Attach this when an action must not inherit configured `DISTINCT` handling
from the REST query builder.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipDistinct`

## Methods

### getDistinct

Tell the REST controller to skip distinct collection initialization.

```php
public getDistinct(): false
```

**Return Value:**

Always disables distinct query state for the action.

***
