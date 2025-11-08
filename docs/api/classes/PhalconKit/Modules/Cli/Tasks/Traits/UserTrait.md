
***

* Full name: `\PhalconKit\Modules\Cli\Tasks\Traits\UserTrait`

## Properties

### tables

```php
public array $tables
```

***

## Methods

### initialize

```php
public initialize(): void
```

***
### getDefinitions

Retrieves an array of class definitions mapped to their respective configurations.

```php
public getDefinitions(): array<string,array<string,string|callable>>
```

***
### createAction

```php
final public createAction(string $email, ?string $password = null): (array|int|mixed)[]
```

* This method is **final**.
**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$email`    | **string**  |             |
| `$password` | **?string** |             |

***
### roleAction

```php
final public roleAction(string $email, string $role): (array|int|mixed)[]
```

* This method is **final**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$email`  | **string** |             |
| `$role`   | **string** |             |

***
### passwordAction

```php
final public passwordAction(?string $username = null, ?string $password = null): array
```

* This method is **final**.
**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$username` | **?string** |             |
| `$password` | **?string** |             |

***
### addModelsPermissions

```php
public addModelsPermissions(?array $tables = null): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$tables` | **?array** |             |

***
