
Clears all prepared bind values after REST bind initialization.

Attach this listener to an action when configured/request-derived bind
values should be ignored while leaving the rest of the query pipeline
enabled.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveBind`

## Methods

### afterInitializeBind

Remove every bind value from the controller query state.

```php
public afterInitializeBind(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                   |
|---------------|----------------------------------------|---------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after bind initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose bind collection should be cleared.      |

***
