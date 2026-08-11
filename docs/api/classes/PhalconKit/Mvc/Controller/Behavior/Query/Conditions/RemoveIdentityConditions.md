
Clears all identity-scope conditions after condition initialization.

Use this only for actions that intentionally bypass identity-derived query
scoping and enforce access through another explicit policy.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveIdentityConditions`

## Methods

### afterInitializeConditions

Remove every identity condition from the controller query state.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose identity conditions should be cleared.       |

***
