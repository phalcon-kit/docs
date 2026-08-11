
Removes only the default request-filter condition after condition initialization.

This keeps custom filter conditions configured by the application while
suppressing the framework's default filter predicate for the action.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultFilterCondition`

## Methods

### afterInitializeConditions

Remove the `default` filter condition entry from the controller.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose filter conditions should be adjusted.        |

***
