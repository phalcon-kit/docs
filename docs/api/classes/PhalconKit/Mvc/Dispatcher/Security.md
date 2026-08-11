
Dispatcher listener that enforces configured ACL permissions.

The listener compares the active controller/task class and action against
PhalconKit ACL components. When permissions are not configured it allows the
request, preserving the framework's permissive default for applications that
have not opted into ACL configuration.

***

* Full name: `\PhalconKit\Mvc\Dispatcher\Security`
* Parent class: [`\PhalconKit\Di\Injectable`](../../Di/Injectable.md)

## Methods

### beforeDispatchLoop

Check ACL permissions before Phalcon enters the dispatch loop.

```php
public beforeDispatchLoop(\Phalcon\Events\Event $event, \Phalcon\Dispatcher\AbstractDispatcher $dispatcher): bool
```

**Parameters:**

| Parameter     | Type                                       | Description                        |
|---------------|--------------------------------------------|------------------------------------|
| `$event`      | **\Phalcon\Events\Event**                  | Dispatch event emitted by Phalcon. |
| `$dispatcher` | **\Phalcon\Dispatcher\AbstractDispatcher** | Active MVC or CLI dispatcher.      |

**Return Value:**

True when dispatch can continue, false after forwarding.

**Throws:**

When dispatcher state cannot be inspected.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### checkAcl

Determine whether the current identity may execute the active handler.

```php
public checkAcl(\Phalcon\Events\Event $event, \Phalcon\Dispatcher\AbstractDispatcher|null $dispatcher = null): bool
```

Unauthorized users with more than one ACL role are forwarded to
`router.unauthorized`; users with only one role are forwarded to
`router.forbidden`. Missing ACL components forward to `router.notFound`.

**Parameters:**

| Parameter     | Type                                             | Description                                                                   |
|---------------|--------------------------------------------------|-------------------------------------------------------------------------------|
| `$event`      | **\Phalcon\Events\Event**                        | Dispatch event emitted by Phalcon.                                            |
| `$dispatcher` | **\Phalcon\Dispatcher\AbstractDispatcher\|null** | Dispatcher to inspect. When
omitted, the injected dispatcher service is used. |

**Return Value:**

True when dispatch can continue, false after forwarding.

**Throws:**

When dispatcher state cannot be inspected.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### isCurrentRoute

Detect dispatcher cycles for full or partial configured routes.

```php
private isCurrentRoute(array $route, ?string $namespace, ?string $module, string $handlerRouteKey, ?string $handler, string $action): bool
```

**Parameters:**

| Parameter          | Type        | Description |
|--------------------|-------------|-------------|
| `$route`           | **array**   |             |
| `$namespace`       | **?string** |             |
| `$module`          | **?string** |             |
| `$handlerRouteKey` | **string**  |             |
| `$handler`         | **?string** |             |
| `$action`          | **string**  |             |

***

### resolveAclComponent

Resolve the configured ACL component for the current dispatcher handler.

```php
private resolveAclComponent(\Phalcon\Acl\Adapter\Memory $acl, array<int,string> $candidates): ?string
```

**Parameters:**

| Parameter     | Type                            | Description                      |
|---------------|---------------------------------|----------------------------------|
| `$acl`        | **\Phalcon\Acl\Adapter\Memory** | Native ACL instance.             |
| `$candidates` | **array<int,string>**           | Handler class and route aliases. |

***

### usesControllerAttributes

Determine whether controller attributes should augment permission config.

```php
private usesControllerAttributes(): bool
```

***
