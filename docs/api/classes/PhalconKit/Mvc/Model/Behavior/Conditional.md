
PhalconKit\Mvc\Model\Traits\Behavior\Conditional

Allows to automatically update a model’s attribute saving the datetime when a
record is created or updated

***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Conditional`
* Parent class: [`Behavior`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### notify

Listens for notifications from the models manager

```php
public notify(string $type, \Phalcon\Mvc\ModelInterface $model): ?bool
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$type`   | **string**                      |             |
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |

***

### getOption

```php
public getOption(string $key, array $options, array|null $params = null): mixed|null
```

**Parameters:**

| Parameter  | Type            | Description |
|------------|-----------------|-------------|
| `$key`     | **string**      |             |
| `$options` | **array**       |             |
| `$params`  | **array\|null** |             |

***

## Inherited methods

### getEnabled

Return true if the behavior is enabled
on the current model instance

```php
public getEnabled(): bool
```

***

### setEnabled

Set true to enable the behavior
on the current model instance

```php
public setEnabled(bool $enabled): void
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$enabled` | **bool** |             |

***

### getStaticEnabled

Return true if the behavior is enabled
globally for every model instance

```php
public static getStaticEnabled(): bool
```

* This method is **static**.
***

### setStaticEnabled

Set true to enable the behavior
globally for every model instance

```php
public static setStaticEnabled(bool $staticEnabled): void
```

* This method is **static**.
**Parameters:**

| Parameter        | Type     | Description |
|------------------|----------|-------------|
| `$staticEnabled` | **bool** |             |

***

### enable

Enable the behavior
on the current model instance

```php
public enable(): void
```

***

### disable

Disable the behavior
on the current model instance

```php
public disable(): void
```

***

### staticEnable

Enable the behavior
globally for every model instance

```php
public static staticEnable(): void
```

* This method is **static**.
***

### staticDisable

Disable the behavior
globally for every model instance

```php
public static staticDisable(): void
```

* This method is **static**.
***

### isEnabled

Return true if the behavior is enabled
on the current model instance and globally

```php
public isEnabled(): bool
```

***

### isDisabled

Return true if the behavior is enabled
on the current model instance and globally

```php
public isDisabled(): bool
```

***
