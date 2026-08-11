
WebSocket module definition backed by Phalcon's CLI-style dispatcher.

WebSocket tasks are routed like CLI tasks but run under the WebSocket/Swoole
runtime. The module registers task/model namespaces and configures dispatcher
and router defaults for the long-running `listen` action.

***

* Full name: `\PhalconKit\Modules\Ws\Module`
* Parent class: [`\PhalconKit\Ws\Module`](../../Ws/Module.md)

## Properties

### name

```php
public string $name
```

***

## Inherited methods

### registerAutoloaders

Register task/model namespaces for the WebSocket module.

```php
public registerAutoloaders(?\Phalcon\Di\DiInterface $container = null): void
```

When a loader service is registered, it must be a Phalcon autoloader.
Otherwise the module creates a local loader for task and model
namespaces.

**Parameters:**

| Parameter    | Type                         | Description |
|--------------|------------------------------|-------------|
| `$container` | **?\Phalcon\Di\DiInterface** |             |

***

### registerServices

Resolve and configure dispatcher/router services for WebSocket tasks.

```php
public registerServices(\Phalcon\Di\DiInterface $container): void
```

Registered replacements for `dispatcher` and `router` are resolved
through the shared service resolver so invalid module wiring fails before
the module mutates service state.

**Parameters:**

| Parameter    | Type                        | Description |
|--------------|-----------------------------|-------------|
| `$container` | **\Phalcon\Di\DiInterface** |             |

***

### getNamespaces

Return namespace-to-directory mappings registered by the module loader.

```php
public getNamespaces(): array<string,string>
```

***

### getServices

Resolve module-owned services from DI or create local defaults.

```php
public getServices(\Phalcon\Di\DiInterface|null $container = null): void
```

**Parameters:**

| Parameter    | Type                              | Description                                                |
|--------------|-----------------------------------|------------------------------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface\|null** | Optional DI container used by Phalcon
module registration. |

***

### setServices

Store resolved module services back into the active DI container.

```php
public setServices(\Phalcon\Di\DiInterface $container): void
```

**Parameters:**

| Parameter    | Type                        | Description |
|--------------|-----------------------------|-------------|
| `$container` | **\Phalcon\Di\DiInterface** |             |

***

### getDefaultNamespace

Return the default task namespace for dispatcher routing.

```php
public getDefaultNamespace(): string
```

***

### getDirname

Return the filesystem directory that contains this module class.

```php
public getDirname(): string
```

***

### getNamespace

Return the PHP namespace for this module class.

```php
public getNamespace(): string
```

***
