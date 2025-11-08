
Provides debug capabilities to Phalcon Kit applications

***

* Full name: `\PhalconKit\Support\Debug`
* Parent class: [`Debug`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### getVersion

Returns the version information for Phalcon Kit and Phalcon Framework.

```php
public getVersion(): string
```

**Return Value:**

The version information as HTML string.

***

### renderHtml

Intercept the rendered HTML and rewrite class links.

```php
public renderHtml(\Throwable $exception): string
```

**Parameters:**

| Parameter    | Type           | Description |
|--------------|----------------|-------------|
| `$exception` | **\Throwable** |             |

***

### getCssSources

```php
public getCssSources(): string
```

***

### getJsSources

```php
public getJsSources(): string
```

***
