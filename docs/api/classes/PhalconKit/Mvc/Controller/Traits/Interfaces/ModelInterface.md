
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\ModelInterface`

## Methods

### getModelName

```php
public getModelName(): ?string
```

***

### setModelName

```php
public setModelName(?string $modelName = null): void
```

**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$modelName` | **?string** |             |

***

### getModelNamespaces

```php
public getModelNamespaces(): array
```

***

### setModelNamespaces

```php
public setModelNamespaces(?array $modelNamespaces = []): void
```

**Parameters:**

| Parameter          | Type       | Description |
|--------------------|------------|-------------|
| `$modelNamespaces` | **?array** |             |

***

### getModelNameFromController

```php
public getModelNameFromController(?array $namespaces = null, string $needle = 'Models'): ?string
```

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

***

### loadModel

```php
public loadModel(?string $modelName = null): \Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$modelName` | **?string** |             |

***
