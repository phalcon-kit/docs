
API error endpoint without model-backed REST actions.

Error routes are dispatch targets for status rendering only. They must not
inherit the `Restful` CRUD/query surface because routes such as
`/api/error/save` would otherwise attempt to infer and load an `Error` model
instead of returning through the status action flow.

***

* Full name: `\PhalconKit\Modules\Api\Controllers\ErrorController`
* Parent class: [`\PhalconKit\Mvc\Controller\Rest`](../../../Mvc/Controller/Rest.md)

## Methods

### errorAction

Render the configured HTTP-exception route through the REST envelope.

```php
public errorAction(?int $code = null, ?string $message = null): void
```

The dispatcher owns status validation and preserves the exception as a
named route parameter. Only HttpException messages are exposed here;
fatal exceptions remain private and use

- **See:** \PhalconKit\Modules\Api\Controllers\fatalAction().

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$code`    | **?int**    |             |
| `$message` | **?string** |             |

***

## Inherited methods

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

### getParam

Retrieve a specific parameter value by key.

```php
public getParam(string $key, array|string|null $filters = null, mixed|null $default = null, array|null $params = null): mixed
```

**Parameters:**

| Parameter  | Type                    | Description |
|------------|-------------------------|-------------|
| `$key`     | **string**              |             |
| `$filters` | **array\|string\|null** |             |
| `$default` | **mixed\|null**         |             |
| `$params`  | **array\|null**         |             |

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### hasParam

Check if a given key exists in the parameter array.

```php
public hasParam(string $key, array|null $params = null, bool $cached = true): bool
```

**Parameters:**

| Parameter | Type            | Description |
|-----------|-----------------|-------------|
| `$key`    | **string**      |             |
| `$params` | **array\|null** |             |
| `$cached` | **bool**        |             |

***

### getParams

Retrieve specific or all request parameters.

```php
public getParams(array|null $fields = null, bool $cached = true, bool $deep = true): array<array-key,mixed>
```

Usage examples:
- getParams() -> all params
- getParams(['email', 'password']) -> only those keys
- getParams(['email' => [Filter::TRIM], 'password']) -> filtered subset

**Parameters:**

| Parameter | Type            | Description                             |
|-----------|-----------------|-----------------------------------------|
| `$fields` | **array\|null** | Keys or key=>filters to extract.        |
| `$cached` | **bool**        | Whether to reuse cached raw parameters. |
| `$deep`   | **bool**        | Whether to apply deep sanitization.     |

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### getAllParams

Retrieve all request parameters, optionally applying filters and caching results.

```php
public getAllParams(array|null $filters = null, bool $cached = true, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter  | Type            | Description                                    |
|------------|-----------------|------------------------------------------------|
| `$filters` | **array\|null** | Temporary filters to apply.                    |
| `$cached`  | **bool**        | Whether to reuse previously loaded parameters. |
| `$deep`    | **bool**        | Whether to apply filters recursively.          |

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### collectRequestParams

Collect parameters from one request source based on the HTTP method.

```php
private collectRequestParams(): array<array-key,mixed>
```

Body methods prefer an explicitly JSON request body and otherwise use the
matching form body. Query parameters are intentionally not merged into
body payloads so save endpoints cannot accidentally persist route/query
controls such as `with`, `filters`, or `order`.

***

### collectBodyParams

Collect body parameters from JSON or the method-specific form payload.

```php
private collectBodyParams(mixed $formParams): array<array-key,mixed>
```

**Parameters:**

| Parameter     | Type      | Description                                |
|---------------|-----------|--------------------------------------------|
| `$formParams` | **mixed** | Method-specific form payload from Phalcon. |

***

### collectJsonRequestParams

Collect JSON request parameters when a body request explicitly sends JSON.

```php
private collectJsonRequestParams(): array<array-key,mixed>|null
```

***

### hasJsonContentType

Return true for standard JSON and vendor JSON request content types.

```php
private hasJsonContentType(): bool
```

***

### normalizeRequestParams

Normalize Phalcon request accessor output into a parameter array.

```php
private normalizeRequestParams(mixed $params): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$params` | **mixed** |             |

***

### applyFilters

Apply filters to parameters (recursively if $deep is true).

```php
public applyFilters(array<array-key,mixed> $params, array<string,array|string> $filters, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$params`  | **array<array-key,mixed>**      |             |
| `$filters` | **array<string,array\|string>** |             |
| `$deep`    | **bool**                        |             |

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### deepSanitize

Recursively sanitize nested arrays.

```php
private deepSanitize(mixed $value, array|string $filters): mixed
```

**Parameters:**

| Parameter  | Type              | Description |
|------------|-------------------|-------------|
| `$value`   | **mixed**         |             |
| `$filters` | **array\|string** |             |

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### setDefaultFilters

Sets default filters, replacing any previously defined.

```php
public setDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### addDefaultFilters

Adds or merges new default filters to existing ones.

```php
public addDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### removeFilters

Remove one or many default filters by key.

```php
public removeFilters(string|array<int,string> $keys): static
```

**Parameters:**

| Parameter | Type                          | Description |
|-----------|-------------------------------|-------------|
| `$keys`   | **string\|array<int,string>** |             |

***

### clearDefaultFilters

Clears all default filters.

```php
public clearDefaultFilters(): static
```

***

### getDefaultFilters

Get currently active default filters.

```php
public getDefaultFilters(): array<string,array|string>
```

***

### getRawParams

Retrieves the raw parameters from the request. If caching is enabled, it returns the cached parameters.

```php
public getRawParams(bool $cached = true): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type     | Description                                                    |
|-----------|----------|----------------------------------------------------------------|
| `$cached` | **bool** | Determines whether to use cached parameters. Defaults to true. |

**Return Value:**

The raw request parameters.

***

### getFractalManager

Get the Fractal Manager object.

```php
public getFractalManager(): \PhalconKit\Fractal\Manager
```

This method returns the Fractal Manager object used for transforming data.
If the Fractal Manager object is not already created, it will be created
and initialized with the Fractal Serializer before being returned.

**Return Value:**

The Fractal Manager object.

***

### setFractalManager

Set the Fractal Manager for the class.

```php
public setFractalManager(\PhalconKit\Fractal\Manager|null $manager): void
```

**Parameters:**

| Parameter  | Type                                  | Description                                                                |
|------------|---------------------------------------|----------------------------------------------------------------------------|
| `$manager` | **\PhalconKit\Fractal\Manager\|null** | The Fractal Manager to be set. If null, the Fractal Manager will be unset. |

***

### getFractalSerializer

Get the fractal serializer for the class.

```php
public getFractalSerializer(): \League\Fractal\Serializer\SerializerAbstract
```

**Return Value:**

The fractal serializer instance.

***

### setFractalSerializer

Set the Fractal serializer for the class.

```php
public setFractalSerializer(\League\Fractal\Serializer\SerializerAbstract $serializer): void
```

**Parameters:**

| Parameter     | Type                                              | Description                       |
|---------------|---------------------------------------------------|-----------------------------------|
| `$serializer` | **\League\Fractal\Serializer\SerializerAbstract** | The Fractal serializer to be set. |

***

### getTransformer

Get the transformer for the class.

```php
public getTransformer(): \League\Fractal\TransformerAbstract
```

If the transformer has not been set, a new instance of ModelTransformer will be created.

**Return Value:**

The transformer for the class.

***

### setTransformer

Set the transformer for the class.

```php
public setTransformer(\League\Fractal\TransformerAbstract|null $transformer = null): void
```

**Parameters:**

| Parameter      | Type                                          | Description                                                        |
|----------------|-----------------------------------------------|--------------------------------------------------------------------|
| `$transformer` | **\League\Fractal\TransformerAbstract\|null** | The transformer to be set. If null, the transformer will be unset. |

***

### hasTransformer

Determine if a default transformer has been set for the fractal manager

```php
public hasTransformer(): bool
```

**Return Value:**

Returns true if a default transformer has been set, false otherwise

***

### transformModel

Transform a model using a transformer and optionally a fractal manager.

```php
public transformModel(\Phalcon\Mvc\ModelInterface $model, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                                                            |
|-------------------|-----------------------------------------------|----------------------------------------------------------------------------------------|
| `$model`          | **\Phalcon\Mvc\ModelInterface**               | The model to transform.                                                                |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer to use. If not provided, the default transformer will be used.         |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The fractal manager to use. If not provided, the default fractal manager will be used. |

**Return Value:**

The transformed model as an array, or null if the transformation fails.

***

### transformResultset

Transforms a resultset using the provided transformer and fractal manager.

```php
public transformResultset(\Phalcon\Mvc\Model\ResultsetInterface $resultset, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                                            |
|-------------------|-----------------------------------------------|------------------------------------------------------------------------|
| `$resultset`      | **\Phalcon\Mvc\Model\ResultsetInterface**     | The resultset to be transformed.                                       |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer instance to be used for transformation (optional).     |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The fractal manager instance to be used for transformation (optional). |

**Return Value:**

The transformed resultset as an array, or null if the transformation failed.

***

### transformItem

Transform an item using the specified transformer and Fractal manager

```php
public transformItem(mixed $data, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                            |
|-------------------|-----------------------------------------------|--------------------------------------------------------|
| `$data`           | **mixed**                                     | The data to transform                                  |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer to use (optional, default is null)     |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The Fractal manager to use (optional, default is null) |

**Return Value:**

The transformed item as an array

***

### transformCollection

Transform a collection of data using a specified transformer and Fractal manager.

```php
public transformCollection(mixed $data, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                                                                |
|-------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------|
| `$data`           | **mixed**                                     | The collection of data to be transformed.                                                  |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer to be used. If not provided, the default transformer will be used.         |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The Fractal manager to be used. If not provided, the default Fractal manager will be used. |

**Return Value:**

The transformed data as an array.

***

### isDebugEnabled

Returns whether debug mode is enabled.

```php
public isDebugEnabled(): bool
```

**Return Value:**

True if debug mode is enabled, false otherwise.

***

### beforeExecuteRoute

```php
public beforeExecuteRoute(): void
```

***

### attachBehavior

Attach a behavior to the object.

```php
public attachBehavior(string $eventClass, string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter     | Type             | Description                                                                                                 |
|---------------|------------------|-------------------------------------------------------------------------------------------------------------|
| `$eventClass` | **string**       | The behavior to attach.                                                                                     |
| `$eventType`  | **string\|null** | The event type to attach the behavior to. If null, the behavior will be attached to the default event type. |
| `$priority`   | **int\|null**    | The priority of the behavior. If null, the behavior will be attached with the default priority.             |

***

### attachBehaviors

Attach multiple behaviors to the object.

```php
public attachBehaviors(array $behaviors = [], string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter    | Type             | Description                                                                                            |
|--------------|------------------|--------------------------------------------------------------------------------------------------------|
| `$behaviors` | **array**        | An array of behaviors to attach.                                                                       |
| `$eventType` | **string\|null** | The event type to attach the behaviors to. If null, the behaviors will be attached to all event types. |
| `$priority`  | **int\|null**    | The priority of the behaviors. If null, the behaviors will be attached with the default priority.      |

***

### getOrCreateEventsManager

```php
protected getOrCreateEventsManager(): \Phalcon\Contracts\Events\Manager
```

***

### attachConfiguredBehaviors

Attach legacy, non-action-scoped behavior config for this controller/model.

```php
private attachConfiguredBehaviors(array<string|int,mixed> $behaviorsContext, array<int,string> $handlerCandidates, ?string $modelName): void
```

**Parameters:**

| Parameter            | Type                         | Description                    |
|----------------------|------------------------------|--------------------------------|
| `$behaviorsContext`  | **array<string\|int,mixed>** | Permission behavior map.       |
| `$handlerCandidates` | **array<int,string>**        | Controller class/name aliases. |
| `$modelName`         | **?string**                  |                                |

***

### attachConfiguredActionBehaviors

Attach action-scoped controller/model behavior config for this request.

```php
private attachConfiguredActionBehaviors(array<string|int,mixed> $behaviorActionsContext, array<int,string> $handlerCandidates, array<int,string> $actionCandidates, ?string $modelName): void
```

**Parameters:**

| Parameter                 | Type                         | Description                    |
|---------------------------|------------------------------|--------------------------------|
| `$behaviorActionsContext` | **array<string\|int,mixed>** | Action behavior map.           |
| `$handlerCandidates`      | **array<int,string>**        | Controller class/name aliases. |
| `$actionCandidates`       | **array<int,string>**        | Current action aliases.        |
| `$modelName`              | **?string**                  |                                |

***

### getBehaviorHandlerCandidates

```php
private getBehaviorHandlerCandidates(): array<int,string>
```

***

### getBehaviorActionCandidates

```php
private getBehaviorActionCandidates(): array<int,string>
```

***

### getBehaviorDispatcher

```php
private getBehaviorDispatcher(): ?\Phalcon\Dispatcher\AbstractDispatcher
```

***

### usesControllerAttributes

Determine whether controller attributes should augment permission config.

```php
private usesControllerAttributes(): bool
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
