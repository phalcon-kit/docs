
Contract for normalizing REST response payloads.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\RestResponseInterface`

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
