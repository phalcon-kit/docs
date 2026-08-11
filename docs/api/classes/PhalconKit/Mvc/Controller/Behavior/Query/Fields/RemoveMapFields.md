
Clears API-to-model field mapping rules after field initialization.

Attach this listener when an action should not use controller field aliases
or mapped field names while preparing query/save state.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Fields\RemoveMapFields`

## Methods

### afterInitializeFields

Remove every field mapping rule from the controller field state.

```php
public afterInitializeFields(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                    |
|---------------|----------------------------------------|----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after field initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose field map should be cleared.             |

***
