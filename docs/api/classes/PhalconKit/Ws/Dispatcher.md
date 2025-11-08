
***

* Full name: `\PhalconKit\Ws\Dispatcher`
* Parent class: [`\PhalconKit\Cli\Dispatcher`](../Cli/Dispatcher.md)
* This class implements:
  [`\PhalconKit\Ws\DispatcherInterface`](./DispatcherInterface.md)

## Inherited methods

### getNamespaceName

```php
public getNamespaceName(): ?string
```

* This method is **abstract**.
***

### getModuleName

```php
public getModuleName(): ?string
```

* This method is **abstract**.
***

### getActionName

```php
public getActionName(): string
```

* This method is **abstract**.
***

### getParams

```php
public getParams(): array
```

* This method is **abstract**.
***

### getHandlerClass

```php
public getHandlerClass(): string
```

* This method is **abstract**.
***

### getHandlerSuffix

```php
public getHandlerSuffix(): string
```

* This method is **abstract**.
***

### getActionSuffix

```php
public getActionSuffix(): string
```

* This method is **abstract**.
***

### getActiveMethod

```php
public getActiveMethod(): string
```

* This method is **abstract**.
***

### callActionMethod

{@inheritDoc}
The string typed keys are not passed to the action method arguments
Only the int keys will be passed

```php
public callActionMethod(mixed $handler, string $actionMethod, array $params = []): mixed
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$handler`      | **mixed**  |             |
| `$actionMethod` | **string** |             |
| `$params`       | **array**  |             |

***

### forward

Extending forwarding event to prevent cyclic routing when forwarding under dispatcher events
{@inheritDoc}

```php
public forward(array $forward, bool $preventCycle = false): void
```

**Parameters:**

| Parameter       | Type      | Description |
|-----------------|-----------|-------------|
| `$forward`      | **array** |             |
| `$preventCycle` | **bool**  |             |

***

### canForward

Check whether the forward attribute can be forwarded
we do additional checks to prevent dispatcher cycling

```php
public canForward(array $forward): bool
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$forward` | **array** |             |

***

### canForwardHandler

Check whether the handler is changed or not
depending on the dispatcher
MVC: controller
CLI: task

```php
private canForwardHandler(array $forward): bool
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$forward` | **array** |             |

***

### canForwardController

Check whether the controller is changed

```php
private canForwardController(?string $controller = null): bool
```

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$controller` | **?string** |             |

***

### canForwardTask

Check whether the task is changed

```php
private canForwardTask(?string $task = null): bool
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$task`   | **?string** |             |

***

### unsetForwardNullParts

```php
public unsetForwardNullParts(array $forward, ?array $parts = null): array
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$forward` | **array**  |             |
| `$parts`   | **?array** |             |

***

### toArray

```php
public toArray(): array
```

***
