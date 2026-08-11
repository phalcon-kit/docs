
Removes the default soft-delete condition after condition assembly.

This legacy skip behavior is still useful in permission config that predates
the newer query-condition remover classes. It keeps the broader condition
pipeline active while removing only the `softDelete` group from the combined
condition collection.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Skip\SkipSoftDeleteCondition`

## Methods

### afterConditions

Remove the combined soft-delete condition group from the controller.

```php
public afterConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                          |
|---------------|----------------------------------------|----------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after conditions are initialized. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose combined conditions should be adjusted.        |

***
