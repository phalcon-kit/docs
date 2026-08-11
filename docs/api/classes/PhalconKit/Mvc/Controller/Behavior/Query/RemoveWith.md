
Clears eager-loading relation requests after `with` initialization.

Use this listener when an action should not honor configured or request
eager-loading relation graphs.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveWith`

## Methods

### afterInitializeWith

Remove every eager-loading relation from the controller query state.

```php
public afterInitializeWith(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                       |
|---------------|----------------------------------------|-------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after `with` initialization.   |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose eager-loading collection should be cleared. |

***
