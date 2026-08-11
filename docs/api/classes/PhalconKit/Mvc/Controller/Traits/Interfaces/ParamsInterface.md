
Contract for filtered REST request parameter access.

Implementations select a single request parameter source according to the
request method, then apply Phalcon filter services on demand. Body methods
may prefer a JSON payload over form data, but query parameters are not merged
into body payloads.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\ParamsInterface`

## Methods

### getParam

Return one filtered parameter value.

```php
public getParam(string $key, array|string|null $filters = null, mixed $default = null, array<array-key,mixed>|null $params = null): mixed
```

**Parameters:**

| Parameter  | Type                             | Description                            |
|------------|----------------------------------|----------------------------------------|
| `$key`     | **string**                       | Parameter key.                         |
| `$filters` | **array\|string\|null**          | Filter name(s) to apply.               |
| `$default` | **mixed**                        | Default value when the key is missing. |
| `$params`  | **array<array-key,mixed>\|null** | Optional parameter source.             |

***

### hasParam

Determine whether a parameter exists.

```php
public hasParam(string $key, array<array-key,mixed>|null $params = null, bool $cached = true): bool
```

**Parameters:**

| Parameter | Type                             | Description                                         |
|-----------|----------------------------------|-----------------------------------------------------|
| `$key`    | **string**                       |                                                     |
| `$params` | **array<array-key,mixed>\|null** | Optional parameter source.                          |
| `$cached` | **bool**                         | Whether cached controller parameters may be reused. |

***

### getParams

Return selected filtered controller parameters.

```php
public getParams(list<string>|array<string,array|string>|null $fields = null, bool $cached = true, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type                                                | Description                                               |
|-----------|-----------------------------------------------------|-----------------------------------------------------------|
| `$fields` | **list<string>\|array<string,array\|string>\|null** | Optional
field names or field-to-filter map.              |
| `$cached` | **bool**                                            | Whether cached controller parameters may be reused.       |
| `$deep`   | **bool**                                            | Whether nested parameters should be filtered
recursively. |

***

### getAllParams

Return all request parameters after default filters are applied.

```php
public getAllParams(array<string,array|string>|null $filters = null, bool $cached = true, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter  | Type                                  | Description                                               |
|------------|---------------------------------------|-----------------------------------------------------------|
| `$filters` | **array<string,array\|string>\|null** | Optional filter map.                                      |
| `$cached`  | **bool**                              | Whether cached controller parameters may be reused.       |
| `$deep`    | **bool**                              | Whether nested parameters should be filtered
recursively. |

***

### applyFilters

```php
public applyFilters(array<array-key,mixed> $params, array<string,array|string> $filters, bool $deep = true): array<array-key,mixed>
```

**Parameters:**

| Parameter  | Type                            | Description                                               |
|------------|---------------------------------|-----------------------------------------------------------|
| `$params`  | **array<array-key,mixed>**      |                                                           |
| `$filters` | **array<string,array\|string>** |                                                           |
| `$deep`    | **bool**                        | Whether nested parameters should be filtered
recursively. |

***

### setDefaultFilters

Replace default filters applied by `getAllParams()`.

```php
public setDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### addDefaultFilters

Merge additional default filters.

```php
public addDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### removeFilters

Remove one or more default filters by parameter key.

```php
public removeFilters(string|array<int,string> $keys): static
```

**Parameters:**

| Parameter | Type                          | Description |
|-----------|-------------------------------|-------------|
| `$keys`   | **string\|array<int,string>** |             |

***

### clearDefaultFilters

Remove all default filters.

```php
public clearDefaultFilters(): static
```

***

### getDefaultFilters

Return default filters applied by `getAllParams()`.

```php
public getDefaultFilters(): array<string,array|string>
```

***

### getRawParams

Return unfiltered request parameters.

```php
public getRawParams(bool $cached = true): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type     | Description                                  |
|-----------|----------|----------------------------------------------|
| `$cached` | **bool** | Whether cached raw parameters may be reused. |

***
