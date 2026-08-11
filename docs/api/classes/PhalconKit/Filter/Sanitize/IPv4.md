
Sanitizer that accepts only valid IPv4 address strings.

Valid IPv4 values are returned unchanged. Invalid input, `null`, and valid
addresses from the wrong family return an empty string, matching Phalcon's
common sanitizer pattern where failed scalar sanitization collapses to an
empty form value.

***

* Full name: `\PhalconKit\Filter\Sanitize\IPv4`

## Methods

### __invoke

Validate and return an IPv4 address.

```php
public __invoke(string|null $input = null): string
```

**Parameters:**

| Parameter | Type             | Description                                  |
|-----------|------------------|----------------------------------------------|
| `$input`  | **string\|null** | Candidate address from request/config input. |

**Return Value:**

The original IPv4 address, or an empty string when invalid.

***
