
URL service that normalizes generated local paths.

PhalconKit keeps Phalcon's URL generation behavior, then normalizes local
paths to absolute paths by resolving duplicate separators and `.`/`..`
segments. Fully-qualified and protocol-relative URLs are preserved.

***

* Full name: `\PhalconKit\Mvc\Url`
* Parent class: [`Url`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### get

Generate a URL and normalize local results to absolute paths.

```php
public get(array|string|null $uri = null, mixed $arguments = null, bool|null $local = null, mixed $baseUri = null, bool $replaceArgs = false): string
```

**Parameters:**

| Parameter      | Type                    | Description                                    |
|----------------|-------------------------|------------------------------------------------|
| `$uri`         | **array\|string\|null** | Phalcon route name/path input.                 |
| `$arguments`   | **mixed**               | Route or query arguments passed to Phalcon.    |
| `$local`       | **bool\|null**          | Whether Phalcon should treat the URL as local. |
| `$baseUri`     | **mixed**               | Optional base URI override.                    |
| `$replaceArgs` | **bool**                | Whether route placeholders should be replaced. |

**Return Value:**

Generated URL with local paths normalized.

***

### getAbsolutePath

Normalize a local path into an absolute path.

```php
public static getAbsolutePath(string $path): string
```

Absolute HTTP(S) URLs and protocol-relative URLs are returned unchanged
because normalizing their path component here could alter an external
target. Local paths are normalized by converting backslashes to forward
slashes, removing empty and `.` segments, and resolving `..` segments
without allowing the result to escape above `/`.

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description                        |
|-----------|------------|------------------------------------|
| `$path`   | **string** | Local path or fully-qualified URL. |

**Return Value:**

Normalized absolute local path, or the original external
URL.

***
