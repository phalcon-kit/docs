
Shared dispatcher contract for PhalconKit MVC, CLI, and WebSocket dispatchers.

The interface keeps native Phalcon dispatcher behavior while adding two
framework conveniences: cycle-aware forward checks and diagnostic state
export. Dispatcher listeners can depend on this contract when they do not
care whether the active handler is an MVC controller or CLI/WebSocket task.

***

* Full name: `\PhalconKit\Dispatcher\DispatcherInterface`
* Parent interfaces:
  `Dispatcher`

**See Also:**

* https://docs.phalcon.io/latest/dispatcher/

## Methods

### canForward

Determine whether a forward target differs from the effective dispatch.

```php
public canForward(array<string,mixed> $forward): bool
```

Resolve empty namespace/handler/action names to dispatcher defaults and
preserve null/omitted parts without changing the live dispatch state.
Module and parameter values remain part of the comparison. Controller
takes precedence over task, matching native forward() in either mode.
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
