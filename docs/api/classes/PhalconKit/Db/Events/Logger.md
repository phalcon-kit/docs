
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

### connectionLost

Log that Phalcon detected a lost PDO connection.

```php
public connectionLost(\Phalcon\Contracts\Events\Event $event, \Phalcon\Db\Adapter\AbstractAdapter $connection): void
```

The event is emitted before an enabled adapter attempts its single
automatic reconnect. Query text and bind values are intentionally omitted
because the lost-connection payload can occur on sensitive operations.

**Parameters:**

| Parameter     | Type                                    | Description                                  |
|---------------|-----------------------------------------|----------------------------------------------|
| `$event`      | **\Phalcon\Contracts\Events\Event**     | Connection-lost event and reconnect context. |
| `$connection` | **\Phalcon\Db\Adapter\AbstractAdapter** | Connection whose state was lost.             |

**Throws:**

If Phalcon cannot write the database log entry.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
