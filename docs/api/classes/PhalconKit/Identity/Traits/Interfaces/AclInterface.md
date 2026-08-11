
Contract for building the effective ACL roles of an identity.

***

* Full name: `\PhalconKit\Identity\Traits\Interfaces\AclInterface`

## Methods

### getAclRoles

Return ACL role objects keyed by role name.

```php
public getAclRoles(array<int,string>|null $roleList = null): array<string,\Phalcon\Acl\Role>
```

Implementations should include contextual roles such as `everyone`,
execution-context roles, identity roles, guest fallback, and inherited
roles according to the identity manager policy.

**Parameters:**

| Parameter   | Type                        | Description                                                                          |
|-------------|-----------------------------|--------------------------------------------------------------------------------------|
| `$roleList` | **array<int,string>\|null** | Optional base role names to use
instead of deriving roles from the current identity. |

***
