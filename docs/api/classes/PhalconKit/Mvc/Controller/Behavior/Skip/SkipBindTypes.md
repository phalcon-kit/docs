
Behavior flag that disables REST query bind-type initialization.

This is useful together with

- **See:** \PhalconKit\Mvc\Controller\Behavior\Skip\SkipBind when an action should not pass
request/configured bind metadata into the compiled Phalcon query options.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipBindTypes`

## Methods

### getBindTypes

Tell the REST controller to skip bind-type collection initialization.

```php
public getBindTypes(): false
```

**Return Value:**

Always disables bind-type values for the action.

***
