
Generic PhalconKit dispatcher helper.

Native Phalcon 5.16 requires concrete dispatchers to implement the internal
exception hooks used by the dispatch loop. MVC and CLI dispatchers keep their
native specialized behavior; this generic wrapper provides a minimal
concrete implementation so shared helper behavior can still be tested and
used where no namespace-specific dispatcher is required.

***

* Full name: `\PhalconKit\Dispatcher\AbstractDispatcher`
* Parent class: [`AbstractDispatcher`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Dispatcher\DispatcherInterface`](./DispatcherInterface.md)

## Methods

### handleException

Bubble user exceptions unchanged for the generic dispatcher wrapper.

```php
protected handleException(\Exception $exception): never
```

Namespace-specific dispatchers can route exceptions through their
`dispatch:beforeException` event flow, but this base helper has no
controller/task domain to recover through.

**Parameters:**

| Parameter    | Type           | Description                       |
|--------------|----------------|-----------------------------------|
| `$exception` | **\Exception** | Exception raised during dispatch. |

**Throws:**

Always rethrows the original exception.
- [`Exception`](https://www.php.net/manual/en/class.exception.php){:target="_blank"}

***

### throwDispatchException

Raise a generic dispatcher exception for base-wrapper dispatch failures.

```php
protected throwDispatchException(string $message, int $exceptionCode = 0): never
```

**Parameters:**

| Parameter        | Type       | Description                       |
|------------------|------------|-----------------------------------|
| `$message`       | **string** | Diagnostic failure message.       |
| `$exceptionCode` | **int**    | Native dispatcher exception code. |

**Throws:**

Always throws the generated dispatcher
exception.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

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
