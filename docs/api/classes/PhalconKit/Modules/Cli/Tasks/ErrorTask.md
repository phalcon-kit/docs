
Base class for PhalconKit CLI tasks.

Extend this class for framework/application CLI tasks that need Phalcon's
native task lifecycle plus PhalconKit injectable service annotations. The
class does not add task behavior itself; action methods remain normal
Phalcon CLI task methods.

***

* Full name: `\PhalconKit\Modules\Cli\Tasks\ErrorTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Methods

### shouldParseUsage

Never parse the error task's usage.

```php
protected shouldParseUsage(): bool
```

The task is reached by dispatcher forwards (not found, forbidden,
unauthorized), which keep the original command's arguments. Parsing them
with this task's usage would print a generic usage text and exit instead
of reporting the actual error.

***

### setStatusCode

Set the status code for the response. Immediately throw a CliException.

```php
public setStatusCode(int $code = 500, string|null $message = null): \Phalcon\Http\ResponseInterface
```

The console prints only the exception message (`Error: <code> - <message>`)
to stderr and exits with status 1.

**Parameters:**

| Parameter  | Type             | Description                                              |
|------------|------------------|----------------------------------------------------------|
| `$code`    | **int**          | The status code to set. Defaults to 500 if not provided. |
| `$message` | **string\|null** | The optional message to associate with the status code.  |

**Throws:**

Always, carrying the status code and message.
- [`CliException`](../../../Exception/CliException.md)

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

### errorAction

Render a generic error using an explicit or already-selected status.

```php
public errorAction(?int $code = null, ?string $message = null): void
```

Dispatcher listeners can set the shared response status before forwarding
here. Direct callers may still provide a status and optional reason phrase;
otherwise the action falls back to HTTP 500.

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$code`    | **?int**    |             |
| `$message` | **?string** |             |

***

### badRequestAction

Http Status Code 400
bad-request

```php
public badRequestAction(): void
```

***

### unauthorizedAction

Http Status Code 401
unauthorized

```php
public unauthorizedAction(): void
```

***

### forbiddenAction

Http Status Code 403
forbidden

```php
public forbiddenAction(): void
```

***

### notFoundAction

Http Status Code 404
not-found

```php
public notFoundAction(): void
```

***

### fatalAction

Http Status Code 500
fatal

```php
public fatalAction(): void
```

***

### maintenanceAction

Http Status Code 503
maintenance

```php
public maintenanceAction(): void
```

***
