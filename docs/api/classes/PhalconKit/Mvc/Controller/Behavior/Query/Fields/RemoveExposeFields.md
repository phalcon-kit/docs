
Clears exposed-field rules after REST field initialization.

Attach this listener when an action should not apply the controller's
configured response-exposure field policy.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Fields\RemoveExposeFields`

## Methods

### afterInitializeFields

Remove every exposed-field rule from the controller field state.

```php
public afterInitializeFields(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                    |
|---------------|----------------------------------------|----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after field initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose exposed fields should be cleared.        |

***
