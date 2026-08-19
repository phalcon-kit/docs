
Contract for WebSocket task dispatchers.

This combines Phalcon's native CLI dispatcher surface with PhalconKit's
shared dispatcher helpers so WebSocket tasks can be resolved and inspected
through the same contract as CLI tasks.

***

* Full name: `\PhalconKit\Ws\DispatcherInterface`
* Parent interfaces:
  `Dispatcher`,
  [`\PhalconKit\Dispatcher\DispatcherInterface`](../Dispatcher/DispatcherInterface.md)

## Inherited methods

### canForward

Determine whether a forward target differs from the current dispatch.

```php
public canForward(array<string,mixed> $forward): bool
```

Implementations should compare only the route parts they understand.
This is used by listeners that forward to error, maintenance, or
unauthorized routes and need to avoid forwarding back to themselves.

**Parameters:**

| Parameter  | Type                    | Description          |
|------------|-------------------------|----------------------|
| `$forward` | **array<string,mixed>** | Forward route parts. |

***

### toArray

Export dispatcher state for logs, diagnostics, and tests.

```php
public toArray(): array<string,mixed>
```

***
