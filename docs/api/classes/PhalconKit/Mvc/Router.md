
Framework router with config-backed module and locale route registration.

The router reads defaults, not-found targets, hostnames, and locales from the
PhalconKit config service. It remains compatible with Phalcon's router API
while exposing a small `toArray()` diagnostic snapshot through
`RouterInterface`.

***

* Full name: `\PhalconKit\Mvc\Router`
* Parent class: [`Router`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  `RouterInterface`,
  [`\PhalconKit\Router\RouterInterface`](../Router/RouterInterface.md)

**See Also:**

* https://docs.phalcon.io/latest/routing/

## Properties

### config

Config service used to build default, hostname, module, and locale routes.

```php
public \PhalconKit\Config\ConfigInterface $config
```

***

## Methods

### getConfig

Return the config service attached to the router.

```php
public getConfig(): \PhalconKit\Config\ConfigInterface
```

***

### setConfig

Attach the config service used by route registration helpers.

```php
public setConfig(\PhalconKit\Config\ConfigInterface $config): void
```

**Parameters:**

| Parameter | Type                                   | Description |
|-----------|----------------------------------------|-------------|
| `$config` | **\PhalconKit\Config\ConfigInterface** |             |

***

### __construct

Create a config-aware router.

```php
public __construct(bool $defaultRoutes = true, \PhalconKit\Config\ConfigInterface|null $config = null): mixed
```

Native Phalcon default routes are disabled so PhalconKit can register its
own module-aware routes. When `$defaultRoutes` is true, route defaults are
read immediately from config.

**Parameters:**

| Parameter        | Type                                         | Description                                                                    |
|------------------|----------------------------------------------|--------------------------------------------------------------------------------|
| `$defaultRoutes` | **bool**                                     | Whether PhalconKit default routes should be
registered during construction.    |
| `$config`        | **\PhalconKit\Config\ConfigInterface\|null** | Optional config service. When omitted
the default DI `config` service is used. |

***

### defaultRoutes

Register the default module route group from config.

```php
public defaultRoutes(): void
```

The method applies configured defaults, configured not-found paths, extra
slash handling, and locale-aware module routes.

***

### hostnamesRoutes

Register hostname-specific module route groups.

```php
public hostnamesRoutes(array<string,array<string,mixed>>|null $hostnames = null, array<string,mixed>|null $defaults = null): void
```

Each hostname entry must declare a string `module`; the remaining values
are merged into the route defaults for that hostname.

**Parameters:**

| Parameter    | Type                                        | Description                                            |
|--------------|---------------------------------------------|--------------------------------------------------------|
| `$hostnames` | **array<string,array<string,mixed>>\|null** | Hostname route
config. Defaults to `router.hostnames`. |
| `$defaults`  | **array<string,mixed>\|null**               | Base route defaults.                                   |

**Throws:**

When a hostname entry does not declare a
string module name.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### modulesRoutes

Register route groups for modules known by the MVC application.

```php
public modulesRoutes(\Phalcon\Mvc\Application $application, array<string,mixed>|null $defaults = null): void
```

The module namespace is inferred from the module class name, matching the
framework module structure. Applications with custom namespaces can mount
their own `ModuleRoute` instances when this convention is not appropriate.

**Parameters:**

| Parameter      | Type                          | Description                                               |
|----------------|-------------------------------|-----------------------------------------------------------|
| `$application` | **\Phalcon\Mvc\Application**  | Application containing the
registered module definitions. |
| `$defaults`    | **array<string,mixed>\|null** | Base route defaults.                                      |

**Throws:**

When a module definition is missing
`className`.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### toArray

Export the current router match state for diagnostics.

```php
public toArray(): array<string,mixed>
```

**Return Value:**

Current namespace, module, controller,
action, params, defaults, matches, and matched-route metadata.

***
