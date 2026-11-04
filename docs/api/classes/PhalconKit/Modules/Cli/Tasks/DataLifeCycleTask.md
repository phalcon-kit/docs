
Base class for PhalconKit CLI tasks.

Extend this class for framework/application CLI tasks that need Phalcon's
native task lifecycle plus PhalconKit injectable service annotations. The
class does not add task behavior itself; action methods remain normal
Phalcon CLI task methods.

***

* Full name: `\PhalconKit\Modules\Cli\Tasks\DataLifeCycleTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
```

***

### dataLifeCycleConfig

Configuration array for defining the data lifecycle settings,
including the models and policies applicable.

```php
public array $dataLifeCycleConfig
```

***

### models

App tasks can populate these before calling parent::initialize().

```php
public array $models
```

***

### policies

```php
public array $policies
```

***

## Methods

### initialize

Initializes the configuration for data life cycle and sets up permissions for models.

```php
public initialize(): void
```

***

### mainAction

Executes the main action by processing the provided table names.

```php
public mainAction(string $tables): array|null
```

This method delegates processing to the modelsAction method with the given
table names. The results are then returned in an associative array under the
'models' key.

**Parameters:**

| Parameter | Type       | Description                                  |
|-----------|------------|----------------------------------------------|
| `$tables` | **string** | A variable number of table names to process. |

**Return Value:**

An associative array with the processed data under the 'models'
key, or null if no data is returned.

***

### modelsAction

Processes lifecycle models based on a defined retention policy and tables whitelist,
executing actions such as deletion and collecting associated messages.

```php
public modelsAction(string $tables): array
```

The method retrieves the lifecycle models and applies retention policies to the records.
It processes only whitelisted tables if specified, and skips models not matching the input.
The response contains information about the number of records processed (deleted) and
any associated messages per table.

**Parameters:**

| Parameter | Type       | Description                                                                                                                                                                      |
|-----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$tables` | **string** | A variadic list of table names, which may include comma-separated
values. These are used to filter models by matching the table names.
Only matched table records are processed. |

**Return Value:**

An associative array where keys are table names and values are arrays
containing the count of deleted records ('deleted') and any messages
('messages') encountered during processing.

***

### requireLifeCycleModel

Require a lifecycle model loaded by the models manager.

```php
protected requireLifeCycleModel(mixed $model, class-string $modelClass): \PhalconKit\Mvc\Model
```

Lifecycle tasks need the concrete PhalconKit model implementation because
they disable soft-delete behavior and call lifecycle helpers on the model
class. Keeping this validation outside the main loop keeps the task flow
readable and gives applications a deterministic PhalconKit exception when
a configured model class resolves to the wrong type.

**Parameters:**

| Parameter     | Type             | Description                                    |
|---------------|------------------|------------------------------------------------|
| `$model`      | **mixed**        | Model instance returned by the models manager. |
| `$modelClass` | **class-string** | Configured lifecycle model class.              |

**Throws:**

When the configured model does not resolve to a
PhalconKit model instance.
- [`LogicException`](../../../Exception/LogicException.md)

***

### requireLifeCycleResultset

Require the lifecycle query to return a Phalcon resultset.

```php
protected requireLifeCycleResultset(mixed $records, class-string $modelClass): \Phalcon\Mvc\Model\Resultset
```

`findLifeCycle()` is expected to return records that can be iterated and
passed to the configured lifecycle callback. This guard avoids silently
continuing with malformed model lifecycle implementations when assertions
are disabled.

**Parameters:**

| Parameter     | Type             | Description                            |
|---------------|------------------|----------------------------------------|
| `$records`    | **mixed**        | Records returned by `findLifeCycle()`. |
| `$modelClass` | **class-string** | Model class being processed.           |

**Throws:**

When the lifecycle query does not return a
Phalcon resultset.
- [`LogicException`](../../../Exception/LogicException.md)

***

### getDataLifeCycleModels

Retrieves the data lifecycle models from the configuration.

```php
public getDataLifeCycleModels(): array
```

**Return Value:**

An array of data lifecycle models or an empty array if not configured.

***

### getDataLifeCyclePolicies

Retrieves the data lifecycle policies from the configuration.

```php
public getDataLifeCyclePolicies(): array
```

**Return Value:**

An array of data lifecycle policies or an empty array if not configured.

***

### getTaskDataLifeCycleModels

```php
private getTaskDataLifeCycleModels(): array
```

***

### getTaskDataLifeCyclePolicies

```php
private getTaskDataLifeCyclePolicies(): array
```

***

### addModelsPermissions

Adds permissions for the specified models to the configuration.

```php
public addModelsPermissions(array|null $models = null): void
```

If no models are provided, the method retrieves models from the data lifecycle.
Each model is granted full permissions ('*'), and these permissions are merged
into the configuration under the 'cli' role.

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                                      |
|-----------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$models` | **array\|null** | An associative array of models to add permissions for,
where keys are the model names and values are entities.
If null, the models are retrieved using the data lifecycle logic. |

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
