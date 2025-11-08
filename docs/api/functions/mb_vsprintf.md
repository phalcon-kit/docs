
Return a formatted string
It should work with any "ASCII preserving" encoding such as UTF-8 and all the ISO-8859 charsets.

It handles sign, padding, alignment, width and precision. Argument swapping is not handled.
Works with all encodings in format and arguments.
Supported: Sign, padding, alignment, width and precision.
Not supported: Argument swapping.

***

* Full name: `mb_vsprintf`
* Defined in: `src/Functions/Sprintf.php`

**See Also:**

* http://php.net/manual/en/function.sprintf.php#89020

## Parameters

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$format`   | **string**  |             |
| `$argv`     | **array**   |             |
| `$encoding` | **?string** |             |

## Return Value

**string**
