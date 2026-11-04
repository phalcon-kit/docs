
Base class for PhalconKit CLI tasks.

Extend this class for framework/application CLI tasks that need Phalcon's
native task lifecycle plus PhalconKit injectable service annotations. The
class does not add task behavior itself; action methods remain normal
Phalcon CLI task methods.

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

Long options that Docopt parsed (`--force`, `--table=<table>`,
`--table <table>`) are then removed from the positional action
arguments, so `cli scaffold models --force` calls the action without a
`"--force"` argument. Other positional tokens, including named Docopt
arguments such as `<key>`, are kept in order.

Invalid task arguments make Docopt print the task usage and exit with a
non-zero status. Parsing is skipped when `shouldParseUsage()` returns
false, which it does for the `help` action.

***

### shouldParseUsage

Whether `beforeExecuteRoute()` should parse the dispatch with `cliDoc`.

```php
protected shouldParseUsage(): bool
```

Returns false for the `help` action, and for the default `main` action
when the task keeps this class's `mainAction()` (which only prints the
usage). `phalcon-kit cli <task> help` and `phalcon-kit cli <task>` then
print the usage and exit with status 0 even when the usage does not
declare those commands. Override it in tasks that are only reached by
dispatcher forwards, or that parse their own arguments.

***

### removeParsedOptionTokens

Remove long-option tokens that Docopt accepted from positional arguments.

```php
protected removeParsedOptionTokens(list $tokens, array<array-key,mixed> $parsed): list
```

A token is removed when it is `--name` or `--name=value` and `--name`
is a key of the Docopt result. For `--name value`, the following token is
removed too when Docopt returned a string value for that option. A bare
`--` ends option processing: it and every later token are kept, matching
Docopt's `<params>` list. Short options and unknown tokens are kept
unchanged.

**Parameters:**

| Parameter | Type                       | Description                         |
|-----------|----------------------------|-------------------------------------|
| `$tokens` | **list**                   | Positional tokens after the action. |
| `$parsed` | **array<array-key,mixed>** | Docopt result keyed by usage name.  |

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

### getPositionalParameters

Return the integer-keyed dispatcher parameters in argument order.

```php
protected getPositionalParameters(): list
```

These are the tokens after the action that Bootstrap did not consume as
global options.

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
