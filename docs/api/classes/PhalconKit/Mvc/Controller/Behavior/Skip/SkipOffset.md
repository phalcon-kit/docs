
Behavior flag that disables offset initialization.

Attach this when an action should ignore request/configured pagination
offsets and manage row positioning itself.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipOffset`

## Methods

### getOffset

Tell the REST controller to skip offset initialization.

```php
public getOffset(): false
```

**Return Value:**

Always disables offset query state for the action.

***
