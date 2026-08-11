
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

**Throws:**

When the PHP intl transliterator cannot be
created or transliteration fails.
- [`ServiceException`](../Exception/ServiceException.md)

***

### createTransliterator

Creates the ICU transliterator used by slug generation.

```php
private static createTransliterator(string $identifier): \Transliterator
```

Keeping this in one place gives callers a stable framework exception when
the intl extension is missing or ICU rejects the transliterator rule set.

* This method is **static**.
**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$identifier` | **string** |             |

**Throws:**

When the transliterator class or identifier is
not available.
- [`ServiceException`](../Exception/ServiceException.md)

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
