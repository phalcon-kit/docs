
HTTP request contract extended with PhalconKit request helpers.

The extra helpers expose CORS, preflight, same-origin checks, and a diagnostic
array snapshot used by framework controllers and debugging tools. The helpers
classify request shape only; response policy such as allowed origins and
headers remains the responsibility of the application layer.

***

* Full name: `\PhalconKit\Http\RequestInterface`
* Parent interfaces:
  `RequestInterface`

## Methods

### isCors

Return true when an Origin header targets a different origin.

```php
public isCors(): bool
```

**Return Value:**

True when the request has a cross-origin `Origin` header.

***

### isPreflight

Return true when the request is a browser CORS preflight request.

```php
public isPreflight(): bool
```

A preflight request must be cross-origin, use `OPTIONS`, and include a
non-empty `Access-Control-Request-Method` header.

**Return Value:**

True when the request is shaped like a browser CORS
preflight.

***

### isSameOrigin

Check whether the Origin header matches the current scheme and host.

```php
public isSameOrigin(): bool
```

**Return Value:**

True when `Origin` equals the request scheme and host.

***

### toArray

Export a diagnostic snapshot of request input and derived request flags.

```php
public toArray(): array<string,mixed>
```

The result may contain headers and authentication metadata. Treat it as a
debug/testing surface and redact sensitive values before production logs.

**Return Value:**

Request bodies, parameters, headers,
negotiated values, origin flags, HTTP method flags, and server
metadata.

***
