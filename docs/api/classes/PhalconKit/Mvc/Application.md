
MVC application with PhalconKit's typed DI boundary and HMVC helper.

The application keeps Phalcon's MVC lifecycle, but it requires a PhalconKit
DI implementation so internal framework code can rely on typed service
helpers. `request()` provides a small HMVC dispatch helper for rendering an
internal controller/task target without mutating the active dispatcher.

***

* Full name: `\PhalconKit\Mvc\Application`
* Parent class: [`Application`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/5.18/application/

## Methods

### __construct

Creates an HMVC application bound to a PhalconKit DI container.

```php
public __construct(\Phalcon\Di\DiInterface $di): mixed
```

The constructor keeps Phalcon's native DI signature so the application
remains compatible with inherited Phalcon APIs, but the provided
container must implement PhalconKit's DI contract. This guarantees
runtime code can use typed service lookups and fail with framework
exceptions when a service is missing or misconfigured.

**Parameters:**

| Parameter | Type                        | Description                                     |
|-----------|-----------------------------|-------------------------------------------------|
| `$di`     | **\Phalcon\Di\DiInterface** | Container used to resolve application
services. |

**Throws:**

When the container does not expose PhalconKit
typed DI helpers.
- [`ServiceException`](../Exception/ServiceException.md)

***

### setDI

Assigns the application DI container.

```php
public setDI(\Phalcon\Di\DiInterface $container): void
```

Phalcon exposes this setter through its injection-aware base class. The
override keeps that public extension point available while enforcing that
replacement containers still implement PhalconKit's typed DI contract.

**Parameters:**

| Parameter    | Type                        | Description                        |
|--------------|-----------------------------|------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface** | Replacement application container. |

**Throws:**

When the container does not expose PhalconKit
typed DI helpers.
- [`ServiceException`](../Exception/ServiceException.md)

***

### request

Dispatches an internal HMVC location and returns its rendered content.

```php
public request(array{namespace?: string, module?: string, controller?: string, task?: string, action?: string, params?: array} $location = []): string
```

The current `dispatcher` DI service is cloned before routing state is
applied, so nested HMVC requests do not mutate the application's main
dispatcher. MVC dispatchers receive a controller name, CLI dispatchers
receive a task name, and all dispatchers receive namespace, module,
action, and params from the location array.

**Parameters:**

| Parameter   | Type                                                                                                                | Description                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `$location` | **array{namespace?: string, module?: string, controller?: string, task?: string, action?: string, params?: array}** | Optional namespace/module/controller/task/action/params
overrides for the internal request. |

**Return Value:**

Response content, scalar dispatcher return value, or an
empty string when the dispatcher returns null.

**Throws:**

When the dispatcher service is missing or does
not extend Phalcon's abstract dispatcher.
- [`ServiceException`](../Exception/ServiceException.md)
Propagates dispatcher and controller failures
unchanged so HTTP/domain exceptions keep their original type and
status semantics.
- [`Throwable`](https://www.php.net/manual/en/class.throwable.php){:target="_blank"}

***
