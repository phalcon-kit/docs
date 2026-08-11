
Contract for setting HTTP status codes on controller responses.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\StatusCodeInterface`

## Methods

### setStatusCode

Set the current response status code.

```php
public setStatusCode(int $code = 200, string|null $message = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter  | Type             | Description                  |
|------------|------------------|------------------------------|
| `$code`    | **int**          | HTTP status code.            |
| `$message` | **string\|null** | Optional HTTP reason phrase. |

***
