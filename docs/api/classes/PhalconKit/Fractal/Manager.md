
Framework-scoped League Fractal manager.

This class currently keeps League Fractal's behavior unchanged. The wrapper
gives PhalconKit controllers, traits, and downstream applications a stable
framework type to depend on when configuring serializers, includes, and
transformers. Future framework-level defaults can be added here without
changing controller method signatures that already type against this manager.

***

* Full name: `\PhalconKit\Fractal\Manager`
* Parent class: [`Manager`](https://fractal.thephpleague.com/){:target="_blank"}

**See Also:**

* https://fractal.thephpleague.com/transformers/
