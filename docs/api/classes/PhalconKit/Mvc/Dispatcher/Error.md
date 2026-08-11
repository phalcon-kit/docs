
Dispatcher listener that maps request and runtime exceptions to error routes.

Missing controllers/actions are forwarded to the configured not-found route.
HttpException instances preserve valid 400-599 status codes and are handled
through the configured HTTP-exception route in every environment. Other
exceptions are forwarded to the configured fatal route only when debug mode
is disabled; in debug mode the original exception is rethrown so developer
tooling can render it.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Error`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Properties

### defaultNotFoundRoute

Fallback route used when `router.notFound` is not fully configured.

```php
public array{module: ?string, namespace: ?string, controller: string, action: string} $defaultNotFoundRoute
```

***

### defaultHttpExceptionRoute

Fallback route used when `router.httpException` is not fully configured.

```php
public array{module: ?string, namespace: ?string, controller: string, action: string} $defaultHttpExceptionRoute
```

Applications may override the route target, but status normalization
remains owned by this listener.

***

### defaultErrorRoute

Fallback route used when `router.fatal` is not fully configured.

```php
public array{module: ?string, namespace: ?string, controller: string, action: string} $defaultErrorRoute
```

The property name is retained for compatibility with applications that
customize the listener directly.

***

## Methods

### beforeException

Forward dispatch and HTTP exceptions to the configured error routes.

```php
public beforeException(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Dispatcher $dispatcher, \Exception $exception): bool
```

**Parameters:**

| Parameter     | Type                           | Description                          |
|---------------|--------------------------------|--------------------------------------|
| `$event`      | **\Phalcon\Events\Event**      | Dispatcher event emitted by Phalcon. |
| `$dispatcher` | **\PhalconKit\Mvc\Dispatcher** | PhalconKit MVC dispatcher.           |
| `$exception`  | **\Exception**                 | Exception raised during dispatch.    |

**Return Value:**

False when the listener handled the exception by forwarding.

**Throws:**

When forwarding to the configured error route
fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When debug mode is enabled for an unexpected
exception.
- [`Exception`](https://www.php.net/manual/en/class.exception.php){:target="_blank"}

***

### normalizeHttpExceptionStatus

Normalize an HttpException code to an HTTP error status.

```php
private normalizeHttpExceptionStatus(\PhalconKit\Exception\HttpException $exception): int
```

Only HttpException owns this numeric-code contract. Invalid codes fail
closed as 500 instead of being sent as successful or malformed statuses.

**Parameters:**

| Parameter    | Type                                    | Description |
|--------------|-----------------------------------------|-------------|
| `$exception` | **\PhalconKit\Exception\HttpException** |             |

***

### getHttpReasonPhrase

Resolve a framework-owned reason phrase for any accepted error status.

```php
private getHttpReasonPhrase(int $status): string
```

Phalcon requires a non-empty phrase for non-standard numeric statuses.
Unmapped 4xx/5xx codes therefore use their category's generic phrase
instead of exposing the exception message as transport metadata.

**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$status` | **int** |             |

***

### forwardHttpException

Forward an expected request exception without handing it to debug output.

```php
private forwardHttpException(\PhalconKit\Mvc\Dispatcher $dispatcher, \PhalconKit\Exception\HttpException $exception): bool
```

**Parameters:**

| Parameter     | Type                                    | Description |
|---------------|-----------------------------------------|-------------|
| `$dispatcher` | **\PhalconKit\Mvc\Dispatcher**          |             |
| `$exception`  | **\PhalconKit\Exception\HttpException** |             |

***

### forwardFatalException

Forward an unexpected production exception or rethrow it for debug tools.

```php
private forwardFatalException(\PhalconKit\Mvc\Dispatcher $dispatcher, \Exception $exception): bool
```

**Parameters:**

| Parameter     | Type                           | Description |
|---------------|--------------------------------|-------------|
| `$dispatcher` | **\PhalconKit\Mvc\Dispatcher** |             |
| `$exception`  | **\Exception**                 |             |

**Throws:**

When either application debug flag is enabled.
- [`Exception`](https://www.php.net/manual/en/class.exception.php){:target="_blank"}

***

### appendDefaultToRoute

Merge missing route parts from a default route definition.

```php
public appendDefaultToRoute(array<string,mixed> $route, array<string,mixed> $default): array<string,mixed>
```

**Parameters:**

| Parameter  | Type                    | Description                |
|------------|-------------------------|----------------------------|
| `$route`   | **array<string,mixed>** | Configured route override. |
| `$default` | **array<string,mixed>** | Fallback route parts.      |

***
