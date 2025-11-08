
Class Controller

***

* Full name: `\PhalconKit\Modules\Api\Controllers\AuthController`
* Parent class: [`\PhalconKit\Mvc\Controller\Rest`](../../../Mvc/Controller/Rest.md)

## Inherited methods

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
public getParams(array|null $fields = null, bool $cached = true, bool $deep = true): array<string,mixed>
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

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### getAllParams

Retrieve all request parameters, optionally applying filters and caching results.

```php
public getAllParams(array|null $filters = null, bool $cached = true, bool $deep = true): array<string,mixed>
```

**Parameters:**

| Parameter  | Type            | Description                                    |
|------------|-----------------|------------------------------------------------|
| `$filters` | **array\|null** | Temporary filters to apply.                    |
| `$cached`  | **bool**        | Whether to reuse previously loaded parameters. |
| `$deep`    | **bool**        | Whether to apply filters recursively.          |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### collectRequestParams

Collect parameters based on the HTTP method.

```php
private collectRequestParams(): array<string,mixed>
```

***

### applyFilters

Apply filters to parameters (recursively if $deep is true).

```php
public applyFilters(array<string,mixed> $params, array<string,array|string> $filters, bool $deep = true): array<string,mixed>
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$params`  | **array<string,mixed>**         |             |
| `$filters` | **array<string,array\|string>** |             |
| `$deep`    | **bool**                        |             |

**Throws:**

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
public getRawParams(bool $cached = true): array<string,mixed>
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

### getIdentityAction

Retrieve the current identity information

```php
public getIdentityAction(): bool
```

***

### getJwtAction

Create or refresh a JWT

```php
public getJwtAction(bool $refresh = false): bool
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***

### refreshAction

Refresh an existing JWT

```php
public refreshAction(): bool
```

***

### loginAction

Login

```php
public loginAction(): bool
```

***

### loginAsAction

Login As (impersonation)

```php
public loginAsAction(): bool
```

***

### logoutAction

Logout from current session

```php
public logoutAction(): bool
```

***

### logoutAsAction

Logout from impersonation

```php
public logoutAsAction(): bool
```

***

### resetPasswordAction

Reset Password Action

```php
public resetPasswordAction(): bool
```

***

### getLoginParams

Retrieves login parameters including email and password with applied filters.

```php
public getLoginParams(): array
```

**Return Value:**

Returns an array of login parameters with specified filters applied.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### getResetPasswordParams

Retrieves the parameters required for resetting a password with applied filters.

```php
public getResetPasswordParams(): array
```

**Return Value:**

Returns an array of reset password parameters with specified filters applied.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
