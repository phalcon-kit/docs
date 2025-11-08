
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

### errorAction

Http Status Code - Generic
error

```php
public errorAction(?int $code = null, ?string $message = null): void
```

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
