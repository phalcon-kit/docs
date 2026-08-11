
Disables the maximum pagination limit before REST query initialization.

The listener sets `maxLimit` to `-1`, the framework sentinel for unrestricted
result sizes, before configured/request pagination state is initialized.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveMaxLimit`

## Methods

### beforeInitializeQuery

Disable the maximum limit before query state is built.

```php
public beforeInitializeQuery(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                     |
|---------------|----------------------------------------|-----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted before query initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose maximum limit should be disabled.         |

***
