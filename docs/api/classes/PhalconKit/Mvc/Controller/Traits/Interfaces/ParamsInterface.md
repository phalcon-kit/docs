
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\ParamsInterface`

## Methods

### getParam

```php
public getParam(string $key, array|string|null $filters = null, mixed $default = null, ?array $params = null): mixed
```

**Parameters:**

| Parameter  | Type                    | Description |
|------------|-------------------------|-------------|
| `$key`     | **string**              |             |
| `$filters` | **array\|string\|null** |             |
| `$default` | **mixed**               |             |
| `$params`  | **?array**              |             |

***

### hasParam

```php
public hasParam(string $key, ?array $params = null, bool $cached = true): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |
| `$params` | **?array** |             |
| `$cached` | **bool**   |             |

***

### getParams

```php
public getParams(?array $fields = null, bool $cached = true, bool $deep = true): array
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$fields` | **?array** |             |
| `$cached` | **bool**   |             |
| `$deep`   | **bool**   |             |

***

### getAllParams

```php
public getAllParams(?array $filters = null, bool $cached = true, bool $deep = true): array
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$filters` | **?array** |             |
| `$cached`  | **bool**   |             |
| `$deep`    | **bool**   |             |

***

### applyFilters

```php
public applyFilters(array<string,mixed> $params, array<string,array|string> $filters, bool $deep = true): array<string,mixed>
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$params`  | **array<string,mixed>**         |             |
| `$filters` | **array<string,array\|string>** |             |
| `$deep`    | **bool**                        |             |

***

### setDefaultFilters

```php
public setDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### addDefaultFilters

```php
public addDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### removeFilters

```php
public removeFilters(string|array<int,string> $keys): static
```

**Parameters:**

| Parameter | Type                          | Description |
|-----------|-------------------------------|-------------|
| `$keys`   | **string\|array<int,string>** |             |

***

### clearDefaultFilters

```php
public clearDefaultFilters(): static
```

***

### getDefaultFilters

```php
public getDefaultFilters(): array
```

***

### getRawParams

```php
public getRawParams(bool $cached = true): array
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$cached` | **bool** |             |

***
