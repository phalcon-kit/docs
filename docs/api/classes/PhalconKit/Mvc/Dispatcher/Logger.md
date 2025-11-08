
***

* Full name: `\PhalconKit\Mvc\Dispatcher\Logger`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### isEnabled

Check if the logger is currently enabled or not from the config

```php
public isEnabled(): bool
```

***

### beforeDispatchLoop

This action is executed before execute any action in the application
Keeping a log of the dispatch event

```php
public beforeDispatchLoop(\Phalcon\Events\Event $event, \PhalconKit\Dispatcher\DispatcherInterface $dispatcher): void
```

**Parameters:**

| Parameter     | Type                                           | Description |
|---------------|------------------------------------------------|-------------|
| `$event`      | **\Phalcon\Events\Event**                      |             |
| `$dispatcher` | **\PhalconKit\Dispatcher\DispatcherInterface** |             |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
