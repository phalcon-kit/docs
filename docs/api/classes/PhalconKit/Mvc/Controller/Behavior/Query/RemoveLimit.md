
Resets the current limit to the configured maximum after limit initialization.

This listener keeps the action bounded by the controller maximum while
discarding a narrower request/configured limit selected earlier in the
initialization pipeline.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveLimit`

## Methods

### afterInitializeLimit

Replace the current limit with the controller maximum limit.

```php
public afterInitializeLimit(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                    |
|---------------|----------------------------------------|----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after limit initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose current limit should be reset.           |

***
