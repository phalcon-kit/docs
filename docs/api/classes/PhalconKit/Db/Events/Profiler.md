
Class Profiler

***

* Full name: `\PhalconKit\Db\Events\Profiler`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### isEnabled

Check if the profiler is currently enabled or not from the config

```php
public isEnabled(): bool
```

***

### beforeQuery

Start the current profile if profiler is enabled

```php
public beforeQuery(\Phalcon\Events\EventInterface $event, \Phalcon\Db\Adapter\AbstractAdapter $connection): void
```

**Parameters:**

| Parameter     | Type                                    | Description |
|---------------|-----------------------------------------|-------------|
| `$event`      | **\Phalcon\Events\EventInterface**      |             |
| `$connection` | **\Phalcon\Db\Adapter\AbstractAdapter** |             |

***

### afterQuery

Stop the current profile

```php
public afterQuery(\Phalcon\Events\EventInterface $event, \Phalcon\Db\Adapter\AbstractAdapter $connection): void
```

**Parameters:**

| Parameter     | Type                                    | Description |
|---------------|-----------------------------------------|-------------|
| `$event`      | **\Phalcon\Events\EventInterface**      |             |
| `$connection` | **\Phalcon\Db\Adapter\AbstractAdapter** |             |

***
