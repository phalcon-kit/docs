
***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Position`
* Parent class: [`Behavior`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Properties

### progress

```php
public bool $progress
```

***

## Methods

### setField

```php
public setField(string $field): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

***

### getField

```php
public getField(): string
```

***

### setRawSql

```php
public setRawSql(bool $rawSql): void
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$rawSql` | **bool** |             |

***

### getRawSql

```php
public getRawSql(): bool
```

***

### hasProperty

```php
public hasProperty(\Phalcon\Mvc\ModelInterface $model, string $field): bool
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |
| `$field`  | **string**                      |             |

***

### __construct

```php
public __construct(array $options = []): mixed
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$options` | **array** |             |

***

### notify

Set the default position field value before validation
Shift position+1 and position-1 to other records after save

```php
public notify(string $type, \Phalcon\Mvc\ModelInterface $model): ?bool
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$type`   | **string**                      |             |
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |

***

### beforeValidation

Force the current position to max(position)+1 if it's empty
will only happen if the position field is present on the current model

```php
public beforeValidation(\Phalcon\Mvc\ModelInterface $model, string $field): void
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |
| `$field`  | **string**                      |             |

***

### afterSave

```php
public afterSave(\Phalcon\Mvc\ModelInterface $model, string $field, bool $rawSql): void
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |
| `$field`  | **string**                      |             |
| `$rawSql` | **bool**                        |             |

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

### getProgress

Return true if the behavior is progress
on the current model instance

```php
public getProgress(): bool
```

***

### setProgress

Set true to enable the behavior
on the current model instance

```php
public setProgress(bool $progress): void
```

**Parameters:**

| Parameter   | Type     | Description |
|-------------|----------|-------------|
| `$progress` | **bool** |             |

***

### getStaticProgress

Return true if the behavior is progress
globally for every model instance

```php
public static getStaticProgress(): bool
```

* This method is **static**.
***

### setStaticProgress

Set true to enable the behavior
globally for every model instance

```php
public static setStaticProgress(bool $staticProgress): void
```

* This method is **static**.
**Parameters:**

| Parameter         | Type     | Description |
|-------------------|----------|-------------|
| `$staticProgress` | **bool** |             |

***

### start

Enable the behavior
on the current model instance

```php
public start(): void
```

***

### stop

Disable the behavior
on the current model instance

```php
public stop(): void
```

***

### staticStart

Enable the behavior
globally for every model instance

```php
public static staticStart(): void
```

* This method is **static**.
***

### staticStop

Disable the behavior
globally for every model instance

```php
public static staticStop(): void
```

* This method is **static**.
***

### inProgress

Return true if the behavior is in progress
on the current model instance and globally

```php
public inProgress(): bool
```

***

### isStarted

Return true if the behavior is started
on the current model instance and globally

```php
public isStarted(): bool
```

***

### isStopped

Return true if the behavior is stopped
on the current model instance and globally

```php
public isStopped(): bool
```

***
