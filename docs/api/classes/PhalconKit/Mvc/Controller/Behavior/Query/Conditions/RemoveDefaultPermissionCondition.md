
Removes only the default permission condition after initialization.

Use this for actions that replace the framework-generated permission
predicate with custom permission conditions or another explicit access rule.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultPermissionCondition`

## Methods

### afterInitializeConditions

Remove the `default` permission condition entry from the controller.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose permission conditions should be adjusted.    |

***
