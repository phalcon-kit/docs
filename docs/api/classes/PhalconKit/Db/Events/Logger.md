
Responsible for logging database query events.

***

* Full name: `\PhalconKit\Db\Events\Logger`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Properties

### inProgress

```php
public bool $inProgress
```

***

## Methods

### beforeQuery

Executes before a database query is executed.

```php
public beforeQuery(\Phalcon\Contracts\Events\Event $event, \Phalcon\Db\Adapter\AbstractAdapter $connection): void
```

**Parameters:**

| Parameter     | Type                                    | Description                     |
|---------------|-----------------------------------------|---------------------------------|
| `$event`      | **\Phalcon\Contracts\Events\Event**     | The event object.               |
| `$connection` | **\Phalcon\Db\Adapter\AbstractAdapter** | The database connection object. |

**Throws:**

If Phalcon cannot write the query log entry.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
