
Builds native Phalcon ACL instances from PhalconKit permission config.

The input permission structure is the same shape used by REST controllers:
roles can reference reusable feature blocks, components map to allowed
accesses, and role inheritance can be applied through a configurable key.
The builder returns a native in-memory ACL so downstream code can use normal
Phalcon ACL checks after PhalconKit has expanded the app config.

***

* Full name: `\PhalconKit\Acl\Acl`
* Parent class: [`AbstractInjectionAware`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Acl\AclInterface`](./AclInterface.md)

## Methods

### get

Build an in-memory ACL for one or more configured component sections.

```php
public get(array<int,string> $componentsName = ['components'], array<string,mixed>|null $permissions = null, string $inherit = 'inherit'): \Phalcon\Acl\Adapter\Memory
```

`componentsName` lets callers build ACLs from alternate permission
sections, for example `components`, `models`, or app-specific groups.
When `permissions` is null, the method reads the `permissions` option
stored on this ACL service. Feature entries referenced by roles are merged
before components are registered.

Integer component keys are treated as shorthand component names with `*`
access. A component named `*` is ignored because Phalcon's native ACL
still needs concrete component registrations.

**Parameters:**

| Parameter         | Type                          | Description                                      |
|-------------------|-------------------------------|--------------------------------------------------|
| `$componentsName` | **array<int,string>**         | Permission sections to inspect.                  |
| `$permissions`    | **array<string,mixed>\|null** | Permission tree to compile.                      |
| `$inherit`        | **string**                    | Role-inheritance key inside the permission tree. |

**Return Value:**

Native Phalcon in-memory ACL populated with roles,
components, accesses, and inheritance.

***

## Inherited methods

### __construct

Construct the object and initialize its options.

```php
public __construct(array<string,mixed>|null $options = null): mixed
```

**Parameters:**

| Parameter  | Type                          | Description                    |
|------------|-------------------------------|--------------------------------|
| `$options` | **array<string,mixed>\|null** | Defaults to capture and apply. |

***

### initializeOptions

Capture defaults, apply the current options, and run initialize().

```php
public initializeOptions(array<string,mixed>|null $options = null): void
```

**Parameters:**

| Parameter  | Type                          | Description                    |
|------------|-------------------------------|--------------------------------|
| `$options` | **array<string,mixed>\|null** | Defaults to capture and apply. |

***

### initialize

Optional hook called after options are initialized.

```php
public initialize(): void
```

Override this in classes that need to derive internal state from options
during construction.

***

### setOptions

Replace or merge the current option set.

```php
public setOptions(array<string,mixed> $options, bool $merge = false): void
```

Options intentionally use PHP's null-coalescing read semantics: a key
stored with a null value remains present in the raw option array, but


- **See:** \PhalconKit\Support\Options\getOption() returns the caller default and
- **See:** \PhalconKit\Support\Options\hasOption()
reports false for that key.

**Parameters:**

| Parameter  | Type                    | Description                                                       |
|------------|-------------------------|-------------------------------------------------------------------|
| `$options` | **array<string,mixed>** | Options to apply.                                                 |
| `$merge`   | **bool**                | Whether to merge into existing options instead of
replacing them. |

***

### getOptions

Return the current option set.

```php
public getOptions(): array<string,mixed>
```

***

### setOption

Store or replace one option value.

```php
public setOption(string $key, mixed $value = null, bool $merge = false): void
```

Passing null stores the key in the raw option array, but the key still
reads as missing through

- **See:** \PhalconKit\Support\Options\getOption() and
- **See:** \PhalconKit\Support\Options\hasOption(). This
preserves the historical contract where null means "fall back to the
caller default" while still allowing callers to inspect raw options.

**Parameters:**

| Parameter | Type       | Description                                                         |
|-----------|------------|---------------------------------------------------------------------|
| `$key`    | **string** |                                                                     |
| `$value`  | **mixed**  |                                                                     |
| `$merge`  | **bool**   | Whether to merge the key/value pair into the existing
option array. |

***

### getOption

Return one option value or a default when it is missing or null.

```php
public getOption(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description                                  |
|------------|------------|----------------------------------------------|
| `$key`     | **string** |                                              |
| `$default` | **mixed**  | Default returned when the option is not set. |

***

### hasOption

Return true when an option is present and not null.

```php
public hasOption(string $key): bool
```

This intentionally mirrors

- **See:** \PhalconKit\Support\Options\getOption() rather than
`array_key_exists()`: null-valued options are stored in the raw option
array but are treated as absent by the public lookup helpers.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### removeOption

Remove one option key when it exists in the raw option array.

```php
public removeOption(string $key): void
```

Removal uses `array_key_exists()` instead of `isset()` so callers can
delete a key even when it currently stores null.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### resetOptions

Restore current options to the initialized defaults.

```php
public resetOptions(): void
```

***

### clearOptions

Remove all current option values.

```php
public clearOptions(): void
```

***
