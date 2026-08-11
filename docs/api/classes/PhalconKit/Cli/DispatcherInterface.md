
Combined dispatcher contract for PhalconKit CLI dispatchers.

Native CLI modules need Phalcon's dispatcher interface, while shared
PhalconKit diagnostics expect the framework dispatcher interface. This
combined contract lets DI providers enforce both without depending on the
concrete dispatcher class.

***

* Full name: `\PhalconKit\Cli\DispatcherInterface`
* Parent interfaces:
  `DispatcherInterface`,
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
