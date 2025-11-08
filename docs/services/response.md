# Response Service

## Response Configuration

### Response Headers

```ini
RESPONSE_HEADER_CSP_REPORT_ONLY=
RESPONSE_HEADER_STRICT_TRANSPORT_SECURITY=max-age=63072000; includeSubDomains; preload
RESPONSE_HEADER_CONTENT_TYPE_OPTIONS=nosniff
RESPONSE_HEADER_FRAME_OPTIONS=Deny
RESPONSE_HEADER_XSS_PROTECTION=0
```

### CORS related Response Headers

```ini
RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_ORIGIN=*
RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_METHODS=GET, POST, OPTIONS, PUT, PATCH, DELETE
RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_HEADERS=Origin, X-Requested-With, Content-Range, Content-Disposition, Content-Type, Authorization, X-Authorization
RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS=true
RESPONSE_HEADER_ACCESS_CONTROL_MAX_AGE=600
```

### Response Service Provider

```ini
PROVIDER_RESPONSE=\Zemit\Provider\Response\ServiceProvider
```

### Response Configuration Object

```php
<?php
new Config([
    'response' => [
        'headers' => [
            'Content-Security-Policy-Report-Only' => Env::get('RESPONSE_HEADER_CSP_REPORT_ONLY', ''),
            'Strict-Transport-Security' => Env::get('RESPONSE_HEADER_STRICT_TRANSPORT_SECURITY', 'max-age=63072000; includeSubDomains; preload'),
            'X-Content-Type-Options' => Env::get('RESPONSE_HEADER_CONTENT_TYPE_OPTIONS', 'nosniff'),
            'X-Frame-Options' => Env::get('RESPONSE_HEADER_FRAME_OPTIONS', 'Deny'),
            'X-XSS-Protection' => Env::get('RESPONSE_HEADER_XSS_PROTECTION', 0),
        ],
        'corsHeaders' => [
            'Access-Control-Allow-Origin' => Env::get('RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_ORIGIN', '*'),
            'Access-Control-Allow-Methods' => Env::get('RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_METHODS', 'GET, POST, OPTIONS, PUT, PATCH, DELETE'),
            'Access-Control-Allow-Headers' => Env::get('RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_HEADERS', 'Origin, X-Requested-With, Content-Range, Content-Disposition, Content-Type, Authorization, X-Authorization'),
            'Access-Control-Allow-Credentials' => Env::get('RESPONSE_HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS', 'true'),
            'Access-Control-Max-Age' => Env::get('RESPONSE_HEADER_ACCESS_CONTROL_MAX_AGE', '600'),
        ],
    ],
]);
```

## Response Service (`response`)

!!! info "Response Service Provider"
    Response Service Provider (`response`):
    [`\Zemit\Provider\Response\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Response/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$response = $this->response;

// Retrieving the service from the DI
$response = $this->di->get('response');

// Retrieving the service from the getDI()
$response = $this->getDI()->get('response');

// Retrieving the service from anywhere
$response = Di::getDefault()->get('response');
```
