
***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveSoftDeleteConditionsWhileFiltering`

## Methods

### afterInitializeConditions

This method is executed after initializing conditions for the given controller.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

Clears the soft delete conditions for the controller if specific filter fields are provided.

**Parameters:**

| Parameter     | Type                                   | Description                                                        |
|---------------|----------------------------------------|--------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | The event instance triggering the method.                          |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | The controller instance on which conditions are being initialized. |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
