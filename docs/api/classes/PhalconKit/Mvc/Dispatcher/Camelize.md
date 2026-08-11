
Normalizes dispatched controller and action names to framework method names.

The listener converts dashed, underscored, or otherwise uncamelized route
parts into the controller/action casing expected by Phalcon dispatching. It
is intentionally not registered by the default dispatcher provider because
automatic route-name rewriting can be a compatibility-sensitive behavior for
applications that rely on exact route values.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Camelize`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### beforeDispatchLoop

Normalize controller and action names before the dispatch loop runs.

```php
public beforeDispatchLoop(\Phalcon\Events\Event $event, \Phalcon\Dispatcher\AbstractDispatcher $dispatcher): void
```

MVC dispatchers also receive a ucfirst-normalized controller name so
class lookup matches conventional controller class casing. All dispatcher
types receive an lcfirst-normalized action name so `my-action` and
`my_action` resolve to `myAction`.

**Parameters:**

| Parameter     | Type                                       | Description |
|---------------|--------------------------------------------|-------------|
| `$event`      | **\Phalcon\Events\Event**                  |             |
| `$dispatcher` | **\Phalcon\Dispatcher\AbstractDispatcher** |             |

***
