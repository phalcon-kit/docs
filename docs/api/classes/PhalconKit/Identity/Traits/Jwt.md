
***

* Full name: `\PhalconKit\Identity\Traits\Jwt`

## Properties

### claim

```php
public array $claim
```

***

## Methods

### getJwt

Generates a new JWT and refresh token based on the specified claim and configuration.

```php
public getJwt(bool $refresh = false): array
```

If the claim does not have a key or is refreshed, it creates a new key and updates the session if enabled.

**Parameters:**

| Parameter  | Type     | Description                                                                                      |
|------------|----------|--------------------------------------------------------------------------------------------------|
| `$refresh` | **bool** | Indicates whether to refresh the claim by generating a new key and invalidating previous tokens. |

**Return Value:**

Contains the generated JWT, refresh token, and a flag indicating if the claim was refreshed.

**Throws:**

- [`\Phalcon\Encryption\Security\Exception|\Phalcon\Encryption\Security\JWT\Exceptions\ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### getClaim

Retrieves the claim using different authentication methods such as JWT, Authorization Header, or Session.

```php
public getClaim(bool $refresh = false, bool $force = false): array
```

If the claim is cached and not forced to refresh, it returns the cached claim.

**Parameters:**

| Parameter  | Type     | Description                                                      |
|------------|----------|------------------------------------------------------------------|
| `$refresh` | **bool** | Determines whether to attempt refreshing the claim if available. |
| `$force`   | **bool** | Forces bypassing the cached claim and retrieving a new one.      |

**Return Value:**

The claim data or an empty array if no claim is found.

***
### setClaim

Sets the claim information for the current instance.

```php
public setClaim(array $claim): void
```

**Parameters:**

| Parameter | Type      | Description            |
|-----------|-----------|------------------------|
| `$claim`  | **array** | The claim data to set. |

***
### getJwtToken

Generates a JWT (JSON Web Token) using the provided identifier, payload data, and additional options.

```php
public getJwtToken(string $id, array $data = [], array $options = []): string
```

**Parameters:**

| Parameter  | Type       | Description                                                                                                                     |
|------------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| `$id`      | **string** | The unique identifier for the JWT, typically representing a specific user or session.                                           |
| `$data`    | **array**  | An associative array containing the payload data to be encoded in the JWT.                                                      |
| `$options` | **array**  | An associative array of options for the token such as issuer, audience, subject, etc. Defaults will be applied if not provided. |

**Return Value:**

The generated JWT token as a string.

**Throws:**

- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### getClaimFromToken

Extracts claims from a provided JWT token after validating it.

```php
public getClaimFromToken(string $token, string|null $claim = null): array
```

**Parameters:**

| Parameter | Type             | Description                                           |
|-----------|------------------|-------------------------------------------------------|
| `$token`  | **string**       | The JWT token to parse and validate.                  |
| `$claim`  | **string\|null** | An optional identifier to validate the token against. |

**Return Value:**

The claims extracted from the token, or an empty array if no valid claims are found.

***
### getClaimFromAuthorization

Extracts claim information from the authorization header if it follows the Bearer token format.

```php
public getClaimFromAuthorization(array $authorization): array
```

**Parameters:**

| Parameter        | Type      | Description                                                           |
|------------------|-----------|-----------------------------------------------------------------------|
| `$authorization` | **array** | The authorization header split into an array with the type and token. |

**Return Value:**

The claim information extracted from the token or an empty array if extraction fails.

***
### getJsonRawBody

Retrieves the raw JSON body from the request.

```php
private getJsonRawBody(): \stdClass
```

If the body is not valid JSON, an empty stdClass object is returned.

**Return Value:**

The raw JSON body as an object or an empty stdClass object if the input is invalid.

***
