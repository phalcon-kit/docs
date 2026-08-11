
Return a formatted multibyte string.

This convenience wrapper delegates to `mb_vsprintf()`. It is intended for
ASCII-preserving encodings such as UTF-8 and ISO-8859 variants, and it
handles sign, padding, alignment, width, and precision. Argument swapping
is intentionally not supported by the multibyte implementation.

***

* Full name: `mb_sprintf`
* Defined in: `src/Functions/Sprintf.php`

## Parameters

| Parameter | Type                   | Description                     |
|-----------|------------------------|---------------------------------|
| `$format` | **string**             | Multibyte-aware sprintf format. |
| `$args`   | **string\|int\|float** | Format arguments.               |

## Return Value

**string**

Formatted string.
