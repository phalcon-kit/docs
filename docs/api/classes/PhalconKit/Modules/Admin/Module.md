
Base MVC module definition used by PhalconKit web modules.

The module wires controller/model/transformer namespaces and configures the
dispatcher, router, view, and URL services for one module. Concrete modules
only need to provide the public `$name` value unless they need custom
namespaces or service registration behavior.

***

* Full name: `\PhalconKit\Modules\Admin\Module`
* Parent class: [`\PhalconKit\Mvc\Module`](../../Mvc/Module.md)

## Properties

### name

```php
public string $name
```

***

## Inherited methods

### registerAutoloaders

Register controller/model/transformer namespaces for the MVC module.

```php
public registerAutoloaders(?\Phalcon\Di\DiInterface $container = null): void
```

When the container defines a loader service, it must be compatible with
Phalcon's autoloader. Otherwise the module creates a local loader for the
module namespace registration.

**Parameters:**

| Parameter    | Type                         | Description |
|--------------|------------------------------|-------------|
| `$container` | **?\Phalcon\Di\DiInterface** |             |

***

### registerServices

Resolve and configure dispatcher, router, view, and URL services.

```php
public registerServices(\Phalcon\Di\DiInterface $container): void
```

Registered replacements for module services are resolved through the
shared service resolver so invalid DI wiring fails before dispatcher,
router, view, or URL state is mutated.

**Parameters:**

| Parameter    | Type                        | Description |
|--------------|-----------------------------|-------------|
| `$container` | **\Phalcon\Di\DiInterface** |             |

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

### getNamespaces

Return namespace-to-directory mappings registered by the module loader.

```php
public getNamespaces(): array<string,string>
```

***

### getDefaultNamespace

Return the default controller namespace for dispatcher routing.

```php
public getDefaultNamespace(): string
```

***

### getViewsDir

Return the view directory list for this module.

```php
public getViewsDir(): array<int,string>
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
