
Return a formatted multibyte string
A more complete and working version of mb_sprintf and mb_vsprintf.

It should work with any "ASCII preserving" encoding such as UTF-8 and all the ISO-8859 charsets.
It handles sign, padding, alignment, width and precision. Argument swapping is not handled.

***

* Full name: `mb_sprintf`
* Defined in: `src/Functions/Sprintf.php`

## Parameters

| Parameter | Type                   | Description |
|-----------|------------------------|-------------|
| `$format` | **string**             |             |
| `$args`   | **string\|int\|float** |             |

## Return Value

**string**
