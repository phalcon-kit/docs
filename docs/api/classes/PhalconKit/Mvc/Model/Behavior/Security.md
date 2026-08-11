
Enforces ACL permissions for model lifecycle operations.

The behavior checks configured model ACL components before write, restore,
reorder, and finder/count operations. It resolves the shared ACL and
identity services lazily from the default PhalconKit DI because native
Phalcon model behaviors are instantiated and notified by Phalcon internals,
not by constructor injection.

Consumers can override the cached ACL adapter or role list with `setAcl()`
and `setRoles()` for tests, CLI workflows, or specialized authorization
flows. Passing null clears the cache and makes the next lookup resolve from
the default DI again.

***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Security`
* Parent class: [`Behavior`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Properties

### roles

Cached ACL role names used by permission checks.

```php
public static array<int|string,string|\Stringable>|null $roles
```

The cache avoids resolving the identity service for every model event.
Set it to null through `setRoles()` when impersonation or login state
changes during the same process.

* This property is **static**.

***

### acl

Cached ACL adapter containing model and component permissions.

```php
public static ?\Phalcon\Contracts\Acl\Adapter\Adapter $acl
```

This is intentionally the native ACL adapter returned by the PhalconKit
ACL service, not the service wrapper itself.

* This property is **static**.

***

## Methods

### setAcl

Replace or clear the cached ACL adapter used by model permission checks.

```php
public static setAcl(\Phalcon\Contracts\Acl\Adapter\Adapter|null $acl = null): void
```

Use this in tests or long-running processes when the permission matrix
changes after the behavior has already resolved it. Passing null clears
the cache so `getAcl()` will resolve a fresh adapter from the default DI.

* This method is **static**.
**Parameters:**

| Parameter | Type                                             | Description                                                                                 |
|-----------|--------------------------------------------------|---------------------------------------------------------------------------------------------|
| `$acl`    | **\Phalcon\Contracts\Acl\Adapter\Adapter\|null** | Native ACL adapter to cache, or null to
force lazy resolution on the next permission check. |

***

### getAcl

Resolve the ACL adapter containing model and component permissions.

```php
public static getAcl(): \Phalcon\Contracts\Acl\Adapter\Adapter
```

The default `acl` service must implement `PhalconKit\Acl\AclInterface`.
Its `get()` method is called with the `models` and `components` sections
so model-level checks share the same permission graph as dispatcher
checks.

* This method is **static**.
**Return Value:**

Native ACL adapter used for permission checks.

**Throws:**

When the default DI or ACL service cannot be
resolved through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### setRoles

Replace or clear the cached role list used by model permission checks.

```php
public static setRoles(array<int|string,string|\Stringable>|null $roles = null): void
```

Passing null clears the cache so `getRoles()` will resolve the current
identity service and rebuild the role list. This matters for tests,
impersonation, and long-running worker processes where identity state can
change without restarting PHP.

* This method is **static**.
**Parameters:**

| Parameter | Type                                             | Description                                                                                   |
|-----------|--------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `$roles`  | **array<int\|string,string\|\Stringable>\|null** | Role names or
ACL role objects to check, or null to force lazy identity resolution
next time. |

***

### getRoles

Resolve ACL role names for the current identity.

```php
public static getRoles(): array<int|string,string|\Stringable>
```

Role names are cached after the first lookup. Clear them with
`setRoles(null)` when identity state changes inside the same request or
worker process.

* This method is **static**.
**Return Value:**

Roles used against the ACL
adapter.

**Throws:**

When the default DI or identity service cannot
be resolved through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### notify

Handle Phalcon model events and stop unauthorized operations.

```php
public notify(string $type, \Phalcon\Mvc\ModelInterface $model): bool|null
```

Only `before*` finder, aggregate, write, restore, and reorder events are
checked. The behavior returns null when disabled or when it is already
resolving permissions, which prevents recursive checks while the identity
service loads role data from models.

**Parameters:**

| Parameter | Type                            | Description                                                                  |
|-----------|---------------------------------|------------------------------------------------------------------------------|
| `$type`   | **string**                      | Phalcon event name such as `beforeCreate`,
`beforeFind`, or `beforeReorder`. |
| `$model`  | **\Phalcon\Mvc\ModelInterface** | Model instance being checked.                                                |

**Return Value:**

True when the event is allowed, false when the model
receives a permission error message, or null when the event is not
handled by this behavior.

**Throws:**

When ACL or identity services cannot be resolved
for a handled event.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

### isAllowed

Check whether roles may execute an operation on a model class.

```php
public isAllowed(string $type, \Phalcon\Mvc\ModelInterface $model, \Phalcon\Contracts\Acl\Adapter\Adapter|null $acl = null, array<int|string,string|\Stringable>|null $roles = null): bool
```

If no ACL adapter or role list is provided, the method falls back to the
cached/default ACL and identity services. Denials are reported on the
model as Phalcon messages so callers following normal model validation
flows can inspect the failure reason.

**Parameters:**

| Parameter | Type                                             | Description                                                                                       |
|-----------|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `$type`   | **string**                                       | Normalized operation name, such as `create`,
`update`, `delete`, `restore`, `find`, or `count`.   |
| `$model`  | **\Phalcon\Mvc\ModelInterface**                  | Model instance being authorized.                                                                  |
| `$acl`    | **\Phalcon\Contracts\Acl\Adapter\Adapter\|null** | Optional adapter override, useful for
tests or callers that already resolved a scoped ACL.        |
| `$roles`  | **array<int\|string,string\|\Stringable>\|null** | Optional role
names or ACL role objects to check instead of resolving the current
identity roles. |

**Return Value:**

True when any role is allowed; false when the model class is
not registered in the ACL or all roles are denied.

**Throws:**

When ACL or identity services must be resolved
but are unavailable or incompatible.
- [`ServiceException`](../../../Exception/ServiceException.md)

***

## Inherited methods

### getProgress

Return true if the behavior is progress
on the current model instance

```php
public getProgress(): bool
```

***

### setProgress

Set true to enable the behavior
on the current model instance

```php
public setProgress(bool $progress): void
```

**Parameters:**

| Parameter   | Type     | Description |
|-------------|----------|-------------|
| `$progress` | **bool** |             |

***

### getStaticProgress

Return true if the behavior is progress
globally for every model instance

```php
public static getStaticProgress(): bool
```

* This method is **static**.
***

### setStaticProgress

Set true to enable the behavior
globally for every model instance

```php
public static setStaticProgress(bool $staticProgress): void
```

* This method is **static**.
**Parameters:**

| Parameter         | Type     | Description |
|-------------------|----------|-------------|
| `$staticProgress` | **bool** |             |

***

### start

Enable the behavior
on the current model instance

```php
public start(): void
```

***

### stop

Disable the behavior
on the current model instance

```php
public stop(): void
```

***

### staticStart

Enable the behavior
globally for every model instance

```php
public static staticStart(): void
```

* This method is **static**.
***

### staticStop

Disable the behavior
globally for every model instance

```php
public static staticStop(): void
```

* This method is **static**.
***

### inProgress

Return true if the behavior is in progress
on the current model instance and globally

```php
public inProgress(): bool
```

***

### isStarted

Return true if the behavior is started
on the current model instance and globally

```php
public isStarted(): bool
```

***

### isStopped

Return true if the behavior is stopped
on the current model instance and globally

```php
public isStopped(): bool
```

***

### getEnabled

Return true if the behavior is enabled
on the current model instance

```php
public getEnabled(): bool
```

***

### setEnabled

Set true to enable the behavior
on the current model instance

```php
public setEnabled(bool $enabled): void
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$enabled` | **bool** |             |

***

### getStaticEnabled

Return true if the behavior is enabled
globally for every model instance

```php
public static getStaticEnabled(): bool
```

* This method is **static**.
***

### setStaticEnabled

Set true to enable the behavior
globally for every model instance

```php
public static setStaticEnabled(bool $staticEnabled): void
```

* This method is **static**.
**Parameters:**

| Parameter        | Type     | Description |
|------------------|----------|-------------|
| `$staticEnabled` | **bool** |             |

***

### enable

Enable the behavior
on the current model instance

```php
public enable(): void
```

***

### disable

Disable the behavior
on the current model instance

```php
public disable(): void
```

***

### staticEnable

Enable the behavior
globally for every model instance

```php
public static staticEnable(): void
```

* This method is **static**.
***

### staticDisable

Disable the behavior
globally for every model instance

```php
public static staticDisable(): void
```

* This method is **static**.
***

### isEnabled

Return true if the behavior is enabled
on the current model instance and globally

```php
public isEnabled(): bool
```

***

### isDisabled

Return true if the behavior is enabled
on the current model instance and globally

```php
public isDisabled(): bool
```

***
