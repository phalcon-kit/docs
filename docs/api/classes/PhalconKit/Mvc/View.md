
MVC view wrapper with PhalconKit path normalization and optional minification.

When a direct controller/action view path is not present, controller and
action names are converted from camelCase to slug form before delegating to
Phalcon. Absolute paths are passed through unchanged so Phalcon's native
path handling remains available. `getContent()` can also perform lightweight
HTML output minification for applications that opt in through `setMinify()`.

***

* Full name: `\PhalconKit\Mvc\View`
* Parent class: [`View`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/5.18/views/

## Properties

### minify

Whether `getContent()` should minify rendered HTML by default.

```php
private bool $minify
```

The flag is intentionally view-local so applications can opt in through
configuration without changing Phalcon's global rendering behavior.

***

## Methods

### getMinify

Return whether response content should be minified by default.

```php
public getMinify(): bool
```

**Return Value:**

True when rendered content should be minified unless a
per-call override is supplied to `getContent()`.

***

### setMinify

Enable or disable response content minification by default.

```php
public setMinify(bool $minify): void
```

**Parameters:**

| Parameter | Type     | Description                                                                                        |
|-----------|----------|----------------------------------------------------------------------------------------------------|
| `$minify` | **bool** | True to minify rendered content returned by
`getContent()` unless the call overrides the behavior. |

***

### render

Render a view, falling back to slugged controller/action paths.

```php
public render(string $controllerName, string $actionName, array<array-key,mixed> $params = []): static|false
```

**Parameters:**

| Parameter         | Type                       | Description                                 |
|-------------------|----------------------------|---------------------------------------------|
| `$controllerName` | **string**                 | Controller name selected by the dispatcher. |
| `$actionName`     | **string**                 | Action name selected by the dispatcher.     |
| `$params`         | **array<array-key,mixed>** | View parameters.                            |

**Return Value:**

Native Phalcon render result.

***

### getRender

Render a view to a string, falling back to slugged paths when needed.

```php
public getRender(string $controllerName, string $actionName, array<array-key,mixed> $params = [], mixed $configCallback = null): string
```

**Parameters:**

| Parameter         | Type                       | Description                                 |
|-------------------|----------------------------|---------------------------------------------|
| `$controllerName` | **string**                 | Controller name selected by the dispatcher. |
| `$actionName`     | **string**                 | Action name selected by the dispatcher.     |
| `$params`         | **array<array-key,mixed>** | View parameters.                            |
| `$configCallback` | **mixed**                  | Optional native Phalcon render callback.    |

***

### isAbsoluteViewPath

Return whether a view path is absolute using Phalcon's platform rules.

```php
private isAbsoluteViewPath(string $path): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getContent

Return rendered output, optionally applying lightweight minification.

```php
public getContent(bool|null $minify = null): string
```

The minifier removes normal HTML comments, single-line JavaScript-style
comments, repeated whitespace, and line breaks. It is intentionally simple
and should be used for conventional rendered views, not as a full HTML,
CSS, or JavaScript optimizer.

**Parameters:**

| Parameter | Type           | Description                                                                    |
|-----------|----------------|--------------------------------------------------------------------------------|
| `$minify` | **bool\|null** | Override the default minification flag for this
call. Null uses `getMinify()`. |

**Return Value:**

Rendered response content.

***
