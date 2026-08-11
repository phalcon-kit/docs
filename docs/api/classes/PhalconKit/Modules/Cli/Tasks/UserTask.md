
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

### addModelsPermissions

```php
public addModelsPermissions(?array $tables = null): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$tables` | **?array** |             |

***
