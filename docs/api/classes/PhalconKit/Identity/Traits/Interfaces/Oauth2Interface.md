
Contract for linking OAuth2 identities to local PhalconKit users.

***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\Oauth2Interface`

## Methods

### oauth2

Create or update an OAuth2 identity and log in the linked local user.

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, string|null $refreshToken = null, array<string,mixed>|null $meta = []): array<string,mixed>
```

**Parameters:**

| Parameter       | Type                          | Description                                |
|-----------------|-------------------------------|--------------------------------------------|
| `$provider`     | **string**                    | Provider key such as `google` or `github`. |
| `$providerUuid` | **string**                    | Stable provider-side user identifier.      |
| `$accessToken`  | **string**                    | Current provider access token.             |
| `$refreshToken` | **string\|null**              | Optional provider refresh token.           |
| `$meta`         | **array<string,mixed>\|null** | Optional provider profile data.            |

**Return Value:**

Save state, login state, validation
messages, and optional JWT values when stateless identity mode
changes the token payload.

***
