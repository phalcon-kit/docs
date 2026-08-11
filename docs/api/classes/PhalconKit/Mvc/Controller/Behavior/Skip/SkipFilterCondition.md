
Behavior flag that disables request-filter condition initialization.

Use this for endpoints where request filter parameters should not generate
SQL/PHQL conditions automatically.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipFilterCondition`

## Methods

### getFilterCondition

Tell the REST controller to skip filter condition initialization.

```php
public getFilterCondition(): false
```

**Return Value:**

Always disables request-filter conditions for the action.

***
