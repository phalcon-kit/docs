
Clears the combined condition collection after REST conditions are initialized.

Attach this only when an action intentionally drops all controller-managed
predicates and supplies its own query constraints elsewhere.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\RemoveConditions`

## Methods

### afterInitializeConditions

Remove every combined condition group from the controller query state.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose condition collection should be cleared.      |

***
