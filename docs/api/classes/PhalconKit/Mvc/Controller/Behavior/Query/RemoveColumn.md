
Clears configured query columns after column initialization.

Use this listener when an action should fall back to the model/default
projection instead of controller-level selected or calculated columns.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveColumn`

## Methods

### afterInitializeColumn

Remove every configured column from the controller query state.

```php
public afterInitializeColumn(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                     |
|---------------|----------------------------------------|-----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after column initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose column collection should be cleared.      |

***
