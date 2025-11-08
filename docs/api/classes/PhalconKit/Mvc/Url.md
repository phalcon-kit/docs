
{@inheritDoc}

***

* Full name: `\PhalconKit\Mvc\Url`
* Parent class: [`Url`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### get

{@inheritdoc}

```php
public get(array|string|null $uri = null, mixed $args = null, bool|null $local = null, mixed $baseUri = null): string
```

**Parameters:**

| Parameter  | Type                    | Description |
|------------|-------------------------|-------------|
| `$uri`     | **array\|string\|null** |             |
| `$args`    | **mixed**               |             |
| `$local`   | **bool\|null**          |             |
| `$baseUri` | **mixed**               |             |

***

### getAbsolutePath

Returns the absolute path from the given path.

```php
public static getAbsolutePath(string $path): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description                              |
|-----------|------------|------------------------------------------|
| `$path`   | **string** | The path to convert to an absolute path. |

**Return Value:**

The absolute path.

***
