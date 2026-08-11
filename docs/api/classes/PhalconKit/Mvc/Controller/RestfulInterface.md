
Contract for full resource controllers.

`RestfulInterface` extends the base REST controller contract with exposure
helpers used by find/list/export actions. It represents controllers that are
expected to provide the package's full resource workflow rather than only
custom REST actions.

***

* Full name: `\PhalconKit\Mvc\Controller\RestfulInterface`
* Parent interfaces:
  [`\PhalconKit\Mvc\Controller\Traits\Interfaces\ExposeInterface`](./Traits/Interfaces/ExposeInterface.md),
  [`\PhalconKit\Mvc\Controller\RestInterface`](./RestInterface.md)

## Inherited methods

### setRestErrorResponse

Set an error response payload and status code.

```php
public setRestErrorResponse(int $code = 400, string $status = 'Bad Request', mixed $response = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type       | Description          |
|-------------|------------|----------------------|
| `$code`     | **int**    | HTTP status code.    |
| `$status`   | **string** | HTTP status message. |
| `$response` | **mixed**  | Error payload.       |

***

### setRestResponse

Set a JSON REST response payload.

```php
public setRestResponse(mixed $response = null, int|null $code = null, string|null $status = null, int $jsonOptions = 0, int $depth = 512): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter      | Type             | Description                   |
|----------------|------------------|-------------------------------|
| `$response`    | **mixed**        | Response payload.             |
| `$code`        | **int\|null**    | Optional HTTP status code.    |
| `$status`      | **string\|null** | Optional HTTP status message. |
| `$jsonOptions` | **int**          | JSON encoding flags.          |
| `$depth`       | **int**          | Maximum JSON encoding depth.  |

***

### getFractalManager

Return the current Fractal manager, creating one when needed.

```php
public getFractalManager(): \PhalconKit\Fractal\Manager
```

***

### setFractalManager

Replace or reset the current Fractal manager.

```php
public setFractalManager(?\PhalconKit\Fractal\Manager $manager): void
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$manager` | **?\PhalconKit\Fractal\Manager** |             |

***

### getFractalSerializer

Return the serializer used by new Fractal managers.

```php
public getFractalSerializer(): \League\Fractal\Serializer\SerializerAbstract
```

***

### setFractalSerializer

Set the serializer used by new Fractal managers.

```php
public setFractalSerializer(\League\Fractal\Serializer\SerializerAbstract $serializer): void
```

**Parameters:**

| Parameter     | Type                                              | Description |
|---------------|---------------------------------------------------|-------------|
| `$serializer` | **\League\Fractal\Serializer\SerializerAbstract** |             |

***

### getTransformer

Return the controller's configured transformer.

```php
public getTransformer(): \League\Fractal\TransformerAbstract
```

***

### setTransformer

Replace or reset the controller's transformer.

```php
public setTransformer(?\League\Fractal\TransformerAbstract $transformer = null): void
```

**Parameters:**

| Parameter      | Type                                     | Description |
|----------------|------------------------------------------|-------------|
| `$transformer` | **?\League\Fractal\TransformerAbstract** |             |

***

### hasTransformer

Determine whether a transformer is currently configured.

```php
public hasTransformer(): bool
```

***

### transformModel

Transform one Phalcon model.

```php
public transformModel(\Phalcon\Mvc\ModelInterface $model, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$model`          | **\Phalcon\Mvc\ModelInterface**          |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***

### transformResultset

Transform a Phalcon model resultset.

```php
public transformResultset(\Phalcon\Mvc\Model\ResultsetInterface $resultset, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                      | Description |
|-------------------|-------------------------------------------|-------------|
| `$resultset`      | **\Phalcon\Mvc\Model\ResultsetInterface** |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract**  |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**          |             |

***

### transformItem

Transform one arbitrary item.

```php
public transformItem(mixed $data, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$data`           | **mixed**                                |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***

### transformCollection

Transform an arbitrary collection.

```php
public transformCollection(mixed $data, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$data`           | **mixed**                                |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***

### getParam

Return one filtered parameter value.

```php
public getParam(string $key, array|string|null $filters = null, mixed $default = null, array<array-key,mixed>|null $params = null): mixed
```

**Parameters:**

| Parameter  | Type                             | Description                            |
|------------|----------------------------------|----------------------------------------|
| `$key`     | **string**                       | Parameter key.                         |
| `$filters` | **array\|string\|null**          | Filter name(s) to apply.               |
| `$default` | **mixed**                        | Default value when the key is missing. |
| `$params`  | **array<array-key,mixed>\|null** | Optional parameter source.             |

***

### hasParam

Determine whether a parameter exists.

```php
public hasParam(string $key, array<array-key,mixed>|null $params = null, bool $cached = true): bool
```

**Parameters:**

| Parameter | Type                             | Description                                         |
|-----------|----------------------------------|-----------------------------------------------------|
| `$key`    | **string**                       |                                                     |
| `$params` | **array<array-key,mixed>\|null** | Optional parameter source.                          |
| `$cached` | **bool**                         | Whether cached controller parameters may be reused. |

***

### getParams

Return selected filtered controller parameters.

```php
public getParams(list<string>|array<string,array|string>|null $fields = null, bool $cached = true, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type                                                | Description                                               |
|-----------|-----------------------------------------------------|-----------------------------------------------------------|
| `$fields` | **list<string>\|array<string,array\|string>\|null** | Optional
field names or field-to-filter map.              |
| `$cached` | **bool**                                            | Whether cached controller parameters may be reused.       |
| `$deep`   | **bool**                                            | Whether nested parameters should be filtered
recursively. |

***

### getAllParams

Return all request parameters after default filters are applied.

```php
public getAllParams(array<string,array|string>|null $filters = null, bool $cached = true, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter  | Type                                  | Description                                               |
|------------|---------------------------------------|-----------------------------------------------------------|
| `$filters` | **array<string,array\|string>\|null** | Optional filter map.                                      |
| `$cached`  | **bool**                              | Whether cached controller parameters may be reused.       |
| `$deep`    | **bool**                              | Whether nested parameters should be filtered
recursively. |

***

### applyFilters

```php
public applyFilters(array<array-key,mixed> $params, array<string,array|string> $filters, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter  | Type                            | Description                                               |
|------------|---------------------------------|-----------------------------------------------------------|
| `$params`  | **array<array-key,mixed>**      |                                                           |
| `$filters` | **array<string,array\|string>** |                                                           |
| `$deep`    | **bool**                        | Whether nested parameters should be filtered
recursively. |

***

### setDefaultFilters

Replace default filters applied by `getAllParams()`.

```php
public setDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### addDefaultFilters

Merge additional default filters.

```php
public addDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### removeFilters

Remove one or more default filters by parameter key.

```php
public removeFilters(string|array<int,string> $keys): static
```

**Parameters:**

| Parameter | Type                          | Description |
|-----------|-------------------------------|-------------|
| `$keys`   | **string\|array<int,string>** |             |

***

### clearDefaultFilters

Remove all default filters.

```php
public clearDefaultFilters(): static
```

***

### getDefaultFilters

Return default filters applied by `getAllParams()`.

```php
public getDefaultFilters(): array<string,array|string>
```

***

### getRawParams

Return unfiltered request parameters.

```php
public getRawParams(bool $cached = true): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type     | Description                                  |
|-----------|----------|----------------------------------------------|
| `$cached` | **bool** | Whether cached raw parameters may be reused. |

***

### attachBehavior

Attach one behavior listener class.

```php
public attachBehavior(class-string $eventClass, string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter     | Type             | Description                               |
|---------------|------------------|-------------------------------------------|
| `$eventClass` | **class-string** | Listener class to instantiate or resolve. |
| `$eventType`  | **string\|null** | Event type, usually `rest` or `model`.    |
| `$priority`   | **int\|null**    | Optional event-manager priority.          |

***

### attachBehaviors

Attach multiple behavior listener definitions.

```php
public attachBehaviors(array<int|string,mixed> $behaviors = [], string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter    | Type                         | Description                                          |
|--------------|------------------------------|------------------------------------------------------|
| `$behaviors` | **array<int\|string,mixed>** | Behavior class names or nested
listener definitions. |
| `$eventType` | **string\|null**             | Default event type for class-name entries.           |
| `$priority`  | **int\|null**                | Optional event-manager priority.                     |

***

### isDebugEnabled

Determine whether debug output should be enabled for the current request.

```php
public isDebugEnabled(): bool
```

***

### expose

Expose one item according to an optional rule map.

```php
public expose(mixed $item, array<string|int,mixed>|null $expose = null): array<string,mixed>
```

**Parameters:**

| Parameter | Type                               | Description               |
|-----------|------------------------------------|---------------------------|
| `$item`   | **mixed**                          | Item to expose.           |
| `$expose` | **array<string\|int,mixed>\|null** | Exposure rule definition. |

***

### listExpose

Expose each item in a list response.

```php
public listExpose(iterable<array-key,mixed> $items, array<string|int,mixed>|null $expose = null): array<int|string,mixed>
```

**Parameters:**

| Parameter | Type                               | Description          |
|-----------|------------------------------------|----------------------|
| `$items`  | **iterable<array-key,mixed>**      | Items to expose.     |
| `$expose` | **array<string\|int,mixed>\|null** | List exposure rules. |

***

### exportExpose

Expose each item in an export response.

```php
public exportExpose(iterable<array-key,mixed> $items, array<string|int,mixed>|null $expose = null): array<int|string,mixed>
```

**Parameters:**

| Parameter | Type                               | Description            |
|-----------|------------------------------------|------------------------|
| `$items`  | **iterable<array-key,mixed>**      | Items to expose.       |
| `$expose` | **array<string\|int,mixed>\|null** | Export exposure rules. |

***
