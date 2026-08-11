
Clears filterable-field rules after REST field initialization.

Use this listener when an action should not accept configured/requested
filter fields through the standard REST field policy.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Fields\RemoveFilterFields`

## Methods

### afterInitializeFields

Remove every filterable-field rule from the controller field state.

```php
public afterInitializeFields(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                    |
|---------------|----------------------------------------|----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after field initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose filter fields should be cleared.         |

***
