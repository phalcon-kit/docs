
***

* Full name: `\PhalconKit\Mvc\Controller\Behavior\Query\Conditions\RemoveDefaultSoftDeleteConditionWhileFiltering`

## Methods

### afterInitializeConditions

Handles the initialization of conditions after the controller is set up.

```php
public afterInitializeConditions(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Controller\Restful $controller): void
```

Removes the default soft delete condition if the specified filtering parameters are present.

**Parameters:**

| Parameter     | Type                                   | Description                                                                                      |
|---------------|----------------------------------------|--------------------------------------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**              | The event instance triggered during the controller's lifecycle.                                  |
| `$controller` | **\PhalconKit\Mvc\Controller\Restful** | The controller instance being processed, containing methods for managing filters and conditions. |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
