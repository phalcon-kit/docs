
Declares ACL role methods required by traits composed into the identity manager.

This abstract trait lets small behavior traits call ACL methods without
depending on a concrete manager class. It is a compile-time contract only;
implementations should follow the public

- **See:** \PhalconKit\Identity\Traits\Interfaces\AclInterface.

***

* Full name: `\PhalconKit\Identity\Traits\Abstracts\AbstractAcl`

## Methods

### getAclRoles

```php
public getAclRoles(?array $roleList = null): array
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$roleList` | **?array** |             |

***
