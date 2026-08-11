
Declares controller actions that belong to one or more permission features.

Roles still opt into features through normal permission config. The attribute
only contributes the controller/action component entries, keeping feature
assignment central while allowing resource classes to declare their own
stable action surface.

***

* Full name: `\PhalconKit\Mvc\Controller\Attributes\PermissionFeature`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Properties

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
public __construct(array<int,string>|string $features, array<int,string>|string|null $actions = null): mixed
```

**Parameters:**

| Parameter   | Type                                | Description                                                                                    |
|-------------|-------------------------------------|------------------------------------------------------------------------------------------------|
| `$features` | **array<int,string>\|string**       | Permission feature names.                                                                      |
| `$actions`  | **array<int,string>\|string\|null** | Optional action names. Both
`findFirstWith` and `find-first-with` are accepted and normalized. |

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
