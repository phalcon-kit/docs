
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Params`

## Properties

### rawParams

```php
protected array<string,mixed>|null $rawParams
```

***
### defaultFilters

```php
protected array<string,array|string> $defaultFilters
```

***

## Methods

### getParam

Retrieve a specific parameter value by key.

```php
public getParam(string $key, array|string|null $filters = null, mixed|null $default = null, array|null $params = null): mixed
```

**Parameters:**

| Parameter  | Type                    | Description |
|------------|-------------------------|-------------|
| `$key`     | **string**              |             |
| `$filters` | **array\|string\|null** |             |
| `$default` | **mixed\|null**         |             |
| `$params`  | **array\|null**         |             |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### hasParam

Check if a given key exists in the parameter array.

```php
public hasParam(string $key, array|null $params = null, bool $cached = true): bool
```

**Parameters:**

| Parameter | Type            | Description |
|-----------|-----------------|-------------|
| `$key`    | **string**      |             |
| `$params` | **array\|null** |             |
| `$cached` | **bool**        |             |

***
### getParams

Retrieve specific or all request parameters.

```php
public getParams(array|null $fields = null, bool $cached = true, bool $deep = true): array<string,mixed>
```

Usage examples:
- getParams() -> all params
- getParams(['email', 'password']) -> only those keys
- getParams(['email' => [Filter::TRIM], 'password']) -> filtered subset

**Parameters:**

| Parameter | Type            | Description                             |
|-----------|-----------------|-----------------------------------------|
| `$fields` | **array\|null** | Keys or key=>filters to extract.        |
| `$cached` | **bool**        | Whether to reuse cached raw parameters. |
| `$deep`   | **bool**        | Whether to apply deep sanitization.     |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### getAllParams

Retrieve all request parameters, optionally applying filters and caching results.

```php
public getAllParams(array|null $filters = null, bool $cached = true, bool $deep = true): array<string,mixed>
```

**Parameters:**

| Parameter  | Type            | Description                                    |
|------------|-----------------|------------------------------------------------|
| `$filters` | **array\|null** | Temporary filters to apply.                    |
| `$cached`  | **bool**        | Whether to reuse previously loaded parameters. |
| `$deep`    | **bool**        | Whether to apply filters recursively.          |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### collectRequestParams

Collect parameters based on the HTTP method.

```php
private collectRequestParams(): array<string,mixed>
```

***
### applyFilters

Apply filters to parameters (recursively if $deep is true).

```php
public applyFilters(array<string,mixed> $params, array<string,array|string> $filters, bool $deep = true): array<string,mixed>
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$params`  | **array<string,mixed>**         |             |
| `$filters` | **array<string,array\|string>** |             |
| `$deep`    | **bool**                        |             |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### deepSanitize

Recursively sanitize nested arrays.

```php
private deepSanitize(mixed $value, array|string $filters): mixed
```

**Parameters:**

| Parameter  | Type              | Description |
|------------|-------------------|-------------|
| `$value`   | **mixed**         |             |
| `$filters` | **array\|string** |             |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### setDefaultFilters

Sets default filters, replacing any previously defined.

```php
public setDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***
### addDefaultFilters

Adds or merges new default filters to existing ones.

```php
public addDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***
### removeFilters

Remove one or many default filters by key.

```php
public removeFilters(string|array<int,string> $keys): static
```

**Parameters:**

| Parameter | Type                          | Description |
|-----------|-------------------------------|-------------|
| `$keys`   | **string\|array<int,string>** |             |

***
### clearDefaultFilters

Clears all default filters.

```php
public clearDefaultFilters(): static
```

***
### getDefaultFilters

Get currently active default filters.

```php
public getDefaultFilters(): array<string,array|string>
```

***
### getRawParams

Retrieves the raw parameters from the request. If caching is enabled, it returns the cached parameters.

```php
public getRawParams(bool $cached = true): array<string,mixed>
```

**Parameters:**

| Parameter | Type     | Description                                                    |
|-----------|----------|----------------------------------------------------------------|
| `$cached` | **bool** | Determines whether to use cached parameters. Defaults to true. |

**Return Value:**

The raw request parameters.

***
