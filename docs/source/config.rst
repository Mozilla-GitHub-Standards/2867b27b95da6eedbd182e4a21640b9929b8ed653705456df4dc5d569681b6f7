Configuration
=============

Configuration is normally handled through Metlog's configuration
system using INI configuration files. A psutil plugin must use the
`metlog_cef.cef_plugin:config_plugin` as the provider of the
plugin.  The suffix of the configuration section name is used to
set the method name on the Metlog client. Any part after
`metlog_plugin_` will be used as the method name.

In the following example, we will bind a method `cef` into the
Metlog client where we will allow network messages to be sent to
the Metlog server. ::

    [metlog_plugin_cef]
    provider=metlog_cef.cef_plugin:config_plugin

The CEF plugin requires no other options to be specified.

Usage
=====

Logging CEF records is similar to using the raw CEF library.
Constants from the `cef` library have been exported in the `metlog_cef` module.

For existing code that uses the `cef` library, you will use the `cef`
method of the metlog client.  Your code will change from this ::

    from cef import log_cef, AUTH_FAILURE

    ...

    log_cef("Authentication attemped without username", 5,
            request.environ, request.registry.settings,
            "", signature=AUTH_FAILURE)

to this ::

    from metlog.decorators.base import CLIENT_WRAPPER
    import metlog_cef

    ...

    client = CLIENT_WRAPPER.client
    client.cef("Authentication attemped without username", 5,
            request.environ, request.registry.settings,
            "", signature=metlog_cef.AUTH_FAILURE)

Note that the CEF plugin has exported important constants into the
`metlog_cef` module. You will find all the existing

Constants exported are:

- AUTH_FAILURE
- CAPTCHA_FAILURE
- OVERRIDE_FAILURE
- ACCOUNT_LOCKED
- PASSWD_RESET_CLR

See the `cef <http://pypi.python.org/pypi/cef>`_ library for details on each of the constants.
