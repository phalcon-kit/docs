
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\RestResponse`

## Methods

### setRestErrorResponse

Return a normalized REST error response.

```php
public setRestErrorResponse(int $code = 400, string|null $status = null, mixed $response = null): \Phalcon\Http\ResponseInterface
```

This is the preferred exit path for controller failures that should use
the standard JSON envelope but carry a non-2xx HTTP status. The response
body remains caller-controlled so legacy actions can keep returning
`false`, `null`, or a custom payload while the envelope status and code
are still set consistently by

- **See:** \PhalconKit\Mvc\Controller\Traits\setRestResponse().

**Parameters:**

| Parameter   | Type             | Description                                                                                                              |
|-------------|------------------|--------------------------------------------------------------------------------------------------------------------------|
| `$code`     | **int**          | HTTP status code to expose in the response and payload.                                                                  |
| `$status`   | **string\|null** | Optional status text; when null, the status is
resolved from the current response or {@see \PhalconKit\Http\StatusCode}. |
| `$response` | **mixed**        | Response body stored under the REST `response`
envelope key.                                                             |

**Return Value:**

The finalized Phalcon response instance.

***
### setRestResponse

Sending rest response as a http response.

```php
public setRestResponse(mixed $response = null, ?int $code = null, ?string $status = null, int $jsonOptions = 0, int $depth = 512): \Phalcon\Http\ResponseInterface
```

The JSON envelope is intentionally centralized here so REST actions can
focus on setting named view fields through

- **See:** \PhalconKit\Mvc\Controller\Traits\setRestViewVar() and

- **See:** \PhalconKit\Mvc\Controller\Traits\setRestViewVars(). The envelope keys are public constants because
they are part of the API contract exposed to clients.

**Parameters:**

| Parameter      | Type        | Description |
|----------------|-------------|-------------|
| `$response`    | **mixed**   |             |
| `$code`        | **?int**    |             |
| `$status`      | **?string** |             |
| `$jsonOptions` | **int**     |             |
| `$depth`       | **int**     |             |

***
### setRestViewVar

Set one public view field for the REST response payload.

```php
protected setRestViewVar(string $key, mixed $value): void
```

The field is later serialized under the top-level `view` envelope key by


- **See:** \PhalconKit\Mvc\Controller\Traits\setRestResponse(). Standard framework actions should use the
`REST_VIEW_*` constants instead of repeating string literals so response
contracts remain discoverable and consistent.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |
| `$value`  | **mixed**  |             |

***
### setRestViewVars

Set several public view fields for the REST response payload.

```php
protected setRestViewVars(array<string,mixed> $vars, bool $merge = true): void
```

**Parameters:**

| Parameter | Type                    | Description                                                                                                                |
|-----------|-------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `$vars`   | **array<string,mixed>** | View fields to expose under the response
envelope's `view` key.                                                            |
| `$merge`  | **bool**                | Whether to merge with existing view variables. This
matches Phalcon's `setVars()` default behavior used by legacy actions. |

***
### getRestViewVars

Return view fields that are safe to serialize in a REST response.

```php
protected getRestViewVars(): array<string,mixed>
```

Phalcon keeps internal render data under `_`; that key is deliberately
stripped so controller actions cannot accidentally leak framework internals
through the public JSON envelope.

***
### buildRestPayload

Build the normalized REST JSON envelope.

```php
protected buildRestPayload(mixed $response, int $code, string $status): array<string,mixed>
```

The shape is intentionally stable for backward compatibility:
`timestamp`, `status`, `code`, `response`, and `view` are always present,
while `debug` is added only when debug mode is enabled.

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$response` | **mixed**  |             |
| `$code`     | **int**    |             |
| `$status`   | **string** |             |

***
### getRestActionFailureStatusCode

Resolve an HTTP status code for REST action failures carrying messages.

```php
protected getRestActionFailureStatusCode(mixed $messages, int $emptyStatusCode = 400, int $defaultStatusCode = 422): int
```

Model, validation, and domain-rule failures normally include messages and
map to 422 Unprocessable Entity. Framework-generated REST failures can
attach explicit client-error codes to Phalcon messages; those 4xx codes
are preserved so actions do not collapse invalid request intent, missing
targets, forbidden operations, or conflicts into generic validation
responses. Server errors stay owned by thrown exceptions or explicit
controller calls to

- **See:** \PhalconKit\Mvc\Controller\Traits\setRestErrorResponse().

A failure without messages is treated as malformed input by default. The
defaults can be overridden for actions that need a different legacy or
protocol-specific response.

**Parameters:**

| Parameter            | Type      | Description                                                                                                                |
|----------------------|-----------|----------------------------------------------------------------------------------------------------------------------------|
| `$messages`          | **mixed** | A Phalcon messages collection, iterable list,
single message, or any legacy message payload returned by model/action
code. |
| `$emptyStatusCode`   | **int**   | Status code used when no message payload is
available.                                                                     |
| `$defaultStatusCode` | **int**   | Status code used when messages exist but no
explicit HTTP status code is attached.                                         |

***
### hasRestActionMessages

Determine whether a REST action failure carried any message payload.

```php
protected hasRestActionMessages(mixed $messages): bool
```

PHP objects are never empty for `empty()`, even when they implement
`Countable` and contain zero messages. Phalcon validation returns
`Phalcon\Messages\Messages`, so status resolution must check the
collection count instead of relying on PHP object truthiness.

**Parameters:**

| Parameter   | Type      | Description |
|-------------|-----------|-------------|
| `$messages` | **mixed** |             |

***
### setRestActionFailureResponse

Return a normalized REST error response for an action failure.

```php
protected setRestActionFailureResponse(mixed $messages, mixed $response = false, int $emptyStatusCode = 400, int $defaultStatusCode = 422): \Phalcon\Http\ResponseInterface
```

This helper keeps REST actions from pre-mutating the response status and
then relying on

- **See:** \PhalconKit\Mvc\Controller\Traits\setRestResponse() to pick that status back up. The
action still owns its public view fields; this method only resolves the
HTTP failure code from explicit message metadata and delegates the final
envelope to
- **See:** \PhalconKit\Mvc\Controller\Traits\setRestErrorResponse().

**Parameters:**

| Parameter            | Type      | Description                                                                                                                |
|----------------------|-----------|----------------------------------------------------------------------------------------------------------------------------|
| `$messages`          | **mixed** | A Phalcon messages collection, iterable list,
single message, or any legacy message payload returned by model/action
code. |
| `$response`          | **mixed** | Response body stored under the REST `response`
envelope key. Standard framework actions usually pass `false`.              |
| `$emptyStatusCode`   | **int**   | Status code used when no message payload is
available.                                                                     |
| `$defaultStatusCode` | **int**   | Status code used when messages exist but no
explicit HTTP status code is attached.                                         |

**Return Value:**

The finalized Phalcon response instance.

***
### getRestActionMessageStatusCode

Extract an explicit HTTP status code from one REST action message.

```php
protected getRestActionMessageStatusCode(mixed $message): int|null
```

Only Phalcon message codes in the HTTP client-error range are considered.
Normal validation messages often carry no code, or a non-HTTP code, and
server-error responses should come from exceptions or explicit controller
error handling instead of model/domain message metadata.

**Parameters:**

| Parameter  | Type      | Description                                          |
|------------|-----------|------------------------------------------------------|
| `$message` | **mixed** | Candidate message value from a model/action failure. |

**Return Value:**

Explicit 4xx HTTP status code when present and valid;
otherwise null.

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

***
