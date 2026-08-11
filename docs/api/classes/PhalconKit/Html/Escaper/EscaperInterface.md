
Escaper contract with PhalconKit's JSON attribute escaping helper.

Services typed against this interface can use every native Phalcon escaper
method plus `json()`, which is required by PhalconKit tag helpers when
embedding structured payloads in HTML attributes.

***

* Full name: `\PhalconKit\Html\Escaper\EscaperInterface`
* Parent interfaces:
  `EscaperInterface`

## Methods

### json

Escape a JSON payload for safe embedding in an HTML attribute.

```php
public json(mixed|null $json = null): string
```

**Parameters:**

| Parameter | Type            | Description                                                                              |
|-----------|-----------------|------------------------------------------------------------------------------------------|
| `$json`   | **mixed\|null** | JSON string or scalar value to encode. Null is
represented as the literal string `null`. |

**Return Value:**

Raw-url-encoded JSON payload.

***
