
Dispatcher listener that redirects traffic while maintenance mode is enabled.

The listener reads `app.maintenance` and `router.maintenance` from config and
forwards matching requests before the target controller/action runs.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Maintenance`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Constants

| Constant                         | Visibility | Type    | Value         |
|----------------------------------|------------|---------|---------------|
| `DEFAULT_MAINTENANCE_MODULE`     | public     | ?string | null          |
| `DEFAULT_MAINTENANCE_CONTROLLER` | public     | ?string | 'error'       |
| `DEFAULT_MAINTENANCE_ACTION`     | public     | ?string | 'maintenance' |

## Methods

### beforeDispatch

Executed before dispatching a request.

```php
public beforeDispatch(\Phalcon\Events\Event $event, \Phalcon\Dispatcher\AbstractDispatcher $dispatcher): void
```

The plugin reads `app.maintenance` and `router.maintenance` from the
PhalconKit config service. When maintenance mode is enabled it forwards
the dispatcher to the configured maintenance route, strips null route
parts through the PhalconKit dispatcher extension when available, and
stops cancelable dispatch events so the original action is not executed.

**Parameters:**

| Parameter     | Type                                       | Description            |
|---------------|--------------------------------------------|------------------------|
| `$event`      | **\Phalcon\Events\Event**                  | The event object.      |
| `$dispatcher` | **\Phalcon\Dispatcher\AbstractDispatcher** | The dispatcher object. |

**Throws:**

If an error happened during the dispatch
forwarding to the maintenance route.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the DI container or config service cannot
be resolved through the PhalconKit DI contract.
- [`ServiceException`](../../Exception/ServiceException.md)

***
