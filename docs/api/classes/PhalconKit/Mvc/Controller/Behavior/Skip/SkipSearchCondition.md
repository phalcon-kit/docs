
Behavior flag that disables search condition initialization.

Use this when request search parameters should not be converted into
controller-managed search predicates.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipSearchCondition`

## Methods

### getSearchCondition

Tell the REST controller to skip search condition initialization.

```php
public getSearchCondition(): false
```

**Return Value:**

Always disables search conditions for the action.

***
