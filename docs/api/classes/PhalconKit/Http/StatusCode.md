
HTTP status-code constants and reason-phrase lookup helpers.

The list combines standard status codes with a few commonly encountered
vendor/proxy extension codes so framework code can avoid hard-coded numeric
literals in controllers, exceptions, and tests.

Example:
```php
StatusCode::getMessage(StatusCode::OK); // 'OK'
StatusCode::getMessage(200); // 'OK'
StatusCode::$messages[200]; // 'OK'
StatusCode::OK; // 200
```

***

* Full name: `\PhalconKit\Http\StatusCode`

**See Also:**

* https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

## Constants

| Constant                               | Visibility | Type | Value |
|----------------------------------------|------------|------|-------|
| `CONTINUE`                             | public     | int  | 100   |
| `SWITCHING_PROTOCOLS`                  | public     | int  | 101   |
| `PROCESSING`                           | public     | int  | 102   |
| `OK`                                   | public     | int  | 200   |
| `CREATED`                              | public     | int  | 201   |
| `ACCEPTED`                             | public     | int  | 202   |
| `NON_AUTHORITATIVE_INFORMATION`        | public     | int  | 203   |
| `NO_CONTENT`                           | public     | int  | 204   |
| `RESET_CONTENT`                        | public     | int  | 205   |
| `PARTIAL_CONTENT`                      | public     | int  | 206   |
| `MULTI_STATUS`                         | public     | int  | 207   |
| `ALREADY_REPORTED`                     | public     | int  | 208   |
| `IM_USED`                              | public     | int  | 226   |
| `MULTIPLE_CHOICES`                     | public     | int  | 300   |
| `MOVED_PERMANENTLY`                    | public     | int  | 301   |
| `FOUND`                                | public     | int  | 302   |
| `SEE_OTHER`                            | public     | int  | 303   |
| `NOT_MODIFIED`                         | public     | int  | 304   |
| `USE_PROXY`                            | public     | int  | 305   |
| `SWITCH_PROXY`                         | public     | int  | 306   |
| `TEMPORARY_REDIRECT`                   | public     | int  | 307   |
| `PERMANENT_REDIRECT`                   | public     | int  | 308   |
| `BAD_REQUEST`                          | public     | int  | 400   |
| `UNAUTHORIZED`                         | public     | int  | 401   |
| `PAYMENT_REQUIRED`                     | public     | int  | 402   |
| `FORBIDDEN`                            | public     | int  | 403   |
| `NOT_FOUND`                            | public     | int  | 404   |
| `METHOD_NOT_ALLOWED`                   | public     | int  | 405   |
| `NOT_ACCEPTABLE`                       | public     | int  | 406   |
| `PROXY_AUTHENTICATION_REQUIRED`        | public     | int  | 407   |
| `REQUEST_TIMEOUT`                      | public     | int  | 408   |
| `CONFLICT`                             | public     | int  | 409   |
| `GONE`                                 | public     | int  | 410   |
| `LENGTH_REQUIRED`                      | public     | int  | 411   |
| `PRECONDITION_FAILED`                  | public     | int  | 412   |
| `REQUEST_ENTITY_TOO_LARGE`             | public     | int  | 413   |
| `REQUEST_URI_TOO_LONG`                 | public     | int  | 414   |
| `UNSUPPORTED_MEDIA_TYPE`               | public     | int  | 415   |
| `REQUESTED_RANGE_NOT_SATISFIABLE`      | public     | int  | 416   |
| `EXPECTATION_FAILED`                   | public     | int  | 417   |
| `IM_A_TEAPOT`                          | public     | int  | 418   |
| `AUTHENTICATION_TIMEOUT`               | public     | int  | 419   |
| `METHOD_FAILURE`                       | public     | int  | 420   |
| `UNPROCESSABLE_ENTITY`                 | public     | int  | 422   |
| `LOCKED`                               | public     | int  | 423   |
| `FAILED_DEPENDENCY`                    | public     | int  | 424   |
| `UPGRADE_REQUIRED`                     | public     | int  | 426   |
| `PRECONDITION_REQUIRED`                | public     | int  | 428   |
| `TOO_MANY_REQUESTS`                    | public     | int  | 429   |
| `REQUEST_HEADER_FIELDS_TOO_LARGE`      | public     | int  | 431   |
| `LOGIN_TIMEOUT`                        | public     | int  | 440   |
| `NO_RESPONSE`                          | public     | int  | 444   |
| `RETRY_WITH`                           | public     | int  | 449   |
| `BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS` | public     | int  | 450   |
| `UNAVAILABLE_FOR_LEGAL_REASONS`        | public     | int  | 451   |
| `REQUEST_HEADER_TOO_LARGE`             | public     | int  | 494   |
| `CERT_ERROR`                           | public     | int  | 495   |
| `NO_CERT`                              | public     | int  | 496   |
| `HTTP_TO_HTTPS`                        | public     | int  | 497   |
| `TOKEN_EXPIREDINVALID`                 | public     | int  | 498   |
| `CLIENT_CLOSED_REQUEST`                | public     | int  | 499   |
| `INTERNAL_SERVER_ERROR`                | public     | int  | 500   |
| `NOT_IMPLEMENTED`                      | public     | int  | 501   |
| `BAD_GATEWAY`                          | public     | int  | 502   |
| `SERVICE_UNAVAILABLE`                  | public     | int  | 503   |
| `GATEWAY_TIMEOUT`                      | public     | int  | 504   |
| `HTTP_VERSION_NOT_SUPPORTED`           | public     | int  | 505   |
| `VARIANT_ALSO_NEGOTIATES`              | public     | int  | 506   |
| `INSUFFICIENT_STORAGE`                 | public     | int  | 507   |
| `LOOP_DETECTED`                        | public     | int  | 508   |
| `BANDWIDTH_LIMIT_EXCEEDED`             | public     | int  | 509   |
| `NOT_EXTENDED`                         | public     | int  | 510   |
| `NETWORK_AUTHENTICATION_REQUIRED`      | public     | int  | 511   |
| `NETWORK_READ_TIMEOUT_ERROR`           | public     | int  | 598   |
| `NETWORK_CONNECT_TIMEOUT_ERROR`        | public     | int  | 599   |
| `FATAL_ERROR`                          | public     | int  | 500   |
| `MAINTENANCE`                          | public     | int  | 503   |
| `OVERLOADED`                           | public     | int  | 503   |
| `BUSY`                                 | public     | int  | 503   |

## Properties

### messages

Map status codes to their reason phrases.

```php
public static array<int,string> $messages
```

* This property is **static**.

***

## Methods

### getMessage

Return the reason phrase for an HTTP status code.

```php
public static getMessage(int $code): string|null
```

* This method is **static**.
**Parameters:**

| Parameter | Type    | Description       |
|-----------|---------|-------------------|
| `$code`   | **int** | HTTP status code. |

**Return Value:**

Reason phrase, or null when the code is unknown.

***

### getCode

Return the HTTP status code for an exact reason phrase.

```php
public static getCode(string $message): int|null
```

Matching is case-sensitive and uses the reason phrases stored in
`StatusCode::$messages`.

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description               |
|------------|------------|---------------------------|
| `$message` | **string** | Reason phrase to look up. |

**Return Value:**

Status code, or null when the phrase is unknown.

***

### getStatus

Return a combined status line fragment such as `200 OK`.

```php
public static getStatus(int $code): string|null
```

Unknown codes return the numeric code as a string because existing callers
and tests use this helper as a display formatter, not only as a strict
lookup.

* This method is **static**.
**Parameters:**

| Parameter | Type    | Description       |
|-----------|---------|-------------------|
| `$code`   | **int** | HTTP status code. |

**Return Value:**

Status code plus reason phrase, or the numeric code as
a string when the phrase is unknown.

***
