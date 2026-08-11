
Contract for switching an authenticated session into and out of impersonation.

***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\ImpersonationInterface`

## Methods

### loginAs

Impersonate another user while preserving the original user id.

```php
public loginAs(array<string,mixed> $params = []): array<string,mixed>
```

**Parameters:**

| Parameter | Type                    | Description                                |
|-----------|-------------------------|--------------------------------------------|
| `$params` | **array<string,mixed>** | Parameters containing the target
`userId`. |

**Return Value:**

Login state, validation messages, and
optional JWT values when stateless identity mode changes the token
payload.

***

### logoutAs

Restore the original user stored in the impersonation session payload.

```php
public logoutAs(): array{loggedIn: bool, loggedInAs: bool, jwt?: string, refreshToken?: string, refreshed?: bool}
```

***
