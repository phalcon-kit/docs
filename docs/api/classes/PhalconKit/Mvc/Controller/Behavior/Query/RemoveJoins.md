
Clears configured and dynamic joins after join initialization.

Use this listener for actions that should query only the root model while
leaving other controller query state, such as filters or limits, available.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveJoins`

## Methods

### afterInitializeJoins

Remove every join definition from the controller query state.

```php
public afterInitializeJoins(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                   |
|---------------|----------------------------------------|---------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after join initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose join collection should be cleared.      |

***
