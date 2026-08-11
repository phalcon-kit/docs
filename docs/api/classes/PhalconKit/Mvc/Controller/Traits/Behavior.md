
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Behavior`

## Methods

### beforeExecuteRoute

```php
public beforeExecuteRoute(): void
```

***
### attachBehavior

Attach a behavior to the object.

```php
public attachBehavior(string $eventClass, string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter     | Type             | Description                                                                                                 |
|---------------|------------------|-------------------------------------------------------------------------------------------------------------|
| `$eventClass` | **string**       | The behavior to attach.                                                                                     |
| `$eventType`  | **string\|null** | The event type to attach the behavior to. If null, the behavior will be attached to the default event type. |
| `$priority`   | **int\|null**    | The priority of the behavior. If null, the behavior will be attached with the default priority.             |

***
### attachBehaviors

Attach multiple behaviors to the object.

```php
public attachBehaviors(array $behaviors = [], string|null $eventType = null, int|null $priority = null): void
```

**Parameters:**

| Parameter    | Type             | Description                                                                                            |
|--------------|------------------|--------------------------------------------------------------------------------------------------------|
| `$behaviors` | **array**        | An array of behaviors to attach.                                                                       |
| `$eventType` | **string\|null** | The event type to attach the behaviors to. If null, the behaviors will be attached to all event types. |
| `$priority`  | **int\|null**    | The priority of the behaviors. If null, the behaviors will be attached with the default priority.      |

***
### getOrCreateEventsManager

```php
protected getOrCreateEventsManager(): \Phalcon\Contracts\Events\Manager
```

***
### attachConfiguredBehaviors

Attach legacy, non-action-scoped behavior config for this controller/model.

```php
private attachConfiguredBehaviors(array<string|int,mixed> $behaviorsContext, array<int,string> $handlerCandidates, ?string $modelName): void
```

**Parameters:**

| Parameter            | Type                         | Description                    |
|----------------------|------------------------------|--------------------------------|
| `$behaviorsContext`  | **array<string\|int,mixed>** | Permission behavior map.       |
| `$handlerCandidates` | **array<int,string>**        | Controller class/name aliases. |
| `$modelName`         | **?string**                  |                                |

***
### attachConfiguredActionBehaviors

Attach action-scoped controller/model behavior config for this request.

```php
private attachConfiguredActionBehaviors(array<string|int,mixed> $behaviorActionsContext, array<int,string> $handlerCandidates, array<int,string> $actionCandidates, ?string $modelName): void
```

**Parameters:**

| Parameter                 | Type                         | Description                    |
|---------------------------|------------------------------|--------------------------------|
| `$behaviorActionsContext` | **array<string\|int,mixed>** | Action behavior map.           |
| `$handlerCandidates`      | **array<int,string>**        | Controller class/name aliases. |
| `$actionCandidates`       | **array<int,string>**        | Current action aliases.        |
| `$modelName`              | **?string**                  |                                |

***
### getBehaviorHandlerCandidates

```php
private getBehaviorHandlerCandidates(): array<int,string>
```

***
### getBehaviorActionCandidates

```php
private getBehaviorActionCandidates(): array<int,string>
```

***
### getBehaviorDispatcher

```php
private getBehaviorDispatcher(): ?\Phalcon\Dispatcher\AbstractDispatcher
```

***
### usesControllerAttributes

Determine whether controller attributes should augment permission config.

```php
private usesControllerAttributes(): bool
```

***
