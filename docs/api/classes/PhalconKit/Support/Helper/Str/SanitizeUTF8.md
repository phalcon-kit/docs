
Sanitize and convert to UTF-8

***

* Full name: `\PhalconKit\Support\Helper\Str\SanitizeUTF8`

## Methods

### __invoke

Invokes the function to sanitize a given string by detecting its encoding,
converting it to UTF-8, and removing invalid UTF-8 characters.

```php
```

**Parameters:**

| Parameter           | Type       | Description                                                                                              |
|---------------------|------------|----------------------------------------------------------------------------------------------------------|
| `$string`           | **string** | The input string to be sanitized.                                                                        |
| `$invalidUtf8Regex` | **string** | A regular expression pattern to identify invalid UTF-8 characters. Default: '[^\\x20-\\x7E\\xA0-\\xFF]'. |

**Return Value:**

The sanitized string in UTF-8 encoding, with invalid characters removed.

***
