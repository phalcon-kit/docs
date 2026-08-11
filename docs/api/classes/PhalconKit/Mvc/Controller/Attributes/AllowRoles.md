
Grants controller actions directly to one or more ACL roles.

The attribute is additive. It compiles into the same permission array consumed
by the existing ACL service, so config-driven features and roles continue to
work. Method-level attributes default to the annotated `*Action()` method;
class-level attributes default to `*` unless `actions` is provided.

***

* Full name: `\PhalconKit\Mvc\Controller\Attributes\AllowRoles`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Properties

### roles

```php
public array<int,string> $roles
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
public __construct(array<int,string>|string $roles, array<int,string>|string|null $actions = null): mixed
```

**Parameters:**

| Parameter  | Type                                | Description                                                                         |
|------------|-------------------------------------|-------------------------------------------------------------------------------------|
| `$roles`   | **array<int,string>\|string**       | ACL roles to grant.                                                                 |
| `$actions` | **array<int,string>\|string\|null** | Optional action names. Both
`findWith` and `find-with` are accepted and normalized. |

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
