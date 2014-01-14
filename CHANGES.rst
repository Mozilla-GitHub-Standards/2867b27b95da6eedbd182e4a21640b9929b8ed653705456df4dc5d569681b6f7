0.3.2 - 2014-01-14
==================

- Use CEF v0.5.1 which allows CEF messages to be encoded as unicode strings.

0.3.1 - 2014-01-13
==================

- Added unicode "band aid" to forcibly convert strings to unicode if the
  protobuf library barfs on non-ASCII input.

0.3 - 2013-09-23
================

- dropped syslog-options as they are not relevant for heka-py-cef
- First official release compatible with heka 0.3


0.2 - 2012-10-01
==================

- Added syslog support for CEF mesages

0.1
==================

- initial release
