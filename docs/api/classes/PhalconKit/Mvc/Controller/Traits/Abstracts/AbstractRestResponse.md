
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\AbstractRestResponse`

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
public setRestResponse(mixed $response = null, ?int $code = null, ?string $status = null, int $jsonOptions, int $depth = 512): \Phalcon\Http\ResponseInterface
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
