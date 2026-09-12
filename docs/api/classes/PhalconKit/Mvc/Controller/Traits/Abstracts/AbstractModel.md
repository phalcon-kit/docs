
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\AbstractModel`

## Methods

### getModelName

```php
public getModelName(): ?string
```

* This method is **abstract**.
***
### setModelName

```php
public setModelName(?string $modelName): void
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$modelName` | **?string** |             |

***
### getModelNamespaces

```php
public getModelNamespaces(): array
```

* This method is **abstract**.
***
### setModelNamespaces

```php
public setModelNamespaces(?array $modelNamespaces): void
```

* This method is **abstract**.
**Parameters:**

| Parameter          | Type       | Description |
|--------------------|------------|-------------|
| `$modelNamespaces` | **?array** |             |

***
### getModelNameFromController

```php
public getModelNameFromController(?array $namespaces = null, string $needle = 'Models'): ?string
```

* This method is **abstract**.
**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$namespaces` | **?array** |             |
| `$needle`     | **string** |             |

***
### getControllerName

```php
public getControllerName(): string
```

* This method is **abstract**.
***
### loadModel

```php
public loadModel(?string $modelName = null): \Phalcon\Mvc\ModelInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$modelName` | **?string** |             |

***
### modelHasColumn

```php
public modelHasColumn(string $column, ?string $modelName = null): bool
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$column`    | **string**  |             |
| `$modelName` | **?string** |             |

***
### assertRequestField

Reject request field selectors containing PHQL expressions with HTTP 400.

```php
protected assertRequestField(string $field): void
```

Implementations must accept identifiers and supported relation scopes only.

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

***
### appendModelName

```php
public appendModelName(string $field, ?string $modelName = null): string
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$field`     | **string**  |             |
| `$modelName` | **?string** |             |

***
