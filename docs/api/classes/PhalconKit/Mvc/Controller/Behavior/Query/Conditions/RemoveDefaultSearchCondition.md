
Removes only the default search condition after initialization.

This keeps custom search predicates intact while disabling the framework's
generated request-search condition for the action.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultSearchCondition`

## Methods

### afterInitializeConditions

Remove the `default` search condition entry from the controller.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose search conditions should be adjusted.        |

***
