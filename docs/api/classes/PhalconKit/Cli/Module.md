
Default CLI module definition.

The module wires CLI task namespaces, dispatcher defaults, router defaults,
and core model namespaces for the built-in command runtime. Applications can
subclass or replace this module when they need different task namespaces or
service defaults, but should keep the same dispatcher/router contracts.

***

* Full name: `\PhalconKit\Cli\Module`
* This class implements:
  `ModuleDefinitionInterface`

## Constants

| Constant   | Visibility | Type   | Value |
|------------|------------|--------|-------|
| `NAME_CLI` | public     | string | 'cli' |

## Properties

### name

Module name written into router defaults.

```php
public string $name
```

***

### config

Config service resolved or created by the module.

```php
public ?\PhalconKit\Bootstrap\Config $config
```

***

### dispatcher

CLI dispatcher resolved or created by the module.

```php
public ?\PhalconKit\Cli\Dispatcher $dispatcher
```

***

### loader

Autoloader used to register task/model namespaces.

```php
public ?\Phalcon\Autoload\Loader $loader
```

***

### router

CLI router resolved or created by the module.

```php
public ?\PhalconKit\Cli\Router $router
```

***

## Methods

### registerAutoloaders

Register task/model namespaces for the CLI module.

```php
public registerAutoloaders(\Phalcon\Di\DiInterface|null $container = null): void
```

When a loader service is registered, it must be a Phalcon autoloader.
Otherwise the module creates a local loader so lightweight CLI modules do
not need to pre-register one.

**Parameters:**

| Parameter    | Type                              | Description                                                        |
|--------------|-----------------------------------|--------------------------------------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface\|null** | Optional container supplied by
Phalcon's module registration flow. |

**Throws:**

When the registered loader is not compatible.
- [`ServiceException`](../Exception/ServiceException.md)

***

### registerServices

Resolve and configure dispatcher/router services for CLI execution.

```php
public registerServices(\Phalcon\Di\DiInterface $container): void
```

Registered replacements for `dispatcher` and `router` are resolved
through the shared service resolver so invalid module wiring fails before
the module mutates service state.

**Parameters:**

| Parameter    | Type                        | Description                                         |
|--------------|-----------------------------|-----------------------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface** | Container receiving the configured module
services. |

**Throws:**

When resolved module services are incompatible.
- [`ServiceException`](../Exception/ServiceException.md)

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

**Throws:**

When a registered replacement service has the
wrong type or cannot be resolved.
- [`ServiceException`](../Exception/ServiceException.md)

***

### setServices

Store resolved module services back into the active DI container.

```php
public setServices(\Phalcon\Di\DiInterface $container): void
```

**Parameters:**

| Parameter    | Type                        | Description                                                                                 |
|--------------|-----------------------------|---------------------------------------------------------------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface** | Container that should receive the resolved
config, dispatcher, loader, and router services. |

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
