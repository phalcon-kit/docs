
PhalconKit\Html\Escaper

Escapes different kinds of text securing them. By using this component you
may prevent XSS attacks.

This component only works with UTF-8. The PREG extension needs to be compiled
with UTF-8 support.

```php
$escaper = new \Phalcon\Html\Escaper();

$escaped = $escaper->escapeCss("font-family: <Verdana>");

echo $escaped; // font\2D family\3A \20 \3C Verdana\3E
```

***

* Full name: `\PhalconKit\Html\Escaper`
* Parent class: [`Escaper`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Html\Escaper\EscaperInterface`](./Escaper/EscaperInterface.md)

## Methods

### json

Escapes a JSON string by raw URL encoding it.

```php
public json(mixed|null $json = null): string
```

JS side could decode and parse this way:
JSON.parse(decodeURIComponent('<?= $this->escaper->json([]);?>'));

**Parameters:**

| Parameter | Type            | Description                                                     |
|-----------|-----------------|-----------------------------------------------------------------|
| `$json`   | **mixed\|null** | The JSON string to escape. If null, an empty string is escaped. |

**Return Value:**

Returns the raw URL encoded JSON string.

***
