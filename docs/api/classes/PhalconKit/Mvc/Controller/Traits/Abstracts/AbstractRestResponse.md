
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\AbstractRestResponse`

## Constants

| Constant                 | Visibility | Type   | Value       |
|--------------------------|------------|--------|-------------|
| `REST_PAYLOAD_TIMESTAMP` | public     | string | 'timestamp' |
| `REST_PAYLOAD_STATUS`    | public     | string | 'status'    |
| `REST_PAYLOAD_CODE`      | public     | string | 'code'      |
| `REST_PAYLOAD_RESPONSE`  | public     | string | 'response'  |
| `REST_PAYLOAD_VIEW`      | public     | string | 'view'      |
| `REST_PAYLOAD_DEBUG`     | public     | string | 'debug'     |
| `REST_VIEW_INTERNAL`     | public     | string | '_'         |
| `REST_VIEW_DATA`         | public     | string | 'data'      |
| `REST_VIEW_MESSAGES`     | public     | string | 'messages'  |
| `REST_VIEW_COUNT`        | public     | string | 'count'     |
| `REST_VIEW_FIELD`        | public     | string | 'field'     |
| `REST_VIEW_SUM`          | public     | string | 'sum'       |
| `REST_VIEW_AVERAGE`      | public     | string | 'average'   |
| `REST_VIEW_MINIMUM`      | public     | string | 'minimum'   |
| `REST_VIEW_MAXIMUM`      | public     | string | 'maximum'   |
| `REST_VIEW_SAVED`        | public     | string | 'saved'     |
| `REST_VIEW_RESULTS`      | public     | string | 'results'   |
| `REST_VIEW_STATS`        | public     | string | 'stats'     |
| `REST_VIEW_DELETED`      | public     | string | 'deleted'   |
| `REST_VIEW_RESTORED`     | public     | string | 'restored'  |
| `REST_VIEW_REORDERED`    | public     | string | 'reordered' |

## Methods

### setRestErrorResponse

```php
public setRestErrorResponse(int $code = 400, string $status = 'Bad Request', mixed $response = null): \Phalcon\Http\ResponseInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$code`     | **int**    |             |
| `$status`   | **string** |             |
| `$response` | **mixed**  |             |

***
### setRestResponse

```php
public setRestResponse(mixed $response = null, ?int $code = null, ?string $status = null, int $jsonOptions = 0, int $depth = 512): \Phalcon\Http\ResponseInterface
```

* This method is **abstract**.
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

Set one public REST view field.

```php
protected setRestViewVar(string $key, mixed $value): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |
| `$value`  | **mixed**  |             |

***
### setRestViewVars

Set several public REST view fields.

```php
protected setRestViewVars(array<string,mixed> $vars, bool $merge = true): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                    | Description |
|-----------|-------------------------|-------------|
| `$vars`   | **array<string,mixed>** |             |
| `$merge`  | **bool**                |             |

***
