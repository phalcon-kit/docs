
Set the status code to the response

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\StatusCode`

## Methods

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
