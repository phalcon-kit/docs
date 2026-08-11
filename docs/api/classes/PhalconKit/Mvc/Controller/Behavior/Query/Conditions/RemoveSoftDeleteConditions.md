
Clears all soft-delete conditions after condition initialization.

Attach this when an action needs full control over deleted-row visibility and
should remove both default and application-provided soft-delete predicates.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveSoftDeleteConditions`

## Methods

### afterInitializeConditions

Remove every soft-delete condition from the controller query state.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose soft-delete conditions should be cleared.    |

***
