
Removes the default soft-delete condition only when the request filters by deletion state.

This lets endpoints keep normal "not deleted" behavior by default, while
allowing explicit `deleted` filters to include deleted rows or select only
deleted rows according to the request filter value.

***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultSoftDeleteConditionWhileFiltering`

## Methods

### afterInitializeConditions

Drop the `default` soft-delete condition when a `deleted` filter is present.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | Controller lifecycle event emitted after condition initialization. |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | REST controller whose soft-delete conditions should be adjusted.   |

**Throws:**

When reading or sanitizing request filter parameters fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
