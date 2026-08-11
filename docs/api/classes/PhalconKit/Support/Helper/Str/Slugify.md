
Create URL-friendly slugs through the shared slug generator.

This helper exposes

- **See:** \PhalconKit\Support\Slug::generate() through the helper factory and
static helper facade, so application code can call `Helper::slugify()` or
resolve the helper service directly.

***

* Full name: `\PhalconKit\Support\Helper\Str\Slugify`

## Methods

### __invoke

Generate a normalized slug.

```php
public __invoke(string $string, array<string,string> $replace = [], string $delimiter = '-'): string
```

**Parameters:**

| Parameter    | Type                     | Description                                       |
|--------------|--------------------------|---------------------------------------------------|
| `$string`    | **string**               | Source text.                                      |
| `$replace`   | **array<string,string>** | Search/replace pairs applied before
slug cleanup. |
| `$delimiter` | **string**               | Word delimiter used in the final slug.            |

***
