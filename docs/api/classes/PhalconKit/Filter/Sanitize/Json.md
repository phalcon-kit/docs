
Sanitizer that keeps only syntactically valid JSON strings.

This sanitizer does not decode, normalize, or re-encode JSON. It returns the
original string when `json_validate()` accepts it, returns `null` for invalid
JSON, and preserves `null` input as `null`. That makes it suitable for fields
that store raw JSON while still rejecting malformed payloads.

***

* Full name: `\PhalconKit\Filter\Sanitize\Json`

## Methods

### __invoke

Validate and return a raw JSON string.

```php
public __invoke(string|null $input = null): string|null
```

**Parameters:**

| Parameter | Type             | Description            |
|-----------|------------------|------------------------|
| `$input`  | **string\|null** | Candidate JSON string. |

**Return Value:**

The original JSON string, or null for invalid/null
input.

***
