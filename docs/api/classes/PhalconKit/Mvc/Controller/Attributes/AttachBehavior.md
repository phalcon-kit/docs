
Attaches controller behaviors through role or feature permissions.

Behaviors declared with this attribute are compiled into action-scoped
permission metadata. When neither `roles` nor `features` is provided the
behavior is attached for the `everyone` role, which matches PhalconKit's
context role available to every identity.

***

* Full name: `\PhalconKit\Mvc\Controller\Attributes\AttachBehavior`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Properties

### behaviors

```php
public array<int,string> $behaviors
```

***

### roles

```php
public array<int,string> $roles
```

***

### features

```php
public array<int,string> $features
```

***

### actions

```php
public array<int,string>|null $actions
```

***

## Methods

### __construct

```php
public __construct(array<int,string>|string $behaviors, array<int,string>|string|null $roles = null, array<int,string>|string|null $features = null, array<int,string>|string|null $actions = null): mixed
```

**Parameters:**

| Parameter    | Type                                | Description                                                                                     |
|--------------|-------------------------------------|-------------------------------------------------------------------------------------------------|
| `$behaviors` | **array<int,string>\|string**       | Behavior class or class list
to attach.                                                         |
| `$roles`     | **array<int,string>\|string\|null** | Optional direct ACL roles.                                                                      |
| `$features`  | **array<int,string>\|string\|null** | Optional permission
features. Roles that already reference these features receive the
behavior. |
| `$actions`   | **array<int,string>\|string\|null** | Optional action names. Both
`saveUser` and `save-user` are accepted.                            |

***

### list

```php
private static list(array|string $values): array<int,string>
```

* This method is **static**.
**Parameters:**

| Parameter | Type              | Description |
|-----------|-------------------|-------------|
| `$values` | **array\|string** |             |

***
