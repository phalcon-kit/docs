
Multibyte-safe variant of `implode_sprintf()`.

Values are formatted with `mb_vsprintf()` so string width and precision
handling respect the selected encoding.

***

* Full name: `implode_mb_sprintf`
* Defined in: `src/Functions/Sprintf.php`

## Parameters

| Parameter   | Type                       | Description                                                                 |
|-------------|----------------------------|-----------------------------------------------------------------------------|
| `$array`    | **array<array-key,mixed>** | Values to format.                                                           |
| `$glue`     | **string**                 | String inserted between formatted values.                                   |
| `$format`   | **string**                 | Multibyte sprintf format string.                                            |
| `$encoding` | **string\|null**           | Encoding used for multibyte formatting. Null
uses `mb_internal_encoding()`. |

## Return Value

**string**

Joined formatted values.
