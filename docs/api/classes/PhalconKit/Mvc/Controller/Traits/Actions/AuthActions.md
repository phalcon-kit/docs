
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\AuthActions`

## Properties

### userExpose

```php
public array $userExpose
```

***

## Methods

### getIdentityAction

Retrieve the current identity information

```php
public getIdentityAction(): bool
```

***
### getJwtAction

Create or refresh a JWT

```php
public getJwtAction(bool $refresh = false): bool
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***
### refreshAction

Refresh an existing JWT

```php
public refreshAction(): bool
```

***
### loginAction

Login

```php
public loginAction(): bool
```

***
### loginAsAction

Login As (impersonation)

```php
public loginAsAction(): bool
```

***
### logoutAction

Logout from current session

```php
public logoutAction(): bool
```

***
### logoutAsAction

Logout from impersonation

```php
public logoutAsAction(): bool
```

***
### resetPasswordAction

Reset Password Action

```php
public resetPasswordAction(): bool
```

***
### getLoginParams

Retrieves login parameters including email and password with applied filters.

```php
public getLoginParams(): array
```

**Return Value:**

Returns an array of login parameters with specified filters applied.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### getResetPasswordParams

Retrieves the parameters required for resetting a password with applied filters.

```php
public getResetPasswordParams(): array
```

**Return Value:**

Returns an array of reset password parameters with specified filters applied.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
