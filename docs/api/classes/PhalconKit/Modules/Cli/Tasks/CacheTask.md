
Base class for PhalconKit CLI tasks.

Extend this class for framework/application CLI tasks that need Phalcon's
native task lifecycle plus PhalconKit injectable service annotations. The
class does not add task behavior itself; action methods remain normal
Phalcon CLI task methods.

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

Parse task-specific arguments and options with this task's `cliDoc`.

```php
public beforeExecuteRoute(): void
```

Bootstrap already parsed the global options (`--format`, `--quiet`,
`--debug`, ...) and stored them as named dispatcher parameters. The task
parser therefore receives only the module, task, action, and positional
tokens, so global options never reach a task usage string that does not
declare them. Parsed task values are stored as camelCase dispatcher
parameters, for example `--password-stdin` becomes `passwordStdin`.

Invalid task arguments make Docopt print the task usage and exit with a
non-zero status.

***

### getTaskArgv

Build the argument vector parsed by the task-level Docopt usage.

```php
protected getTaskArgv(): list<string>
```

The vector is rebuilt from the dispatcher instead of `$_SERVER['argv']`:
`[module, task, action, ...positional tokens]`. Positional tokens are the
integer-keyed dispatcher parameters that Bootstrap left after consuming
its global options; named parameters such as `format` or `quiet` are
excluded.

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

### normalizeCliPayload

Normalize values before CLI output serializers see them.

```php
protected normalizeCliPayload(mixed $payload): mixed
```

Phalcon message objects are useful inside the framework but are opaque for
JSON automation. This helper recursively converts them into scalar arrays
while leaving other payload values unchanged.

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$payload` | **mixed** |             |

***

### normalizeCliMessages

Normalize a list of model messages and optionally add a fallback entry.

```php
protected normalizeCliMessages(iterable $messages, ?string $fallbackMessage = null): list<array{message: string, field: string|null, type: string|null, code: int|null}>
```

**Parameters:**

| Parameter          | Type         | Description                                |
|--------------------|--------------|--------------------------------------------|
| `$messages`        | **iterable** | Messages returned by a model or resultset. |
| `$fallbackMessage` | **?string**  |                                            |

***
