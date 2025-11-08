
***

* Full name: `\PhalconKit\Identity\Traits\Oauth2`

## Methods

### oauth2

OAuth2 authentication

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, string|null $refreshToken = null, array|null $meta = []): array
```

**Parameters:**

| Parameter       | Type             | Description                                             |
|-----------------|------------------|---------------------------------------------------------|
| `$provider`     | **string**       | The OAuth2 provider                                     |
| `$providerUuid` | **string**       | The UUID associated with the provider                   |
| `$accessToken`  | **string**       | The access token provided by the provider               |
| `$refreshToken` | **string\|null** | The refresh token provided by the provider (optional)   |
| `$meta`         | **array\|null**  | Additional metadata associated with the user (optional) |

**Return Value:**

Returns an array with the following keys:
- 'saved': Indicates whether the OAuth2 entity was saved successfully
- 'loggedIn': Indicates whether the user is currently logged in
- 'loggedInAs': Indicates the user that is currently logged in
- 'messages': An array of validation messages

**Throws:**

- [`Exception`](../../../Exception.md)

***
