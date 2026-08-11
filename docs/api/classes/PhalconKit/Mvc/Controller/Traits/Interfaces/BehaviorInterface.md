
Contract for attaching controller behavior listeners.

Behaviors are regular event listeners attached to the controller's events
manager. REST controllers use them to apply role, feature, and model-specific
behavior during request initialization.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\BehaviorInterface`

## Methods

### attachBehavior

Attach one behavior listener class.

```php
public attachBehavior(class-string $eventClass, string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter     | Type             | Description                               |
|---------------|------------------|-------------------------------------------|
| `$eventClass` | **class-string** | Listener class to instantiate or resolve. |
| `$eventType`  | **string\|null** | Event type, usually `rest` or `model`.    |
| `$priority`   | **int\|null**    | Optional event-manager priority.          |

***

### attachBehaviors

Attach multiple behavior listener definitions.

```php
public attachBehaviors(array<int|string,mixed> $behaviors = [], string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter    | Type                         | Description                                          |
|--------------|------------------------------|------------------------------------------------------|
| `$behaviors` | **array<int\|string,mixed>** | Behavior class names or nested
listener definitions. |
| `$eventType` | **string\|null**             | Default event type for class-name entries.           |
| `$priority`  | **int\|null**                | Optional event-manager priority.                     |

***
