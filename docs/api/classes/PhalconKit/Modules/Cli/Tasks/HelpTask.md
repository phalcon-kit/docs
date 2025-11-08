
***

* Full name: `\PhalconKit\Modules\Cli\Tasks\HelpTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
```

***

## Methods

### buildAction

Build Action

```php
public buildAction(): void
```

This method executes the build action by forwarding the request to the build task's help action.

**Throws:**

if there is an error during the forwarding process
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### cronAction

Cron Action

```php
public cronAction(): void
```

This method executes the cron action by forwarding the request to the cron task's help action.

**Throws:**

if there is an error during the forwarding process
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### cacheAction

Cache Action

```php
public cacheAction(): void
```

This method executes the cache action by forwarding the request to the cache task's help action.

**Throws:**

if there is an error during the forwarding process
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

## Inherited methods

### beforeExecuteRoute

```php
public beforeExecuteRoute(): void
```

***

### helpAction

```php
public helpAction(): void
```

***

### mainAction

```php
public mainAction(): ?array
```

***

### afterExecuteRoute

Handle rest response automagically

```php
public afterExecuteRoute(\Phalcon\Cli\Dispatcher $dispatcher): void
```

**Parameters:**

| Parameter     | Type                        | Description |
|---------------|-----------------------------|-------------|
| `$dispatcher` | **\Phalcon\Cli\Dispatcher** |             |

**Throws:**

- [`CliException`](../../../Exception/CliException.md)

***
