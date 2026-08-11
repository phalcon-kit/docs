
Dispatcher listener that logs route resolution metadata.

The listener writes one structured log entry before the dispatch loop starts
when both the global logger flag and dispatcher logger flag are enabled.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Logger`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### isEnabled

Determine whether dispatcher logging is enabled by configuration.

```php
public isEnabled(): bool
```

***

### beforeDispatchLoop

Log the current dispatcher state before action execution.

```php
public beforeDispatchLoop(\Phalcon\Events\Event $event, \PhalconKit\Dispatcher\DispatcherInterface $dispatcher): void
```

**Parameters:**

| Parameter     | Type                                           | Description                        |
|---------------|------------------------------------------------|------------------------------------|
| `$event`      | **\Phalcon\Events\Event**                      | Dispatch event emitted by Phalcon. |
| `$dispatcher` | **\PhalconKit\Dispatcher\DispatcherInterface** | Active PhalconKit dispatcher.      |

**Throws:**

When Phalcon cannot write the dispatch log entry.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
