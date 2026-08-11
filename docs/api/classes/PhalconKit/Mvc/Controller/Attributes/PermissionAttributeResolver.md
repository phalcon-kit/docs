
Compiles controller PHP attributes into PhalconKit permission config arrays.

The resolver deliberately returns the existing `permissions` shape instead of
introducing a second policy system. Dispatcher security, ACL compilation, and
controller behavior attachment can merge the returned fragment into
application config and keep using the established enforcement paths.

***

* Full name: `\PhalconKit\Mvc\Controller\Attributes\PermissionAttributeResolver`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Properties

### cache

```php
private static array<class-string,array<string,mixed>> $cache
```

* This property is **static**.

***

## Methods

### forController

Compile attributes declared on a controller class and its public methods.

```php
public static forController(object|string $controller): array<string,mixed>
```

* This method is **static**.
**Parameters:**

| Parameter     | Type               | Description                        |
|---------------|--------------------|------------------------------------|
| `$controller` | **object\|string** | Controller instance or class name. |

**Return Value:**

Permission fragment containing `features`,
`roles`, `controllers`, and action-scoped `behaviorActions` entries.

***

### mergePermissions

Merge a permission fragment into configured permissions.

```php
public static mergePermissions(array<string,mixed> $base, array<string,mixed> $fragment): array<string,mixed>
```

List values are appended and de-duplicated; associative values are merged
recursively. This matches PhalconKit's additive config expectations without
mutating the original config object.

* This method is **static**.
**Parameters:**

| Parameter   | Type                    | Description                          |
|-------------|-------------------------|--------------------------------------|
| `$base`     | **array<string,mixed>** | Existing permission config.          |
| `$fragment` | **array<string,mixed>** | Attribute-derived permission config. |

**Return Value:**

Merged permissions.

***

### collectAttributes

```php
private static collectAttributes(array& $permissions, \ReflectionClass<object>|\ReflectionMethod $reflection, class-string $controllerClass, array<int,string> $defaultActions): void
```

* This method is **static**.
**Parameters:**

| Parameter          | Type                                            | Description |
|--------------------|-------------------------------------------------|-------------|
| `$permissions`     | **array**                                       |             |
| `$reflection`      | **\ReflectionClass<object>\|\ReflectionMethod** |             |
| `$controllerClass` | **class-string**                                |             |
| `$defaultActions`  | **array<int,string>**                           |             |

***

### attributeInstances

```php
private static attributeInstances(\ReflectionClass<object>|\ReflectionMethod $reflection, class-string<\PhalconKit\Mvc\Controller\Attributes\T> $attributeClass): array<int,\PhalconKit\Mvc\Controller\Attributes\T>
```

* This method is **static**.
**Parameters:**

| Parameter         | Type                                                      | Description |
|-------------------|-----------------------------------------------------------|-------------|
| `$reflection`     | **\ReflectionClass<object>\|\ReflectionMethod**           |             |
| `$attributeClass` | **class-string<\PhalconKit\Mvc\Controller\Attributes\T>** |             |

***

### addControllerAccess

```php
private static addControllerAccess(array<string,mixed>& $permissions, string $section, array<int,string> $keys, class-string $controllerClass, array<int,string> $actions): void
```

* This method is **static**.
**Parameters:**

| Parameter          | Type                    | Description |
|--------------------|-------------------------|-------------|
| `$permissions`     | **array<string,mixed>** |             |
| `$section`         | **string**              |             |
| `$keys`            | **array<int,string>**   |             |
| `$controllerClass` | **class-string**        |             |
| `$actions`         | **array<int,string>**   |             |

***

### addActionBehaviors

```php
private static addActionBehaviors(array<string,mixed>& $permissions, string $section, array<int,string> $keys, class-string $controllerClass, array<int,string> $actions, array<int,string> $behaviors): void
```

* This method is **static**.
**Parameters:**

| Parameter          | Type                    | Description |
|--------------------|-------------------------|-------------|
| `$permissions`     | **array<string,mixed>** |             |
| `$section`         | **string**              |             |
| `$keys`            | **array<int,string>**   |             |
| `$controllerClass` | **class-string**        |             |
| `$actions`         | **array<int,string>**   |             |
| `$behaviors`       | **array<int,string>**   |             |

***

### mergeValue

```php
private static mergeValue(mixed $base, mixed $incoming): array<array-key,mixed>
```

* This method is **static**.
**Parameters:**

| Parameter   | Type      | Description |
|-------------|-----------|-------------|
| `$base`     | **mixed** |             |
| `$incoming` | **mixed** |             |

***

### mergeList

```php
private static mergeList(array<int,mixed> $base, array<int,mixed> $incoming): array<int,mixed>
```

* This method is **static**.
**Parameters:**

| Parameter   | Type                 | Description |
|-------------|----------------------|-------------|
| `$base`     | **array<int,mixed>** |             |
| `$incoming` | **array<int,mixed>** |             |

***
