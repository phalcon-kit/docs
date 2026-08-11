
Normalize input text to UTF-8 and remove invalid characters.

The helper is designed for defensive text cleanup before values are used in
slugs, exports, or generated content. It detects common Western encodings,
converts to UTF-8, then removes characters matching the configured invalid
UTF-8 pattern.

***

* Full name: `\PhalconKit\Support\Helper\Str\SanitizeUTF8`

## Methods

### __invoke

Detect common encodings, convert safely to UTF-8, and strip invalid text.

```php
```

**Parameters:**

| Parameter           | Type       | Description                                                         |
|---------------------|------------|---------------------------------------------------------------------|
| `$string`           | **string** | Input text.                                                         |
| `$invalidUtf8Regex` | **string** | Multibyte regex used to remove invalid
characters after conversion. |

**Return Value:**

UTF-8 text with invalid characters removed.

***
