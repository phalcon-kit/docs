
Base class for PhalconKit CLI tasks.

Extend this class for framework/application CLI tasks that need Phalcon's
native task lifecycle plus PhalconKit injectable service annotations. The
class does not add task behavior itself; action methods remain normal
Phalcon CLI task methods.

***

* Full name: `\PhalconKit\Modules\Cli\Task`
* Parent class: [`\PhalconKit\Cli\Task`](../../Cli/Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
```

***

## Methods

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

- [`CliException`](../../Exception/CliException.md)

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

### normalizeCliMessage

Convert one Phalcon message object to JSON-safe scalar fields.

```php
private normalizeCliMessage(\Phalcon\Messages\MessageInterface $message): array{message: string, field: string|null, type: string|null, code: int|null}
```

**Parameters:**

| Parameter  | Type                                   | Description |
|------------|----------------------------------------|-------------|
| `$message` | **\Phalcon\Messages\MessageInterface** |             |

***

### normalizeCliMessageValue

Convert optional Phalcon message fields and types to JSON-safe strings.

```php
private normalizeCliMessageValue(mixed $value): ?string
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

### stringifyCliMessage

Convert non-standard message values to a concise CLI-safe string.

```php
private stringifyCliMessage(mixed $message): string
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$message` | **mixed** |             |

***
