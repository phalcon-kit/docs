
***

* Full name: `\PhalconKit\Mvc\Module`
* This class implements:
  `ModuleDefinitionInterface`
* This class is an **Abstract class**

## Constants

| Constant        | Visibility | Type | Value      |
|-----------------|------------|------|------------|
| `NAME_FRONTEND` | public     |      | 'frontend' |
| `NAME_ADMIN`    | public     |      | 'admin'    |
| `NAME_API`      | public     |      | 'api'      |
| `NAME_OAUTH2`   | public     |      | 'oauth2'   |

## Properties

### name

```php
public string $name
```

***

### config

```php
public ?\PhalconKit\Bootstrap\Config $config
```

***

### dispatcher

```php
public ?\PhalconKit\Mvc\Dispatcher $dispatcher
```

***

### loader

```php
public ?\Phalcon\Autoload\Loader $loader
```

***

### router

```php
public ?\PhalconKit\Mvc\Router $router
```

***

### view

```php
public ?\PhalconKit\Mvc\View $view
```

***

### url

```php
public ?\PhalconKit\Mvc\Url $url
```

***

## Methods

### registerAutoloaders

Registers an autoloader related to the frontend module

```php
public registerAutoloaders(?\Phalcon\Di\DiInterface $container = null): void
```

**Parameters:**

| Parameter    | Type                         | Description |
|--------------|------------------------------|-------------|
| `$container` | **?\Phalcon\Di\DiInterface** |             |

***

### registerServices

Registers services related to the module

```php
public registerServices(\Phalcon\Di\DiInterface $container): void
```

**Parameters:**

| Parameter    | Type                        | Description |
|--------------|-----------------------------|-------------|
| `$container` | **\Phalcon\Di\DiInterface** |             |

***

### getServices

```php
public getServices(?\Phalcon\Di\DiInterface $container = null): void
```

**Parameters:**

| Parameter    | Type                         | Description |
|--------------|------------------------------|-------------|
| `$container` | **?\Phalcon\Di\DiInterface** |             |

***

### setServices

```php
public setServices(\Phalcon\Di\DiInterface $container): void
```

**Parameters:**

| Parameter    | Type                        | Description |
|--------------|-----------------------------|-------------|
| `$container` | **\Phalcon\Di\DiInterface** |             |

***

### getNamespaces

```php
public getNamespaces(): array
```

***

### getDefaultNamespace

```php
public getDefaultNamespace(): string
```

***

### getViewsDir

```php
public getViewsDir(): array
```

***

### getDirname

```php
public getDirname(): string
```

***

### getNamespace

```php
public getNamespace(): string
```

***
