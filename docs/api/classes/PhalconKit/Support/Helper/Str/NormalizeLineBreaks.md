
Normalize line-break sequences in text.

The default pattern converts CRLF and old Mac CR line breaks to LF while
leaving existing LF characters untouched. Callers can pass a custom regex and
replacement when they need a different normalization policy.

***

* Full name: `\PhalconKit\Support\Helper\Str\NormalizeLineBreaks`

## Methods

### __invoke

Replace matching line-break sequences.

```php
public __invoke(string $string, string $lineBreaksRegex = "/\r\n|\r/", string $replacement = "\n"): string
```

**Parameters:**

| Parameter          | Type       | Description                                                                                             |
|--------------------|------------|---------------------------------------------------------------------------------------------------------|
| `$string`          | **string** | The input string where line breaks will be replaced.                                                    |
| `$lineBreaksRegex` | **string** | Regex passed to `preg_replace()`. An empty
string disables replacement and returns the input unchanged. |
| `$replacement`     | **string** | Replacement text for matched line breaks.                                                               |

**Return Value:**

The processed string with line breaks replaced.

***
