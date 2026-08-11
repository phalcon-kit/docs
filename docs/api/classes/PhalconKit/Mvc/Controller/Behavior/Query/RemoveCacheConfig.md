
Clears REST cache options after cache configuration is initialized.

Attach this listener to endpoints that should bypass controller-level query
caching without disabling the rest of the find-option preparation pipeline.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveCacheConfig`

## Methods

### afterInitializeCacheConfig

Remove every cache option from the controller query state.

```php
public afterInitializeCacheConfig(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                           |
|---------------|----------------------------------------|-----------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after cache config initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose cache config should be cleared.                 |

***
