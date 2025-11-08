
***

* Full name: `\PhalconKit\Modules\Cli\Tasks\CacheTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
```

***

## Methods

### clearAction

Clears all items from the cache.

```php
public clearAction(): bool
```

**Return Value:**

True if all items were successfully cleared, false otherwise.

***

### hasAction

Checks if the given action key exists in the cache.

```php
public hasAction(string $key): bool
```

**Parameters:**

| Parameter | Type       | Description                                  |
|-----------|------------|----------------------------------------------|
| `$key`    | **string** | The key identifying the action in the cache. |

**Return Value:**

Returns true if the action key exists in the cache, false otherwise.

**Throws:**

- [`InvalidArgumentException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### deleteAction

Deletes an item from the cache.

```php
public deleteAction(string $key): bool
```

**Parameters:**

| Parameter | Type       | Description                        |
|-----------|------------|------------------------------------|
| `$key`    | **string** | The key of the item to be deleted. |

**Return Value:**

True if the item was successfully deleted, false otherwise.

**Throws:**

- [`InvalidArgumentException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### deleteMultipleAction

Deletes multiple cache entries specified by the given keys.

```php
public deleteMultipleAction(string $keys): bool
```

**Parameters:**

| Parameter | Type       | Description                                                             |
|-----------|------------|-------------------------------------------------------------------------|
| `$keys`   | **string** | A variable number of keys representing the cache entries to be deleted. |

**Return Value:**

Returns true if all cache entries were successfully deleted, false otherwise.

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
