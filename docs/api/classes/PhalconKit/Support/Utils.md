
***

* Full name: `\PhalconKit\Support\Utils`

## Methods

### setUnlimitedRuntime

Remove time and memory limits

```php
public static setUnlimitedRuntime(): void
```

* This method is **static**.
***

### getNamespace

Get the Namespace from a class object

```php
public static getNamespace(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

***

### getShortName

Get the Namespace from a class object

```php
public static getShortName(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

***

### getName

Get the Namespace from a class object

```php
public static getName(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

***

### getDirname

Get the directory from a class object

```php
public static getDirname(object $class): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **object** |             |

***

### getMemoryUsage

Return an array of the current memory usage in MB

```php
public static getMemoryUsage(float $divider = 1048576.2, string $suffix = ' MB'): array{memory: string, memoryPeak: string, realMemory: string, realMemoryPeak: string}
```

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$divider` | **float**  |             |
| `$suffix`  | **string** |             |

***
