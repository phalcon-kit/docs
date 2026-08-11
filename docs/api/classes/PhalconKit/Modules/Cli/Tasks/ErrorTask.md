
Base class for PhalconKit CLI tasks.

Extend this class for framework/application CLI tasks that need Phalcon's
native task lifecycle plus PhalconKit injectable service annotations. The
class does not add task behavior itself; action methods remain normal
Phalcon CLI task methods.

***

* Full name: `\PhalconKit\Modules\Cli\Tasks\ErrorTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Methods

### setStatusCode

Set the status code for the response. Immediately throw a CliException.

```php
public setStatusCode(int $code = 500, string|null $message = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter  | Type             | Description                                              |
|------------|------------------|----------------------------------------------------------|
| `$code`    | **int**          | The status code to set. Defaults to 500 if not provided. |
| `$message` | **string\|null** | The optional message to associate with the status code.  |

**Throws:**

If an error occurs while setting the status code.
- [`CliException`](../../../Exception/CliException.md)

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
