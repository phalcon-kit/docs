
This is the security plugin which controls that users only have access to the modules they're assigned to

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Security`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### beforeDispatchLoop

This action is executed before execute any action in the application

```php
public beforeDispatchLoop(\Phalcon\Events\Event $event, \Phalcon\Dispatcher\AbstractDispatcher $dispatcher): bool
```

**Parameters:**

| Parameter     | Type                                       | Description |
|---------------|--------------------------------------------|-------------|
| `$event`      | **\Phalcon\Events\Event**                  |             |
| `$dispatcher` | **\Phalcon\Dispatcher\AbstractDispatcher** |             |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### checkAcl

Check if the current identity is allowed from the dispatcher

```php
public checkAcl(\Phalcon\Events\Event $event, ?\Phalcon\Dispatcher\AbstractDispatcher $dispatcher = null): bool
```

**Parameters:**

| Parameter     | Type                                        | Description |
|---------------|---------------------------------------------|-------------|
| `$event`      | **\Phalcon\Events\Event**                   |             |
| `$dispatcher` | **?\Phalcon\Dispatcher\AbstractDispatcher** |             |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
