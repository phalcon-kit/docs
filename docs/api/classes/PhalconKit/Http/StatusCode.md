
According to Wikipedia List of HTTP status codes

Example:
```php
 StatusCode::getMessage[StatusCode::OK] // 'OK'
 StatusCode::getMessage[200] // 'OK'
 StatusCode::$messages[200] // 'OK'
 StatusCode::OK // 200
```

***

* Full name: `\PhalconKit\Http\StatusCode`

**See Also:**

* https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

## Constants

| Constant                               | Visibility | Type | Value |
|----------------------------------------|------------|------|-------|
| `CONTINUE`                             | public     |      | 100   |
| `SWITCHING_PROTOCOLS`                  | public     |      | 101   |
| `PROCESSING`                           | public     |      | 102   |
| `OK`                                   | public     |      | 200   |
| `CREATED`                              | public     |      | 201   |
| `ACCEPTED`                             | public     |      | 202   |
| `NON_AUTHORITATIVE_INFORMATION`        | public     |      | 203   |
| `NO_CONTENT`                           | public     |      | 204   |
| `RESET_CONTENT`                        | public     |      | 205   |
| `PARTIAL_CONTENT`                      | public     |      | 206   |
| `MULTI_STATUS`                         | public     |      | 207   |
| `ALREADY_REPORTED`                     | public     |      | 208   |
| `IM_USED`                              | public     |      | 226   |
| `MULTIPLE_CHOICES`                     | public     |      | 300   |
| `MOVED_PERMANENTLY`                    | public     |      | 301   |
| `FOUND`                                | public     |      | 302   |
| `SEE_OTHER`                            | public     |      | 303   |
| `NOT_MODIFIED`                         | public     |      | 304   |
| `USE_PROXY`                            | public     |      | 305   |
| `SWITCH_PROXY`                         | public     |      | 306   |
| `TEMPORARY_REDIRECT`                   | public     |      | 307   |
| `PERMANENT_REDIRECT`                   | public     |      | 308   |
| `BAD_REQUEST`                          | public     |      | 400   |
| `UNAUTHORIZED`                         | public     |      | 401   |
| `PAYMENT_REQUIRED`                     | public     |      | 402   |
| `FORBIDDEN`                            | public     |      | 403   |
| `NOT_FOUND`                            | public     |      | 404   |
| `METHOD_NOT_ALLOWED`                   | public     |      | 405   |
| `NOT_ACCEPTABLE`                       | public     |      | 406   |
| `PROXY_AUTHENTICATION_REQUIRED`        | public     |      | 407   |
| `REQUEST_TIMEOUT`                      | public     |      | 408   |
| `CONFLICT`                             | public     |      | 409   |
| `GONE`                                 | public     |      | 410   |
| `LENGTH_REQUIRED`                      | public     |      | 411   |
| `PRECONDITION_FAILED`                  | public     |      | 412   |
| `REQUEST_ENTITY_TOO_LARGE`             | public     |      | 413   |
| `REQUEST_URI_TOO_LONG`                 | public     |      | 414   |
| `UNSUPPORTED_MEDIA_TYPE`               | public     |      | 415   |
| `REQUESTED_RANGE_NOT_SATISFIABLE`      | public     |      | 416   |
| `EXPECTATION_FAILED`                   | public     |      | 417   |
| `IM_A_TEAPOT`                          | public     |      | 418   |
| `AUTHENTICATION_TIMEOUT`               | public     |      | 419   |
| `METHOD_FAILURE`                       | public     |      | 420   |
| `UNPROCESSABLE_ENTITY`                 | public     |      | 422   |
| `LOCKED`                               | public     |      | 423   |
| `FAILED_DEPENDENCY`                    | public     |      | 424   |
| `UPGRADE_REQUIRED`                     | public     |      | 426   |
| `PRECONDITION_REQUIRED`                | public     |      | 428   |
| `TOO_MANY_REQUESTS`                    | public     |      | 429   |
| `REQUEST_HEADER_FIELDS_TOO_LARGE`      | public     |      | 431   |
| `LOGIN_TIMEOUT`                        | public     |      | 440   |
| `NO_RESPONSE`                          | public     |      | 444   |
| `RETRY_WITH`                           | public     |      | 449   |
| `BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS` | public     |      | 450   |
| `UNAVAILABLE_FOR_LEGAL_REASONS`        | public     |      | 451   |
| `REQUEST_HEADER_TOO_LARGE`             | public     |      | 494   |
| `CERT_ERROR`                           | public     |      | 495   |
| `NO_CERT`                              | public     |      | 496   |
| `HTTP_TO_HTTPS`                        | public     |      | 497   |
| `TOKEN_EXPIREDINVALID`                 | public     |      | 498   |
| `CLIENT_CLOSED_REQUEST`                | public     |      | 499   |
| `INTERNAL_SERVER_ERROR`                | public     |      | 500   |
| `NOT_IMPLEMENTED`                      | public     |      | 501   |
| `BAD_GATEWAY`                          | public     |      | 502   |
| `SERVICE_UNAVAILABLE`                  | public     |      | 503   |
| `GATEWAY_TIMEOUT`                      | public     |      | 504   |
| `HTTP_VERSION_NOT_SUPPORTED`           | public     |      | 505   |
| `VARIANT_ALSO_NEGOTIATES`              | public     |      | 506   |
| `INSUFFICIENT_STORAGE`                 | public     |      | 507   |
| `LOOP_DETECTED`                        | public     |      | 508   |
| `BANDWIDTH_LIMIT_EXCEEDED`             | public     |      | 509   |
| `NOT_EXTENDED`                         | public     |      | 510   |
| `NETWORK_AUTHENTICATION_REQUIRED`      | public     |      | 511   |
| `NETWORK_READ_TIMEOUT_ERROR`           | public     |      | 598   |
| `NETWORK_CONNECT_TIMEOUT_ERROR`        | public     |      | 599   |
| `FATAL_ERROR`                          | public     |      | 500   |
| `MAINTENANCE`                          | public     |      | 503   |
| `OVERLOADED`                           | public     |      | 503   |
| `BUSY`                                 | public     |      | 503   |

## Properties

### messages

```php
public static array $messages
```

* This property is **static**.

***

## Methods

### getMessage

Get the HTTP status message for the specified HTTP status code
getMessage(200) -> 'OK'

```php
public static getMessage(int $code): ?string
```

* This method is **static**.
**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$code`   | **int** |             |

***

### getCode

Get the HTTP code from the specified HTTP status message
getCode('OK') -> 200

```php
public static getCode(string $message): ?int
```

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$message` | **string** |             |

***

### getStatus

Get the HTTP code from the specified HTTP status message
getStatus(200) -> '200 OK'

```php
public static getStatus(int $code): ?string
```

* This method is **static**.
**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$code`   | **int** |             |

***
