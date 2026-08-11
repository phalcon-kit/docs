
Attaches config-declared listeners to a Phalcon events manager.

This helper keeps the bootstrap-level event attachment contract small and
explicit. Applications configure listeners by event type, then each listener
definition resolves to a class or DI service. Listener priorities use
Phalcon's native priority support; the helper enables
priorities before attaching so configured ordering works consistently across
MVC, CLI, WebSocket, and test bootstraps that share the same events manager.

Supported listener definition forms:

- `ListenerClass::class`
- `'listenerServiceName'`
- `['class' => ListenerClass::class, 'priority' => 200]`
- `['service' => 'listenerServiceName', 'priority' => 200]`

Array definitions may set `enabled => false` to disable one entry without
removing it from merged configuration.

***

* Full name: `\PhalconKit\Events\ConfiguredEventListeners`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Methods

### __construct

```php
private __construct(): mixed
```

***

### attach

Attach configured listeners to the provided manager.

```php
public static attach(\PhalconKit\Di\DiInterface $di, \Phalcon\Contracts\Events\Manager $eventsManager, array<array-key,mixed> $listeners): void
```

The expected config shape is an event-type map. Each value may be a
single listener definition or a list of listener definitions:

```php
[
    'dispatch' => [
        ['class' => App\Listener\Security::class, 'priority' => 200],
        ['service' => 'auditDispatchListener', 'priority' => 100],
    ],
]
```

* This method is **static**.
**Parameters:**

| Parameter        | Type                                  | Description                                                                                                                         |
|------------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `$di`            | **\PhalconKit\Di\DiInterface**        | Container used to resolve listener services and
inject DI into listener objects that implement Phalcon's
`InjectionAwareInterface`. |
| `$eventsManager` | **\Phalcon\Contracts\Events\Manager** | Events manager that receives the
listener attachments.                                                                              |
| `$listeners`     | **array<array-key,mixed>**            | Event-type map from config.                                                                                                         |

**Throws:**

When an event type, listener definition,
listener class, listener service, or priority is invalid.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### normalizeDefinitions

Normalize one event-type value to a list of listener definitions.

```php
private static normalizeDefinitions(mixed $definitions): array<int|string,mixed>
```

* This method is **static**.
**Parameters:**

| Parameter      | Type      | Description                      |
|----------------|-----------|----------------------------------|
| `$definitions` | **mixed** | Config value for one event type. |

***

### isAssociativeListenerDefinition

Detect whether an array is a single listener definition.

```php
private static isAssociativeListenerDefinition(array<array-key,mixed> $definition): bool
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                       | Description           |
|---------------|----------------------------|-----------------------|
| `$definition` | **array<array-key,mixed>** | Candidate definition. |

***

### resolveDefinition

Resolve one listener definition and expose its priority by reference.

```php
private static resolveDefinition(\PhalconKit\Di\DiInterface $di, mixed $definition, string $eventType, int|string $index, int& $priority): object|callable|null
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                           | Description                                  |
|---------------|--------------------------------|----------------------------------------------|
| `$di`         | **\PhalconKit\Di\DiInterface** |                                              |
| `$definition` | **mixed**                      | Listener definition from config.             |
| `$eventType`  | **string**                     |                                              |
| `$index`      | **int\|string**                | Original index inside the event-type config. |
| `$priority`   | **int**                        | Priority updated from the definition.        |

**Return Value:**

Resolved listener, or null when disabled.

***

### resolvePriority

Resolve and validate a listener priority.

```php
private static resolvePriority(mixed $priority, string $eventType, int|string $index): int
```

* This method is **static**.
**Parameters:**

| Parameter    | Type            | Description |
|--------------|-----------------|-------------|
| `$priority`  | **mixed**       |             |
| `$eventType` | **string**      |             |
| `$index`     | **int\|string** |             |

***

### listenerFromString

Resolve a shorthand string as a class name or DI service name.

```php
private static listenerFromString(\PhalconKit\Di\DiInterface $di, string $definition, string $eventType, int|string $index): object|callable
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                           | Description |
|---------------|--------------------------------|-------------|
| `$di`         | **\PhalconKit\Di\DiInterface** |             |
| `$definition` | **string**                     |             |
| `$eventType`  | **string**                     |             |
| `$index`      | **int\|string**                |             |

***

### listenerFromService

Resolve a listener from a configured DI service.

```php
private static listenerFromService(\PhalconKit\Di\DiInterface $di, mixed $service, string $eventType, int|string $index): object|callable
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                           | Description |
|--------------|--------------------------------|-------------|
| `$di`        | **\PhalconKit\Di\DiInterface** |             |
| `$service`   | **mixed**                      |             |
| `$eventType` | **string**                     |             |
| `$index`     | **int\|string**                |             |

***

### listenerFromClass

Instantiate a configured listener class.

```php
private static listenerFromClass(\PhalconKit\Di\DiInterface $di, mixed $class, string $eventType, int|string $index, array<array-key,mixed> $arguments = []): object|callable
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                           | Description            |
|--------------|--------------------------------|------------------------|
| `$di`        | **\PhalconKit\Di\DiInterface** |                        |
| `$class`     | **mixed**                      |                        |
| `$eventType` | **string**                     |                        |
| `$index`     | **int\|string**                |                        |
| `$arguments` | **array<array-key,mixed>**     | Constructor arguments. |

***

### finalizeListener

Validate the listener and inject the DI container when supported.

```php
private static finalizeListener(\PhalconKit\Di\DiInterface $di, mixed $listener, string $eventType, int|string $index): object|callable
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                           | Description |
|--------------|--------------------------------|-------------|
| `$di`        | **\PhalconKit\Di\DiInterface** |             |
| `$listener`  | **mixed**                      |             |
| `$eventType` | **string**                     |             |
| `$index`     | **int\|string**                |             |

***
