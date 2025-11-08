
***

* Full name: `\PhalconKit\Support\Slug`

## Methods

### generate

Generates a cleaned and formatted string by performing transliteration, replacements, and normalization.

```php
public static generate(string $string, array $replace = [], string $delimiter = '-'): string
```

- Transliterates characters to Latin equivalents.
- Replaces specified substrings in the input string.
- Cleans the string and normalizes it using a specified delimiter.
- Creates a slug to be used for pretty URLs

* This method is **static**.
**Parameters:**

| Parameter    | Type       | Description                                                                                                         |
|--------------|------------|---------------------------------------------------------------------------------------------------------------------|
| `$string`    | **string** | The input string to be transformed.                                                                                 |
| `$replace`   | **array**  | An associative array of substrings to replace, where keys are substrings to find and values are their replacements. |
| `$delimiter` | **string** | The character to use as a replacement for unwanted characters in the string.                                        |

**Return Value:**

The transformed, cleaned, and formatted string.

***

### restoreLocale

Restore the locale settings based on the provided old locale.

```php
private static restoreLocale(string|string[] $oldLocale): void
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                 | Description                                                                                                                                                  |
|--------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$oldLocale` | **string\|string[]** | The old locale settings.
Can be either a string or an array of locale settings.
If a string, it will be parsed and converted to an array of locale settings. |

***

### cleanString

Cleans a given string by normalizing it to a specific format and replacing unwanted characters with a specified delimiter.

```php
public static cleanString(string $string, string $delimiter): string
```

- Replace non-letter or non-digits by "-"
- Trim trailing "-"

* This method is **static**.
**Parameters:**

| Parameter    | Type       | Description                                                                  |
|--------------|------------|------------------------------------------------------------------------------|
| `$string`    | **string** | The input string to be cleaned.                                              |
| `$delimiter` | **string** | The character to use as a replacement for unwanted characters in the string. |

**Return Value:**

The cleaned and formatted string.

***
