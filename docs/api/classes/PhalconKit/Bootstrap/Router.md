
Phalcon Kit Router
{@inheritDoc}

***

* Full name: `\PhalconKit\Bootstrap\Router`
* Parent class: [`\PhalconKit\Mvc\Router`](../Mvc/Router.md)

## Properties

### defaults

```php
public array $defaults
```

***

### notFound

```php
public array $notFound
```

***

## Methods

### __construct

Router constructor.

```php
public __construct(bool $defaultRoutes = true, ?\PhalconKit\Config\ConfigInterface $config = null): mixed
```

**Parameters:**

| Parameter        | Type                                    | Description |
|------------------|-----------------------------------------|-------------|
| `$defaultRoutes` | **bool**                                |             |
| `$config`        | **?\PhalconKit\Config\ConfigInterface** |             |

***

### baseRoutes

```php
public baseRoutes(): void
```

***

## Inherited methods

### getConfig

```php
public getConfig(): \PhalconKit\Config\ConfigInterface
```

***

### setConfig

```php
public setConfig(\PhalconKit\Config\ConfigInterface $config): void
```

**Parameters:**

| Parameter | Type                                   | Description |
|-----------|----------------------------------------|-------------|
| `$config` | **\PhalconKit\Config\ConfigInterface** |             |

***

### __construct

Router constructor.

```php
public __construct(bool $defaultRoutes = true, ?\PhalconKit\Config\ConfigInterface $config = null): mixed
```

**Parameters:**

| Parameter        | Type                                    | Description |
|------------------|-----------------------------------------|-------------|
| `$defaultRoutes` | **bool**                                |             |
| `$config`        | **?\PhalconKit\Config\ConfigInterface** |             |

***

### defaultRoutes

Default routes
- Default namespace
- Default controller
- Default action
- Default notFound

```php
public defaultRoutes(): void
```

***

### hostnamesRoutes

```php
public hostnamesRoutes(array|null $hostnames = null, array|null $defaults = null): void
```

**Parameters:**

| Parameter    | Type            | Description |
|--------------|-----------------|-------------|
| `$hostnames` | **array\|null** |             |
| `$defaults`  | **array\|null** |             |

***

### modulesRoutes

Defines our frontend routes
/controller/action/params

```php
public modulesRoutes(\Phalcon\Mvc\Application $application, ?array $defaults = null): void
```

**Parameters:**

| Parameter      | Type                         | Description |
|----------------|------------------------------|-------------|
| `$application` | **\Phalcon\Mvc\Application** |             |
| `$defaults`    | **?array**                   |             |

***

### toArray

```php
public toArray(): array
```

***
