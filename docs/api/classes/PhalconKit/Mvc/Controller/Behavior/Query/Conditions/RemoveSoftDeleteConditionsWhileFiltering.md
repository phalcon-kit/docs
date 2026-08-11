
Clears all soft-delete conditions only when the request filters by deletion state.

This variant is stronger than

- **See:** \PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultSoftDeleteConditionWhileFiltering:
when a `deleted` filter is present, it removes every soft-delete predicate so
the explicit request filter owns deleted-row visibility.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveSoftDeleteConditionsWhileFiltering`

## Methods

### afterInitializeConditions

Clear all soft-delete conditions when a `deleted` filter is present.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose soft-delete conditions should be cleared.    |

**Throws:**

When reading or sanitizing request filter parameters fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
