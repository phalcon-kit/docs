
WebSocket router built on Phalcon's CLI routing model.

WebSocket commands are dispatched more like CLI tasks than MVC HTTP routes,
so the WebSocket module reuses the PhalconKit CLI router while exposing the
shared framework router contract.

***

* Full name: `\PhalconKit\Ws\Router`
* Parent class: [`\PhalconKit\Cli\Router`](../Cli/Router.md)
* This class implements:
  [`\PhalconKit\Router\RouterInterface`](../Router/RouterInterface.md)

**See Also:**

* \PhalconKit\Cli\Router - for the native CLI router-interface compatibility
note.

## Inherited methods

### toArray

Export the current CLI router match state for diagnostics.

```php
public toArray(): array<string,mixed>
```

**Return Value:**

Current module, task, action, params,
matches, and matched-route metadata.

***
