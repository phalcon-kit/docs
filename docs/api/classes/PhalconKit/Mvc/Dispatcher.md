
MVC dispatcher with PhalconKit's shared dispatcher safeguards.

The dispatcher keeps Phalcon's MVC dispatch behavior and mixes in the
framework forwarding protections and diagnostic export helpers from
`DispatcherTrait`.

***

* Full name: `\PhalconKit\Mvc\Dispatcher`
* Parent class: [`Dispatcher`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Dispatcher\DispatcherInterface`](../Dispatcher/DispatcherInterface.md)

**See Also:**

* https://docs.phalcon.io/5.18/dispatcher/

## Inherited methods

### getNamespaceName

Return the namespace currently targeted by the dispatcher.

```php
public getNamespaceName(): ?string
```

* This method is **abstract**.
***

### getModuleName

Return the module currently targeted by the dispatcher.

```php
public getModuleName(): ?string
```

* This method is **abstract**.
***

### setModuleName

Update the current module name before forwarding.

```php
public setModuleName(?string $moduleName = null): void
```

* This method is **abstract**.
**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$moduleName` | **?string** |             |

***

### getActionName

Return the action currently targeted by the dispatcher.

```php
public getActionName(): string
```

* This method is **abstract**.
***

### getParams

Return current dispatch parameters.

```php
public getParams(): array<int|string,mixed>
```

* This method is **abstract**.
***

### getHandlerClass

Return the resolved controller or task class name.

```php
public getHandlerClass(): string
```

* This method is **abstract**.
***

### getHandlerSuffix

Return the native handler suffix used by the dispatcher.

```php
public getHandlerSuffix(): string
```

* This method is **abstract**.
***

### getActionSuffix

Return the native action suffix used by the dispatcher.

```php
public getActionSuffix(): string
```

* This method is **abstract**.
***

### getActiveMethod

Return the concrete handler method name Phalcon will invoke.

```php
public getActiveMethod(): string
```

* This method is **abstract**.
***

### callActionMethod

Invoke a controller or task action with positional parameters only.

```php
public callActionMethod(mixed $handler, string $actionMethod, array<int|string,mixed> $params = []): mixed
```

Phalcon stores dispatch params as an array that may contain named metadata.
Only integer-keyed entries are passed to action method arguments so route
metadata cannot accidentally shift the method signature.

**Parameters:**

| Parameter       | Type                         | Description                                      |
|-----------------|------------------------------|--------------------------------------------------|
| `$handler`      | **mixed**                    | Controller or task instance selected by Phalcon. |
| `$actionMethod` | **string**                   | Method name to call on the handler.              |
| `$params`       | **array<int\|string,mixed>** | Dispatch parameters.                             |

**Return Value:**

Action return value.

***

### forward

Forward to another target, optionally skipping cyclic forwards.

```php
public forward(array<string,mixed> $forward, bool $preventCycle = false): void
```

Null forward parts are stripped before delegating to Phalcon. When
`$preventCycle` is true, forwarding only happens if at least one target
part differs from the current dispatch state.

**Parameters:**

| Parameter       | Type                    | Description                                   |
|-----------------|-------------------------|-----------------------------------------------|
| `$forward`      | **array<string,mixed>** | Forward target parts.                         |
| `$preventCycle` | **bool**                | Whether identical forwards should be ignored. |

***

### canForward

Determine whether a forward target differs from the current dispatch.

```php
public canForward(array<array-key,mixed> $forward): bool
```

**Parameters:**

| Parameter  | Type                       | Description           |
|------------|----------------------------|-----------------------|
| `$forward` | **array<array-key,mixed>** | Forward target parts. |

***

### canForwardHandler

Determine whether the dispatcher-specific handler target changes.

```php
private canForwardHandler(array<string,mixed> $forward): bool
```

MVC dispatchers compare controllers; CLI dispatchers compare tasks.

**Parameters:**

| Parameter  | Type                    | Description           |
|------------|-------------------------|-----------------------|
| `$forward` | **array<string,mixed>** | Forward target parts. |

***

### canForwardController

Determine whether an MVC forward points to a different controller.

```php
private canForwardController(?string $controller = null): bool
```

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$controller` | **?string** |             |

***

### canForwardTask

Determine whether a CLI forward points to a different task.

```php
private canForwardTask(?string $task = null): bool
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$task`   | **?string** |             |

***

### unsetForwardNullParts

Remove null parts from a forward target before delegating to Phalcon.

```php
public unsetForwardNullParts(array<string,mixed> $forward, array<int,string>|null $parts = null): array<string,mixed>
```

**Parameters:**

| Parameter  | Type                        | Description                                                              |
|------------|-----------------------------|--------------------------------------------------------------------------|
| `$forward` | **array<string,mixed>**     | Forward target parts.                                                    |
| `$parts`   | **array<int,string>\|null** | Forward keys to inspect. Defaults
to the common MVC and CLI target keys. |

**Return Value:**

Forward target with null parts removed.

***

### toArray

Export the active dispatcher state for diagnostics and debug responses.

```php
public toArray(): array<string,mixed>
```

**Return Value:**

Current namespace, module, handler, action,
parameters, and dispatcher-specific previous route state.

***
