
Sanitizer for md5-style lowercase hexadecimal strings.

The sanitizer strips every character outside `0-9` and `a-f`. It does not
hash the input and it does not validate that the remaining value is exactly
32 characters long, so callers that need a strict md5 digest should combine
this sanitizer with a length or pattern validator.

***

* Full name: `\PhalconKit\Filter\Sanitize\Md5`

## Methods

### __invoke

Keep only lowercase hexadecimal characters from the input.

```php
public __invoke(string $input): string|null
```

**Parameters:**

| Parameter | Type       | Description                |
|-----------|------------|----------------------------|
| `$input`  | **string** | Candidate token or digest. |

**Return Value:**

Sanitized lowercase hex characters, or null if the
underlying regular-expression engine reports an error.

***
