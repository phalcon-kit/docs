
Clears group-by expressions after group initialization.

Use this listener when an action needs to ignore configured or request-driven
grouping while keeping other controller query state intact.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveGroup`

## Methods

### afterInitializeGroup

Remove every group expression from the controller query state.

```php
public afterInitializeGroup(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                    |
|---------------|----------------------------------------|----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after group initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose group collection should be cleared.      |

***
