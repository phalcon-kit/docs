
Removes only the default identity-scope condition after initialization.

Attach this when an action should not apply the framework-generated identity
predicate but should keep any custom identity conditions configured by the
application.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultIdentityCondition`

## Methods

### afterInitializeConditions

Remove the `default` identity condition entry from the controller.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose identity conditions should be adjusted.      |

***
