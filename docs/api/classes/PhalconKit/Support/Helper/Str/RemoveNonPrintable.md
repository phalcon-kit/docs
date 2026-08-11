
Remove non-printable characters from text.

The helper uses multibyte regular expressions so callers can customize the
character class without losing UTF-8 behavior. By default it strips control
characters and line endings.

***

* Full name: `\PhalconKit\Support\Helper\Str\RemoveNonPrintable`

## Methods

### __invoke

Replace characters matching the non-printable regex.

```php
public __invoke(string $string, string $nonPrintableRegex = '[[:cntrl:]' . \PhalconKit\Support\Helper\Str\PHP_EOL . ']', string $replacement = ''): string
```

**Parameters:**

| Parameter            | Type       | Description                                    |
|----------------------|------------|------------------------------------------------|
| `$string`            | **string** | Input text.                                    |
| `$nonPrintableRegex` | **string** | Multibyte regex passed to
`mb_ereg_replace()`. |
| `$replacement`       | **string** | Replacement text for matched characters.       |

**Return Value:**

Sanitized text, or an empty string when replacement fails.

***
