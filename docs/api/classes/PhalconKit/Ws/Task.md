
Base class for WebSocket tasks.

Tasks get typed access to the WebSocket console, router, and dispatcher
through PhalconKit injectable properties. Concrete tasks should implement
action methods such as `listenAction()`.

***

* Full name: `\PhalconKit\Ws\Task`
* Parent class: [`Task`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Ws\TaskInterface`](./TaskInterface.md)
