
The EventsAwareTrait provides methods for managing events within a class.

***

* Full name: `\PhalconKit\Events\EventsAwareTrait`

## Properties

### eventsPrefix

Event prefix to use as a component
my-component:beforeSomeTask
my-component:afterSomeTask

```php
public static ?string $eventsPrefix
```

* This property is **static**.

***
### eventsManager

The event manager responsible for handling and triggering events.

```php
protected ?\Phalcon\Contracts\Events\Manager $eventsManager
```

***

## Methods

### setEventsManager

Set the events manager

```php
public setEventsManager(\Phalcon\Contracts\Events\Manager $manager): void
```

**Parameters:**

| Parameter  | Type                                  | Description |
|------------|---------------------------------------|-------------|
| `$manager` | **\Phalcon\Contracts\Events\Manager** |             |

***
### getEventsManager

Get the events manager.

```php
public getEventsManager(): ?\Phalcon\Contracts\Events\Manager
```

***
### getEventsPrefix

Get the event component prefix

```php
public static getEventsPrefix(): string|null
```

* This method is **static**.
**Return Value:**

The event component prefix, or null if not set

***
### setEventsPrefix

Sets the events prefix.

```php
public static setEventsPrefix(string|null $eventsPrefix): void
```

* This method is **static**.
**Parameters:**

| Parameter       | Type             | Description                                                       |
|-----------------|------------------|-------------------------------------------------------------------|
| `$eventsPrefix` | **string\|null** | The prefix to be used for events. Pass null to remove the prefix. |

***
### fire

Fire an event.

```php
public fire(string $task, mixed|null $data = null, bool $cancelable = false, bool|null $stopOnFalse = null): mixed
```

A non-null stop-on-false override is supported by Phalcon's native
manager without changing its global setting.

**Parameters:**

| Parameter      | Type            | Description                                                |
|----------------|-----------------|------------------------------------------------------------|
| `$task`        | **string**      | The task to execute.                                       |
| `$data`        | **mixed\|null** | The optional data to pass to the event.                    |
| `$cancelable`  | **bool**        | Whether the event is cancelable or not. Defaults to false. |
| `$stopOnFalse` | **bool\|null**  | Per-call override; null uses the manager setting.          |

**Throws:**

When the events manager is missing, or
when a per-call stop-on-false override is requested from a custom
manager that does not support Phalcon 5.20.3's fifth argument.
- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***
