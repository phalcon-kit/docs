
Renders Phalcon 5.16+ debug reports with PhalconKit's inline theme.

Phalcon 5.16 moved debug output behind a renderer/template contract. This
renderer uses that contract directly so debug pages do not load remote
assets and so PhalconKit's theme stays attached to the active render path.

***

* Full name: `\PhalconKit\Support\Debug\Renderer\HtmlRenderer`
* Parent class: [`HtmlRenderer`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

```php
public __construct(): mixed
```

***

### getLogoDataUri

```php
private getLogoDataUri(): string
```

***

### getCssSources

Return inline CSS for PhalconKit's debug page theme.

```php
public getCssSources(string $uri): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$uri`    | **string** |             |

***

### getJsSources

Return inline JavaScript for tabs, theme toggling, and source previews.

```php
public getJsSources(string $uri): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$uri`    | **string** |             |

***

### getVersion

Return a PhalconKit-aware version badge for the inline debug header.

```php
public getVersion(): string
```

***
