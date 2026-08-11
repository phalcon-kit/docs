
Behavior flag that disables HAVING-clause initialization.

Use this with aggregate/grouped endpoints that need full control over their
HAVING predicates instead of the REST controller defaults.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipHaving`

## Methods

### getHaving

Tell the REST controller to skip HAVING collection initialization.

```php
public getHaving(): false
```

**Return Value:**

Always disables HAVING query state for the action.

***
