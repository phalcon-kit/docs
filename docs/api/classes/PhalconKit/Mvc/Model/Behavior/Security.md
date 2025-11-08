
The Security class provides methods for access control and permission checking.

This behavior will stop operations if the user is not allowed to run a certain type of action for the model

***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Security`
* Parent class: [`Behavior`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Properties

### roles

```php
public static ?array $roles
```

* This property is **static**.

***

### acl

```php
public static ?\Phalcon\Acl\Adapter\AdapterInterface $acl
```

* This property is **static**.

***

## Methods

### setAcl

Set the Access Control List (ACL) adapter.

```php
public static setAcl(\Phalcon\Acl\Adapter\AdapterInterface|null $acl = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type                                            | Description                               |
|-----------|-------------------------------------------------|-------------------------------------------|
| `$acl`    | **\Phalcon\Acl\Adapter\AdapterInterface\|null** | The ACL adapter to set. Defaults to null. |

***

### getAcl

Get the Access Control List (ACL) with models and components elements

```php
public static getAcl(): \Phalcon\Acl\Adapter\AdapterInterface
```

* This method is **static**.
**Return Value:**

The ACL adapter instance

***

### setRoles

Set the roles

```php
public static setRoles(array|null $roles = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type            | Description                         |
|-----------|-----------------|-------------------------------------|
| `$roles`  | **array\|null** | The roles to set. Defaults to null. |

***

### getRoles

Get the roles of the current user

```php
public static getRoles(): array
```

This method retrieves the roles of the current user from the identity object. If the roles have not been
retrieved before, it retrieves them using the 'getAclRoles' method of the identity object. If the roles
have already been retrieved, it returns the cached roles. If the identity object is not found in the
DI container, an exception will be thrown.

* This method is **static**.
**Return Value:**

The roles of the current user

***

### notify

```php
public notify(string $type, \Phalcon\Mvc\ModelInterface $model): bool|null
```

**Parameters:**

| Parameter | Type                            | Description                                                                                                                                                                                                                   |
|-----------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$type`   | **string**                      | The type of event to notify. Should be one of the following:
'beforeFind', 'beforeFindFirst', 'beforeCount', 'beforeSum', 'beforeAverage', 'beforeCreate', 
'beforeUpdate', 'beforeDelete', 'beforeRestore', 'beforeReorder'. |
| `$model`  | **\Phalcon\Mvc\ModelInterface** | The model associated with the event.                                                                                                                                                                                          |

**Return Value:**

Returns true if the event is allowed, false otherwise.
Returns null if the notification is disabled or if the check is skipped while in progress.

***

### isAllowed

Check if a specified type of operation is allowed on a model

```php
public isAllowed(string $type, \Phalcon\Mvc\ModelInterface $model, \Phalcon\Acl\Adapter\AdapterInterface|null $acl = null, array|null $roles = null): bool
```

**Parameters:**

| Parameter | Type                                            | Description                                                                                                 |
|-----------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `$type`   | **string**                                      | The type of operation to check                                                                              |
| `$model`  | **\Phalcon\Mvc\ModelInterface**                 | The model to check permissions on                                                                           |
| `$acl`    | **\Phalcon\Acl\Adapter\AdapterInterface\|null** | The ACL adapter to use for permission checks (optional, will default to the configured ACL if not provided) |
| `$roles`  | **array\|null**                                 | The roles to check for permission (optional, will use the configured roles if not provided)                 |

**Return Value:**

Returns true if the operation is allowed, false otherwise

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
