
Provides some utility methods to export data

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Export`

## Methods

### getContentType

Get the content type based on the given parameters.

```php
public getContentType(array|null $params = null): string
```

**Parameters:**

| Parameter | Type            | Description                                                                                                  |
|-----------|-----------------|--------------------------------------------------------------------------------------------------------------|
| `$params` | **array\|null** | Optional. The parameters to determine the content type. If not provided, it will use the default parameters. |

**Return Value:**

The content type. Possible values: "json", "csv", "xlsx".

**Throws:**

When an unsupported content type is provided.
- [`HttpException`](../../../Exception/HttpException.md)

***
### getFilename

Returns the filename for the exported file.

```php
public getFilename(): string
```

The filename is generated based on the model class name, with any
namespaces replaced by slashes, and then slugified. It is then
prepended with the current date in the 'Y-m-d' format.

**Return Value:**

The generated filename for the exported file.

***
### getExportColumns

Retrieves the columns from the given list of data.

```php
public getExportColumns(array $list): array
```

**Parameters:**

| Parameter | Type      | Description                               |
|-----------|-----------|-------------------------------------------|
| `$list`   | **array** | The list of data to extract columns from. |

**Return Value:**

An associative array containing the export columns as keys.

***
### export

Exports the given list to a specified file in the specified format.

```php
public export(array $list = [], string|null $filename = null, string|null $contentType = null, array|null $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter      | Type             | Description                                                                                         |
|----------------|------------------|-----------------------------------------------------------------------------------------------------|
| `$list`        | **array**        | The list of data to export.                                                                         |
| `$filename`    | **string\|null** | The filename of the exported file. If not provided, the default filename will be used.              |
| `$contentType` | **string\|null** | The content type of the exported file. If not provided, the default content type will be used.      |
| `$params`      | **array\|null**  | Additional parameters for the export process. If not provided, the default parameters will be used. |

**Return Value:**

Returns true if the export was successful, otherwise false.

**Throws:**

Thrown if the specified content type is not supported.
- [`HttpException`](../../../Exception/HttpException.md)

***
### exportXml

Exports the given list to an XML file with the specified filename.

```php
public exportXml(array $list, string|null $filename = null, ?array $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type             | Description                                                                              |
|-------------|------------------|------------------------------------------------------------------------------------------|
| `$list`     | **array**        | The list of data to export.                                                              |
| `$filename` | **string\|null** | The filename of the exported XML file. If not provided, a default filename will be used. |
| `$params`   | **?array**       |                                                                                          |

***
### exportJson

Export data as JSON file for download.

```php
public exportJson(mixed $list, string|null $filename = null, int $flags = \PhalconKit\Mvc\Controller\Traits\JSON_PRETTY_PRINT, int $depth = 2048): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type             | Description                                                                              |
|-------------|------------------|------------------------------------------------------------------------------------------|
| `$list`     | **mixed**        | The data to be exported as JSON. Can be an array, object, or any serializable data type. |
| `$filename` | **string\|null** | The name of the exported file. If not provided, the default filename will be used.       |
| `$flags`    | **int**          | Optional JSON encoding options. Default is JSON_PRETTY_PRINT.                            |
| `$depth`    | **int**          | Optional maximum depth of recursion. Default is 2048.                                    |

***
### exportExcel

Export data as an Excel spreadsheet

```php
public exportExcel(array $list, string|null $filename = null, bool $forceRawValue = true): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter        | Type             | Description                                           |
|------------------|------------------|-------------------------------------------------------|
| `$list`          | **array**        | The data to be exported                               |
| `$filename`      | **string\|null** | The desired filename for the exported file (optional) |
| `$forceRawValue` | **bool**         |                                                       |

***
### exportCsv

Export rows as CSV and translate CSV library failures into stable
PhalconKit exceptions.

```php
public exportCsv(array<array-key,mixed> $list, string|null $filename = null, array<array-key,mixed>|null $params = null): \Phalcon\Http\ResponseInterface
```

Request-controlled CSV options are validated by the League CSV writer.
Invalid delimiters, enclosures, escape characters, or BOM values become a
`400` HTTP exception because the client supplied an unsupported export
option. Insert/write failures remain server-side runtime errors and keep
the original League exception as `previous` for diagnostics.

**Parameters:**

| Parameter   | Type                             | Description                 |
|-------------|----------------------------------|-----------------------------|
| `$list`     | **array<array-key,mixed>**       | Rows to export.             |
| `$filename` | **string\|null**                 | Filename without extension. |
| `$params`   | **array<array-key,mixed>\|null** | CSV export options.         |

**Return Value:**

Download response containing CSV content.

**Throws:**

When a CSV export option has an invalid type or
value.
- [`HttpException`](../../../Exception/HttpException.md)
When CSV generation fails after options have
been accepted.
- [`RuntimeException`](../../../Exception/RuntimeException.md)

***
### buildCsvExportResponse

Build the CSV writer output and attach it to the controller response.

```php
private buildCsvExportResponse(array<array-key,mixed> $list, string|null $filename, array<array-key,mixed>|null $params): \Phalcon\Http\ResponseInterface
```

This method assumes its caller wraps League CSV exceptions through


- **See:** \PhalconKit\Mvc\Controller\Traits\withCsvExceptions(). Keeping the generation logic separate from
exception translation keeps the public method small while preserving the
current CSV behavior: Windows-compatible UTF-8 by default, UTF-16/tab
output for `mode=mac`, forced enclosures unless relaxed, and optional
newline collapsing for spreadsheet compatibility.

**Parameters:**

| Parameter   | Type                             | Description                 |
|-------------|----------------------------------|-----------------------------|
| `$list`     | **array<array-key,mixed>**       | Rows to export.             |
| `$filename` | **string\|null**                 | Filename without extension. |
| `$params`   | **array<array-key,mixed>\|null** | CSV export options.         |

**Throws:**

When League CSV rejects an option or cannot write
rows.
- [`Exception`](https://csv.thephpleague.com/){:target="_blank"}
When an option has a type that should not reach the
League writer.
- [`HttpException`](../../../Exception/HttpException.md)

***
### withCsvExceptions

Execute CSV generation while exposing stable framework exceptions.

```php
private withCsvExceptions(callable $callback): \Phalcon\Http\ResponseInterface
```

League CSV exceptions are useful internally but too vendor-specific for a
public REST controller helper. This wrapper keeps client option mistakes
as HTTP `400` errors and turns lower-level writer failures into
PhalconKit runtime exceptions with the original exception attached for
logs and debuggers.

**Parameters:**

| Parameter   | Type         | Description              |
|-------------|--------------|--------------------------|
| `$callback` | **callable** | CSV generation callback. |

**Throws:**

When a CSV option is rejected by the writer.
- [`HttpException`](../../../Exception/HttpException.md)
When CSV writing fails after options are valid.
- [`RuntimeException`](../../../Exception/RuntimeException.md)

***
### getCsvStringOption

Return a string-based CSV option from the export parameter array.

```php
private getCsvStringOption(array<array-key,mixed> $params, string $name): ?string
```

CSV control options are normally request values and must be strings before
they are passed to League CSV's typed setters. Validating the shape here
turns accidental nested arrays or objects into a stable HTTP `400` instead
of a PHP `TypeError`.

**Parameters:**

| Parameter | Type                       | Description          |
|-----------|----------------------------|----------------------|
| `$params` | **array<array-key,mixed>** | Export options.      |
| `$name`   | **string**                 | Option name to read. |

**Throws:**

When the option is present but not a string.
- [`HttpException`](../../../Exception/HttpException.md)

***
### getCsvOutputBomOption

Return the optional output BOM value accepted by the CSV writer.

```php
private getCsvOutputBomOption(array<array-key,mixed> $params): \League\Csv\Bom|string|null
```

Application code can pass a League `Bom` enum directly, while request
input usually passes one of the string values supported by League CSV.
Other shapes are rejected before they reach the writer's typed API.

**Parameters:**

| Parameter | Type                       | Description     |
|-----------|----------------------------|-----------------|
| `$params` | **array<array-key,mixed>** | Export options. |

**Throws:**

When the `outputBOM` option has an unsupported type.
- [`HttpException`](../../../Exception/HttpException.md)

***
