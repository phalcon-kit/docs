
Shared contract for PhalconKit routers.

Routers expose their configured state as arrays for diagnostics, CLI output,
and tests while still supporting native Phalcon DI injection. MVC, CLI, and
WebSocket routers can implement this interface so bootstrap code can resolve
them through the same typed DI contract.

***

* Full name: `\PhalconKit\Router\RouterInterface`
* Parent interfaces:
  `InjectionAwareInterface`

## Methods

### toArray

Export router configuration/state as an array.

```php
public toArray(): array<string,mixed>
```

***

### setDefaults

Set default routing values.

```php
public setDefaults(array<string,mixed> $defaults): mixed
```

Native Phalcon router implementations return different concrete types
from `setDefaults()`, so this interface deliberately mirrors the native
loose return surface.

**Parameters:**

| Parameter   | Type                    | Description |
|-------------|-------------------------|-------------|
| `$defaults` | **array<string,mixed>** |             |

***
