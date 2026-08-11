
Disables default pagination before REST query initialization.

This listener sets both `maxLimit` and `limit` to `-1`, the framework
sentinel used for unrestricted queries, before request/configured pagination
state is assembled.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveDefaultLimit`

## Methods

### beforeInitializeQuery

Disable the maximum and current limits before query state is built.

```php
public beforeInitializeQuery(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                     |
|---------------|----------------------------------------|-----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted before query initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose pagination defaults should be disabled.   |

***
