
Class Preflight

The Preflight class is attached to the dispatcher events manager.
It handles Cross-Origin Resource Sharing (CORS) requests and preflight
requests by setting the appropriate headers on the response object.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Preflight`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### beforeExecuteRoute

This method is called before routing the request. It checks if the request is a CORS (Cross-Origin Resource Sharing) request.

```php
public beforeExecuteRoute(): void
```

If it is a CORS request, it retrieves the origin from the request headers and sets the CORS headers on the response object using the setCorsHeaders() method.
The CORS headers are determined by the "response.corsHeaders" configuration option.

After setting the CORS headers, it checks if the request is a preflight request.
If it is a preflight request, it calls the sendNoContent() method to send a "204 No Content" response.

***

### setCorsHeaders

Set the CORS headers for the response.

```php
public setCorsHeaders(\Phalcon\Http\ResponseInterface $response, string $origin, array $headers = []): void
```

This method sets the CORS (Cross-Origin Resource Sharing) headers on the given response object.

**Parameters:**

| Parameter   | Type                                | Description                                                                                                                                                                                                                                                                                       |
|-------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$response` | **\Phalcon\Http\ResponseInterface** | The response object to set the headers on.                                                                                                                                                                                                                                                        |
| `$origin`   | **string**                          | The origin value to be checked against the allowed origins.                                                                                                                                                                                                                                       |
| `$headers`  | **array**                           | An optional array of additional headers to be set on the response.
Each header should be represented as key-value pairs in the array.
The keys represent the header names, and the values represent the header values.
If a header key exists in the response object, it will not be overwritten. |

***

### sendNoContent

Send a "No Content" response.

```php
public sendNoContent(\Phalcon\Http\ResponseInterface $response): void
```

This method sends a "No Content" response by setting the status code to 204 and sending the response.
After sending the response, the script execution is terminated by calling the exit function with a status code of 0.

**Parameters:**

| Parameter   | Type                                | Description                  |
|-------------|-------------------------------------|------------------------------|
| `$response` | **\Phalcon\Http\ResponseInterface** | The response object to send. |

***
