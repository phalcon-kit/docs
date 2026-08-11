
Base MVC controller for PhalconKit applications.

The class keeps Phalcon's native controller behavior and adds typed injectable
properties used throughout the framework. Application controllers can extend
it when they want direct access to the PhalconKit DI helper surface without
re-declaring those service properties.

***

* Full name: `\PhalconKit\Modules\Frontend\Controllers\ErrorController`
* Parent class: [`\PhalconKit\Modules\Frontend\Controllers\AbstractController`](./AbstractController.md)

## Methods

### initialize

```php
public initialize(): void
```

***

### afterExecuteRoute

```php
public afterExecuteRoute(): void
```

***

## Inherited methods

### initialize

```php
public initialize(): void
```

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

### setStatusCode

Sets the status code and message for a response.

```php
public setStatusCode(int $code = 200, string|null $message = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter  | Type             | Description                                                                                                                           |
|------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `$code`    | **int**          | The HTTP status code to set. Default is 200.                                                                                          |
| `$message` | **string\|null** | The optional message for the status code. If not provided, the default message
associated with the provided status code will be used. |

**Return Value:**

The updated response object.

***
