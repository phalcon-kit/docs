
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
