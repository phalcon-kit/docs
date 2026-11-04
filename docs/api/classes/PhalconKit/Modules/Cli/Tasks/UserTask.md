
Base class for PhalconKit CLI tasks.

Extend this class for framework/application CLI tasks that need Phalcon's
native task lifecycle plus PhalconKit injectable service annotations. The
class does not add task behavior itself; action methods remain normal
Phalcon CLI task methods.

***

* Full name: `\PhalconKit\Modules\Cli\Tasks\UserTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
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
non-zero status.

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

Normalize model messages through the base CLI task output contract.

```php
protected normalizeCliMessages(iterable $messages, ?string $fallbackMessage = null): list<array{message: string, field: string|null, type: string|null, code: int|null}>
```

* This method is **abstract**.
**Parameters:**

| Parameter          | Type         | Description                                |
|--------------------|--------------|--------------------------------------------|
| `$messages`        | **iterable** | Messages returned by a model or resultset. |
| `$fallbackMessage` | **?string**  |                                            |

***

### initialize

```php
public initialize(): void
```

***

### getDefinitions

Retrieves an array of class definitions mapped to their respective configurations.

```php
public getDefinitions(): array<string,array<string,string|callable>>
```

***

### createAction

```php
public createAction(string $email, ?string $password = null): (array|int|mixed)[]
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$email`    | **string**  |             |
| `$password` | **?string** |             |

***

### roleAction

```php
public roleAction(string $email, string $role): (array|int|mixed)[]
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$email`  | **string** |             |
| `$role`   | **string** |             |

***

### passwordAction

```php
public passwordAction(?string $username = null, ?string $password = null): array
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$username` | **?string** |             |
| `$password` | **?string** |             |

***

### newUserEntity

Create a fresh configured user model for CLI create operations.

```php
protected newUserEntity(): \PhalconKit\Models\Interfaces\UserInterface
```

Applications may map `User::class` to their own model implementation via
the framework model map. This hook keeps create operations on that mapped
class while still letting app tasks override the instantiation strategy
when they need custom construction.

***

### resolvePasswordInput

Resolve an explicitly requested stdin password without exposing it in argv.

```php
protected resolvePasswordInput(?string $password): ?string
```

Existing positional/custom-model assignment remains supported. Stdin mode
rejects empty input and conflicting password arguments before any writes.

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$password` | **?string** |             |

**Throws:**

When input is empty or ambiguous.
- [`InvalidArgumentException`](../../../Exception/InvalidArgumentException.md)

***

### readPasswordFromStdin

Read CLI secret input; override only for an application input adapter.

```php
protected readPasswordFromStdin(): string
```

***

### getUserRoleAssignmentAlias

Resolve the application's direct user-role membership relationship.

```php
protected getUserRoleAssignmentAlias(\PhalconKit\Models\Interfaces\UserInterface $user): string
```

Core's generated User defines UserRoleList. Application models may retain
RoleNode; prefer that alias when present to preserve their save hooks.
A missing relationship is a configuration error, never a successful role
assignment. The model manager must have initialized the resolved user.

**Parameters:**

| Parameter | Type                                            | Description |
|-----------|-------------------------------------------------|-------------|
| `$user`   | **\PhalconKit\Models\Interfaces\UserInterface** |             |

**Throws:**

When neither membership alias exists.
- [`LogicException`](../../../Exception/LogicException.md)

***

### addModelsPermissions

```php
public addModelsPermissions(?array $tables = null): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$tables` | **?array** |             |

***
