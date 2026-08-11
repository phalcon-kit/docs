
Contract for REST file export helpers.

Implementations prepare a download response for JSON, XML, CSV, or XLSX
output. Export methods return the response object so callers can continue
using the normal Phalcon response pipeline.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\ExportInterface`

## Methods

### getContentType

Resolve the requested export content type.

```php
public getContentType(array<string,mixed>|null $params = null): string
```

**Parameters:**

| Parameter | Type                          | Description                |
|-----------|-------------------------------|----------------------------|
| `$params` | **array<string,mixed>\|null** | Request/export parameters. |

**Return Value:**

One of `json`, `xml`, `csv`, or `xlsx`.

**Throws:**

When the requested content type is unsupported.
- [`HttpException`](../../../../Exception/HttpException.md)

***

### getFilename

Build the default export filename without a file extension.

```php
public getFilename(): string
```

***

### getExportColumns

Determine the union of exported columns from an array payload.

```php
public getExportColumns(array<array-key,mixed> $list): list<string>
```

**Parameters:**

| Parameter | Type                       | Description      |
|-----------|----------------------------|------------------|
| `$list`   | **array<array-key,mixed>** | Rows to inspect. |

***

### export

Export rows using the requested or detected content type.

```php
public export(array<array-key,mixed> $list, string|null $filename = null, string|null $contentType = null, array<array-key,mixed>|null $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter      | Type                             | Description                 |
|----------------|----------------------------------|-----------------------------|
| `$list`        | **array<array-key,mixed>**       | Rows to export.             |
| `$filename`    | **string\|null**                 | Filename without extension. |
| `$contentType` | **string\|null**                 | Explicit export type.       |
| `$params`      | **array<array-key,mixed>\|null** | Export options.             |

**Throws:**

When the content type or request-controlled export
options are invalid.
- [`HttpException`](../../../../Exception/HttpException.md)
When the selected exporter accepts its options
but cannot generate the response payload.
- [`RuntimeException`](../../../../Exception/RuntimeException.md)

***

### exportXml

Export rows as XML.

```php
public exportXml(array<array-key,mixed> $list, string|null $filename = null, array<array-key,mixed>|null $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type                             | Description                 |
|-------------|----------------------------------|-----------------------------|
| `$list`     | **array<array-key,mixed>**       | Rows to export.             |
| `$filename` | **string\|null**                 | Filename without extension. |
| `$params`   | **array<array-key,mixed>\|null** | XML export options.         |

***

### exportJson

Export a serializable value as JSON.

```php
public exportJson(mixed $list, string|null $filename = null, int $flags = \PhalconKit\Mvc\Controller\Traits\Interfaces\JSON_PRETTY_PRINT, int $depth = 2048): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type             | Description                  |
|-------------|------------------|------------------------------|
| `$list`     | **mixed**        | Serializable export payload. |
| `$filename` | **string\|null** | Filename without extension.  |
| `$flags`    | **int**          | `json_encode()` flags.       |
| `$depth`    | **int**          | Maximum JSON depth.          |

***

### exportExcel

Export rows as XLSX.

```php
public exportExcel(array<array-key,mixed> $list, string|null $filename = null, bool $forceRawValue = true): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter        | Type                       | Description                                                              |
|------------------|----------------------------|--------------------------------------------------------------------------|
| `$list`          | **array<array-key,mixed>** | Rows to export.                                                          |
| `$filename`      | **string\|null**           | Filename without extension.                                              |
| `$forceRawValue` | **bool**                   | Prefix formula-like values to reduce
spreadsheet formula injection risk. |

***

### exportCsv

Export rows as CSV.

```php
public exportCsv(array<array-key,mixed> $list, string|null $filename = null, array<array-key,mixed>|null $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type                             | Description                 |
|-------------|----------------------------------|-----------------------------|
| `$list`     | **array<array-key,mixed>**       | Rows to export.             |
| `$filename` | **string\|null**                 | Filename without extension. |
| `$params`   | **array<array-key,mixed>\|null** | CSV export options.         |

**Throws:**

When a CSV option has an invalid type or value.
- [`HttpException`](../../../../Exception/HttpException.md)
When CSV generation fails after options have
been accepted.
- [`RuntimeException`](../../../../Exception/RuntimeException.md)

***
