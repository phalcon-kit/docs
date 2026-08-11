
Format every non-null array value and join the formatted parts.

The callback receives both value and key, so formats can use `%%1$s` for
the value and `%%2$s` for the key. Null values are omitted before
formatting; false, zero, and empty strings are preserved.

***

* Full name: `implode_sprintf`
* Defined in: `src/Functions/Sprintf.php`

## Parameters

| Parameter    | Type                       | Description                                                                             |
|--------------|----------------------------|-----------------------------------------------------------------------------------------|
| `$array`     | **array<array-key,mixed>** | Values to format.                                                                       |
| `$glue`      | **string**                 | String inserted between formatted values.                                               |
| `$format`    | **string**                 | `sprintf()`/`mb_vsprintf()` format string.                                              |
| `$multibyte` | **bool**                   | Whether formatting should use `mb_vsprintf()`.                                          |
| `$encoding`  | **string\|null**           | Encoding used when multibyte formatting is
enabled. Null uses `mb_internal_encoding()`. |

## Return Value

**string**

Joined formatted values, or an empty string for an empty
input array.
