
Normalize Line Breaks

***

* Full name: `\PhalconKit\Support\Helper\Str\NormalizeLineBreaks`

## Methods

### __invoke

Replaces line breaks in the given string based on a specified regular expression and replacement string.

```php
public __invoke(string $string, string $lineBreaksRegex = "/
|/", string $replacement = "
"): string
```

**Parameters:**

| Parameter          | Type       | Description                                                                    |
|--------------------|------------|--------------------------------------------------------------------------------|
| `$string`          | **string** | The input string where line breaks will be replaced.                           |
| `$lineBreaksRegex` | **string** | The regular expression pattern to match line breaks. Defaults to "/\r\n\|\r/". |
| `$replacement`     | **string** | The string to replace matched line breaks with. Defaults to "\n".              |

**Return Value:**

The processed string with line breaks replaced.

***
