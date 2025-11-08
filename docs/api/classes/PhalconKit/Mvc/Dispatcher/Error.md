
***

* Full name: `\PhalconKit\Mvc\Dispatcher\Error`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Properties

### defaultNotFoundRoute

```php
public array $defaultNotFoundRoute
```

***

### defaultErrorRoute

```php
public array $defaultErrorRoute
```

***

## Methods

### beforeException

Forward to 404 or 500 error controller

```php
public beforeException(\Phalcon\Events\Event $event, \PhalconKit\Mvc\Dispatcher $dispatcher, \Exception $exception): bool
```

**Parameters:**

| Parameter     | Type                           | Description |
|---------------|--------------------------------|-------------|
| `$event`      | **\Phalcon\Events\Event**      |             |
| `$dispatcher` | **\PhalconKit\Mvc\Dispatcher** |             |
| `$exception`  | **\Exception**                 |             |

**Throws:**

- [`Exception`](../../../Exception.md)

***

### appendDefaultToRoute

```php
public appendDefaultToRoute(array $route, array $default): array
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$route`   | **array** |             |
| `$default` | **array** |             |

***
