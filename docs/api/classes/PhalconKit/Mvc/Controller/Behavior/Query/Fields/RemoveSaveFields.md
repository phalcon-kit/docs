
Clears saveable-field rules after REST field initialization.

Use this listener when an action should not use the controller's configured
create/update field allow-list during payload normalization.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Fields\RemoveSaveFields`

## Methods

### afterInitializeFields

Remove every saveable-field rule from the controller field state.

```php
public afterInitializeFields(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                    |
|---------------|----------------------------------------|----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after field initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose save fields should be cleared.           |

***
