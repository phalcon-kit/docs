
***

* Full name: `\PhalconKit\Identity\Traits\Impersonation`

## Methods

### loginAs

Allows an admin or developer to log in as another user based on their user ID.

```php
public loginAs(array $params = []): array
```

Validates the provided parameters to ensure the presence and numericality of the user ID.
Also handles the scenario where the user attempts to return to their original session.

**Parameters:**

| Parameter | Type      | Description                                                                                      |
|-----------|-----------|--------------------------------------------------------------------------------------------------|
| `$params` | **array** | Associative array containing the key 'userId', which represents the ID of the user to log in as. |

**Return Value:**

An array containing the validation messages, login status, and login-as status:
- 'messages': Validation messages, if any.
- 'loggedIn': Boolean indicating whether the user is logged in under their original session.
- 'loggedInAs': Boolean indicating whether the user is logged in as another user.

***
### logoutAs

Logs out from a session where the user was logged in (impersonating)
as another user, reverting back to the original session identity.

```php
public logoutAs(): array
```

If the current session identity includes an 'asUserId', the identity
is updated to the corresponding 'userId'.

**Return Value:**

An array containing the user's login status after reverting:
- 'loggedIn': Boolean indicating whether the original user is logged in.
- 'loggedInAs': Boolean indicating whether the session is currently logged in as another user.

***
