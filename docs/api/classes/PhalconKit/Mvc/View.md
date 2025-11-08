
{@inheritdoc}

***

* Full name: `\PhalconKit\Mvc\View`
* Parent class: [`View`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Properties

### minify

```php
private bool $minify
```

***

## Methods

### getMinify

True if content minifier is enabled

```php
public getMinify(): bool
```

***

### setMinify

Set true to enable content minifier

```php
public setMinify(bool $minify): void
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$minify` | **bool** |             |

***

### render

{@inheritdoc}

```php
public render(string $controllerName, string $actionName, array $params = []): \Phalcon\Mvc\View|bool
```

**Parameters:**

| Parameter         | Type       | Description |
|-------------------|------------|-------------|
| `$controllerName` | **string** |             |
| `$actionName`     | **string** |             |
| `$params`         | **array**  |             |

***

### getRender

Perform the automatic rendering returning the output as a string

```php
public getRender(string $controllerName, string $actionName, array $params = [], mixed $configCallback = null): string
```



- **See:** 

**Parameters:**

| Parameter         | Type       | Description |
|-------------------|------------|-------------|
| `$controllerName` | **string** |             |
| `$actionName`     | **string** |             |
| `$params`         | **array**  |             |
| `$configCallback` | **mixed**  |             |

***

### getContent

Returns output from another view stage
Can also minify the content

```php
public getContent(?bool $minify = null): string
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$minify` | **?bool** |             |

***
