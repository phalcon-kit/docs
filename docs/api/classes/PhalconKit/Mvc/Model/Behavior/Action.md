
***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Action`
* Parent class: [`Behavior`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### notify

```php
public notify(string $type, \Phalcon\Mvc\ModelInterface $model): void
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$type`   | **string**                      |             |
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |

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
