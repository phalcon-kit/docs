
Removes only the default soft-delete condition after initialization.

Attach this when an action needs visibility into soft-deleted rows while
retaining any application-defined soft-delete predicates.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultSoftDeleteCondition`

## Methods

### afterInitializeConditions

Remove the `default` soft-delete condition entry from the controller.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose soft-delete conditions should be adjusted.   |

***
