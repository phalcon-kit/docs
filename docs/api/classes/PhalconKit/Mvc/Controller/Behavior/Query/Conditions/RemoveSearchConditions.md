
Clears all search conditions after condition initialization.

Use this when request search parameters should be ignored entirely by the
controller query builder.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveSearchConditions`

## Methods

### afterInitializeConditions

Remove every search condition from the controller query state.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose search conditions should be cleared.         |

***
