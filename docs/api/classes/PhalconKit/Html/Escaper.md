
HTML escaper with PhalconKit JSON-attribute support.

The class keeps Phalcon's native HTML/CSS/JS escaping behavior and adds a
`json()` helper used by PhalconKit tag helpers for safely embedding JSON
payloads in HTML attributes. The JSON helper raw-url-encodes the payload so a
client can decode it with `decodeURIComponent()` before parsing.

Like Phalcon's escaper, this component is intended for UTF-8 content. The
PREG extension must have UTF-8 support enabled.

```php
$escaper = new \PhalconKit\Html\Escaper();

$escaped = $escaper->json('{"name":"Ada"}');

echo $escaped; // %%7B%%22name%%22%%3A%%22Ada%%22%%7D
```

***

* Full name: `\PhalconKit\Html\Escaper`
* Parent class: [`Escaper`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Html\Escaper\EscaperInterface`](./Escaper/EscaperInterface.md)

**See Also:**

* \Phalcon\Html\Escaper

## Methods

### json

Escape a JSON payload for safe embedding in an HTML attribute.

```php
public json(mixed|null $json = null): string
```

Pass an already encoded JSON string when possible. If the value is a
scalar that is not valid JSON, it is JSON-encoded as a scalar before raw
URL encoding. Raw arrays and objects are not accepted by the current
contract because `json_validate()` requires a string input before the
fallback `json_encode()` branch is reached.

JavaScript can decode and parse values like this:
```js
JSON.parse(decodeURIComponent(encodedValue))
```

**Parameters:**

| Parameter | Type            | Description                                                                              |
|-----------|-----------------|------------------------------------------------------------------------------------------|
| `$json`   | **mixed\|null** | JSON string or scalar value to encode. Null is
represented as the literal string `null`. |

**Return Value:**

Raw-url-encoded JSON payload.

***
