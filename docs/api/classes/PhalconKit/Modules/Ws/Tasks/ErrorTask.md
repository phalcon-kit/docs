
Base class for WebSocket tasks.

Tasks get typed access to the WebSocket console, router, and dispatcher
through PhalconKit injectable properties. Concrete tasks should implement
action methods such as `listenAction()`.

***

* Full name: `\PhalconKit\Modules\Ws\Tasks\ErrorTask`
* Parent class: [`\PhalconKit\Modules\Ws\Task`](../Task.md)

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
- [`WsException`](../../../Exception/WsException.md)

***

## Inherited methods

### resetConnectionState

Clear request-scoped model connection state in a long-running worker.

```php
public resetConnectionState(): void
```

Call this before custom WebSocket callbacks that perform model reads or
writes. The built-in abstract task invokes it for open, message, close,
HTTP request, and pipe-message callbacks.

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
