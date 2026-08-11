
Behavior flag that disables REST query bind initialization for an action.

Attach this behavior when an action must ignore request/configured bind
values and leave the final Phalcon find options without a `bind` entry.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipBind`

## Methods

### getBind

Tell the REST controller to skip bind collection initialization.

```php
public getBind(): false
```

**Return Value:**

Always disables bind values for the behavior-aware action.

***
