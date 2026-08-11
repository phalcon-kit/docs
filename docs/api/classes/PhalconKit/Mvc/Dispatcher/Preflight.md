
Dispatcher listener for CORS and preflight requests.

Register this listener on the MVC dispatcher events manager when an
application wants framework-level CORS handling before controller actions are
executed. CORS headers are read from `response.corsHeaders`; preflight
requests receive a 204 response immediately.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Preflight`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### beforeExecuteRoute

Apply configured CORS headers and short-circuit preflight requests.

```php
public beforeExecuteRoute(): void
```

***

### setCorsHeaders

Set configured CORS headers on a response.

```php
public setCorsHeaders(\Phalcon\Http\ResponseInterface $response, string $origin, array<string,array<int,string>|bool|string> $headers = []): void
```

The configured `Access-Control-Allow-Origin` value is treated specially:
wildcard or explicitly allowed origins are reflected as the current
request origin, while unrelated origins are ignored. Existing headers are
preserved so controllers or earlier listeners can override framework
defaults.

**Parameters:**

| Parameter   | Type                                              | Description                                                 |
|-------------|---------------------------------------------------|-------------------------------------------------------------|
| `$response` | **\Phalcon\Http\ResponseInterface**               | The response object to set the headers on.                  |
| `$origin`   | **string**                                        | The origin value to be checked against the allowed origins. |
| `$headers`  | **array<string,array<int,string>\|bool\|string>** | Configured
CORS header values.                              |

***

### sendNoContent

Send an immediate 204 No Content response.

```php
public sendNoContent(\Phalcon\Http\ResponseInterface $response): void
```

This method terminates the process after sending the response because a
preflight request must not continue into controller execution.

**Parameters:**

| Parameter   | Type                                | Description                  |
|-------------|-------------------------------------|------------------------------|
| `$response` | **\Phalcon\Http\ResponseInterface** | The response object to send. |

***
