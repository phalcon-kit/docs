
Clears HAVING predicates after HAVING initialization.

Attach this listener when aggregate/grouped endpoints need to drop
controller-managed HAVING clauses but keep the rest of the query pipeline.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveHaving`

## Methods

### afterInitializeHaving

Remove every HAVING predicate from the controller query state.

```php
public afterInitializeHaving(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                     |
|---------------|----------------------------------------|-----------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after HAVING initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose HAVING collection should be cleared.      |

***
