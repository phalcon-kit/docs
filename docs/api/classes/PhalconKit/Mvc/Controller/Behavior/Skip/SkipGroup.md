
Behavior flag that disables group-by initialization.

Attach this when an action must not carry configured or request-derived
grouping into the final model query.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipGroup`

## Methods

### getGroup

Tell the REST controller to skip group collection initialization.

```php
public getGroup(): false
```

**Return Value:**

Always disables group-by query state for the action.

***
