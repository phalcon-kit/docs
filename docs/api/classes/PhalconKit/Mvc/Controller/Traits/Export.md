
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
- [`Exception`](../../../../Exception.md)

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
- [`Exception`](../../../../Exception.md)

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
public exportJson(mixed $list, string|null $filename = null, int $flags = JSON_PRETTY_PRINT, int $depth = 2048): \Phalcon\Http\ResponseInterface
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

```php
public exportCsv(array $list, ?string $filename = null, ?array $params = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$list`     | **array**   |             |
| `$filename` | **?string** |             |
| `$params`   | **?array**  |             |

**Throws:**

- [`InvalidArgument`](https://csv.thephpleague.com/){:target="_blank"}
- [`CannotInsertRecord`](https://csv.thephpleague.com/){:target="_blank"}
- [`Exception`](https://csv.thephpleague.com/){:target="_blank"}

***
