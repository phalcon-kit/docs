
Clears searchable-field rules after REST field initialization.

Attach this listener when request search terms should not be mapped across
the controller's configured searchable field set.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Fields\RemoveSearchFields`

## Methods

### afterInitializeFields

Remove every searchable-field rule from the controller field state.

```php
public afterInitializeFields(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                    |
|---------------|----------------------------------------|----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after field initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose search fields should be cleared.         |

***
