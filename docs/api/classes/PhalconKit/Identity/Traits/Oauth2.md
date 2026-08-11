
Links provider OAuth2 identities to local users.

The trait owns the core OAuth2 persistence flow: find or create the provider
identity, store current tokens and profile metadata, attach the provider
identity to the logged-in local user when possible, then establish the
PhalconKit identity payload for the linked user. Stateless identity mode
returns refreshed JWT values after a successful login so API clients can
replace the token that now carries the linked user id.

***

* Full name: `\PhalconKit\Identity\Traits\Oauth2`

## Methods

### oauth2

Create/update an OAuth2 identity and log in its linked local user.

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, string|null $refreshToken = null, array<string,mixed>|null $meta = []): array{saved: bool, loggedIn: bool, loggedInAs: bool, messages: \Phalcon\Messages\Messages, jwt?: string, refreshToken?: string, refreshed?: bool}
```

If the provider identity is not linked yet and a local user is already
logged in, the provider identity is attached to that user. Otherwise the
saved provider identity must already contain a user id before login can
succeed.

**Parameters:**

| Parameter       | Type                          | Description                           |
|-----------------|-------------------------------|---------------------------------------|
| `$provider`     | **string**                    | Provider key.                         |
| `$providerUuid` | **string**                    | Stable provider-side user identifier. |
| `$accessToken`  | **string**                    | Provider access token.                |
| `$refreshToken` | **string\|null**              | Optional provider refresh token.      |
| `$meta`         | **array<string,mixed>\|null** | Optional provider profile data.       |

**Throws:**

When OAuth provider fields cannot be sanitized.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless token key
generation fails after a successful OAuth2 login.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When stateless JWT creation fails after a successful OAuth2 login.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
