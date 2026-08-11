
Implements session-based user impersonation.

The effective `userId` is replaced with the target user while the original
user id is stored in `asUserId`. Calling

- **See:** \PhalconKit\Identity\Traits\logoutAs() restores the
original id. Authorization is currently the legacy admin/dev role check; a
configurable permission contract is tracked as a future design topic.

***

* Full name: `\PhalconKit\Identity\Traits\Impersonation`

## Methods

### loginAs

Switch the current session to another user.

```php
public loginAs(array<string,mixed> $params = []): array{messages?: \Phalcon\Messages\Messages, loggedIn: bool, loggedInAs: bool, jwt?: string, refreshToken?: string, refreshed?: bool}
```

The target `userId` must be present, numeric, and resolvable through the
configured user model. If the target id equals the current `asUserId`, the
method treats the request as a return-to-self action and restores the
original session.

**Parameters:**

| Parameter | Type                    | Description                     |
|-----------|-------------------------|---------------------------------|
| `$params` | **array<string,mixed>** | Parameters containing `userId`. |

**Throws:**

When stateless token key
generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### logoutAs

Restore the original user from an impersonated session.

```php
public logoutAs(): array{loggedIn: bool, loggedInAs: bool, jwt?: string, refreshToken?: string, refreshed?: bool}
```

If both `userId` and `asUserId` are present, the original id becomes the
effective `userId` and the impersonation marker is removed.

**Return Value:**

Login state after
the restore attempt.

**Throws:**

When stateless token key
generation fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
