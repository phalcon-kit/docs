
Dispatcher listener that keeps the module name synchronized during forwards.

Phalcon forwards can carry a `module` route part without automatically
updating the dispatcher module name. This listener applies that route part so
downstream listeners and diagnostics see the forwarded module consistently.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Module`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### beforeForward

Apply a forwarded module name before Phalcon continues dispatching.

```php
public beforeForward(\Phalcon\Events\Event $event, \Phalcon\Dispatcher\DispatcherInterface $dispatcher, array<string,mixed> $forward): void
```

**Parameters:**

| Parameter     | Type                                        | Description                        |
|---------------|---------------------------------------------|------------------------------------|
| `$event`      | **\Phalcon\Events\Event**                   | Dispatch event emitted by Phalcon. |
| `$dispatcher` | **\Phalcon\Dispatcher\DispatcherInterface** | Active dispatcher instance.        |
| `$forward`    | **array<string,mixed>**                     | Forward route parts.               |

***
