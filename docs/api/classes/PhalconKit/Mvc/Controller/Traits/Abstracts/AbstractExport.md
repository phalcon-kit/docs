
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\AbstractExport`

## Methods

### getContentType

```php
public getContentType(?array $params = null): string
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$params` | **?array** |             |

***
### getFilename

```php
public getFilename(): string
```

* This method is **abstract**.
***
### getExportColumns

```php
public getExportColumns(array $list): array
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$list`   | **array** |             |

***
### export

```php
public export(array $list, ?string $filename = null, ?string $contentType = null, ?array $params = null): \Phalcon\Http\ResponseInterface
```

* This method is **abstract**.
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
public exportXml(array $list, ?string $filename = null, ?array $params = null): \Phalcon\Http\ResponseInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$list`     | **array**   |             |
| `$filename` | **?string** |             |
| `$params`   | **?array**  |             |

***
### exportJson

```php
public exportJson(mixed $list, ?string $filename = null, int $flags = JSON_PRETTY_PRINT, int $depth = 2048): \Phalcon\Http\ResponseInterface
```

* This method is **abstract**.
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
public exportExcel(array $list, ?string $filename = null, bool $forceRawValue = true): \Phalcon\Http\ResponseInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter        | Type        | Description |
|------------------|-------------|-------------|
| `$list`          | **array**   |             |
| `$filename`      | **?string** |             |
| `$forceRawValue` | **bool**    |             |

***
### exportCsv

```php
public exportCsv(array $list, ?string $filename = null, ?array $params = null): \Phalcon\Http\ResponseInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$list`     | **array**   |             |
| `$filename` | **?string** |             |
| `$params`   | **?array**  |             |

***
