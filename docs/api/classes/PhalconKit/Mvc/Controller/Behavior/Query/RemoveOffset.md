
Resets request/configured pagination offset after offset initialization.

Attach this listener when an action should always start at the first result
while preserving the rest of the controller's pagination/query state.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveOffset`

## Methods

### afterInitializeOffset

Reset the controller offset to the first row.

```php
public afterInitializeOffset(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                     |
|---------------|----------------------------------------|-----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after offset initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose offset should be reset.                   |

***
