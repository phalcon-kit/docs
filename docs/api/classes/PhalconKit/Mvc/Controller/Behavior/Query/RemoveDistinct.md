
Clears distinct query expressions after distinct initialization.

Attach this listener when an action must not inherit configured distinct
projection state from the controller query policy.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveDistinct`

## Methods

### afterInitializeDistinct

Remove every distinct expression from the controller query state.

```php
public afterInitializeDistinct(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                       |
|---------------|----------------------------------------|-------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after distinct initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose distinct collection should be cleared.      |

***
