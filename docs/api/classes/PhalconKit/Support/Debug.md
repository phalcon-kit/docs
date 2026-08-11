
Customizes Phalcon's debug renderer for PhalconKit applications.

The renderer keeps Phalcon's native exception/debug page behavior but adds
current-version documentation links, PhalconKit API links, and a compact
responsive layout for large stack traces. The output is intended for
development/debug environments only; production error handlers should not
expose this HTML to end users.

***

* Full name: `\PhalconKit\Support\Debug`
* Parent class: [`Debug`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

Install PhalconKit's inline renderer on the native 5.16+ debug pipeline.

```php
public __construct(): mixed
```

***

### onUncaughtException

Render an uncaught exception debug page with a server-error status.

```php
public onUncaughtException(\Throwable $exception): bool
```

Phalcon's native debug renderer writes the HTML page but does not
consistently update PHP's active response code. In browser/dev-server
workflows that means a fatal controller error can be shown to developers
while the HTTP response still reports `200 OK`. Setting the status before
delegating keeps debug output useful without lying to clients, upload
widgets, or test harnesses that rely on the transport status.

**Parameters:**

| Parameter    | Type           | Description |
|--------------|----------------|-------------|
| `$exception` | **\Throwable** |             |

***

### setUncaughtExceptionStatusCode

Set the transport status used by uncaught-exception debug output.

```php
protected setUncaughtExceptionStatusCode(): void
```

The debug page is only reached for exceptions that escaped normal
controller/dispatcher handling. Treating those as `500` is the safest
default: expected REST validation failures should be converted to
framework responses before this point, while uncaught throwables represent
server-side failures even when their exception code happens to contain a
different integer.

***

### getVersion

Return version links for PhalconKit and the active Phalcon runtime.

```php
public getVersion(): string
```

The Phalcon documentation link is generated from the installed major and
medium version so local debug pages do not drift when the framework
dependency is upgraded.

**Return Value:**

HTML fragment rendered in Phalcon's debug footer.

***

### renderHtml

Rewrite Phalcon debug HTML with stable docs/API links and table markup.

```php
public renderHtml(\Throwable $exception): string
```

Native Phalcon debug output contains versioned API links and some table
header markup that is awkward to style. This method normalizes those
fragments, adds links for PhalconKit class names, and fails with a scoped
framework exception if one of the internal regex rewrites unexpectedly
fails.

**Parameters:**

| Parameter    | Type           | Description |
|--------------|----------------|-------------|
| `$exception` | **\Throwable** |             |

**Throws:**

When an internal debug HTML rewrite fails.
- [`RuntimeException`](../Exception/RuntimeException.md)

***

### normalizeBacktraceFrames

Keep backtrace metadata visible while only the source block expands.

```php
private static normalizeBacktraceFrames(string $html): string
```

Phalcon 5.16+ renders each frame as a `<details>` element, which hides the
file and line number when a frame is collapsed. PhalconKit keeps the frame
header and file path visible, then moves source context into its own
expandable region. When the source file is readable and reasonably sized,
a hidden full-file template is also embedded for the inline toggle button.

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$html`   | **string** |             |

**Throws:**

When an internal debug HTML rewrite fails.
- [`RuntimeException`](../Exception/RuntimeException.md)

***

### normalizeBacktraceFrame

Normalize one native debug frame after the frame boundary is known.

```php
private static normalizeBacktraceFrame(string $openingTag, string $body, string $originalFrame): string
```

Frame extraction intentionally avoids a document-wide regex so large
backtraces cannot exhaust PCRE backtracking before the per-frame rewrite
runs. If Phalcon changes the opening tag shape, the original frame is
preserved instead of dropping debug output.

* This method is **static**.
**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$openingTag`    | **string** |             |
| `$body`          | **string** |             |
| `$originalFrame` | **string** |             |

**Throws:**

When an internal frame rewrite fails.
- [`RuntimeException`](../Exception/RuntimeException.md)

***

### makeBacktraceFrameHeadToggle

Turn the native frame header into the source-context toggle.

```php
private static makeBacktraceFrameHeadToggle(string $head, bool $isOpen): string
```

The path row remains outside the toggle so file and line metadata stay
visible even when source context is collapsed.

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$head`   | **string** |             |
| `$isOpen` | **bool**   |             |

**Throws:**

When the rewrite failed.
- [`RuntimeException`](../Exception/RuntimeException.md)

***

### readHtmlAttribute

Read an HTML attribute value from a native debug fragment.

```php
private static readHtmlAttribute(string $html, string $attribute): ?string
```

* This method is **static**.
**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$html`      | **string** |             |
| `$attribute` | **string** |             |

***

### buildFullFileSourceTemplate

Build a hidden full-file source table for the inline source toggle.

```php
private static buildFullFileSourceTemplate(?string $file, ?int $line): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$file`   | **?string** |             |
| `$line`   | **?int**    |             |

***

### requireRenderedHtml

Require an internal debug rewrite to return rendered HTML.

```php
private static requireRenderedHtml(string|array|null $html, string $operation): string
```

`preg_replace()` and `preg_replace_callback()` return null on regex
failures and can return arrays when the subject is an array. This class
always rewrites a string subject, so anything other than a string means
PhalconKit's debug renderer is misconfigured or has drifted from the
native Phalcon output shape.

* This method is **static**.
**Parameters:**

| Parameter    | Type                    | Description |
|--------------|-------------------------|-------------|
| `$html`      | **string\|array\|null** |             |
| `$operation` | **string**              |             |

**Throws:**

When the rewrite failed.
- [`RuntimeException`](../Exception/RuntimeException.md)

***

### getCssSources

Return the CSS injected into Phalcon's debug page.

```php
public getCssSources(): string
```

The stylesheet intentionally avoids external assets so debug pages remain
useful when the asset pipeline, router, or public document root is broken.

***

### getJsSources

Return the JavaScript injected into Phalcon's debug page.

```php
public getJsSources(): string
```

The script progressively enhances the native debug output: tabs are only
activated when the expected markup exists, and source previews collapse
large files around the highlighted line without requiring external
dependencies.

***
