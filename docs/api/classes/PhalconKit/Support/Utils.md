
Miscellaneous low-level utility helpers.

These methods are intentionally small and static because they are used by
bootstrap, diagnostics, and legacy integration code before richer services
are always available. Prefer more specific services/helpers for new domain
behavior.

***

* Full name: `\PhalconKit\Support\Utils`

## Methods

### setUnlimitedRuntime

Remove memory and execution-time limits for long-running maintenance work.

```php
public static setUnlimitedRuntime(): void
```

This changes process-wide PHP INI settings. It is appropriate for trusted
CLI maintenance tasks, but should be used carefully in request/worker
contexts where unlimited runtime can exhaust server resources.

* This method is **static**.
***

### getNamespace

Return the namespace of an object instance.

```php
public static getNamespace(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

**Throws:**

If the object cannot be reflected.
- [`ReflectionException`](https://www.php.net/manual/en/class.reflectionexception.php){:target="_blank"}

***

### getShortName

Return the short class name of an object instance.

```php
public static getShortName(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

**Throws:**

If the object cannot be reflected.
- [`ReflectionException`](https://www.php.net/manual/en/class.reflectionexception.php){:target="_blank"}

***

### getName

Return the fully qualified class name of an object instance.

```php
public static getName(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

**Throws:**

If the object cannot be reflected.
- [`ReflectionException`](https://www.php.net/manual/en/class.reflectionexception.php){:target="_blank"}

***

### getDirname

Return the directory containing an object's declaring file.

```php
public static getDirname(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

**Throws:**

If the object cannot be reflected.
- [`ReflectionException`](https://www.php.net/manual/en/class.reflectionexception.php){:target="_blank"}

***

### getMemoryUsage

Return current and peak memory usage.

```php
public static getMemoryUsage(float $divider = 1048576.2, string $suffix = ' MB'): array{memory: string, memoryPeak: string, realMemory: string, realMemoryPeak: string}
```

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description                                      |
|------------|------------|--------------------------------------------------|
| `$divider` | **float**  | Number used to convert bytes into display units. |
| `$suffix`  | **string** | Suffix appended to formatted values.             |

***
