
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\ExportInterface`

## Methods

### getContentType

```php
public getContentType(?array $params = null): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$params` | **?array** |             |

***

### getFilename

```php
public getFilename(): string
```

***

### getExportColumns

```php
public getExportColumns(array $list): array
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$list`   | **array** |             |

***

### export

```php
public export(array $list, ?string $filename = null, ?string $contentType = null, ?array $params = null): bool
```

**Parameters:**

| Parameter      | Type        | Description |
|----------------|-------------|-------------|
| `$list`        | **array**   |             |
| `$filename`    | **?string** |             |
| `$contentType` | **?string** |             |
| `$params`      | **?array**  |             |

***

### exportXml

```php
public exportXml(array $list, ?string $filename = null, ?array $params = null): bool
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$list`     | **array**   |             |
| `$filename` | **?string** |             |
| `$params`   | **?array**  |             |

***

### exportJson

```php
public exportJson(mixed $list, ?string $filename = null, int $flags = JSON_PRETTY_PRINT, int $depth = 2048): bool
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$list`     | **mixed**   |             |
| `$filename` | **?string** |             |
| `$flags`    | **int**     |             |
| `$depth`    | **int**     |             |

***

### exportExcel

```php
public exportExcel(array $list, ?string $filename = null): bool
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$list`     | **array**   |             |
| `$filename` | **?string** |             |

***

### exportCsv

```php
public exportCsv(array $list, ?string $filename = null, ?array $params = null): bool
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$list`     | **array**   |             |
| `$filename` | **?string** |             |
| `$params`   | **?array**  |             |

***
