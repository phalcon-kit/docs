
HTTP request implementation with PhalconKit request helpers.

The class preserves Phalcon's request API and adds CORS/preflight helpers plus
a diagnostic array export used by framework tooling. The CORS helpers are
intentionally request classifiers only; they do not apply policy, authorize
origins, or emit response headers.

***

* Full name: `\PhalconKit\Http\Request`
* Parent class: [`Request`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Http\RequestInterface`](./RequestInterface.md)

**See Also:**

* \Phalcon\Http\Request

## Methods

### isCors

Return true when an Origin header targets a different origin.

```php
public isCors(): bool
```

Same-origin requests with an `Origin` header are not considered CORS by
this helper. Policy decisions such as allowed origins should be handled by
middleware/controllers using this signal.

**Return Value:**

True when the request has a cross-origin `Origin` header.

***

### isPreflight

Return true when the request is a browser CORS preflight request.

```php
public isPreflight(): bool
```

A preflight request must be cross-origin, use `OPTIONS`, and include a
non-empty `Access-Control-Request-Method` header. This method only
identifies the request shape; it does not decide whether the preflight is
allowed.

**Return Value:**

True when the request is shaped like a browser CORS
preflight.

***

### isSameOrigin

Check whether the Origin header matches the current scheme and host.

```php
public isSameOrigin(): bool
```

The comparison uses Phalcon's detected scheme and HTTP host. Deployments
behind proxies should make sure those values are normalized before relying
on this helper.

**Return Value:**

True when `Origin` equals the request scheme and host.

***

### toArray

Export a diagnostic snapshot of request input and derived request flags.

```php
public toArray(): array<string,mixed>
```

The result is meant for debug output and tests. It includes request
headers and authentication metadata, so applications should avoid logging
this array wholesale in production unless sensitive values are redacted.

**Return Value:**

Request bodies, parameters, headers,
negotiated values, origin flags, HTTP method flags, and server
metadata.

***
