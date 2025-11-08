
This is an automatically generated documentation for **Phalcon Kit Documentation**.

## Namespaces

### \


| Function                                                          | Description                                                                                                                  |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [`array_unset_recursive()`](./functions/array_unset_recursive.md) |                                                                                                                              |
| [`dump()`](./functions/dump.md)                                   | Dump the passed variables and end the script.                                                                                |
| [`exit_500()`](./functions/exit_500.md)                           | Terminate execution with a 500 Internal Server Error response code.                                                          |
| [`dd()`](./functions/dd.md)                                       | Dump variables and terminate execution with an error 500.                                                                    |
| [`vdd()`](./functions/vdd.md)                                     | Prints the values of the given parameters using var_dump and
then exits the program with a HTTP response status code of 500. |
| [`implode_sprintf()`](./functions/implode_sprintf.md)             | Will implode an array_map return of the sprintf or mb_sprintf results                                                        |
| [`implode_mb_sprintf()`](./functions/implode_mb_sprintf.md)       | Will implode an array_map return of the mb_sprintf results                                                                   |
| [`sprintfn()`](./functions/sprintfn.md)                           | version of sprintf for cases where named arguments are desired (php syntax)                                                  |
| [`mb_sprintf()`](./functions/mb_sprintf.md)                       | Return a formatted multibyte string
A more complete and working version of mb_sprintf and mb_vsprintf.                       |
| [`mb_vsprintf()`](./functions/mb_vsprintf.md)                     | Return a formatted string
It should work with any "ASCII preserving" encoding such as UTF-8 and all the ISO-8859 charsets.   |

### \PhalconKit


| Class                                            | Description                                                                         |
|--------------------------------------------------|-------------------------------------------------------------------------------------|
| [`Bootstrap`](./classes/PhalconKit/Bootstrap.md) | Phalcon Kit's Bootstrap for the MVC Application & CLI Console mode                  |
| [`Exception`](./classes/PhalconKit/Exception.md) | PhalconKit\Exception
All Phalcon Kit exceptions should use or extend this exception |
| [`Locale`](./classes/PhalconKit/Locale.md)       | Allow to manage and lookup the locale for the localisation                          |
| [`Tag`](./classes/PhalconKit/Tag.md)             | This file is part of the Phalcon Kit.                                               |

### \PhalconKit\Acl


| Class                                    | Description |
|------------------------------------------|-------------|
| [`Acl`](./classes/PhalconKit/Acl/Acl.md) | Class Acl   |


| Interface                                                  | Description |
|------------------------------------------------------------|-------------|
| [`AclInterface`](./classes/PhalconKit/Acl/AclInterface.md) |             |

### \PhalconKit\Assets


| Class                                               | Description   |
|-----------------------------------------------------|---------------|
| [`Manager`](./classes/PhalconKit/Assets/Manager.md) | {@inheritDoc} |

### \PhalconKit\Autoload


| Class                                               | Description  |
|-----------------------------------------------------|--------------|
| [`Loader`](./classes/PhalconKit/Autoload/Loader.md) | Class Loader |

### \PhalconKit\Bootstrap


| Class                                                        | Description                          |
|--------------------------------------------------------------|--------------------------------------|
| [`Config`](./classes/PhalconKit/Bootstrap/Config.md)         | Global Phalcon Kit Configuration     |
| [`Deployment`](./classes/PhalconKit/Bootstrap/Deployment.md) | Phalcon Kit Deployment Configuration |
| [`Devtools`](./classes/PhalconKit/Bootstrap/Devtools.md)     | Global Phalcon Kit Configuration     |
| [`Router`](./classes/PhalconKit/Bootstrap/Router.md)         | Phalcon Kit Router
{@inheritDoc}     |

### \PhalconKit\Bootstrap\Permissions


| Class                                                                              | Description |
|------------------------------------------------------------------------------------|-------------|
| [`ColumnConfig`](./classes/PhalconKit/Bootstrap/Permissions/ColumnConfig.md)       |             |
| [`DynamicConfig`](./classes/PhalconKit/Bootstrap/Permissions/DynamicConfig.md)     |             |
| [`RecordConfig`](./classes/PhalconKit/Bootstrap/Permissions/RecordConfig.md)       |             |
| [`TableConfig`](./classes/PhalconKit/Bootstrap/Permissions/TableConfig.md)         |             |
| [`TemplateConfig`](./classes/PhalconKit/Bootstrap/Permissions/TemplateConfig.md)   |             |
| [`WorkspaceConfig`](./classes/PhalconKit/Bootstrap/Permissions/WorkspaceConfig.md) |             |

### \PhalconKit\Cache


| Class                                          | Description |
|------------------------------------------------|-------------|
| [`Cache`](./classes/PhalconKit/Cache/Cache.md) | Class Cache |

### \PhalconKit\Cli


| Class                                                              | Description |
|--------------------------------------------------------------------|-------------|
| [`Console`](./classes/PhalconKit/Cli/Console.md)                   |             |
| [`Dispatcher`](./classes/PhalconKit/Cli/Dispatcher.md)             |             |
| [`ExceptionHandler`](./classes/PhalconKit/Cli/ExceptionHandler.md) |             |
| [`Module`](./classes/PhalconKit/Cli/Module.md)                     |             |
| [`Router`](./classes/PhalconKit/Cli/Router.md)                     |             |
| [`Task`](./classes/PhalconKit/Cli/Task.md)                         |             |


| Interface                                                                | Description                 |
|--------------------------------------------------------------------------|-----------------------------|
| [`DispatcherInterface`](./classes/PhalconKit/Cli/DispatcherInterface.md) |                             |
| [`TaskInterface`](./classes/PhalconKit/Cli/TaskInterface.md)             | Interface for task handlers |

### \PhalconKit\Config


| Class                                             | Description |
|---------------------------------------------------|-------------|
| [`Config`](./classes/PhalconKit/Config/Config.md) |             |


| Interface                                                           | Description |
|---------------------------------------------------------------------|-------------|
| [`ConfigInterface`](./classes/PhalconKit/Config/ConfigInterface.md) |             |

### \PhalconKit\Db


| Class                                             | Description   |
|---------------------------------------------------|---------------|
| [`Column`](./classes/PhalconKit/Db/Column.md)     |               |
| [`Profiler`](./classes/PhalconKit/Db/Profiler.md) | {@inheritdoc} |

### \PhalconKit\Db\Adapter\Pdo


| Class                                                   | Description |
|---------------------------------------------------------|-------------|
| [`Mysql`](./classes/PhalconKit/Db/Adapter/Pdo/Mysql.md) |             |

### \PhalconKit\Db\Dialect


| Class                                               | Description |
|-----------------------------------------------------|-------------|
| [`Mysql`](./classes/PhalconKit/Db/Dialect/Mysql.md) | Class MySQL |

### \PhalconKit\Db\Events


| Class                                                    | Description                                    |
|----------------------------------------------------------|------------------------------------------------|
| [`Logger`](./classes/PhalconKit/Db/Events/Logger.md)     | Responsible for logging database query events. |
| [`Profiler`](./classes/PhalconKit/Db/Events/Profiler.md) | Class Profiler                                 |

### \PhalconKit\Di


| Class                                                 | Description |
|-------------------------------------------------------|-------------|
| [`Injectable`](./classes/PhalconKit/Di/Injectable.md) |             |


| Trait                                                                     | Description                                                                                 |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [`AbstractInjectable`](./classes/PhalconKit/Di/AbstractInjectable.md)     | Trait AbstractInjectable                                                                    |
| [`InjectableProperties`](./classes/PhalconKit/Di/InjectableProperties.md) |                                                                                             |
| [`InjectableTrait`](./classes/PhalconKit/Di/InjectableTrait.md)           | The InjectableTrait trait provides methods for using dependency injection within an object. |

### \PhalconKit\Dispatcher


| Class                                                                         | Description |
|-------------------------------------------------------------------------------|-------------|
| [`AbstractDispatcher`](./classes/PhalconKit/Dispatcher/AbstractDispatcher.md) |             |


| Trait                                                                   | Description |
|-------------------------------------------------------------------------|-------------|
| [`DispatcherTrait`](./classes/PhalconKit/Dispatcher/DispatcherTrait.md) |             |


| Interface                                                                       | Description |
|---------------------------------------------------------------------------------|-------------|
| [`DispatcherInterface`](./classes/PhalconKit/Dispatcher/DispatcherInterface.md) |             |

### \PhalconKit\Encryption


| Class                                                     | Description   |
|-----------------------------------------------------------|---------------|
| [`Security`](./classes/PhalconKit/Encryption/Security.md) | {@inheritDoc} |

### \PhalconKit\Encryption\Security


| Class                                                          | Description |
|----------------------------------------------------------------|-------------|
| [`Random`](./classes/PhalconKit/Encryption/Security/Random.md) |             |

### \PhalconKit\Events


| Trait                                                                 | Description                                                               |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`EventsAwareTrait`](./classes/PhalconKit/Events/EventsAwareTrait.md) | The EventsAwareTrait provides methods for managing events within a class. |

### \PhalconKit\Exception


| Class                                                              | Description                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`CliException`](./classes/PhalconKit/Exception/CliException.md)   | PhalconKit\Exception
All Phalcon Kit exceptions should use or extend this exception |
| [`HttpException`](./classes/PhalconKit/Exception/HttpException.md) | PhalconKit\Exception
All Phalcon Kit exceptions should use or extend this exception |
| [`WsException`](./classes/PhalconKit/Exception/WsException.md)     | PhalconKit\Exception
All Phalcon Kit exceptions should use or extend this exception |

### \PhalconKit\Filter


| Class                                                           | Description                                                                                               |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`Filter`](./classes/PhalconKit/Filter/Filter.md)               | Filter class extends the \Phalcon\Filter\Filter class and provides additional methods for filtering data. |
| [`FilterFactory`](./classes/PhalconKit/Filter/FilterFactory.md) |                                                                                                           |
| [`Validation`](./classes/PhalconKit/Filter/Validation.md)       | {@inheritDoc}                                                                                             |

### \PhalconKit\Filter\Sanitize


| Class                                                  | Description |
|--------------------------------------------------------|-------------|
| [`IPv4`](./classes/PhalconKit/Filter/Sanitize/IPv4.md) |             |
| [`IPv6`](./classes/PhalconKit/Filter/Sanitize/IPv6.md) |             |
| [`Json`](./classes/PhalconKit/Filter/Sanitize/Json.md) |             |
| [`Md5`](./classes/PhalconKit/Filter/Sanitize/Md5.md)   |             |

### \PhalconKit\Filter\Validation\Validator


| Class                                                                | Description |
|----------------------------------------------------------------------|-------------|
| [`Color`](./classes/PhalconKit/Filter/Validation/Validator/Color.md) |             |
| [`Json`](./classes/PhalconKit/Filter/Validation/Validator/Json.md)   |             |

### \PhalconKit\Fractal


| Class                                                                  | Description                                                                                       |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [`Manager`](./classes/PhalconKit/Fractal/Manager.md)                   | The Manager class extends the League\Fractal\Manager class and provides additional functionality. |
| [`ModelTransformer`](./classes/PhalconKit/Fractal/ModelTransformer.md) | This class is responsible for transforming a Model object into an array representation.           |
| [`Transformer`](./classes/PhalconKit/Fractal/Transformer.md)           | This class extends the TransformerAbstract class and implements the InjectionAwareInterface.      |

### \PhalconKit\Fractal\Serializer


| Class                                                                                 | Description              |
|---------------------------------------------------------------------------------------|--------------------------|
| [`RawArraySerializer`](./classes/PhalconKit/Fractal/Serializer/RawArraySerializer.md) | Class RawArraySerializer |

### \PhalconKit\Html


| Class                                                   | Description             |
|---------------------------------------------------------|-------------------------|
| [`Escaper`](./classes/PhalconKit/Html/Escaper.md)       | PhalconKit\Html\Escaper |
| [`TagFactory`](./classes/PhalconKit/Html/TagFactory.md) | Class TagFactory        |

### \PhalconKit\Html\Escaper


| Interface                                                                   | Description |
|-----------------------------------------------------------------------------|-------------|
| [`EscaperInterface`](./classes/PhalconKit/Html/Escaper/EscaperInterface.md) |             |

### \PhalconKit\Http


| Class                                                   | Description                                      |
|---------------------------------------------------------|--------------------------------------------------|
| [`Request`](./classes/PhalconKit/Http/Request.md)       | Represents an HTTP request.                      |
| [`Response`](./classes/PhalconKit/Http/Response.md)     | Represents an HTTP response.                     |
| [`StatusCode`](./classes/PhalconKit/Http/StatusCode.md) | According to Wikipedia List of HTTP status codes |


| Interface                                                             | Description   |
|-----------------------------------------------------------------------|---------------|
| [`RequestInterface`](./classes/PhalconKit/Http/RequestInterface.md)   | {@inheritDoc} |
| [`ResponseInterface`](./classes/PhalconKit/Http/ResponseInterface.md) | {@inheritDoc} |

### \PhalconKit\Identity


| Class                                                 | Description |
|-------------------------------------------------------|-------------|
| [`Manager`](./classes/PhalconKit/Identity/Manager.md) |             |


| Interface                                                               | Description |
|-------------------------------------------------------------------------|-------------|
| [`ManagerInterface`](./classes/PhalconKit/Identity/ManagerInterface.md) |             |

### \PhalconKit\Identity\Traits


| Trait                                                                    | Description |
|--------------------------------------------------------------------------|-------------|
| [`Acl`](./classes/PhalconKit/Identity/Traits/Acl.md)                     |             |
| [`Impersonation`](./classes/PhalconKit/Identity/Traits/Impersonation.md) |             |
| [`Jwt`](./classes/PhalconKit/Identity/Traits/Jwt.md)                     |             |
| [`Oauth2`](./classes/PhalconKit/Identity/Traits/Oauth2.md)               |             |
| [`Role`](./classes/PhalconKit/Identity/Traits/Role.md)                   |             |
| [`Session`](./classes/PhalconKit/Identity/Traits/Session.md)             |             |
| [`User`](./classes/PhalconKit/Identity/Traits/User.md)                   |             |

### \PhalconKit\Identity\Traits\Abstracts


| Trait                                                                                              | Description |
|----------------------------------------------------------------------------------------------------|-------------|
| [`AbstractAcl`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractAcl.md)                     |             |
| [`AbstractImpersonation`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractImpersonation.md) |             |
| [`AbstractJwt`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractJwt.md)                     |             |
| [`AbstractOauth2`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractOauth2.md)               |             |
| [`AbstractRole`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractRole.md)                   |             |
| [`AbstractSession`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractSession.md)             |             |
| [`AbstractUser`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractUser.md)                   |             |

### \PhalconKit\Identity\Traits\Interfaces


| Interface                                                                                             | Description |
|-------------------------------------------------------------------------------------------------------|-------------|
| [`AclInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/AclInterface.md)                     |             |
| [`ImpersonationInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/ImpersonationInterface.md) |             |
| [`JwtInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/JwtInterface.md)                     |             |
| [`Oauth2Interface`](./classes/PhalconKit/Identity/Traits/Interfaces/Oauth2Interface.md)               |             |
| [`RoleInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/RoleInterface.md)                   |             |
| [`SessionInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/SessionInterface.md)             |             |
| [`UserInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/UserInterface.md)                   |             |

### \PhalconKit\Locales


| Class                                      | Description |
|--------------------------------------------|-------------|
| [`En`](./classes/PhalconKit/Locales/En.md) |             |
| [`Fr`](./classes/PhalconKit/Locales/Fr.md) |             |

### \PhalconKit\Logger


| Class                                               | Description |
|-----------------------------------------------------|-------------|
| [`Loggers`](./classes/PhalconKit/Logger/Loggers.md) |             |

### \PhalconKit\Models


| Class                                                                   | Description                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`AbstractModel`](./classes/PhalconKit/Models/AbstractModel.md)         | Events
- afterCreate
- afterDelete
- afterFetch
- afterSave
- afterUpdate
- afterValidation
- afterValidationOnCreate
- afterValidationOnUpdate
- beforeDelete
- beforeCreate
- beforeSave
- beforeUpdate
- beforeValidation
- beforeValidationOnCreate
- beforeValidationOnUpdate
- notDeleted
- notSaved
- onValidationFails
- prepareSave
- validation |
| [`Audit`](./classes/PhalconKit/Models/Audit.md)                         | Class Audit                                                                                                                                                                                                                                                                                                                                               |
| [`AuditDetail`](./classes/PhalconKit/Models/AuditDetail.md)             | Class AuditDetail                                                                                                                                                                                                                                                                                                                                         |
| [`Backup`](./classes/PhalconKit/Models/Backup.md)                       | Class Backup                                                                                                                                                                                                                                                                                                                                              |
| [`Category`](./classes/PhalconKit/Models/Category.md)                   | Class Category                                                                                                                                                                                                                                                                                                                                            |
| [`Column`](./classes/PhalconKit/Models/Column.md)                       | Class Column                                                                                                                                                                                                                                                                                                                                              |
| [`Data`](./classes/PhalconKit/Models/Data.md)                           | Class Data                                                                                                                                                                                                                                                                                                                                                |
| [`Email`](./classes/PhalconKit/Models/Email.md)                         | Class Email                                                                                                                                                                                                                                                                                                                                               |
| [`EmailFile`](./classes/PhalconKit/Models/EmailFile.md)                 | Class EmailFile                                                                                                                                                                                                                                                                                                                                           |
| [`Feature`](./classes/PhalconKit/Models/Feature.md)                     | Class Feature                                                                                                                                                                                                                                                                                                                                             |
| [`File`](./classes/PhalconKit/Models/File.md)                           | Class File                                                                                                                                                                                                                                                                                                                                                |
| [`FileRelation`](./classes/PhalconKit/Models/FileRelation.md)           | Class FileRelation                                                                                                                                                                                                                                                                                                                                        |
| [`Flag`](./classes/PhalconKit/Models/Flag.md)                           | Class Flag                                                                                                                                                                                                                                                                                                                                                |
| [`Group`](./classes/PhalconKit/Models/Group.md)                         | Class Group                                                                                                                                                                                                                                                                                                                                               |
| [`GroupFeature`](./classes/PhalconKit/Models/GroupFeature.md)           | Class GroupFeature                                                                                                                                                                                                                                                                                                                                        |
| [`GroupRole`](./classes/PhalconKit/Models/GroupRole.md)                 | Class GroupRole                                                                                                                                                                                                                                                                                                                                           |
| [`GroupType`](./classes/PhalconKit/Models/GroupType.md)                 | Class GroupType                                                                                                                                                                                                                                                                                                                                           |
| [`Job`](./classes/PhalconKit/Models/Job.md)                             | Class Job                                                                                                                                                                                                                                                                                                                                                 |
| [`JobScheduler`](./classes/PhalconKit/Models/JobScheduler.md)           | Class JobScheduler                                                                                                                                                                                                                                                                                                                                        |
| [`Lang`](./classes/PhalconKit/Models/Lang.md)                           | Class Lang                                                                                                                                                                                                                                                                                                                                                |
| [`Log`](./classes/PhalconKit/Models/Log.md)                             | Class Log                                                                                                                                                                                                                                                                                                                                                 |
| [`Menu`](./classes/PhalconKit/Models/Menu.md)                           | Class Menu                                                                                                                                                                                                                                                                                                                                                |
| [`Meta`](./classes/PhalconKit/Models/Meta.md)                           | Class Meta                                                                                                                                                                                                                                                                                                                                                |
| [`Oauth2`](./classes/PhalconKit/Models/Oauth2.md)                       | Class Oauth2                                                                                                                                                                                                                                                                                                                                              |
| [`Page`](./classes/PhalconKit/Models/Page.md)                           | Class Page                                                                                                                                                                                                                                                                                                                                                |
| [`PhalconMigrations`](./classes/PhalconKit/Models/PhalconMigrations.md) | Class PhalconMigrations                                                                                                                                                                                                                                                                                                                                   |
| [`Post`](./classes/PhalconKit/Models/Post.md)                           | Class Post                                                                                                                                                                                                                                                                                                                                                |
| [`PostCategory`](./classes/PhalconKit/Models/PostCategory.md)           | Class PostCategory                                                                                                                                                                                                                                                                                                                                        |
| [`Profile`](./classes/PhalconKit/Models/Profile.md)                     | Class Profile                                                                                                                                                                                                                                                                                                                                             |
| [`Record`](./classes/PhalconKit/Models/Record.md)                       | Class Record                                                                                                                                                                                                                                                                                                                                              |
| [`Role`](./classes/PhalconKit/Models/Role.md)                           | Class Role                                                                                                                                                                                                                                                                                                                                                |
| [`RoleFeature`](./classes/PhalconKit/Models/RoleFeature.md)             | Class RoleFeature                                                                                                                                                                                                                                                                                                                                         |
| [`RoleRole`](./classes/PhalconKit/Models/RoleRole.md)                   | Class RoleRole                                                                                                                                                                                                                                                                                                                                            |
| [`Session`](./classes/PhalconKit/Models/Session.md)                     | Class Session                                                                                                                                                                                                                                                                                                                                             |
| [`Setting`](./classes/PhalconKit/Models/Setting.md)                     | Class Setting                                                                                                                                                                                                                                                                                                                                             |
| [`Site`](./classes/PhalconKit/Models/Site.md)                           | Class Site                                                                                                                                                                                                                                                                                                                                                |
| [`SiteLang`](./classes/PhalconKit/Models/SiteLang.md)                   | Class SiteLang                                                                                                                                                                                                                                                                                                                                            |
| [`Table`](./classes/PhalconKit/Models/Table.md)                         | Class Table                                                                                                                                                                                                                                                                                                                                               |
| [`Template`](./classes/PhalconKit/Models/Template.md)                   | Class Template                                                                                                                                                                                                                                                                                                                                            |
| [`Translate`](./classes/PhalconKit/Models/Translate.md)                 | Class Translate                                                                                                                                                                                                                                                                                                                                           |
| [`Type`](./classes/PhalconKit/Models/Type.md)                           | Class Type                                                                                                                                                                                                                                                                                                                                                |
| [`User`](./classes/PhalconKit/Models/User.md)                           | Class User                                                                                                                                                                                                                                                                                                                                                |
| [`UserFeature`](./classes/PhalconKit/Models/UserFeature.md)             | Class UserFeature                                                                                                                                                                                                                                                                                                                                         |
| [`UserGroup`](./classes/PhalconKit/Models/UserGroup.md)                 | Class UserGroup                                                                                                                                                                                                                                                                                                                                           |
| [`UserRole`](./classes/PhalconKit/Models/UserRole.md)                   | Class UserRole                                                                                                                                                                                                                                                                                                                                            |
| [`UserType`](./classes/PhalconKit/Models/UserType.md)                   | Class UserType                                                                                                                                                                                                                                                                                                                                            |
| [`Validator`](./classes/PhalconKit/Models/Validator.md)                 | Class Validator                                                                                                                                                                                                                                                                                                                                           |
| [`Workspace`](./classes/PhalconKit/Models/Workspace.md)                 | Class Workspace                                                                                                                                                                                                                                                                                                                                           |
| [`WorkspaceLang`](./classes/PhalconKit/Models/WorkspaceLang.md)         | Class WorkspaceLang                                                                                                                                                                                                                                                                                                                                       |

### \PhalconKit\Models\Abstracts


| Class                                                                                             | Description                     |
|---------------------------------------------------------------------------------------------------|---------------------------------|
| [`AuditAbstract`](./classes/PhalconKit/Models/Abstracts/AuditAbstract.md)                         | Class AuditAbstract             |
| [`AuditDetailAbstract`](./classes/PhalconKit/Models/Abstracts/AuditDetailAbstract.md)             | Class AuditDetailAbstract       |
| [`BackupAbstract`](./classes/PhalconKit/Models/Abstracts/BackupAbstract.md)                       | Class BackupAbstract            |
| [`CategoryAbstract`](./classes/PhalconKit/Models/Abstracts/CategoryAbstract.md)                   | Class CategoryAbstract          |
| [`ColumnAbstract`](./classes/PhalconKit/Models/Abstracts/ColumnAbstract.md)                       | Class ColumnAbstract            |
| [`DataAbstract`](./classes/PhalconKit/Models/Abstracts/DataAbstract.md)                           | Class DataAbstract              |
| [`EmailAbstract`](./classes/PhalconKit/Models/Abstracts/EmailAbstract.md)                         | Class EmailAbstract             |
| [`EmailFileAbstract`](./classes/PhalconKit/Models/Abstracts/EmailFileAbstract.md)                 | Class EmailFileAbstract         |
| [`FeatureAbstract`](./classes/PhalconKit/Models/Abstracts/FeatureAbstract.md)                     | Class FeatureAbstract           |
| [`FileAbstract`](./classes/PhalconKit/Models/Abstracts/FileAbstract.md)                           | Class FileAbstract              |
| [`FileRelationAbstract`](./classes/PhalconKit/Models/Abstracts/FileRelationAbstract.md)           | Class FileRelationAbstract      |
| [`FlagAbstract`](./classes/PhalconKit/Models/Abstracts/FlagAbstract.md)                           | Class FlagAbstract              |
| [`GroupAbstract`](./classes/PhalconKit/Models/Abstracts/GroupAbstract.md)                         | Class GroupAbstract             |
| [`GroupFeatureAbstract`](./classes/PhalconKit/Models/Abstracts/GroupFeatureAbstract.md)           | Class GroupFeatureAbstract      |
| [`GroupRoleAbstract`](./classes/PhalconKit/Models/Abstracts/GroupRoleAbstract.md)                 | Class GroupRoleAbstract         |
| [`GroupTypeAbstract`](./classes/PhalconKit/Models/Abstracts/GroupTypeAbstract.md)                 | Class GroupTypeAbstract         |
| [`JobAbstract`](./classes/PhalconKit/Models/Abstracts/JobAbstract.md)                             | Class JobAbstract               |
| [`JobSchedulerAbstract`](./classes/PhalconKit/Models/Abstracts/JobSchedulerAbstract.md)           | Class JobSchedulerAbstract      |
| [`LangAbstract`](./classes/PhalconKit/Models/Abstracts/LangAbstract.md)                           | Class LangAbstract              |
| [`LogAbstract`](./classes/PhalconKit/Models/Abstracts/LogAbstract.md)                             | Class LogAbstract               |
| [`MenuAbstract`](./classes/PhalconKit/Models/Abstracts/MenuAbstract.md)                           | Class MenuAbstract              |
| [`MetaAbstract`](./classes/PhalconKit/Models/Abstracts/MetaAbstract.md)                           | Class MetaAbstract              |
| [`Oauth2Abstract`](./classes/PhalconKit/Models/Abstracts/Oauth2Abstract.md)                       | Class Oauth2Abstract            |
| [`PageAbstract`](./classes/PhalconKit/Models/Abstracts/PageAbstract.md)                           | Class PageAbstract              |
| [`PhalconMigrationsAbstract`](./classes/PhalconKit/Models/Abstracts/PhalconMigrationsAbstract.md) | Class PhalconMigrationsAbstract |
| [`PostAbstract`](./classes/PhalconKit/Models/Abstracts/PostAbstract.md)                           | Class PostAbstract              |
| [`PostCategoryAbstract`](./classes/PhalconKit/Models/Abstracts/PostCategoryAbstract.md)           | Class PostCategoryAbstract      |
| [`ProfileAbstract`](./classes/PhalconKit/Models/Abstracts/ProfileAbstract.md)                     | Class ProfileAbstract           |
| [`RecordAbstract`](./classes/PhalconKit/Models/Abstracts/RecordAbstract.md)                       | Class RecordAbstract            |
| [`RoleAbstract`](./classes/PhalconKit/Models/Abstracts/RoleAbstract.md)                           | Class RoleAbstract              |
| [`RoleFeatureAbstract`](./classes/PhalconKit/Models/Abstracts/RoleFeatureAbstract.md)             | Class RoleFeatureAbstract       |
| [`RoleRoleAbstract`](./classes/PhalconKit/Models/Abstracts/RoleRoleAbstract.md)                   | Class RoleRoleAbstract          |
| [`SessionAbstract`](./classes/PhalconKit/Models/Abstracts/SessionAbstract.md)                     | Class SessionAbstract           |
| [`SettingAbstract`](./classes/PhalconKit/Models/Abstracts/SettingAbstract.md)                     | Class SettingAbstract           |
| [`SiteAbstract`](./classes/PhalconKit/Models/Abstracts/SiteAbstract.md)                           | Class SiteAbstract              |
| [`SiteLangAbstract`](./classes/PhalconKit/Models/Abstracts/SiteLangAbstract.md)                   | Class SiteLangAbstract          |
| [`TableAbstract`](./classes/PhalconKit/Models/Abstracts/TableAbstract.md)                         | Class TableAbstract             |
| [`TemplateAbstract`](./classes/PhalconKit/Models/Abstracts/TemplateAbstract.md)                   | Class TemplateAbstract          |
| [`TranslateAbstract`](./classes/PhalconKit/Models/Abstracts/TranslateAbstract.md)                 | Class TranslateAbstract         |
| [`TypeAbstract`](./classes/PhalconKit/Models/Abstracts/TypeAbstract.md)                           | Class TypeAbstract              |
| [`UserAbstract`](./classes/PhalconKit/Models/Abstracts/UserAbstract.md)                           | Class UserAbstract              |
| [`UserFeatureAbstract`](./classes/PhalconKit/Models/Abstracts/UserFeatureAbstract.md)             | Class UserFeatureAbstract       |
| [`UserGroupAbstract`](./classes/PhalconKit/Models/Abstracts/UserGroupAbstract.md)                 | Class UserGroupAbstract         |
| [`UserRoleAbstract`](./classes/PhalconKit/Models/Abstracts/UserRoleAbstract.md)                   | Class UserRoleAbstract          |
| [`UserTypeAbstract`](./classes/PhalconKit/Models/Abstracts/UserTypeAbstract.md)                   | Class UserTypeAbstract          |
| [`ValidatorAbstract`](./classes/PhalconKit/Models/Abstracts/ValidatorAbstract.md)                 | Class ValidatorAbstract         |
| [`WorkspaceAbstract`](./classes/PhalconKit/Models/Abstracts/WorkspaceAbstract.md)                 | Class WorkspaceAbstract         |
| [`WorkspaceLangAbstract`](./classes/PhalconKit/Models/Abstracts/WorkspaceLangAbstract.md)         | Class WorkspaceLangAbstract     |

### \PhalconKit\Models\Abstracts\Interfaces


| Interface                                                                                                                      | Description |
|--------------------------------------------------------------------------------------------------------------------------------|-------------|
| [`AuditAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/AuditAbstractInterface.md)                         |             |
| [`AuditDetailAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/AuditDetailAbstractInterface.md)             |             |
| [`BackupAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/BackupAbstractInterface.md)                       |             |
| [`CategoryAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/CategoryAbstractInterface.md)                   |             |
| [`ColumnAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/ColumnAbstractInterface.md)                       |             |
| [`DataAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/DataAbstractInterface.md)                           |             |
| [`EmailAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/EmailAbstractInterface.md)                         |             |
| [`EmailFileAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/EmailFileAbstractInterface.md)                 |             |
| [`FeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FeatureAbstractInterface.md)                     |             |
| [`FileAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FileAbstractInterface.md)                           |             |
| [`FileRelationAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FileRelationAbstractInterface.md)           |             |
| [`FlagAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FlagAbstractInterface.md)                           |             |
| [`GroupAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupAbstractInterface.md)                         |             |
| [`GroupFeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupFeatureAbstractInterface.md)           |             |
| [`GroupRoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupRoleAbstractInterface.md)                 |             |
| [`GroupTypeAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupTypeAbstractInterface.md)                 |             |
| [`JobAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/JobAbstractInterface.md)                             |             |
| [`JobSchedulerAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/JobSchedulerAbstractInterface.md)           |             |
| [`LangAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/LangAbstractInterface.md)                           |             |
| [`LogAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/LogAbstractInterface.md)                             |             |
| [`MenuAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/MenuAbstractInterface.md)                           |             |
| [`MetaAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/MetaAbstractInterface.md)                           |             |
| [`Oauth2AbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/Oauth2AbstractInterface.md)                       |             |
| [`PageAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PageAbstractInterface.md)                           |             |
| [`PhalconMigrationsAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PhalconMigrationsAbstractInterface.md) |             |
| [`PostAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PostAbstractInterface.md)                           |             |
| [`PostCategoryAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PostCategoryAbstractInterface.md)           |             |
| [`ProfileAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/ProfileAbstractInterface.md)                     |             |
| [`RecordAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RecordAbstractInterface.md)                       |             |
| [`RoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RoleAbstractInterface.md)                           |             |
| [`RoleFeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RoleFeatureAbstractInterface.md)             |             |
| [`RoleRoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RoleRoleAbstractInterface.md)                   |             |
| [`SessionAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SessionAbstractInterface.md)                     |             |
| [`SettingAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SettingAbstractInterface.md)                     |             |
| [`SiteAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SiteAbstractInterface.md)                           |             |
| [`SiteLangAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SiteLangAbstractInterface.md)                   |             |
| [`TableAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TableAbstractInterface.md)                         |             |
| [`TemplateAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TemplateAbstractInterface.md)                   |             |
| [`TranslateAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TranslateAbstractInterface.md)                 |             |
| [`TypeAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TypeAbstractInterface.md)                           |             |
| [`UserAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserAbstractInterface.md)                           |             |
| [`UserFeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserFeatureAbstractInterface.md)             |             |
| [`UserGroupAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserGroupAbstractInterface.md)                 |             |
| [`UserRoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserRoleAbstractInterface.md)                   |             |
| [`UserTypeAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserTypeAbstractInterface.md)                   |             |
| [`ValidatorAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/ValidatorAbstractInterface.md)                 |             |
| [`WorkspaceAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/WorkspaceAbstractInterface.md)                 |             |
| [`WorkspaceLangAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/WorkspaceLangAbstractInterface.md)         |             |

### \PhalconKit\Models\Behaviors


| Interface                                                                             | Description |
|---------------------------------------------------------------------------------------|-------------|
| [`BlameableInterface`](./classes/PhalconKit/Models/Behaviors/BlameableInterface.md)   |             |
| [`SoftDeleteInterface`](./classes/PhalconKit/Models/Behaviors/SoftDeleteInterface.md) |             |

### \PhalconKit\Models\Behaviors\Blameable


| Interface                                                                                   | Description |
|---------------------------------------------------------------------------------------------|-------------|
| [`CreatedInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/CreatedInterface.md)   |             |
| [`DeletedInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/DeletedInterface.md)   |             |
| [`RestoredInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/RestoredInterface.md) |             |
| [`UpdateInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/UpdateInterface.md)     |             |

### \PhalconKit\Models\Interfaces


| Interface                                                                                            | Description |
|------------------------------------------------------------------------------------------------------|-------------|
| [`AuditDetailInterface`](./classes/PhalconKit/Models/Interfaces/AuditDetailInterface.md)             |             |
| [`AuditInterface`](./classes/PhalconKit/Models/Interfaces/AuditInterface.md)                         |             |
| [`BackupInterface`](./classes/PhalconKit/Models/Interfaces/BackupInterface.md)                       |             |
| [`CategoryInterface`](./classes/PhalconKit/Models/Interfaces/CategoryInterface.md)                   |             |
| [`ColumnInterface`](./classes/PhalconKit/Models/Interfaces/ColumnInterface.md)                       |             |
| [`DataInterface`](./classes/PhalconKit/Models/Interfaces/DataInterface.md)                           |             |
| [`EmailFileInterface`](./classes/PhalconKit/Models/Interfaces/EmailFileInterface.md)                 |             |
| [`EmailInterface`](./classes/PhalconKit/Models/Interfaces/EmailInterface.md)                         |             |
| [`FeatureInterface`](./classes/PhalconKit/Models/Interfaces/FeatureInterface.md)                     |             |
| [`FileInterface`](./classes/PhalconKit/Models/Interfaces/FileInterface.md)                           |             |
| [`FileRelationInterface`](./classes/PhalconKit/Models/Interfaces/FileRelationInterface.md)           |             |
| [`FlagInterface`](./classes/PhalconKit/Models/Interfaces/FlagInterface.md)                           |             |
| [`GroupFeatureInterface`](./classes/PhalconKit/Models/Interfaces/GroupFeatureInterface.md)           |             |
| [`GroupInterface`](./classes/PhalconKit/Models/Interfaces/GroupInterface.md)                         |             |
| [`GroupRoleInterface`](./classes/PhalconKit/Models/Interfaces/GroupRoleInterface.md)                 |             |
| [`GroupTypeInterface`](./classes/PhalconKit/Models/Interfaces/GroupTypeInterface.md)                 |             |
| [`JobInterface`](./classes/PhalconKit/Models/Interfaces/JobInterface.md)                             |             |
| [`JobSchedulerInterface`](./classes/PhalconKit/Models/Interfaces/JobSchedulerInterface.md)           |             |
| [`LangInterface`](./classes/PhalconKit/Models/Interfaces/LangInterface.md)                           |             |
| [`LogInterface`](./classes/PhalconKit/Models/Interfaces/LogInterface.md)                             |             |
| [`MenuInterface`](./classes/PhalconKit/Models/Interfaces/MenuInterface.md)                           |             |
| [`MetaInterface`](./classes/PhalconKit/Models/Interfaces/MetaInterface.md)                           |             |
| [`Oauth2Interface`](./classes/PhalconKit/Models/Interfaces/Oauth2Interface.md)                       |             |
| [`PageInterface`](./classes/PhalconKit/Models/Interfaces/PageInterface.md)                           |             |
| [`PhalconMigrationsInterface`](./classes/PhalconKit/Models/Interfaces/PhalconMigrationsInterface.md) |             |
| [`PostCategoryInterface`](./classes/PhalconKit/Models/Interfaces/PostCategoryInterface.md)           |             |
| [`PostInterface`](./classes/PhalconKit/Models/Interfaces/PostInterface.md)                           |             |
| [`ProfileInterface`](./classes/PhalconKit/Models/Interfaces/ProfileInterface.md)                     |             |
| [`RecordInterface`](./classes/PhalconKit/Models/Interfaces/RecordInterface.md)                       |             |
| [`RoleFeatureInterface`](./classes/PhalconKit/Models/Interfaces/RoleFeatureInterface.md)             |             |
| [`RoleInterface`](./classes/PhalconKit/Models/Interfaces/RoleInterface.md)                           |             |
| [`RoleRoleInterface`](./classes/PhalconKit/Models/Interfaces/RoleRoleInterface.md)                   |             |
| [`SessionInterface`](./classes/PhalconKit/Models/Interfaces/SessionInterface.md)                     |             |
| [`SettingInterface`](./classes/PhalconKit/Models/Interfaces/SettingInterface.md)                     |             |
| [`SiteInterface`](./classes/PhalconKit/Models/Interfaces/SiteInterface.md)                           |             |
| [`SiteLangInterface`](./classes/PhalconKit/Models/Interfaces/SiteLangInterface.md)                   |             |
| [`TableInterface`](./classes/PhalconKit/Models/Interfaces/TableInterface.md)                         |             |
| [`TemplateInterface`](./classes/PhalconKit/Models/Interfaces/TemplateInterface.md)                   |             |
| [`TranslateInterface`](./classes/PhalconKit/Models/Interfaces/TranslateInterface.md)                 |             |
| [`TypeInterface`](./classes/PhalconKit/Models/Interfaces/TypeInterface.md)                           |             |
| [`UserFeatureInterface`](./classes/PhalconKit/Models/Interfaces/UserFeatureInterface.md)             |             |
| [`UserGroupInterface`](./classes/PhalconKit/Models/Interfaces/UserGroupInterface.md)                 |             |
| [`UserInterface`](./classes/PhalconKit/Models/Interfaces/UserInterface.md)                           |             |
| [`UserRoleInterface`](./classes/PhalconKit/Models/Interfaces/UserRoleInterface.md)                   |             |
| [`UserTypeInterface`](./classes/PhalconKit/Models/Interfaces/UserTypeInterface.md)                   |             |
| [`ValidatorInterface`](./classes/PhalconKit/Models/Interfaces/ValidatorInterface.md)                 |             |
| [`WorkspaceInterface`](./classes/PhalconKit/Models/Interfaces/WorkspaceInterface.md)                 |             |
| [`WorkspaceLangInterface`](./classes/PhalconKit/Models/Interfaces/WorkspaceLangInterface.md)         |             |

### \PhalconKit\Modules\Admin


| Class                                                            | Description      |
|------------------------------------------------------------------|------------------|
| [`Controller`](./classes/PhalconKit/Modules/Admin/Controller.md) | Class Controller |
| [`Module`](./classes/PhalconKit/Modules/Admin/Module.md)         |                  |

### \PhalconKit\Modules\Admin\Controllers


| Class                                                                                        | Description      |
|----------------------------------------------------------------------------------------------|------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Admin/Controllers/AbstractController.md) | Class Controller |
| [`ErrorController`](./classes/PhalconKit/Modules/Admin/Controllers/ErrorController.md)       | Class Controller |
| [`IndexController`](./classes/PhalconKit/Modules/Admin/Controllers/IndexController.md)       | Class Controller |

### \PhalconKit\Modules\Api


| Class                                                          | Description      |
|----------------------------------------------------------------|------------------|
| [`Controller`](./classes/PhalconKit/Modules/Api/Controller.md) | Class Controller |
| [`Module`](./classes/PhalconKit/Modules/Api/Module.md)         |                  |

### \PhalconKit\Modules\Api\Controllers


| Class                                                                                                        | Description      |
|--------------------------------------------------------------------------------------------------------------|------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Api/Controllers/AbstractController.md)                   | Class Controller |
| [`AuditController`](./classes/PhalconKit/Modules/Api/Controllers/AuditController.md)                         | Class Controller |
| [`AuditDetailController`](./classes/PhalconKit/Modules/Api/Controllers/AuditDetailController.md)             | Class Controller |
| [`AuthController`](./classes/PhalconKit/Modules/Api/Controllers/AuthController.md)                           | Class Controller |
| [`CategoryController`](./classes/PhalconKit/Modules/Api/Controllers/CategoryController.md)                   | Class Controller |
| [`ClamavController`](./classes/PhalconKit/Modules/Api/Controllers/ClamavController.md)                       | Class Controller |
| [`ColumnController`](./classes/PhalconKit/Modules/Api/Controllers/ColumnController.md)                       | Class Controller |
| [`DataController`](./classes/PhalconKit/Modules/Api/Controllers/DataController.md)                           | Class Controller |
| [`EmailController`](./classes/PhalconKit/Modules/Api/Controllers/EmailController.md)                         | Class Controller |
| [`ErrorController`](./classes/PhalconKit/Modules/Api/Controllers/ErrorController.md)                         | Class Controller |
| [`FieldController`](./classes/PhalconKit/Modules/Api/Controllers/FieldController.md)                         | Class Controller |
| [`FileController`](./classes/PhalconKit/Modules/Api/Controllers/FileController.md)                           | Class Controller |
| [`FlagController`](./classes/PhalconKit/Modules/Api/Controllers/FlagController.md)                           | Class Controller |
| [`GroupController`](./classes/PhalconKit/Modules/Api/Controllers/GroupController.md)                         | Class Controller |
| [`IndexController`](./classes/PhalconKit/Modules/Api/Controllers/IndexController.md)                         | Class Controller |
| [`LangController`](./classes/PhalconKit/Modules/Api/Controllers/LangController.md)                           | Class Controller |
| [`LogController`](./classes/PhalconKit/Modules/Api/Controllers/LogController.md)                             | Class Controller |
| [`MenuController`](./classes/PhalconKit/Modules/Api/Controllers/MenuController.md)                           | Class Controller |
| [`MetaController`](./classes/PhalconKit/Modules/Api/Controllers/MetaController.md)                           | Class Controller |
| [`PageController`](./classes/PhalconKit/Modules/Api/Controllers/PageController.md)                           | Class Controller |
| [`PhalconMigrationsController`](./classes/PhalconKit/Modules/Api/Controllers/PhalconMigrationsController.md) | Class Controller |
| [`PostController`](./classes/PhalconKit/Modules/Api/Controllers/PostController.md)                           | Class Controller |
| [`ProfileController`](./classes/PhalconKit/Modules/Api/Controllers/ProfileController.md)                     | Class Controller |
| [`RecordController`](./classes/PhalconKit/Modules/Api/Controllers/RecordController.md)                       | Class Controller |
| [`RoleController`](./classes/PhalconKit/Modules/Api/Controllers/RoleController.md)                           | Class Controller |
| [`SessionController`](./classes/PhalconKit/Modules/Api/Controllers/SessionController.md)                     | Class Controller |
| [`SettingController`](./classes/PhalconKit/Modules/Api/Controllers/SettingController.md)                     | Class Controller |
| [`TableController`](./classes/PhalconKit/Modules/Api/Controllers/TableController.md)                         | Class Controller |
| [`TemplateController`](./classes/PhalconKit/Modules/Api/Controllers/TemplateController.md)                   | Class Controller |
| [`TestController`](./classes/PhalconKit/Modules/Api/Controllers/TestController.md)                           | Class Controller |
| [`TranslateController`](./classes/PhalconKit/Modules/Api/Controllers/TranslateController.md)                 | Class Controller |
| [`TranslateFieldController`](./classes/PhalconKit/Modules/Api/Controllers/TranslateFieldController.md)       | Class Controller |
| [`TranslateTableController`](./classes/PhalconKit/Modules/Api/Controllers/TranslateTableController.md)       | Class Controller |
| [`TypeController`](./classes/PhalconKit/Modules/Api/Controllers/TypeController.md)                           | Class Controller |
| [`UserController`](./classes/PhalconKit/Modules/Api/Controllers/UserController.md)                           | Class Controller |
| [`WorkspaceController`](./classes/PhalconKit/Modules/Api/Controllers/WorkspaceController.md)                 | Class Controller |

### \PhalconKit\Modules\Api\Transformers


| Class                                                                                     | Description                                                                                  |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [`RecordTransformer`](./classes/PhalconKit/Modules/Api/Transformers/RecordTransformer.md) | This class extends the TransformerAbstract class and implements the InjectionAwareInterface. |

### \PhalconKit\Modules\Cli


| Class                                                  | Description |
|--------------------------------------------------------|-------------|
| [`Module`](./classes/PhalconKit/Modules/Cli/Module.md) |             |
| [`Task`](./classes/PhalconKit/Modules/Cli/Task.md)     |             |

### \PhalconKit\Modules\Cli\Tasks


| Class                                                                              | Description |
|------------------------------------------------------------------------------------|-------------|
| [`AbstractTask`](./classes/PhalconKit/Modules/Cli/Tasks/AbstractTask.md)           |             |
| [`CacheTask`](./classes/PhalconKit/Modules/Cli/Tasks/CacheTask.md)                 |             |
| [`CronTask`](./classes/PhalconKit/Modules/Cli/Tasks/CronTask.md)                   |             |
| [`DatabaseTask`](./classes/PhalconKit/Modules/Cli/Tasks/DatabaseTask.md)           |             |
| [`DataLifeCycleTask`](./classes/PhalconKit/Modules/Cli/Tasks/DataLifeCycleTask.md) |             |
| [`ErrorTask`](./classes/PhalconKit/Modules/Cli/Tasks/ErrorTask.md)                 |             |
| [`FakerTask`](./classes/PhalconKit/Modules/Cli/Tasks/FakerTask.md)                 |             |
| [`HelpTask`](./classes/PhalconKit/Modules/Cli/Tasks/HelpTask.md)                   |             |
| [`ScaffoldTask`](./classes/PhalconKit/Modules/Cli/Tasks/ScaffoldTask.md)           |             |
| [`TsScaffoldTask`](./classes/PhalconKit/Modules/Cli/Tasks/TsScaffoldTask.md)       |             |
| [`UserTask`](./classes/PhalconKit/Modules/Cli/Tasks/UserTask.md)                   |             |

### \PhalconKit\Modules\Cli\Tasks\Traits


| Trait                                                                               | Description          |
|-------------------------------------------------------------------------------------|----------------------|
| [`DatabaseTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/DatabaseTrait.md)   |                      |
| [`DescribesTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/DescribesTrait.md) | Trait DescribesTrait |
| [`ScaffoldTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/ScaffoldTrait.md)   | Trait DescribesTrait |
| [`UserTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/UserTrait.md)           |                      |

### \PhalconKit\Modules\Frontend


| Class                                                               | Description      |
|---------------------------------------------------------------------|------------------|
| [`Controller`](./classes/PhalconKit/Modules/Frontend/Controller.md) | Class Controller |
| [`Module`](./classes/PhalconKit/Modules/Frontend/Module.md)         |                  |

### \PhalconKit\Modules\Frontend\Controllers


| Class                                                                                           | Description      |
|-------------------------------------------------------------------------------------------------|------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Frontend/Controllers/AbstractController.md) | Class Controller |
| [`ErrorController`](./classes/PhalconKit/Modules/Frontend/Controllers/ErrorController.md)       | Class Controller |
| [`IndexController`](./classes/PhalconKit/Modules/Frontend/Controllers/IndexController.md)       | Class Controller |

### \PhalconKit\Modules\Oauth2


| Class                                                             | Description      |
|-------------------------------------------------------------------|------------------|
| [`Controller`](./classes/PhalconKit/Modules/Oauth2/Controller.md) | Class Controller |
| [`Module`](./classes/PhalconKit/Modules/Oauth2/Module.md)         |                  |

### \PhalconKit\Modules\Oauth2\Controllers


| Class                                                                                           | Description      |
|-------------------------------------------------------------------------------------------------|------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Oauth2/Controllers/AbstractController.md)   | Class Controller |
| [`ClientController`](./classes/PhalconKit/Modules/Oauth2/Controllers/ClientController.md)       | Class Controller |
| [`FacebookController`](./classes/PhalconKit/Modules/Oauth2/Controllers/FacebookController.md)   | Class Controller |
| [`GithubController`](./classes/PhalconKit/Modules/Oauth2/Controllers/GithubController.md)       | Class Controller |
| [`GoogleController`](./classes/PhalconKit/Modules/Oauth2/Controllers/GoogleController.md)       | Class Controller |
| [`InstagramController`](./classes/PhalconKit/Modules/Oauth2/Controllers/InstagramController.md) | Class Controller |
| [`LinkedinController`](./classes/PhalconKit/Modules/Oauth2/Controllers/LinkedinController.md)   | Class Controller |

### \PhalconKit\Modules\Ws


| Class                                                 | Description |
|-------------------------------------------------------|-------------|
| [`Module`](./classes/PhalconKit/Modules/Ws/Module.md) |             |
| [`Task`](./classes/PhalconKit/Modules/Ws/Task.md)     |             |

### \PhalconKit\Modules\Ws\Tasks


| Class                                                                   | Description |
|-------------------------------------------------------------------------|-------------|
| [`AbstractTask`](./classes/PhalconKit/Modules/Ws/Tasks/AbstractTask.md) |             |
| [`ErrorTask`](./classes/PhalconKit/Modules/Ws/Tasks/ErrorTask.md)       |             |

### \PhalconKit\Mvc


| Class                                                    | Description                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`Application`](./classes/PhalconKit/Mvc/Application.md) | Simple HMVC - allow requests with namespaces and modules
{@inheritdoc}                                                                                                                                                                                                                                                                                    |
| [`Controller`](./classes/PhalconKit/Mvc/Controller.md)   | Class Controller                                                                                                                                                                                                                                                                                                                                          |
| [`Dispatcher`](./classes/PhalconKit/Mvc/Dispatcher.md)   | {@inheritDoc}                                                                                                                                                                                                                                                                                                                                             |
| [`Model`](./classes/PhalconKit/Mvc/Model.md)             | Events
- afterCreate
- afterDelete
- afterFetch
- afterSave
- afterUpdate
- afterValidation
- afterValidationOnCreate
- afterValidationOnUpdate
- beforeDelete
- beforeCreate
- beforeSave
- beforeUpdate
- beforeValidation
- beforeValidationOnCreate
- beforeValidationOnUpdate
- notDeleted
- notSaved
- onValidationFails
- prepareSave
- validation |
| [`Module`](./classes/PhalconKit/Mvc/Module.md)           |                                                                                                                                                                                                                                                                                                                                                           |
| [`Router`](./classes/PhalconKit/Mvc/Router.md)           | {@inheritDoc}                                                                                                                                                                                                                                                                                                                                             |
| [`Url`](./classes/PhalconKit/Mvc/Url.md)                 | {@inheritDoc}                                                                                                                                                                                                                                                                                                                                             |
| [`View`](./classes/PhalconKit/Mvc/View.md)               | {@inheritdoc}                                                                                                                                                                                                                                                                                                                                             |


| Interface                                                      | Description |
|----------------------------------------------------------------|-------------|
| [`ModelInterface`](./classes/PhalconKit/Mvc/ModelInterface.md) |             |

### \PhalconKit\Mvc\Controller


| Class                                                       | Description      |
|-------------------------------------------------------------|------------------|
| [`Error`](./classes/PhalconKit/Mvc/Controller/Error.md)     | Class Controller |
| [`Rest`](./classes/PhalconKit/Mvc/Controller/Rest.md)       | Class Controller |
| [`Restful`](./classes/PhalconKit/Mvc/Controller/Restful.md) | Class Controller |


| Interface                                                                     | Description |
|-------------------------------------------------------------------------------|-------------|
| [`RestfulInterface`](./classes/PhalconKit/Mvc/Controller/RestfulInterface.md) |             |
| [`RestInterface`](./classes/PhalconKit/Mvc/Controller/RestInterface.md)       |             |

### \PhalconKit\Mvc\Controller\Behavior\Model


| Class                                                                      | Description |
|----------------------------------------------------------------------------|-------------|
| [`Create`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Create.md)   |             |
| [`Delete`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Delete.md)   |             |
| [`Restore`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Restore.md) |             |
| [`Update`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Update.md)   |             |

### \PhalconKit\Mvc\Controller\Behavior\Query


| Class                                                                                            | Description |
|--------------------------------------------------------------------------------------------------|-------------|
| [`RemoveBind`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveBind.md)                 |             |
| [`RemoveCacheConfig`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveCacheConfig.md)   |             |
| [`RemoveColumn`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveColumn.md)             |             |
| [`RemoveConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveConditions.md)     |             |
| [`RemoveDefaultLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveDefaultLimit.md) |             |
| [`RemoveDistinct`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveDistinct.md)         |             |
| [`RemoveGroup`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveGroup.md)               |             |
| [`RemoveHaving`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveHaving.md)             |             |
| [`RemoveJoins`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveJoins.md)               |             |
| [`RemoveLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveLimit.md)               |             |
| [`RemoveMaxLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveMaxLimit.md)         |             |
| [`RemoveOffset`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveOffset.md)             |             |
| [`RemoveWith`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveWith.md)                 |             |

### \PhalconKit\Mvc\Controller\Behavior\Query\Conditions


| Class                                                                                                                                                               | Description |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [`RemoveDefaultFilterCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultFilterCondition.md)                                     |             |
| [`RemoveDefaultIdentityCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultIdentityCondition.md)                                 |             |
| [`RemoveDefaultPermissionCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultPermissionCondition.md)                             |             |
| [`RemoveDefaultSearchCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultSearchCondition.md)                                     |             |
| [`RemoveDefaultSoftDeleteCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultSoftDeleteCondition.md)                             |             |
| [`RemoveDefaultSoftDeleteConditionWhileFiltering`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultSoftDeleteConditionWhileFiltering.md) |             |
| [`RemoveFilterConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveFilterConditions.md)                                                 |             |
| [`RemoveIdentityConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveIdentityConditions.md)                                             |             |
| [`RemovePermissionConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemovePermissionConditions.md)                                         |             |
| [`RemoveSearchConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveSearchConditions.md)                                                 |             |
| [`RemoveSoftDeleteConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveSoftDeleteConditions.md)                                         |             |
| [`RemoveSoftDeleteConditionsWhileFiltering`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveSoftDeleteConditionsWhileFiltering.md)             |             |

### \PhalconKit\Mvc\Controller\Behavior\Query\Fields


| Class                                                                                                   | Description |
|---------------------------------------------------------------------------------------------------------|-------------|
| [`RemoveExposeFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveExposeFields.md) |             |
| [`RemoveFilterFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveFilterFields.md) |             |
| [`RemoveMapFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveMapFields.md)       |             |
| [`RemoveSaveFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveSaveFields.md)     |             |
| [`RemoveSearchFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveSearchFields.md) |             |

### \PhalconKit\Mvc\Controller\Behavior\Skip


| Class                                                                                                     | Description |
|-----------------------------------------------------------------------------------------------------------|-------------|
| [`SkipBind`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipBind.md)                               |             |
| [`SkipBindTypes`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipBindTypes.md)                     |             |
| [`SkipCache`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipCache.md)                             |             |
| [`SkipColumns`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipColumns.md)                         |             |
| [`SkipConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipConditions.md)                   |             |
| [`SkipDistinct`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipDistinct.md)                       |             |
| [`SkipFilterCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipFilterCondition.md)         |             |
| [`SkipGroup`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipGroup.md)                             |             |
| [`SkipHaving`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipHaving.md)                           |             |
| [`SkipIdentityCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipIdentityCondition.md)     |             |
| [`SkipJoins`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipJoins.md)                             |             |
| [`SkipLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipLimit.md)                             |             |
| [`SkipOffset`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipOffset.md)                           |             |
| [`SkipOrder`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipOrder.md)                             |             |
| [`SkipPermissionCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipPermissionCondition.md) |             |
| [`SkipSearchCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipSearchCondition.md)         |             |
| [`SkipSoftDeleteCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipSoftDeleteCondition.md) |             |
| [`SkipWhiteList`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipWhiteList.md)                     |             |

### \PhalconKit\Mvc\Controller\Traits


| Trait                                                                        | Description                                                                                       |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [`Behavior`](./classes/PhalconKit/Mvc/Controller/Traits/Behavior.md)         |                                                                                                   |
| [`Debug`](./classes/PhalconKit/Mvc/Controller/Traits/Debug.md)               |                                                                                                   |
| [`DynamicJoins`](./classes/PhalconKit/Mvc/Controller/Traits/DynamicJoins.md) |                                                                                                   |
| [`Export`](./classes/PhalconKit/Mvc/Controller/Traits/Export.md)             | Provides some utility methods to export data                                                      |
| [`Expose`](./classes/PhalconKit/Mvc/Controller/Traits/Expose.md)             |                                                                                                   |
| [`Fractal`](./classes/PhalconKit/Mvc/Controller/Traits/Fractal.md)           | This trait provides methods for working with Fractal, a library for transforming data structures. |
| [`Model`](./classes/PhalconKit/Mvc/Controller/Traits/Model.md)               |                                                                                                   |
| [`Params`](./classes/PhalconKit/Mvc/Controller/Traits/Params.md)             |                                                                                                   |
| [`Query`](./classes/PhalconKit/Mvc/Controller/Traits/Query.md)               | Class Query                                                                                       |
| [`RestResponse`](./classes/PhalconKit/Mvc/Controller/Traits/RestResponse.md) |                                                                                                   |
| [`StatusCode`](./classes/PhalconKit/Mvc/Controller/Traits/StatusCode.md)     | Set the status code to the response                                                               |

### \PhalconKit\Mvc\Controller\Traits\Abstracts


| Trait                                                                                                  | Description              |
|--------------------------------------------------------------------------------------------------------|--------------------------|
| [`AbstractBehavior`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractBehavior.md)         |                          |
| [`AbstractDebug`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractDebug.md)               |                          |
| [`AbstractExport`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractExport.md)             |                          |
| [`AbstractExpose`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractExpose.md)             |                          |
| [`AbstractFractal`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractFractal.md)           |                          |
| [`AbstractInjectable`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractInjectable.md)     | Trait AbstractInjectable |
| [`AbstractModel`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractModel.md)               |                          |
| [`AbstractParams`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractParams.md)             |                          |
| [`AbstractQuery`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractQuery.md)               |                          |
| [`AbstractRestResponse`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractRestResponse.md) |                          |
| [`AbstractStatusCode`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractStatusCode.md)     |                          |

### \PhalconKit\Mvc\Controller\Traits\Abstracts\Query


| Trait                                                                                                    | Description                                                                   |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`AbstractBind`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractBind.md)             |                                                                               |
| [`AbstractCache`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractCache.md)           |                                                                               |
| [`AbstractColumn`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractColumn.md)         |                                                                               |
| [`AbstractConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractConditions.md) |                                                                               |
| [`AbstractDistinct`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractDistinct.md)     |                                                                               |
| [`AbstractFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractFields.md)         |                                                                               |
| [`AbstractGroup`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractGroup.md)           |                                                                               |
| [`AbstractHaving`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractHaving.md)         |                                                                               |
| [`AbstractJoins`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractJoins.md)           |                                                                               |
| [`AbstractLimit`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractLimit.md)           | The Limit trait provides methods to handle query limits.                      |
| [`AbstractOffset`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractOffset.md)         | This trait provides functionality to set and get an offset value for a query. |
| [`AbstractOrder`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractOrder.md)           |                                                                               |
| [`AbstractSave`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractSave.md)             |                                                                               |
| [`AbstractWith`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractWith.md)             |                                                                               |

### \PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions


| Trait                                                                                                                                   | Description |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [`AbstractFilterConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractFilterConditions.md)         |             |
| [`AbstractIdentityConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractIdentityConditions.md)     |             |
| [`AbstractPermissionConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractPermissionConditions.md) |             |
| [`AbstractSearchConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractSearchConditions.md)         |             |
| [`AbstractSoftDeleteConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractSoftDeleteConditions.md) |             |

### \PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields


| Trait                                                                                                               | Description                                                                         |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`AbstractExposeFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractExposeFields.md) | The AbstractExposeFields trait provides a base implementation for exposing fields.  |
| [`AbstractFilterFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractFilterFields.md) | The AbstractFilterFields trait provides a base implementation for filtering fields. |
| [`AbstractMapFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractMapFields.md)       | The AbstractMapFields trait provides a base implementation for mapping fields.      |
| [`AbstractSaveFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractSaveFields.md)     | The AbstractSaveFields trait provides a base implementation for saving fields.      |
| [`AbstractSearchFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractSearchFields.md) | The AbstractSearchFields trait provides a base implementation for searching fields. |

### \PhalconKit\Mvc\Controller\Traits\Actions


| Trait                                                                                  | Description           |
|----------------------------------------------------------------------------------------|-----------------------|
| [`AuthActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/AuthActions.md)     |                       |
| [`ClamavActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/ClamavActions.md) |                       |
| [`ErrorActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/ErrorActions.md)   | Default Error Actions |
| [`RestActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/RestActions.md)     |                       |

### \PhalconKit\Mvc\Controller\Traits\Actions\Rest


| Trait                                                                                           | Description |
|-------------------------------------------------------------------------------------------------|-------------|
| [`AverageAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/AverageAction.md)     |             |
| [`CountAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/CountAction.md)         |             |
| [`DeleteAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/DeleteAction.md)       |             |
| [`DistinctAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/DistinctAction.md)   |             |
| [`ExportAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/ExportAction.md)       |             |
| [`FindAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/FindAction.md)           |             |
| [`FindFirstAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/FindFirstAction.md) |             |
| [`IndexAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/IndexAction.md)         |             |
| [`MaximumAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/MaximumAction.md)     |             |
| [`MinimumAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/MinimumAction.md)     |             |
| [`NewAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/NewAction.md)             |             |
| [`ReorderAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/ReorderAction.md)     |             |
| [`RestoreAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/RestoreAction.md)     |             |
| [`SaveAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/SaveAction.md)           |             |
| [`SumAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/SumAction.md)             |             |

### \PhalconKit\Mvc\Controller\Traits\Interfaces


| Interface                                                                                                 | Description |
|-----------------------------------------------------------------------------------------------------------|-------------|
| [`BehaviorInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/BehaviorInterface.md)         |             |
| [`CacheInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/CacheInterface.md)               |             |
| [`DebugInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/DebugInterface.md)               |             |
| [`ExportInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ExportInterface.md)             |             |
| [`ExposeInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ExposeInterface.md)             |             |
| [`FractalInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/FractalInterface.md)           |             |
| [`ModelInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ModelInterface.md)               |             |
| [`ParamsInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ParamsInterface.md)             |             |
| [`RestResponseInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/RestResponseInterface.md) |             |
| [`StatusCodeInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/StatusCodeInterface.md)     |             |

### \PhalconKit\Mvc\Controller\Traits\Query


| Trait                                                                          | Description                                                                   |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`Bind`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Bind.md)             |                                                                               |
| [`Cache`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Cache.md)           | This trait provides methods for caching data for the query.                   |
| [`Column`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Column.md)         |                                                                               |
| [`Conditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions.md) |                                                                               |
| [`Distinct`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Distinct.md)     |                                                                               |
| [`Fields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields.md)         |                                                                               |
| [`Group`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Group.md)           |                                                                               |
| [`Having`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Having.md)         |                                                                               |
| [`Joins`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Joins.md)           |                                                                               |
| [`Limit`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Limit.md)           | The Limit trait provides methods to handle query limits.                      |
| [`Offset`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Offset.md)         | This trait provides functionality to set and get an offset value for a query. |
| [`Order`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Order.md)           | The Order trait sets and retrieves the order parameter for the query.         |
| [`Save`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Save.md)             |                                                                               |
| [`With`](./classes/PhalconKit/Mvc/Controller/Traits/Query/With.md)             |                                                                               |

### \PhalconKit\Mvc\Controller\Traits\Query\Conditions


| Trait                                                                                                         | Description                                                                   |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`FilterConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/FilterConditions.md)         |                                                                               |
| [`IdentityConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/IdentityConditions.md)     |                                                                               |
| [`PermissionConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/PermissionConditions.md) | This trait provides methods for managing permission conditions for the query. |
| [`SearchConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/SearchConditions.md)         | This trait provides methods for managing search conditions.                   |
| [`SoftDeleteConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/SoftDeleteConditions.md) |                                                                               |

### \PhalconKit\Mvc\Controller\Traits\Query\Fields


| Trait                                                                                     | Description |
|-------------------------------------------------------------------------------------------|-------------|
| [`ExposeFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/ExposeFields.md) |             |
| [`FilterFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/FilterFields.md) |             |
| [`MapFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/MapFields.md)       |             |
| [`SaveFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/SaveFields.md)     |             |
| [`SearchFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/SearchFields.md) |             |

### \PhalconKit\Mvc\Dispatcher


| Class                                                               | Description                                                                                               |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`Camelize`](./classes/PhalconKit/Mvc/Dispatcher/Camelize.md)       |                                                                                                           |
| [`Error`](./classes/PhalconKit/Mvc/Dispatcher/Error.md)             |                                                                                                           |
| [`Logger`](./classes/PhalconKit/Mvc/Dispatcher/Logger.md)           |                                                                                                           |
| [`Maintenance`](./classes/PhalconKit/Mvc/Dispatcher/Maintenance.md) | Maintenance Dispatcher Plugin
Redirect to the maintenance module/controller/action                        |
| [`Module`](./classes/PhalconKit/Mvc/Dispatcher/Module.md)           |                                                                                                           |
| [`Preflight`](./classes/PhalconKit/Mvc/Dispatcher/Preflight.md)     | Class Preflight                                                                                           |
| [`Rest`](./classes/PhalconKit/Mvc/Dispatcher/Rest.md)               |                                                                                                           |
| [`Security`](./classes/PhalconKit/Mvc/Dispatcher/Security.md)       | This is the security plugin which controls that users only have access to the modules they're assigned to |

### \PhalconKit\Mvc\Model


| Class                                                  | Description |
|--------------------------------------------------------|-------------|
| [`Manager`](./classes/PhalconKit/Mvc/Model/Manager.md) |             |


| Interface                                                                | Description |
|--------------------------------------------------------------------------|-------------|
| [`ManagerInterface`](./classes/PhalconKit/Mvc/Model/ManagerInterface.md) |             |

### \PhalconKit\Mvc\Model\Behavior


| Class                                                                       | Description                                                                     |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [`Action`](./classes/PhalconKit/Mvc/Model/Behavior/Action.md)               |                                                                                 |
| [`Blameable`](./classes/PhalconKit/Mvc/Model/Behavior/Blameable.md)         | PhalconKit\Mvc\Model\Traits\Behavior\Blameable                                  |
| [`Conditional`](./classes/PhalconKit/Mvc/Model/Behavior/Conditional.md)     | PhalconKit\Mvc\Model\Traits\Behavior\Conditional                                |
| [`Position`](./classes/PhalconKit/Mvc/Model/Behavior/Position.md)           |                                                                                 |
| [`Security`](./classes/PhalconKit/Mvc/Model/Behavior/Security.md)           | The Security class provides methods for access control and permission checking. |
| [`Snapshot`](./classes/PhalconKit/Mvc/Model/Behavior/Snapshot.md)           |                                                                                 |
| [`SoftDelete`](./classes/PhalconKit/Mvc/Model/Behavior/SoftDelete.md)       | {@inheritDoc}                                                                   |
| [`Transformable`](./classes/PhalconKit/Mvc/Model/Behavior/Transformable.md) | PhalconKit\Mvc\Model\Traits\Behavior\Transformable                              |

### \PhalconKit\Mvc\Model\Behavior\Traits


| Trait                                                                                | Description                                                                                                                       |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [`ProgressTrait`](./classes/PhalconKit/Mvc/Model/Behavior/Traits/ProgressTrait.md)   | Allow to enable or disable trait
on the current model instance ($progress)
or globally for every model instance ($staticProgress) |
| [`SkippableTrait`](./classes/PhalconKit/Mvc/Model/Behavior/Traits/SkippableTrait.md) | Allow to enable or disable trait
on the current model instance ($enabled)
or globally for every model instance ($staticEnabled)   |

### \PhalconKit\Mvc\Model\EagerLoading


| Class                                                                         | Description                                                   |
|-------------------------------------------------------------------------------|---------------------------------------------------------------|
| [`EagerLoad`](./classes/PhalconKit/Mvc/Model/EagerLoading/EagerLoad.md)       | Represents a level in the relations tree to be eagerly loaded |
| [`Loader`](./classes/PhalconKit/Mvc/Model/EagerLoading/Loader.md)             |                                                               |
| [`QueryBuilder`](./classes/PhalconKit/Mvc/Model/EagerLoading/QueryBuilder.md) |                                                               |

### \PhalconKit\Mvc\Model\Interfaces


| Interface                                                                                     | Description                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------|
| [`AttributeInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/AttributeInterface.md)       |                                             |
| [`BehaviorInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/BehaviorInterface.md)         |                                             |
| [`BlameableInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/BlameableInterface.md)       |                                             |
| [`EagerLoadInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/EagerLoadInterface.md)       |                                             |
| [`ExposeInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/ExposeInterface.md)             |                                             |
| [`HashInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/HashInterface.md)                 |                                             |
| [`IdentityInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/IdentityInterface.md)         |                                             |
| [`InstanceInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/InstanceInterface.md)         |                                             |
| [`JsonInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/JsonInterface.md)                 |                                             |
| [`LocaleInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/LocaleInterface.md)             |                                             |
| [`MetaDataInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/MetaDataInterface.md)         |                                             |
| [`OptionsInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/OptionsInterface.md)           |                                             |
| [`PositionInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/PositionInterface.md)         |                                             |
| [`RelationshipInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/RelationshipInterface.md) | Interface for model relationship management |
| [`ReplicationInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/ReplicationInterface.md)   |                                             |
| [`SecurityInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SecurityInterface.md)         |                                             |
| [`SlugInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SlugInterface.md)                 |                                             |
| [`SnapshotInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SnapshotInterface.md)         |                                             |
| [`SoftDeleteInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SoftDeleteInterface.md)     |                                             |
| [`ValidateInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/ValidateInterface.md)         |                                             |

### \PhalconKit\Mvc\Model\Interfaces\Blameable


| Interface                                                                                       | Description |
|-------------------------------------------------------------------------------------------------|-------------|
| [`BlameAtInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/BlameAtInterface.md)   |             |
| [`CreatedInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/CreatedInterface.md)   |             |
| [`DeletedInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/DeletedInterface.md)   |             |
| [`RestoredInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/RestoredInterface.md) |             |
| [`UpdatedInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/UpdatedInterface.md)   |             |

### \PhalconKit\Mvc\Model\Traits


| Trait                                                                   | Description                                                                                                   |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [`Attribute`](./classes/PhalconKit/Mvc/Model/Traits/Attribute.md)       | This trait provides methods to get and set attributes in a model using the get/set methods                    |
| [`Behavior`](./classes/PhalconKit/Mvc/Model/Traits/Behavior.md)         | Trait Behavior                                                                                                |
| [`Blameable`](./classes/PhalconKit/Mvc/Model/Traits/Blameable.md)       |                                                                                                               |
| [`Cache`](./classes/PhalconKit/Mvc/Model/Traits/Cache.md)               | Flush Cache on changes                                                                                        |
| [`Count`](./classes/PhalconKit/Mvc/Model/Traits/Count.md)               | Trait Count                                                                                                   |
| [`EagerLoad`](./classes/PhalconKit/Mvc/Model/Traits/EagerLoad.md)       |                                                                                                               |
| [`Events`](./classes/PhalconKit/Mvc/Model/Traits/Events.md)             |                                                                                                               |
| [`Expose`](./classes/PhalconKit/Mvc/Model/Traits/Expose.md)             |                                                                                                               |
| [`FindIn`](./classes/PhalconKit/Mvc/Model/Traits/FindIn.md)             |                                                                                                               |
| [`Hash`](./classes/PhalconKit/Mvc/Model/Traits/Hash.md)                 |                                                                                                               |
| [`Identity`](./classes/PhalconKit/Mvc/Model/Traits/Identity.md)         | This trait provides convenient methods for managing user identity and authentication within a model.          |
| [`Instance`](./classes/PhalconKit/Mvc/Model/Traits/Instance.md)         |                                                                                                               |
| [`Json`](./classes/PhalconKit/Mvc/Model/Traits/Json.md)                 | Trait Json                                                                                                    |
| [`LifeCycle`](./classes/PhalconKit/Mvc/Model/Traits/LifeCycle.md)       |                                                                                                               |
| [`Locale`](./classes/PhalconKit/Mvc/Model/Traits/Locale.md)             | This trait provides functionality to handle localization in models.                                           |
| [`MetaData`](./classes/PhalconKit/Mvc/Model/Traits/MetaData.md)         | The MetaData trait provides methods for retrieving metadata information about a model or entity.              |
| [`Options`](./classes/PhalconKit/Mvc/Model/Traits/Options.md)           | The Options trait provides methods for managing options using an options manager.                             |
| [`Position`](./classes/PhalconKit/Mvc/Model/Traits/Position.md)         | The Position trait is used to manage the position behavior of an object.                                      |
| [`Relationship`](./classes/PhalconKit/Mvc/Model/Traits/Relationship.md) | Allow to automagically save relationship                                                                      |
| [`Replication`](./classes/PhalconKit/Mvc/Model/Traits/Replication.md)   | Replica Lag Workaround
Prevents Phalcon to use read connection while
it might be lagging behind the master db |
| [`Security`](./classes/PhalconKit/Mvc/Model/Traits/Security.md)         | The Security trait provides methods to handle security-related functionalities.                               |
| [`Slug`](./classes/PhalconKit/Mvc/Model/Traits/Slug.md)                 |                                                                                                               |
| [`Snapshot`](./classes/PhalconKit/Mvc/Model/Traits/Snapshot.md)         | Trait that provides snapshot functionality for a model.                                                       |
| [`SoftDelete`](./classes/PhalconKit/Mvc/Model/Traits/SoftDelete.md)     | This trait provides soft delete functionality to a model class.                                               |
| [`Uuid`](./classes/PhalconKit/Mvc/Model/Traits/Uuid.md)                 |                                                                                                               |
| [`Validate`](./classes/PhalconKit/Mvc/Model/Traits/Validate.md)         |                                                                                                               |

### \PhalconKit\Mvc\Model\Traits\Abstracts


| Trait                                                                                               | Description |
|-----------------------------------------------------------------------------------------------------|-------------|
| [`AbstractBehavior`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractBehavior.md)           |             |
| [`AbstractBlameable`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractBlameable.md)         |             |
| [`AbstractEntity`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractEntity.md)               |             |
| [`AbstractEventsManager`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractEventsManager.md) |             |
| [`AbstractIdentity`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractIdentity.md)           |             |
| [`AbstractInjectable`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractInjectable.md)       |             |
| [`AbstractInstance`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractInstance.md)           |             |
| [`AbstractLocale`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractLocale.md)               |             |
| [`AbstractMetaData`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractMetaData.md)           |             |
| [`AbstractModelsCache`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractModelsCache.md)     |             |
| [`AbstractModelsManager`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractModelsManager.md) |             |
| [`AbstractOptions`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractOptions.md)             |             |
| [`AbstractSave`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractSave.md)                   |             |

### \PhalconKit\Mvc\Model\Traits\Blameable


| Trait                                                                     | Description |
|---------------------------------------------------------------------------|-------------|
| [`BlameAt`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/BlameAt.md)   |             |
| [`Created`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Created.md)   |             |
| [`Deleted`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Deleted.md)   |             |
| [`Restored`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Restored.md) |             |
| [`Updated`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Updated.md)   |             |

### \PhalconKit\Mvc\Router


| Class                                                           | Description |
|-----------------------------------------------------------------|-------------|
| [`ModuleRoute`](./classes/PhalconKit/Mvc/Router/ModuleRoute.md) |             |

### \PhalconKit\Mvc\View


| Class                                             | Description |
|---------------------------------------------------|-------------|
| [`Error`](./classes/PhalconKit/Mvc/View/Error.md) |             |

### \PhalconKit\Provider


| Class                                                                                 | Description                   |
|---------------------------------------------------------------------------------------|-------------------------------|
| [`AbstractServiceProvider`](./classes/PhalconKit/Provider/AbstractServiceProvider.md) | Class AbstractServiceProvider |


| Interface                                                                               | Description                        |
|-----------------------------------------------------------------------------------------|------------------------------------|
| [`ServiceProviderInterface`](./classes/PhalconKit/Provider/ServiceProviderInterface.md) | Interface ServiceProviderInterface |

### \PhalconKit\Provider\Acl


| Class                                                                     | Description                   |
|---------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Acl/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Annotations


| Class                                                                             | Description                   |
|-----------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Annotations/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Application


| Class                                                                             | Description                   |
|-----------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Application/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Assets


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Assets/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Aws


| Class                                                                     | Description                   |
|---------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Aws/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Cache


| Class                                                                       | Description                   |
|-----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Cache/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Clamav


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Clamav/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Config


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Config/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Console


| Class                                                                         | Description                   |
|-------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Console/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Cookies


| Class                                                                         | Description                   |
|-------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Cookies/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Crypt


| Class                                                                       | Description                   |
|-----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Crypt/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Database


| Class                                                                          | Description                   |
|--------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Database/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\DatabaseDynamic


| Class                                                                                 | Description                   |
|---------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/DatabaseDynamic/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\DatabaseReadOnly


| Class                                                                                  | Description                   |
|----------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/DatabaseReadOnly/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Debug


| Class                                                                       | Description                   |
|-----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Debug/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Dispatcher


| Class                                                                            | Description                   |
|----------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Dispatcher/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Env


| Class                                                                     | Description                   |
|---------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Env/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Escaper


| Class                                                                         | Description                   |
|-------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Escaper/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\EventsManager


| Class                                                                               | Description                   |
|-------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/EventsManager/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\FileSystem


| Class                                                                            | Description                   |
|----------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/FileSystem/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Filter


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Filter/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Flash


| Class                                                                       | Description                   |
|-----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Flash/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Gravatar


| Class                                                                          | Description                   |
|--------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Gravatar/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Helper


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Helper/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Identity


| Class                                                                          | Description                   |
|--------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Identity/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Imap


| Class                                                                      | Description                   |
|----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Imap/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Jwt


| Class                                                                     | Description                                                               |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`Jwt`](./classes/PhalconKit/Provider/Jwt/Jwt.md)                         | Issue, parse and validate JSON Web Tokens (JWT) as described in RFC 7519. |
| [`ServiceProvider`](./classes/PhalconKit/Provider/Jwt/ServiceProvider.md) | Class AbstractServiceProvider                                             |

### \PhalconKit\Provider\Locale


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Locale/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Logger


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Logger/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Loggers


| Class                                                                         | Description                   |
|-------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Loggers/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\LoremIpsum


| Class                                                                            | Description                   |
|----------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/LoremIpsum/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Mailer


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Mailer/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Models


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Models/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\ModelsCache


| Class                                                                             | Description                   |
|-----------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ModelsCache/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\ModelsManager


| Class                                                                               | Description                   |
|-------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ModelsManager/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\ModelsMetadata


| Class                                                                                | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ModelsMetadata/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\OCR


| Class                                                                     | Description                   |
|---------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/OCR/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Oauth2Client


| Class                                                                              | Description                   |
|------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Oauth2Client/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Oauth2Facebook


| Class                                                                                | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Oauth2Facebook/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Oauth2Google


| Class                                                                              | Description                   |
|------------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Oauth2Google/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\OpenAi


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/OpenAi/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Profiler


| Class                                                                          | Description                   |
|--------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Profiler/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\ReCaptcha


| Class                                                                           | Description                   |
|---------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ReCaptcha/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Redis


| Class                                                                       | Description                   |
|-----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Redis/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Request


| Class                                                                         | Description                   |
|-------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Request/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Response


| Class                                                                          | Description                   |
|--------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Response/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Router


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Router/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Security


| Class                                                                          | Description                   |
|--------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Security/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Session


| Class                                                                         | Description                   |
|-------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Session/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Swoole


| Class                                                                        | Description                   |
|------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Swoole/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Tag


| Class                                                                     | Description                   |
|---------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Tag/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Translate


| Class                                                                           | Description                   |
|---------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Translate/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Url


| Class                                                                     | Description                   |
|---------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Url/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Utils


| Class                                                                       | Description                   |
|-----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Utils/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Version


| Class                                                                         | Description                   |
|-------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Version/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\View


| Class                                                                      | Description                   |
|----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/View/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\Volt


| Class                                                                      | Description                   |
|----------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Volt/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Provider\WebSocket


| Class                                                                           | Description                   |
|---------------------------------------------------------------------------------|-------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/WebSocket/ServiceProvider.md) | Class AbstractServiceProvider |

### \PhalconKit\Router


| Interface                                                           | Description |
|---------------------------------------------------------------------|-------------|
| [`RouterInterface`](./classes/PhalconKit/Router/RouterInterface.md) |             |

### \PhalconKit\Support


| Class                                                            | Description                                                                              |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [`Debug`](./classes/PhalconKit/Support/Debug.md)                 | Provides debug capabilities to Phalcon Kit applications                                  |
| [`Env`](./classes/PhalconKit/Support/Env.md)                     | This class provides utilities for managing environment variables and loading .env files. |
| [`Helper`](./classes/PhalconKit/Support/Helper.md)               | Class Helper                                                                             |
| [`HelperFactory`](./classes/PhalconKit/Support/HelperFactory.md) | HelperFactory Class                                                                      |
| [`Models`](./classes/PhalconKit/Support/Models.md)               | Allow to get mapped classes without using magic methods                                  |
| [`Php`](./classes/PhalconKit/Support/Php.md)                     | Class Php                                                                                |
| [`Slug`](./classes/PhalconKit/Support/Slug.md)                   |                                                                                          |
| [`Utils`](./classes/PhalconKit/Support/Utils.md)                 |                                                                                          |
| [`Version`](./classes/PhalconKit/Support/Version.md)             | This class allows to get the installed version of the core                               |


| Trait                                                    | Description                                             |
|----------------------------------------------------------|---------------------------------------------------------|
| [`ModelsMap`](./classes/PhalconKit/Support/ModelsMap.md) | Allow to get mapped classes without using magic methods |

### \PhalconKit\Support\Exposer


| Class                                                        | Description  |
|--------------------------------------------------------------|--------------|
| [`Builder`](./classes/PhalconKit/Support/Exposer/Builder.md) |              |
| [`Exposer`](./classes/PhalconKit/Support/Exposer/Exposer.md) | Class Expose |


| Interface                                                                      | Description |
|--------------------------------------------------------------------------------|-------------|
| [`BuilderInterface`](./classes/PhalconKit/Support/Exposer/BuilderInterface.md) |             |

### \PhalconKit\Support\Helper\Arr


| Class                                                                                   | Description                                                                                                                                                  |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`FlattenKeys`](./classes/PhalconKit/Support/Helper/Arr/FlattenKeys.md)                 | This class provides methods to parse an array into a flatten array with key path separated by a delimiter.                                                   |
| [`RecursiveMap`](./classes/PhalconKit/Support/Helper/Arr/RecursiveMap.md)               | Class RecursiveMap                                                                                                                                           |
| [`RecursiveStrReplace`](./classes/PhalconKit/Support/Helper/Arr/RecursiveStrReplace.md) | This class provides functionality to recursively replace specific patterns in strings
within a nested array structure using a key/value map of replacements. |

### \PhalconKit\Support\Helper\Str


| Class                                                                                   | Description                               |
|-----------------------------------------------------------------------------------------|-------------------------------------------|
| [`NormalizeLineBreaks`](./classes/PhalconKit/Support/Helper/Str/NormalizeLineBreaks.md) | Normalize Line Breaks                     |
| [`RemoveNonPrintable`](./classes/PhalconKit/Support/Helper/Str/RemoveNonPrintable.md)   | Remove non-printable characters           |
| [`SanitizeUTF8`](./classes/PhalconKit/Support/Helper/Str/SanitizeUTF8.md)               | Sanitize and convert to UTF-8             |
| [`Slugify`](./classes/PhalconKit/Support/Helper/Str/Slugify.md)                         | Creates a slug to be used for pretty URLs |

### \PhalconKit\Support\Options


| Class                                                        | Description |
|--------------------------------------------------------------|-------------|
| [`Manager`](./classes/PhalconKit/Support/Options/Manager.md) |             |


| Trait                                                        | Description                                                                  |
|--------------------------------------------------------------|------------------------------------------------------------------------------|
| [`Options`](./classes/PhalconKit/Support/Options/Options.md) | The Options trait provides a set of methods for managing options in a class. |


| Interface                                                                      | Description |
|--------------------------------------------------------------------------------|-------------|
| [`ManagerInterface`](./classes/PhalconKit/Support/Options/ManagerInterface.md) |             |
| [`OptionsInterface`](./classes/PhalconKit/Support/Options/OptionsInterface.md) |             |

### \PhalconKit\Translate\Adapter


| Class                                                                              | Description                                                                                                                         |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [`NestedNativeArray`](./classes/PhalconKit/Translate/Adapter/NestedNativeArray.md) | NestedNativeArray class is an implementation of the Translate Adapter interface that uses
a nested array as the translation source. |

### \PhalconKit\Ws


| Class                                                 | Description |
|-------------------------------------------------------|-------------|
| [`Dispatcher`](./classes/PhalconKit/Ws/Dispatcher.md) |             |
| [`Module`](./classes/PhalconKit/Ws/Module.md)         |             |
| [`Router`](./classes/PhalconKit/Ws/Router.md)         |             |
| [`Task`](./classes/PhalconKit/Ws/Task.md)             |             |
| [`WebSocket`](./classes/PhalconKit/Ws/WebSocket.md)   |             |


| Interface                                                               | Description |
|-------------------------------------------------------------------------|-------------|
| [`DispatcherInterface`](./classes/PhalconKit/Ws/DispatcherInterface.md) |             |
| [`TaskInterface`](./classes/PhalconKit/Ws/TaskInterface.md)             |             |
