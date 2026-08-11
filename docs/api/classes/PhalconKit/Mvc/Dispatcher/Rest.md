
Pass-through dispatcher listener reserved for REST dispatch customization.

The class is intentionally inert until REST-specific dispatch behavior is
promoted to a supported framework contract.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Rest`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

**See Also:**

* https://docs.phalcon.io/latest/dispatcher/

## Methods

### beforeDispatch

Allow the dispatcher to continue before a REST controller is invoked.

```php
public beforeDispatch(\Phalcon\Events\Event $event, \Phalcon\Mvc\Dispatcher $dispatcher): bool
```

The native Phalcon dispatcher event signature is kept even though the
current implementation does not need the arguments. That makes this class
a safe place to add future REST dispatch behavior without changing the
listener's public shape.

**Parameters:**

| Parameter     | Type                        | Description |
|---------------|-----------------------------|-------------|
| `$event`      | **\Phalcon\Events\Event**   |             |
| `$dispatcher` | **\Phalcon\Mvc\Dispatcher** |             |

***
