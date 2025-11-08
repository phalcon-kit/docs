
Allow to enable or disable trait
on the current model instance ($progress)
or globally for every model instance ($staticProgress)

***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Traits\ProgressTrait`

## Properties

### progress

```php
public bool $progress
```

***
### staticProgress

```php
public static bool $staticProgress
```

* This property is **static**.

***

## Methods

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
