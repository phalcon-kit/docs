
Clears all request-filter conditions after condition initialization.

Attach this when an action should ignore every controller-managed filter
predicate, including both default and application-provided filter rules.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveFilterConditions`

## Methods

### afterInitializeConditions

Remove every filter condition from the controller query state.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose filter conditions should be cleared.         |

***
