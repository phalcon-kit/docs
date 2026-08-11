
Base class for WebSocket tasks.

Tasks get typed access to the WebSocket console, router, and dispatcher
through PhalconKit injectable properties. Concrete tasks should implement
action methods such as `listenAction()`.

***

* Full name: `\PhalconKit\Modules\Ws\Task`
* Parent class: [`\PhalconKit\Ws\Task`](../../Ws/Task.md)
