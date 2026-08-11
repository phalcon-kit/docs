
Behavior flag that disables the combined REST condition collection.

This bypasses condition assembly for actions that intentionally build their
own query or should run without controller-managed filtering constraints.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipConditions`

## Methods

### getConditions

Tell the REST controller to skip condition collection initialization.

```php
public getConditions(): false
```

**Return Value:**

Always disables the combined condition collection.

***
