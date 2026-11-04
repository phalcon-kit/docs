
Base class for WebSocket tasks.

Tasks get typed access to the WebSocket console, router, and dispatcher
through PhalconKit injectable properties. Concrete tasks should implement
action methods such as `listenAction()`.

***

* Full name: `\PhalconKit\Modules\Ws\Task`
* Parent class: [`\PhalconKit\Ws\Task`](../../Ws/Task.md)

## Inherited methods

### resetRequestState

Clear all request-scoped state in a long-running worker.

```php
public resetRequestState(): void
```

One Swoole worker serves many clients with the same container, so state
from one callback must not reach the next: write-connection pinning, the
identity manager's cached claim and users, the model ACL role cache, and
the Blameable parent link. The built-in abstract task invokes this for
open, message, close, HTTP request, and pipe-message callbacks; call it
before custom callbacks that authenticate or perform model operations.

***

### resetConnectionState

Clear request-scoped model connection state in a long-running worker.

```php
public resetConnectionState(): void
```

This is part of `resetRequestState()`, which callbacks should call
instead so identity and model ACL caches are reset too.

***
