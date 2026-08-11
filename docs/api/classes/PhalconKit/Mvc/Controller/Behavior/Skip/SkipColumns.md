
Behavior flag that disables selected-column initialization.

Use this when an action should rely on the model/default query projection
instead of the REST controller's configured column collection.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipColumns`

## Methods

### getColumns

Tell the REST controller to skip column collection initialization.

```php
public getColumns(): false
```

**Return Value:**

Always disables configured column selection for the action.

***
