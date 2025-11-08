
Class Controller

***

* Full name: `\PhalconKit\Modules\Oauth2\Controllers\FacebookController`
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

Redirect to Authorization Url

```php
public authorizationUrlAction(?string $scope = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$scope`  | **?string** |             |

***

### validateState

Validate State

```php
public validateState(?string $state = null): bool
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$state`  | **?string** |             |

***

### getAccessToken

Get Access Token

```php
public getAccessToken(?string $code = null): \League\OAuth2\Client\Token\AccessTokenInterface
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$code`   | **?string** |             |

**Throws:**

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
