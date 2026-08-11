
Clears all permission conditions after condition initialization.

Attach this only when an action intentionally replaces permission-derived
predicates with another explicit authorization mechanism.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemovePermissionConditions`

## Methods

### afterInitializeConditions

Remove every permission condition from the controller query state.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose permission conditions should be cleared.     |

***
