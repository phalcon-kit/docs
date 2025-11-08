
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\RestResponse`

## Methods

### setRestErrorResponse

Set the REST response error

```php
public setRestErrorResponse(int $code = 400, ?string $status = null, mixed $response = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type        | Description                                 |
|-------------|-------------|---------------------------------------------|
| `$code`     | **int**     | The HTTP status code (default: 400)         |
| `$status`   | **?string** | The status message (default: 'Bad Request') |
| `$response` | **mixed**   | The response body (default: null)           |

**Return Value:**

The REST response object

**Throws:**

- [`Exception`](../../../../Exception.md)

***
### setRestResponse

Sending rest response as a http response

```php
public setRestResponse(mixed $response = null, ?int $code = null, ?string $status = null, int $jsonOptions, int $depth = 512): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter      | Type        | Description |
|----------------|-------------|-------------|
| `$response`    | **mixed**   |             |
| `$code`        | **?int**    |             |
| `$status`      | **?string** |             |
| `$jsonOptions` | **int**     |             |
| `$depth`       | **int**     |             |

**Throws:**

- [`Exception`](../../../../Exception.md)

***
### applyCacheHeaders

Applies automatic, safe Cache-Control and ETag headers.

```php
protected applyCacheHeaders(array $payload, int $code): void
```

Logic:
- Only cache "GET" 200 responses.
- Authenticated requests → private cache.
- Unauthenticated requests → public cache.
- Everything else → no-store.

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$payload` | **array** |             |
| `$code`    | **int**   |             |

***
### setVaryHeaders

Sets the "Vary" HTTP header to assist caching proxies in varying responses
based on specific headers, particularly authentication-related headers.

```php
public setVaryHeaders(bool|null $isAuthenticated = null): void
```

Logic:
- Retrieves the default list of headers from configuration.
- If the user is authenticated, adds the authorization header.
- Ensures the "Vary" header is set with all relevant headers, avoiding duplicates.

**Parameters:**

| Parameter          | Type           | Description                                                                           |
|--------------------|----------------|---------------------------------------------------------------------------------------|
| `$isAuthenticated` | **bool\|null** | Indicates if the request is authenticated;
defaults to checking the current identity. |

***
### getDebugInfo

Gather debug context.

```php
public getDebugInfo(): array
```

***
### afterExecuteRoute

Update the Dispatcher after executing the route.

```php
public afterExecuteRoute(\Phalcon\Mvc\Dispatcher $dispatcher): void
```

**Parameters:**

| Parameter     | Type                        | Description              |
|---------------|-----------------------------|--------------------------|
| `$dispatcher` | **\Phalcon\Mvc\Dispatcher** | The Dispatcher instance. |

**Throws:**

- [`Exception`](../../../../Exception.md)

***
