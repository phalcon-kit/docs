
Shared dispatcher contract for PhalconKit MVC, CLI, and WebSocket dispatchers.

The interface keeps native Phalcon dispatcher behavior while adding two
framework conveniences: cycle-aware forward checks and diagnostic state
export. Dispatcher listeners can depend on this contract when they do not
care whether the active handler is an MVC controller or CLI/WebSocket task.

***

* Full name: `\PhalconKit\Dispatcher\DispatcherInterface`
* Parent interfaces:
  `DispatcherInterface`

**See Also:**

* https://docs.phalcon.io/latest/dispatcher/

## Methods

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
