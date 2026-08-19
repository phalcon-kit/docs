
Coordinates PhalconKit runtime setup for MVC, CLI, and WebSocket entrypoints.

The bootstrap owns the default startup sequence: select the runtime mode,
create and expose the PhalconKit DI container, register configuration,
register service providers, initialize core services, register modules, and
finally register the router. Applications may subclass this class to override
individual steps, but should preserve this ordering unless they fully own the
corresponding service wiring.

***

* Full name: `\PhalconKit\Bootstrap`

## Constants

| Constant   | Visibility | Type   | Value |
|------------|------------|--------|-------|
| `MODE_CLI` | public     | string | 'cli' |
| `MODE_WS`  | public     | string | 'ws'  |
| `MODE_MVC` | public     | string | 'mvc' |

## Properties

### di

Active application container.

```php
public \PhalconKit\Di\DiInterface $di
```

Bootstrap always stores a PhalconKit DI implementation so framework and
app code can rely on `getTyped()` and `getConfig()` while services are
being registered.

***

### mode

Runtime mode handled by this bootstrap instance.

```php
public string $mode
```

Supported values are `mvc`, `cli`, and `ws`. A custom mode can be stored
by subclasses, but the default `run()` and module-registration logic only
know the three built-in modes.

***

### args

Optional argument bag exposed for custom CLI bootstraps.

```php
public ?array $args
```

The default `getArgs()` implementation parses the current
`$_SERVER['argv']` value with Docopt. Subclasses that need pre-parsed
arguments can use this property as their own storage convention.

***

### config

Registered framework configuration, available after `registerConfig()`.

```php
public ?\PhalconKit\Config\ConfigInterface $config
```

***

### router

Registered MVC or CLI router, available after `registerRouter()`.

```php
public ?\PhalconKit\Router\RouterInterface $router
```

***

### response

Last MVC response produced by `handleApplication()`.

```php
public ?\Phalcon\Http\ResponseInterface $response
```

CLI and WebSocket modes do not populate this property.

***

### configuredEventListenersAttached

Whether config-declared listeners were attached to the shared manager.

```php
protected bool $configuredEventListenersAttached
```

`bootServices()` can be called directly in tests and custom bootstraps.
Tracking this state prevents duplicate configured listener registration
while keeping the default bootstrap sequence deterministic.

***

### cliDoc

Docopt command specification used by the default CLI argument parser.

```php
public string $cliDoc
```

Applications with custom CLI commands may override this string in a
bootstrap subclass before calling `getArgs()`.

***

## Methods

### __construct

Builds a ready-to-run bootstrap and executes the core registration steps.

```php
public __construct(string|null $mode = null): mixed
```

Passing `null` lets PhalconKit detect CLI versus MVC mode. WebSocket
entrypoints should pass `Bootstrap::MODE_WS` explicitly.

**Parameters:**

| Parameter | Type             | Description                                           |
|-----------|------------------|-------------------------------------------------------|
| `$mode`   | **string\|null** | Runtime mode to initialize, or `null` to auto-detect. |

**Throws:**

When configured service providers are
invalid or the selected runtime mode cannot be handled.
- [`ConfigurationException`](./Exception/ConfigurationException.md)
When configuration cannot be resolved.
- [`ConfigurationException`](./Exception/ConfigurationException.md)

***

### initialize

Application hook executed before config and service registration.

```php
public initialize(): void
```

Override this method in an application bootstrap for very early setup that
does not require configured services. Services from `config.providers`
are not registered yet, so provider-level customization usually belongs
in application config instead.

***

### setDI

Sets the active DI container and exposes it as the global Phalcon default.

```php
public setDI(?\PhalconKit\Di\DiInterface $di = null): void
```

When no container is provided, the bootstrap creates a PhalconKit default
container for the current mode. Custom containers must implement
`PhalconKit\Di\DiInterface`; native Phalcon containers do not expose the
typed helper methods used by bootstrap and service providers.

The bootstrap instance is registered as the shared `bootstrap` service so
injectable classes can inspect runtime state when they need to.

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$di`     | **?\PhalconKit\Di\DiInterface** |             |

***

### setMode

Sets the runtime mode for this bootstrap.

```php
public setMode(?string $mode = null): void
```

Passing `null` auto-detects CLI mode from the PHP runtime and otherwise
falls back to MVC. WebSocket mode must be selected explicitly.

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$mode`   | **?string** |             |

***

### getMode

Returns the selected runtime mode.

```php
public getMode(): string
```

***

### getDI

Returns the active PhalconKit DI container.

```php
public getDI(): \PhalconKit\Di\DiInterface
```

Consumers can use the returned container for native Phalcon DI access and
the PhalconKit-specific `getTyped()` and `getConfig()` helpers.

***

### setConfig

Stores the resolved framework configuration.

```php
public setConfig(\PhalconKit\Config\ConfigInterface $config): void
```

This method is primarily used by `registerConfig()` after the config
provider has created the `config` service. Application code normally
changes configuration through config files instead of calling this setter.

**Parameters:**

| Parameter | Type                                   | Description |
|-----------|----------------------------------------|-------------|
| `$config` | **\PhalconKit\Config\ConfigInterface** |             |

***

### getConfig

Returns the registered framework configuration.

```php
public getConfig(): \PhalconKit\Config\ConfigInterface
```

**Throws:**

When `registerConfig()` has not provided a
valid config instance.
- [`ConfigurationException`](./Exception/ConfigurationException.md)

***

### setRouter

Stores the resolved MVC or CLI router.

```php
public setRouter(\PhalconKit\Router\RouterInterface $router): void
```

This is normally called by `registerRouter()` after the router service has
been registered in DI.

**Parameters:**

| Parameter | Type                                   | Description |
|-----------|----------------------------------------|-------------|
| `$router` | **\PhalconKit\Router\RouterInterface** |             |

***

### getRouter

Returns the registered MVC or CLI router, when one has been initialized.

```php
public getRouter(): ?\PhalconKit\Router\RouterInterface
```

***

### registerConfig

Registers and stores the framework configuration service.

```php
public registerConfig(): void
```

If a `config` service already exists in DI, it is reused. Otherwise the
built-in config service provider is registered first. This method must run
before provider registration because `config.providers` drives the rest of
the bootstrap service graph.

***

### registerServices

Registers configured application and framework service providers.

```php
public registerServices(array<string,string>|null $providers = null): void
```

Provider values must be class-string names. Each provider is constructed
with the active PhalconKit DI container and must implement
`ServiceProviderInterface`; its `register()` method is then called
directly. This avoids relying on native Phalcon provider registration,
which cannot express PhalconKit's typed DI boundary.

**Parameters:**

| Parameter    | Type                           | Description                                            |
|--------------|--------------------------------|--------------------------------------------------------|
| `$providers` | **array<string,string>\|null** | Provider map. When `null`,
`config.providers` is used. |

**Throws:**

When a provider value is not a
class-string, the class cannot be found, or the instance does not
implement the provider contract.
- [`ConfigurationException`](./Exception/ConfigurationException.md)

***

### registerRouter

Registers and stores the router service for the current runtime.

```php
public registerRouter(): void
```

Existing DI router services are reused. Otherwise the built-in router
provider is registered, then the service is resolved through `getTyped()`
so invalid replacements fail with a clear service-contract error.

***

### bootServices

Resolves early services that need to be initialized before modules run.

```php
public bootServices(): void
```

At the moment this eagerly initializes the `debug` service and attaches
any configured shared event-manager listeners. The
`ServiceProviderInterface::boot()` hook remains available to provider
implementations, but the default bootstrap does not iterate provider
instances after registration.

***

### attachConfiguredEventListeners

Attach listeners declared under `eventsManager.listeners`.

```php
protected attachConfiguredEventListeners(): void
```

This hook runs after providers are registered and before modules/router
setup. That timing lets application config add listeners for shared event
types such as `dispatch`, `db`, `model`, or `view` without replacing the
core providers that create those services.

**Throws:**

When listener config exists but no
`eventsManager` service is registered.
- [`ConfigurationException`](./Exception/ConfigurationException.md)
When a configured listener definition is
invalid.
- [`ConfigurationException`](./Exception/ConfigurationException.md)

***

### registerModules

Registers configured modules on the selected application object.

```php
public registerModules(\Phalcon\Application\AbstractApplication|null $application = null, array<string,array<string,mixed>>|null $modules = null, string|null $defaultModule = null): void
```

When no application is provided, the method resolves the mode-specific
console, WebSocket, or MVC application service from DI. Module definitions
default to `config.modules`, and the default module defaults to
`config.router.defaults.module`.

**Parameters:**

| Parameter        | Type                                               | Description                                                                             |
|------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------|
| `$application`   | **\Phalcon\Application\AbstractApplication\|null** | Application instance to
mutate, or `null` to resolve the mode-specific service from DI. |
| `$modules`       | **array<string,array<string,mixed>>\|null**        | Module
definitions, or `null` to use config.                                            |
| `$defaultModule` | **string\|null**                                   | Default module name, or `null` to use
config.                                           |

**Throws:**

When the bootstrap mode cannot be mapped
to an application service.
- [`ConfigurationException`](./Exception/ConfigurationException.md)

***

### run

Dispatches the selected runtime and returns the produced content.

```php
public run(): ?string
```

The `beforeRun` event is fired before dispatch and `afterRun` is fired
with the produced content afterward. MVC mode returns response content,
CLI mode returns captured command output, and WebSocket mode returns
`null` after handing control to the server runtime.

**Throws:**

When the bootstrap mode cannot be handled.
- [`ConfigurationException`](./Exception/ConfigurationException.md)

***

### resetConnectionState

Clear request-scoped model connection state before dispatch.

```php
public resetConnectionState(): void
```

Native Phalcon sticky read/write tracking belongs to one logical request.
Traditional PHP runtimes build a new container per request, while
RoadRunner-style runtimes may reuse the bootstrap and its shared model
manager. This reset prevents a write in one request from pinning an
unrelated later request to the write connection.

Swoole WebSocket handlers should also reset at the start of every logical
message or HTTP request; PhalconKit's base WebSocket task does this for
the built-in callbacks.

***

### handleConsole

Handles a CLI console request and returns captured output.

```php
public handleConsole(\PhalconKit\Cli\Console $console): ?string
```

Console exceptions are rendered through the CLI exception handler so CLI
users receive formatted output instead of raw PHP exception text.

**Parameters:**

| Parameter  | Type                        | Description |
|------------|-----------------------------|-------------|
| `$console` | **\PhalconKit\Cli\Console** |             |

***

### handleWebSocket

Handles a WebSocket/Swoole server request.

```php
public handleWebSocket(\PhalconKit\Ws\WebSocket $webSocket): ?string
```

WebSocket handling is long-running and does not produce an HTTP response
body for bootstrap callers, so this method always returns `null`.

**Parameters:**

| Parameter    | Type                         | Description |
|--------------|------------------------------|-------------|
| `$webSocket` | **\PhalconKit\Ws\WebSocket** |             |

***

### handleApplication

Handles an MVC HTTP request and stores the resulting response.

```php
public handleApplication(\PhalconKit\Mvc\Application $application): ?string
```

The request URI is read from `$_SERVER['REQUEST_URI']`, defaulting to `/`
when unavailable. The returned string is the response body content, or
`null` if the application did not return a response object.

**Parameters:**

| Parameter      | Type                            | Description |
|----------------|---------------------------------|-------------|
| `$application` | **\PhalconKit\Mvc\Application** |             |

**Throws:**

Propagates failures from Phalcon MVC request handling
unchanged so the application's configured error pipeline can decide
how to render or log them.
- [`Throwable`](https://www.php.net/manual/en/class.throwable.php){:target="_blank"}

***

### getArgs

Parses CLI arguments into PhalconKit's camelCase argument format.

```php
public getArgs(): array<string,mixed>
```

The parser uses `cliDoc` as its Docopt specification and reads the
current process arguments from `$_SERVER['argv']`. Non-CLI runtimes return
an empty array so shared code can call this method safely.

***

### isCli

Returns true when this bootstrap is running in CLI mode.

```php
public isCli(): bool
```

***

### isWs

Returns true when this bootstrap is running in WebSocket mode.

```php
public isWs(): bool
```

***

### isMvc

Returns true when this bootstrap is running in MVC mode.

```php
public isMvc(): bool
```

***

## Inherited methods

### setEventsManager

Set the events manager

```php
public setEventsManager(\Phalcon\Contracts\Events\Manager $manager): void
```

**Parameters:**

| Parameter  | Type                                  | Description |
|------------|---------------------------------------|-------------|
| `$manager` | **\Phalcon\Contracts\Events\Manager** |             |

***

### getEventsManager

Get the events manager.

```php
public getEventsManager(): ?\Phalcon\Contracts\Events\Manager
```

***

### getEventsPrefix

Get the event component prefix

```php
public static getEventsPrefix(): string|null
```

* This method is **static**.
**Return Value:**

The event component prefix, or null if not set

***

### setEventsPrefix

Sets the events prefix.

```php
public static setEventsPrefix(string|null $eventsPrefix): void
```

* This method is **static**.
**Parameters:**

| Parameter       | Type             | Description                                                       |
|-----------------|------------------|-------------------------------------------------------------------|
| `$eventsPrefix` | **string\|null** | The prefix to be used for events. Pass null to remove the prefix. |

***

### fire

Fire an event.

```php
public fire(string $task, mixed|null $data = null, bool $cancelable = false): mixed
```

**Parameters:**

| Parameter     | Type            | Description                                                |
|---------------|-----------------|------------------------------------------------------------|
| `$task`       | **string**      | The task to execute.                                       |
| `$data`       | **mixed\|null** | The optional data to pass to the event.                    |
| `$cancelable` | **bool**        | Whether the event is cancelable or not. Defaults to false. |

***
