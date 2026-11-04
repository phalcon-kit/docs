
Marks a shared DI service that caches state for one logical request.

Long-running runtimes (RoadRunner-style workers that reuse the bootstrap,
Swoole WebSocket workers) keep shared services alive between requests.
Before each request or WebSocket callback, `RequestState::reset()` calls
`resetRequestState()` on every shared service implementing this interface
that has already been instantiated, so per-request caches such as the
authenticated identity are never served to the next request.

Implementations must only drop cached request state: they must not open
connections, read the request, or throw. Under PHP-FPM every request starts
with a fresh container, so the reset is a no-op there.

***

* Full name: `\PhalconKit\Di\RequestScopedInterface`

## Methods

### resetRequestState

Discard state cached for the previous request.

```php
public resetRequestState(): void
```

***
