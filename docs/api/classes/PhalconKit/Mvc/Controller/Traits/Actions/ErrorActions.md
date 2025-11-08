
Default Error Actions

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\ErrorActions`

## Methods

### errorAction

Http Status Code - Generic
error

```php
public errorAction(?int $code = null, ?string $message = null): void
```

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$code`    | **?int**    |             |
| `$message` | **?string** |             |

***
### badRequestAction

Http Status Code 400
bad-request

```php
public badRequestAction(): void
```

***
### unauthorizedAction

Http Status Code 401
unauthorized

```php
public unauthorizedAction(): void
```

***
### forbiddenAction

Http Status Code 403
forbidden

```php
public forbiddenAction(): void
```

***
### notFoundAction

Http Status Code 404
not-found

```php
public notFoundAction(): void
```

***
### fatalAction

Http Status Code 500
fatal

```php
public fatalAction(): void
```

***
### maintenanceAction

Http Status Code 503
maintenance

```php
public maintenanceAction(): void
```

***
