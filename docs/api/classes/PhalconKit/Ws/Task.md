
Base class for WebSocket tasks.

Tasks get typed access to the WebSocket console, router, and dispatcher
through PhalconKit injectable properties. Concrete tasks should implement
action methods such as `listenAction()`.

***

* Full name: `\PhalconKit\Ws\Task`
* Parent class: [`Task`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Ws\TaskInterface`](./TaskInterface.md)

## Methods

### resetConnectionState

Clear request-scoped model connection state in a long-running worker.

```php
public resetConnectionState(): void
```

Call this before custom WebSocket callbacks that perform model reads or
writes. The built-in abstract task invokes it for open, message, close,
HTTP request, and pipe-message callbacks.

***
