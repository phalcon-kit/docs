
Base MVC controller for PhalconKit applications.

***

* Full name: `\PhalconKit\Modules\Oauth2\Controllers\GithubController`
* Parent class: [`\PhalconKit\Modules\Oauth2\Controllers\AbstractController`](./AbstractController.md)

## Properties

### providerName

```php
public string $providerName
```

***

### sessionKey

```php
public string $sessionKey
```

***

## Inherited methods

### authorizationUrlAction

Start authorization and store a bounded, provider-specific state record.

```php
public authorizationUrlAction(?string $scope = null): \Phalcon\Http\ResponseInterface
```

`oauth2.stateLifetime` controls its lifetime in seconds (default 600).
A new attempt replaces the pending attempt for this provider/session.
Configured League PKCE verifiers are retained for the callback request.

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$scope`  | **?string** |             |

**Throws:**

When the state lifetime is invalid.
- [`ConfigurationException`](../../../Exception/ConfigurationException.md)

***

### validateState

Validate and consume callback state before authorizing one code exchange.

```php
public validateState(?string $state = null): bool
```

Values are compared verbatim; malformed, expired, legacy string, missing,
and wrong-provider states fail closed. A successful call consumes stored
state and allows getAccessToken() once in this controller instance.
Session storage must serialize requests or provide equivalent atomic
consumption when implementing a custom concurrent session backend.

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$state`  | **?string** |             |

***

### getAccessToken

Exchange a callback code only after successful one-time state validation.

```php
public getAccessToken(?string $code = null): \League\OAuth2\Client\Token\AccessTokenInterface
```

Existing callbacks may call validateState() first; otherwise this method
validates request state itself. The context is consumed before the remote
exchange, including failed exchanges. Retry by starting authorization again.

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$code`   | **?string** |             |

**Throws:**

With generic status 401 for invalid callback credentials.
- [`HttpException`](../../../Exception/HttpException.md)
When the provider rejects the exchange.
- [`IdentityProviderException`](https://oauth2-client.thephpleague.com/){:target="_blank"}

***

### refreshToken

Refresh Token

```php
public refreshToken(?string $refreshToken = null): \League\OAuth2\Client\Token\AccessTokenInterface
```

**Parameters:**

| Parameter       | Type        | Description |
|-----------------|-------------|-------------|
| `$refreshToken` | **?string** |             |

**Throws:**

- [`IdentityProviderException`](https://oauth2-client.thephpleague.com/){:target="_blank"}

***

### getToken

Use this to interact with an API on the users behalf

```php
public getToken(\League\OAuth2\Client\Token\AccessTokenInterface $token): string
```

**Parameters:**

| Parameter | Type                                                 | Description |
|-----------|------------------------------------------------------|-------------|
| `$token`  | **\League\OAuth2\Client\Token\AccessTokenInterface** |             |

***

### getRefreshToken

Use this to get a new access token if the old one expires

```php
public getRefreshToken(\League\OAuth2\Client\Token\AccessTokenInterface $token): ?string
```

**Parameters:**

| Parameter | Type                                                 | Description |
|-----------|------------------------------------------------------|-------------|
| `$token`  | **\League\OAuth2\Client\Token\AccessTokenInterface** |             |

***

### getExpires

Unix timestamp at which the access token expires

```php
public getExpires(\League\OAuth2\Client\Token\AccessTokenInterface $token): ?int
```

**Parameters:**

| Parameter | Type                                                 | Description |
|-----------|------------------------------------------------------|-------------|
| `$token`  | **\League\OAuth2\Client\Token\AccessTokenInterface** |             |

***

### getResourceOwner

Requests and returns the resource owner of given access token.

```php
public getResourceOwner(\League\OAuth2\Client\Token\AccessToken $token): \League\OAuth2\Client\Provider\ResourceOwnerInterface
```

**Parameters:**

| Parameter | Type                                        | Description |
|-----------|---------------------------------------------|-------------|
| `$token`  | **\League\OAuth2\Client\Token\AccessToken** |             |

***
