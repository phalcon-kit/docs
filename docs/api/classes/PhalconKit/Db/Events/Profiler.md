
Database event listener that feeds executed queries into the profiler.

Attach this class to a database connection events manager to start a profile
before each query and stop it afterwards. Profiling is controlled by
`app.profiler`, falling back to `profiler.enable`, so applications can keep
the listener registered while disabling collection in production.

***

* Full name: `\PhalconKit\Db\Events\Profiler`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### isEnabled

Determine whether query profiling is enabled by configuration.

```php
public isEnabled(): bool
```

***

### beforeQuery

Start profiling the SQL statement about to be executed.

```php
public beforeQuery(\Phalcon\Contracts\Events\Event $event, \Phalcon\Db\Adapter\AbstractAdapter $connection): void
```

Stopped events are ignored so listeners earlier in the chain can cancel
profiling together with the query.

**Parameters:**

| Parameter     | Type                                    | Description                                        |
|---------------|-----------------------------------------|----------------------------------------------------|
| `$event`      | **\Phalcon\Contracts\Events\Event**     | Database `beforeQuery` event.                      |
| `$connection` | **\Phalcon\Db\Adapter\AbstractAdapter** | Connection that is about to execute
the statement. |

***

### afterQuery

Stop the active query profile after execution.

```php
public afterQuery(\Phalcon\Contracts\Events\Event $event, \Phalcon\Db\Adapter\AbstractAdapter $connection): void
```

**Parameters:**

| Parameter     | Type                                    | Description                             |
|---------------|-----------------------------------------|-----------------------------------------|
| `$event`      | **\Phalcon\Contracts\Events\Event**     | Database `afterQuery` event.            |
| `$connection` | **\Phalcon\Db\Adapter\AbstractAdapter** | Connection that executed the statement. |

***
