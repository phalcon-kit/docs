
Return a formatted string with multibyte-aware `%s` handling.

The format is converted to UTF-8 while parsing directives, then converted
back to the requested encoding before delegating non-string directives to
`vsprintf()`. String directives support sign, padding, alignment, width,
and precision. Argument swapping is intentionally not supported.

***

* Full name: `mb_vsprintf`
* Defined in: `src/Functions/Sprintf.php`

**See Also:**

* http://php.net/manual/en/function.sprintf.php#89020

## Parameters

| Parameter   | Type                 | Description                                                                     |
|-------------|----------------------|---------------------------------------------------------------------------------|
| `$format`   | **string**           | Multibyte-aware sprintf format.                                                 |
| `$argv`     | **array<int,mixed>** | Format arguments.                                                               |
| `$encoding` | **string\|null**     | Encoding used for the format and arguments.
Null uses `mb_internal_encoding()`. |

## Return Value

**string**

Formatted string.
