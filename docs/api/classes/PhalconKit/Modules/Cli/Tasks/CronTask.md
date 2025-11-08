
***

* Full name: `\PhalconKit\Modules\Cli\Tasks\CronTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
```

***

## Methods

### mainAction

```php
public mainAction(): ?array
```

***

### hourlyAction

```php
public hourlyAction(): ?array
```

***

### dailyAction

```php
public dailyAction(): ?array
```

***

### weeklyAction

```php
public weeklyAction(): ?array
```

***

### monthlyAction

```php
public monthlyAction(): ?array
```

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
