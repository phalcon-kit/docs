
Declares OAuth2 linking methods required by composed identity traits.

Implementations should normalize provider data into the core OAuth2 model,
link it to a local user, and establish the standard session identity when
the linked user can log in.

***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractOauth2`

## Methods

### oauth2

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, ?string $refreshToken = null, array<string,mixed>|null $meta = []): array<string,mixed>
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type                          | Description |
|-----------------|-------------------------------|-------------|
| `$provider`     | **string**                    |             |
| `$providerUuid` | **string**                    |             |
| `$accessToken`  | **string**                    |             |
| `$refreshToken` | **?string**                   |             |
| `$meta`         | **array<string,mixed>\|null** |             |

***
