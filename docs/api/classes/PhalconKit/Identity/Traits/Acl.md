
***

* Full name: `\PhalconKit\Identity\Traits\Acl`

## Methods

### getAclRoles

Return the list of ACL roles
- role `ws` is automatically added if the bootstrap mode is websocket/ws
- role `cli` is automatically added if the bootstrap mode is console/cli
- role `everyone` is automatically added to everyone at all time
- role `guest` is automatically added only if no role was found
- inherited roles are automatically added from the base roles

```php
public getAclRoles(array|null $roleList = null): array
```

**Parameters:**

| Parameter   | Type            | Description |
|-------------|-----------------|-------------|
| `$roleList` | **array\|null** |             |

***
