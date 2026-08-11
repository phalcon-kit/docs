
Applies configured attribute transformations during model lifecycle events.

Each watched event can define a field-to-value map. Values may be scalars or
callbacks; callbacks receive the model and field name on the first pass and
may return another callback for deferred value generation. The final value is
written through Phalcon's entity API so column maps and model internals stay
consistent.

***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Transformable`
* Parent class: [`Behavior`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/latest/db-models-events/

## Methods

### notify

Handle a model manager lifecycle notification.

```php
public notify(string $type, \Phalcon\Mvc\ModelInterface $model): bool|null
```

**Parameters:**

| Parameter | Type                            | Description                                    |
|-----------|---------------------------------|------------------------------------------------|
| `$type`   | **string**                      | Event name emitted by Phalcon's model manager. |
| `$model`  | **\Phalcon\Mvc\ModelInterface** | Model receiving transformed values.            |

**Return Value:**

True when a configured transformation ran, null when
the behavior is disabled, does not match the event, or has no work.

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
