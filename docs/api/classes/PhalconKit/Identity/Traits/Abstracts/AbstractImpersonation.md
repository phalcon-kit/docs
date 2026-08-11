
Declares impersonation methods required by composed identity traits.

The concrete manager stores `userId` as the effective user and `asUserId` as
the original user during impersonation. Implementations should preserve that
payload shape unless they also replace the session helpers that consume it.

***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractImpersonation`

## Methods

### loginAs

```php
public loginAs(array<string,mixed> $params = []): array<string,mixed>
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                    | Description |
|-----------|-------------------------|-------------|
| `$params` | **array<string,mixed>** |             |

***
### logoutAs

```php
public logoutAs(): array{loggedIn: bool, loggedInAs: bool}
```

* This method is **abstract**.
***
