
Normalizes controller and action names used by ACL permissions.

Public routes often use dash-case while PHP actions use camelCase methods.
This helper gives permission config, attributes, dispatcher security, and
behavior attachment one shared vocabulary: component checks prefer the real
handler class and action checks canonicalize to dash-case while retaining raw
aliases for backwards compatibility.

***

* Full name: `\PhalconKit\Acl\PermissionName`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Methods

### action

Normalize a dispatcher or method action name into the ACL action key.

```php
public static action(string $action): string
```

Examples:

- `findWith` becomes `find-with`
- `find-with` remains `find-with`
- `findWithAction` becomes `find-with`

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description                                                         |
|-----------|------------|---------------------------------------------------------------------|
| `$action` | **string** | Action name from a route, dispatcher, method, or
permission config. |

**Return Value:**

Dash-case ACL action key, `*`, or an empty string.

***

### actionCandidates

Return action aliases to try for a dispatcher action.

```php
public static actionCandidates(string $action): array<int,string>
```

The canonical dash-case action is first so new config and attributes take
precedence. The raw action follows so older camelCase permission configs
remain valid during migration.

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description             |
|-----------|------------|-------------------------|
| `$action` | **string** | Dispatcher action name. |

**Return Value:**

Unique action candidates.

***

### accessList

Normalize a public action list for native Phalcon ACL registration.

```php
public static accessList(mixed $accessList): array<int,string>
```

Raw camelCase entries are preserved and dash-case aliases are added. This
keeps direct `Acl::isAllowed(..., 'findWith')` callers compatible while
allowing dispatcher security to check canonical dash-case actions.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                           |
|---------------|-----------|---------------------------------------|
| `$accessList` | **mixed** | String, array, or scalar access list. |

**Return Value:**

ACL access names.

***

### actionFromMethod

Derive a canonical action key from an action method name.

```php
public static actionFromMethod(string $methodName): string
```

* This method is **static**.
**Parameters:**

| Parameter     | Type       | Description                                  |
|---------------|------------|----------------------------------------------|
| `$methodName` | **string** | PHP method name, usually ending in `Action`. |

**Return Value:**

Dash-case ACL action key.

***

### handlerCandidates

Build component aliases for the active controller or task.

```php
public static handlerCandidates(string $handlerClass, string|null $routeName = null, string $suffix = 'Controller'): array<int,string>
```

The fully qualified handler class remains the preferred component key.
Short class names and route-style aliases are accepted so existing apps can
gradually move from route names such as `project-user` to class constants.

* This method is **static**.
**Parameters:**

| Parameter       | Type             | Description                                     |
|-----------------|------------------|-------------------------------------------------|
| `$handlerClass` | **string**       | Fully qualified dispatcher handler class.       |
| `$routeName`    | **string\|null** | Controller or task name from the dispatcher.    |
| `$suffix`       | **string**       | Handler suffix, usually `Controller` or `Task`. |

**Return Value:**

Unique component candidates.

***

### normalizeAttributeActions

Normalize a method/class attribute action list.

```php
public static normalizeAttributeActions(array<int,string>|null $actions, array<int,string> $defaultActions): array<int,string>
```

* This method is **static**.
**Parameters:**

| Parameter         | Type                        | Description                                                     |
|-------------------|-----------------------------|-----------------------------------------------------------------|
| `$actions`        | **array<int,string>\|null** | Explicit attribute actions.                                     |
| `$defaultActions` | **array<int,string>**       | Actions used when the attribute
omitted its `actions` argument. |

**Return Value:**

Canonical dash-case action keys.

***

### dash

Convert camelCase, PascalCase, snake_case, or spaced names to dash-case.

```php
private static dash(string $name): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$name`   | **string** |             |

***

### unique

```php
private static unique(array $values): array<int,string>
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$values` | **array** |             |

***

### shortClass

```php
private static shortClass(string $className): string
```

* This method is **static**.
**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$className` | **string** |             |

***

### withoutSuffix

```php
private static withoutSuffix(string $name, string $suffix): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$name`   | **string** |             |
| `$suffix` | **string** |             |

***
