
Raised for WebSocket bootstrap, routing, or request-handling failures.

Use this exception when an error belongs specifically to the WebSocket
execution boundary and should be distinguishable from MVC HTTP or CLI
failures. Service/configuration problems inside that boundary should still
prefer the more specific PhalconKit exception category when possible.

***

* Full name: `\PhalconKit\Exception\WsException`
* Parent class: [`\PhalconKit\Exception`](../Exception.md)
