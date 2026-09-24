
Combined dispatcher contract for PhalconKit CLI dispatchers.

Native CLI modules need Phalcon's dispatcher interface, while shared
PhalconKit diagnostics expect the framework dispatcher interface. This
combined contract lets DI providers enforce both without depending on the
concrete dispatcher class.

***

* Full name: `\PhalconKit\Cli\DispatcherInterface`
* Parent interfaces:
  `Dispatcher`,
  [`\PhalconKit\Dispatcher\DispatcherInterface`](../Dispatcher/DispatcherInterface.md)

## Inherited methods

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
