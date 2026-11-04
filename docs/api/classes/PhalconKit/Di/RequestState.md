
Clears request-scoped framework state before a new logical request.

`Bootstrap::run()` and the base WebSocket task call this before every
request or callback. It resets:

- every already-instantiated shared service implementing
  `RequestScopedInterface` (for example the identity manager's cached
  claim, user, and impersonating user);
- the model security behavior's cached ACL roles;
- the Blameable behavior's parent-audit link.

Instances are found in two places: shared services the container has
built, and any service (shared or not) cached by `Di::getShared()`, which
is also how `Injectable` magic properties such as `$this->identity` resolve
services. Each instance is reset once. Services that were never
instantiated are left untouched, so the reset does not build services a
request does not use. The cached ACL permission matrix
(`Security::setAcl()`) is configuration, not identity, and is kept.

***

* Full name: `\PhalconKit\Di\RequestState`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Properties

### sharedInstances

```php
private static ?\ReflectionProperty $sharedInstances
```

* This property is **static**.

***

## Methods

### reset

Reset request-scoped state held by shared services and model behaviors.

```php
public static reset(\Phalcon\Di\DiInterface $di): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type                        | Description                                    |
|-----------|-----------------------------|------------------------------------------------|
| `$di`     | **\Phalcon\Di\DiInterface** | Container whose shared services are inspected. |

***

### getBuiltInstances

Yield the service instances the container has already built.

```php
private static getBuiltInstances(\Phalcon\Di\DiInterface $di): \Generator<int,mixed>
```

Covers shared services resolved through `get()` or registered as
instances, plus every instance cached by `Di::getShared()`, including
non-shared services fetched that way. The latter cache has no public
accessor, so it is read through reflection on `Phalcon\Di\Di`; other
`DiInterface` implementations only contribute their shared services.

* This method is **static**.
**Parameters:**

| Parameter | Type                        | Description |
|-----------|-----------------------------|-------------|
| `$di`     | **\Phalcon\Di\DiInterface** |             |

***
