
Base MVC controller for PhalconKit applications.

The class keeps Phalcon's native controller behavior and adds typed injectable
properties used throughout the framework. Application controllers can extend
it when they want direct access to the PhalconKit DI helper surface without
re-declaring those service properties.

***

* Full name: `\PhalconKit\Modules\Api\Controllers\MenuController`
* Parent class: [`\PhalconKit\Modules\Api\Controller`](../Controller.md)

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

### initializeQuery

Initializes the query builder with default values for various properties.

```php
public initializeQuery(): void
```

**Throws:**

When request parameter filtering fails during
query initialization.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### initializeFind

Initializes the `find` property with a new Collection object.

```php
public initializeFind(): void
```

The values of various properties are assigned to the corresponding keys of the Collection object.

***

### setFind

Sets the value of the `find` property.

```php
public setFind(array|\Phalcon\Support\Collection|null $find): void
```

**Parameters:**

| Parameter | Type                                         | Description                            |
|-----------|----------------------------------------------|----------------------------------------|
| `$find`   | **array\|\Phalcon\Support\Collection\|null** | The new value for the `find` property. |

***

### getFind

Retrieves the value of the `find` property.

```php
public getFind(): \Phalcon\Support\Collection|null
```

**Return Value:**

The value of the `find` property.

***

### prepareFind

Builds the `find` array for a query.

```php
public prepareFind(\Phalcon\Support\Collection|null $find = null, bool $ignoreKey = false): array
```

**Parameters:**

| Parameter    | Type                                  | Description                                                      |
|--------------|---------------------------------------|------------------------------------------------------------------|
| `$find`      | **\Phalcon\Support\Collection\|null** | The collection to build the find array from. Defaults to null.   |
| `$ignoreKey` | **bool**                              | Whether to ignore the keys in the collection. Defaults to false. |

**Return Value:**

The built find array.

***

### prepareFindListToString

Converts find list options to their PHQL string form.

```php
protected prepareFindListToString(array $items): string
```

Collection-backed query options can be represented either as plain values
or as enabled field maps, for example ['id' => true]. Values remain the
default source, but true map entries use their string key as the selected
field instead of compiling to "1".

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$items`  | **array** |             |

***

### conditionsShouldBeHaving

Determines whether WHERE conditions must be promoted to HAVING.

```php
public conditionsShouldBeHaving(?string $conditions): bool
```

Currently disabled by design.

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$conditions` | **?string** |             |

***

### find

Find records in the database using the specified criteria.

```php
public find(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface&\Traversable
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                      |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation.

***

### findWith

Find records in the database using the specified criteria and include related records.

```php
public findWith(array|null $with = null, array|null $find = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                      |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$with`   | **array\|null** | Optional. An array of related models to include
with the found records. Passing null uses the
controller's normalized default `with` graph.                      |
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation with loaded relationships.

**Throws:**

When the configured model does not support
PhalconKit eager-loading helpers.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### findFirst

Find the first record in the database using the specified criteria.

```php
public findFirst(array|null $find = null): \Phalcon\Mvc\ModelInterface|false|null
```

Note: We intentionally removed the Row from the return type to simplify usages.
If you need to access the Row, use a query builder instead.

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                                              |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional. An array of criteria to determine the record to find.
If not provided, the default criteria from `getFind()` method
will be used to find the first record. Defaults to `null`. |

**Return Value:**

The result of the find operation, which is the first record that matches the criteria.

***

### findFirstWith

Find the first record in the database using the specified criteria and relations.

```php
public findFirstWith(array|null $with = null, array|null $find = null): ?\Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                      |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$with`   | **array\|null** | Optional. An array of relations to eager load for the record.
Passing null uses the controller's normalized
default `with` graph.                                |
| `$find`   | **array\|null** | Optional. An array of criteria to determine the records to find.
If not provided, the default criteria from `getFind()` method
will be used. Defaults to `null`. |

**Return Value:**

The result of the find operation for the first record.

**Throws:**

When the configured model does not support
PhalconKit eager-loading helpers.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### requireEagerLoadModel

Require a loaded model that supports PhalconKit eager-loading helpers.

```php
protected requireEagerLoadModel(\Phalcon\Mvc\ModelInterface $model, string $method): \PhalconKit\Mvc\Model\Interfaces\EagerLoadInterface
```

Controller query helpers can load any Phalcon model, but `findWith()` and
`findFirstWith()` need the PhalconKit eager-loading contract. Keeping this
check in one helper keeps the public query methods readable while still
producing a stable service-resolution exception instead of a late static
method error when a controller is wired to the wrong model class.

**Parameters:**

| Parameter | Type                            | Description                                           |
|-----------|---------------------------------|-------------------------------------------------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** | Loaded model instance used for static query
dispatch. |
| `$method` | **string**                      | Query helper that requires eager loading.             |

**Return Value:**

The same model narrowed to the eager-loading
contract.

**Throws:**

When the configured model does not support
PhalconKit eager-loading helpers.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### average

Calculates the average value based on a given set of criteria.

```php
public average(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                       |
|-----------|-----------------|---------------------------------------------------|
| `$find`   | **array\|null** | The criteria to filter the records by (optional). |

**Return Value:**

The average value or a result set containing the average value.

***

### count

Retrieves the total count of items based on the specified model name and find criteria.

```php
public count(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|int|false
```

Note: limit and offset are removed from the parameters in order to retrieve the total count

**Parameters:**

| Parameter | Type            | Description                                                                                     |
|-----------|-----------------|-------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | An array of find criteria to filter the results. If null, the default criteria will be applied. |

**Return Value:**

The total count of items that match the specified criteria.

***

### prepareCountFind

Prepare count-specific options without overriding an explicit count column.

```php
protected prepareCountFind(array $find): array
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$find`   | **array** |             |

***

### getJoinedCountColumn

Joined count queries default to the root model identity for single-column primary keys.

```php
protected getJoinedCountColumn(array $find): ?string
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$find`   | **array** |             |

***

### sum

Calculates the sum of values based on a given search criteria.

```php
public sum(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional: The criteria to find the maximum value from.
Default: null (will retrieve the `find` from $this->getFind()) |

**Return Value:**

The calculated sum of values.

***

### maximum

Retrieves the minimum value.

```php
public maximum(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional: The criteria to find the maximum value from.
Default: null (will retrieve the `find` from $this->getFind()) |

**Return Value:**

The maximum value from the dataset or a `ResultsetInterface` that represents the grouped maximum values.

***

### minimum

Retrieves the minimum value.

```php
public minimum(array|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

**Parameters:**

| Parameter | Type            | Description                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| `$find`   | **array\|null** | Optional: The criteria to find the minimum value from.
Default: null (will retrieve the `find` from $this->getFind()) |

**Return Value:**

The minimum value from the dataset or a `ResultsetInterface` that represents the grouped minimum values.

***

### getCalculationFind

Prepares and retrieves the modified `find` array with optional adjustments.

```php
protected getCalculationFind(array|null $find = null, bool $removeLimitOffset = true): array
```

**Parameters:**

| Parameter            | Type            | Description                                                                                                         |
|----------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| `$find`              | **array\|null** | The initial `find` array to modify. If null, it defaults
to the result of `getFind()->toArray()` or an empty array. |
| `$removeLimitOffset` | **bool**        | Whether to remove `limit` and `offset` keys
from the `find` array. Defaults to true.                                |

**Return Value:**

The adjusted `find` array, filtered with any necessary modifications.

***

### generateBindKey

Generates a unique bind key with the given prefix.

```php
public generateBindKey(string $prefix): string
```

**Parameters:**

| Parameter | Type       | Description                            |
|-----------|------------|----------------------------------------|
| `$prefix` | **string** | The prefix to be used in the bind key. |

**Return Value:**

The generated bind key.

***

### getModelName

Retrieves the name of the model associated with the controller.

```php
public getModelName(): string|null
```

**Return Value:**

The name of the model associated with the controller, or null if not found.

***

### setModelName

Sets the name of the model to be used.

```php
public setModelName(string|null $modelName): void
```

**Parameters:**

| Parameter    | Type             | Description                      |
|--------------|------------------|----------------------------------|
| `$modelName` | **string\|null** | The name of the model to be set. |

***

### getModelNamespaces

Get namespaces used when deriving a model class from the controller name.

```php
public getModelNamespaces(): array<string,string>
```

Explicit namespaces set through

- **See:** \PhalconKit\Mvc\Controller\Traits\setModelNamespaces() win. When no
explicit map exists and the DI contains a `loader` service, the method
reads namespaces from Phalcon's autoloader. A registered but incompatible
loader is treated as a configuration error because otherwise model
inference would fail later with a less useful method-call error when PHP
assertions are disabled.

**Return Value:**

Namespace-to-directory map used for model
lookup.

**Throws:**

When the optional `loader` service is present
but is not a Phalcon autoload loader.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### setModelNamespaces

Set the namespaces for the models.

```php
public setModelNamespaces(array|null $modelNamespaces): void
```

**Parameters:**

| Parameter          | Type            | Description                             |
|--------------------|-----------------|-----------------------------------------|
| `$modelNamespaces` | **array\|null** | The array of namespaces for the models. |

***

### getModelNameFromController

Retrieves the model name from the controller by following certain naming conventions.

```php
public getModelNameFromController(array|null $namespaces = null, string $needle = 'Models'): string|null
```

**Parameters:**

| Parameter     | Type            | Description                                                                                                         |
|---------------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| `$namespaces` | **array\|null** | Optional. An array of namespaces to search for the model. Default is null and will use $this->getModelNamespaces(). |
| `$needle`     | **string**      | Optional. The keyword to search for in the namespace. Default is 'Models'.                                          |

**Return Value:**

The model name if found, otherwise null.

***

### getControllerName

Returns the name of the controller.

```php
public getControllerName(): string
```

If the controller name is not set in the dispatcher, it extracts the controller name from the class name
of the current instance.

**Return Value:**

The name of the controller.

***

### loadModel

Loads a model by its name using the modelsManager.

```php
public loadModel(string|null $modelName = null): \Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter    | Type             | Description                                                                        |
|--------------|------------------|------------------------------------------------------------------------------------|
| `$modelName` | **string\|null** | The name of the model to load. Default is null and will use $this->getModelName(). |

**Return Value:**

The loaded model.

**Throws:**

When no model can be resolved or the resolved
class does not implement Phalcon's model contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### modelHasColumn

Determine whether the configured model exposes a database column or mapped
model attribute.

```php
public modelHasColumn(string $column, string|null $modelName = null): bool
```

The helper prefers generated model `columnMap()` definitions, then falls
back to Phalcon's model metadata for models that do not declare a column
map. Metadata availability depends on the application's configured
metadata strategy and cache; if metadata cannot be read safely, the helper
returns false instead of turning an optional controller condition into a
runtime failure.

**Parameters:**

| Parameter    | Type             | Description                                                                                     |
|--------------|------------------|-------------------------------------------------------------------------------------------------|
| `$column`    | **string**       | Database column name or mapped model attribute name.                                            |
| `$modelName` | **string\|null** | Optional model class; defaults to the
current controller model. Non-model strings return false. |

**Return Value:**

True when the model column map contains the raw column or
mapped attribute name.

***

### appendModelName

Normalize and qualify a field reference with the model (alias) name.

```php
public appendModelName(string $field, string|null $modelName = null): string
```

Responsibilities
----------------
• Provides **syntactic normalization only** (no metadata validation).
• Safely formats identifiers into PHQL bracket notation: [Alias].[column].
• Preserves SQL/PHQL function or expression calls (e.g. RAND(), COUNT(id)).
• Supports optional ORDER BY direction (ASC | DESC).
• Rejects obvious injection vectors.

Assumptions
-----------
• Column / alias allow-listing and validation occur upstream.
• This method must be deterministic and side-effect free.

Supported inputs
----------------
id                     → [Model].[id]
id desc                → [Model].[id] desc
alias.id               → [alias].[id]
COUNT(id)              → COUNT(id)
COUNT(id) DESC         → COUNT(id) desc
RAND()                 → RAND()
[alias].[id]           → unchanged

Rejected inputs
---------------
foo.bar.baz            → Invalid identifier
id; DROP TABLE         → Unsafe expression

**Parameters:**

| Parameter    | Type             | Description                     |
|--------------|------------------|---------------------------------|
| `$field`     | **string**       | Raw field string.               |
| `$modelName` | **string\|null** | Default alias if none provided. |

**Return Value:**

Normalized field string.

**Throws:**

When identifier or expression is unsafe.
- [`InvalidArgumentException`](../../../Exception/InvalidArgumentException.md)

***

### getPrimaryKeyAttributes

Retrieves the primary key attributes for a given model.

```php
public getPrimaryKeyAttributes(string|null $modelName = null): array
```

**Parameters:**

| Parameter    | Type             | Description                                                                                                       |
|--------------|------------------|-------------------------------------------------------------------------------------------------------------------|
| `$modelName` | **string\|null** | The name of the model to retrieve primary key attributes for. Default is null and will use $this->getModelName(). |

**Return Value:**

An array of primary key attributes for the model. Returns an empty array if no model name is specified.

***

### cacheModelColumns

```php
protected cacheModelColumns(class-string<\Phalcon\Mvc\ModelInterface> $modelName): void
```

**Parameters:**

| Parameter    | Type                                          | Description |
|--------------|-----------------------------------------------|-------------|
| `$modelName` | **class-string<\Phalcon\Mvc\ModelInterface>** |             |

***

### getGeneratedModelColumnMap

```php
protected getGeneratedModelColumnMap(\Phalcon\Mvc\ModelInterface $model): array<array-key,mixed>|null
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |

***

### collectModelColumnMap

```php
protected collectModelColumnMap(array<string,bool>& $lookup, array<array-key,mixed>|null $columnMap): void
```

**Parameters:**

| Parameter    | Type                             | Description |
|--------------|----------------------------------|-------------|
| `$lookup`    | **array<string,bool>**           |             |
| `$columnMap` | **array<array-key,mixed>\|null** |             |

***

### collectModelAttributes

```php
protected collectModelAttributes(array<string,bool>& $lookup, array<array-key,mixed> $attributes): void
```

**Parameters:**

| Parameter     | Type                       | Description |
|---------------|----------------------------|-------------|
| `$lookup`     | **array<string,bool>**     |             |
| `$attributes` | **array<array-key,mixed>** |             |

***

### isExpression

```php
protected isExpression(string $field): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

***

### expose

Expose properties of an item

```php
public expose(mixed $item, array|null $expose = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                    |
|-----------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| `$item`   | **mixed**       | The item to expose properties for                                                                                              |
| `$expose` | **array\|null** | The array defining which properties to expose (optional).
If not provided, the default $this->getExpose() method will be used. |

**Return Value:**

The exposed properties as an array

***

### listExpose

List entities with specified expose definition

```php
public listExpose(iterable $items, array|null $expose = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                |
|-----------|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| `$items`  | **iterable**    | The iterable collection of items to be listed                                                                              |
| `$expose` | **array\|null** | The expose definition for the entities (optional)
If not provided, the default $this->getListExpose() method will be used. |

**Return Value:**

The array of exposed entities

***

### exportExpose

Export items with expose definition

```php
public exportExpose(iterable $items, array|null $expose = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                         |
|-----------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| `$items`  | **iterable**    | The items to be exported                                                                                            |
| `$expose` | **array\|null** | The expose definition for the items.
If not provided, the default $this->getExportExpose() definition will be used. |

**Return Value:**

The exported items

***

### getContentType

Get the content type based on the given parameters.

```php
public getContentType(array|null $params = null): string
```

**Parameters:**

| Parameter | Type            | Description                                                                                                  |
|-----------|-----------------|--------------------------------------------------------------------------------------------------------------|
| `$params` | **array\|null** | Optional. The parameters to determine the content type. If not provided, it will use the default parameters. |

**Return Value:**

The content type. Possible values: "json", "csv", "xlsx".

**Throws:**

When an unsupported content type is provided.
- [`HttpException`](../../../Exception/HttpException.md)

***

### getFilename

Returns the filename for the exported file.

```php
public getFilename(): string
```

The filename is generated based on the model class name, with any
namespaces replaced by slashes, and then slugified. It is then
prepended with the current date in the 'Y-m-d' format.

**Return Value:**

The generated filename for the exported file.

***

### getExportColumns

Retrieves the columns from the given list of data.

```php
public getExportColumns(array $list): array
```

**Parameters:**

| Parameter | Type      | Description                               |
|-----------|-----------|-------------------------------------------|
| `$list`   | **array** | The list of data to extract columns from. |

**Return Value:**

An associative array containing the export columns as keys.

***

### export

Exports the given list to a specified file in the specified format.

```php
public export(array $list = [], string|null $filename = null, string|null $contentType = null, array|null $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter      | Type             | Description                                                                                         |
|----------------|------------------|-----------------------------------------------------------------------------------------------------|
| `$list`        | **array**        | The list of data to export.                                                                         |
| `$filename`    | **string\|null** | The filename of the exported file. If not provided, the default filename will be used.              |
| `$contentType` | **string\|null** | The content type of the exported file. If not provided, the default content type will be used.      |
| `$params`      | **array\|null**  | Additional parameters for the export process. If not provided, the default parameters will be used. |

**Return Value:**

Returns true if the export was successful, otherwise false.

**Throws:**

Thrown if the specified content type is not supported.
- [`HttpException`](../../../Exception/HttpException.md)

***

### exportXml

Exports the given list to an XML file with the specified filename.

```php
public exportXml(array $list, string|null $filename = null, ?array $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type             | Description                                                                              |
|-------------|------------------|------------------------------------------------------------------------------------------|
| `$list`     | **array**        | The list of data to export.                                                              |
| `$filename` | **string\|null** | The filename of the exported XML file. If not provided, a default filename will be used. |
| `$params`   | **?array**       |                                                                                          |

***

### exportJson

Export data as JSON file for download.

```php
public exportJson(mixed $list, string|null $filename = null, int $flags = \PhalconKit\Mvc\Controller\Traits\JSON_PRETTY_PRINT, int $depth = 2048): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type             | Description                                                                              |
|-------------|------------------|------------------------------------------------------------------------------------------|
| `$list`     | **mixed**        | The data to be exported as JSON. Can be an array, object, or any serializable data type. |
| `$filename` | **string\|null** | The name of the exported file. If not provided, the default filename will be used.       |
| `$flags`    | **int**          | Optional JSON encoding options. Default is JSON_PRETTY_PRINT.                            |
| `$depth`    | **int**          | Optional maximum depth of recursion. Default is 2048.                                    |

***

### exportExcel

Export data as an Excel spreadsheet

```php
public exportExcel(array $list, string|null $filename = null, bool $forceRawValue = true): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter        | Type             | Description                                           |
|------------------|------------------|-------------------------------------------------------|
| `$list`          | **array**        | The data to be exported                               |
| `$filename`      | **string\|null** | The desired filename for the exported file (optional) |
| `$forceRawValue` | **bool**         |                                                       |

***

### exportCsv

Export rows as CSV and translate CSV library failures into stable
PhalconKit exceptions.

```php
public exportCsv(array<array-key,mixed> $list, string|null $filename = null, array<array-key,mixed>|null $params = null): \Phalcon\Http\ResponseInterface
```

Request-controlled CSV options are validated by the League CSV writer.
Invalid delimiters, enclosures, escape characters, or BOM values become a
`400` HTTP exception because the client supplied an unsupported export
option. Insert/write failures remain server-side runtime errors and keep
the original League exception as `previous` for diagnostics.

**Parameters:**

| Parameter   | Type                             | Description                 |
|-------------|----------------------------------|-----------------------------|
| `$list`     | **array<array-key,mixed>**       | Rows to export.             |
| `$filename` | **string\|null**                 | Filename without extension. |
| `$params`   | **array<array-key,mixed>\|null** | CSV export options.         |

**Return Value:**

Download response containing CSV content.

**Throws:**

When a CSV export option has an invalid type or
value.
- [`HttpException`](../../../Exception/HttpException.md)
When CSV generation fails after options have
been accepted.
- [`RuntimeException`](../../../Exception/RuntimeException.md)

***

### buildCsvExportResponse

Build the CSV writer output and attach it to the controller response.

```php
private buildCsvExportResponse(array<array-key,mixed> $list, string|null $filename, array<array-key,mixed>|null $params): \Phalcon\Http\ResponseInterface
```

This method assumes its caller wraps League CSV exceptions through


- **See:** \PhalconKit\Mvc\Controller\Traits\withCsvExceptions(). Keeping the generation logic separate from
exception translation keeps the public method small while preserving the
current CSV behavior: Windows-compatible UTF-8 by default, UTF-16/tab
output for `mode=mac`, forced enclosures unless relaxed, and optional
newline collapsing for spreadsheet compatibility.

**Parameters:**

| Parameter   | Type                             | Description                 |
|-------------|----------------------------------|-----------------------------|
| `$list`     | **array<array-key,mixed>**       | Rows to export.             |
| `$filename` | **string\|null**                 | Filename without extension. |
| `$params`   | **array<array-key,mixed>\|null** | CSV export options.         |

**Throws:**

When League CSV rejects an option or cannot write
rows.
- [`Exception`](https://csv.thephpleague.com/){:target="_blank"}
When an option has a type that should not reach the
League writer.
- [`HttpException`](../../../Exception/HttpException.md)

***

### withCsvExceptions

Execute CSV generation while exposing stable framework exceptions.

```php
private withCsvExceptions(callable $callback): \Phalcon\Http\ResponseInterface
```

League CSV exceptions are useful internally but too vendor-specific for a
public REST controller helper. This wrapper keeps client option mistakes
as HTTP `400` errors and turns lower-level writer failures into
PhalconKit runtime exceptions with the original exception attached for
logs and debuggers.

**Parameters:**

| Parameter   | Type         | Description              |
|-------------|--------------|--------------------------|
| `$callback` | **callable** | CSV generation callback. |

**Throws:**

When a CSV option is rejected by the writer.
- [`HttpException`](../../../Exception/HttpException.md)
When CSV writing fails after options are valid.
- [`RuntimeException`](../../../Exception/RuntimeException.md)

***

### getCsvStringOption

Return a string-based CSV option from the export parameter array.

```php
private getCsvStringOption(array<array-key,mixed> $params, string $name): ?string
```

CSV control options are normally request values and must be strings before
they are passed to League CSV's typed setters. Validating the shape here
turns accidental nested arrays or objects into a stable HTTP `400` instead
of a PHP `TypeError`.

**Parameters:**

| Parameter | Type                       | Description          |
|-----------|----------------------------|----------------------|
| `$params` | **array<array-key,mixed>** | Export options.      |
| `$name`   | **string**                 | Option name to read. |

**Throws:**

When the option is present but not a string.
- [`HttpException`](../../../Exception/HttpException.md)

***

### getCsvOutputBomOption

Return the optional output BOM value accepted by the CSV writer.

```php
private getCsvOutputBomOption(array<array-key,mixed> $params): \League\Csv\Bom|string|null
```

Application code can pass a League `Bom` enum directly, while request
input usually passes one of the string values supported by League CSV.
Other shapes are rejected before they reach the writer's typed API.

**Parameters:**

| Parameter | Type                       | Description     |
|-----------|----------------------------|-----------------|
| `$params` | **array<array-key,mixed>** | Export options. |

**Throws:**

When the `outputBOM` option has an unsupported type.
- [`HttpException`](../../../Exception/HttpException.md)

***

### initializeRestActions

Initialize action-level REST configuration.

```php
public initializeRestActions(): void
```

Query configuration lives in

- **See:** \PhalconKit\Mvc\Controller\Traits\Query::initializeQuery(),
while action traits can expose smaller policy sets that affect only their
response behavior. Count, distinct, and list-count policies are
initialized here so controllers can customize action metadata through the
same lifecycle used by the rest of the REST API layer.

***

### initialize

Initialize the model-backed REST controller.

```php
public initialize(): mixed
```

The query initializer prepares filters, joins, conditions, bind values,
pagination, and the final `find` policy used by the standard REST actions.
The action initializer prepares response-shaping policies that are not part
of the database query itself, such as optional count-action metadata,
embedded list counts, and distinct-value fields.

Concrete API controllers that override `initialize()` should call
`parent::initialize()` unless they intentionally replace the full REST
setup lifecycle.

***
