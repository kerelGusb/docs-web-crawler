## End of life

The Commons HttpClient project is now end of life, and is no longer being developed.
It has been replaced by the [Apache HttpComponents](../) project
in its [HttpClient](../httpcomponents-client-ga) and [HttpCore](../httpcomponents-core-ga/) modules,
which offer better performance and more flexibility.

## User Guide

The HttpClient user guide is designed to help developers use
HttpClient in their applications. While the concept of a user guide
being for developers may seem strange, the term developer is
already in use for people helping to develop HttpClient.

If you are new to HttpClient, make sure to work through the
[Tutorial](tutorial.html) and have a look at the
[Sample Code](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link").
Before reporting problems, read about
[Trouble Shooting](troubleshooting.html)

## Overview

| Document | Description |
| --- | --- |
| [Authentication Guide](authentication.html) | This document describes the authentication schemes supported by HttpClient and how to use them. |
| [Character Encodings](charencodings.html) | Guidelines for correctly detecting the character encoding to use when sending and receiving data with HttpClient. |
| [Redirects Handling](redirects.html) | Provide sample code for custom redirects handling. |
| [Exception Handling](exception-handling.html) | This document outlines common types of errors that the users may encounter and describes the exception handling framework used by HttpClient. |
| [Logging Guide](logging.html) | This document describes the logging mechanism used by HttpClient and how to control what it outputs. |
| [Methods](methods.html) | This document describes the various methods that are provided by HttpClient and how to use them. |
| [Optimization Guide](performance.html) | This document outlines HttpClient performance optimization techniques. |
| [Preference Architecture](preference-api.html) | This document explains the preference architecture used by HttpClient and enumerates standard HttpClient parameters. |
| [Sample Code](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link") | This is a link to the sample code for using HttpClient that is stored in the Subversion repository and is available in source releases of HttpClient. |
| [Trouble Shooting](troubleshooting.html) | This document provides hints and tips for debugging problems with HttpClient. |
| [Tutorial](tutorial.html) | This document provides a simple introductory tutorial for new users of HttpClient. |

---
## End of life

The Commons HttpClient project is now end of life, and is no longer being developed.
It has been replaced by the [Apache HttpComponents](../) project
in its [HttpClient](../httpcomponents-client-ga) and [HttpCore](../httpcomponents-core-ga/) modules,
which offer better performance and more flexibility.

## Features

* Standards based, pure Java, implementation of HTTP versions 1.0 and 1.1
* Full implementation of all HTTP methods (GET, POST, PUT, DELETE,
  HEAD, OPTIONS, and TRACE) in an extensible OO framework.
* Supports encryption with HTTPS (HTTP over SSL) protocol.
* Granular non-standards configuration and tracking.
* Transparent connections through HTTP proxies.
* Tunneled HTTPS connections through HTTP proxies, via the CONNECT method.
* Transparent connections through SOCKS proxies (version 4 & 5) using native Java
  socket support.
* Authentication using Basic, Digest and the encrypting NTLM (NT Lan Manager) methods.
* Plug-in mechanism for custom authentication methods.
* Multi-Part form POST for uploading large files.
* Pluggable secure sockets implementations, making it easier to use third party solutions
* Connection management support for use in multi-threaded applications. Supports setting the
  maximum total connections as well as the maximum connections per host. Detects and closes
  stale connections.
* Automatic Cookie handling for reading Set-Cookie: headers from the server and sending
  them back out in a Cookie: header when appropriate.
* Plug-in mechanism for custom cookie policies.
* Request output streams to avoid buffering any content body by streaming
  directly to the socket to the server.
* Response input streams to efficiently read the response body by streaming
  directly from the socket to the server.
* Persistent connections using KeepAlive in HTTP/1.0 and persistance in HTTP/1.1
* Direct access to the response code and headers sent by the server.
* The ability to set connection timeouts.
* HttpMethods implement the Command Pattern to allow for parallel requests
  and efficient re-use of connections.
* Source code is freely available under the Apache Software License.

## Standards Compliance

*HttpClient* implements the following specifications
endorsed by the Internet Engineering Task Force (IETF)
and the internet at large:

* [RFC1945](http://www.ietf.org/rfc/rfc1945.txt "External Link")
  Hypertext Transfer Protocol -- HTTP/1.0
* [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link")
  Hypertext Transfer Protocol -- HTTP/1.1
* [RFC2617](http://www.ietf.org/rfc/rfc2617.txt "External Link")
  HTTP Authentication: Basic and Digest Access Authentication
* [RFC2109](http://www.ietf.org/rfc/rfc2109.txt "External Link")
  HTTP State Management Mechanism (Cookies)
* [RFC2396](http://www.ietf.org/rfc/rfc2396.txt "External Link")
  Uniform Resource Identifiers (URI): Generic Syntax
* [RFC1867](http://www.ietf.org/rfc/rfc1867.txt "External Link")
  Form-based File Upload in HTML

## Product Comparision

The HTTP protocol is so ubiquitous on the internet that you can find other
client side implementations written in Java. The jdk has the HttpUrlConnection
which is limited and in many ways flawed. This is one reason why Jakarta, and
others free and commercial vendors, have implemented independant HTTP clients.
To help you choose the right solution, one of those commercial vendors, Oakland Software, has a fair
[product comparison](http://www.oaklandsoftware.com/product_16.html#compare "External Link").

---
## Development Process

[http://maven.apache.org/development-process.html](http://maven.apache.org/development-process.html "External Link")

---
## End of life

The Commons HttpClient project is now end of life, and is no longer being developed.
It has been replaced by the [Apache HttpComponents](../) project
in its [HttpClient](../httpcomponents-client-ga) and [HttpCore](../httpcomponents-core-ga/) modules,
which offer better performance and more flexibility.

## 16 December 2007 - HttpClient 3.1 website moved

The website for HttpClient 3.1 has moved to the new domain
of the HttpComponents top level project. The new location is:
  
<http://hc.apache.org/httpclient-3.x/>

## 13 December 2007 - Mailing lists moved

As part of the move to a top level project, the HttpComponents
team has moved the mailing lists to a new domain.
The new mailing list names are:

* [httpclient-users@hc.apache.org](mailto:httpclient-users@hc.apache.org) - user list, renamed from httpclient-user@jakarta.apache.org
* [dev@hc.apache.org](mailto:dev@hc.apache.org) - developer list, renamed from httpcomponents-dev@jakarta.apache.org

Subscribers to the old lists have been moved to the new ones.
No action is required for posting and receiving mails on the
lists, but you may have to update your mail filter rules
with the new list names.
Please see the HttpClient
[mailing list page](mail-lists.html) for
(un)subscription and archive details.

## 22 August 2007 - HttpClient 3.1 released

HttpClient 3.1 has been released. This version adds a number improvements to the
connection management code and fixes a number of minor bugs. It is likely to be the
last non bug fixing release of the HttpClient 3.x codeline.

## 16 March 2007 - HttpClient 3.1-rc1 released

HttpClient 3.1-rc1 has been released. This version fixes a number of issues
found since 3.1-beta1. This release is expected to be the last one before
HttpClient 3.1 goes final.

## 30 October 2006 - HttpClient 3.1-beta1 released

HttpClient 3.1-beta1 has been released. This version finalizes the RFC 2965 cookie
management API and adds a number of improvements to the HTTP connection management
classes.

## 26 June 2006 - HttpClient 3.1-alpha1 released

HttpClient 3.1-alpha1 has been released. This version adds support for the RFC 2965 cookie
management (also known as Cookie2 or port sensitive cookies). All upstream projects dependent
on HttpClient are strongly encouraged to review the new API and test new features for
compatibility with their products.

## 12 May 2006 - HttpClient issue tracking migrated to Jira

HttpClient issue tracking has migrated from Bugzilla to Jira. Please do not enter new bug reports
and update exiting ones in Bugzilla. HttpComponents project will be using
[Jira](http://issues.apache.org/jira/ "External Link") to manage HttpClient related issues as of today.
Please use [this project](http://issues.apache.org/jira/browse/HTTPCLIENT "External Link") in Jira to
report new issues against HttpClient and search for reported ones. All existing issue reports can
be accessed in Jira by their original Bugzilla bug id.

## 08 May 2006 - HttpClient 3.0.1 released

HttpClient 3.0.1 has been released. This version fixes a number of bugs found since the release of 3.0.
All HttpClient users are encouraged to upgrade.

## 27 February 2006 - HttpClient 2.x codebase declared 'End of Life'

HttpClient 2.x will no longer be supported. There will be no more HttpClient 2.x releases

## 19 December 2005 - HttpClient 3.0 released

The Jakarta Commons HttpClient project is pleased to announce the release of HttpClient 3.0.
This release fixes all of the bugs discovered in RC4. As before, we strongly recommend that all users upgrade
to HttpClient 3.0. Please [download](downloads.html) and enjoy.

HttpClient 3.0 provides the following new features:

* Architecture
  * New preference architecture
  * Improved exception handling framework
  * Granular non-standards configuration and tracking
  * Improved HTTP Version configuration and tracking
  * Support for streaming entities
  * Support for tunneled HTTP proxies via the ProxyClient
  * Ability to abort execution of HTTP methods
* Connection management
  * Support for closing idle connections
  * Support for JDK1.4 connect timeout through reflection
  * Support for connection manager shutdown
* Authentication
  * Improved authentication framework
  * Plug-in mechanism for authentication modules
  * Interactive authentication support
  * Alternate authentication support
* Cookie management
  * Cookie specification plug-in mechanism
  * 'Ignore cookies' cookie policy
  * Improved Netscape cookie support
* Redirects
  * Cross-site redirect support

## 11 October 2005 - HttpClient 3.0 RC4 released

The Jakarta Commons HttpClient project is pleased to announce the fourth and hopefully final
release candidate of HttpClient 3.0. RC4 fixes a number of hard to find bugs left over in the
previous release. We strongly recommend that all users upgrade
to HttpClient 3.0 RC4. Please [download](downloads.html) and enjoy.

## 26 June 2005 - HttpClient 3.0 RC3 released

The Jakarta Commons HttpClient project is pleased to announce the third release
candidate of HttpClient 3.0. RC3 has undergone quite a lot of user testing
and it fixes a number of bugs from RC2. We strongly recommend that all users upgrade
to HttpClient 3.0 RC3. Please [download](downloads.html) and enjoy.

## 09 April 2005 - HttpClient 3.0 RC2 released

The Jakarta Commons HttpClient project is pleased to announce the second release
candidate of HttpClient 3.0. Several minor issues have been fixed since RC1 and
HttpClient 3.0 has made significant progess towards the final release. We are
confident HttpClient 3.0 is ready to replace HttpClient 2.0 as a production
quality release. We strongly recommend upgrading to HttpClient 3.0. Please
[download](downloads.html) and enjoy.

## 06 February 2005 - HttpClient 3.0 RC1 released

We are pleased to announce the HttpClient 3.0 RC1 release. The 3.0 API is frozen and
all known bugs have been fixed. Assuming no major problems are discovered in RC1 a final 3.0
release will follow shortly. We strongly encourage all current HttpClient users to start migrating.
Please [download](downloads.html) and enjoy.

## 30 January 2005 - Source control switched to Subversion

Along with the rest of the Jakarta Commons projects, HttpClient's version control
has been switched to Subversion. Please see the links below for more information:

* [Apache Subversion information](http://www.apache.org/dev/version-control.html "External Link")
* [Commons Subversion Wiki](http://wiki.apache.org/jakarta-commons/UsingSVN "External Link")
* HttpClient 3.0 repository - [http://svn.apache.org/viewcvs.cgi/jakarta/commons/proper/httpclient/trunk/](http://svn.apache.org/viewcvs.cgi/jakarta/commons/proper/httpclient/trunk/ "External Link")
* HttpClient 2.0 repository - [http://svn.apache.org/viewcvs.cgi/jakarta/commons/proper/httpclient/branches/HTTPCLIENT\_2\_0\_BRANCH/](http://svn.apache.org/viewcvs.cgi/jakarta/commons/proper/httpclient/branches/HTTPCLIENT_2_0_BRANCH/ "External Link")

## 21 November 2004 - HttpClient 3.0 beta1 released

We are pleased to announce the first beta release of HttpClient 3.0.
As of this release the 3.0 API is frozen. We will now focus on creating additional
documentation and test cases. All current HttpClient 2.0 users are
strongly encouraged to migrate to 3.0. As always we encourage
suggestions and bug reports. Please [download](downloads.html) and enjoy.

The HttpClient 3.0 site can be found
[here](http://jakarta.apache.org/commons/httpclient/3.0/ "External Link").

## 23 October 2004 - New HttpClient mailing lists

Starting today HttpClient has two new mailing lists for
developer and user discussion. People previously subscribed to *commons-httpclient-dev* have
been automatically moved to the new developer mailing list. People
subscribed to *commons-user* who are interested in HttpClient will have
to join the HttpClient user mailing list manually.

Please see the HttpClient [mailing list page](mail-lists.html) for
(un)subscription and archive details.

## 11 October 2004 - HttpClient issue tracking in Bugzilla

HttpClient project has taken a very important step toward becoming
a full-fledged Jakarta level project. From today, HttpClient is
a separate project in Apache Bugzilla issue tracking system. It is no
longer a component of the Commons project. Please use the following
details when filing bug reports for 2.0 and 3.0 branches of HttpClient:

|  |  |
| --- | --- |
| **Product:** | HttpClient |
| **Component:** | Commons HttpClient |

Use the following URL for convenience:
[Jakarta HttpClient new issue report](http://issues.apache.org/bugzilla/enter_bug.cgi?product=HttpClient "External Link").

Currently HttpClient project is debating whether we should continue using Bugzilla
as an issue tracking system or migrate to JIRA.
[JIRA](http://www.atlassian.com/software/jira/ "External Link") is a newer, more flexible
issue tracking system. However, [JIRA](http://www.atlassian.com/software/jira/ "External Link") is not open-source software. If you have a strong opinion on this matter,
please let us know.

## 11 October 2004 - HttpClient 2.0.2 released

We are pleased to announce the latest stable release of HttpClient,
version 2.0.2. This release greatly improves the performance of executing
methods where the response contains little or no content. Please see the
[release notes](http://www.apache.org/dist/jakarta/commons/httpclient/RELEASE-NOTES-2.0.txt "External Link") for more detail.

Please [download](downloads.html) and enjoy.

## 19 September 2004 - HttpClient 3.0 alpha2 released

We are pleased to announce the final alpha release of HttpClient 3.0.
At this point HttpClient is fully feature-complete and is just a
few issue reports short of being code and documentation complete.
All of the important new features such as the new preferences
architecture and exception handling framework are completely documented.
We strongly encourage comment and criticism of the current API so we can
have everything worked out by the first beta release. Following this
release the development effort will focus on stabilizing the 3.0 API
and adding more documentation. Depending on on how well this release is
received, as well as the quality and quantity of feedback, we are looking
at an API freeze in one to two months time.

The preview of the HttpClient 3.0 site can be found
[here](http://jakarta.apache.org/commons/httpclient/3.0/ "External Link").

Please [download](downloads.html) and enjoy.

## 1 August 2004 - HttpClient 2.0.1 released

We are pleased to announce the latest stable release of HttpClient,
version 2.0.1. This release contains a few minor bug fixes and
enhancements. Please see the [release notes](http://www.apache.org/dist/jakarta/commons/httpclient/RELEASE-NOTES-2.0.txt "External Link") for more detail.

Please [download](downloads.html) and enjoy.

## 17 May 2004 - HttpClient 3.0 alpha1 released

We are pleased to announce the first HttpClient 3.0 release.
HttpClient 3.0 provides a wealth of features and enhancements
that did not make it into the 2.0 release, while preserving API
compatibility as much as possible. In a relatively few cases
[API
compatibility with HttpClient 2.0](http://svn.apache.org/viewcvs.cgi/jakarta/commons/proper/httpclient/trunk/API_CHANGES_3_0.txt?view=markup "External Link") could not maintained.

Noteworthy enhancements include:

* New preference architecture
* Improved exception handling framework
* Granular non-standards configuration and tracking
* Improved authentication framework
* Plug-in mechanism for authentication modules
* Cookie specification plug-in mechanism
* Cross-site redirect support

We see our fellow Apache developers as well as other open-source
projects already reliant on HttpClient as the primary target
audience for this release. This is the right time to evaluate
HttpClient 3.0 and give us some feedback, critique or other thought on
the new API. Please feel free to file requests for additional features.

The goal of the second ALPHA release is to incorporate the feedback, polish
the API, and update documentation. The next ALPHA release will target the
wider audience beyond the Apache Jakarta and Apache WS communities.

Please [download](downloads.html) and
let us know what you think.

## 16 April 2004 - Welcome Jakarta HttpClient!

By the count 26 votes in favor, none against, Jakarta Commons HttpClient as been promoted
to the Jakarta sub-project level. The move to the Jakarta sub-project level is a next step in
HttpClient evolution which will result in many exiting changes and new developments.
So, stay tuned.

## 15 February 2004 - HttpClient 2.0 Final released

At last 2.0 final is upon us. This release represents a great deal of work by quite
a number of people. We would like to thank all of those who contributed to this
release.

Please [download](downloads.html) and enjoy.

## 16 January 2004 - HttpClient 2.0 Release Candidate 3 released

While a final 2.0 release still eludes us, we have continued to make
good progress. This release fixes some significant bugs that crept into RC2.
Assuming that there are no major bugs found in this release a final release should
follow shortly.

## 13 October 2003 - HttpClient 2.0 Release Candidate 2 released

Releasing a final version of HttpClient 2.0 by the end of Summer 2003, as
originally planned, was not possible. There were a significant number of minor
bugs reported against RC1. None of them were major, but verifying, fixing, and
testing simply took time more time than anticipated. We are pleased to
announce the second release candidate of HttpClient 2.0 and hope to follow up
with a final release shortly.

At the same time we have been busy working on our next release, currently
designated as 2.1. It it shaping up quite well. We already have a new preferences
architecture in place that will help us provide greater control over HttpClient
without polluting its API with too many options. We have also completely reworked
redirect/authentication/retry logic and can now support cross-host redirects, a
much complained about limitation of HttpClient 2.0.

## 1 August 2003 - HttpClient 2.0 Release Candidate 1 released

The *HttpClient 2.0 BETA* development phase has been
concluded. The number of bugs discovered in the course of the BETA development
was surprisingly low. We are confident that *HttpClient 2.0* has
reached the required level of maturity, and we hope to have a final 2.0
release by the end of the Summer.

## 02 July 2003 - HttpClient 2.0 Beta 2 released

This release contains some minor bug fixes and documentation enhancements.
Most likely this will be the final beta release before 2.0 Release Candidate 1. As
always thank you to the HttpClient users and developers for their efforts.
Please [download](downloads.html) HttpClient 2.0 Beta 2 and
enjoy.

## 25 May 2003 - HttpClient 2.0 Beta 1 released

This is the first feature-complete release of HttpClient 2.0. A lot of
effort has been put into making this release functional, stable and
reliable. Many thanks to everyone who contributed code, time and testing.
Please [download](downloads.html) HttpClient 2.0 Beta 1 and
enjoy.

**Note:** The binary distributions were updated on 2 June, 2003 to
fix a problem with the original jar's MANIFEST.MF. Using the original
HttpClient jar from within a servlet container or J2EE managed environment
may have caused some problems.

## 25 February 2003 - HttpClient 2.0 Alpha 3 released

This is an intermediate alpha release. The build process used in
the previous Alpha 2 changed from generating 4 build artifacts to
a single distribution. This one zip contains everything: all
the source, the binary jar, the logging dependancy, generated
javadoc and required build files for Ant builds and JUnit tests.

> "One zip to rule them all, one zip to find them, one zip to
> bring them all and in the darkness bind them"

## 19 February, 2003 - Welcome new committer Michael Becke

Mike been an active contributor for many months. He has worked on a diverse range
of problems with high quality results. In particular he is known for the massive
HttpClient/HttpMultiClient merger that took place in December.

Welcome to Middle Earth Mike!

## 26 January 2003 - new mailing list archives

There are two new mailing list archives of the commons-httpclient-dev
mailing list. It looks like someone up there is starting to like us!

* [http://archives.apache.org/eyebrowse/SummarizeList?listId=128](http://archives.apache.org/eyebrowse/SummarizeList?listId=128 "External Link")
* [http://www.mail-archive.com/commons-httpclient-dev%40jakarta.apache.org/](http://www.mail-archive.com/commons-httpclient-dev%40jakarta.apache.org/ "External Link")

## 25 January 2003 - HttpClient 2.0 Alpha 2 released

After many months and a great resurgence of developers, the new build
of *HttpClient* is finally here. The new group of developers has done
extensive refactoring to move the project along the new vision.
The code base has reached a significant level of maturity and we
expect that the beta builds will come quickly and that the
final release of 2.0 is not far away!

Also check out the new *HttpClient* logo!

## 21 December, 2002 - Welcome new committer Oleg Kalnichevski

Oleg is the first committer to be voted in on the dedicated httpclient
mailing list. Welcome to the fellowship Olegolas!

## 3 December, 2002 - HttpClient/HttpMultiClient merger

The initial merger of the top level classes HttpClient and HttpMultiClient
is complete. Thanks for the patches and hard work from everyone
particularly to Michale Becke for supplying the primary patch.

## 3 October, 2002 - commons-httpclient-dev mailing list

The mailing list was renamed to be **commons-httpclient-dev**.
Sorry for the confusion.

## 12 July, 2002 - HttpClient 2.0 Release Planning

The *HttpClient* project has go through some very active
development leading up to Alpha 1 last year, but unfortunately
lost momentum shortly after that. There is now renewed interest
and greatly increased activity on the dev-commons mailing list.
The committers and contributors are working on a new release plan
for 2.0.

The 2.0 release plan is expected to be posted to the mailing list for
review by July 22, 2002.

## 5 October, 2001 - HttpClient 2.0 Alpha 1 Released

The *HttpClient* revision 2.0 alpha 1 is
available at
[http://jakarta.apache.org/builds/jakarta-commons/release/commons-httpclient/v2.0/](http://jakarta.apache.org/builds/jakarta-commons/release/commons-httpclient/v2.0/ "External Link").

## 25 April, 2001 - HttpClient Proposal Accepted

The *HttpClient* [proposal](proposal.html)
has been accepted by the
[Jakarta Commons](http://jakarta.apache.org/commons "External Link")
team and the source has been moved into the
[Subversion repository](http://svn.apache.org/viewcvs.cgi/jakarta/commons/proper/httpclient/trunk/ "External Link").

## 18 April, 2001 - HttpClient Proposed

*HttpClient*, originally developed by the
[Jakarta Slide](http://jakarta.apache.org/slide "External Link")
team, has been
[proposed](http://www.mail-archive.com/jakarta-commons@jakarta.apache.org/msg01153.html "External Link")
as a [Jakarta Commons](http://jakarta.apache.org/commons "External Link")
component.

---
## Exception handling

There are two main type of exceptions that the user of HttpClient may encounter
when executing HTTP methods:

1. **transport exceptions**
2. **protocol exceptions**

Not all of these exceptions will be propagated to the user in regular HttpClient use.
Exceptions handled internally by HttpClient are marked below as **INTERNAL**.

* [Transport exceptions](#Transport_exceptions)
* [Protocol exceptions](#Protocol_exceptions)
* [HTTP transport safety](#HTTP_transport_safety)
* [Automatic exception recovery](#Automatic_exception_recovery)
* [Custom exception handler](#Custom_exception_handler)

## Transport exceptions

Transport exceptions are those caused by input/output failures such as an unreliable connection
or an inability to complete the execution of an HTTP method within the given time constraint
(socket timeout). Generally transport exceptions are non-fatal and may be recovered from by
retrying the failed method. However, special care must be taken when recovering from
exceptions in non-idempotent methods (refer to [HTTP transport safety](#HTTP_transport_safety)
for details).

### java.io.IOException

Generic transport exceptions in HttpClient are represented by the standard Java
java.io.IOException class or its sub classes such as java.net.SocketException and
java.net.InterruptedIOException.

In addition to standard input/output exception classes HttpClient defines several custom transport
exceptions that convey HttpClient specific information.

### org.apache.commons.httpclient.NoHttpResponseException

```
java.io.IOException
  +- org.apache.commons.httpclient.NoHttpResponseException
```

In some circumstances, usually when under heavy load, the web server may be able to receive
requests but unable to process them. A lack of sufficient resources like worker threads is a good
example. This may cause the server to drop the connection to the client
without giving any response. HttpClient throws NoHttpResponseException when it encounters
such a condition. In most cases it is safe to retry a method that failed with
NoHttpResponseException.

### org.apache.commons.httpclient.ConnectTimeoutException

```
java.io.IOException
  +- java.io.InterruptedIOException
    +- org.apache.commons.httpclient.ConnectTimeoutException
```

This exception signals that HttpClient is unable to establish a connection with the target
server or proxy server within the given period of time.

### org.apache.commons.httpclient.ConnectionPoolTimeoutException

```
java.io.IOException
  +- java.io.InterruptedIOException
    +- org.apache.commons.httpclient.ConnectTimeoutException
      +- org.apache.commons.httpclient.ConnectionPoolTimeoutException
```

This exception can only occur when using the multithreaded connection manager. The exception
signals that the connection manager fails to obtain a free connection from the connection pool
within the given period of time.

### org.apache.commons.httpclient.HttpRecoverableException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.HttpRecoverableException
```

Deprecated and no longer thrown any of the standard HttpClient classes.

## Protocol exceptions

Protocol exceptions generally indicate logical errors caused by a mismatch between the client
and the server (web server or proxy server) in their interpretation of the HTTP specification.
Usually protocol exceptions cannot be recovered from without making adjustments to either
the client request or the server. Some aspects of the HTTP specification allow for different,
at times conflicting, interpretations. HttpClient can be configured to support different degrees
of HTTP specification compliance varying from very lenient to very strict.

### org.apache.commons.httpclient.HttpException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
```

HttpException represents an abstract logical error in HttpClient. Generally this kind of exception
cannot be automatically recovered from.

### org.apache.commons.httpclient.ProtocolException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
```

ProtocolException signals a violation of the HTTP specification. It is important to note that HTTP
proxies and HTTP servers can have different level of HTTP specification compliance. It may be
possible to recover from some HTTP protocol exceptions by configuring HttpClient to be more
lenient about non-fatal protocol violations.

### org.apache.commons.httpclient.auth.MalformedChallengeException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.MalformedChallengeException
```

**INTERNAL**

MalformedChallengeException signals that an authentication challenge is in some way invalid or
illegal in the given authentication context.

### org.apache.commons.httpclient.auth.AuthenticationException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
```

**INTERNAL**

AuthenticationException signals a failure in the authentication process. Usually authentication
exceptions are handled internally when executing HTTP methods and are not propagated to the
caller.

### org.apache.commons.httpclient.auth.AuthChallengeException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
        +- org.apache.commons.httpclient.auth.AuthChallengeException
```

**INTERNAL**

AuthenticationException is thrown when HttpClient is unable to respond to any of the authentication
challenges sent by the server.

### org.apache.commons.httpclient.auth.CredentialsNotAvailableException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
        +- org.apache.commons.httpclient.auth.CredentialsNotAvailableException
```

**INTERNAL**

CredentialsNotAvailableException indicates that credentials required to respond to the authentication
challenge are not available.

### org.apache.commons.httpclient.auth.InvalidCredentialsException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
        +- org.apache.commons.httpclient.auth.InvalidCredentialsException
```

**INTERNAL**

InvalidCredentialsException indicates that the credentials used to respond to the authentication
challenge have been rejected by the server.

### org.apache.commons.httpclient.cookie.MalformedCookieException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.cookie.MalformedCookieException
```

**INTERNAL**

MalformedCookieException signals that the cookie is in some way invalid or illegal in the given
HTTP session context.

There are several cookie specifications that are often incompatible. Thus the validity of
a cookie is established within a context of a specific cookie specification used to parse
and validate the cookie header(s) sent by the server. If the application needs to process cookies
differently from the commonly used cookie specifications, it may choose to provide a
custom cookie policy or extend the existing one. Please see [cookies](cookies.html)
for more details.

### org.apache.commons.httpclient.RedirectException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.RedirectException
```

RedirectException signals violation of the HTTP specification caused by an invalid
redirect response. If the application that uses HttpClient needs to be more lenient
about redirect responses, it may choose to disable automatic redirect processing and implement
a custom redirect strategy.

### org.apache.commons.httpclient.URIException

```
java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.URIException
```

URIException is thrown when the request URI violates the URI specification.

## HTTP transport safety

It is important to understand that the HTTP protocol is not well suited for all types of applications.
HTTP is a simple request/response oriented protocol which was initially designed to support static
or dynamically generated content retrieval. It has never been intended to support transactional
operations. For instance, the HTTP server will consider its part of the contract fulfilled if it
succeeds in receiving and processing the request, generating a response and sending a status code back
to the client. The server will make no attempts to roll back the transaction if the client fails to
receive the response in its entirety due to a read timeout, a request cancellation or a system crash.
If the client decides to retry the same request, the server will inevitably end up executing the same
transaction more than once. In some cases this may lead to application data corruption or inconsistent
application state.

Even though HTTP has never been designed to support transactional processing, it can still be used
as a transport protocol for mission critical applications provided certain conditions are met. To
ensure HTTP transport layer safety the system must ensure the idempotency of HTTP methods on the
application layer.

### Idempotent methods

HTTP/1.1 specification defines idempotent method as

> Methods can also have the property of "idempotence" in that (aside from error or expiration
> issues) the side-effects of N > 0 identical requests is the same as for a single request.

In other words the application ought to ensure that it is prepared to deal with the
implications of multiple execution of the same method. This can be achieved, for instance,
by providing a unique transaction id and by other means of avoiding execution of the same
logical operation.

Please note that this problem is not specific to HttpClient. Browser based applications
are subject to exactly the same issues related to HTTP methods non-idempotency.

## Automatic exception recovery

By default HttpClient attempts to automatically recover from exceptions. The default
auto-recovery mechanism is limited to just a few exceptions that are known to be safe.

HttpClient will make no attempt to recover from any logical or HTTP protocol error (those derived
from HttpException class).

HttpClient will automatically retry up to 5 times those methods that fail with a transport exception
while the HTTP request is still being transmitted to the target server (i.e. the request has
not been fully transmitted to the server).

HttpClient will automatically retry up to 5 times those methods that have been fully transmitted to
the server, but the server failed to respond with an HTTP status code (the server simply drops the
connection without sending anything back). In this case it is assumed that the request has not been
processed by the server and the application state has not changed. If this assumption may not hold
true for the web server your application is targeting it is highly recommended to provide a custom
exception handler.

## Custom exception handler

In order to enable a custom exception recovery mechanism one should provide an implementation
of the [HttpMethodRetryHandler](apidocs/org/apache/commons/httpclient/HttpMethodRetryHandler.html) interface.

```
HttpClient client = new HttpClient();

HttpMethodRetryHandler myretryhandler = new HttpMethodRetryHandler() {
    public boolean retryMethod(
        final HttpMethod method, 
        final IOException exception, 
        int executionCount) {
        if (executionCount >= 5) {
            // Do not retry if over max retry count
            return false;
        }
        if (exception instanceof NoHttpResponseException) {
            // Retry if the server dropped connection on us
            return true;
        }
        if (!method.isRequestSent()) {
            // Retry if the request has not been sent fully or
            // if it's OK to retry methods that have been sent
            return true;
        }
        // otherwise do not retry
        return false;
    }
};
        
GetMethod httpget = new GetMethod("http://www.whatever.com/");
httpget.getParams().
    setParameter(HttpMethodParams.RETRY_HANDLER, myretryhandler);
try {
    client.executeMethod(httpget);
    System.out.println(httpget.getStatusLine().toString());
} finally {
    httpget.releaseConnection();
}
```

---
## Logging Practices

Being a library HttpClient is not to dictate which logging framework
the user has to use. Therefore *HttpClient* utilizes the logging
interface provided by the
[Commons Logging](http://commons.apache.org/logging/ "External Link") package. *Commons Logging* provides
a simple and generalized
[log interface](http://commons.apache.org/logging/commons-logging-1.0.4/docs/apidocs/ "External Link") to various logging packages. By using
*Commons Logging*, *HttpClient* can be configured
for a variety of different logging behaviours. That means the user will have
to make a choice which logging framework to use. By default *Commons Logging*
supports the following logging frameworks:

* [Log4J](http://logging.apache.org/log4j/docs/index.html "External Link")
* [java.util.logging](http://java.sun.com/j2se/1.4.2/docs/api/java/util/logging/package-summary.html "External Link")
* [SimpleLog](http://commons.apache.org/logging/commons-logging-1.0.4/docs/apidocs/org/apache/commons/logging/impl/SimpleLog.html "External Link") (internal to *Commons Logging*)

By implementing some simple interfaces *Commons Logging* can be extended to support
basically any other custom logging framework.
*Commons Logging* tries to automatically discover the logging framework to use. If it
fails to select the expected one, you must configure *Commons Logging* by hand. Please
refer to the *Commons Logging* documentation for more information.

*HttpClient* performs two different kinds of logging: the standard
context logging used within each class, and wire logging.

### Context Logging

Context logging contains information about the internal operation
of HttpClient as it performs HTTP requests. Each class has its own
log named according to the class's fully qualified name. For example
the class `HttpClient` has a log named
`org.apache.commons.httpclient.HttpClient`. Since all classes
follow this convention it is possible to configure context logging for
all classes using the single log named `org.apache.commons.httpclient`.

### Wire Logging

The wire log is used to log all data transmitted to and from servers when
executing HTTP requests. This log should only be enabled to debug problems,
as it will produce an extremely large amount of log data, some of it in binary
format.

Because the content of HTTP requests is usually less important for debugging
than the HTTP headers, these two types of data have been separated into
different wire logs. The content log is `httpclient.wire.content`
and the header log is `httpclient.wire.header`.

## Configuration Examples

*Commons Logging* can delegate to a variety of loggers for processing
the actual output. Below are configuration examples for *Commons Logging*,
*Log4j* and *java.util.logging*.

### Commons Logging Examples

*Commons Logging* comes with a basic logger called
`SimpleLog`. This logger writes all logged messages to
`System.err`. The following examples show how to configure
*Commons Logging* via system properties to use `SimpleLog`.

**Note:** The system properties must be set before a reference to any
*Commons Logging* class is made.

Enable header wire + context logging - **Best for Debugging**  
> System.setProperty("org.apache.commons.logging.Log", "org.apache.commons.logging.impl.SimpleLog");  
> System.setProperty("org.apache.commons.logging.simplelog.showdatetime", "true");  
> System.setProperty("org.apache.commons.logging.simplelog.log.httpclient.wire.header", "debug");  
> System.setProperty("org.apache.commons.logging.simplelog.log.org.apache.commons.httpclient", "debug");

Enable full wire(header and content) + context logging  
> System.setProperty("org.apache.commons.logging.Log", "org.apache.commons.logging.impl.SimpleLog");  
> System.setProperty("org.apache.commons.logging.simplelog.showdatetime", "true");  
> System.setProperty("org.apache.commons.logging.simplelog.log.httpclient.wire", "debug");  
> System.setProperty("org.apache.commons.logging.simplelog.log.org.apache.commons.httpclient", "debug");

Enable just context logging  
> System.setProperty("org.apache.commons.logging.Log", "org.apache.commons.logging.impl.SimpleLog");  
> System.setProperty("org.apache.commons.logging.simplelog.showdatetime", "true");  
> System.setProperty("org.apache.commons.logging.simplelog.log.org.apache.commons.httpclient", "debug");

### Log4j Examples

The simplest way to configure [Log4j](http://logging.apache.org/log4j/ "External Link")
is via a *log4j.properties* file. *Log4j* will automatically
read and configure itself using a file named *log4j.properties* when
it's present at the root of the application classpath. Below are some
*Log4j* configuration examples.

**Note:** *Log4j* is not included in the *HttpClient* distribution.

Enable header wire + context logging - **Best for Debugging**  
> log4j.rootLogger=INFO, stdout  
>   
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender  
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout  
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n  
>   
> log4j.logger.httpclient.wire.header=DEBUG  
> log4j.logger.org.apache.commons.httpclient=DEBUG

Enable full wire(header and content) + context logging  
> log4j.rootLogger=INFO, stdout  
>   
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender  
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout  
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n  
>   
> log4j.logger.httpclient.wire=DEBUG  
> log4j.logger.org.apache.commons.httpclient=DEBUG

Log wire to file + context logging  
> log4j.rootLogger=INFO  
>   
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender  
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout  
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n  
>   
> log4j.appender.F=org.apache.log4j.FileAppender  
> log4j.appender.F.File=wire.log  
> log4j.appender.F.layout=org.apache.log4j.PatternLayout  
> log4j.appender.F.layout.ConversionPattern =%5p [%c] %m%n  
>   
> log4j.logger.httpclient.wire=DEBUG, F  
> log4j.logger.org.apache.commons.httpclient=DEBUG, stdout

Enable just context logging  
> log4j.rootLogger=INFO, stdout  
>   
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender  
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout  
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n  
>   
> log4j.logger.org.apache.commons.httpclient=DEBUG

Note that the default configuration for Log4J is very
inefficient as it causes all the logging information to be
generated but not actually sent anywhere. The Log4J manual is the
best reference for how to configure Log4J. It is available at [http://logging.apache.org/log4j/docs/manual.html](http://logging.apache.org/log4j/docs/manual.html "External Link")

### java.util.logging Examples

Since JDK 1.4 there has been a package
[java.util.logging](http://java.sun.com/j2se/1.4.2/docs/api/java/util/logging/package-summary.html "External Link") that provides a
logging framework similar to *Log4J*. By default it reads a config file from
`$JAVA_HOME/jre/lib/logging.properties` which looks like this
(comments stripped):
> handlers=java.util.logging.ConsoleHandler  
> .level=INFO  
> java.util.logging.FileHandler.pattern = %h/java%u.log  
> java.util.logging.FileHandler.limit = 50000  
> java.util.logging.FileHandler.count = 1  
> java.util.logging.FileHandler.formatter = java.util.logging.XMLFormatter  
> java.util.logging.ConsoleHandler.level = INFO  
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter  
> com.xyz.foo.level = SEVERE

To customize logging a custom `logging.properties` file should be created
in the project directory. The location of this file must be passed to the JVM as a
system property. This can be done on the command line like so:
> $JAVA\_HOME/java -Djava.util.logging.config.file=$HOME/myapp/logging.properties
> -classpath $HOME/myapp/target/classes com.myapp.Main

Alternatively
[LogManager#readConfiguration(InputStream)](http://java.sun.com/j2se/1.4.2/docs/api/java/util/logging/LogManager.html#readConfiguration(java.io.InputStream) "External Link") can be used to pass it the desired
configuration.

Enable header wire + context logging - **Best for Debugging**  
> .level=INFO  
>   
> handlers=java.util.logging.ConsoleHandler  
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter  
>   
> httpclient.wire.header.level=FINEST  
> org.apache.commons.httpclient.level=FINEST

Enable full wire(header and content) + context logging  
> .level=INFO  
>   
> handlers=java.util.logging.ConsoleHandler  
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter  
>   
> httpclient.wire.level=FINEST  
> org.apache.commons.httpclient.level=FINEST

Enable just context logging  
> .level=INFO  
>   
> handlers=java.util.logging.ConsoleHandler  
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter  
>   
> org.apache.commons.httpclient.level=FINEST

More detailed information is available from the
[Java Logging documentation](http://java.sun.com/j2se/1.4.2/docs/guide/util/logging/overview.html "External Link").

---
## Introduction

These documents provide a brief introduction to using the methods
provided by *HttpClient*. The information here does not cover all the
possible options, but covers enough of the basics to get you up and
running. For more information on the available options, refer to the [API Reference](apidocs/index.html).

The examples on the following pages are not complete and are only used
to highlight the important features that are unique to each method. For
complete examples, please refer to the [sample
code](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link").

## Overview

| Document | Description |
| --- | --- |
| [Options](methods/options.html) | The OPTIONS method represents a request for information about the communication options available. |
| [Get](methods/get.html) | The GET method means retrieve whatever information is identified by the requested URL. Also refer to the [tutorial](tutorial.html). |
| [Head](methods/head.html) | The HEAD method is identical to GET except that the server *must not* return a message-body in the response. This method can be used for obtaining metainformation about the document implied by the request without transferring the document itself. |
| [Post](methods/post.html) | The POST method is used to request that the origin server accept the data enclosed in the request as a new child of the request URL. POST is designed to allow a uniform method to cover a variety of functions such as appending to a database, providing data to a data-handling process or posting to a message board. |
| [Multipart Post](methods/multipartpost.html) | The multipart post method is identical to the POST method, except that the request body is separated into multiple parts. This method is generally used when uploading files to the server. |
| [Put](methods/put.html) | The PUT method requests that the enclosed document be stored under the supplied URL. This method is generally disabled on publicly available servers because it is generally undesireable to allow clients to put new files on the server or to replace existing files. |
| [Delete](methods/delete.html) | The DELETE method requests that the server delete the resource identified by the request URL. This method is generally disabled on publicly available servers because it is generally undesireable to allow clients to delete files on the server. |
| [Trace](methods/trace.html) | The TRACE method is used to invoke a remote, application-layer loop-back of the request message. This allows the client to see what is being received at the other end of the request chain and use that data for testing or diagnostic information. |

---
## Introduction

This document provides an overview of how HttpClient handles character
encodings and how to use HttpClient in an encoding safe way. There are
three main sections:
[HTTP Headers](#HTTP_Headers),
[Request/Response Body](#Request_Response_Body) and
[URLs](#URLs).

## HTTP Headers

The headers of a HTTP request or response must be in US-ASCII format.
It is not possible to use non US-ASCII characters in the header of a
request or response. Generally this is not an issue however, because the
HTTP headers are designed to facilite the transfer of data rather than to
actually transfer the data itself.

One exception however are cookies. Since cookies are transfered as HTTP Headers
they are confined to the US-ASCII character set. See the Cookie Guide
for more information.

## Request/Response Body

The request or response body can be any encoding, but by default is
ISO-8859-1. The encoding may be specified in the
Content-Type header, for example:
> Content-Type: text/html; charset=UTF-8

In this case the application should be careful to use UTF-8 encoding
when converting the body to a String or some characters may be corrupt.
You can set the content type header for a request with the
`addRequestHeader` method in each method and retrieve the
encoding for the response body with the `getResponseCharSet`
method.

If the response is known to be a String, you can use the
`getResponseBodyAsString` method which will automatically use
the encoding specified in the Content-Type header or
ISO-8859-1 if no charset is specified.

Note that some document types, such as HTML and XML allow the author
to specify the content type of the file. In this case, you should
consult the appropriate standards regarding how to resovle any conflicts
in the reported charsets.

## URLs

The standard for URLs ([RFC1738](http://www.ietf.org/rfc/rfc1738.txt "External Link")) explictly
states that URLs may only contain graphic printable characters of the
US-ASCII coded character set and is defined in terms of octets.
The octets `80-FF` hexadecimal are not used in US-ASCII and the octets
`OO-1F` hexadecimal represent control characters; characters in these
ranges must be encoded.

Characters which cannot be represented by an 8-bit ASCII code, can not
be used in an URL as there is no way to reliably encode them (the
encoding scheme for URLs is based off of octets). Despite this, some
servers do support varying means of encoding double byte characters in
URLs, the most common technique seems to be to use UTF-8 encoding and
encode each octet separately even if a pair of octets represents one
character. This however, is not specified by the standard and is highly
prone to error, so it is recommended that URLs be restricted to the 8-bit
ASCII range.

---
## Overview

This tutorial is designed to provide a basic overview of how to use
*HttpClient*. When you have completed the tutorial you will have written
a simple application that downloads a page using *HttpClient*.

It is assumed that you have an understanding of how to program in
Java and are familiar with the development environment you are using.

## Getting Ready

The first thing you need to do is get a copy of *HttpClient* and its
[dependencies](dependencies.html). This tutorial was
written for *HttpClient* 3.0. You will also need JDK 1.3 or above.

Once you've downloaded *HttpClient* and dependencies you will need to
put them on your classpath. There is also an optional dependency on JSSE
which is required for HTTPS connections; this is not required for this
tutorial.

## Concepts

The general process for using *HttpClient* consists of a number of
steps:

1. Create an instance of `HttpClient`.
2. Create an instance of one of the methods (GetMethod in this
   case). The URL to connect to is passed in to the the method
   constructor.
3. Tell `HttpClient` to execute the method.
4. Read the response.
5. Release the connection.
6. Deal with the response.

We'll cover how to perform each of these steps below. Notice that we
go through the entire process regardless of whether the server returned
an error or not. This is important because HTTP 1.1 allows multiple
requests to use the same connection by simply sending the requests one
after the other. Obviously, if we don't read the entire response to
the first request, the left over data will get in the way of the second
response. *HttpClient* tries to handle this but to avoid problems it is
important to always release the connection.

Upon the connection release
HttpClient will do its best to ensure that the connection is reusable.

It is important to always release the connection regardless of whether the server
returned an error or not.

## Instantiating HttpClient

The no argument constructor for `HttpClient` provides a good set of
defaults for most situations so that is what we'll use.

```
HttpClient client = new HttpClient();
```

## Creating a Method

The various methods defined by the HTTP specification correspond to
the various classes in *HttpClient* which implement the HttpMethod
interface. These classes are all found in the package
`org.apache.commons.httpclient.methods`.

We will be using the Get method which is a simple method that simply
takes a URL and gets the document the URL points to.

```
HttpMethod method = new GetMethod("http://www.apache.org/");
```

## Execute the Method

The actual execution of the method is performed by calling
`executeMethod` on the client and passing in the method to
execute. Since networks connections are unreliable, we also need to deal
with any errors that occur.

There are two kinds of exceptions that could be thrown by
executeMethod, `HttpException` and `IOException`.

The other useful piece of information is the status code that is
returned by the server. This code is returned by executeMethod as an
int and can be used to determine if the request was successful or not
and can sometimes indicate that further action is required by the
client such as providing authentication credentials.

### HttpException

An HttpException represents a logical error and is thrown when the request
cannot be sent or the response cannot be processed due to a fatal violation of
the HTTP specification. Usually this kind of exceptions cannot be recovered
from. For a detailed discussion on protocol exceptions please refer to
[the HttpClient exception
handling guide](exception-handling.html#Protocol exceptions). Note that HttpException actually extends IOException
so you can just ignore it and catch the IOException if your application does
not distinguish between protocol and transport errors.

### IOException

A plain IOException (which is not a subclass of HttpException) represents a
transport error and is thrown when an error occurs that is likely to be a
once-off I/O problem. Usually the request has a good chance of succeeding on
a second attempt, so per default HttpClient will try to recover the request
automatically. For a detailed discussion on transport exceptions please refer to
[the HttpClient exception
handling guide](exception-handling.html#Transport exceptions).

### Method recovery

Per default HttpClient will automatically attempt to recover from the not-fatal
errors, that is, when a plain IOException is thrown. HttpClient will retry the
method three times provided that the request has never been fully transmitted to
the target server. For a detailed discussion on HTTP method recovery please refer
to [the HttpClient
exception handling guide](exception-handling.html#HTTP transport safety)

```
// set per default
client.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, 
  new DefaultHttpMethodRetryHandler());
```

Default recovery procedure can be replaced with a custom one. The number
of automatic retries can be increased. HttpClient can also be instructed to
retry the method even though the request may have already been processed by
the server and the I/O exception has occurred while receiving the response.
Please exercise caution when enabling auto-retrial. Use it only if the method
is known to be idempotent, that is, it is known to be safe to retry multiple
times without causing data corruption or data inconsistency.

The rule of thumb is GET methods are usually safe unless known otherwise,
entity enclosing methods such as POST and PUT are usually unsafe unless known
otherwise.

```
DefaultMethodRetryHandler retryhandler = new DefaultMethodRetryHandler(10, true);
client.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, retryhandler);
```

## Read the Response

It is vital that the response body is always read regardless of the
status returned by the server. There are three ways to do this:

* Call `method.getResponseBody()`. This will return a
  byte array containing the data in the response body.
* Call `method.getResponseBodyAsString()`. This will
  return a String containing the response body. Be warned though that
  the conversion from bytes to a String is done using the default
  encoding so this method may not be portable across all platforms.
* Call `method.getResponseBodyAsStream()` and read the
  entire contents of the stream then call `stream.close()`.
  This method is best if it is possible for a lot of data to be received
  as it can be buffered to a file or processed as it is read. Be sure to
  always read the entirety of the data and call close on the stream.

For this tutorial we will use `getResponseBody()` for simplicity.

```
byte[] responseBody = method.getResponseBody();
```

## Release the Connection

This is a crucial step to keep things flowing. We must tell
*HttpClient* that we are done with the connection and that it can now be
reused. Without doing this *HttpClient* will wait indefinitely for a
connection to free up so that it can be reused.

```
method.releaseConnection();
```

## Deal with the Repsonse

We've now completed our interaction with *HttpClient* and can just
concentrate on doing what we need to do with the data. In our case,
we'll just print it out to the console.

It's worth noting that if you were retrieving the response as a stream
and processing it as it is read, this step would actually be combined
with reading the connection, and when you'd finished processing all the
data, you'd then close the input stream and release the connection.

Note: We should pay attention to character encodings here instead of
just using the system default.

```
System.out.println(new String(responseBody));
```

## Final Source Code

When we put all of that together plus a little bit of glue code we get
the program below.

```
import org.apache.commons.httpclient.*;
import org.apache.commons.httpclient.methods.*;
import org.apache.commons.httpclient.params.HttpMethodParams;

import java.io.*;

public class HttpClientTutorial {
  
  private static String url = "http://www.apache.org/";

  public static void main(String[] args) {
    // Create an instance of HttpClient.
    HttpClient client = new HttpClient();

    // Create a method instance.
    GetMethod method = new GetMethod(url);
    
    // Provide custom retry handler is necessary
    method.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, 
    		new DefaultHttpMethodRetryHandler(3, false));

    try {
      // Execute the method.
      int statusCode = client.executeMethod(method);

      if (statusCode != HttpStatus.SC_OK) {
        System.err.println("Method failed: " + method.getStatusLine());
      }

      // Read the response body.
      byte[] responseBody = method.getResponseBody();

      // Deal with the response.
      // Use caution: ensure correct character encoding and is not binary data
      System.out.println(new String(responseBody));

    } catch (HttpException e) {
      System.err.println("Fatal protocol violation: " + e.getMessage());
      e.printStackTrace();
    } catch (IOException e) {
      System.err.println("Fatal transport error: " + e.getMessage());
      e.printStackTrace();
    } finally {
      // Release the connection.
      method.releaseConnection();
    }  
  }
}
```

---
## Maven Generated Reports

This document provides an overview of the various reports that are automatically generated by
[Maven](http://maven.apache.org/ "External Link")
. Each report is briefly described below.

### Overview

| Document | Description |
| --- | --- |
| [JavaDocs](apidocs/index.html "New Window") | JavaDoc API documentation. |
| [JavaDoc Report](javadoc.html) | Report on the generation of JavaDoc. |
| [JavaDoc Warnings Report](javadoc-warnings-report.html) | Formatted report of JavaDoc warnings. |
| [Metrics](jdepend-report.html) | Report on source code metrics. |
| [Unit Tests](junit-report.html) | Report on the results of the unit tests. |
| [Source Xref](xref/index.html "New Window") | A set of browsable cross-referenced sources. |
| [Test Xref](xref-test/index.html "New Window") | A set of browsable cross-referenced test sources. |
| [Project License](license.html) | Displays the primary license for the project. |

---
## End of life

The Commons HttpClient project is now end of life, and is no longer being developed.
It has been replaced by the [Apache HttpComponents](../) project
in its [HttpClient](../httpcomponents-client-ga) and [HttpCore](../httpcomponents-core-ga/) modules,
which offer better performance and more flexibility.

## Introduction

The Hyper-Text Transfer Protocol (HTTP) is perhaps the most
significant protocol used on the Internet today.
Web services, network-enabled appliances and the growth
of network computing continue to expand the role of the HTTP
protocol beyond user-driven web browsers, while increasing the
number of applications that require HTTP support.

Although the java.net
package provides basic functionality for accessing resources via HTTP,
it doesn't provide the full flexibility or functionality needed
by many applications. The Jakarta Commons *HttpClient*
component seeks to fill this void
by providing an efficient, up-to-date, and feature-rich package
implementing the client side of the most recent HTTP standards
and recommendations. See the [Features](features.html) page
for more details on standards compliance and capabilities.

Designed for extension while providing robust support for the
base HTTP protocol, the *HttpClient* component may be of interest
to anyone building HTTP-aware client applications such as web
browsers, web service clients, or systems that leverage or extend
the HTTP protocol for distributed communication.

There are many projects that use *HttpClient* to provide the core HTTP functionality.
Some of these are open source with project pages you can find on the web
while others are closed source that you would never see or hear about.
The Apache Source License provides maximum flexibility for source and binary
reuse. Please see the [Applications](http://wiki.apache.org/jakarta-httpclient/HttpClientPowered "External Link") page for projects using *HttpClient*.

## History

*HttpClient* was started in 2001 as a subproject of the
Jakarta Commons, based on code developed by the
[Jakarta Slide](http://jakarta.apache.org/slide/ "External Link") project.
It was promoted out of the Commons in 2004, graduating to a separate
Jakarta project. In 2005, the HttpComponents project at Jakarta was
created, with the task of developing a successor
to *HttpClient 3.x* and to maintain the existing codebase until
the new one is ready to take over.
The [Commons](http://commons.apache.org/ "External Link") project,
cradle of *HttpClient*,
left [Jakarta](http://jakarta.apache.org/ "External Link")
in 2007 to become an independent Top Level Project.
Later in the same year, the
[HttpComponents](http://httpcomponents.apache.org/ "External Link")
project also left Jakarta to become an independent Top Level Project,
taking the responsibility for maintaining *HttpClient* with it.

---
## Introduction

HttpClient supports automatic management of cookies, including
allowing the server to set cookies and automatically return them to the
server when required. It is also possible to manually set cookies to be
sent to the server.

Unfortunately, there are several at times conflicting standards for
handling Cookies: the Netscape Cookie draft, RFC2109, RFC2965 and a large
number of vendor specific implementations that are compliant with neither
specification. To deal with this, HttpClient provides policy driven cookie
management. This guide will explain how to use the different cookie
specifications and identify some of the common problems people have when
using Cookies and HttpClient.

## Supported Specifications

The following cookie specifications are supported by HttpClient 3.1.

### RFC2109

RFC2109 is the first official cookie specification released by the W3C.
Theoretically, all servers that handle version 1 cookies should use this
specification and as such this specification is used by default within
HttpClient.

Unfortunately, many servers either incorrectly implement this
standard or are still using the Netscape draft so occasionally this
specification is too strict. If this is the case, you should switch to
the compatibility specification as described below.

RFC2109 is available at
[http://www.w3.org/Protocols/rfc2109/rfc2109.txt](http://www.w3.org/Protocols/rfc2109/rfc2109.txt "External Link")

RFC2109 is the default cookie policy used by HttpClient.

### RFC2965

RFC2965 defines cookie version 2 and attempts to address the
shortcomings of the RFC2109 regarding cookie version 1.
RFC2965 is intended to eventually supersede RFC2109.

Servers that send RFC2965 cookies will use the Set-Cookie2 header
in addition to the Set-Cookie header. RFC2965 cookies are port
sensitive.

RFC2965 is available at
[http://www.w3.org/Protocols/rfc2965/rfc2965.txt](http://www.w3.org/Protocols/rfc2965/rfc2965.txt "External Link")

### Netscape Draft

The Netscape draft is the original cookie specification which formed
the basis for RFC2109. Despite this it has some significant
differences with RFC2109 and thus may be required for compatibility
with some servers.

The Netscape cookie draft is available at [http://wp.netscape.com/newsref/std/cookie\_spec.html](http://wp.netscape.com/newsref/std/cookie_spec.html "External Link")

### Browser Compatibility

The compatibility specification is designed to be compatible with as
many different servers as possible even if they are not completely
standards compliant. If you are encountering problems with parsing
cookies, you should probably try using this specification.

There are many web sites with badly written CGI scripts that only work
when all cookies are put into one request header. It is advisable to
set [http.protocol.single-cookie-header](preference-api.html)
parameter to `true` for maximum compatibility.

### Ignore Cookies

This cookie specification ignores all cookies. It should be used to
prevent HttpClient from accepting and sending cookies.

## Specifying the Specification

There are two ways to specify which cookie specification should be
used, either for each `HttpMethod` instance using the
`HttpMethodParams`, or by setting the default value on
`CookiePolicy`.

### Per HttpMethod

In most cases, the best way to specify the cookie spec to use is the
`setCookiePolicy(String policy)` method on
`HttpMethodParams`. The value of `policy`
must be one of the values registered with `CookiePolicy.registerCookieSpec()`.

```
        HttpMethod method = new GetMethod();
        method.getParams().setCookiePolicy(CookiePolicy.RFC_2109);
```

## Manual handling of cookies

The cookie management API of HttpClient can co-exist with the manual
cookie handling. One can manually set request `Cookie`
headers or process response `Set-Cookie` headers in addition
or instead of the automatic cookie management

```
        HttpMethod method = new GetMethod();
        method.getParams().setCookiePolicy(CookiePolicy.IGNORE_COOKIES);
        method.setRequestHeader("Cookie", "special-cookie=value");
```

## Common Problems

The most common problems encountered with parsing cookies is due to
non-compliant servers. In these cases, switching to the compatibility
cookie specification usually solves the problem.

## Encoding Issues

Since cookies are transfered as HTTP Headers they are confined to
the US-ASCII character set. Other characters will be lost or
mangeled. Cookies are typically set and read by the same server, so
a custom scheme for escaping non-ASCII characters can be used, for
instance the well-established URL encoding scheme. If cookies are
used to transfer data between server and client both parties must
agree on the escaping scheme used in a custom way. The HttpClient
cookie implementation provides no special means to handle non-ASCII
characters nor does it issue warnings.

---
## Introduction

This document outlines some of the techniques that often help when
trying to track down a problem in *HttpClient*. Please try the suggestions
on this page before emailing the user or dev lists with questions. If
none of these things help, please provide the information they provide to
help the developers track down the problem.

## Things To Try

1. Try connecting with a normal browser and make sure the server gives
   the right response.
2. If you're using a proxy server try without it if possible.
3. Try the same code on a different server (preferably running
   different server software).
4. Check that your code matches the general pattern for using
   *HttpClient* as described in the [tutorial](tutorial.html).
5. Set the `User-Agent` request header to masquerade *HttpClient* as a popular browser such as IE or Firefox. Certain web sites are optimized
   to work with just one or a number of specific browser applications. These sites
   frequently reject requests originating from user agents they do not recognize.
   For example, setting the `User-Agent` request header to `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)` would deceive the target
   server into believing that the request was issues by Microsoft Internet Explorer
   6.0 on Windows 2000.
6. Set the [logging level](logging.html) to debug and check
   the output for the cause of the problem.
7. Enable the [wire trace](logging.html) and follow the
   communication between the client and server to determine where the
   problem is occurring.
8. Consult the "Known limitations and problems" section of the
   [SSL Guide](sslguide.html#Known%20limitations%20and%20problems)
   and the [Authentication Guide](authentication.html#Known%20limitations%20and%20problems) to see if this is a known problem and follow the
   instructions given in these resources
9. Use telnet or netcat to manually send the request to the server.
   This is particularly useful once you think you know what the problem is
   and you want to easily test that changing what *HttpClient* sends will
   fix it.
10. Use netcat in listen mode to act as the server and check how
    *HttpClient* handles various responses.
11. Try updating to the latest nightly build of *HttpClient*. Bugs
    happen and they are generally fixed pretty quickly so testing against
    the latest build is often worthwhile.

## Asking For Help

If you've tried the things above and still can't work out how to fix
the problem, it might be time to contact the [mailing list](mail-lists.html) for support. All questions, bug
reports etc should be directed to the HttpClient user list.

When you do send off the email, please include as much detail as you
can, particularly inlined wire trace logs as there is almost
nothing we can do to help without them.
If you are seeing exceptions being thrown, the full stack
trace is essential to tracking down the problem. Any of the information
you gained from the "things to try" section above are probably worth
mentioning.

## Reporting Bugs

If you're fairly certain that the problem is a bug in *HttpClient*,
log it in [JIRA](http://issues.apache.org/jira/browse/HTTPCLIENT "External Link").
Make sure you spend some time searching the existing bugs to make sure it
hasn't already been logged. If you're unsure about whether or not to log
something in JIRA, it's probably worth bringing it up on the
developer mailing list to clarify the situation.

---
## Introduction

HttpClient provides full support for HTTP over Secure Sockets Layer (SSL) or IETF Transport Layer
Security (TLS) protocols by leveraging the [Java Secure Socket Extension (JSSE)](http://java.sun.com/products/jsse/index.html "External Link"). JSSE has been integrated into the Java 2 platform as of
version 1.4 and works with HttpClient out of the box. On older Java 2 versions JSSE
needs to be manually installed and configured. Installation instructions can be found
[here](http://java.sun.com/products/jsse/doc/guide/API_users_guide.html#Installation "External Link")

## Standard SSL in HttpClient

Once you have JSSE correctly installed, secure HTTP communication over SSL should be as simple
as plain HTTP communication.

```
  HttpClient httpclient = new HttpClient();
  GetMethod httpget = new GetMethod("https://www.verisign.com/"); 
  try { 
    httpclient.executeMethod(httpget);
    System.out.println(httpget.getStatusLine());
  } finally {
    httpget.releaseConnection();
  }
```

HTTPS communication via an authenticating proxy server is also no different from plain HTTP
communication. All the low-level details of establishing a tunneled SSL connection are handled
by HttpClient:

```
  HttpClient httpclient = new HttpClient();
  httpclient.getHostConfiguration().setProxy("myproxyhost", 8080);
  httpclient.getState().setProxyCredentials("my-proxy-realm", " myproxyhost",
  new UsernamePasswordCredentials("my-proxy-username", "my-proxy-password"));
  GetMethod httpget = new GetMethod("https://www.verisign.com/");
  try { 
    httpclient.executeMethod(httpget);
    System.out.println(httpget.getStatusLine());
  } finally {
    httpget.releaseConnection();
  }
```

## Customizing SSL in HttpClient

The default behaviour of HttpClient is suitable for most uses, however
there are some aspects which you may want to configure. The most common
requirements for customizing SSL are:

* Ability to accept self-signed or untrusted SSL certificates. This
  is highlighted by an `SSLException` with the message
  *Unrecognized SSL handshake* (or similar) being thrown when a
  connection attempt is made.
* You want to use a third party SSL library instead of Sun's default
  implementation.

Implementation of a custom protocol involves the following steps:

1. Provide a custom socket factory that implements
   [org.apache.commons.httpclient.protocol.SecureProtocolSocketFactory](apidocs/org/apache/commons/httpclient/protocol/SecureProtocolSocketFactory.html) interface. The socket
   factory is responsible for opening a socket to the target server
   using either the standard or a third party SSL library and
   performing any required initialization such as performing the
   connection handshake. Generally the initialization is performed
   automatically when the socket is created.
2. Instantiate an object of type [org.apache.commons.httpclient.protocol.Protocol](apidocs/org/apache/commons/httpclient/protocol/Protocol.html). The new instance
   would be created with a valid URI protocol scheme (https in this
   case), the custom socket factory (discussed above) and a default port
   number (typically 443 for https). For example:

   ```
   Protocol myhttps = new Protocol("https", new MySSLSocketFactory(), 443);
   ```

   The new instance of protocol can then be set as the protocol handler
   for a HostConfiguration. For example to configure the default host and
   protocol handler for a HttpClient instance use:

   ```
   HttpClient httpclient = new HttpClient();
   httpclient.getHostConfiguration().setHost("www.whatever.com", 443, myhttps);
   GetMethod httpget = new GetMethod("/");
   try {
     httpclient.executeMethod(httpget);
     System.out.println(httpget.getStatusLine());
   } finally {
     httpget.releaseConnection();
   }
   ```
3. Finally, you can register your custom protocol as the default handler
   for a specific protocol designator (eg: https) by calling the
   Protocol.registerProtocol method. You can specify your own protocol
   designator (such as 'myhttps') if you need to use your custom
   protocol as well as the default SSL protocol implementation.

   ```
   Protocol.registerProtocol("myhttps", 
   new Protocol("https", new MySSLSocketFactory(), 9443));
   ```

   Once registered the protocol be used as a 'virtual' scheme inside target URIs.

   ```
   HttpClient httpclient = new HttpClient();
   GetMethod httpget = new GetMethod("myhttps://www.whatever.com/");
   try {
     httpclient.executeMethod(httpget);
     System.out.println(httpget.getStatusLine());
   } finally {
     httpget.releaseConnection();
   }
   ```

   If you want this protocol to represent the default SSL protocol implementation, simply register
   it under 'https' designator, which will make the protocol object take place of the existing one

   ```
   Protocol.registerProtocol("https", 
   new Protocol("https", new MySSLSocketFactory(), 443));
   HttpClient httpclient = new HttpClient();
   GetMethod httpget = new GetMethod("https://www.whatever.com/");
   try {
     httpclient.executeMethod(httpget);
     System.out.println(httpget.getStatusLine());
   } finally {
     httpget.releaseConnection();
   }
   ```

## Examples of SSL customization in HttpClient

There are several custom socket factories available in our contribution
package. They can be a good start for those who seek to tailor the
behavior of the HTTPS protocol to the specific needs of their
application:

* [EasySSLProtocolSocketFactory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/contrib/org/apache/commons/httpclient/contrib/ssl/EasySSLProtocolSocketFactory.java?view=markup "External Link") can be used to create SSL connections that allow the target
  server to authenticate with a self-signed certificate.
* [StrictSSLProtocolSocketFactory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/contrib/org/apache/commons/httpclient/contrib/ssl/StrictSSLProtocolSocketFactory.java?view=markup "External Link") can be used to create SSL connections that can optionally perform host name verification in order to help preventing man-in-the-middle type of attacks.
* [AuthSSLProtocolSocketFactory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/contrib/org/apache/commons/httpclient/contrib/ssl/AuthSSLProtocolSocketFactory.java?view=markup "External Link") can be used to optionally enforce mutual client/server authentication. This is the most flexible
  implementation of a protocol socket factory. It allows for customization of most, if not all, aspects of the SSL authentication.

## Known limitations and problems

1. **Persistent SSL connections do not work on Sun's JVMs below 1.4**

   Due to what appears to be a bug in Sun's older (below 1.4) implementation of
   Java Virtual Machines or JSSE there's no reliable way of telling if an SSL connection
   is 'stale' or not. For example, the HTTP 1.1 specification permits HTTP servers in
   'keep-alive' mode to drop the connection to the client after a given period inactivity
   without having to notify the client, effectively rendering such connection unusable or
   'stale'. For the HTTP agent written in Java there's no reliable way to test
   if a connection is 'stale' other than attempting to perform a read on it.
   However, a read
   operation on an idle SSL connection on Sun JVM older than 1.4 returns 'end of stream'
   instead of an expected read timeout. That effectively makes the connection appear 'stale'
   to HttpClient, which leaves it with no other way but to drop the connection and to
   open a new one, thus defeating HTTP 1.1 keep-alive mechanism and resulting in significant
   performance degradation (SSL authentication is a highly time consuming operation). The problem appears to have been fixed in Sun's
   Java 1.4 SSL implementation. Sockets which are not using HTTPS are
   unaffected on any JVM.

   **Workaround:** Disable stale connection check if upgrade to Java 1.4 or above is
   not an option. Please note that HttpClient will no longer be able to detect invalid connections
   and some requests may fail due to transport errors. For details on how transport errors can be
   recovered from please refer to the [Exception Handling Guide](exception-handling.html#Transport%20exceptions). If persistent SSL connections support and transport reliability
   is an issue for your application we strongly advise you to upgrade to Java 1.4.
2. **Authetication schemes that rely on persistent connection state do not work on Sun's JVMs
   below 1.4 if SSL is used**

   This problem is directly related to the problem described above. Certain authentication schemes or
   certain implementations of standard authentication schemes are connection based, that is, the user
   authentication is performed once when the connection is being established, rather than every time
   a request is being processed. Microsoft NTLM scheme and Digest scheme as implemented in Microsoft
   Proxy and IIS servers are known to fall into this category. If connections cannot be kept alive
   the user authorization is lost along with the persistent connection state

   **Workaround:** Disable stale connection check or upgrade to Java 1.4 or above.
3. **JSSE prior to Java 1.4 incorrectly reports socket timeout.**

   Prior to Java 1.4, in Sun's JSSE implementation, a read operation that has timed out incorrect
   reports end of stream condition instead of throwing java.io.InterruptedIOException as expected.
   HttpClient responds to this exception by assuming that the connection was dropped and throws a
   NoHttpResponseException. It should instead report "java.io.InterruptedIOException: Read timed
   out". If you encounter NoHttpResponseException when working with an older version of JDK and
   JSSE, it can be caused by the timeout waiting for data and not by a problem with the connection.

   **Work-around:** One possible solution is to increase the timeout value as the server is
   taking too long to start sending the response. Alternatively you may choose to upgrade to Java 1.4 or
   above which does not exhibit this problem.

   The problem has been discovered and reported by Daniel C. Amadei.
4. **HttpClient does not work with IBM JSSE shipped with IBM Websphere Application Platform**

   Several releases of the IBM JSSE exhibit a bug that cause HttpClient to fail while detecting the size
   of the socket send buffer (java.net.Socket.getSendBufferSize method throws java.net.SocketException:
   "Socket closed" exception).

   **Solution:** Make sure that you have all the latest Websphere fix packs applied and IBMJSSE
   is at least version 1.0.3. HttpClient users have reported that IBM Websphere Application Server versions
   4.0.6, 5.0.2.2, 5.1.0 and above do not exhibit this problem.

## Troubleshooting

JSSE is prone to configuration problems, especially on older JVMs,
which it is not an integral part of. As such, if you do encounter
problems with SSL and HttpClient it is important to check that JSSE is
correctly installed.

The application below can be used as an ultimate test that can reliably
tell if SSL configured properly, as it relies on a plain socket in
order to communicate with the target server. If an exception is thrown
when executing this code, SSL is not correctly installed and configured.
Please refer to Sun's official resources for support or additional
details on JSSE configuration.

```
  import java.io.BufferedReader;
  import java.io.InputStreamReader;
  import java.io.OutputStreamWriter;
  import java.io.Writer;
  import java.net.Socket;

  import javax.net.ssl.SSLSocketFactory;

  public class Test {
        
     public static final String TARGET_HTTPS_SERVER = "www.verisign.com"; 
     public static final int    TARGET_HTTPS_PORT   = 443; 
        
     public static void main(String[] args) throws Exception {
        
       Socket socket = SSLSocketFactory.getDefault().
         createSocket(TARGET_HTTPS_SERVER, TARGET_HTTPS_PORT);
       try {
         Writer out = new OutputStreamWriter(
            socket.getOutputStream(), "ISO-8859-1");
         out.write("GET / HTTP/1.1\r\n");  
         out.write("Host: " + TARGET_HTTPS_SERVER + ":" + 
             TARGET_HTTPS_PORT + "\r\n");  
         out.write("Agent: SSL-TEST\r\n");  
         out.write("\r\n");  
         out.flush();  
         BufferedReader in = new BufferedReader(
            new InputStreamReader(socket.getInputStream(), "ISO-8859-1"));
         String line = null;
         while ((line = in.readLine()) != null) {
            System.out.println(line);
         }
       } finally {
         socket.close(); 
       }
     }
  }
```

---
## Introduction

HttpClient supports three different types of http authentication schemes:
Basic, Digest and NTLM. These can be used to authenticate with http servers
or proxies.

### Contents

* [Server Authentication](#Server_Authentication)
  * [Preemptive Authentication](#Preemptive_Authentication)
  * [Security aspects of server authentication](#Security_aspects_of_server_authentication)
* [Proxy Authentication](#Proxy_Authentication)
* [Authentication Schemes](#Authentication_Schemes)
  * [Basic](#Basic)
  * [Digest](#Digest)
  * [NTLM](#NTLM)
  * [Alternate authentication](#Alternate_authentication)
  * [Custom authentication scheme](#Custom_authentication_scheme)
* [Examples](#Examples)
* [Known limitations and problems](#Known_limitations_and_problems)
* [Troubleshooting](#Troubleshooting)

## Server Authentication

HttpClient handles authenticating with servers almost transparently,
the only thing a developer must do is actually provide the login
credentials. These credentials are stored in the HttpState instance
and can be set or retrieved using the `setCredentials(AuthScope authscope,
Credentials cred)` and `getCredentials(AuthScope authscope)`
methods.

The automatic authorization built in to HttpClient can be disabled
with the method `setDoAuthentication(boolean doAuthentication)`
in the HttpMethod class. The change only affects that method instance.

### Preemptive Authentication

Preemptive authentication can be enabled within HttpClient. In this
mode HttpClient will send the basic authentication response even before
the server gives an unauthorized response in certain situations, thus reducing the overhead
of making the connection. To enable this use the following:

```
client.getParams().setAuthenticationPreemptive(true);
```

Preemptive authentication mode also requires default Credentials to be set
for the target or proxy host against which preemptive authentication is to be
attempted. Failure to provide default credentials will render the preemptive
authentication mode ineffective.

```
Credentials defaultcreds = new UsernamePasswordCredentials("username", "password");
client.getState().setCredentials(new AuthScope("myhost", 80, AuthScope.ANY_REALM), defaultcreds);
```

The preemptive authentication in HttpClient conforms to rfc2617:

> A client SHOULD assume that all paths at or deeper than the depth
> of the last symbolic element in the path field of the Request-URI also
> are within the protection space specified by the Basic realm value
> of the current challenge. A client MAY preemptively send the
> corresponding Authorization header with requests for resources in
> that space without receipt of another challenge from the server.
> Similarly, when a client sends a request to a proxy, it may reuse
> a userid and password in the Proxy-Authorization header field without
> receiving another challenge from the proxy server.

### Security aspects of server authentication

Use default credentials with caution when developing applications
that may need to communicate with untrusted web sites or web applications. When
preemptive authentication is activated or credentials are not explicitly given
for a specific authentication realm and host HttpClient will use default credentials
to try to authenticate with the target site. If you want to avoid sending sensitive
credentials to an untrusted site, narrow the credentials scope as much as possible:
always specify the host and, when known, the realm the credentials are intended for.

Setting credentials with AuthScope.ANY authentication scope (`null` value
for host and/or realm) is highly discouraged in production applications. Doing this
will result in the credentials being sent for all authentication attempts (all
requests in the case of preemptive authentication). Use of this setting should be
limited to debugging only.

```
// To be avoided unless in debug mode
Credentials defaultcreds = new UsernamePasswordCredentials("username", "password");
client.getState().setCredentials(AuthScope.ANY, defaultcreds);
```

## Proxy Authentication

Proxy authentication in HttpClient is almost identical to server
authentication with the exception that the credentials for each are
stored independantly. So for proxy authentication you must use
`setProxyCredentials(AuthScope authscope, Credentials cred)` and
`getProxyCredentials(AuthScope authscope)`.

## Authentication Schemes

The following authentication schemes are supported by HttpClient.

### Basic

Basic authentication is the original and most compatible authentication
scheme for HTTP. Unfortunately, it is also the least secure as it sends
the username and password unencrypted to the server. Basic authentication
requires an instance of UsernamePasswordCredentials (which NTCredentials
extends) to be available, either for the specific realm specified by the
server or as the default credentials.

### Digest

Digest authentication was added in the HTTP 1.1 protocol and while
not being as widely supported as Basic authentication there is a great
deal of support for it. Digest authentication is significantly more
secure than basic authentication as it never transfers the actual
password across the network, but instead uses it to encrypt a "nonce"
value sent from the server.

Digest authentication requires an instance of
UsernamePasswordCredentials (which NTCredentials extends) to be
available either for the specific realm specified by the server or as
the default credentials.

### NTLM

NTLM is the most complex of the authentication protocols supported
by HttpClient. It is a proprietary protocol designed by Microsoft
with no publicly available specification. Early version of NTLM were
less secure than Digest authentication due to faults in the design,
however these were fixed in a service pack for Windows NT 4 and the
protocol is now considered more secure than Digest authentication.

NTLM authentication requires an instance of NTCredentials be
available for the *domain name* of the server or the default
credentials. Note that since NTLM does not use the notion of realms
HttpClient uses the domain name of the server as the name of the realm.
Also note that the username provided to the NTCredentials should not
be prefixed with the domain - ie: "adrian" is correct whereas
"DOMAIN\adrian" is not correct.

There are some significant differences in the way that NTLM works
compared with basic and digest authentication. These differences
are generally handled by HttpClient, however having an
understanding of these differences can help avoid problems when using
NTLM authentication.

1. NTLM authentication works almost exactly the same as any other form of
   authentication in terms of the HttpClient API. The only difference is that
   you need to supply 'NTCredentials' instead of 'UsernamePasswordCredentials'
   (NTCredentials actually extends UsernamePasswordCredentials so you can use
   NTCredentials right throughout your application if need be).
2. The realm for NTLM authentication is the domain name of the computer
   being connected to, this can be troublesome as servers often have
   multiple domain names that refer to them. Only the domain name
   that HttpClient connects to (as specified by the HostConfiguration)
   is used to look up the credentials.
   It is generally advised that while initially testing NTLM
   authentication, you pass the realm in as null which is used as
   the default.
3. NTLM authenticates a connection and not a request, so you need to
   authenticate every time a new connection is made and keeping the connection
   open during authentication is vital. Due to this, NTLM cannot
   be used to authenticate with both a proxy and the server, nor can
   NTLM be used with HTTP 1.0 connections or servers that do not
   support HTTP keep-alives.

For a detailed explanation of how NTLM authentication works, please see
[http://davenport.sourceforge.net/ntlm.html](http://davenport.sourceforge.net/ntlm.html "External Link").

### Alternate authentication

Some servers support multiple schemes for authenticating users.
Given that only one scheme may be used at a time for authenticating, HttpClient
must choose which scheme to use. To accompish this, HttpClient uses an order of
preference to select the correct authentication scheme. By default
this order is: NTLM, Digest, Basic.

In certain cases it may be desirable to change this default. The
default preference of the authentication schemes may be altered using the
'http.auth.scheme-priority' parameter. The parameter value is expected to be a List
of Strings containing names of authentication schemes in descending order of
preference.

```
HttpClient client = new HttpClient();
List authPrefs = new ArrayList(2);
authPrefs.add(AuthPolicy.DIGEST);
authPrefs.add(AuthPolicy.BASIC);
// This will exclude the NTLM authentication scheme
client.getParams().setParameter(AuthPolicy.AUTH_SCHEME_PRIORITY, authPrefs);
```

### Custom authentication scheme

HttpClient natively supports basic, digest, and NTLM authentication. It also contains
a mechanism to plugin additional custom authentication schemes via the
[AuthScheme](apidocs/org/apache/commons/httpclient/auth/AuthScheme.html) interface.
The following steps are required to make use of a custom authentication scheme.

1. Implement the `AuthScheme` interface.
2. Register the custom `AuthScheme` with [AuthPolicy.registerAuthScheme()](apidocs/org/apache/commons/httpclient/auth/AuthPolicy.html#registerAuthScheme(java.lang.String,%20java.lang.Class)).
3. Include the custom `AuthScheme` in the AuthPolicy.AUTH\_SCHEME\_PRIORITY preference
   (see the [Alternate authentication](#Alternate_authentication) section).

## Examples

There are a number of authentication examples in the [example directory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link"), including:

* [Basic authentication](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/BasicAuthenticationExample.java?view=markup "External Link")
* [Custom authentication](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/CustomAuthenticationExample.java?view=markup "External Link")
* [Interactive authentication](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/InteractiveAuthenticationExample.java?view=markup "External Link")

## Known limitations and problems

1. **Authentication schemes that rely on persistent connection state do not work on Sun's JVMs
   below 1.4 if SSL is used**

   For details please refer to the [Known
   limitations and problems](sslguide.html#Known%20limitations%20and%20problems) section of the [SSL Guide](sslguide.html)

   **Workaround:** Disable stale connection check or upgrade to Java 1.4 or above.
2. **Cannot authenticate with Microsoft IIS using NTLM authentication scheme**

   NT Lan Manager (NTLM) authentication is a proprietary, closed challenge/response authentication
   protocol for Microsoft Windows. Only some details about NTLM protocol are available through
   reverse engineering. HttpClient provides limited support for what is known as NTLMv1, the early
   version of the NTLM protocol. HttpClient does not support NTLMv2 at all.

   **Workaround:** Disable NTLMv2. For details refer to this Microsoft Support
   [Article](http://support.microsoft.com/default.aspx?scid=KB;en-us;239869 "External Link")

## Troubleshooting

Some authentication schemes may use cryptographic algorithms. It is recommended to include the
[Java Cryptography Extension](http://java.sun.com/products/jce/ "New Window") in
your runtime environment prior to JDK 1.4. Also note that you must register the JCE
implementation manually as HttpClient will not do so automatically. For instance to
register the Sun JCE implementation, you should execute the following code before attempting
to use HttpClient.

```
String secProviderName = "com.sun.crypto.provider.SunJCE");
java.security.Provider secProvider = 
    (java.security.Provider)Class.forName(secProviderName).newInstance();
Security.addProvider(secProvider);
	
```

---
## General Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by
[Maven](http://maven.apache.org/ "External Link")
on behalf of the project.

### Overview

| Document | Description |
| --- | --- |
| [Mailing Lists](mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Project Team](team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Dependencies](dependencies.html) | This document lists the projects dependencies and provides information on each dependency. |
| [Source Repository](scm-usage.html) | This is a link to the online source repository that can be viewed via a web browser. |
| [Issue Tracking](issue-tracking.html) | This is a link to the issue tracking system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |

---
## Introduction

This document provides an overview of how to use HttpClient safely from within a
multi-threaded environment. It is broken down into the following main sections:

* [MultiThreadedHttpConnectionManager](#MultiThreadedHttpConnectionManager)
* [Connection Release](#Connection_Release)

Please see the [MultiThreadedExample](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/MultiThreadedExample.java?view=markup "External Link")
for a concrete example.

## MultiThreadedHttpConnectionManager

The main reason for using multiple theads in HttpClient is to allow the
execution of multiple methods at once (Simultaniously downloading the latest builds of HttpClient and
Tomcat for example). During execution each method uses an instance of an HttpConnection.
Since connections can only be safely used from a single thread and method at a time and
are a finite resource, we need to ensure that connections are properly allocated to the methods that require them.
This job goes to the [MultiThreadedHttpConnectionManager](apidocs/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html).

To get started one must create an instance of the MultiThreadedHttpConnectionManager
and give it to an HttpClient. This looks something like:

```
      	MultiThreadedHttpConnectionManager connectionManager = 
      		new MultiThreadedHttpConnectionManager();
      	HttpClient client = new HttpClient(connectionManager);
```

This instance of HttpClient can now be used to execute multiple methods from multiple
threads. Each subsequent call to HttpClient.executeMethod() will go to the connection
manager and ask for an instance of HttpConnection. This connection will be checked out
to the method and as a result it must also be returned. More on this below in **Connection Release**.

### Options

The MultiThreadedHttpConnectionManager supports the following options:

|  |  |
| --- | --- |
| connectionStaleCheckingEnabled | The connectionStaleCheckingEnabled flag to set on all created connections. This value should be left true except in special circumstances. Consult the [HttpConnection](apidocs/org/apache/commons/httpclient/HttpConnection.html#setStaleCheckingEnabled(boolean)) docs for more detail. |
| maxConnectionsPerHost | The maximum number of connections that will be created for any particular HostConfiguration. Defaults to 2. |
| maxTotalConnections | The maximum number of active connections. Defaults to 20. |

In general the connection manager makes an attempt to reuse connections
for a particular host while still allowing different connections to
be used simultaneously. Connection are reclaimed using a least recently
used approach.

## Connection Release

One main side effect of connection management is that connections must
be manually released when no longer used. This is due to the fact
that HttpClient cannot determine when a method is no longer using its connection.
This occurs because a method's response body is not read directly by
HttpClient, but by the application using HttpClient. When the response is read it must obviously make use of the method's
connection. Thus, a connection cannot be released from a method until the method's
response body is read which is after HttpClient finishes executing the
method. The application therefore must manually release the
connection by calling releaseConnection() on the method after the
response body has been read. To safely ensure
connection release HttpClient should be used in the following manner:

```
      	MultiThreadedHttpConnectionManager connectionManager = 
      		new MultiThreadedHttpConnectionManager();
      	HttpClient client = new HttpClient(connectionManager);
			...
        // and then from inside some thread executing a method
        GetMethod get = new GetMethod("http://httpcomponents.apache.org/");
        try {
            client.executeMethod(get);
            // print response to stdout
            System.out.println(get.getResponseBodyAsStream());
        } finally {
            // be sure the connection is released back to the connection 
            // manager
            get.releaseConnection();
        }
```

Particularly, notice that the connection is released regardless of
what the result of executing the method was or whether or not an
exception was thrown. For every call to HttpClient.executeMethod there
must be a matching call to method.releaseConnection().

---
## Introduction

This document provides a brief guide to custom handling of redirects
with *HttpClient*.

There are a few types of redirect that HttpClient can't handle
automatically either because they require user interaction, or they are
outside of the scope of HttpClient (these status codes are listed [below](#Special%20Redirect%20Codes)), or due to internal
limitations. Currently HttpClient is unable to automatically handle
redirects of entity enclosing methods such as POST and
PUT. There can also be situations when manual processing
of redirects is desired due to specific application requirements.

## Handling redirects manually

All response codes between 300 and 399 inclusive are redirect responses
of some form. The most common redirect response codes are:

* 301 Moved Permanently.
  `HttpStatus.SC_MOVED_PERMANENTLY`
* 302 Moved Temporarily.
  `HttpStatus.SC_MOVED_TEMPORARILY`
* 303 See Other. `HttpStatus.SC_SEE_OTHER`
* 307 Temporary Redirect.
  `HttpStatus.SC_TEMPORARY_REDIRECT`

**Note:** there are a number of response codes in the 3xx range
which do not simply indicate a different URI to send the request to.
These response codes are listed [below](#Special%20Redirect%20Codes) and the manner they are
handled will be application specific.

When your application receives one of the "simple" redirect responses,
it should extract the new URL from the HttpMethod object and retry
downloading from that URL.
Additionally, it is usually a good idea to limit the number of
redirects that will be followed in case the redirects form a recursive
loop.

The URL to connect to can be extracted from the Location
header.

```
        String redirectLocation;
        Header locationHeader = method.getResponseHeader("location");
        if (locationHeader != null) {
            redirectLocation = locationHeader.getValue();
        } else {
            // The response is invalid and did not provide the new location for
            // the resource.  Report an error or possibly handle the response
            // like a 404 Not Found error.
        }
```

Once you have determined the new location, you can reattempt the
connection as normal. See the [Tutorial](tutorial.html) for
more information on this.

## Special Redirect Codes

The HTTP specification defines a number of somewhat unusual redirect
response codes that will likely need to be handled in a different manner
to the codes above. In particular these are:

* 300 Multiple Choices.
  `HttpStatus.SC_MULTIPLE_CHOICES`  

  There are multiple choices available for the redirection. A
  preferred redirect URI may be specified in the location header, however
  generally it is expected that the user will be given the choice of
  which URI to be redirected to. It is however permissible to simply
  select one of the available choices arbitrarily.
* 304 Not Modified.
  `HttpStatus.SC_NOT_MODIFIED`  

  The resource has not been modified since it was last requested. You
  should retrieve the resource from cache instead. If the resource is no
  longer available in the cache the request should be retried without the
  conditional headers.
* 305 Use Proxy.
  `HttpStatus.SC_USE_PROXY`  

  The resource must be accessed through the specified proxy. The
  proxy is specified in the Location header.

---
## Introduction

By default HttpClient is configured to provide maximum reliability and standards
compliance rather than raw performance. There are several configuration options and
optimization techniques which can significantly improve the performance of HttpClient.
This document outlines various techniques to achieve maximum HttpClient performance.

### Contents

* [Reuse the HttpClient instance](#Reuse_of_HttpClient_instance)
* [Connection persistence](#Connection_persistence)
* [Concurrent execution of HTTP methods](#Concurrent_execution_of_HTTP_methods)
* [Request/Response entity streaming](#Request_Response_entity_streaming)
* [Expect-continue handshake](#Expect-continue_handshake)
* [Stale connection check](#Stale_connection_check)
* [Cookie processing](#Cookie_processing)

## Reuse the HttpClient instance

Generally it is recommended to have a single instance of HttpClient per communication
component or even per application. However, if the application makes use of HttpClient
only very infrequently, and keeping an idle instance of HttpClient in memory is not warranted,
it is highly recommended to explicitly [shut down](apidocs/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#shutdown()) the multithreaded connection manager prior to disposing
the HttpClient instance. This will ensure proper closure of all HTTP connections in the
connection pool.

## Connection persistence

HttpClient always does its best to reuse connections. Connection persistence is enabled
by default and requires no configuration. Under some situations this can lead to leaked
connections and therefore lost resources. The easiest way to disable connection persistence
is to provide or extend a connection manager that force-closes connections
upon release in the [releaseConnection](apidocs/org/apache/commons/httpclient/HttpConnectionManager.html#releaseConnection(org.apache.commons.httpclient.HttpConnection)) method.

## Concurrent execution of HTTP methods

If the application logic allows for execution of multiple HTTP requests concurrently
(e.g. multiple requests against various sites, or multiple requests representing
different user identities), the use of a dedicated thread per HTTP session can result in a
significant performance gain. HttpClient is fully thread-safe when used with a thread-safe
connection manager such as [MultiThreadedHttpConnectionManager](apidocs/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html). Please note that each respective thread of execution
must have a local instance of HttpMethod and can have a local instance of HttpState or/and
HostConfiguration to represent a specific host configuration and conversational state. At the
same time the HttpClient instance and connection manager should be shared among all threads
for maximum efficiency.

For details on using multiple threads with HttpClient please refer to the [HttpClient Threading Guide](threading.html).

## Request/Response entity streaming

HttpClient is capable of efficient request/response body streaming. Large entities may be submitted
or received without being buffered in memory. This is especially critical if multiple HTTP
methods may be executed concurrently. While there are convenience methods to deal with entities such as
strings or byte arrays, their use is discouraged. Unless used carefully they can easily lead to
out of memory conditions, since they imply buffering of the complete entity in memory.

**Response streaming:** It is recommended to consume the HTTP response body as a stream of
bytes/characters using HttpMethod#getResponseBodyAsStream method. The use of HttpMethod#getResponseBody and
HttpMethod#getResponseBodyAsString are strongly discouraged.

```
  HttpClient httpclient = new HttpClient();
  GetMethod httpget = new GetMethod("http://www.myhost.com/");
  try {
    httpclient.executeMethod(httpget);
    Reader reader = new InputStreamReader(
            httpget.getResponseBodyAsStream(), httpget.getResponseCharSet()); 
    // consume the response entity
  } finally {
    httpget.releaseConnection();
  }
```

**Request streaming:** The main difficulty encountered when streaming request bodies is that
some entity enclosing methods need to be retried due to an authentication failure or an I/O failure.
Obviously non-buffered entities cannot be reread and resubmitted. The recommended approach is to create a custom
[RequestEntity](apidocs/org/apache/commons/httpclient/methods/RequestEntity.html) capable of
reconstructing the underlying input stream.

```
public class FileRequestEntity implements RequestEntity {

    private File file = null;
    
    public FileRequestEntity(File file) {
        super();
        this.file = file;
    }

    public boolean isRepeatable() {
        return true;
    }

    public String getContentType() {
        return "text/plain; charset=UTF-8";
    }
    
    public void writeRequest(OutputStream out) throws IOException {
        InputStream in = new FileInputStream(this.file);
        try {
            int l;
            byte[] buffer = new byte[1024];
            while ((l = in.read(buffer)) != -1) {
                out.write(buffer, 0, l);
            }
        } finally {
            in.close();
        }
    }

    public long getContentLength() {
        return file.length();
    }
}

File myfile = new File("myfile.txt");
PostMethod httppost = new PostMethod("/stuff");
httppost.setRequestEntity(new FileRequestEntity(myfile));
```

## Expect-continue handshake

The purpose of the HTTP 100 (Continue) status is to allow a client sending a request entity to
determine if the target server is willing to accept the request (based on the
request headers) before the client sends the request entity. It is highly inefficient for the client
to send the request entity if the server will reject the request without looking at the body.
Authentication failures are the most common reason for the request to be rejected based on the request
headers alone. Therefore, use of the 'Expect-continue' handshake is especially recommended with
those target servers that require HTTP authentication. For proxied requests caution
must be taken as older HTTP/1.0 proxies may be unable to correctly handle the 'Expect-continue'
handshake.

See the [http.protocol.expect-continue](preference-api.html) parameter documentation
for more information.

## Stale connection check

HTTP specification permits both the client and the server to terminate a persistent (keep-alive)
connection at any time without notice to the counterpart, thus rendering the connection invalid
or stale. By default HttpClient performs a check, just prior to executing a request, to determine if the
active connection is stale. The cost of this operation is about 15-30 ms, depending on the JRE used.
Disabling stale connection check may result in slight performance improvement, especially for small
payload responses, at the risk of getting an I/O error when executing a request over a connection
that has been closed at the server side.

See the [http.connection.stalecheck](preference-api.html) parameter documentation for more
information.

## Cookie processing

If an application, such as web spider, does not need to maintain conversational state with the target
server, a small performance gain can made by disabling cookie processing. For details
on cookie processing please to the [HttpClient Cookies Guide](cookies.html).

---
## Table of contents

* [HttpClient preference architecture](#HttpClient_preference_architecture)
  * [HTTP parameters](#HTTP_parameters)
  * [HTTP parameter hierarchy](#HTTP_parameter_hierarchy)
* [Supported parameters](#Supported_parameters)
  * [HTTP method parameters](#HTTP_method_parameters)
  * [HTTP connection parameters](#HTTP_connection_parameters)
  * [HTTP connection manager parameters](#HTTP_connection_manager_parameters)
  * [HTTP client parameters](#HTTP_client_parameters)

## HttpClient preference architecture

Quality and extent of the [`HTTP/1.0`](http://www.ietf.org/rfc/rfc1945.txt "External Link") and [`HTTP/1.1`](http://www.ietf.org/rfc/rfc2616.txt "External Link") spec compliance vary significantly among commonly
used HTTP agents and HTTP servers. That requires of HttpClient to be able to

* mimic (mis-)behavior of widely used web browsers;
* support flexible and configurable level of leniency toward non-critical
  protocol violations especially in those gray areas of the specification
  subject to different, at times conflicting, interpretations;
* apply a different set of parameters to individual HTTP methods, hosts, or
  client instances using common interface;

### HTTP parameters

As of version 3 HttpClient sports a new preference API based on
[HttpParams](apidocs/org/apache/commons/httpclient/params/HttpParams.html) interface. All major components of the HttpClient toolkit
(agents, host configurations, methods, connections, connection managers)
contain a collection of HTTP parameters, which determine the runtime behavior
of those components.

```
HttpClient httpclient = new HttpClient();
HttpVersion ver = (HttpVersion)httpclient.getParams().getParameter("http.protocol.version");
```

In a nutshell HTTP parameters is a collection of name/object pairs that can be linked
with other collections to form a hierarchy. If a particular parameter value has not been
explicitly defined in the collection itself, its value will be drawn from the upper level
collection of parameters.

```
HttpClient httpclient = new HttpClient();
httpclient.getParams().setParameter("http.protocol.version", HttpVersion.HTTP_1_1);
httpclient.getParams().setParameter("http.socket.timeout", new Integer(1000));
httpclient.getParams().setParameter("http.protocol.content-charset", "UTF-8");

HostConfiguration hostconfig = new HostConfiguration();
hostconfig.setHost("www.yahoo.com");
hostconfig.getParams().setParameter("http.protocol.version", HttpVersion.HTTP_1_0);
		
GetMethod httpget = new GetMethod("/");
httpget.getParams().setParameter("http.socket.timeout", new Integer(5000));
		
try {
  // Internally the parameter collections will be linked together
  // by performing the following operations: 
  // hostconfig.getParams().setDefaults(httpclient.getParams());
  // httpget.getParams().setDefaults(hostconfig.getParams());
  httpclient.executeMethod(hostconfig, httpget);
  System.out.println(httpget.getParams().getParameter("http.protocol.version"));
  System.out.println(httpget.getParams().getParameter("http.socket.timeout"));
  System.out.println(httpget.getParams().getParameter("http.protocol.content-charset"));
} finally {
  httpget.releaseConnection();
}
```

The code above will produce the following output:

```
HTTP/1.0
5000
UTF-8
```

When resolving a parameter HttpClient uses the following algorithm:

* start parameter lookup from the lowest level at which this parameter applies
* if the parameter is undefined at the current level, defer its resolution to the
  next level up in the hierarchy
* return parameter value from the lowest level in the hierarchy the parameter
  defined at
* return null if the parameter is undefined

This architecture enables the users to define generic parameters at a higher
level (for instance, at the agent level or host level) and selectively override
specific parameters at a lower level (for instance, at the method level). Whenever
a parameter is not explicitly defined at a given level, the defaults of the upper
levels will apply.

### HTTP parameter hierarchy

Presently HttpClient provides the following parameter hierarchy:

```
global--+                            | DefaultHttpParams
        |                            |
      client                         | HttpClient
        |                            |
        +-- connection manager       | HttpConnectionManager
        |     |                      |
        |     +-- connection         | HttpConnection
        |                            |
        +-- host                     | HostConfiguration
              |                      |
              +-- method             | HttpMethod
```

## Supported parameters

### HTTP method parameters

Applicable at the following levels: **global** -> **client** -> **host** -> **method**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.useragent | String | The content of the `User-Agent` header used by the HTTP methods. | official release name, e.g. "Jakarta Commons-HttpClient/3.0" |
| http.protocol.version | [HttpVersion](apidocs/org/apache/commons/httpclient/HttpVersion.html) | The HTTP protocol version used per default by the HTTP methods. | [`HttpVersion.HTTP_1_1`](apidocs/org/apache/commons/httpclient/HttpVersion.html#HTTP_1_1) |
| http.protocol.unambiguous-statusline | Boolean | Defines whether HTTP methods should reject ambiguous HTTP status line. | `<undefined>` |
| http.protocol.single-cookie-header | Boolean | Defines whether cookies should be put on a single response header. | `<undefined>` |
| http.protocol.strict-transfer-encoding | Boolean | Defines whether responses with an invalid `Transfer-Encoding` header should be rejected. | `<undefined>` |
| http.protocol.reject-head-body | Boolean | Defines whether the content body sent in response to `HEAD` request should be rejected. | `<undefined>` |
| http.protocol.head-body-timeout | Integer | Sets period of time in milliseconds to wait for a content body sent in response to `HEAD` response from a non-compliant server. If the parameter is not set or set to `-1` non-compliant response body check is disabled. | `<undefined>` |
| http.protocol.expect-continue | Boolean | Activates 'Expect: 100-Continue' handshake for the entity enclosing methods. The 'Expect: 100-Continue' handshake allows a client that is sending a request message with a request body to determine if the origin server is willing to accept the request (based on the request headers) before the client sends the request body.  The use of the 'Expect: 100-continue' handshake can result in noticeable performance improvement for entity enclosing requests (such as `POST` and `PUT`) that require the target server's authentication.  'Expect: 100-continue' handshake should be used with caution, as it may cause problems with HTTP servers and proxies that do not support `HTTP/1.1` protocol.  `<undefined>` | |
| http.protocol.credential-charset | String | The charset to be used when encoding credentials. If not defined then the value of the 'http.protocol.element-charset' should be used. | `<undefined>` |
| http.protocol.element-charset | String | The charset to be used for encoding/decoding HTTP protocol elements (status line and headers). | 'US-ASCII' |
| http.protocol.content-charset | String | The charset to be used for encoding content body. | 'ISO-8859-1' |
| http.protocol.cookie-policy | String | The cookie policy to be used for cookie management. | [`CookiePolicy.RFC_2109`](apidocs/org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2109) |
| http.protocol.warn-extra-input | Boolean | Defines HttpClient's behavior when a response provides more bytes than expected (specified with `Content-Length` header, for example).  Such surplus data makes the HTTP connection unreliable for keep-alive requests, as malicious response data (faked headers etc.) can lead to undesired results on the next request using that connection.  If this parameter is set to `true`, any detection of extra input data will generate a warning in the log. | `<undefined>` |
| http.protocol.status-line-garbage-limit | Integer | Defines the maximum number of ignorable lines before we expect a HTTP response's status code.  With HTTP/1.1 persistent connections, the problem arises that broken scripts could return a wrong `Content-Length` (there are more bytes sent than specified). Unfortunately, in some cases, this is not possible after the bad response, but only before the next one. So, HttpClient must be able to skip those surplus lines this way.  Set this to `0` to disallow any garbage/empty lines before the status line. To specify no limit, use `Integer#MAX_VALUE`. | `<undefined>` |
| http.socket.timeout | Integer | Sets the socket timeout (`SO_TIMEOUT`) in milliseconds to be used when executing the method. A timeout value of zero is interpreted as an infinite timeout. | `<undefined>` |
| http.method.retry-handler | [HttpMethodRetryHandler](apidocs/org/apache/commons/httpclient/HttpMethodRetryHandler.html) | The method retry handler used for retrying failed methods. For details see the [Exception handling guide](exception-handling.html#Custom%20exception%20handler). | [default implementation](apidocs/org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html) |
| http.dateparser.patterns | [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link") | Date patterns used for parsing. The patterns are stored in a [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link") and must be compatible with [SimpleDateFormat](http://java.sun.com/j2se/1.4.2/docs/api/java/text/SimpleDateFormat.html "External Link"). | 'EEE, dd MMM yyyy HH:mm:ss zzz',  'EEEE, dd-MMM-yy HH:mm:ss zzz',  'EEE MMM d HH:mm:ss yyyy',  'EEE, dd-MMM-yyyy HH:mm:ss z',  'EEE, dd-MMM-yyyy HH-mm-ss z',  'EEE, dd MMM yy HH:mm:ss z',  'EEE dd-MMM-yyyy HH:mm:ss z',  'EEE dd MMM yyyy HH:mm:ss z',  'EEE dd-MMM-yyyy HH-mm-ss z',  'EEE dd-MMM-yy HH:mm:ss z',  'EEE dd MMM yy HH:mm:ss z',  'EEE,dd-MMM-yy HH:mm:ss z',  'EEE,dd-MMM-yyyy HH:mm:ss z',  'EEE, dd-MM-yyyy HH:mm:ss z' |
| http.method.response.buffer.warnlimit | Integer | The maximum buffered response size (in bytes) that triggers no warning. Buffered responses exceeding this size will trigger a warning in the log. If not set, the limit is 1 MB. | `<undefined>` |
| http.method.multipart.boundary | String | The multipart boundary string to use in conjunction with the [MultipartRequestEntity](apidocs/org/apache/commons/httpclient/params/MultipartRequestEntity.html). When not set a random value will be generated for each request. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

### HTTP connection parameters

Applicable at the following levels: **global** -> **client** -> **connection manager** ->
**connection**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.socket.timeout | Integer | The default socket timeout (`SO_TIMEOUT`) in milliseconds which is the timeout for waiting for data. A timeout value of zero is interpreted as an infinite timeout. This value is used when no socket timeout is set in the HTTP method parameters. | `<undefined>` |
| http.tcp.nodelay | Boolean | Determines whether Nagle's algorithm is to be used. The Nagle's algorithm tries to conserve bandwidth by minimizing the number of segments that are sent. When applications wish to decrease network latency and increase performance, they can disable Nagle's algorithm (by enabling `TCP_NODELAY`). Data will be sent earlier, at the cost of an increase in bandwidth consumption and number of packets. | `<undefined>` |
| http.socket.sendbuffer | Integer | The value to set on [Socket.setSendBufferSize(int)](http://java.sun.com/j2se/1.4.2/docs/api/java/net/Socket.html#setSendBufferSize(int) "External Link"). This value is a suggestion to the kernel from the application about the size of buffers to use for the data to be sent over the socket. | `<undefined>` |
| http.socket.receivebuffer | Integer | The value to set on [Socket.setReceiveBufferSize(int)](http://java.sun.com/j2se/1.4.2/docs/api/java/net/Socket.html#setReceiveBufferSize(int) "External Link"). This value is a suggestion to the kernel from the application about the size of buffers to use for the data to be received over the socket. | `<undefined>` |
| http.socket.linger | Integer | The linger time (`SO_LINGER`) in seconds. This option disables/enables immediate return from a close() of a TCP Socket. Enabling this option with a non-zero Integer timeout means that a close() will block pending the transmission and acknowledgement of all data written to the peer, at which point the socket is closed gracefully. Value `0` implies that the option is disabled. Value `-1` implies that the JRE default is used. | `<undefined>` |
| http.connection.timeout | Integer | The timeout until a connection is established. A value of zero means the timeout is not used. | `<undefined>` |
| http.connection.stalecheck | Boolean | Determines whether stale connection check is to be used. Disabling stale connection check may result in slight performance improvement at the risk of getting an I/O error when executing a request over a connection that has been closed at the server side. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

### HTTP connection manager parameters

Applicable at the following levels: **global** -> **client** -> **connection manager**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.connection-manager.max-per-host | [Map](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Map.html "External Link") | Defines the maximum number of connections allowed per host configuration. These values only apply to the number of connections from a particular instance of HttpConnectionManager.  This parameter expects a value of type [`Map`](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Map.html "External Link"). The value should map instances of [`HostConfiguration`](apidocs/org/apache/commons/httpclient/HostConfiguration.html) to [`Integer`](http://java.sun.com/j2se/1.4.2/docs/api/java/lang/Integer.html "External Link")s. The default value can be specified using [`ANY_HOST_CONFIGURATION`](apidocs/org/apache/commons/httpclient/HostConfiguration.html#ANY_HOST_CONFIGURATION). | `<undefined>` |
| http.connection-manager.max-total | Integer | Defines the maximum number of connections allowed overall. This value only applies to the number of connections from a particular instance of HttpConnectionManager. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

### Host configuration parameters

Applicable at the following levels: **global** -> **client** -> **host**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.default-headers | [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link") | The request headers to be sent per default with each request. This parameter expects a value of type [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link"). The collection is expected to contain [HTTP headers](apidocs/org/apache/commons/httpclient/Header.html) | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

### HTTP client parameters

Applicable at the following levels: **global** -> **client**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.connection-manager.timeout | Long | The timeout in milliseconds used when retrieving an HTTP connection from the HTTP connection manager. 0 means to wait indefinitely. | `<undefined>` |
| http.connection-manager.class | Class | The default HTTP connection manager class. | [`SimpleHttpConnectionManager`](apidocs/org/apache/commons/httpclient/SimpleHttpConnectionManager.html) class |
| http.authentication.preemptive | Boolean | Defines whether authentication should be attempted preemptively. See authentication guide. | `<undefined>` |
| http.protocol.reject-relative-redirect | Boolean | Defines whether relative redirects should be rejected. Although redirects are supposed to be absolute it is common internet practice to use relative URLs. | `<undefined>` |
| http.protocol.max-redirects | Integer | Defines the maximum number of redirects to be followed. The limit on number of redirects is intended to prevent infinite loops. | `<undefined>` |
| http.protocol.allow-circular-redirects | Boolean | Defines whether circular redirects (redirects to the same location) should be allowed. The HTTP spec is not sufficiently clear whether circular redirects are permitted, therefore optionally they can be enabled. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

---
## Downloads

You must define the `maven.xdoc.distributionUrl`property if you wish to generate the download report.

---
## Mailing Lists

These are the mailing lists that have been established for this project. For each list, there is a subscribe, unsubscribe, and an archive link.

| List Name | Subscribe | Unsubscribe | Post | Archive | Other Archives |
| --- | --- | --- | --- | --- | --- |
| HttpClient User List | [Subscribe](mailto:httpclient-users-subscribe@hc.apache.org) | [Unsubscribe](mailto:httpclient-users-unsubscribe@hc.apache.org) | Not Available | [Archive](http://mail-archives.apache.org/mod_mbox/hc-httpclient-users/ "External Link") |  |
| HttpComponents Developer List | [Subscribe](mailto:dev-subscribe@hc.apache.org) | [Unsubscribe](mailto:dev-unsubscribe@hc.apache.org) | Not Available | [Archive](http://mail-archives.apache.org/mod_mbox/hc-dev/ "External Link") |  |
| HttpComponents Commits List | [Subscribe](mailto:commits-subscribe@hc.apache.org) | [Unsubscribe](mailto:commits-unsubscribe@hc.apache.org) | Not Available | [Archive](http://mail-archives.apache.org/mod_mbox/hc-commits/ "External Link") |  |

---
## Rationale

HTTP is the main protocol used today on the internet. Although the JDK
includes basic support for building HTTP-aware client applications, it
doesn't provide the flexibility or ease of use needed for many projects.

A Commons package would give committers an opportunity to coordinate
their efforts to create and maintain a efficient, feature-rich package
under the ASF license.

## Scope of the Package

The package shall create and maintain a Java library implementing the client
side of the HTTP/1.1 protocol, as defined in RFC 2616 and RFC 2617.

The package should :

* Have an API which should be as simple to use as possible
* Be as easy to extend as possible
* Provide unconditional support for HTTP/1.1

The package is quite different from the HTTP client provided as part of the JDK
(java.net.HttpURLConnection), as it focuses on the HTTP methods being sent
(instead of making that transparent to the user), and generally allows more
interaction with the lower level connection. The JDK client is also not very
intuitive to use.

The package is used by the Slide project to build a WebDAV client
library supporting WebDAV level 2.

## Interaction With Other Packages

*HttpClient* relies on:

* Java Development Kit (Version 1.1 or later; 1.3 or later recommended)

## Initial Source of the Package

The initial codebase exists in the jakarta-slide cvs tree under the
org.apache.webdav.lib package. It would be moved to commons under
the http subdirectory.

The proposed package name for the new component is
org.apache.commons.httpclient.

## Required Jakarta-Commons Resources

* CVS Repository - New directory `httpclient` in the
  `jakarta-commons` CVS repository.
* Initial Committers - The list is provided below. Some of the proposed
  committers are not currently jakarta-commons committers, but are committers
  on the jakarta-slide project, and contributed to this component.
* Mailing List - Discussions will take place on the general
  *jakarta-commons@jakarta.apache.org* mailing list. To help list
  subscribers identify messages of interest, it is suggested that the
  message subject of messages about this component be prefixed with
  [httpclient].
* Bugzilla - New component "HttpClient" under the "Commons" product
  category, with appropriate version identifiers as needed.
* Jyve FAQ - New category "commons-httpclient" (when available).

## Initial Committers

The initial committers on the *HttpClient* component shall be:

* Remy Maucherat
* B.C.Holmes
* Sung-Gu Park
* Juergen Pill
* Costin Manolache

## Proposal ChangeLog

2002/07/19 - Replace uses of *HTTP Client* with *HttpClient*
for consistency.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpMethodRetryHandler.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpParser.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpMethodRetryHandler.html)    [**NO FRAMES**](HttpMethodRetryHandler.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Interface HttpMethodRetryHandler

**All Known Implementing Classes:**: [DefaultHttpMethodRetryHandler](../../../../org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html "class in org.apache.commons.httpclient")

---

``` public interface HttpMethodRetryHandler ```

A handler for determining if an HttpMethod should be retried after a
recoverable exception during execution.

Classes implementing this interface must synchronize access to shared
data as methods of this interfrace may be executed from multiple threads

**Author:**
:   Michael Becke, [Oleg Kalnichevski](mailto:oleg -at- ural.ru)

**See Also:**: [`HttpMethod.execute(HttpState, HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethod.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---

| **Method Summary** | |
| --- | --- |
| `boolean` | `retryMethod(HttpMethod method, IOException exception, int executionCount)`             Determines if a method should be retried after an HttpRecoverableException occurs during execution. |

| **Method Detail** |
| --- |

### retryMethod

```
boolean retryMethod(HttpMethod method,
                    IOException exception,
                    int executionCount)
```

:   Determines if a method should be retried after an HttpRecoverableException
    occurs during execution.

    :   **Parameters:**: `method` - the method being executed: `exception` - the exception that occurred: `executionCount` - the number of times this method has been unsuccessfully executed **Returns:**: `true` if the method should be retried, `false` otherwise



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpMethodRetryHandler.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpParser.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpMethodRetryHandler.html)    [**NO FRAMES**](HttpMethodRetryHandler.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
## Introduction

The delete method requests that the origin server delete the resource
identified by the request URL. This method *may* be overridden by
human intervention (or other means) on the origin server. The client
cannot be guaranteed that the operation has been carried out, even if the
status code returned from the origin server indicates that the action has
been completed successfully. However, the server *should not*
indicate success unless, at the time the response is given, it intends to
delete the resource or move it to an inaccessible location.

A successful response *should* be 200 (OK) if the response
includes a response body describing the status, 202 (Accepted) if the
action has not yet been enacted, or 204 (No Content) if the action has
been enacted but the response does not include a response body.

If the request passes through a cache and the URL identifies one or
more currently cached entities, those entries *should* be treated as
stale. Responses to this method are not cacheable.

## Typical Usage

The delete method is used by supplying a URL to delete the resource at
and reading the response from the server.

```
        DeleteMethod delete = new DeleteMethod("http://jakarata.apache.org");
        // execute the method and handle any error responses.
        ...
        // Ensure that if there is a response body it is read, then release the
        // connection.
        ...
        delete.releaseConnection();
```

## Common Problems

The DELETE method is not widely supported on public servres due to
security concerns and generally FTP is used to delete files on the
webserver. Before executing a DELETE method, it may be worth checking
that DELETE is supported using the [OPTIONS](options.html)
method.

## RFC Section

The delete method is defined in section 9.7 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

---
## Introduction

The PUT method requests that the enclosed entity be stored under the
supplied URL. If the URL refers to an already existing resource, the
enclosed entity *should* be considered as a modified version of the
one residing on the origin server. If the URL does not point to an
existing resource, and that URL is capable of being defined as a new
resource by the requesting user agent, the origin server can create the
resource with that URL.

If the request passes through a cache and the URL identifies one or
more currently cached entities, those entries *should* be treated as
stale. Responses to this method are not cacheable.

The fundamental difference between [POST](post.html) and
PUT requests is reflected in the different meaning of the request URL.
The URL in a POST request identifies the resource that will handle the
enclosed entity. That resource might be a data-accepting process, a
gateway to some other protocol, or a separate entity that accepts
annotations. In contrast, the URL in a PUT request identifies the entity
enclosed with the request -- the user agent knows what URL is intended
and the server **must not** attempt to apply the request to some other
resource.

Unless otherwise specified for a particular entity-header, the
entity-headers in the PUT request *should* be applied to the
resource created or modified by the PUT.

## Typical Usage

The put method is very simple, it takes a URL to put to and requires
that the body of the request method be set to the data to upload. The
body can be set with an input stream or a string.

```
        PutMethod put = new PutMethod("http://jakarta.apache.org");
        put.setRequestBody(new FileInputStream("UploadMe.gif"));
        // execute the method and handle any error responses.
        ...
        // Handle the response.  Note that a successful response may not be
        // 200, but may also be 201 Created, 204 No Content or any of the other
        // 2xx range responses.
```

## Common Problems

The PUT method is not widely supported on public servers due to
security concerns and generally FTP is used to upload new and modified
files to the webserver. Before executing a PUT method on a URL, it may
be worth checking that PUT is supported using the [OPTIONS](options.html) method.

## RFC Section

The put method is defined in section 9.6 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

---
## Introduction

The OPTIONS method represents a request for information about the
communication options available on the request/response chain identified
by the request URL. This method allows the client to determine the
options and/or requirements associated with a resource, or the
capabilities of a server, without implying a resource action or
initiating a resource retrieval.

## Typical Usage

Typically the options method is used to determine what methods are
supported by the server, and this is accomodated by the
`getAllowedMethods` function.

```
        OptionsMethod options = new OptionsMethod("http://jakarta.apache.org");
        // execute method and handle any error responses.
        ...
        Enumeration allowedMethods = options.getAllowedMethods();
        options.releaseConnection();
```

## Common Problems

None.

## RFC Section

The options method is defined in section 9.2 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

---
## Introduction

The multipart post method is a different request body format for a
[POST](post.html) method. The media-type multipart/form-data
follows the rules of all multipart MIME data streams as outlined in RFC
1521. It is intended for use in returning the data that comes about from
filling out a form, particularly when the form requires binary data to
be uploaded such as the contents of a file.

## Typical Usage

Like for the standard POST method, there are two main steps to using
the multipart post method, setting the request data and retrieving the
response data.

The request data is specified by adding parameters to the method,
these are defined by the
`org.apache.commons.httpclient.methods.multipart.Part` class
and it's various subclasses. A description of each of these is below.

| Part | Description |
| --- | --- |
| StringPart | The string part is a simple part that takes a name for the part and the value of the part as a string. This is typically used for standard form elements such as a text area within a multipart form. |
| FilePart | The file part is actually a very generic type of part that can contain any type of data and specify a name, content type and charset for the data. In it's simplest form, it takes just a name and a File object and uploads the contents of the file, however it can also be passed a `PartSource` object to upload. See the part source section below for more information. |

### Part Sources

The `PartSource` interface provides a generic container
for providing data to the FilePart class. There are two concrete
implementations of PartSource provided with HttpClient (described
below) but you can also provide your own implementation easily. The
input for the multipart post could come from anywhere, perhaps it's
being received from another server or process, and all that the
PartSource class needs to be able to do is provide the length of the
data that will be provided, an input stream to retrieve the data from
and a file name (or some name identifying the data).

The two concrete implementations of PartSource are FilePartSource
and ByteArrayPartSource. FilePartSource simply takes a File to upload
whereas ByteArrayPartSource allows for the case where the data has been
cached in memory and takes a file name and a byte array to upload.

## Common Problems

The most common problem people run into with multipart uploads is that
the length of the data must be known before hand. If the length of the
data can not be determined in advance, it needs to be cached either in
memory or to a file and then uploaded using either ByteArrayPartSource or
FilePartSource. The HTTP specification does not allow for POST data to
be of an unknown length.

## RFC Section

The multipart form data uses the POST method from the HTTP standard
which is defined in section 8.3 of [RFC1945](http://www.ietf.org/rfc//rfc1945.txt "External Link") and similarly
redefined for HTTP 1.1 in section 9.5 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

The multipart/form-data MIME type used to format the body of the
request is defined in [RFC1867](http://www.ietf.org/rfc/rfc1867.txt "External Link").

---
## Introduction

The HEAD method is identical to the [GET](get.html) method
except that the server *must not* return a message-body in the
response. The metainformation contained in the HTTP headers in response
to a HEAD request *should* be identical to the information sent in
response to a GET request. This allows a client to obtain
meta-information about a resource without actually transferring the
resource itself.

The head method is often used for testing hyperlinks, accessibility
and for determining if a document has been recently modifed.

When your program is implementing caching, it is important to note
that if the HEAD response indicates that the cached entity differs from
the current entity, such as by a change in the Content-Length,
Content-MD5, ETag or Last-Modified, the cache **must** treat the
cached entry as stale.

## Typical Usage

Typically the head method is used to retrieve the meta-information for
a resource, perhaps to check if the resource has been modifed. There are
no methods specific to HeadMethod as the headers can be retreived using
`getResponseHeaders()` as with any other method.

```
        HeadMethod head = new HeadMethod("http://jakarta.apache.org");
        // execute the method and handle any error responses.
        ...
        // Retrieve all the headers.
        Header[] headers = head.getResponseHeaders();

        // Retrieve just the last modified header value.
        String lastModified =
            head.getResponseHeader("last-modified").getValue();
```

## Common Problems

None.

## RFC Section

The head method is defined in section 8.2 of [RFC1945](http://www.ietf.org/rfc/rfc1945.txt "External Link") and similarly
redefined for HTTP 1.1 in section 9.4 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

---
## Introduction

The GET method retrieves whatever information (in the form of an
entity) is identified by the Request-URI. If the Request-URI refers to a
data-producing process, it is the produced data which shall be returned
as the entity in the response and not the source text of the process,
unless that text happens to be the output of the process.

The semantics of the GET method change to a "conditional GET" if the
request message includes an If-ModifiedSince, If-Unmodified-Since,
If-Match, If-None-Match, or If-Range header field. A conditional GET
method requests that the entity be transferred only under the
circumstances described by the conditional header field(s). This reduces
unnecessary network usage by allowing cached entities to be refreshed
without requiring multiple requests or transferring data already held by
the client.

If a Range header field is included, the request is for only the part
of the entity specified by the range header. This allows partially
retrieved entities to be completed without transferring previously
received data.

## Typical Usage

Typically the get method is used to download a document from a web
server. This can be achieved with the method, getResponseBody,
getResponseBodyAsStream or getResponseBodyAsString. Of these methods,
getResponseBodyAsStream is generally the best choice as it avoids
unnessecary buffering of all data into memory before processing.

See the [tutorial](../tutorial.html) for a full example
of using the GET method. There are also a number of examples in the [sample
code](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link").

```
        GetMethod get = new GetMethod("http://httpcomponents.apache.org");
        // execute method and handle any error responses.
        ...
        InputStream in = get.getResponseBodyAsStream();
        // Process the data from the input stream.
        get.releaseConnection();
```

## Common Problems

The most common mistake when using the GET method is failing to read
the entire response body even if an error code, redirect or any other
response status is received. As with all methods, one must also be sure to call
method.releaseConnection(), regardless of the response code received.

## RFC Section

The get method is defined in section 8.1 of [RFC1945](http://www.ietf.org/rfc/rfc1945.txt "External Link") and similarly
defined for HTTP 1.1 in section 9.3 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

---
## Introduction

The post method is used to request that the origin server accept the
entity enclosed in the request as a new subordinate of the resource
identified by the Request-URI in the Request-Line. Essentially this
means that the POST data will be stored by the server and usually will be
processed by a server side application.

Post is designed to allow a uniform method to cover the following
functions:

* Annotation of existing resources.
* Posting a message to a bulletin board, newsgroup, mailing list, or
  similar group of articles.
* Providing a block of data, such as the result of submitting a form,
  to a data-handling process.
* Extending a database through an append operation.

It is generally expected that a POST request will have some side
effect on the server such as writing to a database, and the HTTP
specification suggests that user agents represent user actions which
result in a POST request in a special way, so that the user is made aware
of the fact that a possibly unsafe action is being requested. This
however, is not a requirement.

## Typical Usage

There are two major steps to using the POST method, firstly providing
the data for the request and secondly reading the response from the
server.

The request data is supplied by one of the variants of
`setRequestBody` which can either take an
`InputStream` an array of `NameValuePair` objects
or a `String`. The simplest form is to pass in a
NameValuePair and allow HttpClient to format the request body according
to the standard, however this requires that the full content be stored in
memory which may not be desireable. In this case, passing in an
InputStream would be more appropriate.

The POST response body can be read using any of the `getResponseBody*`
methods much like the [GET](get.html) method.

```
        PostMethod post = new PostMethod("http://jakarata.apache.org/");
        NameValuePair[] data = {
          new NameValuePair("user", "joe"),
          new NameValuePair("password", "bloggs")
        };
        post.setRequestBody(data);
        // execute method and handle any error responses.
        ...
        InputStream in = post.getResponseBodyAsStream();
        // handle response.
```

## Common Problems

The most common problem when using the post method is not reading the
entire response body and calling releaseConnection regardless of the
response received from the server or whether or not the response body is
useful to your application.

## RFC Section

The post method is defined in section 8.3 of [RFC1945](http://www.ietf.org/rfc/rfc1945.txt "External Link") and similarly
redefined for HTTP 1.1 in section 9.5 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

---
## Introduction

The TRACE method is primarily used for debugging and testing purposes,
and simply requests that the server echo back the request it received.
This can be useful for identifying any changes to the request that is
made by proxies.

The TRACE method is used to invoke a remote, application-layer
loop-back of the request message. The final recipient of the request
*should* reflect the message received back to the client as the
entity-body of a 200 (OK) response. The final recipient is either the
origin server or the first proxy or gateway to receive a max-Forwards
value of zero (0) in the request (see section 14.31 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link")).

## Typical Usage

The trace method simply requires providing a URL and reading the
response received. Additional headers can be added with the
`addRequestHeader` method as with any other HttpMethod.

```
        TraceMethod trace = new TraceMethod("http://jakarata.apache.org");
        // Execute the method and handle any errors.
        ...
        // Read the response body.
        String request = trace.getResponseBodyAsString();
        trace.releaseConnection();
```

## Common Problems

None.

## RFC Section

The trace method is defined in section 9.6 of [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link").

---
HttpClient 3.1 API








## Frame Alert

This document is designed to be viewed using the frames feature. If you see this message, you are using a non-frame-capable web client.
  
Link to[Non-frame version.](overview-summary.html)

---
## Dependencies

The following is a list of dependencies for this project. These dependencies are required to compile and run the application:

| Artifact ID | Type | Version | Scope | URL | Comment |
| --- | --- | --- | --- | --- | --- |
| commons-codec | jar | 1.2 |  | [http://commons.apache.org/codec/](http://commons.apache.org/codec/ "External Link") |  |
| commons-logging | jar | 1.0.4 |  | [http://commons.apache.org/logging/](http://commons.apache.org/logging/ "External Link") |  |
| junit | jar | 3.8.1 | test | [http://www.junit.org/](http://www.junit.org/ "External Link") |  |

---
## Metric Results

[
[summary](#Summary)] [
[packages](#Packages)] [
[cycles](#Cycles)] [
[explanations](#Explanations)]

The following document contains the results of a
[JDepend](http://www.clarkware.com/software/JDepend.html "External Link")metric analysis. The various metrics are defined at the bottom of this document.

## Summary

[
[summary](#Summary)] [
[packages](#Packages)] [
[cycles](#Cycles)] [
[explanations](#Explanations)]

| Package | TC | AC | CC | AC | EC | A | I | D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.httpclient](#org_apache_commons_httpclient) | 68 | 7 | 61 | 6 | 15 | 0,1 | 71% | 18% |
| [org.apache.commons.httpclient.auth](#org_apache_commons_httpclient_auth) | 20 | 5 | 15 | 1 | 10 | 0,25 | 91% | 16% |
| [org.apache.commons.httpclient.cookie](#org_apache_commons_httpclient_cookie) | 23 | 4 | 19 | 1 | 6 | 0,17 | 86% | 3% |
| [org.apache.commons.httpclient.methods](#org_apache_commons_httpclient_methods) | 15 | 3 | 12 | 1 | 8 | 0,2 | 89% | 9% |
| [org.apache.commons.httpclient.methods.multipart](#org_apache_commons_httpclient_methods_multipart) | 8 | 3 | 5 | 1 | 7 | 0,38 | 88% | 25% |
| [org.apache.commons.httpclient.params](#org_apache_commons_httpclient_params) | 9 | 2 | 7 | 5 | 5 | 0,22 | 50% | 28% |
| [org.apache.commons.httpclient.protocol](#org_apache_commons_httpclient_protocol) | 9 | 3 | 6 | 1 | 10 | 0,33 | 91% | 24% |
| [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) | 15 | 0 | 15 | 6 | 11 | 0 | 65% | 35% |

## Packages

[
[summary](#Summary)] [
[packages](#Packages)] [
[cycles](#Cycles)] [
[explanations](#Explanations)]

### org.apache.commons.httpclient

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 6 | 15 | 10% | 71% | 18% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| * [Credentials](xref/org/apache/commons/httpclient/Credentials.html) * [HttpConnectionManager](xref/org/apache/commons/httpclient/HttpConnectionManager.html) * [HttpMethod](xref/org/apache/commons/httpclient/HttpMethod.html) * [HttpMethodBase](xref/org/apache/commons/httpclient/HttpMethodBase.html) * [HttpMethodRetryHandler](xref/org/apache/commons/httpclient/HttpMethodRetryHandler.html) * [MethodRetryHandler](xref/org/apache/commons/httpclient/MethodRetryHandler.html) * [ResponseConsumedWatcher](xref/org/apache/commons/httpclient/ResponseConsumedWatcher.html) | * [AutoCloseInputStream](xref/org/apache/commons/httpclient/AutoCloseInputStream.html) * [ChunkedInputStream](xref/org/apache/commons/httpclient/ChunkedInputStream.html) * [ChunkedOutputStream](xref/org/apache/commons/httpclient/ChunkedOutputStream.html) * [CircularRedirectException](xref/org/apache/commons/httpclient/CircularRedirectException.html) * [ConnectMethod](xref/org/apache/commons/httpclient/ConnectMethod.html) * [ConnectTimeoutException](xref/org/apache/commons/httpclient/ConnectTimeoutException.html) * [ConnectionPoolTimeoutException](xref/org/apache/commons/httpclient/ConnectionPoolTimeoutException.html) * [ContentLengthInputStream](xref/org/apache/commons/httpclient/ContentLengthInputStream.html) * [Cookie](xref/org/apache/commons/httpclient/Cookie.html) * [DefaultHttpMethodRetryHandler](xref/org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html) * [DefaultMethodRetryHandler](xref/org/apache/commons/httpclient/DefaultMethodRetryHandler.html) * [Header](xref/org/apache/commons/httpclient/Header.html) * [HeaderElement](xref/org/apache/commons/httpclient/HeaderElement.html) * [HeaderGroup](xref/org/apache/commons/httpclient/HeaderGroup.html) * [HostConfiguration](xref/org/apache/commons/httpclient/HostConfiguration.html) * [HttpClient](xref/org/apache/commons/httpclient/HttpClient.html) * [HttpClientError](xref/org/apache/commons/httpclient/HttpClientError.html) * [HttpConnection](xref/org/apache/commons/httpclient/HttpConnection.html) * [HttpConstants](xref/org/apache/commons/httpclient/HttpConstants.html) * [HttpContentTooLargeException](xref/org/apache/commons/httpclient/HttpContentTooLargeException.html) * [HttpException](xref/org/apache/commons/httpclient/HttpException.html) * [HttpHost](xref/org/apache/commons/httpclient/HttpHost.html) * [HttpMethodBase$1](xref/org/apache/commons/httpclient/HttpMethodBase.html) * [HttpMethodDirector](xref/org/apache/commons/httpclient/HttpMethodDirector.html) * [HttpParser](xref/org/apache/commons/httpclient/HttpParser.html) * [HttpRecoverableException](xref/org/apache/commons/httpclient/HttpRecoverableException.html) * [HttpState](xref/org/apache/commons/httpclient/HttpState.html) * [HttpStatus](xref/org/apache/commons/httpclient/HttpStatus.html) * [HttpURL](xref/org/apache/commons/httpclient/HttpURL.html) * [HttpVersion](xref/org/apache/commons/httpclient/HttpVersion.html) * [HttpsURL](xref/org/apache/commons/httpclient/HttpsURL.html) * [InvalidRedirectLocationException](xref/org/apache/commons/httpclient/InvalidRedirectLocationException.html) * [MultiThreadedHttpConnectionManager](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$1](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$ConnectionPool](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$ConnectionSource](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$HostConnectionPool](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$HttpConnectionAdapter](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$HttpConnectionWithReference](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$ReferenceQueueThread](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [MultiThreadedHttpConnectionManager$WaitingThread](xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html) * [NTCredentials](xref/org/apache/commons/httpclient/NTCredentials.html) * [NameValuePair](xref/org/apache/commons/httpclient/NameValuePair.html) * [NoHttpResponseException](xref/org/apache/commons/httpclient/NoHttpResponseException.html) * [ProtocolException](xref/org/apache/commons/httpclient/ProtocolException.html) * [ProxyClient](xref/org/apache/commons/httpclient/ProxyClient.html) * [ProxyClient$1](xref/org/apache/commons/httpclient/ProxyClient.html) * [ProxyClient$ConnectResponse](xref/org/apache/commons/httpclient/ProxyClient.html) * [ProxyClient$DummyConnectionManager](xref/org/apache/commons/httpclient/ProxyClient.html) * [ProxyHost](xref/org/apache/commons/httpclient/ProxyHost.html) * [RedirectException](xref/org/apache/commons/httpclient/RedirectException.html) * [SimpleHttpConnectionManager](xref/org/apache/commons/httpclient/SimpleHttpConnectionManager.html) * [StatusLine](xref/org/apache/commons/httpclient/StatusLine.html) * [URI](xref/org/apache/commons/httpclient/URI.html) * [URI$DefaultCharsetChanged](xref/org/apache/commons/httpclient/URI.html) * [URI$LocaleToCharsetMap](xref/org/apache/commons/httpclient/URI.html) * [URIException](xref/org/apache/commons/httpclient/URIException.html) * [UsernamePasswordCredentials](xref/org/apache/commons/httpclient/UsernamePasswordCredentials.html) * [Wire](xref/org/apache/commons/httpclient/Wire.html) * [WireLogInputStream](xref/org/apache/commons/httpclient/WireLogInputStream.html) * [WireLogOutputStream](xref/org/apache/commons/httpclient/WireLogOutputStream.html) | * [org.apache.commons.httpclient.auth](#org_apache_commons_httpclient_auth) * [org.apache.commons.httpclient.cookie](#org_apache_commons_httpclient_cookie) * [org.apache.commons.httpclient.methods](#org_apache_commons_httpclient_methods) * [org.apache.commons.httpclient.params](#org_apache_commons_httpclient_params) * [org.apache.commons.httpclient.protocol](#org_apache_commons_httpclient_protocol) * [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) | * [java.io](#java_io) * [java.lang](#java_lang) * [java.lang.ref](#java_lang_ref) * [java.lang.reflect](#java_lang_reflect) * [java.net](#java_net) * [java.security](#java_security) * [java.util](#java_util) * [org.apache.commons.codec](#org_apache_commons_codec) * [org.apache.commons.codec.net](#org_apache_commons_codec_net) * [org.apache.commons.httpclient.auth](#org_apache_commons_httpclient_auth) * [org.apache.commons.httpclient.cookie](#org_apache_commons_httpclient_cookie) * [org.apache.commons.httpclient.params](#org_apache_commons_httpclient_params) * [org.apache.commons.httpclient.protocol](#org_apache_commons_httpclient_protocol) * [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) * [org.apache.commons.logging](#org_apache_commons_logging) |

### org.apache.commons.httpclient.auth

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 10 | 25% | 91% | 16% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| * [AuthPolicy](xref/org/apache/commons/httpclient/auth/AuthPolicy.html) * [AuthScheme](xref/org/apache/commons/httpclient/auth/AuthScheme.html) * [AuthSchemeBase](xref/org/apache/commons/httpclient/auth/AuthSchemeBase.html) * [CredentialsProvider](xref/org/apache/commons/httpclient/auth/CredentialsProvider.html) * [RFC2617Scheme](xref/org/apache/commons/httpclient/auth/RFC2617Scheme.html) | * [AuthChallengeException](xref/org/apache/commons/httpclient/auth/AuthChallengeException.html) * [AuthChallengeParser](xref/org/apache/commons/httpclient/auth/AuthChallengeParser.html) * [AuthChallengeProcessor](xref/org/apache/commons/httpclient/auth/AuthChallengeProcessor.html) * [AuthScope](xref/org/apache/commons/httpclient/auth/AuthScope.html) * [AuthState](xref/org/apache/commons/httpclient/auth/AuthState.html) * [AuthenticationException](xref/org/apache/commons/httpclient/auth/AuthenticationException.html) * [BasicScheme](xref/org/apache/commons/httpclient/auth/BasicScheme.html) * [CredentialsNotAvailableException](xref/org/apache/commons/httpclient/auth/CredentialsNotAvailableException.html) * [DigestScheme](xref/org/apache/commons/httpclient/auth/DigestScheme.html) * [HttpAuthRealm](xref/org/apache/commons/httpclient/auth/HttpAuthRealm.html) * [HttpAuthenticator](xref/org/apache/commons/httpclient/auth/HttpAuthenticator.html) * [InvalidCredentialsException](xref/org/apache/commons/httpclient/auth/InvalidCredentialsException.html) * [MalformedChallengeException](xref/org/apache/commons/httpclient/auth/MalformedChallengeException.html) * [NTLM](xref/org/apache/commons/httpclient/auth/NTLM.html) * [NTLMScheme](xref/org/apache/commons/httpclient/auth/NTLMScheme.html) | * [org.apache.commons.httpclient](#org_apache_commons_httpclient) | * [java.lang](#java_lang) * [java.security](#java_security) * [java.util](#java_util) * [javax.crypto](#javax_crypto) * [javax.crypto.spec](#javax_crypto_spec) * [org.apache.commons.codec.binary](#org_apache_commons_codec_binary) * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.httpclient.params](#org_apache_commons_httpclient_params) * [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) * [org.apache.commons.logging](#org_apache_commons_logging) |

### org.apache.commons.httpclient.cookie

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 6 | 17% | 86% | 3% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| * [CookieAttributeHandler](xref/org/apache/commons/httpclient/cookie/CookieAttributeHandler.html) * [CookiePolicy](xref/org/apache/commons/httpclient/cookie/CookiePolicy.html) * [CookieSpec](xref/org/apache/commons/httpclient/cookie/CookieSpec.html) * [CookieVersionSupport](xref/org/apache/commons/httpclient/cookie/CookieVersionSupport.html) | * [Cookie2](xref/org/apache/commons/httpclient/cookie/Cookie2.html) * [CookieOrigin](xref/org/apache/commons/httpclient/cookie/CookieOrigin.html) * [CookiePathComparator](xref/org/apache/commons/httpclient/cookie/CookiePathComparator.html) * [CookieSpecBase](xref/org/apache/commons/httpclient/cookie/CookieSpecBase.html) * [IgnoreCookiesSpec](xref/org/apache/commons/httpclient/cookie/IgnoreCookiesSpec.html) * [MalformedCookieException](xref/org/apache/commons/httpclient/cookie/MalformedCookieException.html) * [NetscapeDraftSpec](xref/org/apache/commons/httpclient/cookie/NetscapeDraftSpec.html) * [RFC2109Spec](xref/org/apache/commons/httpclient/cookie/RFC2109Spec.html) * [RFC2965Spec](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$1](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$Cookie2DomainAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$Cookie2MaxageAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$Cookie2PathAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$Cookie2PortAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$Cookie2VersionAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$CookieCommentAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$CookieCommentUrlAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$CookieDiscardAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) * [RFC2965Spec$CookieSecureAttributeHandler](xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html) | * [org.apache.commons.httpclient](#org_apache_commons_httpclient) | * [java.lang](#java_lang) * [java.text](#java_text) * [java.util](#java_util) * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) * [org.apache.commons.logging](#org_apache_commons_logging) |

### org.apache.commons.httpclient.methods

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 8 | 20% | 89% | 9% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| * [EntityEnclosingMethod](xref/org/apache/commons/httpclient/methods/EntityEnclosingMethod.html) * [ExpectContinueMethod](xref/org/apache/commons/httpclient/methods/ExpectContinueMethod.html) * [RequestEntity](xref/org/apache/commons/httpclient/methods/RequestEntity.html) | * [ByteArrayRequestEntity](xref/org/apache/commons/httpclient/methods/ByteArrayRequestEntity.html) * [DeleteMethod](xref/org/apache/commons/httpclient/methods/DeleteMethod.html) * [FileRequestEntity](xref/org/apache/commons/httpclient/methods/FileRequestEntity.html) * [GetMethod](xref/org/apache/commons/httpclient/methods/GetMethod.html) * [HeadMethod](xref/org/apache/commons/httpclient/methods/HeadMethod.html) * [InputStreamRequestEntity](xref/org/apache/commons/httpclient/methods/InputStreamRequestEntity.html) * [MultipartPostMethod](xref/org/apache/commons/httpclient/methods/MultipartPostMethod.html) * [OptionsMethod](xref/org/apache/commons/httpclient/methods/OptionsMethod.html) * [PostMethod](xref/org/apache/commons/httpclient/methods/PostMethod.html) * [PutMethod](xref/org/apache/commons/httpclient/methods/PutMethod.html) * [StringRequestEntity](xref/org/apache/commons/httpclient/methods/StringRequestEntity.html) * [TraceMethod](xref/org/apache/commons/httpclient/methods/TraceMethod.html) | * [org.apache.commons.httpclient.methods.multipart](#org_apache_commons_httpclient_methods_multipart) | * [java.io](#java_io) * [java.lang](#java_lang) * [java.util](#java_util) * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.httpclient.methods.multipart](#org_apache_commons_httpclient_methods_multipart) * [org.apache.commons.httpclient.params](#org_apache_commons_httpclient_params) * [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) * [org.apache.commons.logging](#org_apache_commons_logging) |

### org.apache.commons.httpclient.methods.multipart

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 7 | 38% | 88% | 25% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| * [Part](xref/org/apache/commons/httpclient/methods/multipart/Part.html) * [PartBase](xref/org/apache/commons/httpclient/methods/multipart/PartBase.html) * [PartSource](xref/org/apache/commons/httpclient/methods/multipart/PartSource.html) | * [ByteArrayPartSource](xref/org/apache/commons/httpclient/methods/multipart/ByteArrayPartSource.html) * [FilePart](xref/org/apache/commons/httpclient/methods/multipart/FilePart.html) * [FilePartSource](xref/org/apache/commons/httpclient/methods/multipart/FilePartSource.html) * [MultipartRequestEntity](xref/org/apache/commons/httpclient/methods/multipart/MultipartRequestEntity.html) * [StringPart](xref/org/apache/commons/httpclient/methods/multipart/StringPart.html) | * [org.apache.commons.httpclient.methods](#org_apache_commons_httpclient_methods) | * [java.io](#java_io) * [java.lang](#java_lang) * [java.util](#java_util) * [org.apache.commons.httpclient.methods](#org_apache_commons_httpclient_methods) * [org.apache.commons.httpclient.params](#org_apache_commons_httpclient_params) * [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) * [org.apache.commons.logging](#org_apache_commons_logging) |

### org.apache.commons.httpclient.params

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 5 | 5 | 22% | 50% | 28% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| * [HttpParams](xref/org/apache/commons/httpclient/params/HttpParams.html) * [HttpParamsFactory](xref/org/apache/commons/httpclient/params/HttpParamsFactory.html) | * [DefaultHttpParams](xref/org/apache/commons/httpclient/params/DefaultHttpParams.html) * [DefaultHttpParamsFactory](xref/org/apache/commons/httpclient/params/DefaultHttpParamsFactory.html) * [HostParams](xref/org/apache/commons/httpclient/params/HostParams.html) * [HttpClientParams](xref/org/apache/commons/httpclient/params/HttpClientParams.html) * [HttpConnectionManagerParams](xref/org/apache/commons/httpclient/params/HttpConnectionManagerParams.html) * [HttpConnectionParams](xref/org/apache/commons/httpclient/params/HttpConnectionParams.html) * [HttpMethodParams](xref/org/apache/commons/httpclient/params/HttpMethodParams.html) | * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.httpclient.auth](#org_apache_commons_httpclient_auth) * [org.apache.commons.httpclient.methods](#org_apache_commons_httpclient_methods) * [org.apache.commons.httpclient.methods.multipart](#org_apache_commons_httpclient_methods_multipart) * [org.apache.commons.httpclient.protocol](#org_apache_commons_httpclient_protocol) | * [java.io](#java_io) * [java.lang](#java_lang) * [java.util](#java_util) * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.logging](#org_apache_commons_logging) |

### org.apache.commons.httpclient.protocol

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 10 | 33% | 91% | 24% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| * [ControllerThreadSocketFactory$SocketTask](xref/org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.html) * [ProtocolSocketFactory](xref/org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html) * [SecureProtocolSocketFactory](xref/org/apache/commons/httpclient/protocol/SecureProtocolSocketFactory.html) | * [ControllerThreadSocketFactory](xref/org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.html) * [ControllerThreadSocketFactory$1](xref/org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.html) * [DefaultProtocolSocketFactory](xref/org/apache/commons/httpclient/protocol/DefaultProtocolSocketFactory.html) * [Protocol](xref/org/apache/commons/httpclient/protocol/Protocol.html) * [ReflectionSocketFactory](xref/org/apache/commons/httpclient/protocol/ReflectionSocketFactory.html) * [SSLProtocolSocketFactory](xref/org/apache/commons/httpclient/protocol/SSLProtocolSocketFactory.html) | * [org.apache.commons.httpclient](#org_apache_commons_httpclient) | * [java.io](#java_io) * [java.lang](#java_lang) * [java.lang.reflect](#java_lang_reflect) * [java.net](#java_net) * [java.util](#java_util) * [javax.net](#javax_net) * [javax.net.ssl](#javax_net_ssl) * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.httpclient.params](#org_apache_commons_httpclient_params) * [org.apache.commons.httpclient.util](#org_apache_commons_httpclient_util) |

### org.apache.commons.httpclient.util

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 6 | 11 | 0% | 65% | 35% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| *None* | * [DateParseException](xref/org/apache/commons/httpclient/util/DateParseException.html) * [DateParser](xref/org/apache/commons/httpclient/util/DateParser.html) * [DateUtil](xref/org/apache/commons/httpclient/util/DateUtil.html) * [EncodingUtil](xref/org/apache/commons/httpclient/util/EncodingUtil.html) * [ExceptionUtil](xref/org/apache/commons/httpclient/util/ExceptionUtil.html) * [HttpURLConnection](xref/org/apache/commons/httpclient/util/HttpURLConnection.html) * [IdleConnectionHandler](xref/org/apache/commons/httpclient/util/IdleConnectionHandler.html) * [IdleConnectionTimeoutThread](xref/org/apache/commons/httpclient/util/IdleConnectionTimeoutThread.html) * [LangUtils](xref/org/apache/commons/httpclient/util/LangUtils.html) * [ParameterFormatter](xref/org/apache/commons/httpclient/util/ParameterFormatter.html) * [ParameterParser](xref/org/apache/commons/httpclient/util/ParameterParser.html) * [TimeoutController](xref/org/apache/commons/httpclient/util/TimeoutController.html) * [TimeoutController$TimeoutException](xref/org/apache/commons/httpclient/util/TimeoutController.html) * [URIUtil](xref/org/apache/commons/httpclient/util/URIUtil.html) * [URIUtil$Coder](xref/org/apache/commons/httpclient/util/URIUtil.html) | * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.httpclient.auth](#org_apache_commons_httpclient_auth) * [org.apache.commons.httpclient.cookie](#org_apache_commons_httpclient_cookie) * [org.apache.commons.httpclient.methods](#org_apache_commons_httpclient_methods) * [org.apache.commons.httpclient.methods.multipart](#org_apache_commons_httpclient_methods_multipart) * [org.apache.commons.httpclient.protocol](#org_apache_commons_httpclient_protocol) | * [java.io](#java_io) * [java.lang](#java_lang) * [java.lang.reflect](#java_lang_reflect) * [java.net](#java_net) * [java.security](#java_security) * [java.text](#java_text) * [java.util](#java_util) * [org.apache.commons.codec](#org_apache_commons_codec) * [org.apache.commons.codec.net](#org_apache_commons_codec_net) * [org.apache.commons.httpclient](#org_apache_commons_httpclient) * [org.apache.commons.logging](#org_apache_commons_logging) |

## Cycles

[
[summary](#Summary)] [
[packages](#Packages)] [
[cycles](#Cycles)] [
[explanations](#Explanations)]

| Package | Cyclic Dependencies |
| --- | --- |
| org.apache.commons.httpclient | * org.apache.commons.httpclient.util * org.apache.commons.httpclient |
| org.apache.commons.httpclient.auth | * org.apache.commons.httpclient * org.apache.commons.httpclient.util * org.apache.commons.httpclient |
| org.apache.commons.httpclient.cookie | * org.apache.commons.httpclient * org.apache.commons.httpclient.util * org.apache.commons.httpclient |
| org.apache.commons.httpclient.methods | * org.apache.commons.httpclient * org.apache.commons.httpclient.util * org.apache.commons.httpclient |
| org.apache.commons.httpclient.methods.multipart | * org.apache.commons.httpclient.util * org.apache.commons.httpclient * org.apache.commons.httpclient.util |
| org.apache.commons.httpclient.params | * org.apache.commons.httpclient * org.apache.commons.httpclient.util * org.apache.commons.httpclient |
| org.apache.commons.httpclient.protocol | * org.apache.commons.httpclient.util * org.apache.commons.httpclient * org.apache.commons.httpclient.util |
| org.apache.commons.httpclient.util | * org.apache.commons.httpclient * org.apache.commons.httpclient.util |

## Explanations

[
[summary](#Summary)] [
[packages](#Packages)] [
[cycles](#Cycles)] [
[explanations](#Explanations)]

The following explanations are for quick reference and are lifted directly from the original
[JDepend documentation](http://www.clarkware.com/software/JDepend.html "External Link").

| Term | Description |
| --- | --- |
| Number of Classes | The number of concrete and abstract classes (and interfaces) in the package is an indicator of the extensibility of the package. |
| Afferent Couplings | The number of other packages that depend upon classes within the package is an indicator of the package's responsibility. |
| Efferent Couplings | The number of other packages that the classes in the package depend upon is an indicator of the package's independence. |
| Abstractness | The ratio of the number of abstract classes (and interfaces) in the analyzed package to the total number of classes in the analyzed package. The range for this metric is 0 to 1, with A=0 indicating a completely concrete package and A=1 indicating a completely abstract package. |
| Instability | The ratio of efferent coupling (Ce) to total coupling (Ce / (Ce + Ca)). This metric is an indicator of the package's resilience to change. The range for this metric is 0 to 1, with I=0 indicating a completely stable package and I=1 indicating a completely instable package. |
| Distance | The perpendicular distance of a package from the idealized line A + I = 1. This metric is an indicator of the package's balance between abstractness and stability. A package squarely on the main sequence is optimally balanced with respect to its abstractness and stability. Ideal packages are either completely abstract and stable (x=0, y=1) or completely concrete and instable (x=1, y=0). The range for this metric is 0 to 1, with D=0 indicating a package that is coincident with the main sequence and D=1 indicating a package that is as far from the main sequence as possible. |
| Cycles | Packages participating in a package dependency cycle are in a deadly embrace with respect to reusability and their release cycle. Package dependency cycles can be easily identified by reviewing the textual reports of dependency cycles. Once these dependency cycles have been identified with JDepend, they can be broken by employing various object-oriented techniques. |

---
## JavaDoc Warnings

The following document contains JavaDoc warnings.

## Summary

| Files | Errors |
| --- | --- |
| 0 | 0 |

## Files

| Files | Errors |
| --- | --- |

---
## Project License

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS
```

---
## Summary

[
[summary](#Summary)] [
[package list](#Package_List)] [
[test cases](#Test_Cases)]

| Tests | Errors | Failures | Success rate | Time(s) |
| --- | --- | --- | --- | --- |
| 591 | 0 | 0 | 100,00% | 31,48 |

Note:
*failures*are anticipated and checked for with assertions while
*errors*are unanticipated.

## Package List

[
[summary](#Summary)] [
[package list](#Package_List)] [
[test cases](#Test_Cases)]

| Package | Tests | Errors | Failures | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| [org.apache.commons.httpclient](#org_apache_commons_httpclient) | 591 | 0 | 0 | 100,00% | 31,48 |

Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.

### org.apache.commons.httpclient

| Class | | Tests | Errors | Failures | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- |
| Success | [TestAll](#TestAll) | 591 | 0 | 0 | 100,00% | 31,481 |

## Test Cases

[
[summary](#Summary)] [
[package list](#Package_List)] [
[test cases](#Test_Cases)]

### TestAll

|  |  |  |
| --- | --- | --- |
| Success | testHttpMethodBasePaths | 0,04 |
| Success | testHttpMethodBaseDefaultPath | 0,00 |
| Success | testHttpMethodBasePathConstructor | 0,01 |
| Success | testHttpMethodBaseTEandCL | 0,05 |
| Success | testConnectionAutoClose | 0,01 |
| Success | testSetGetQueryString1 | 0,00 |
| Success | testQueryURIEncoding | 0,00 |
| Success | testSetGetQueryString2 | 0,00 |
| Success | testReleaseConnection | 0,00 |
| Success | testEmptyBodyAsString | 0,11 |
| Success | testEmptyBodyAsByteArray | 0,00 |
| Success | testLongBodyAsString | 0,21 |
| Success | testUrlGetMethodWithPathQuery | 0,00 |
| Success | testUrlGetMethodWithPath | 0,00 |
| Success | testUrlGetMethod | 0,00 |
| Success | testUrlGetMethodWithInvalidProtocol | 0,00 |
| Success | testHttpMethodBasePaths | 0,00 |
| Success | testHttpMethodBaseDefaultPath | 0,00 |
| Success | testHttpMethodBasePathConstructor | 0,00 |
| Success | testHttpMethodBaseTEandCL | 0,01 |
| Success | testConnectionAutoClose | 0,01 |
| Success | testSetGetQueryString1 | 0,00 |
| Success | testQueryURIEncoding | 0,00 |
| Success | testSetGetQueryString2 | 0,00 |
| Success | testReleaseConnection | 0,00 |
| Success | testEmptyBodyAsString | 0,11 |
| Success | testEmptyBodyAsByteArray | 0,00 |
| Success | testLongBodyAsString | 0,21 |
| Success | testUrlGetMethodWithPathQuery | 0,00 |
| Success | testUrlGetMethodWithPath | 0,00 |
| Success | testUrlGetMethod | 0,00 |
| Success | testUrlGetMethodWithInvalidProtocol | 0,00 |
| Success | testStatusText | 0,00 |
| Success | testStatusTextNegative | 0,00 |
| Success | testStatusTextAll | 0,00 |
| Success | testIfStatusLine | 0,00 |
| Success | testSuccess | 0,00 |
| Success | testFailure | 0,00 |
| Success | testRequestLineGeneral | 0,00 |
| Success | testRequestLineQuery | 0,00 |
| Success | testRequestLinePath | 0,00 |
| Success | testToExternalFormNull | 0,00 |
| Success | testToExternalFormNullName | 0,00 |
| Success | testToExternalFormNullValue | 0,00 |
| Success | testToExternalForm | 0,00 |
| Success | testEqualToNVP | 0,00 |
| Success | testGet | 0,00 |
| Success | testSet | 0,00 |
| Success | testHashCode | 0,00 |
| Success | testEquals | 0,00 |
| Success | testOldMain | 0,00 |
| Success | testFringeCase1 | 0,00 |
| Success | testFringeCase2 | 0,00 |
| Success | testFringeCase3 | 0,00 |
| Success | testGet | 0,00 |
| Success | testSet | 0,00 |
| Success | testHashCode | 0,00 |
| Success | testEquals | 0,00 |
| Success | testAddRequestHeader | 0,00 |
| Success | testRemoveRequestHeader | 0,00 |
| Success | testOverwriteRequestHeader | 0,00 |
| Success | testGetResponseHeader | 0,00 |
| Success | testHostRequestHeader | 0,11 |
| Success | testHeaders | 0,00 |
| Success | testDuplicateContentLength | 0,00 |
| Success | testDuplicateConnection | 0,10 |
| Success | testNoContentLength | 0,10 |
| Success | testInvalidContentLength1 | 0,00 |
| Success | testInvalidContentLength2 | 0,00 |
| Success | testProxyNoContentLength | 0,10 |
| Success | testNullHeaders | 0,00 |
| Success | testFoldedHeaders | 0,00 |
| Success | testForceCloseConnection | 0,00 |
| Success | testForceCloseConnection2 | 0,00 |
| Success | testNoContent | 0,10 |
| Success | testNullHeader | 0,00 |
| Success | testHostHeaderPortHTTP80 | 0,00 |
| Success | testHostHeaderPortHTTP81 | 0,00 |
| Success | testHostHeaderPortHTTPS443 | 0,00 |
| Success | testHostHeaderPortHTTPS444 | 0,00 |
| Success | testHeadersPreserveCaseKeyIgnoresCase | 0,00 |
| Success | testChunkedInputStream | 0,00 |
| Success | testCorruptChunkedInputStream1 | 0,00 |
| Success | testEmptyChunkedInputStream | 0,00 |
| Success | testContentLengthInputStream | 0,00 |
| Success | testContentLengthInputStreamSkip | 0,00 |
| Success | testChunkedConsitance | 0,00 |
| Success | testChunkedOutputStream | 0,00 |
| Success | testChunkedOutputStreamLargeChunk | 0,00 |
| Success | testChunkedOutputStreamSmallChunk | 0,00 |
| Success | testAutoCloseInputStream | 0,00 |
| Success | testParsing | 0,00 |
| Success | testParsingEscapedChars | 0,00 |
| Success | testParsingBlankParams | 0,00 |
| Success | testBasicValueFormatting | 0,00 |
| Success | testGet | 0,00 |
| Success | testSet | 0,00 |
| Success | testHashCode | 0,00 |
| Success | testEquals | 0,00 |
| Success | testRequestCharEncoding | 0,00 |
| Success | testNoExplicitCharEncoding | 0,00 |
| Success | testExplicitCharEncoding | 0,00 |
| Success | testLatinAccentInRequestBody | 0,00 |
| Success | testRussianInRequestBody | 0,00 |
| Success | testQueryParams | 0,00 |
| Success | testUrlEncodedRequestBody | 0,00 |
| Success | testRequestEntityLength | 0,01 |
| Success | testHttpVersionInvalidConstructorInput | 0,00 |
| Success | testHttpVersionParsing | 0,00 |
| Success | testInvalidHttpVersionParsing | 0,00 |
| Success | testHttpVersionEquality | 0,00 |
| Success | testHttpVersionComparison | 0,00 |
| Success | testClientLevelHttpVersion | 0,00 |
| Success | testMethodLevelHttpVersion | 0,01 |
| Success | testHostLevelHttpVersion | 0,00 |
| Success | testReadHttpLine | 0,00 |
| Success | testReadWellFormedHttpHeaders | 0,00 |
| Success | testReadMalformedHttpHeaders | 0,00 |
| Success | testHeadersTerminatorLeniency1 | 0,00 |
| Success | testHeadersTerminatorLeniency2 | 0,00 |
| Success | test1Lenient | 0,10 |
| Success | test1Strict | 0,10 |
| Success | testProtocol | 0,00 |
| Success | testProtocolSocketFactory | 0,00 |
| Success | testProtocolSocketFactorySublass | 0,00 |
| Success | testHostConfiguration | 0,00 |
| Success | testGetMethodQueryString | 0,00 |
| Success | testGetMethodQueryString2 | 0,00 |
| Success | testGetMethodParameters | 0,00 |
| Success | testGetMethodMultiParameters | 0,00 |
| Success | testGetMethodParameterWithoutValue | 0,00 |
| Success | testGetMethodParameterAppearsTwice | 0,00 |
| Success | testGetMethodOverwriteQueryString | 0,00 |
| Success | testPostMethodParameterAndQueryString | 0,00 |
| Success | testGetCause | 0,00 |
| Success | testStackTraceWriter | 0,00 |
| Success | testStackTraceStream | 0,00 |
| Success | testHttpStateCredentials | 0,00 |
| Success | testToString | 0,00 |
| Success | testHttpStateNoCredentials | 0,00 |
| Success | testHttpStateDefaultCredentials | 0,00 |
| Success | testHttpStateProxyCredentials | 0,00 |
| Success | testHttpStateProxyNoCredentials | 0,00 |
| Success | testHttpStateProxyDefaultCredentials | 0,00 |
| Success | testDefaultCredentials | 0,00 |
| Success | testRealmCredentials | 0,00 |
| Success | testHostCredentials | 0,00 |
| Success | testWrongHostCredentials | 0,00 |
| Success | testWrongRealmCredentials | 0,00 |
| Success | testScopeMatching | 0,00 |
| Success | testCredentialsMatching | 0,00 |
| Success | testDefaultConstuctor | 0,00 |
| Success | testComparator | 0,01 |
| Success | testDefaultConstuctor | 0,00 |
| Success | testComparator | 0,01 |
| Success | testParseAttributeInvalidAttrib | 0,00 |
| Success | testParseAttributeInvalidCookie | 0,00 |
| Success | testParseAttributeNullPath | 0,00 |
| Success | testParseAttributeBlankPath | 0,00 |
| Success | testParseAttributeNullDomain | 0,00 |
| Success | testParseAttributeBlankDomain | 0,00 |
| Success | testParseAttributeNullMaxAge | 0,00 |
| Success | testParseAttributeInvalidMaxAge | 0,00 |
| Success | testParseAttributeNullExpires | 0,00 |
| Success | testParseAttributeUnknownValue | 0,00 |
| Success | testValidateNullHost | 0,00 |
| Success | testValidateBlankHost | 0,00 |
| Success | testValidateNullPath | 0,00 |
| Success | testValidateBlankPath | 0,00 |
| Success | testValidateInvalidPort | 0,00 |
| Success | testValidateInvalidCookieVersion | 0,00 |
| Success | testDomainCaseInsensitivity | 0,00 |
| Success | testParse1 | 0,00 |
| Success | testParse2 | 0,00 |
| Success | testParse3 | 0,00 |
| Success | testQuotedExpiresAttribute | 0,00 |
| Success | testSecurityError | 0,00 |
| Success | testParseSimple | 0,00 |
| Success | testParseSimple2 | 0,00 |
| Success | testParseNoName | 0,00 |
| Success | testParseNoValue | 0,00 |
| Success | testParseWithWhiteSpace | 0,00 |
| Success | testParseWithQuotes | 0,00 |
| Success | testParseWithPath | 0,00 |
| Success | testParseWithDomain | 0,00 |
| Success | testParseWithSecure | 0,00 |
| Success | testParseWithComment | 0,00 |
| Success | testParseWithExpires | 0,00 |
| Success | testParseWithAll | 0,00 |
| Success | testParseMultipleDifferentPaths | 0,00 |
| Success | testParseMultipleSamePaths | 0,00 |
| Success | testParseRelativePath | 0,00 |
| Success | testParseWithWrongDomain | 0,00 |
| Success | testParseWithNullHost | 0,00 |
| Success | testParseWithBlankHost | 0,00 |
| Success | testParseWithNullPath | 0,00 |
| Success | testParseWithBlankPath | 0,00 |
| Success | testParseWithNegativePort | 0,00 |
| Success | testParseWithNullHostAndPath | 0,00 |
| Success | testParseWithPathMismatch | 0,00 |
| Success | testParseWithPathMismatch2 | 0,00 |
| Success | testParseWithInvalidHeader1 | 0,00 |
| Success | testParseWithInvalidHeader2 | 0,00 |
| Success | testCookieNameWithBlanks | 0,00 |
| Success | testCookieNameStartingWithDollarSign | 0,00 |
| Success | testCookieWithComma | 0,00 |
| Success | testDateFormats | 0,02 |
| Success | testSecondDomainLevelCookie | 0,00 |
| Success | testSecondDomainLevelCookieMatch1 | 0,00 |
| Success | testSecondDomainLevelCookieMatch2 | 0,00 |
| Success | testSecondDomainLevelCookieMatch3 | 0,00 |
| Success | testInvalidSecondDomainLevelCookieMatch1 | 0,00 |
| Success | testInvalidSecondDomainLevelCookieMatch2 | 0,00 |
| Success | testMatchNullHost | 0,00 |
| Success | testMatchBlankHost | 0,00 |
| Success | testMatchInvalidPort | 0,00 |
| Success | testMatchNullPath | 0,00 |
| Success | testMatchBlankPath | 0,00 |
| Success | testMatchNullCookie | 0,00 |
| Success | testMatchNullCookieDomain | 0,00 |
| Success | testMatchNullCookiePath | 0,00 |
| Success | testCookieMatch1 | 0,00 |
| Success | testCookieMatch2 | 0,00 |
| Success | testCookieMatch3 | 0,00 |
| Success | testCookieMatch4 | 0,00 |
| Success | testCookieMismatch1 | 0,00 |
| Success | testCookieMismatch2 | 0,00 |
| Success | testCookieMismatch3 | 0,00 |
| Success | testCookieMismatch4 | 0,00 |
| Success | testCookieMatch5 | 0,00 |
| Success | testCookieMismatch6 | 0,00 |
| Success | testMatchNullCookies | 0,00 |
| Success | testMatchedCookiesOrder | 0,00 |
| Success | testInvalidMatchDomain | 0,00 |
| Success | testFormatInvalidCookie | 0,00 |
| Success | testGenericCookieFormatting | 0,00 |
| Success | testGenericCookieFormattingAsHeader | 0,00 |
| Success | testNullCookieValueFormatting | 0,00 |
| Success | testFormatInvalidCookies | 0,00 |
| Success | testFormatZeroCookies | 0,00 |
| Success | testFormatSeveralCookies | 0,00 |
| Success | testFormatOneCookie | 0,00 |
| Success | testFormatSeveralCookiesAsHeader | 0,00 |
| Success | testKeepCloverHappy | 0,00 |
| Success | testParseAttributeInvalidAttrib | 0,00 |
| Success | testParseAttributeInvalidCookie | 0,00 |
| Success | testParseAttributeNullPath | 0,00 |
| Success | testParseAttributeBlankPath | 0,00 |
| Success | testCookieNameWithBlanks | 0,00 |
| Success | testCookieNameStartingWithDollarSign | 0,00 |
| Success | testCookieWithComma | 0,00 |
| Success | testSecondDomainLevelCookie | 0,00 |
| Success | testNullCookieValueFormatting | 0,00 |
| Success | testFormatInvalidCookies | 0,00 |
| Success | testParseAttributeNullVersion | 0,00 |
| Success | testParseAttributeInvalidVersion | 0,00 |
| Success | testParseVersion | 0,00 |
| Success | testParseDomainEqualsHost | 0,00 |
| Success | testParseWithIllegalDomain1 | 0,00 |
| Success | testParseWithIllegalDomain2 | 0,00 |
| Success | testParseWithIllegalDomain3 | 0,00 |
| Success | testParseWithIllegalDomain4 | 0,00 |
| Success | testSecondDomainLevelCookieMatch | 0,00 |
| Success | testParseWithWrongPath | 0,00 |
| Success | testInvalidDomainWithSimpleHostName | 0,00 |
| Success | testRFC2109CookieFormatting | 0,00 |
| Success | testRFC2109CookiesFormatting | 0,00 |
| Success | testCookieNullDomainNullPathFormatting | 0,00 |
| Success | testFormatInvalidCookie | 0,00 |
| Success | testParseVersion | 0,00 |
| Success | testParseInvalidParams | 0,00 |
| Success | testParsePath | 0,00 |
| Success | testParsePathDefault | 0,00 |
| Success | testParseNullPath | 0,00 |
| Success | testParseBlankPath | 0,00 |
| Success | testParseDomain | 0,00 |
| Success | testParseDomainDefault | 0,00 |
| Success | testParseNullDomain | 0,00 |
| Success | testParseBlankDomain | 0,00 |
| Success | testParsePort | 0,00 |
| Success | testParsePortDefault | 0,00 |
| Success | testParseNullPort | 0,00 |
| Success | testParseBlankPort | 0,00 |
| Success | testParseInvalidPort | 0,00 |
| Success | testParseNegativePort | 0,00 |
| Success | testParseNameValue | 0,00 |
| Success | testParseNullVersion | 0,00 |
| Success | testParseNegativeVersion | 0,00 |
| Success | testParseMaxage | 0,00 |
| Success | testParseMaxageDefault | 0,00 |
| Success | testParseNullMaxage | 0,00 |
| Success | testParseNegativeMaxage | 0,00 |
| Success | testParseSecure | 0,00 |
| Success | testParseDiscard | 0,00 |
| Success | testParseOtherAttributes | 0,00 |
| Success | testCookiesWithComma | 0,00 |
| Success | testValidateNoDomain | 0,00 |
| Success | testValidateDomainLeadingDot | 0,00 |
| Success | testValidateDomainEmbeddedDot | 0,00 |
| Success | testValidateDomainLocal | 0,00 |
| Success | testValidateDomainEffectiveHost | 0,00 |
| Success | testValidateDomainIllegal | 0,00 |
| Success | testValidatePath | 0,00 |
| Success | testValidateCookieName | 0,00 |
| Success | testValidatePort | 0,00 |
| Success | testValidateVersion | 0,00 |
| Success | testMatchPath | 0,00 |
| Success | testMatchDomain | 0,00 |
| Success | testMatchDomainLocal | 0,00 |
| Success | testMatchPort | 0,00 |
| Success | testCookieExpiration | 0,00 |
| Success | testCookieSecure | 0,00 |
| Success | testRFC2965CookieFormatting | 0,00 |
| Success | testRFC2965CookiesFormatting | 0,00 |
| Success | testCompatibilityWithSetCookie | 0,00 |
| Success | testParseAttributeInvalidAttrib | 0,00 |
| Success | testParseAttributeInvalidCookie | 0,00 |
| Success | testParseRelativePath | 0,00 |
| Success | testParseWithNullHost | 0,00 |
| Success | testParseWithBlankHost | 0,00 |
| Success | testParseWithNullPath | 0,00 |
| Success | testParseWithBlankPath | 0,00 |
| Success | testParseWithNegativePort | 0,00 |
| Success | testParseWithInvalidHeader1 | 0,00 |
| Success | testCookieWithComma | 0,00 |
| Success | testParseAttributeInvalidCookieExpires | 0,00 |
| Success | testParseAbsPath | 0,00 |
| Success | testParseAbsPath2 | 0,00 |
| Success | testParseWithIllegalNetscapeDomain1 | 0,00 |
| Success | testParseWithWrongNetscapeDomain2 | 0,00 |
| Success | testNetscapeCookieFormatting | 0,00 |
| Success | testNetscapeCookieExpireAttribute | 0,00 |
| Success | testNetscapeCookieExpireAttributeNoTimeZone | 0,00 |
| Success | testKeepCloverHappy | 0,00 |
| Success | testIgnoreCookies | 0,00 |
| Success | testRegisterNullPolicyId | 0,00 |
| Success | testRegisterNullPolicy | 0,00 |
| Success | testUnregisterNullPolicy | 0,00 |
| Success | testGetPolicyNullId | 0,00 |
| Success | testRegisterUnregister | 0,00 |
| Success | testGetDefaultPolicy | 0,00 |
| Success | testFourDigitYear | 0,00 |
| Success | testThreeDigitYear | 0,00 |
| Success | testTwoDigitYear | 0,00 |
| Success | testUnequality1 | 0,00 |
| Success | testUnequality2 | 0,00 |
| Success | testEquality1 | 0,00 |
| Success | testEquality2 | 0,00 |
| Success | testEquality3 | 0,00 |
| Success | testEquality4 | 0,00 |
| Success | testCookieVersionSupportHeader1 | 0,04 |
| Success | testCookieVersionSupportHeader2 | 0,04 |
| Success | testCookieVersionSupportHeader3 | 0,04 |
| Success | testSetCookieVersionMix | 0,00 |
| Success | testCredentialConstructors | 0,00 |
| Success | testCredentialEquals | 0,00 |
| Success | testParsingChallenge | 0,00 |
| Success | testChallengeSelection | 0,00 |
| Success | testInvalidChallenge | 0,00 |
| Success | testUnsupportedChallenge | 0,00 |
| Success | testChallengeProcessing | 0,00 |
| Success | testInvalidChallengeProcessing | 0,00 |
| Success | testBasicAuthenticationWithNoCreds | 0,00 |
| Success | testBasicAuthenticationWithNoCredsRetry | 0,08 |
| Success | testBasicAuthenticationWithNoRealm | 0,00 |
| Success | testBasicAuthenticationWith88591Chars | 0,00 |
| Success | testBasicAuthenticationWithDefaultCreds | 0,04 |
| Success | testBasicAuthentication | 0,04 |
| Success | testBasicAuthenticationWithInvalidCredentials | 0,05 |
| Success | testBasicAuthenticationWithMutlipleRealms1 | 0,04 |
| Success | testBasicAuthenticationWithMutlipleRealms2 | 0,04 |
| Success | testPreemptiveAuthorizationTrueWithCreds | 0,00 |
| Success | testPreemptiveAuthorizationTrueWithoutCreds | 0,00 |
| Success | testCustomAuthorizationHeader | 0,00 |
| Success | testHeadBasicAuthentication | 0,00 |
| Success | testPostBasicAuthentication | 0,04 |
| Success | testPutBasicAuthentication | 0,05 |
| Success | testPreemptiveAuthorizationFailure | 0,00 |
| Success | testBasicAuthenticationWithNoCreds | 0,01 |
| Success | testBasicAuthenticationWithNoCredsRetry | 0,09 |
| Success | testBasicAuthenticationWithNoRealm | 0,00 |
| Success | testBasicAuthenticationWith88591Chars | 0,00 |
| Success | testBasicAuthenticationWithDefaultCreds | 0,05 |
| Success | testBasicAuthentication | 0,05 |
| Success | testBasicAuthenticationWithInvalidCredentials | 0,05 |
| Success | testBasicAuthenticationWithMutlipleRealms1 | 0,05 |
| Success | testBasicAuthenticationWithMutlipleRealms2 | 0,05 |
| Success | testPreemptiveAuthorizationTrueWithCreds | 0,00 |
| Success | testPreemptiveAuthorizationTrueWithoutCreds | 0,00 |
| Success | testCustomAuthorizationHeader | 0,01 |
| Success | testHeadBasicAuthentication | 0,01 |
| Success | testPostBasicAuthentication | 0,08 |
| Success | testPutBasicAuthentication | 0,08 |
| Success | testPreemptiveAuthorizationFailure | 0,00 |
| Success | testDigestAuthenticationWithNoRealm | 0,00 |
| Success | testDigestAuthenticationWithNoRealm2 | 0,00 |
| Success | testDigestAuthenticationWithDefaultCreds | 0,01 |
| Success | testDigestAuthentication | 0,00 |
| Success | testDigestAuthenticationWithQueryStringInDigestURI | 0,00 |
| Success | testDigestAuthenticationWithMultipleRealms | 0,00 |
| Success | testDigestAuthenticationMD5Sess | 0,00 |
| Success | testDigestAuthenticationMD5SessNoQop | 0,00 |
| Success | testDigestAuthenticationMD5SessInvalidQop | 0,00 |
| Success | testDigestAuthenticationWithStaleNonce | 0,09 |
| Success | testNTLMAuthenticationResponse1 | 0,00 |
| Success | testNTLMAuthenticationResponse2 | 0,34 |
| Success | testNTLMAuthenticationRetry | 0,09 |
| Success | testPreemptiveAuthorization | 0,00 |
| Success | testBasicRedirect300 | 0,00 |
| Success | testBasicRedirect301 | 0,11 |
| Success | testBasicRedirect302 | 0,10 |
| Success | testBasicRedirect303 | 0,10 |
| Success | testBasicRedirect304 | 0,00 |
| Success | testBasicRedirect305 | 0,00 |
| Success | testBasicRedirect307 | 0,11 |
| Success | testNoRedirect | 0,00 |
| Success | testMaxRedirectCheck | 0,02 |
| Success | testCircularRedirect | 0,01 |
| Success | testPostRedirect | 0,00 |
| Success | testRelativeRedirect | 0,04 |
| Success | testRejectRelativeRedirect | 0,00 |
| Success | testRejectBogusRedirectLocation | 0,00 |
| Success | testRejectInvalidRedirectLocation | 0,00 |
| Success | testCrossSiteRedirect | 0,00 |
| Success | testRedirectWithCookie | 0,10 |
| Success | testBasicRedirect300 | 0,00 |
| Success | testBasicRedirect301 | 0,11 |
| Success | testBasicRedirect302 | 0,11 |
| Success | testBasicRedirect303 | 0,10 |
| Success | testBasicRedirect304 | 0,00 |
| Success | testBasicRedirect305 | 0,00 |
| Success | testBasicRedirect307 | 0,11 |
| Success | testNoRedirect | 0,00 |
| Success | testMaxRedirectCheck | 0,02 |
| Success | testCircularRedirect | 0,01 |
| Success | testPostRedirect | 0,00 |
| Success | testRelativeRedirect | 0,05 |
| Success | testRejectRelativeRedirect | 0,00 |
| Success | testRejectBogusRedirectLocation | 0,00 |
| Success | testRejectInvalidRedirectLocation | 0,00 |
| Success | testCrossSiteRedirect | 0,00 |
| Success | testRedirectWithCookie | 0,11 |
| Success | testConstructThenClose | 0,00 |
| Success | testConnTimeoutRelease | 0,01 |
| Success | testConnTimeout | 0,00 |
| Success | testForIllegalStateExceptions | 0,00 |
| Success | testReleaseConnection | 0,02 |
| Success | testConnectMethodFailureRelease | 0,22 |
| Success | testGetConnection | 0,00 |
| Success | testDroppedThread | 1,10 |
| Success | testWriteRequestReleaseConnection | 0,00 |
| Success | testResponseAutoRelease | 0,01 |
| Success | testConnectionReclaiming | 0,00 |
| Success | testShutdownAll | 0,00 |
| Success | testShutdown | 0,00 |
| Success | testMaxConnections | 0,10 |
| Success | testMaxConnectionsPerHost | 0,32 |
| Success | testHostReusePreference | 0,20 |
| Success | testMaxConnectionsPerServer | 0,00 |
| Success | testDeleteClosedConnections | 0,00 |
| Success | testWaitingThreadInterrupted | 0,50 |
| Success | testReclaimUnusedConnection | 0,10 |
| Success | testGetFromMultipleThreads | 0,10 |
| Success | testTimeout | 1,00 |
| Success | testConnPersisenceHTTP10 | 0,10 |
| Success | testConnPersisenceHTTP11 | 0,04 |
| Success | testConnClose | 0,00 |
| Success | testConnKeepAlive | 0,10 |
| Success | testRequestConnClose | 0,00 |
| Success | testProxyConnClose | 0,00 |
| Success | testHandler | 0,51 |
| Success | testTimeoutThread | 0,50 |
| Success | testAbortMethod | 0,50 |
| Success | testAbortedMethodExecute | 0,00 |
| Success | testDefaultHeaders | 0,05 |
| Success | testDefaults | 0,04 |
| Success | testTunnellingParamsAgentLevel | 0,54 |
| Success | testTunnellingParamsHostLevel | 0,42 |
| Success | testTunnellingParamsHostHTTP10AndMethodHTTP11 | 0,43 |
| Success | testVirtualHostHeader | 0,00 |
| Success | testNoVirtualHostHeader | 0,00 |
| Success | testRedirectWithVirtualHost | 0,21 |
| Success | testRelativeURLHitWithDefaultHost | 0,00 |
| Success | testRelativeURLHitWithoutDefaultHost | 0,00 |
| Success | testAbsoluteURLHitWithoutDefaultHost | 0,00 |
| Success | testAbsoluteURLOverridesClientDefaultHost | 0,17 |
| Success | testAbsoluteURLOverridesDefaultHostParam | 0,26 |
| Success | testClientClonesHostConfiguration | 0,00 |
| Success | testIPv4Address | 0,00 |
| Success | testUrl | 0,00 |
| Success | testRelativeURIConstructor | 0,01 |
| Success | testTestURIAuthorityString | 0,00 |
| Success | testTestHttpUrlAuthorityString | 0,00 |
| Success | testTestHttpsUrlAuthorityString | 0,00 |
| Success | testURIEscaping | 0,00 |
| Success | testBug578 | 0,00 |
| Success | testVariousCharacters | 0,00 |
| Success | testRelativeWithScheme | 0,00 |
| Success | testRelativeWithDoubleSlash | 0,00 |
| Success | testGetPath | 0,00 |
| Success | testGetQueryString | 0,00 |
| Success | testGetPath | 0,00 |
| Success | testGetQueryString | 0,00 |
| Success | testEnclosedEntityAutoLength | 0,00 |
| Success | testEnclosedEntityExplicitLength | 0,00 |
| Success | testEnclosedEntityChunked | 0,00 |
| Success | testEnclosedEntityChunkedHTTP1\_0 | 0,00 |
| Success | testEnclosedEntityRepeatable | 0,05 |
| Success | testEnclosedEntityNonRepeatable | 0,00 |
| Success | testEnclosedEntityNegativeLength | 0,00 |
| Success | testEnclosedEntityNegativeLengthHTTP1\_0 | 0,00 |
| Success | testEmptyPostMethod | 0,14 |
| Success | testPostParametersEncoding | 0,00 |
| Success | testPostSetRequestBody | 0,00 |
| Success | testParametersBodyToParamServlet | 0,00 |
| Success | testStringBodyToParamServlet | 0,00 |
| Success | testStringBodyToBodyServlet | 0,00 |
| Success | testAddParametersToParamServlet | 0,00 |
| Success | testAddRemoveParametersToParamServlet | 0,00 |
| Success | testRemoveParameterReturnValue | 0,00 |
| Success | testAddParameterFollowedBySetParameter | 0,00 |
| Success | testFilePartResendsFileData | 0,00 |
| Success | testStringPartResendsData | 0,00 |
| Success | testFilePartNullFileResendsData | 0,00 |
| Success | testPostStringPart | 0,00 |
| Success | testPostFilePart | 0,00 |
| Success | testPostFilePartUnknownLength | 0,00 |
| Success | testPostStringPart | 0,00 |
| Success | testPostFilePart | 0,00 |
| Success | testPostFilePartUnknownLength | 0,00 |
| Success | testNoncompliantPostMethodString | 0,01 |
| Success | testNoncompliantStatusLine | 0,00 |
| Success | testNoncompliantHeadWithResponseBody | 0,00 |
| Success | testNoncompliantHeadStrictMode | 0,00 |
| Success | testMalformed304Response | 0,00 |
| Success | testMalformed204Response | 0,00 |
| Success | testSimpleGet | 0,00 |
| Success | testGetHostAuthConnKeepAlive | 0,05 |
| Success | testGetHostAuthConnClose | 0,11 |
| Success | testGetHostInvalidAuth | 0,04 |
| Success | testGetInteractiveHostAuthConnKeepAlive | 0,09 |
| Success | testGetInteractiveHostAuthConnClose | 0,21 |
| Success | testGetProxyAuthHostAuthConnKeepAlive | 0,09 |
| Success | testGetAuthProxy | 0,04 |
| Success | testGetProxyAuthHostAuthConnClose | 0,11 |
| Success | testGetProxyAuthHostInvalidAuth | 0,09 |
| Success | testGetInteractiveProxyAuthHostAuthConnKeepAlive | 0,18 |
| Success | testGetInteractiveProxyAuthHostAuthConnClose | 0,26 |
| Success | testSimplePost | 0,00 |
| Success | testPostHostAuthConnKeepAlive | 0,09 |
| Success | testPostHostAuthConnClose | 0,10 |
| Success | testPostHostInvalidAuth | 0,09 |
| Success | testPostInteractiveHostAuthConnKeepAlive | 0,17 |
| Success | testPostInteractiveHostAuthConnClose | 0,21 |
| Success | testPostAuthProxy | 0,05 |
| Success | testPostProxyAuthHostAuthConnKeepAlive | 0,13 |
| Success | testPostProxyAuthHostAuthConnClose | 0,11 |
| Success | testPostProxyAuthHostInvalidAuth | 0,13 |
| Success | testPostInteractiveProxyAuthHostAuthConnKeepAlive | 0,26 |
| Success | testPostInteractiveProxyAuthHostAuthConnClose | 0,25 |
| Success | testPreemptiveAuthProxy | 0,00 |
| Success | testGetProxyAuthHostAuthHTTP10 | 0,11 |
| Success | testSimpleGet | 0,42 |
| Success | testGetHostAuthConnKeepAlive | 0,51 |
| Success | testGetHostAuthConnClose | 0,61 |
| Success | testGetHostInvalidAuth | 0,51 |
| Success | testGetInteractiveHostAuthConnKeepAlive | 0,62 |
| Success | testGetInteractiveHostAuthConnClose | 1,11 |
| Success | testGetProxyAuthHostAuthConnKeepAlive | 0,51 |
| Success | testGetAuthProxy | 0,50 |
| Success | testGetProxyAuthHostAuthConnClose | 0,64 |
| Success | testGetProxyAuthHostInvalidAuth | 0,51 |
| Success | testGetInteractiveProxyAuthHostAuthConnKeepAlive | 0,54 |
| Success | testGetInteractiveProxyAuthHostAuthConnClose | 0,73 |
| Success | testSimplePost | 0,40 |
| Success | testPostHostAuthConnKeepAlive | 0,40 |
| Success | testPostHostAuthConnClose | 0,51 |
| Success | testPostHostInvalidAuth | 0,51 |
| Success | testPostInteractiveHostAuthConnKeepAlive | 0,71 |
| Success | testPostInteractiveHostAuthConnClose | 1,10 |
| Success | testPostAuthProxy | 0,50 |
| Success | testPostProxyAuthHostAuthConnKeepAlive | 0,51 |
| Success | testPostProxyAuthHostAuthConnClose | 0,70 |
| Success | testPostProxyAuthHostInvalidAuth | 0,41 |
| Success | testPostInteractiveProxyAuthHostAuthConnKeepAlive | 0,53 |
| Success | testPostInteractiveProxyAuthHostAuthConnClose | 1,12 |
| Success | testPreemptiveAuthProxy | 0,50 |
| Success | testGetProxyAuthHostAuthHTTP10 | 0,49 |
| Success | testAuthProxyWithRedirect | 0,12 |
| Success | testAuthProxyWithCrossSiteRedirect | 0,11 |
| Success | testPreemptiveAuthProxyWithCrossSiteRedirect | 0,11 |

---
## Javadoc Report

```
  Generating Javadoc
  Javadoc execution
  Loading source files for package org.apache.commons.httpclient...
  Loading source files for package org.apache.commons.httpclient.auth...
  Loading source files for package org.apache.commons.httpclient.protocol...
  Loading source files for package org.apache.commons.httpclient.methods...
  Loading source files for package org.apache.commons.httpclient.methods.multipart...
  Loading source files for package org.apache.commons.httpclient.cookie...
  Loading source files for package org.apache.commons.httpclient.params...
  Loading source files for package org.apache.commons.httpclient.util...
  Constructing Javadoc information...
  Standard Doclet version 1.5.0_13
  Building tree for all the packages and classes...
  Generating target/docs/apidocs/serialized-form.html...
  Copying file /home/rweber/.maven/cache/maven-javadoc-plugin-1.7/plugin-resources/stylesheet.css to file target/docs/apidocs/stylesheet.css...
  Building index for all the packages and classes...
  Building index for all classes...
```

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/SecureProtocolSocketFactory.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/protocol/ReflectionSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/protocol/SSLProtocolSocketFactory.html "class in org.apache.commons.httpclient.protocol") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/protocol/SecureProtocolSocketFactory.html)    [**NO FRAMES**](SecureProtocolSocketFactory.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient.protocol Interface SecureProtocolSocketFactory

**All Superinterfaces:**: [ProtocolSocketFactory](../../../../../org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol")

**All Known Implementing Classes:**: [SSLProtocolSocketFactory](../../../../../org/apache/commons/httpclient/protocol/SSLProtocolSocketFactory.html "class in org.apache.commons.httpclient.protocol")

---

``` public interface SecureProtocolSocketFactory extends ProtocolSocketFactory ```

A ProtocolSocketFactory that is secure.

**Since:**
:   2.0

**Author:**
:   Michael Becke, [Mike Bowler](mailto:mbowler@GargoyleSoftware.com)

**See Also:**: [`ProtocolSocketFactory`](../../../../../org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol")

---

| **Method Summary** | |
| --- | --- |
| `Socket` | `createSocket(Socket socket, String host, int port, boolean autoClose)`             Returns a socket connected to the given host that is layered over an existing socket. |

| **Methods inherited from interface org.apache.commons.httpclient.protocol.[ProtocolSocketFactory](../../../../../org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol")** |
| --- |
| `createSocket, createSocket, createSocket` |

| **Method Detail** |
| --- |

### createSocket

```
Socket createSocket(Socket socket,
                    String host,
                    int port,
                    boolean autoClose)
                    throws IOException,
                           UnknownHostException
```

:   Returns a socket connected to the given host that is layered over an
    existing socket. Used primarily for creating secure sockets through
    proxies.

    :   **Parameters:**: `socket` - the existing socket: `host` - the host name/IP: `port` - the port on the host: `autoClose` - a flag for closing the underling socket when the created socket is closed **Returns:**: Socket a new socket **Throws:**: `IOException` - if an I/O error occurs while creating the socket: `UnknownHostException` - if the IP address of the host cannot be determined



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/SecureProtocolSocketFactory.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/protocol/ReflectionSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/protocol/SSLProtocolSocketFactory.html "class in org.apache.commons.httpclient.protocol") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/protocol/SecureProtocolSocketFactory.html)    [**NO FRAMES**](SecureProtocolSocketFactory.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/Protocol.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/protocol/DefaultProtocolSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/protocol/Protocol.html)    [**NO FRAMES**](Protocol.html) |
| SUMMARY: NESTED | FIELD | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: FIELD | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient.protocol Class Protocol

```
java.lang.Object
  ![extended by ](assets/httpclient-legacy_apidocs_resources_inherit.gif)org.apache.commons.httpclient.protocol.Protocol
```

---

``` public class Protocol extends Object ```

A class to encapsulate the specifics of a protocol. This class class also
provides the ability to customize the set and characteristics of the
protocols used.

One use case for modifying the default set of protocols would be to set a
custom SSL socket factory. This would look something like the following:

```
 Protocol myHTTPS = new Protocol( "https", new MySSLSocketFactory(), 443 );
 
 Protocol.registerProtocol( "https", myHTTPS );
```

**Since:**
:   2.0

**Author:**
:   Michael Becke, Jeff Dever, [Mike Bowler](mailto:mbowler@GargoyleSoftware.com)

---

| **Constructor Summary** | |
| --- | --- |
| `Protocol(String scheme, ProtocolSocketFactory factory, int defaultPort)`             Constructs a new Protocol. |
| `Protocol(String scheme, SecureProtocolSocketFactory factory, int defaultPort)`             **Deprecated.** *Use the constructor that uses ProtocolSocketFactory, this version of the constructor is only kept for backwards API compatibility.* |



| **Method Summary** | |
| --- | --- |
| `boolean` | `equals(Object obj)`             Return true if the specified object equals this object. |
| `int` | `getDefaultPort()`             Returns the defaultPort. |
| `static Protocol` | `getProtocol(String id)`             Gets the protocol with the given ID. |
| `String` | `getScheme()`             Returns the scheme. |
| `ProtocolSocketFactory` | `getSocketFactory()`             Returns the socketFactory. |
| `int` | `hashCode()`             Return a hash code for this object |
| `boolean` | `isSecure()`             Returns true if this protocol is secure |
| `static void` | `registerProtocol(String id, Protocol protocol)`             Registers a new protocol with the given identifier. |
| `int` | `resolvePort(int port)`             Resolves the correct port for this protocol. |
| `String` | `toString()`             Return a string representation of this object. |
| `static void` | `unregisterProtocol(String id)`             Unregisters the protocol with the given ID. |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, finalize, getClass, notify, notifyAll, wait, wait, wait` |

| **Constructor Detail** |
| --- |

### Protocol

```
public Protocol(String scheme,
                ProtocolSocketFactory factory,
                int defaultPort)
```

:   Constructs a new Protocol. Whether the created protocol is secure depends on
    the class of `factory`.

    **Parameters:**: `scheme` - the scheme (e.g. http, https): `factory` - the factory for creating sockets for communication using this protocol: `defaultPort` - the port this protocol defaults to

---



### Protocol

```
public Protocol(String scheme,
                SecureProtocolSocketFactory factory,
                int defaultPort)
```

:   **Deprecated.** *Use the constructor that uses ProtocolSocketFactory, this version of
    the constructor is only kept for backwards API compatibility.*

    :   Constructs a new Protocol. Whether the created protocol is secure depends on
        the class of `factory`.

        **Parameters:**: `scheme` - the scheme (e.g. http, https): `factory` - the factory for creating sockets for communication using this protocol: `defaultPort` - the port this protocol defaults to



| **Method Detail** |
| --- |

### registerProtocol

```
public static void registerProtocol(String id,
                                    Protocol protocol)
```

:   Registers a new protocol with the given identifier. If a protocol with
    the given ID already exists it will be overridden. This ID is the same
    one used to retrieve the protocol from getProtocol(String).

    :   **Parameters:**: `id` - the identifier for this protocol: `protocol` - the protocol to register **See Also:**: [`getProtocol(String)`](../../../../../org/apache/commons/httpclient/protocol/Protocol.html#getProtocol(java.lang.String))

---



### unregisterProtocol

```
public static void unregisterProtocol(String id)
```

:   Unregisters the protocol with the given ID.

    :   **Parameters:**: `id` - the ID of the protocol to remove

---



### getProtocol

```
public static Protocol getProtocol(String id)
                            throws IllegalStateException
```

:   Gets the protocol with the given ID.

    :   **Parameters:**: `id` - the protocol ID **Returns:**: Protocol a protocol **Throws:**: `IllegalStateException` - if a protocol with the ID cannot be found

---



### getDefaultPort

```
public int getDefaultPort()
```

:   Returns the defaultPort.

    :   **Returns:**: int

---



### getSocketFactory

```
public ProtocolSocketFactory getSocketFactory()
```

:   Returns the socketFactory. If secure the factory is a
    SecureProtocolSocketFactory.

    :   **Returns:**: SocketFactory

---



### getScheme

```
public String getScheme()
```

:   Returns the scheme.

    :   **Returns:**: The scheme

---



### isSecure

```
public boolean isSecure()
```

:   Returns true if this protocol is secure

    :   **Returns:**: true if this protocol is secure

---



### resolvePort

```
public int resolvePort(int port)
```

:   Resolves the correct port for this protocol. Returns the given port if
    valid or the default port otherwise.

    :   **Parameters:**: `port` - the port to be resolved **Returns:**: the given port or the defaultPort

---



### toString

```
public String toString()
```

:   Return a string representation of this object.

    :   **Overrides:**: `toString` in class `Object`
    :   **Returns:**: a string representation of this object.

---



### equals

```
public boolean equals(Object obj)
```

:   Return true if the specified object equals this object.

    :   **Overrides:**: `equals` in class `Object`
    :   **Parameters:**: `obj` - The object to compare against. **Returns:**: true if the objects are equal.

---



### hashCode

```
public int hashCode()
```

:   Return a hash code for this object

    :   **Overrides:**: `hashCode` in class `Object`
    :   **Returns:**: The hash code.



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/Protocol.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/protocol/DefaultProtocolSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/protocol/Protocol.html)    [**NO FRAMES**](Protocol.html) |
| SUMMARY: NESTED | FIELD | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: FIELD | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/AuthPolicy.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthenticationException.html "class in org.apache.commons.httpclient.auth")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/auth/AuthPolicy.html)    [**NO FRAMES**](AuthPolicy.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient.auth Class AuthPolicy

```
java.lang.Object
  ![extended by ](../../../../../resources/inherit.gif)org.apache.commons.httpclient.auth.AuthPolicy
```

---

``` public abstract class AuthPolicy extends Object ```

Authentication policy class. The Authentication policy provides corresponding
authentication scheme interfrace for a given type of authorization challenge.

The following specifications are provided:

* Basic: Basic authentication scheme as defined in RFC2617
  (considered inherently insecure, but most widely supported)* Digest: Digest authentication scheme as defined in RFC2617* NTLM: The NTLM scheme is a proprietary Microsoft Windows
      Authentication protocol (considered to be the most secure among
      currently supported authentication schemes)

**Since:**
:   3.0

**Version:**
:   $Revision: 1425331 $

**Author:**
:   [Oleg Kalnichevski](mailto:oleg@ural.ru)

---

| **Field Summary** | |
| --- | --- |
| `static String` | `AUTH_SCHEME_PRIORITY`             The key used to look up the list of IDs of supported [`authentication schemes`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") in their order of preference. |
| `static String` | `BASIC`             Basic authentication scheme as defined in RFC2617 (considered inherently insecure, but most widely supported) |
| `static String` | `DIGEST`             Digest authentication scheme as defined in RFC2617. |
| `protected static Log` | `LOG`             Log object. |
| `static String` | `NTLM`             The NTLM scheme is a proprietary Microsoft Windows Authentication protocol (considered to be the most secure among currently supported authentication schemes). |



| **Constructor Summary** | |
| --- | --- |
| `AuthPolicy()` |



| **Method Summary** | |
| --- | --- |
| `static AuthScheme` | `getAuthScheme(String id)`             Gets the [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") with the given ID. |
| `static List` | `getDefaultAuthPrefs()`             Returns a list containing all registered [`authentication schemes`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") in their default order. |
| `static void` | `registerAuthScheme(String id, Class clazz)`             Registers a class implementing an [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") with the given identifier. |
| `static void` | `unregisterAuthScheme(String id)`             Unregisters the class implementing an [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") with the given ID. |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Field Detail** |
| --- |

### AUTH\_SCHEME\_PRIORITY

```
public static final String AUTH_SCHEME_PRIORITY
```

:   The key used to look up the list of IDs of supported [`authentication schemes`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") in their order of preference. The scheme IDs are
    stored in a [`Collection`](http://java.sun.com/j2se/1.5.0/docs/api/java/util/Collection.html "class or interface in java.util") as [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang")s.

    If several schemes are returned in the WWW-Authenticate
    or Proxy-Authenticate header, this parameter defines which
    [`authentication schemes`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") takes precedence over others.
    The first item in the collection represents the most preferred
    [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth"), the last item represents the ID
    of the least preferred one.

    **See Also:**: [`DefaultHttpParams`](../../../../../org/apache/commons/httpclient/params/DefaultHttpParams.html "class in org.apache.commons.httpclient.params"), [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.auth.AuthPolicy.AUTH_SCHEME_PRIORITY)

---



### NTLM

```
public static final String NTLM
```

:   The NTLM scheme is a proprietary Microsoft Windows Authentication
    protocol (considered to be the most secure among currently supported
    authentication schemes).

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.auth.AuthPolicy.NTLM)

---



### DIGEST

```
public static final String DIGEST
```

:   Digest authentication scheme as defined in RFC2617.

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.auth.AuthPolicy.DIGEST)

---



### BASIC

```
public static final String BASIC
```

:   Basic authentication scheme as defined in RFC2617 (considered inherently
    insecure, but most widely supported)

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.auth.AuthPolicy.BASIC)

---



### LOG

```
protected static final Log LOG
```

:   Log object.



| **Constructor Detail** |
| --- |

### AuthPolicy

```
public AuthPolicy()
```



| **Method Detail** |
| --- |

### registerAuthScheme

```
public static void registerAuthScheme(String id,
                                      Class clazz)
```

:   Registers a class implementing an [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") with
    the given identifier. If a class with the given ID already exists it will be overridden.
    This ID is the same one used to retrieve the [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth")
    from [`getAuthScheme(String)`](../../../../../org/apache/commons/httpclient/auth/AuthPolicy.html#getAuthScheme(java.lang.String)).

    Please note that custom authentication preferences, if used, need to be updated accordingly
    for the new [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") to take effect.

    :   **Parameters:**: `id` - the identifier for this scheme: `clazz` - the class to register **See Also:**: [`getAuthScheme(String)`](../../../../../org/apache/commons/httpclient/auth/AuthPolicy.html#getAuthScheme(java.lang.String)), [`AUTH_SCHEME_PRIORITY`](../../../../../org/apache/commons/httpclient/auth/AuthPolicy.html#AUTH_SCHEME_PRIORITY)

---



### unregisterAuthScheme

```
public static void unregisterAuthScheme(String id)
```

:   Unregisters the class implementing an [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") with
    the given ID.

    :   **Parameters:**: `id` - the ID of the class to unregister

---



### getAuthScheme

```
public static AuthScheme getAuthScheme(String id)
                                throws IllegalStateException
```

:   Gets the [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") with the given ID.

    :   **Parameters:**: `id` - the [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") ID **Returns:**: [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") **Throws:**: `IllegalStateException` - if a scheme with the ID cannot be found

---



### getDefaultAuthPrefs

```
public static List getDefaultAuthPrefs()
```

:   Returns a list containing all registered [`authentication
    schemes`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") in their default order.

    :   **Returns:**: [`authentication scheme`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth")



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/AuthPolicy.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthenticationException.html "class in org.apache.commons.httpclient.auth")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/auth/AuthPolicy.html)    [**NO FRAMES**](AuthPolicy.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/AuthScheme.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthPolicy.html "class in org.apache.commons.httpclient.auth")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthSchemeBase.html "class in org.apache.commons.httpclient.auth") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/auth/AuthScheme.html)    [**NO FRAMES**](AuthScheme.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient.auth Interface AuthScheme

**All Known Implementing Classes:**: [AuthSchemeBase](../../../../../org/apache/commons/httpclient/auth/AuthSchemeBase.html "class in org.apache.commons.httpclient.auth"), [BasicScheme](../../../../../org/apache/commons/httpclient/auth/BasicScheme.html "class in org.apache.commons.httpclient.auth"), [DigestScheme](../../../../../org/apache/commons/httpclient/auth/DigestScheme.html "class in org.apache.commons.httpclient.auth"), [NTLMScheme](../../../../../org/apache/commons/httpclient/auth/NTLMScheme.html "class in org.apache.commons.httpclient.auth"), [RFC2617Scheme](../../../../../org/apache/commons/httpclient/auth/RFC2617Scheme.html "class in org.apache.commons.httpclient.auth")

---

``` public interface AuthScheme ```

This interface represents an abstract challenge-response oriented
authentication scheme.

An authentication scheme should be able to support the following
functions:

* Parse and process the challenge sent by the targer server
  in response to request for a protected resource* Provide its textual designation* Provide its parameters, if available* Provide the realm this authentication scheme is applicable to,
        if available* Generate authorization string for the given set of credentials,
          request method and URI as specificed in the HTTP request line
          in response to the actual authorization challenge

Authentication schemes may ignore method name and URI parameters
if they are not relevant for the given authentication mechanism

Authentication schemes may be stateful involving a series of
challenge-response exchanges

**Since:**
:   2.0beta1

**Author:**
:   [Oleg Kalnichevski](mailto:oleg@ural.ru), [Adrian Sutton](mailto:adrian@ephox.com)

---

| **Method Summary** | |
| --- | --- |
| `String` | `authenticate(Credentials credentials, HttpMethod method)`             Produces an authorization string for the given set of [`Credentials`](../../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient"). |
| `String` | `authenticate(Credentials credentials, String method, String uri)`             **Deprecated.** *Use [`authenticate(Credentials, HttpMethod)`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod)) Produces an authorization string for the given set of [`Credentials`](../../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient"), method name and URI using the given authentication scheme in response to the actual authorization challenge.* |
| `String` | `getID()`             **Deprecated.** *no longer used* |
| `String` | `getParameter(String name)`             Returns authentication parameter with the given name, if available. |
| `String` | `getRealm()`             Returns authentication realm. |
| `String` | `getSchemeName()`             Returns textual designation of the given authentication scheme. |
| `boolean` | `isComplete()`             Authentication process may involve a series of challenge-response exchanges. |
| `boolean` | `isConnectionBased()`             Tests if the authentication scheme is provides authorization on a per connection basis instead of usual per request basis |
| `void` | `processChallenge(String challenge)`             Processes the given challenge token. |

| **Method Detail** |
| --- |

### processChallenge

```
void processChallenge(String challenge)
                      throws MalformedChallengeException
```

:   Processes the given challenge token. Some authentication schemes
    may involve multiple challenge-response exchanges. Such schemes must be able
    to maintain the state information when dealing with sequential challenges

    :   **Parameters:**: `challenge` - the challenge string **Throws:**: `MalformedChallengeException` **Since:** : 3.0

---



### getSchemeName

```
String getSchemeName()
```

:   Returns textual designation of the given authentication scheme.

    :   **Returns:**: the name of the given authentication scheme

---



### getParameter

```
String getParameter(String name)
```

:   Returns authentication parameter with the given name, if available.

    :   **Parameters:**: `name` - The name of the parameter to be returned **Returns:**: the parameter with the given name

---



### getRealm

```
String getRealm()
```

:   Returns authentication realm. If the concept of an authentication
    realm is not applicable to the given authentication scheme, returns
    `null`.

    :   **Returns:**: the authentication realm

---



### getID

```
String getID()
```

:   **Deprecated.** *no longer used*

    :   Returns a String identifying the authentication challenge. This is
        used, in combination with the host and port to determine if
        authorization has already been attempted or not. Schemes which
        require multiple requests to complete the authentication should
        return a different value for each stage in the request.

        Additionally, the ID should take into account any changes to the
        authentication challenge and return a different value when appropriate.
        For example when the realm changes in basic authentication it should be
        considered a different authentication attempt and a different value should
        be returned.

        :   **Returns:**: String a String identifying the authentication challenge. The returned value may be null.

---



### isConnectionBased

```
boolean isConnectionBased()
```

:   Tests if the authentication scheme is provides authorization on a per
    connection basis instead of usual per request basis

    :   **Returns:**: true if the scheme is connection based, false if the scheme is request based. **Since:** : 3.0

---



### isComplete

```
boolean isComplete()
```

:   Authentication process may involve a series of challenge-response exchanges.
    This method tests if the authorization process has been completed, either
    successfully or unsuccessfully, that is, all the required authorization
    challenges have been processed in their entirety.

    :   **Returns:**: true if the authentication process has been completed, false otherwise. **Since:** : 3.0

---



### authenticate

```
String authenticate(Credentials credentials,
                    String method,
                    String uri)
                    throws AuthenticationException
```

:   **Deprecated.** *Use [`authenticate(Credentials, HttpMethod)`](../../../../../org/apache/commons/httpclient/auth/AuthScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod))
    Produces an authorization string for the given set of [`Credentials`](../../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient"),
    method name and URI using the given authentication scheme in response to
    the actual authorization challenge.*

    :   **Parameters:**: `credentials` - The set of credentials to be used for athentication: `method` - The name of the method that requires authorization. This parameter may be ignored, if it is irrelevant or not applicable to the given authentication scheme: `uri` - The URI for which authorization is needed. This parameter may be ignored, if it is irrelevant or not applicable to the given authentication scheme **Returns:**: the authorization string **Throws:**: `AuthenticationException` - if authorization string cannot be generated due to an authentication failure **See Also:**: [`HttpMethod.getName()`](../../../../../org/apache/commons/httpclient/HttpMethod.html#getName()), [`HttpMethod.getPath()`](../../../../../org/apache/commons/httpclient/HttpMethod.html#getPath())

---



### authenticate

```
String authenticate(Credentials credentials,
                    HttpMethod method)
                    throws AuthenticationException
```

:   Produces an authorization string for the given set of [`Credentials`](../../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient").

    :   **Parameters:**: `credentials` - The set of credentials to be used for athentication: `method` - The method being authenticated **Returns:**: the authorization string **Throws:**: `AuthenticationException` - if authorization string cannot be generated due to an authentication failure **Since:** : 3.0



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/AuthScheme.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthPolicy.html "class in org.apache.commons.httpclient.auth")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/auth/AuthSchemeBase.html "class in org.apache.commons.httpclient.auth") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/auth/AuthScheme.html)    [**NO FRAMES**](AuthScheme.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
## Issue Tracking

This project uses an Issue Management System to manage its issues.

Issues, bugs, and feature requests for this project should be submitted to the following issue tracking system:

```
http://issues.apache.org/jira/browse/HTTPCLIENT
```

---
## Web Access

This is a link to the online source repository that can be viewed via a web browser:

```
http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/
```

## Source Repository

This project uses
[Subversion](http://subversion.tigris.org/ "External Link")
to manage its source code. Instructions for using Subversion can be found at
[http://svnbook.red-bean.com/](http://svnbook.red-bean.com/ "External Link").

### Anonymous Access with Maven

This project's source can be checked out anonymously from SVN with the following instruction set on a single line:

```
      maven scm:checkout
        -Dmaven.scm.method=svn
        -Dmaven.scm.url=scm:svn:http://svn.apache.org/repos/asf/httpcomponents/oac.hc3x/trunk
        -Dmaven.scm.checkout.dir=commons-httpclient
```

### Anonymous Access

This project's source can be checked out anonymously from SVN with the following command:

```
svn checkout http://svn.apache.org/repos/asf/httpcomponents/oac.hc3x/trunk commons-httpclient
```

### Developer Access with Maven

Even though everyone can checkout the Subversion repository via HTTPS, committers have to use HTTPS if they want to be able to check back in their changes. Use the following instruction set on a single line:

```
      maven scm:checkout
        -Dmaven.scm.method=svn
        -Dmaven.scm.url=scm:svn:https://svn.apache.org/repos/asf/httpcomponents/oac.hc3x/trunk
        -Dmaven.scm.checkout.dir=commons-httpclient
```

### Developer Access

Even though everyone can checkout the Subversion repository via HTTPS, committers have to use HTTPS if they want to be able to check back in their changes. Use the following command:

```
svn checkout https://svn.apache.org/repos/asf/httpcomponents/oac.hc3x/trunk commons-httpclient
```

### Access from behind a firewall

For those users who are stuck behind a corporate firewall which is blocking http access to the Subversion repository, you can try to access it via the developer connection:

```
svn checkout https://svn.apache.org/repos/asf/httpcomponents/oac.hc3x/trunk commons-httpclient
```

### Access through a proxy

The Subversion client can go through a proxy, if you configure it to do so. First, edit your "servers" configuration file to indicate which proxy to use. The files location depends on your operating system. On Linux or Unix it is located in the directory "~/.subversion". On Windows it is in "%APPDATA%\Subversion". (Try "echo %APPDATA%", note this is a hidden directory.)

There are comments in the file explaining what to do. If you don't have that file, get the latest Subversion client and run any command; this will cause the configuration directory and template files to be created.

Example : Edit the 'servers' file and add something like:

```
[global]
http-proxy-host = your.proxy.name
http-proxy-port = 3128
```

---
## The Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Name | Id | Email | Organization | Roles | TZ Offset | Time |
| --- | --- | --- | --- | --- | --- | --- |
| Michael Becke | mbecke | [mbecke -at- apache.org](mailto:mbecke -at- apache.org) |  | Java Developer   Release Prime |  | Unknown |
| Jeff Dever | jsdever | [jsdever -at- apache.org](mailto:jsdever -at- apache.org) | Independent consultant | 2.0 Release Prime   Java Developer |  | Unknown |
| dIon Gillard | dion | [dion -at- apache.org](mailto:dion -at- apache.org) | Multitask Consulting | Java Developer |  | Unknown |
| [Ortwin Glueck](http://www.odi.ch/ "External Link") | oglueck | [oglueck -at- apache.org](mailto:oglueck -at- apache.org) |  | Java Developer |  | Unknown |
| Sung-Gu | jericho | [jericho -at- apache.org](mailto:jericho -at- apache.org) |  | Java Developer |  | Unknown |
| Oleg Kalnichevski | olegk | [olegk -at- apache.org](mailto:olegk -at- apache.org) |  | Java Developer |  | Unknown |
| Sean C. Sullivan | sullis | [sullis -at- apache.org](mailto:sullis -at- apache.org) | Independent consultant | Java Developer |  | Unknown |
| Adrian Sutton | adrian | [adrian.sutton -at- ephox.com](mailto:adrian.sutton -at- ephox.com) | Intencha | Java Developer |  | Unknown |
| Rodney Waldhoff | rwaldhoff | [rwaldhoff -at- apache](mailto:rwaldhoff -at- apache) | Britannica | Java Developer |  | Unknown |

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Name | Email | Organization | Roles | TZ Offset | Time |
| --- | --- | --- | --- | --- | --- |
| Armando Anton | [armando.anton -at- newknow.com](mailto:armando.anton -at- newknow.com) |  |  |  | Unknown |
| Sebastian Bazley | [sebb -at- apache.org](mailto:sebb -at- apache.org) |  |  |  | Unknown |
| Ola Berg |  |  |  |  | Unknown |
| Sam Berlin | [sberlin -at- limepeer.com](mailto:sberlin -at- limepeer.com) |  |  |  | Unknown |
| Mike Bowler |  |  |  |  | Unknown |
| Samit Jain | [jain.samit -at- gmail.com](mailto:jain.samit -at- gmail.com) |  |  |  | Unknown |
| Eric Johnson | [eric -at- tibco.com](mailto:eric -at- tibco.com) |  |  |  | Unknown |
| Christian Kohlschuetter | [ck -at- newsclub.de](mailto:ck -at- newsclub.de) |  |  |  | Unknown |
| Ryan Lubke | [Ryan.Lubke -at- Sun.COM](mailto:Ryan.Lubke -at- Sun.COM) |  |  |  | Unknown |
| Sam Maloney | [sam.maloney -at- filogix.com](mailto:sam.maloney -at- filogix.com) |  |  |  | Unknown |
| Rob Di Marco | [rdimarco -at- hmsonline.com](mailto:rdimarco -at- hmsonline.com) |  |  |  | Unknown |
| Juergen Pill | [Juergen.Pill -at- softwareag.com](mailto:Juergen.Pill -at- softwareag.com) |  |  |  | Unknown |
| Mohammad Rezaei | [mohammad.rezaei -at- gs.com](mailto:mohammad.rezaei -at- gs.com) |  |  |  | Unknown |
| Roland Weber | [rolandw -at- apache.org](mailto:rolandw -at- apache.org) |  |  |  | Unknown |
| Laura Werner | [laura -at- lwerner.org](mailto:laura -at- lwerner.org) |  |  |  | Unknown |
| Mikael Wilstrom | [mikael.wikstrom -at- it.su.se](mailto:mikael.wikstrom -at- it.su.se) |  |  |  | Unknown |

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/MultiThreadedHttpConnectionManager.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/NameValuePair.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html)    [**NO FRAMES**](MultiThreadedHttpConnectionManager.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class MultiThreadedHttpConnectionManager

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.MultiThreadedHttpConnectionManager
```

**All Implemented Interfaces:**: [HttpConnectionManager](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient")

---

``` public class MultiThreadedHttpConnectionManager extends Object implements HttpConnectionManager ```

Manages a set of HttpConnections for various HostConfigurations.

**Since:**
:   2.0

**Author:**
:   [Michael Becke](mailto:becke@u.washington.edu), Eric Johnson, [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), Carl A. Dunham

---

| **Field Summary** | |
| --- | --- |
| `static int` | `DEFAULT_MAX_HOST_CONNECTIONS`             The default maximum number of connections allowed per host |
| `static int` | `DEFAULT_MAX_TOTAL_CONNECTIONS`             The default maximum number of connections allowed overall |



| **Constructor Summary** | |
| --- | --- |
| `MultiThreadedHttpConnectionManager()`             No-args constructor |



| **Method Summary** | |
| --- | --- |
| `void` | `closeIdleConnections(long idleTimeout)`             Closes connections that have been idle for at least the given amount of time. |
| `void` | `deleteClosedConnections()`             Deletes all closed connections. |
| `HttpConnection` | `getConnection(HostConfiguration hostConfiguration)`             Gets an HttpConnection for a given host configuration. |
| `HttpConnection` | `getConnection(HostConfiguration hostConfiguration, long timeout)`             **Deprecated.** *Use #getConnectionWithTimeout(HostConfiguration, long)* |
| `int` | `getConnectionsInPool()`             Gets the total number of pooled connections. |
| `int` | `getConnectionsInPool(HostConfiguration hostConfiguration)`             Gets the total number of pooled connections for the given host configuration. |
| `int` | `getConnectionsInUse()`             **Deprecated.** *Use [`getConnectionsInPool()`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInPool())* |
| `int` | `getConnectionsInUse(HostConfiguration hostConfiguration)`             **Deprecated.** *Use [`getConnectionsInPool(HostConfiguration)`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInPool(org.apache.commons.httpclient.HostConfiguration))* |
| `HttpConnection` | `getConnectionWithTimeout(HostConfiguration hostConfiguration, long timeout)`             Gets a connection or waits if one is not available. |
| `int` | `getMaxConnectionsPerHost()`             **Deprecated.** *Use [`HttpConnectionManagerParams.getDefaultMaxConnectionsPerHost()`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#getDefaultMaxConnectionsPerHost()), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `int` | `getMaxTotalConnections()`             **Deprecated.** *Use [`HttpConnectionManagerParams.getMaxTotalConnections()`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#getMaxTotalConnections()), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `HttpConnectionManagerParams` | `getParams()`             Returns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") associated with this connection manager. |
| `boolean` | `isConnectionStaleCheckingEnabled()`             **Deprecated.** *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `void` | `releaseConnection(HttpConnection conn)`             Make the given HttpConnection available for use by other requests. |
| `void` | `setConnectionStaleCheckingEnabled(boolean connectionStaleCheckingEnabled)`             **Deprecated.** *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `void` | `setMaxConnectionsPerHost(int maxHostConnections)`             **Deprecated.** *Use [`HttpConnectionManagerParams.setDefaultMaxConnectionsPerHost(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#setDefaultMaxConnectionsPerHost(int)), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `void` | `setMaxTotalConnections(int maxTotalConnections)`             **Deprecated.** *Use [`HttpConnectionManagerParams.setMaxTotalConnections(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#setMaxTotalConnections(int)), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `void` | `setParams(HttpConnectionManagerParams params)`             Assigns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") for this connection manager. |
| `void` | `shutdown()`             Shuts down the connection manager and releases all resources. |
| `static void` | `shutdownAll()`             Shuts down and cleans up resources used by all instances of MultiThreadedHttpConnectionManager. |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Field Detail** |
| --- |

### DEFAULT\_MAX\_HOST\_CONNECTIONS

```
public static final int DEFAULT_MAX_HOST_CONNECTIONS
```

:   The default maximum number of connections allowed per host

    **See Also:**: [Constant Field Values](../../../../constant-values.html#org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.DEFAULT_MAX_HOST_CONNECTIONS)

---



### DEFAULT\_MAX\_TOTAL\_CONNECTIONS

```
public static final int DEFAULT_MAX_TOTAL_CONNECTIONS
```

:   The default maximum number of connections allowed overall

    **See Also:**: [Constant Field Values](../../../../constant-values.html#org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.DEFAULT_MAX_TOTAL_CONNECTIONS)



| **Constructor Detail** |
| --- |

### MultiThreadedHttpConnectionManager

```
public MultiThreadedHttpConnectionManager()
```

:   No-args constructor



| **Method Detail** |
| --- |

### shutdownAll

```
public static void shutdownAll()
```

:   Shuts down and cleans up resources used by all instances of
    MultiThreadedHttpConnectionManager. All static resources are released, all threads are
    stopped, and [`shutdown()`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#shutdown()) is called on all live instances of
    MultiThreadedHttpConnectionManager.

    :   **See Also:**: [`shutdown()`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#shutdown())

---



### shutdown

```
public void shutdown()
```

:   Shuts down the connection manager and releases all resources. All connections associated
    with this class will be closed and released.

    The connection manager can no longer be used once shut down.

    Calling this method more than once will have no effect.

---



### isConnectionStaleCheckingEnabled

```
public boolean isConnectionStaleCheckingEnabled()
```

:   **Deprecated.** *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Gets the staleCheckingEnabled value to be set on HttpConnections that are created.

        :   **Returns:**: `true` if stale checking will be enabled on HttpConnections **See Also:**: [`HttpConnection.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/HttpConnection.html#isStaleCheckingEnabled())

---



### setConnectionStaleCheckingEnabled

```
public void setConnectionStaleCheckingEnabled(boolean connectionStaleCheckingEnabled)
```

:   **Deprecated.** *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Sets the staleCheckingEnabled value to be set on HttpConnections that are created.

        :   **Parameters:**: `connectionStaleCheckingEnabled` - `true` if stale checking will be enabled on HttpConnections **See Also:**: [`HttpConnection.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/HttpConnection.html#setStaleCheckingEnabled(boolean))

---



### setMaxConnectionsPerHost

```
public void setMaxConnectionsPerHost(int maxHostConnections)
```

:   **Deprecated.** *Use [`HttpConnectionManagerParams.setDefaultMaxConnectionsPerHost(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#setDefaultMaxConnectionsPerHost(int)),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Sets the maximum number of connections allowed for a given
        HostConfiguration. Per RFC 2616 section 8.1.4, this value defaults to 2.

        :   **Parameters:**: `maxHostConnections` - the number of connections allowed for each hostConfiguration

---



### getMaxConnectionsPerHost

```
public int getMaxConnectionsPerHost()
```

:   **Deprecated.** *Use [`HttpConnectionManagerParams.getDefaultMaxConnectionsPerHost()`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#getDefaultMaxConnectionsPerHost()),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Gets the maximum number of connections allowed for a given
        hostConfiguration.

        :   **Returns:**: The maximum number of connections allowed for a given hostConfiguration.

---



### setMaxTotalConnections

```
public void setMaxTotalConnections(int maxTotalConnections)
```

:   **Deprecated.** *Use [`HttpConnectionManagerParams.setMaxTotalConnections(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#setMaxTotalConnections(int)),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Sets the maximum number of connections allowed for this connection manager.

        :   **Parameters:**: `maxTotalConnections` - the maximum number of connections allowed

---



### getMaxTotalConnections

```
public int getMaxTotalConnections()
```

:   **Deprecated.** *Use [`HttpConnectionManagerParams.getMaxTotalConnections()`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#getMaxTotalConnections()),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Gets the maximum number of connections allowed for this connection manager.

        :   **Returns:**: The maximum number of connections allowed

---



### getConnection

```
public HttpConnection getConnection(HostConfiguration hostConfiguration)
```

:   **Description copied from interface: `HttpConnectionManager`**
:   Gets an HttpConnection for a given host configuration. If a connection is
    not available this method will block until one is.
    The connection manager should be registered with any HttpConnection that
    is created.

    :   **Specified by:**: `getConnection` in interface `HttpConnectionManager`
    :   **Parameters:**: `hostConfiguration` - the host configuration to use to configure the connection **Returns:**: an HttpConnection for the given configuration **See Also:**: [`HttpConnectionManager.getConnection(HostConfiguration)`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getConnection(org.apache.commons.httpclient.HostConfiguration))

---



### getConnectionWithTimeout

```
public HttpConnection getConnectionWithTimeout(HostConfiguration hostConfiguration,
                                               long timeout)
                                        throws ConnectionPoolTimeoutException
```

:   Gets a connection or waits if one is not available. A connection is
    available if one exists that is not being used or if fewer than
    maxHostConnections have been created in the connectionPool, and fewer
    than maxTotalConnections have been created in all connectionPools.

    :   **Specified by:**: `getConnectionWithTimeout` in interface `HttpConnectionManager`
    :   **Parameters:**: `hostConfiguration` - The host configuration specifying the connection details.: `timeout` - the number of milliseconds to wait for a connection, 0 to wait indefinitely **Returns:**: HttpConnection an available connection **Throws:**: `HttpException` - if a connection does not become available in 'timeout' milliseconds: `ConnectionPoolTimeoutException` - if no connection becomes available before the timeout expires **Since:** : 3.0 **See Also:**: [`HttpConnection.setHttpConnectionManager(HttpConnectionManager)`](../../../../org/apache/commons/httpclient/HttpConnection.html#setHttpConnectionManager(org.apache.commons.httpclient.HttpConnectionManager))

---



### getConnection

```
public HttpConnection getConnection(HostConfiguration hostConfiguration,
                                    long timeout)
                             throws HttpException
```

:   **Deprecated.** *Use #getConnectionWithTimeout(HostConfiguration, long)*

    :   **Description copied from interface: `HttpConnectionManager`**
    :   Gets an HttpConnection for a given host configuration. If a connection is
        not available, this method will block for at most the specified number of
        milliseconds or until a connection becomes available.
        The connection manager should be registered with any HttpConnection that
        is created.

        :   **Specified by:**: `getConnection` in interface `HttpConnectionManager`
        :   **Parameters:**: `hostConfiguration` - the host configuration to use to configure the connection: `timeout` - - the time (in milliseconds) to wait for a connection to become available, 0 to specify an infinite timeout **Returns:**: an HttpConnection for the given configuraiton **Throws:**: `HttpException` - if no connection becomes available before the timeout expires **See Also:**: [`HttpConnectionManager.getConnection(HostConfiguration, long)`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getConnection(org.apache.commons.httpclient.HostConfiguration, long))

---



### getConnectionsInPool

```
public int getConnectionsInPool(HostConfiguration hostConfiguration)
```

:   Gets the total number of pooled connections for the given host configuration. This
    is the total number of connections that have been created and are still in use
    by this connection manager for the host configuration. This value will
    not exceed the [`maximum number of connections per
    host`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getMaxConnectionsPerHost()).

    :   **Parameters:**: `hostConfiguration` - The host configuration **Returns:**: The total number of pooled connections

---



### getConnectionsInPool

```
public int getConnectionsInPool()
```

:   Gets the total number of pooled connections. This is the total number of
    connections that have been created and are still in use by this connection
    manager. This value will not exceed the [`maximum number of connections`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getMaxTotalConnections()).

    :   **Returns:**: the total number of pooled connections

---



### getConnectionsInUse

```
public int getConnectionsInUse(HostConfiguration hostConfiguration)
```

:   **Deprecated.** *Use [`getConnectionsInPool(HostConfiguration)`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInPool(org.apache.commons.httpclient.HostConfiguration))*

    :   Gets the number of connections in use for this configuration.

        :   **Parameters:**: `hostConfiguration` - the key that connections are tracked on **Returns:**: the number of connections in use

---



### getConnectionsInUse

```
public int getConnectionsInUse()
```

:   **Deprecated.** *Use [`getConnectionsInPool()`](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInPool())*

    :   Gets the total number of connections in use.

        :   **Returns:**: the total number of connections in use

---



### deleteClosedConnections

```
public void deleteClosedConnections()
```

:   Deletes all closed connections. Only connections currently owned by the connection
    manager are processed.

    :   **Since:**
        :   3.0

        **See Also:**: [`HttpConnection.isOpen()`](../../../../org/apache/commons/httpclient/HttpConnection.html#isOpen())

---



### closeIdleConnections

```
public void closeIdleConnections(long idleTimeout)
```

:   **Description copied from interface: `HttpConnectionManager`**
:   Closes connections that have been idle for at least the given amount of time. Only
    connections that are currently owned, not checked out, are subject to idle timeouts.

    :   **Specified by:**: `closeIdleConnections` in interface `HttpConnectionManager`
    :   **Parameters:**: `idleTimeout` - the minimum idle time, in milliseconds, for connections to be closed **Since:** : 3.0

---



### releaseConnection

```
public void releaseConnection(HttpConnection conn)
```

:   Make the given HttpConnection available for use by other requests.
    If another thread is blocked in getConnection() that could use this
    connection, it will be woken up.

    :   **Specified by:**: `releaseConnection` in interface `HttpConnectionManager`
    :   **Parameters:**: `conn` - the HttpConnection to make available.

---



### getParams

```
public HttpConnectionManagerParams getParams()
```

:   Returns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") associated
    with this connection manager.

    :   **Specified by:**: `getParams` in interface `HttpConnectionManager`
    :   **Since:**
        :   3.0

        **See Also:**: [`HttpConnectionManagerParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params")

---



### setParams

```
public void setParams(HttpConnectionManagerParams params)
```

:   Assigns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") for this
    connection manager.

    :   **Specified by:**: `setParams` in interface `HttpConnectionManager`
    :   **Since:**
        :   3.0

        **See Also:**: [`HttpConnectionManagerParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params")



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/MultiThreadedHttpConnectionManager.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/NameValuePair.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html)    [**NO FRAMES**](MultiThreadedHttpConnectionManager.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpConnection.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpClientError.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpConnection.html)    [**NO FRAMES**](HttpConnection.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class HttpConnection

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.HttpConnection
```

---

``` public class HttpConnection extends Object ```

An abstraction of an HTTP [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io") and [`OutputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/OutputStream.html "class or interface in java.io")
pair, together with the relevant attributes.

The following options are set on the socket before getting the input/output
streams in the [`open()`](../../../../org/apache/commons/httpclient/HttpConnection.html#open()) method:

| Socket Method Sockets Option Configuration | | |
| --- | --- | --- |
| [`Socket.setTcpNoDelay(boolean)`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#setTcpNoDelay(boolean) "class or interface in java.net") SO\_NODELAY [`HttpConnectionParams.setTcpNoDelay(boolean)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setTcpNoDelay(boolean)) | | |
| [`Socket.setSoTimeout(int)`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#setSoTimeout(int) "class or interface in java.net") SO\_TIMEOUT [`HttpConnectionParams.setSoTimeout(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setSoTimeout(int)) | | |
| [`Socket.setSendBufferSize(int)`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#setSendBufferSize(int) "class or interface in java.net") SO\_SNDBUF [`HttpConnectionParams.setSendBufferSize(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setSendBufferSize(int)) | | |
| [`Socket.setReceiveBufferSize(int)`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#setReceiveBufferSize(int) "class or interface in java.net") SO\_RCVBUF [`HttpConnectionParams.setReceiveBufferSize(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setReceiveBufferSize(int)) | | |

**Version:**
:   $Revision: 1425331 $ $Date: 2012-12-22 18:29:41 +0000 (Sat, 22 Dec 2012) $

**Author:**
:   Rod Waldhoff, Sean C. Sullivan, Ortwin Glueck, [Jeff Dever](mailto:jsdever@apache.org), [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), [Oleg Kalnichevski](mailto:oleg@ural.ru), Michael Becke, Eric E Johnson, Laura Werner

---

| **Field Summary** | |
| --- | --- |
| `protected  boolean` | `isOpen`             Whether or not the connection is connected. |



| **Constructor Summary** | |
| --- | --- |
| `HttpConnection(HostConfiguration hostConfiguration)`             Creates a new HTTP connection for the given host configuration. |
| `HttpConnection(String host, int port)`             Creates a new HTTP connection for the given host and port. |
| `HttpConnection(String host, int port, Protocol protocol)`             Creates a new HTTP connection for the given host and port using the given protocol. |
| `HttpConnection(String proxyHost, int proxyPort, String host, int port)`             Creates a new HTTP connection for the given host and port via the given proxy host and port using the default protocol. |
| `HttpConnection(String proxyHost, int proxyPort, String host, int port, Protocol protocol)`             Creates a new HTTP connection for the given host with the virtual alias and port via the given proxy host and port using the given protocol. |
| `HttpConnection(String proxyHost, int proxyPort, String host, String virtualHost, int port, Protocol protocol)`             **Deprecated.** *use #HttpConnection(String, int, String, int, Protocol)* |
| `HttpConnection(String host, String virtualHost, int port, Protocol protocol)`             Creates a new HTTP connection for the given host with the virtual alias and port using given protocol. |



| **Method Summary** | |
| --- | --- |
| `protected  void` | `assertNotOpen()`             Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the connection is already open. |
| `protected  void` | `assertOpen()`             Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the connection is not open. |
| `void` | `close()`             Closes the socket and streams. |
| `boolean` | `closeIfStale()`             Closes the connection if stale. |
| `protected  void` | `closeSocketAndStreams()`             Closes everything out. |
| `void` | `flushRequestOutputStream()`             Flushes the output request stream. |
| `String` | `getHost()`             Returns the host. |
| `HttpConnectionManager` | `getHttpConnectionManager()`             Returns the httpConnectionManager. |
| `InputStream` | `getLastResponseInputStream()`             Returns the stream used to read the last response's body. |
| `InetAddress` | `getLocalAddress()`             Return the local address used when creating the connection. |
| `HttpConnectionParams` | `getParams()`             Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params") associated with this method. |
| `int` | `getPort()`             Returns the port of the host. |
| `Protocol` | `getProtocol()`             Returns the protocol used to establish the connection. |
| `String` | `getProxyHost()`             Returns the proxy host. |
| `int` | `getProxyPort()`             Returns the port of the proxy host. |
| `OutputStream` | `getRequestOutputStream()`             Returns an [`OutputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/OutputStream.html "class or interface in java.io") suitable for writing the request. |
| `InputStream` | `getResponseInputStream()`             Return a [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io") suitable for reading the response. |
| `int` | `getSendBufferSize()`             Gets the socket's sendBufferSize. |
| `protected  Socket` | `getSocket()`             Returns the connection socket. |
| `int` | `getSoTimeout()`             **Deprecated.** *Use [`HttpConnectionParams.getSoTimeout()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#getSoTimeout()), [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| `String` | `getVirtualHost()`             **Deprecated.** *no longer applicable* |
| `protected  boolean` | `isLocked()`             Tests if the connection is locked. |
| `boolean` | `isOpen()`             Tests if the connection is open. |
| `boolean` | `isProxied()`             Returns true if the connection is established via a proxy, false otherwise. |
| `boolean` | `isResponseAvailable()`             Tests if input data avaialble. |
| `boolean` | `isResponseAvailable(int timeout)`             Tests if input data becomes available within the given period time in milliseconds. |
| `boolean` | `isSecure()`             Returns true if the connection is established over a secure protocol. |
| `protected  boolean` | `isStale()`             Determines whether this connection is "stale", which is to say that either it is no longer open, or an attempt to read the connection would fail. |
| `boolean` | `isStaleCheckingEnabled()`             **Deprecated.** *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()), [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| `boolean` | `isTransparent()`             Indicates if the connection is completely transparent from end to end. |
| `void` | `open()`             Establishes a connection to the specified host and port (via a proxy if specified). |
| `void` | `print(String data)`             **Deprecated.** *Use [`print(String, String)`](../../../../org/apache/commons/httpclient/HttpConnection.html#print(java.lang.String, java.lang.String)) Writes the specified String (as bytes) to the output stream.* |
| `void` | `print(String data, String charset)`             Writes the specified String (as bytes) to the output stream. |
| `void` | `printLine()`             Writes "\r\n".getBytes() to the output stream. |
| `void` | `printLine(String data)`             **Deprecated.** *Use [`printLine(String, String)`](../../../../org/apache/commons/httpclient/HttpConnection.html#printLine(java.lang.String, java.lang.String)) Writes the specified String (as bytes), followed by "\r\n".getBytes() to the output stream.* |
| `void` | `printLine(String data, String charset)`             Writes the specified String (as bytes), followed by "\r\n".getBytes() to the output stream. |
| `String` | `readLine()`             **Deprecated.** *use #readLine(String)* |
| `String` | `readLine(String charset)`             Reads up to "\n" from the (unchunked) input stream. |
| `void` | `releaseConnection()`             Releases the connection. |
| `void` | `setConnectionTimeout(int timeout)`             **Deprecated.** *Use [`HttpConnectionParams.setConnectionTimeout(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setConnectionTimeout(int)), [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| `void` | `setHost(String host)`             Sets the host to connect to. |
| `void` | `setHttpConnectionManager(HttpConnectionManager httpConnectionManager)`             Sets the httpConnectionManager. |
| `void` | `setLastResponseInputStream(InputStream inStream)`             Set the state to keep track of the last response for the last request. |
| `void` | `setLocalAddress(InetAddress localAddress)`             Set the local address used when creating the connection. |
| `protected  void` | `setLocked(boolean locked)`             Locks or unlocks the connection. |
| `void` | `setParams(HttpConnectionParams params)`             Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params") for this method. |
| `void` | `setPort(int port)`             Sets the port to connect to. |
| `void` | `setProtocol(Protocol protocol)`             Sets the protocol used to establish the connection |
| `void` | `setProxyHost(String host)`             Sets the host to proxy through. |
| `void` | `setProxyPort(int port)`             Sets the port of the host to proxy through. |
| `void` | `setSendBufferSize(int sendBufferSize)`             **Deprecated.** *Use [`HttpConnectionParams.setSendBufferSize(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setSendBufferSize(int)), [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| `void` | `setSocketTimeout(int timeout)`             Sets `SO_TIMEOUT` value directly on the underlying [`socket`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html "class or interface in java.net"). |
| `void` | `setSoTimeout(int timeout)`             **Deprecated.** *Use [`HttpConnectionParams.setSoTimeout(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setSoTimeout(int)), [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| `void` | `setStaleCheckingEnabled(boolean staleCheckEnabled)`             **Deprecated.** *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)), [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| `void` | `setVirtualHost(String host)`             **Deprecated.** *no longer applicable* |
| `void` | `shutdownOutput()`             **Deprecated.** *unused* |
| `void` | `tunnelCreated()`             Instructs the proxy to establish a secure tunnel to the host. |
| `void` | `write(byte[] data)`             Writes the specified bytes to the output stream. |
| `void` | `write(byte[] data, int offset, int length)`             Writes *length* bytes in *data* starting at *offset* to the output stream. |
| `void` | `writeLine()`             Writes "\r\n".getBytes() to the output stream. |
| `void` | `writeLine(byte[] data)`             Writes the specified bytes, followed by "\r\n".getBytes() to the output stream. |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Field Detail** |
| --- |

### isOpen

```
protected boolean isOpen
```

:   Whether or not the connection is connected.



| **Constructor Detail** |
| --- |

### HttpConnection

```
public HttpConnection(String host,
                      int port)
```

:   Creates a new HTTP connection for the given host and port.

    **Parameters:**: `host` - the host to connect to: `port` - the port to connect to

---



### HttpConnection

```
public HttpConnection(String host,
                      int port,
                      Protocol protocol)
```

:   Creates a new HTTP connection for the given host and port
    using the given protocol.

    **Parameters:**: `host` - the host to connect to: `port` - the port to connect to: `protocol` - the protocol to use

---



### HttpConnection

```
public HttpConnection(String host,
                      String virtualHost,
                      int port,
                      Protocol protocol)
```

:   Creates a new HTTP connection for the given host with the virtual
    alias and port using given protocol.

    **Parameters:**: `host` - the host to connect to: `virtualHost` - the virtual host requests will be sent to: `port` - the port to connect to: `protocol` - the protocol to use

---



### HttpConnection

```
public HttpConnection(String proxyHost,
                      int proxyPort,
                      String host,
                      int port)
```

:   Creates a new HTTP connection for the given host and port via the
    given proxy host and port using the default protocol.

    **Parameters:**: `proxyHost` - the host to proxy via: `proxyPort` - the port to proxy via: `host` - the host to connect to: `port` - the port to connect to

---



### HttpConnection

```
public HttpConnection(HostConfiguration hostConfiguration)
```

:   Creates a new HTTP connection for the given host configuration.

    **Parameters:**: `hostConfiguration` - the host/proxy/protocol to use

---



### HttpConnection

```
public HttpConnection(String proxyHost,
                      int proxyPort,
                      String host,
                      String virtualHost,
                      int port,
                      Protocol protocol)
```

:   **Deprecated.** *use #HttpConnection(String, int, String, int, Protocol)*

    :   Creates a new HTTP connection for the given host with the virtual
        alias and port via the given proxy host and port using the given
        protocol.

        **Parameters:**: `proxyHost` - the host to proxy via: `proxyPort` - the port to proxy via: `host` - the host to connect to. Parameter value must be non-null.: `virtualHost` - No longer applicable.: `port` - the port to connect to: `protocol` - The protocol to use. Parameter value must be non-null.

---



### HttpConnection

```
public HttpConnection(String proxyHost,
                      int proxyPort,
                      String host,
                      int port,
                      Protocol protocol)
```

:   Creates a new HTTP connection for the given host with the virtual
    alias and port via the given proxy host and port using the given
    protocol.

    **Parameters:**: `proxyHost` - the host to proxy via: `proxyPort` - the port to proxy via: `host` - the host to connect to. Parameter value must be non-null.: `port` - the port to connect to: `protocol` - The protocol to use. Parameter value must be non-null.



| **Method Detail** |
| --- |

### getSocket

```
protected Socket getSocket()
```

:   Returns the connection socket.

    :   **Returns:**: the socket. **Since:** : 3.0

---



### getHost

```
public String getHost()
```

:   Returns the host.

    :   **Returns:**: the host.

---



### setHost

```
public void setHost(String host)
             throws IllegalStateException
```

:   Sets the host to connect to.

    :   **Parameters:**: `host` - the host to connect to. Parameter value must be non-null. **Throws:**: `IllegalStateException` - if the connection is already open

---



### getVirtualHost

```
public String getVirtualHost()
```

:   **Deprecated.** *no longer applicable*

    :   Returns the target virtual host.

        :   **Returns:**: the virtual host.

---



### setVirtualHost

```
public void setVirtualHost(String host)
                    throws IllegalStateException
```

:   **Deprecated.** *no longer applicable*

    :   Sets the virtual host to target.

        :   **Parameters:**: `host` - the virtual host name that should be used instead of physical host name when sending HTTP requests. Virtual host name can be set to null if virtual host name is not to be used **Throws:**: `IllegalStateException` - if the connection is already open

---



### getPort

```
public int getPort()
```

:   Returns the port of the host.
    If the port is -1 (or less than 0) the default port for
    the current protocol is returned.

    :   **Returns:**: the port.

---



### setPort

```
public void setPort(int port)
             throws IllegalStateException
```

:   Sets the port to connect to.

    :   **Parameters:**: `port` - the port to connect to **Throws:**: `IllegalStateException` - if the connection is already open

---



### getProxyHost

```
public String getProxyHost()
```

:   Returns the proxy host.

    :   **Returns:**: the proxy host.

---



### setProxyHost

```
public void setProxyHost(String host)
                  throws IllegalStateException
```

:   Sets the host to proxy through.

    :   **Parameters:**: `host` - the host to proxy through. **Throws:**: `IllegalStateException` - if the connection is already open

---



### getProxyPort

```
public int getProxyPort()
```

:   Returns the port of the proxy host.

    :   **Returns:**: the proxy port.

---



### setProxyPort

```
public void setProxyPort(int port)
                  throws IllegalStateException
```

:   Sets the port of the host to proxy through.

    :   **Parameters:**: `port` - the port of the host to proxy through. **Throws:**: `IllegalStateException` - if the connection is already open

---



### isSecure

```
public boolean isSecure()
```

:   Returns true if the connection is established over
    a secure protocol.

    :   **Returns:**: true if connected over a secure protocol.

---



### getProtocol

```
public Protocol getProtocol()
```

:   Returns the protocol used to establish the connection.

    :   **Returns:**: The protocol

---



### setProtocol

```
public void setProtocol(Protocol protocol)
```

:   Sets the protocol used to establish the connection

    :   **Parameters:**: `protocol` - The protocol to use. **Throws:**: `IllegalStateException` - if the connection is already open

---



### getLocalAddress

```
public InetAddress getLocalAddress()
```

:   Return the local address used when creating the connection.
    If null, the default address is used.

    :   **Returns:**: InetAddress the local address to be used when creating Sockets

---



### setLocalAddress

```
public void setLocalAddress(InetAddress localAddress)
```

:   Set the local address used when creating the connection.
    If unset or null, the default address is used.

    :   **Parameters:**: `localAddress` - the local address to use

---



### isOpen

```
public boolean isOpen()
```

:   Tests if the connection is open.

    :   **Returns:**: `true` if the connection is open

---



### closeIfStale

```
public boolean closeIfStale()
                     throws IOException
```

:   Closes the connection if stale.

    :   **Returns:**: `true` if the connection was stale and therefore closed, `false` otherwise. **Throws:**: `IOException` **Since:** : 3.0 **See Also:**: [`isStale()`](../../../../org/apache/commons/httpclient/HttpConnection.html#isStale())

---



### isStaleCheckingEnabled

```
public boolean isStaleCheckingEnabled()
```

:   **Deprecated.** *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()),
    [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).*

    :   Tests if stale checking is enabled.

        :   **Returns:**: `true` if enabled **See Also:**: [`isStale()`](../../../../org/apache/commons/httpclient/HttpConnection.html#isStale())

---



### setStaleCheckingEnabled

```
public void setStaleCheckingEnabled(boolean staleCheckEnabled)
```

:   **Deprecated.** *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)),
    [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).*

    :   Sets whether or not isStale() will be called when testing if this connection is open.

        Setting this flag to `false` will increase performance when reusing
        connections, but it will also make them less reliable. Stale checking ensures that
        connections are viable before they are used. When set to `false` some
        method executions will result in IOExceptions and they will have to be retried.

        :   **Parameters:**: `staleCheckEnabled` - `true` to enable isStale() **See Also:**: [`isStale()`](../../../../org/apache/commons/httpclient/HttpConnection.html#isStale()), [`isOpen()`](../../../../org/apache/commons/httpclient/HttpConnection.html#isOpen())

---



### isStale

```
protected boolean isStale()
                   throws IOException
```

:   Determines whether this connection is "stale", which is to say that either
    it is no longer open, or an attempt to read the connection would fail.

    Unfortunately, due to the limitations of the JREs prior to 1.4, it is
    not possible to test a connection to see if both the read and write channels
    are open - except by reading and writing. This leads to a difficulty when
    some connections leave the "write" channel open, but close the read channel
    and ignore the request. This function attempts to ameliorate that
    problem by doing a test read, assuming that the caller will be doing a
    write followed by a read, rather than the other way around.

    To avoid side-effects, the underlying connection is wrapped by a
    [`BufferedInputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/BufferedInputStream.html "class or interface in java.io"), so although data might be read, what is visible
    to clients of the connection will not change with this call.:   **Returns:**: true if the connection is already closed, or a read would fail. **Throws:**: `IOException` - if the stale connection test is interrupted.

---



### isProxied

```
public boolean isProxied()
```

:   Returns true if the connection is established via a proxy,
    false otherwise.

    :   **Returns:**: true if a proxy is used to establish the connection, false otherwise.

---



### setLastResponseInputStream

```
public void setLastResponseInputStream(InputStream inStream)
```

:   Set the state to keep track of the last response for the last request.

    The connection managers use this to ensure that previous requests are
    properly closed before a new request is attempted. That way, a GET
    request need not be read in its entirety before a new request is issued.
    Instead, this stream can be closed as appropriate.

    :   **Parameters:**: `inStream` - The stream associated with an HttpMethod.

---



### getLastResponseInputStream

```
public InputStream getLastResponseInputStream()
```

:   Returns the stream used to read the last response's body.

    Clients will generally not need to call this function unless
    using HttpConnection directly, instead of calling [`HttpClient.executeMethod(org.apache.commons.httpclient.HttpMethod)`](../../../../org/apache/commons/httpclient/HttpClient.html#executeMethod(org.apache.commons.httpclient.HttpMethod)).
    For those clients, call this function, and if it returns a non-null stream,
    close the stream before attempting to execute a method. Note that
    calling "close" on the stream returned by this function *may* close
    the connection if the previous response contained a "Connection: close" header.

    :   **Returns:**: An [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io") corresponding to the body of the last response.

---



### getParams

```
public HttpConnectionParams getParams()
```

:   Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params") associated with this method.

    :   **Returns:**: HTTP parameters. **Since:** : 3.0

---



### setParams

```
public void setParams(HttpConnectionParams params)
```

:   Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params") for this method.

    :   **Since:**
        :   3.0

        **See Also:**: [`HttpConnectionParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params")

---



### setSoTimeout

```
public void setSoTimeout(int timeout)
                  throws SocketException,
                         IllegalStateException
```

:   **Deprecated.** *Use [`HttpConnectionParams.setSoTimeout(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setSoTimeout(int)),
    [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).*

    :   Set the [`Socket`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html "class or interface in java.net")'s timeout, via [`Socket.setSoTimeout(int)`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#setSoTimeout(int) "class or interface in java.net"). If the
        connection is already open, the SO\_TIMEOUT is changed. If no connection
        is open, then subsequent connections will use the timeout value.

        Note: This is not a connection timeout but a timeout on network traffic!

        :   **Parameters:**: `timeout` - the timeout value **Throws:**: `SocketException` - - if there is an error in the underlying protocol, such as a TCP error.: `IllegalStateException`

---



### setSocketTimeout

```
public void setSocketTimeout(int timeout)
                      throws SocketException,
                             IllegalStateException
```

:   Sets `SO_TIMEOUT` value directly on the underlying [`socket`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html "class or interface in java.net").
    This method does not change the default read timeout value set via
    [`HttpConnectionParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params").

    :   **Parameters:**: `timeout` - the timeout value **Throws:**: `SocketException` - - if there is an error in the underlying protocol, such as a TCP error.: `IllegalStateException` - if not connected **Since:** : 3.0

---



### getSoTimeout

```
public int getSoTimeout()
                 throws SocketException
```

:   **Deprecated.** *Use [`HttpConnectionParams.getSoTimeout()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#getSoTimeout()),
    [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).*

    :   Returns the [`Socket`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html "class or interface in java.net")'s timeout, via [`Socket.getSoTimeout()`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#getSoTimeout() "class or interface in java.net"), if the
        connection is already open. If no connection is open, return the value subsequent
        connection will use.

        Note: This is not a connection timeout but a timeout on network traffic!

        :   **Returns:**: the timeout value **Throws:**: `SocketException`

---



### setConnectionTimeout

```
public void setConnectionTimeout(int timeout)
```

:   **Deprecated.** *Use [`HttpConnectionParams.setConnectionTimeout(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setConnectionTimeout(int)),
    [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).*

    :   Sets the connection timeout. This is the maximum time that may be spent
        until a connection is established. The connection will fail after this
        amount of time.

        :   **Parameters:**: `timeout` - The timeout in milliseconds. 0 means timeout is not used.

---



### open

```
public void open()
          throws IOException
```

:   Establishes a connection to the specified host and port
    (via a proxy if specified).
    The underlying socket is created from the [`ProtocolSocketFactory`](../../../../org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol").

    :   **Throws:**: `IOException` - if an attempt to establish the connection results in an I/O error.

---



### tunnelCreated

```
public void tunnelCreated()
                   throws IllegalStateException,
                          IOException
```

:   Instructs the proxy to establish a secure tunnel to the host. The socket will
    be switched to the secure socket. Subsequent communication is done via the secure
    socket. The method can only be called once on a proxied secure connection.

    :   **Throws:**: `IllegalStateException` - if connection is not secure and proxied or if the socket is already secure.: `IOException` - if an attempt to establish the secure tunnel results in an I/O error.

---



### isTransparent

```
public boolean isTransparent()
```

:   Indicates if the connection is completely transparent from end to end.

    :   **Returns:**: true if conncetion is not proxied or tunneled through a transparent proxy; false otherwise.

---



### flushRequestOutputStream

```
public void flushRequestOutputStream()
                              throws IOException
```

:   Flushes the output request stream. This method should be called to
    ensure that data written to the request OutputStream is sent to the server.

    :   **Throws:**: `IOException` - if an I/O problem occurs

---



### getRequestOutputStream

```
public OutputStream getRequestOutputStream()
                                    throws IOException,
                                           IllegalStateException
```

:   Returns an [`OutputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/OutputStream.html "class or interface in java.io") suitable for writing the request.

    :   **Returns:**: a stream to write the request to **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs

---



### getResponseInputStream

```
public InputStream getResponseInputStream()
                                   throws IOException,
                                          IllegalStateException
```

:   Return a [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io") suitable for reading the response.

    :   **Returns:**: InputStream The response input stream. **Throws:**: `IOException` - If an IO problem occurs: `IllegalStateException` - If the connection isn't open.

---



### isResponseAvailable

```
public boolean isResponseAvailable()
                            throws IOException
```

:   Tests if input data avaialble. This method returns immediately
    and does not perform any read operations on the input socket

    :   **Returns:**: boolean true if input data is available, false otherwise. **Throws:**: `IOException` - If an IO problem occurs: `IllegalStateException` - If the connection isn't open.

---



### isResponseAvailable

```
public boolean isResponseAvailable(int timeout)
                            throws IOException
```

:   Tests if input data becomes available within the given period time in milliseconds.

    :   **Parameters:**: `timeout` - The number milliseconds to wait for input data to become available **Returns:**: boolean true if input data is availble, false otherwise. **Throws:**: `IOException` - If an IO problem occurs: `IllegalStateException` - If the connection isn't open.

---



### write

```
public void write(byte[] data)
           throws IOException,
                  IllegalStateException
```

:   Writes the specified bytes to the output stream.

    :   **Parameters:**: `data` - the data to be written **Throws:**: `IllegalStateException` - if not connected: `IOException` - if an I/O problem occurs **See Also:**: [`write(byte[],int,int)`](../../../../org/apache/commons/httpclient/HttpConnection.html#write(byte[], int, int))

---



### write

```
public void write(byte[] data,
                  int offset,
                  int length)
           throws IOException,
                  IllegalStateException
```

:   Writes *length* bytes in *data* starting at
    *offset* to the output stream.
    The general contract for
    write(b, off, len) is that some of the bytes in the array b are written
    to the output stream in order; element b[off] is the first byte written
    and b[off+len-1] is the last byte written by this operation.

    :   **Parameters:**: `data` - array containing the data to be written.: `offset` - the start offset in the data.: `length` - the number of bytes to write. **Throws:**: `IllegalStateException` - if not connected: `IOException` - if an I/O problem occurs

---



### writeLine

```
public void writeLine(byte[] data)
               throws IOException,
                      IllegalStateException
```

:   Writes the specified bytes, followed by "\r\n".getBytes() to the
    output stream.

    :   **Parameters:**: `data` - the bytes to be written **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs

---



### writeLine

```
public void writeLine()
               throws IOException,
                      IllegalStateException
```

:   Writes "\r\n".getBytes() to the output stream.

    :   **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs

---



### print

```
public void print(String data)
           throws IOException,
                  IllegalStateException
```

:   **Deprecated.** *Use [`print(String, String)`](../../../../org/apache/commons/httpclient/HttpConnection.html#print(java.lang.String, java.lang.String))
    Writes the specified String (as bytes) to the output stream.*

    :   **Parameters:**: `data` - the string to be written **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs

---



### print

```
public void print(String data,
                  String charset)
           throws IOException,
                  IllegalStateException
```

:   Writes the specified String (as bytes) to the output stream.

    :   **Parameters:**: `data` - the string to be written: `charset` - the charset to use for writing the data **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs **Since:** : 3.0

---



### printLine

```
public void printLine(String data)
               throws IOException,
                      IllegalStateException
```

:   **Deprecated.** *Use [`printLine(String, String)`](../../../../org/apache/commons/httpclient/HttpConnection.html#printLine(java.lang.String, java.lang.String))
    Writes the specified String (as bytes), followed by
    "\r\n".getBytes() to the output stream.*

    :   **Parameters:**: `data` - the data to be written **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs

---



### printLine

```
public void printLine(String data,
                      String charset)
               throws IOException,
                      IllegalStateException
```

:   Writes the specified String (as bytes), followed by
    "\r\n".getBytes() to the output stream.

    :   **Parameters:**: `data` - the data to be written: `charset` - the charset to use for writing the data **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs **Since:** : 3.0

---



### printLine

```
public void printLine()
               throws IOException,
                      IllegalStateException
```

:   Writes "\r\n".getBytes() to the output stream.

    :   **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs

---



### readLine

```
public String readLine()
                throws IOException,
                       IllegalStateException
```

:   **Deprecated.** *use #readLine(String)*

    :   Reads up to "\n" from the (unchunked) input stream.
        If the stream ends before the line terminator is found,
        the last part of the string will still be returned.

        :   **Returns:**: a line from the response **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs

---



### readLine

```
public String readLine(String charset)
                throws IOException,
                       IllegalStateException
```

:   Reads up to "\n" from the (unchunked) input stream.
    If the stream ends before the line terminator is found,
    the last part of the string will still be returned.

    :   **Parameters:**: `charset` - the charset to use for reading the data **Returns:**: a line from the response **Throws:**: `IllegalStateException` - if the connection is not open: `IOException` - if an I/O problem occurs **Since:** : 3.0

---



### shutdownOutput

```
public void shutdownOutput()
```

:   **Deprecated.** *unused*

    :   Attempts to shutdown the [`Socket`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html "class or interface in java.net")'s output, via Socket.shutdownOutput()
        when running on JVM 1.3 or higher.

---



### close

```
public void close()
```

:   Closes the socket and streams.

---



### getHttpConnectionManager

```
public HttpConnectionManager getHttpConnectionManager()
```

:   Returns the httpConnectionManager.

    :   **Returns:**: HttpConnectionManager

---



### setHttpConnectionManager

```
public void setHttpConnectionManager(HttpConnectionManager httpConnectionManager)
```

:   Sets the httpConnectionManager.

    :   **Parameters:**: `httpConnectionManager` - The httpConnectionManager to set

---



### releaseConnection

```
public void releaseConnection()
```

:   Releases the connection. If the connection is locked or does not have a connection
    manager associated with it, this method has no effect. Note that it is completely safe
    to call this method multiple times.

---



### isLocked

```
protected boolean isLocked()
```

:   Tests if the connection is locked. Locked connections cannot be released.
    An attempt to release a locked connection will have no effect.

    :   **Returns:**: true if the connection is locked, false otherwise. **Since:** : 3.0

---



### setLocked

```
protected void setLocked(boolean locked)
```

:   Locks or unlocks the connection. Locked connections cannot be released.
    An attempt to release a locked connection will have no effect.

    :   **Parameters:**: `locked` - true to lock the connection, false to unlock the connection. **Since:** : 3.0

---



### closeSocketAndStreams

```
protected void closeSocketAndStreams()
```

:   Closes everything out.

---



### assertNotOpen

```
protected void assertNotOpen()
                      throws IllegalStateException
```

:   Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the connection is already open.

    :   **Throws:**: `IllegalStateException` - if connected

---



### assertOpen

```
protected void assertOpen()
                   throws IllegalStateException
```

:   Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the connection is not open.

    :   **Throws:**: `IllegalStateException` - if not connected

---



### getSendBufferSize

```
public int getSendBufferSize()
                      throws SocketException
```

:   Gets the socket's sendBufferSize.

    :   **Returns:**: the size of the buffer for the socket OutputStream, -1 if the value has not been set and the socket has not been opened **Throws:**: `SocketException` - if an error occurs while getting the socket value **See Also:**: [`Socket.getSendBufferSize()`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#getSendBufferSize() "class or interface in java.net")

---



### setSendBufferSize

```
public void setSendBufferSize(int sendBufferSize)
                       throws SocketException
```

:   **Deprecated.** *Use [`HttpConnectionParams.setSendBufferSize(int)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setSendBufferSize(int)),
    [`getParams()`](../../../../org/apache/commons/httpclient/HttpConnection.html#getParams()).*

    :   Sets the socket's sendBufferSize.

        :   **Parameters:**: `sendBufferSize` - the size to set for the socket OutputStream **Throws:**: `SocketException` - if an error occurs while setting the socket value **See Also:**: [`Socket.setSendBufferSize(int)`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html#setSendBufferSize(int) "class or interface in java.net")



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpConnection.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpClientError.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpConnection.html)    [**NO FRAMES**](HttpConnection.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpConnectionManager.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpConstants.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpConnectionManager.html)    [**NO FRAMES**](HttpConnectionManager.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Interface HttpConnectionManager

**All Known Implementing Classes:**: [MultiThreadedHttpConnectionManager](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html "class in org.apache.commons.httpclient"), [SimpleHttpConnectionManager](../../../../org/apache/commons/httpclient/SimpleHttpConnectionManager.html "class in org.apache.commons.httpclient")

---

``` public interface HttpConnectionManager ```

An interface for classes that manage HttpConnections.

**Since:**
:   2.0

**Author:**
:   Michael Becke, [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), [Oleg Kalnichevski](mailto:oleg@ural.ru)

**See Also:**: [`HttpConnection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"), [`HttpClient.HttpClient(HttpConnectionManager)`](../../../../org/apache/commons/httpclient/HttpClient.html#HttpClient(org.apache.commons.httpclient.HttpConnectionManager))

---

| **Method Summary** | |
| --- | --- |
| `void` | `closeIdleConnections(long idleTimeout)`             Closes connections that have been idle for at least the given amount of time. |
| `HttpConnection` | `getConnection(HostConfiguration hostConfiguration)`             Gets an HttpConnection for a given host configuration. |
| `HttpConnection` | `getConnection(HostConfiguration hostConfiguration, long timeout)`             **Deprecated.** *Use #getConnectionWithTimeout(HostConfiguration, long)* |
| `HttpConnection` | `getConnectionWithTimeout(HostConfiguration hostConfiguration, long timeout)`             Gets an HttpConnection for a given host configuration. |
| `HttpConnectionManagerParams` | `getParams()`             Returns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") associated with this connection manager. |
| `void` | `releaseConnection(HttpConnection conn)`             Releases the given HttpConnection for use by other requests. |
| `void` | `setParams(HttpConnectionManagerParams params)`             Assigns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") for this connection manager. |

| **Method Detail** |
| --- |

### getConnection

```
HttpConnection getConnection(HostConfiguration hostConfiguration)
```

:   Gets an HttpConnection for a given host configuration. If a connection is
    not available this method will block until one is.
    The connection manager should be registered with any HttpConnection that
    is created.

    :   **Parameters:**: `hostConfiguration` - the host configuration to use to configure the connection **Returns:**: an HttpConnection for the given configuration **See Also:**: [`HttpConnection.setHttpConnectionManager(HttpConnectionManager)`](../../../../org/apache/commons/httpclient/HttpConnection.html#setHttpConnectionManager(org.apache.commons.httpclient.HttpConnectionManager))

---



### getConnection

```
HttpConnection getConnection(HostConfiguration hostConfiguration,
                             long timeout)
                             throws HttpException
```

:   **Deprecated.** *Use #getConnectionWithTimeout(HostConfiguration, long)*

    :   Gets an HttpConnection for a given host configuration. If a connection is
        not available, this method will block for at most the specified number of
        milliseconds or until a connection becomes available.
        The connection manager should be registered with any HttpConnection that
        is created.

        :   **Parameters:**: `hostConfiguration` - the host configuration to use to configure the connection: `timeout` - - the time (in milliseconds) to wait for a connection to become available, 0 to specify an infinite timeout **Returns:**: an HttpConnection for the given configuraiton **Throws:**: `HttpException` - if no connection becomes available before the timeout expires **See Also:**: [`HttpConnection.setHttpConnectionManager(HttpConnectionManager)`](../../../../org/apache/commons/httpclient/HttpConnection.html#setHttpConnectionManager(org.apache.commons.httpclient.HttpConnectionManager))

---



### getConnectionWithTimeout

```
HttpConnection getConnectionWithTimeout(HostConfiguration hostConfiguration,
                                        long timeout)
                                        throws ConnectionPoolTimeoutException
```

:   Gets an HttpConnection for a given host configuration. If a connection is
    not available, this method will block for at most the specified number of
    milliseconds or until a connection becomes available.
    The connection manager should be registered with any HttpConnection that
    is created.

    :   **Parameters:**: `hostConfiguration` - the host configuration to use to configure the connection: `timeout` - - the time (in milliseconds) to wait for a connection to become available, 0 to specify an infinite timeout **Returns:**: an HttpConnection for the given configuraiton **Throws:**: `ConnectionPoolTimeoutException` - if no connection becomes available before the timeout expires **Since:** : 3.0 **See Also:**: [`HttpConnection.setHttpConnectionManager(HttpConnectionManager)`](../../../../org/apache/commons/httpclient/HttpConnection.html#setHttpConnectionManager(org.apache.commons.httpclient.HttpConnectionManager))

---



### releaseConnection

```
void releaseConnection(HttpConnection conn)
```

:   Releases the given HttpConnection for use by other requests.

    :   **Parameters:**: `conn` - - The HttpConnection to make available.

---



### closeIdleConnections

```
void closeIdleConnections(long idleTimeout)
```

:   Closes connections that have been idle for at least the given amount of time. Only
    connections that are currently owned, not checked out, are subject to idle timeouts.

    :   **Parameters:**: `idleTimeout` - the minimum idle time, in milliseconds, for connections to be closed **Since:** : 3.0

---



### getParams

```
HttpConnectionManagerParams getParams()
```

:   Returns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") associated
    with this connection manager.

    :   **Since:**
        :   3.0

        **See Also:**: [`HttpConnectionManagerParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params")

---



### setParams

```
void setParams(HttpConnectionManagerParams params)
```

:   Assigns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") for this
    connection manager.

    :   **Since:**
        :   3.0

        **See Also:**: [`HttpConnectionManagerParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params")



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpConnectionManager.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpConstants.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpConnectionManager.html)    [**NO FRAMES**](HttpConnectionManager.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/RequestEntity.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/methods/PutMethod.html "class in org.apache.commons.httpclient.methods")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/methods/StringRequestEntity.html "class in org.apache.commons.httpclient.methods") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/methods/RequestEntity.html)    [**NO FRAMES**](RequestEntity.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient.methods Interface RequestEntity

**All Known Implementing Classes:**: [ByteArrayRequestEntity](../../../../../org/apache/commons/httpclient/methods/ByteArrayRequestEntity.html "class in org.apache.commons.httpclient.methods"), [FileRequestEntity](../../../../../org/apache/commons/httpclient/methods/FileRequestEntity.html "class in org.apache.commons.httpclient.methods"), [InputStreamRequestEntity](../../../../../org/apache/commons/httpclient/methods/InputStreamRequestEntity.html "class in org.apache.commons.httpclient.methods"), [MultipartRequestEntity](../../../../../org/apache/commons/httpclient/methods/multipart/MultipartRequestEntity.html "class in org.apache.commons.httpclient.methods.multipart"), [StringRequestEntity](../../../../../org/apache/commons/httpclient/methods/StringRequestEntity.html "class in org.apache.commons.httpclient.methods")

---

``` public interface RequestEntity ```

**Since:**
:   3.0

---

| **Method Summary** | |
| --- | --- |
| `long` | `getContentLength()`             Gets the request entity's length. |
| `String` | `getContentType()`             Gets the entity's content type. |
| `boolean` | `isRepeatable()`             Tests if [`writeRequest(OutputStream)`](../../../../../org/apache/commons/httpclient/methods/RequestEntity.html#writeRequest(java.io.OutputStream)) can be called more than once. |
| `void` | `writeRequest(OutputStream out)`             Writes the request entity to the given stream. |

| **Method Detail** |
| --- |

### isRepeatable

```
boolean isRepeatable()
```

:   Tests if [`writeRequest(OutputStream)`](../../../../../org/apache/commons/httpclient/methods/RequestEntity.html#writeRequest(java.io.OutputStream)) can be called more than once.

    :   **Returns:**: true if the entity can be written to [`OutputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/OutputStream.html "class or interface in java.io") more than once, false otherwise.

---



### writeRequest

```
void writeRequest(OutputStream out)
                  throws IOException
```

:   Writes the request entity to the given stream.

    :   **Parameters:**: `out` - **Throws:**: `IOException`

---



### getContentLength

```
long getContentLength()
```

:   Gets the request entity's length. This method should return a non-negative value if the content
    length is known or a negative value if it is not. In the latter case the
    [`EntityEnclosingMethod`](../../../../../org/apache/commons/httpclient/methods/EntityEnclosingMethod.html "class in org.apache.commons.httpclient.methods") will use chunk encoding to
    transmit the request entity.

    :   **Returns:**: a non-negative value when content length is known or a negative value when content length is not known

---



### getContentType

```
String getContentType()
```

:   Gets the entity's content type. This content type will be used as the value for the
    "Content-Type" header.

    :   **Returns:**: the entity's content type **See Also:**: [`HttpMethod.setRequestHeader(String, String)`](../../../../../org/apache/commons/httpclient/HttpMethod.html#setRequestHeader(java.lang.String, java.lang.String))



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/RequestEntity.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/methods/PutMethod.html "class in org.apache.commons.httpclient.methods")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/methods/StringRequestEntity.html "class in org.apache.commons.httpclient.methods") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/methods/RequestEntity.html)    [**NO FRAMES**](RequestEntity.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpParams.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/params/HttpParamsFactory.html "interface in org.apache.commons.httpclient.params") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/params/HttpParams.html)    [**NO FRAMES**](HttpParams.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient.params Interface HttpParams

**All Known Implementing Classes:**: [DefaultHttpParams](../../../../../org/apache/commons/httpclient/params/DefaultHttpParams.html "class in org.apache.commons.httpclient.params"), [HostParams](../../../../../org/apache/commons/httpclient/params/HostParams.html "class in org.apache.commons.httpclient.params"), [HttpClientParams](../../../../../org/apache/commons/httpclient/params/HttpClientParams.html "class in org.apache.commons.httpclient.params"), [HttpConnectionManagerParams](../../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params"), [HttpConnectionParams](../../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params"), [HttpMethodParams](../../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")

---

``` public interface HttpParams ```

This interface represents a collection of HTTP protocol parameters. Protocol parameters
may be linked together to form a hierarchy. If a particular parameter value has not been
explicitly defined in the collection itself, its value will be drawn from the parent
collection of parameters.

**Since:**
:   3.0

**Version:**
:   $Revision: 1425331 $

**Author:**
:   [Oleg Kalnichevski](mailto:oleg@ural.ru)

---

| **Method Summary** | |
| --- | --- |
| `boolean` | `getBooleanParameter(String name, boolean defaultValue)`             Returns a [`Boolean`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Boolean.html "class or interface in java.lang") parameter value with the given name. |
| `HttpParams` | `getDefaults()`             Returns the parent collection that this collection will defer to for a default value if a particular parameter is not explicitly set in the collection itself |
| `double` | `getDoubleParameter(String name, double defaultValue)`             Returns a [`Double`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Double.html "class or interface in java.lang") parameter value with the given name. |
| `int` | `getIntParameter(String name, int defaultValue)`             Returns an [`Integer`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Integer.html "class or interface in java.lang") parameter value with the given name. |
| `long` | `getLongParameter(String name, long defaultValue)`             Returns a [`Long`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html "class or interface in java.lang") parameter value with the given name. |
| `Object` | `getParameter(String name)`             Returns a parameter value with the given name. |
| `boolean` | `isParameterFalse(String name)`             Returns true if the parameter is either not set or is false, false otherwise. |
| `boolean` | `isParameterSet(String name)`             Returns true if the parameter is set at any level, false otherwise. |
| `boolean` | `isParameterSetLocally(String name)`             Returns true if the parameter is set locally, false otherwise. |
| `boolean` | `isParameterTrue(String name)`             Returns true if the parameter is set and is true, false otherwise. |
| `void` | `setBooleanParameter(String name, boolean value)`             Assigns a [`Boolean`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Boolean.html "class or interface in java.lang") to the parameter with the given name |
| `void` | `setDefaults(HttpParams params)`             Assigns the parent collection that this collection will defer to for a default value if a particular parameter is not explicitly set in the collection itself |
| `void` | `setDoubleParameter(String name, double value)`             Assigns a [`Double`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Double.html "class or interface in java.lang") to the parameter with the given name |
| `void` | `setIntParameter(String name, int value)`             Assigns an [`Integer`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Integer.html "class or interface in java.lang") to the parameter with the given name |
| `void` | `setLongParameter(String name, long value)`             Assigns a [`Long`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html "class or interface in java.lang") to the parameter with the given name |
| `void` | `setParameter(String name, Object value)`             Assigns the value to the parameter with the given name |

| **Method Detail** |
| --- |

### getDefaults

```
HttpParams getDefaults()
```

:   Returns the parent collection that this collection will defer to
    for a default value if a particular parameter is not explicitly
    set in the collection itself

    :   **Returns:**: the parent collection to defer to, if a particular parameter is not explictly set in the collection itself. **See Also:**: [`setDefaults(HttpParams)`](../../../../../org/apache/commons/httpclient/params/HttpParams.html#setDefaults(org.apache.commons.httpclient.params.HttpParams))

---



### setDefaults

```
void setDefaults(HttpParams params)
```

:   Assigns the parent collection that this collection will defer to
    for a default value if a particular parameter is not explicitly
    set in the collection itself

    :   **Parameters:**: `params` - the parent collection to defer to, if a particular parameter is not explictly set in the collection itself. **See Also:**: [`getDefaults()`](../../../../../org/apache/commons/httpclient/params/HttpParams.html#getDefaults())

---



### getParameter

```
Object getParameter(String name)
```

:   Returns a parameter value with the given name. If the parameter is
    not explicitly defined in this collection, its value will be drawn
    from a higer level collection at which this parameter is defined.
    If the parameter is not explicitly set anywhere up the hierarchy,
    null value is returned.

    :   **Parameters:**: `name` - the parent name. **Returns:**: an object that represents the value of the parameter. **See Also:**: [`setParameter(String, Object)`](../../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object))

---



### setParameter

```
void setParameter(String name,
                  Object value)
```

:   Assigns the value to the parameter with the given name

    :   **Parameters:**: `name` - parameter name: `value` - parameter value

---



### getLongParameter

```
long getLongParameter(String name,
                      long defaultValue)
```

:   Returns a [`Long`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html "class or interface in java.lang") parameter value with the given name.
    If the parameter is not explicitly defined in this collection, its
    value will be drawn from a higer level collection at which this parameter
    is defined. If the parameter is not explicitly set anywhere up the hierarchy,
    the default value is returned.

    :   **Parameters:**: `name` - the parent name.: `defaultValue` - the default value. **Returns:**: a [`Long`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html "class or interface in java.lang") that represents the value of the parameter. **See Also:**: [`setLongParameter(String, long)`](../../../../../org/apache/commons/httpclient/params/HttpParams.html#setLongParameter(java.lang.String, long))

---



### setLongParameter

```
void setLongParameter(String name,
                      long value)
```

:   Assigns a [`Long`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html "class or interface in java.lang") to the parameter with the given name

    :   **Parameters:**: `name` - parameter name: `value` - parameter value

---



### getIntParameter

```
int getIntParameter(String name,
                    int defaultValue)
```

:   Returns an [`Integer`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Integer.html "class or interface in java.lang") parameter value with the given name.
    If the parameter is not explicitly defined in this collection, its
    value will be drawn from a higer level collection at which this parameter
    is defined. If the parameter is not explicitly set anywhere up the hierarchy,
    the default value is returned.

    :   **Parameters:**: `name` - the parent name.: `defaultValue` - the default value. **Returns:**: a [`Integer`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Integer.html "class or interface in java.lang") that represents the value of the parameter. **See Also:**: [`setIntParameter(String, int)`](../../../../../org/apache/commons/httpclient/params/HttpParams.html#setIntParameter(java.lang.String, int))

---



### setIntParameter

```
void setIntParameter(String name,
                     int value)
```

:   Assigns an [`Integer`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Integer.html "class or interface in java.lang") to the parameter with the given name

    :   **Parameters:**: `name` - parameter name: `value` - parameter value

---



### getDoubleParameter

```
double getDoubleParameter(String name,
                          double defaultValue)
```

:   Returns a [`Double`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Double.html "class or interface in java.lang") parameter value with the given name.
    If the parameter is not explicitly defined in this collection, its
    value will be drawn from a higer level collection at which this parameter
    is defined. If the parameter is not explicitly set anywhere up the hierarchy,
    the default value is returned.

    :   **Parameters:**: `name` - the parent name.: `defaultValue` - the default value. **Returns:**: a [`Double`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Double.html "class or interface in java.lang") that represents the value of the parameter. **See Also:**: [`setDoubleParameter(String, double)`](../../../../../org/apache/commons/httpclient/params/HttpParams.html#setDoubleParameter(java.lang.String, double))

---



### setDoubleParameter

```
void setDoubleParameter(String name,
                        double value)
```

:   Assigns a [`Double`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Double.html "class or interface in java.lang") to the parameter with the given name

    :   **Parameters:**: `name` - parameter name: `value` - parameter value

---



### getBooleanParameter

```
boolean getBooleanParameter(String name,
                            boolean defaultValue)
```

:   Returns a [`Boolean`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Boolean.html "class or interface in java.lang") parameter value with the given name.
    If the parameter is not explicitly defined in this collection, its
    value will be drawn from a higer level collection at which this parameter
    is defined. If the parameter is not explicitly set anywhere up the hierarchy,
    the default value is returned.

    :   **Parameters:**: `name` - the parent name.: `defaultValue` - the default value. **Returns:**: a [`Boolean`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Boolean.html "class or interface in java.lang") that represents the value of the parameter. **See Also:**: [`setBooleanParameter(String, boolean)`](../../../../../org/apache/commons/httpclient/params/HttpParams.html#setBooleanParameter(java.lang.String, boolean))

---



### setBooleanParameter

```
void setBooleanParameter(String name,
                         boolean value)
```

:   Assigns a [`Boolean`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Boolean.html "class or interface in java.lang") to the parameter with the given name

    :   **Parameters:**: `name` - parameter name: `value` - parameter value

---



### isParameterSet

```
boolean isParameterSet(String name)
```

:   Returns true if the parameter is set at any level, false otherwise.

    :   **Parameters:**: `name` - parameter name **Returns:**: true if the parameter is set at any level, false otherwise.

---



### isParameterSetLocally

```
boolean isParameterSetLocally(String name)
```

:   Returns true if the parameter is set locally, false otherwise.

    :   **Parameters:**: `name` - parameter name **Returns:**: true if the parameter is set locally, false otherwise.

---



### isParameterTrue

```
boolean isParameterTrue(String name)
```

:   Returns true if the parameter is set and is true, false
    otherwise.

    :   **Parameters:**: `name` - parameter name **Returns:**: true if the parameter is set and is true, false otherwise.

---



### isParameterFalse

```
boolean isParameterFalse(String name)
```

:   Returns true if the parameter is either not set or is false,
    false otherwise.

    :   **Parameters:**: `name` - parameter name **Returns:**: true if the parameter is either not set or is false, false otherwise.



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpParams.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/params/HttpParamsFactory.html "interface in org.apache.commons.httpclient.params") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/params/HttpParams.html)    [**NO FRAMES**](HttpParams.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/CookiePolicy.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/cookie/CookiePathComparator.html "class in org.apache.commons.httpclient.cookie")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/cookie/CookiePolicy.html)    [**NO FRAMES**](CookiePolicy.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient.cookie Class CookiePolicy

```
java.lang.Object
  ![extended by ](../../../../../resources/inherit.gif)org.apache.commons.httpclient.cookie.CookiePolicy
```

---

``` public abstract class CookiePolicy extends Object ```

Cookie management policy class. The cookie policy provides corresponding
cookie management interfrace for a given type or version of cookie.

RFC 2109 specification is used per default. Other supported specification
can be chosen when appropriate or set default when desired

The following specifications are provided:

* BROWSER\_COMPATIBILITY: compatible with the common cookie
  management practices (even if they are not 100% standards compliant)* NETSCAPE: Netscape cookie draft compliant* RFC\_2109: RFC2109 compliant (default)* IGNORE\_COOKIES: do not automcatically process cookies

**Since:**
:   2.0

**Author:**
:   [Oleg Kalnichevski](mailto:oleg@ural.ru), [Mike Bowler](mailto:mbowler@GargoyleSoftware.com)

---

| **Field Summary** | |
| --- | --- |
| `static String` | `BROWSER_COMPATIBILITY`             The policy that provides high degree of compatibilty with common cookie management of popular HTTP agents. |
| `static int` | `COMPATIBILITY`             **Deprecated.** *Use [`BROWSER_COMPATIBILITY`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#BROWSER_COMPATIBILITY)* |
| `static String` | `DEFAULT`             The default cookie policy. |
| `static String` | `IGNORE_COOKIES`             The policy that ignores cookies. |
| `protected static Log` | `LOG`             Log object. |
| `static String` | `NETSCAPE`             The Netscape cookie draft compliant policy. |
| `static int` | `NETSCAPE_DRAFT`             **Deprecated.** *Use [`NETSCAPE`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#NETSCAPE)* |
| `static String` | `RFC_2109`             The RFC 2109 compliant policy. |
| `static String` | `RFC_2965`             The RFC 2965 compliant policy. |
| `static int` | `RFC2109`             **Deprecated.** *Use [`RFC_2109`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2109)* |
| `static int` | `RFC2965`             **Deprecated.** *Use [`RFC_2965`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2965)* |



| **Constructor Summary** | |
| --- | --- |
| `CookiePolicy()` |



| **Method Summary** | |
| --- | --- |
| `static CookieSpec` | `getCompatibilitySpec()`             **Deprecated.** *Use [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))* |
| `static CookieSpec` | `getCookieSpec(String id)`             Gets the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") with the given ID. |
| `static int` | `getDefaultPolicy()`             **Deprecated.** *Use [`getDefaultSpec()`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getDefaultSpec())* |
| `static CookieSpec` | `getDefaultSpec()`             Returns [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") registered as [`DEFAULT`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#DEFAULT). |
| `static String[]` | `getRegisteredCookieSpecs()`             Obtains the currently registered cookie policy names. |
| `static CookieSpec` | `getSpecByPolicy(int policy)`             **Deprecated.** *Use [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))* |
| `static CookieSpec` | `getSpecByVersion(int ver)`             **Deprecated.** *Use [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))* |
| `static void` | `registerCookieSpec(String id, Class clazz)`             Registers a new [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") with the given identifier. |
| `static void` | `setDefaultPolicy(int policy)`             **Deprecated.** *Use [`registerCookieSpec(String, Class)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#registerCookieSpec(java.lang.String, java.lang.Class))* |
| `static void` | `unregisterCookieSpec(String id)`             Unregisters the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") with the given ID. |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Field Detail** |
| --- |

### BROWSER\_COMPATIBILITY

```
public static final String BROWSER_COMPATIBILITY
```

:   The policy that provides high degree of compatibilty
    with common cookie management of popular HTTP agents.

    **Since:**
    :   3.0

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.BROWSER_COMPATIBILITY)

---



### NETSCAPE

```
public static final String NETSCAPE
```

:   The Netscape cookie draft compliant policy.

    **Since:**
    :   3.0

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.NETSCAPE)

---



### RFC\_2109

```
public static final String RFC_2109
```

:   The RFC 2109 compliant policy.

    **Since:**
    :   3.0

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.RFC_2109)

---



### RFC\_2965

```
public static final String RFC_2965
```

:   The RFC 2965 compliant policy.

    **Since:**
    :   3.0

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.RFC_2965)

---



### IGNORE\_COOKIES

```
public static final String IGNORE_COOKIES
```

:   The policy that ignores cookies.

    **Since:**
    :   3.0

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.IGNORE_COOKIES)

---



### DEFAULT

```
public static final String DEFAULT
```

:   The default cookie policy.

    **Since:**
    :   3.0

    **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.DEFAULT)

---



### COMPATIBILITY

```
public static final int COMPATIBILITY
```

:   **Deprecated.** *Use [`BROWSER_COMPATIBILITY`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#BROWSER_COMPATIBILITY)*:   The COMPATIBILITY policy provides high compatibilty
        with common cookie management of popular HTTP agents.

        **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.COMPATIBILITY)

---



### NETSCAPE\_DRAFT

```
public static final int NETSCAPE_DRAFT
```

:   **Deprecated.** *Use [`NETSCAPE`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#NETSCAPE)*:   The NETSCAPE\_DRAFT Netscape draft compliant policy.

        **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.NETSCAPE_DRAFT)

---



### RFC2109

```
public static final int RFC2109
```

:   **Deprecated.** *Use [`RFC_2109`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2109)*:   The RFC2109 RFC 2109 compliant policy.

        **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.RFC2109)

---



### RFC2965

```
public static final int RFC2965
```

:   **Deprecated.** *Use [`RFC_2965`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2965)*:   The RFC2965 RFC 2965 compliant policy.

        **See Also:**: [Constant Field Values](../../../../../constant-values.html#org.apache.commons.httpclient.cookie.CookiePolicy.RFC2965)

---



### LOG

```
protected static final Log LOG
```

:   Log object.



| **Constructor Detail** |
| --- |

### CookiePolicy

```
public CookiePolicy()
```



| **Method Detail** |
| --- |

### registerCookieSpec

```
public static void registerCookieSpec(String id,
                                      Class clazz)
```

:   Registers a new [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") with the given identifier.
    If a specification with the given ID already exists it will be overridden.
    This ID is the same one used to retrieve the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie")
    from [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String)).

    :   **Parameters:**: `id` - the identifier for this specification: `clazz` - the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") class to register **Since:** : 3.0 **See Also:**: [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))

---



### unregisterCookieSpec

```
public static void unregisterCookieSpec(String id)
```

:   Unregisters the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") with the given ID.

    :   **Parameters:**: `id` - the ID of the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") to unregister **Since:** : 3.0

---



### getCookieSpec

```
public static CookieSpec getCookieSpec(String id)
                                throws IllegalStateException
```

:   Gets the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") with the given ID.

    :   **Parameters:**: `id` - the [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") ID **Returns:**: [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") **Throws:**: `IllegalStateException` - if a policy with the ID cannot be found **Since:** : 3.0

---



### getDefaultPolicy

```
public static int getDefaultPolicy()
```

:   **Deprecated.** *Use [`getDefaultSpec()`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getDefaultSpec())*

    :   **Returns:**: default cookie policy **See Also:**: [`getDefaultSpec()`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getDefaultSpec())

---



### setDefaultPolicy

```
public static void setDefaultPolicy(int policy)
```

:   **Deprecated.** *Use [`registerCookieSpec(String, Class)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#registerCookieSpec(java.lang.String, java.lang.Class))*

    :   **Parameters:**: `policy` - new default cookie policy **See Also:**: [`DEFAULT`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#DEFAULT)

---



### getSpecByPolicy

```
public static CookieSpec getSpecByPolicy(int policy)
```

:   **Deprecated.** *Use [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))*

    :   **Parameters:**: `policy` - cookie policy to get the CookieSpec for **Returns:**: cookie specification interface for the given policy

---



### getDefaultSpec

```
public static CookieSpec getDefaultSpec()
```

:   Returns [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") registered as [`DEFAULT`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#DEFAULT).
    If no default [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") has been registered,
    [`RFC2109 specification`](../../../../../org/apache/commons/httpclient/cookie/RFC2109Spec.html "class in org.apache.commons.httpclient.cookie") is returned.

    :   **Returns:**: default [`cookie specification`](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") **See Also:**: [`DEFAULT`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#DEFAULT)

---



### getSpecByVersion

```
public static CookieSpec getSpecByVersion(int ver)
```

:   **Deprecated.** *Use [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))*

    :   Gets the CookieSpec for a particular cookie version.

        Supported versions:

        * version 0 corresponds to the Netscape draft* version 1 corresponds to the RFC 2109* Any other cookie value coresponds to the default spec


              :   **Parameters:**: `ver` - the cookie version to get the spec for **Returns:**: cookie specification interface intended for processing cookies with the given version

---



### getCompatibilitySpec

```
public static CookieSpec getCompatibilitySpec()
```

:   **Deprecated.** *Use [`getCookieSpec(String)`](../../../../../org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))*

    :   **Returns:**: cookie specification interface that provides high compatibilty with common cookie management of popular HTTP agents

---



### getRegisteredCookieSpecs

```
public static String[] getRegisteredCookieSpecs()
```

:   Obtains the currently registered cookie policy names.
    Note that the DEFAULT policy (if present) is likely to be the same
    as one of the other policies, but does not have to be.

    :   **Returns:**: array of registered cookie policy names **Since:** : 3.1



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/CookiePolicy.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../../org/apache/commons/httpclient/cookie/CookiePathComparator.html "class in org.apache.commons.httpclient.cookie")   [**NEXT CLASS**](../../../../../org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie") | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient/cookie/CookiePolicy.html)    [**NO FRAMES**](CookiePolicy.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/SimpleHttpConnectionManager.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/RedirectException.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/StatusLine.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/SimpleHttpConnectionManager.html)    [**NO FRAMES**](SimpleHttpConnectionManager.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class SimpleHttpConnectionManager

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.SimpleHttpConnectionManager
```

**All Implemented Interfaces:**: [HttpConnectionManager](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient")

---

``` public class SimpleHttpConnectionManager extends Object implements HttpConnectionManager ```

A connection manager that provides access to a single HttpConnection. This
manager makes no attempt to provide exclusive access to the contained
HttpConnection.

**Since:**
:   2.0

**Author:**
:   [Michael Becke](mailto:becke@u.washington.edu), Eric Johnson, [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), [Oleg Kalnichevski](mailto:oleg@ural.ru), Laura Werner

---

| **Field Summary** | |
| --- | --- |
| `protected  HttpConnection` | `httpConnection`             The http connection |



| **Constructor Summary** | |
| --- | --- |
| `SimpleHttpConnectionManager()`             The connection manager created with this constructor will always try to keep the connection open (alive) between consecutive requests. |
| `SimpleHttpConnectionManager(boolean alwaysClose)`             The connection manager created with this constructor will try to keep the connection open (alive) between consecutive requests if the alwaysClose parameter is set to false. |



| **Method Summary** | |
| --- | --- |
| `void` | `closeIdleConnections(long idleTimeout)`             Closes connections that have been idle for at least the given amount of time. |
| `HttpConnection` | `getConnection(HostConfiguration hostConfiguration)`             Gets an HttpConnection for a given host configuration. |
| `HttpConnection` | `getConnection(HostConfiguration hostConfiguration, long timeout)`             **Deprecated.** *Use #getConnectionWithTimeout(HostConfiguration, long)* |
| `HttpConnection` | `getConnectionWithTimeout(HostConfiguration hostConfiguration, long timeout)`             This method always returns the same connection object. |
| `HttpConnectionManagerParams` | `getParams()`             Returns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") associated with this connection manager. |
| `boolean` | `isConnectionStaleCheckingEnabled()`             **Deprecated.** *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `void` | `releaseConnection(HttpConnection conn)`             Releases the given HttpConnection for use by other requests. |
| `void` | `setConnectionStaleCheckingEnabled(boolean connectionStaleCheckingEnabled)`             **Deprecated.** *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)), [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| `void` | `setParams(HttpConnectionManagerParams params)`             Assigns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") for this connection manager. |
| `void` | `shutdown()`             since 3.1 |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Field Detail** |
| --- |

### httpConnection

```
protected HttpConnection httpConnection
```

:   The http connection



| **Constructor Detail** |
| --- |

### SimpleHttpConnectionManager

```
public SimpleHttpConnectionManager(boolean alwaysClose)
```

:   The connection manager created with this constructor will try to keep the
    connection open (alive) between consecutive requests if the alwaysClose
    parameter is set to false. Otherwise the connection manager will
    always close connections upon release.

    **Parameters:**: `alwaysClose` - if set true, the connection manager will always close connections upon release.

---



### SimpleHttpConnectionManager

```
public SimpleHttpConnectionManager()
```

:   The connection manager created with this constructor will always try to keep
    the connection open (alive) between consecutive requests.



| **Method Detail** |
| --- |

### getConnection

```
public HttpConnection getConnection(HostConfiguration hostConfiguration)
```

:   **Description copied from interface: `HttpConnectionManager`**
:   Gets an HttpConnection for a given host configuration. If a connection is
    not available this method will block until one is.
    The connection manager should be registered with any HttpConnection that
    is created.

    :   **Specified by:**: `getConnection` in interface `HttpConnectionManager`
    :   **Parameters:**: `hostConfiguration` - the host configuration to use to configure the connection **Returns:**: an HttpConnection for the given configuration **See Also:**: [`HttpConnectionManager.getConnection(HostConfiguration)`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getConnection(org.apache.commons.httpclient.HostConfiguration))

---



### isConnectionStaleCheckingEnabled

```
public boolean isConnectionStaleCheckingEnabled()
```

:   **Deprecated.** *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Gets the staleCheckingEnabled value to be set on HttpConnections that are created.

        :   **Returns:**: `true` if stale checking will be enabled on HttpConections **See Also:**: [`HttpConnection.isStaleCheckingEnabled()`](../../../../org/apache/commons/httpclient/HttpConnection.html#isStaleCheckingEnabled())

---



### setConnectionStaleCheckingEnabled

```
public void setConnectionStaleCheckingEnabled(boolean connectionStaleCheckingEnabled)
```

:   **Deprecated.** *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)),
    [`HttpConnectionManager.getParams()`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).*

    :   Sets the staleCheckingEnabled value to be set on HttpConnections that are created.

        :   **Parameters:**: `connectionStaleCheckingEnabled` - `true` if stale checking will be enabled on HttpConections **See Also:**: [`HttpConnection.setStaleCheckingEnabled(boolean)`](../../../../org/apache/commons/httpclient/HttpConnection.html#setStaleCheckingEnabled(boolean))

---



### getConnectionWithTimeout

```
public HttpConnection getConnectionWithTimeout(HostConfiguration hostConfiguration,
                                               long timeout)
```

:   This method always returns the same connection object. If the connection is already
    open, it will be closed and the new host configuration will be applied.

    :   **Specified by:**: `getConnectionWithTimeout` in interface `HttpConnectionManager`
    :   **Parameters:**: `hostConfiguration` - The host configuration specifying the connection details.: `timeout` - this parameter has no effect. The connection is always returned immediately. **Returns:**: an HttpConnection for the given configuraiton **Since:** : 3.0 **See Also:**: [`HttpConnection.setHttpConnectionManager(HttpConnectionManager)`](../../../../org/apache/commons/httpclient/HttpConnection.html#setHttpConnectionManager(org.apache.commons.httpclient.HttpConnectionManager))

---



### getConnection

```
public HttpConnection getConnection(HostConfiguration hostConfiguration,
                                    long timeout)
```

:   **Deprecated.** *Use #getConnectionWithTimeout(HostConfiguration, long)*

    :   **Description copied from interface: `HttpConnectionManager`**
    :   Gets an HttpConnection for a given host configuration. If a connection is
        not available, this method will block for at most the specified number of
        milliseconds or until a connection becomes available.
        The connection manager should be registered with any HttpConnection that
        is created.

        :   **Specified by:**: `getConnection` in interface `HttpConnectionManager`
        :   **Parameters:**: `hostConfiguration` - the host configuration to use to configure the connection: `timeout` - - the time (in milliseconds) to wait for a connection to become available, 0 to specify an infinite timeout **Returns:**: an HttpConnection for the given configuraiton **See Also:**: [`HttpConnectionManager.getConnection(HostConfiguration, long)`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#getConnection(org.apache.commons.httpclient.HostConfiguration, long))

---



### releaseConnection

```
public void releaseConnection(HttpConnection conn)
```

:   **Description copied from interface: `HttpConnectionManager`**
:   Releases the given HttpConnection for use by other requests.

    :   **Specified by:**: `releaseConnection` in interface `HttpConnectionManager`
    :   **Parameters:**: `conn` - - The HttpConnection to make available. **See Also:**: [`HttpConnectionManager.releaseConnection(org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpConnectionManager.html#releaseConnection(org.apache.commons.httpclient.HttpConnection))

---



### getParams

```
public HttpConnectionManagerParams getParams()
```

:   Returns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") associated
    with this connection manager.

    :   **Specified by:**: `getParams` in interface `HttpConnectionManager`
    :   **Since:**
        :   2.1

        **See Also:**: [`HttpConnectionManagerParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params")

---



### setParams

```
public void setParams(HttpConnectionManagerParams params)
```

:   Assigns [`parameters`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params") for this
    connection manager.

    :   **Specified by:**: `setParams` in interface `HttpConnectionManager`
    :   **Since:**
        :   2.1

        **See Also:**: [`HttpConnectionManagerParams`](../../../../org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params")

---



### closeIdleConnections

```
public void closeIdleConnections(long idleTimeout)
```

:   **Description copied from interface: `HttpConnectionManager`**
:   Closes connections that have been idle for at least the given amount of time. Only
    connections that are currently owned, not checked out, are subject to idle timeouts.

    :   **Specified by:**: `closeIdleConnections` in interface `HttpConnectionManager`
    :   **Parameters:**: `idleTimeout` - the minimum idle time, in milliseconds, for connections to be closed **Since:** : 3.0

---



### shutdown

```
public void shutdown()
```

:   since 3.1



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/SimpleHttpConnectionManager.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/RedirectException.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/StatusLine.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/SimpleHttpConnectionManager.html)    [**NO FRAMES**](SimpleHttpConnectionManager.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/Header.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/Header.html)    [**NO FRAMES**](Header.html) |
| SUMMARY: NESTED | FIELD | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: FIELD | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class Header

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.NameValuePair
      ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.Header
```

**All Implemented Interfaces:**: [Serializable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Serializable.html "class or interface in java.io")

---

``` public class Header extends NameValuePair ```

An HTTP header.

**Version:**
:   $Revision: 1425331 $ $Date: 2012-12-22 18:29:41 +0000 (Sat, 22 Dec 2012) $

**Author:**
:   [Remy Maucherat](mailto:remm@apache.org), [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), [Oleg Kalnichevski](mailto:oleg@ural.ru)

**See Also:**: [Serialized Form](../../../../serialized-form.html#org.apache.commons.httpclient.Header)

---

| **Constructor Summary** | |
| --- | --- |
| `Header()`             Default constructor. |
| `Header(String name, String value)`             Constructor with name and value |
| `Header(String name, String value, boolean isAutogenerated)`             Constructor with name and value |



| **Method Summary** | |
| --- | --- |
| `HeaderElement[]` | `getElements()`             Returns an array of [`HeaderElement`](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient")s constructed from my value. |
| `HeaderElement[]` | `getValues()`             **Deprecated.** *Use #getElements* |
| `boolean` | `isAutogenerated()`             Returns the value of the auto-generated header flag. |
| `String` | `toExternalForm()`             Returns a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang") representation of the header. |
| `String` | `toString()`             Returns a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang") representation of the header. |

| **Methods inherited from class org.apache.commons.httpclient.[NameValuePair](../../../../org/apache/commons/httpclient/NameValuePair.html "class in org.apache.commons.httpclient")** |
| --- |
| `equals, getName, getValue, hashCode, setName, setValue` |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, finalize, getClass, notify, notifyAll, wait, wait, wait` |

| **Constructor Detail** |
| --- |

### Header

```
public Header()
```

:   Default constructor.

---



### Header

```
public Header(String name,
              String value)
```

:   Constructor with name and value

    **Parameters:**: `name` - the header name: `value` - the header value

---



### Header

```
public Header(String name,
              String value,
              boolean isAutogenerated)
```

:   Constructor with name and value

    **Parameters:**: `name` - the header name: `value` - the header value: `isAutogenerated` - true if the header is autogenerated, false otherwise. **Since:** : 3.0



| **Method Detail** |
| --- |

### toExternalForm

```
public String toExternalForm()
```

:   Returns a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang") representation of the header.

    :   **Returns:**: stringHEAD

---



### toString

```
public String toString()
```

:   Returns a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang") representation of the header.

    :   **Overrides:**: `toString` in class `NameValuePair`
    :   **Returns:**: stringHEAD

---



### getValues

```
public HeaderElement[] getValues()
                          throws HttpException
```

:   **Deprecated.** *Use #getElements*

    :   Returns an array of [`HeaderElement`](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient")s
        constructed from my value.

        :   **Returns:**: an array of header elements **Throws:**: `HttpException` - if the header cannot be parsed **See Also:**: [`HeaderElement.parse(java.lang.String)`](../../../../org/apache/commons/httpclient/HeaderElement.html#parse(java.lang.String))

---



### getElements

```
public HeaderElement[] getElements()
```

:   Returns an array of [`HeaderElement`](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient")s
    constructed from my value.

    :   **Returns:**: an array of header elements **Since:** : 3.0 **See Also:**: [`HeaderElement.parseElements(String)`](../../../../org/apache/commons/httpclient/HeaderElement.html#parseElements(java.lang.String))

---



### isAutogenerated

```
public boolean isAutogenerated()
```

:   Returns the value of the auto-generated header flag.

    :   **Returns:**: true if the header is autogenerated, false otherwise. **Since:** : 3.0



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/Header.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/Header.html)    [**NO FRAMES**](Header.html) |
| SUMMARY: NESTED | FIELD | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: FIELD | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HostConfiguration.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpClient.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HostConfiguration.html)    [**NO FRAMES**](HostConfiguration.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class HostConfiguration

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.HostConfiguration
```

**All Implemented Interfaces:**: [Cloneable](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Cloneable.html "class or interface in java.lang")

---

``` public class HostConfiguration extends Object implements Cloneable ```

Holds all of the variables needed to describe an HTTP connection to a host. This includes
remote host, port and protocol, proxy host and port, local address, and virtual host.

**Since:**
:   2.0

**Author:**
:   [Michael Becke](mailto:becke@u.washington.edu), [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), [Oleg Kalnichevski](mailto:oleg@ural.ru), Laura Werner

---

| **Field Summary** | |
| --- | --- |
| `static HostConfiguration` | `ANY_HOST_CONFIGURATION`             A value to represent any host configuration, instead of using something like `null`. |



| **Constructor Summary** | |
| --- | --- |
| `HostConfiguration()`             Constructor for HostConfiguration. |
| `HostConfiguration(HostConfiguration hostConfiguration)`             Copy constructor for HostConfiguration |



| **Method Summary** | |
| --- | --- |
| `Object` | `clone()` |
| `boolean` | `equals(Object o)` |
| `String` | `getHost()`             Returns the host. |
| `String` | `getHostURL()`             Return the host url. |
| `InetAddress` | `getLocalAddress()`             Return the local address to be used when creating connections. |
| `HostParams` | `getParams()`             Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HostParams.html "class in org.apache.commons.httpclient.params") associated with this host. |
| `int` | `getPort()`             Returns the port. |
| `Protocol` | `getProtocol()`             Returns the protocol. |
| `String` | `getProxyHost()`             Returns the proxyHost. |
| `int` | `getProxyPort()`             Returns the proxyPort. |
| `String` | `getVirtualHost()`             **Deprecated.** *use HostParams* |
| `int` | `hashCode()` |
| `boolean` | `hostEquals(HttpConnection connection)`             Tests if the host configuration equals the configuration set on the connection. |
| `boolean` | `isHostSet()`             **Deprecated.** *no longer used* |
| `boolean` | `isProxySet()`             **Deprecated.** *no longer used* |
| `boolean` | `proxyEquals(HttpConnection connection)`             Tests if the proxy configuration equals the configuration set on the connection. |
| `void` | `setHost(HttpHost host)`             Sets the given host |
| `void` | `setHost(String host)`             Set the given host. |
| `void` | `setHost(String host, int port)`             Sets the given host and port. |
| `void` | `setHost(String host, int port, Protocol protocol)`             Sets the given host, port and protocol. |
| `void` | `setHost(String host, int port, String protocol)`             Sets the given host, port and protocol |
| `void` | `setHost(String host, String virtualHost, int port, Protocol protocol)`             **Deprecated.** *#setHost(String, int, Protocol)* |
| `void` | `setHost(URI uri)`             Sets the protocol, host and port from the given URI. |
| `void` | `setLocalAddress(InetAddress localAddress)`             Set the local address to be used when creating connections. |
| `void` | `setParams(HostParams params)`             Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HostParams.html "class in org.apache.commons.httpclient.params") specific to this host. |
| `void` | `setProxy(String proxyHost, int proxyPort)`             Set the proxy settings. |
| `void` | `setProxyHost(ProxyHost proxyHost)`             Sets the given proxy host |
| `String` | `toString()` |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `finalize, getClass, notify, notifyAll, wait, wait, wait` |

| **Field Detail** |
| --- |

### ANY\_HOST\_CONFIGURATION

```
public static final HostConfiguration ANY_HOST_CONFIGURATION
```

:   A value to represent any host configuration, instead of using something like
    `null`. This value should be treated as immutable and only used in
    lookups and other such places to represent "any" host config.



| **Constructor Detail** |
| --- |

### HostConfiguration

```
public HostConfiguration()
```

:   Constructor for HostConfiguration.

---



### HostConfiguration

```
public HostConfiguration(HostConfiguration hostConfiguration)
```

:   Copy constructor for HostConfiguration

    **Parameters:**: `hostConfiguration` - the hostConfiguration to copy



| **Method Detail** |
| --- |

### clone

```
public Object clone()
```

:   **Overrides:**: `clone` in class `Object`
:   **See Also:**: [`Object.clone()`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#clone() "class or interface in java.lang")

---



### toString

```
public String toString()
```

:   **Overrides:**: `toString` in class `Object`
:   **See Also:**: [`Object.toString()`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#toString() "class or interface in java.lang")

---



### hostEquals

```
public boolean hostEquals(HttpConnection connection)
```

:   Tests if the host configuration equals the configuration set on the
    connection. True only if the host, port, protocol, local address and virtual address
    are equal. If no host configuration has been set false will be returned.

    :   **Parameters:**: `connection` - the connection to test against **Returns:**: `true` if the connection's host information equals that of this configuration **See Also:**: [`proxyEquals(HttpConnection)`](../../../../org/apache/commons/httpclient/HostConfiguration.html#proxyEquals(org.apache.commons.httpclient.HttpConnection))

---



### proxyEquals

```
public boolean proxyEquals(HttpConnection connection)
```

:   Tests if the proxy configuration equals the configuration set on the
    connection. True only if the proxyHost and proxyPort are equal.

    :   **Parameters:**: `connection` - the connection to test against **Returns:**: `true` if the connection's proxy information equals that of this configuration **See Also:**: [`hostEquals(HttpConnection)`](../../../../org/apache/commons/httpclient/HostConfiguration.html#hostEquals(org.apache.commons.httpclient.HttpConnection))

---



### isHostSet

```
public boolean isHostSet()
```

:   **Deprecated.** *no longer used*

    :   Returns true if the host is set.

        :   **Returns:**: `true` if the host is set.

---



### setHost

```
public void setHost(HttpHost host)
```

:   Sets the given host

    :   **Parameters:**: `host` - the host

---



### setHost

```
public void setHost(String host,
                    int port,
                    String protocol)
```

:   Sets the given host, port and protocol

    :   **Parameters:**: `host` - the host(IP or DNS name): `port` - The port: `protocol` - The protocol.

---



### setHost

```
public void setHost(String host,
                    String virtualHost,
                    int port,
                    Protocol protocol)
```

:   **Deprecated.** *#setHost(String, int, Protocol)*

    :   Sets the given host, virtual host, port and protocol.

        :   **Parameters:**: `host` - the host(IP or DNS name): `virtualHost` - the virtual host name or `null`: `port` - the host port or -1 to use protocol default: `protocol` - the protocol

---



### setHost

```
public void setHost(String host,
                    int port,
                    Protocol protocol)
```

:   Sets the given host, port and protocol.

    :   **Parameters:**: `host` - the host(IP or DNS name): `port` - The port: `protocol` - the protocol

---



### setHost

```
public void setHost(String host,
                    int port)
```

:   Sets the given host and port. Uses the default protocol "http".

    :   **Parameters:**: `host` - the host(IP or DNS name): `port` - The port

---



### setHost

```
public void setHost(String host)
```

:   Set the given host. Uses the default protocol("http") and its port.

    :   **Parameters:**: `host` - The host(IP or DNS name).

---



### setHost

```
public void setHost(URI uri)
```

:   Sets the protocol, host and port from the given URI.

    :   **Parameters:**: `uri` - the URI.

---



### getHostURL

```
public String getHostURL()
```

:   Return the host url.

    :   **Returns:**: The host url.

---



### getHost

```
public String getHost()
```

:   Returns the host.

    :   **Returns:**: the host(IP or DNS name), or `null` if not set **See Also:**: [`isHostSet()`](../../../../org/apache/commons/httpclient/HostConfiguration.html#isHostSet())

---



### getVirtualHost

```
public String getVirtualHost()
```

:   **Deprecated.** *use HostParams*

    :   Returns the virtual host.

        :   **Returns:**: the virtual host name, or `null` if not set

---



### getPort

```
public int getPort()
```

:   Returns the port.

    :   **Returns:**: the host port, or `-1` if not set **See Also:**: [`isHostSet()`](../../../../org/apache/commons/httpclient/HostConfiguration.html#isHostSet())

---



### getProtocol

```
public Protocol getProtocol()
```

:   Returns the protocol.

    :   **Returns:**: The protocol.

---



### isProxySet

```
public boolean isProxySet()
```

:   **Deprecated.** *no longer used*

    :   Tests if the proxy host/port have been set.

        :   **Returns:**: `true` if a proxy server has been set. **See Also:**: [`setProxy(String, int)`](../../../../org/apache/commons/httpclient/HostConfiguration.html#setProxy(java.lang.String, int))

---



### setProxyHost

```
public void setProxyHost(ProxyHost proxyHost)
```

:   Sets the given proxy host

    :   **Parameters:**: `proxyHost` - the proxy host

---



### setProxy

```
public void setProxy(String proxyHost,
                     int proxyPort)
```

:   Set the proxy settings.

    :   **Parameters:**: `proxyHost` - The proxy host: `proxyPort` - The proxy port

---



### getProxyHost

```
public String getProxyHost()
```

:   Returns the proxyHost.

    :   **Returns:**: the proxy host, or `null` if not set **See Also:**: [`isProxySet()`](../../../../org/apache/commons/httpclient/HostConfiguration.html#isProxySet())

---



### getProxyPort

```
public int getProxyPort()
```

:   Returns the proxyPort.

    :   **Returns:**: the proxy port, or `-1` if not set **See Also:**: [`isProxySet()`](../../../../org/apache/commons/httpclient/HostConfiguration.html#isProxySet())

---



### setLocalAddress

```
public void setLocalAddress(InetAddress localAddress)
```

:   Set the local address to be used when creating connections.
    If this is unset, the default address will be used.
    This is useful for specifying the interface to use on multi-homed or clustered systems.

    :   **Parameters:**: `localAddress` - the local address to use

---



### getLocalAddress

```
public InetAddress getLocalAddress()
```

:   Return the local address to be used when creating connections.
    If this is unset, the default address should be used.

    :   **Returns:**: the local address to be used when creating Sockets, or `null`

---



### getParams

```
public HostParams getParams()
```

:   Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HostParams.html "class in org.apache.commons.httpclient.params") associated with this host.

    :   **Returns:**: HTTP parameters. **Since:** : 3.0

---



### setParams

```
public void setParams(HostParams params)
```

:   Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HostParams.html "class in org.apache.commons.httpclient.params") specific to this host.

    :   **Since:**
        :   3.0

        **See Also:**: [`HostParams`](../../../../org/apache/commons/httpclient/params/HostParams.html "class in org.apache.commons.httpclient.params")

---



### equals

```
public boolean equals(Object o)
```

:   **Overrides:**: `equals` in class `Object`
:   **See Also:**: [`Object.equals(java.lang.Object)`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#equals(java.lang.Object) "class or interface in java.lang")

---



### hashCode

```
public int hashCode()
```

:   **Overrides:**: `hashCode` in class `Object`
:   **See Also:**: [`Object.hashCode()`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#hashCode() "class or interface in java.lang")



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HostConfiguration.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpClient.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HostConfiguration.html)    [**NO FRAMES**](HostConfiguration.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/DefaultHttpMethodRetryHandler.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html)    [**NO FRAMES**](DefaultHttpMethodRetryHandler.html) |
| SUMMARY: NESTED | FIELD | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: FIELD | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class DefaultHttpMethodRetryHandler

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.DefaultHttpMethodRetryHandler
```

**All Implemented Interfaces:**: [HttpMethodRetryHandler](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")

---

``` public class DefaultHttpMethodRetryHandler extends Object implements HttpMethodRetryHandler ```

The default [`HttpMethodRetryHandler`](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") used by [`HttpMethod`](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")s.

**Author:**
:   Michael Becke, [Oleg Kalnichevski](mailto:oleg -at- ural.ru)

---

| **Constructor Summary** | |
| --- | --- |
| `DefaultHttpMethodRetryHandler()`             Creates a new DefaultHttpMethodRetryHandler that retries up to 3 times but does not retry methods that have successfully sent their requests. |
| `DefaultHttpMethodRetryHandler(int retryCount, boolean requestSentRetryEnabled)`             Creates a new DefaultHttpMethodRetryHandler. |



| **Method Summary** | |
| --- | --- |
| `int` | `getRetryCount()` |
| `boolean` | `isRequestSentRetryEnabled()` |
| `boolean` | `retryMethod(HttpMethod method, IOException exception, int executionCount)`             Used `retryCount` and `requestSentRetryEnabled` to determine if the given method should be retried. |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Constructor Detail** |
| --- |

### DefaultHttpMethodRetryHandler

```
public DefaultHttpMethodRetryHandler(int retryCount,
                                     boolean requestSentRetryEnabled)
```

:   Creates a new DefaultHttpMethodRetryHandler.

    **Parameters:**: `retryCount` - the number of times a method will be retried: `requestSentRetryEnabled` - if true, methods that have successfully sent their request will be retried

---



### DefaultHttpMethodRetryHandler

```
public DefaultHttpMethodRetryHandler()
```

:   Creates a new DefaultHttpMethodRetryHandler that retries up to 3 times
    but does not retry methods that have successfully sent their requests.



| **Method Detail** |
| --- |

### retryMethod

```
public boolean retryMethod(HttpMethod method,
                           IOException exception,
                           int executionCount)
```

:   Used `retryCount` and `requestSentRetryEnabled` to determine
    if the given method should be retried.

    :   **Specified by:**: `retryMethod` in interface `HttpMethodRetryHandler`
    :   **Parameters:**: `method` - the method being executed: `exception` - the exception that occurred: `executionCount` - the number of times this method has been unsuccessfully executed **Returns:**: `true` if the method should be retried, `false` otherwise **See Also:**: [`HttpMethodRetryHandler.retryMethod(HttpMethod, IOException, int)`](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html#retryMethod(org.apache.commons.httpclient.HttpMethod, java.io.IOException, int))

---



### isRequestSentRetryEnabled

```
public boolean isRequestSentRetryEnabled()
```

:   **Returns:**: `true` if this handler will retry methods that have successfully sent their request, `false` otherwise

---



### getRetryCount

```
public int getRetryCount()
```

:   **Returns:**: the maximum number of times a method will be retried



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/DefaultHttpMethodRetryHandler.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html)    [**NO FRAMES**](DefaultHttpMethodRetryHandler.html) |
| SUMMARY: NESTED | FIELD | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: FIELD | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpVersion.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpURL.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/InvalidRedirectLocationException.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpVersion.html)    [**NO FRAMES**](HttpVersion.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class HttpVersion

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.HttpVersion
```

**All Implemented Interfaces:**: [Comparable](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Comparable.html "class or interface in java.lang")

---

``` public class HttpVersion extends Object implements Comparable ```

HTTP version, as specified in RFC 2616.

HTTP uses a "<major>.<minor>" numbering scheme to indicate
versions of the protocol. The protocol versioning policy is intended to
allow the sender to indicate the format of a message and its capacity for
understanding further HTTP communication, rather than the features
obtained via that communication. No change is made to the version
number for the addition of message components which do not affect
communication behavior or which only add to extensible field values.
The <minor> number is incremented when the changes made to the
protocol add features which do not change the general message parsing
algorithm, but which may add to the message semantics and imply
additional capabilities of the sender. The <major> number is
incremented when the format of a message within the protocol is
changed. See RFC 2145 [36] for a fuller explanation.

The version of an HTTP message is indicated by an HTTP-Version field
in the first line of the message.

```
     HTTP-Version   = "HTTP" "/" 1*DIGIT "." 1*DIGIT
```

Note that the major and minor numbers MUST be treated as separate
integers and that each MAY be incremented higher than a single digit.
Thus, HTTP/2.4 is a lower version than HTTP/2.13, which in turn is
lower than HTTP/12.3. Leading zeros MUST be ignored by recipients and
MUST NOT be sent.

**Since:**
:   3.0

**Version:**
:   $Revision: 1425331 $ $Date: 2012-12-22 18:29:41 +0000 (Sat, 22 Dec 2012) $

**Author:**
:   [Oleg Kalnichevski](mailto:oleg@ural.ru)

---

| **Field Summary** | |
| --- | --- |
| `static HttpVersion` | `HTTP_0_9`             HTTP protocol version 0.9 |
| `static HttpVersion` | `HTTP_1_0`             HTTP protocol version 1.0 |
| `static HttpVersion` | `HTTP_1_1`             HTTP protocol version 1.1 |



| **Constructor Summary** | |
| --- | --- |
| `HttpVersion(int major, int minor)`             Create an HTTP protocol version designator. |



| **Method Summary** | |
| --- | --- |
| `int` | `compareTo(HttpVersion anotherVer)`             Compares this HTTP protocol version with another one. |
| `int` | `compareTo(Object o)` |
| `boolean` | `equals(HttpVersion version)`             Test if the HTTP protocol version is equal to the given number. |
| `boolean` | `equals(Object obj)` |
| `int` | `getMajor()`             Returns the major version number of the HTTP protocol. |
| `int` | `getMinor()`             Returns the minor version number of the HTTP protocol. |
| `boolean` | `greaterEquals(HttpVersion version)`             Test if the HTTP protocol version is greater or equal to the given number. |
| `int` | `hashCode()` |
| `boolean` | `lessEquals(HttpVersion version)`             Test if the HTTP protocol version is less or equal to the given number. |
| `static HttpVersion` | `parse(String s)`             Parses the textual representation of the given HTTP protocol version. |
| `String` | `toString()` |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, finalize, getClass, notify, notifyAll, wait, wait, wait` |

| **Field Detail** |
| --- |

### HTTP\_0\_9

```
public static final HttpVersion HTTP_0_9
```

:   HTTP protocol version 0.9

---



### HTTP\_1\_0

```
public static final HttpVersion HTTP_1_0
```

:   HTTP protocol version 1.0

---



### HTTP\_1\_1

```
public static final HttpVersion HTTP_1_1
```

:   HTTP protocol version 1.1



| **Constructor Detail** |
| --- |

### HttpVersion

```
public HttpVersion(int major,
                   int minor)
```

:   Create an HTTP protocol version designator.

    **Parameters:**: `major` - the major version number of the HTTP protocol: `minor` - the minor version number of the HTTP protocol **Throws:**: `IllegalArgumentException` - if either major or minor version number is negative



| **Method Detail** |
| --- |

### getMajor

```
public int getMajor()
```

:   Returns the major version number of the HTTP protocol.

    :   **Returns:**: the major version number.

---



### getMinor

```
public int getMinor()
```

:   Returns the minor version number of the HTTP protocol.

    :   **Returns:**: the minor version number.

---



### hashCode

```
public int hashCode()
```

:   **Overrides:**: `hashCode` in class `Object`
:   **See Also:**: [`Object.hashCode()`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#hashCode() "class or interface in java.lang")

---



### equals

```
public boolean equals(Object obj)
```

:   **Overrides:**: `equals` in class `Object`
:   **See Also:**: [`Object.equals(java.lang.Object)`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#equals(java.lang.Object) "class or interface in java.lang")

---



### compareTo

```
public int compareTo(HttpVersion anotherVer)
```

:   Compares this HTTP protocol version with another one.

    :   **Parameters:**: `anotherVer` - the version to be compared with. **Returns:**: a negative integer, zero, or a positive integer as this version is less than, equal to, or greater than the specified version.

---



### compareTo

```
public int compareTo(Object o)
```

:   **Specified by:**: `compareTo` in interface `Comparable`
:   **See Also:**: [`Comparable.compareTo(java.lang.Object)`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Comparable.html#compareTo(T) "class or interface in java.lang")

---



### equals

```
public boolean equals(HttpVersion version)
```

:   Test if the HTTP protocol version is equal to the given number.

    :   **Returns:**: true if HTTP protocol version is given to the given number, false otherwise.

---



### greaterEquals

```
public boolean greaterEquals(HttpVersion version)
```

:   Test if the HTTP protocol version is greater or equal to the given number.

    :   **Returns:**: true if HTTP protocol version is greater or equal given to the given number, false otherwise.

---



### lessEquals

```
public boolean lessEquals(HttpVersion version)
```

:   Test if the HTTP protocol version is less or equal to the given number.

    :   **Returns:**: true if HTTP protocol version is less or equal to given to the given number, false otherwise.

---



### toString

```
public String toString()
```

:   **Overrides:**: `toString` in class `Object`
:   **See Also:**: [`Object.toString()`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#toString() "class or interface in java.lang")

---



### parse

```
public static HttpVersion parse(String s)
                         throws ProtocolException
```

:   Parses the textual representation of the given HTTP protocol version.

    :   **Returns:**: HTTP protocol version. **Throws:**: `ProtocolException` - if the string is not a valid HTTP protocol version.



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpVersion.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpURL.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/InvalidRedirectLocationException.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpVersion.html)    [**NO FRAMES**](HttpVersion.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpMethod.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpHost.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpMethod.html)    [**NO FRAMES**](HttpMethod.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Interface HttpMethod

**All Known Implementing Classes:**: [ConnectMethod](../../../../org/apache/commons/httpclient/ConnectMethod.html "class in org.apache.commons.httpclient"), [DeleteMethod](../../../../org/apache/commons/httpclient/methods/DeleteMethod.html "class in org.apache.commons.httpclient.methods"), [EntityEnclosingMethod](../../../../org/apache/commons/httpclient/methods/EntityEnclosingMethod.html "class in org.apache.commons.httpclient.methods"), [ExpectContinueMethod](../../../../org/apache/commons/httpclient/methods/ExpectContinueMethod.html "class in org.apache.commons.httpclient.methods"), [GetMethod](../../../../org/apache/commons/httpclient/methods/GetMethod.html "class in org.apache.commons.httpclient.methods"), [HeadMethod](../../../../org/apache/commons/httpclient/methods/HeadMethod.html "class in org.apache.commons.httpclient.methods"), [HttpMethodBase](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient"), [MultipartPostMethod](../../../../org/apache/commons/httpclient/methods/MultipartPostMethod.html "class in org.apache.commons.httpclient.methods"), [OptionsMethod](../../../../org/apache/commons/httpclient/methods/OptionsMethod.html "class in org.apache.commons.httpclient.methods"), [PostMethod](../../../../org/apache/commons/httpclient/methods/PostMethod.html "class in org.apache.commons.httpclient.methods"), [PutMethod](../../../../org/apache/commons/httpclient/methods/PutMethod.html "class in org.apache.commons.httpclient.methods"), [TraceMethod](../../../../org/apache/commons/httpclient/methods/TraceMethod.html "class in org.apache.commons.httpclient.methods")

---

``` public interface HttpMethod ```

HttpMethod interface represents a request to be sent via a
[`HTTP connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") and a corresponding response.

**Since:**
:   1.0

**Version:**
:   $Revision: 1425331 $ $Date: 2012-12-22 18:29:41 +0000 (Sat, 22 Dec 2012) $

**Author:**
:   [Remy Maucherat](mailto:remm@apache.org), Rod Waldhoff, [Jeff Dever](jsdever@apache.org), [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), [Oleg Kalnichevski](mailto:oleg@ural.ru)

---

| **Method Summary** | |
| --- | --- |
| `void` | `abort()`             Aborts the execution of the HTTP method. |
| `void` | `addRequestHeader(Header header)`             Adds the specified request header, *not* overwriting any previous value. |
| `void` | `addRequestHeader(String headerName, String headerValue)`             Adds the specified request header, *not* overwriting any previous value. |
| `void` | `addResponseFooter(Header footer)`             Add a footer to this method's response. |
| `int` | `execute(HttpState state, HttpConnection connection)`             Executes this method using the specified `HttpConnection` and `HttpState`. |
| `boolean` | `getDoAuthentication()`             Returns true if the HTTP method should automatically handle HTTP authentication challenges (status code 401, etc.), false otherwise |
| `boolean` | `getFollowRedirects()`             Returns true if the HTTP method should automatically follow HTTP redirects (status code 302, etc.), false otherwise. |
| `AuthState` | `getHostAuthState()`             Returns the target host [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth") |
| `HostConfiguration` | `getHostConfiguration()`             **Deprecated.** *no longer applicable* |
| `String` | `getName()`             Obtains the name of the HTTP method as used in the HTTP request line, for example "GET" or "POST". |
| `HttpMethodParams` | `getParams()`             Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") associated with this method. |
| `String` | `getPath()`             Returns the path of the HTTP method. |
| `AuthState` | `getProxyAuthState()`             Returns the proxy [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth") |
| `String` | `getQueryString()`             Returns the query string of this HTTP method. |
| `Header` | `getRequestHeader(String headerName)`             Gets the request header with the given name. |
| `Header[]` | `getRequestHeaders()`             Returns the current request headers for this HTTP method. |
| `Header[]` | `getRequestHeaders(String headerName)`             Returns the request headers with the given name. |
| `byte[]` | `getResponseBody()`             Returns the response body of the HTTP method, if any, as an array of bytes. |
| `InputStream` | `getResponseBodyAsStream()`             Returns the response body of the HTTP method, if any, as an InputStream. |
| `String` | `getResponseBodyAsString()`             Returns the response body of the HTTP method, if any, as a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang"). |
| `Header` | `getResponseFooter(String footerName)`             Return the specified response footer. |
| `Header[]` | `getResponseFooters()`             Returns the response footers from the most recent execution of this request. |
| `Header` | `getResponseHeader(String headerName)`             Returns the specified response header. |
| `Header[]` | `getResponseHeaders()`             Returns the response headers from the most recent execution of this request. |
| `Header[]` | `getResponseHeaders(String headerName)`             Returns the response headers with the given name. |
| `int` | `getStatusCode()`             Returns the status code associated with the latest response. |
| `StatusLine` | `getStatusLine()`             Returns the Status-Line from the most recent response for this method, or `null` if the method has not been executed. |
| `String` | `getStatusText()`             Returns the status text (or "reason phrase") associated with the latest response. |
| `URI` | `getURI()`             Returns the URI for this method. |
| `boolean` | `hasBeenUsed()`             Returns true if the HTTP method has been already [`executed`](../../../../org/apache/commons/httpclient/HttpMethod.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), but not [`recycled`](../../../../org/apache/commons/httpclient/HttpMethod.html#recycle()). |
| `boolean` | `isRequestSent()`             Returns true if the HTTP has been transmitted to the target server in its entirety, false otherwise. |
| `boolean` | `isStrictMode()`             **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| `void` | `recycle()`             **Deprecated.** *no longer supported and will be removed in the future version of HttpClient* |
| `void` | `releaseConnection()`             Releases the connection being used by this HTTP method. |
| `void` | `removeRequestHeader(Header header)`             Removes the given request header. |
| `void` | `removeRequestHeader(String headerName)`             Removes all request headers with the given name. |
| `void` | `setDoAuthentication(boolean doAuthentication)`             Sets whether or not the HTTP method should automatically handle HTTP authentication challenges (status code 401, etc.) |
| `void` | `setFollowRedirects(boolean followRedirects)`             Sets whether or not the HTTP method should automatically follow HTTP redirects (status code 302, etc.) |
| `void` | `setParams(HttpMethodParams params)`             Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") for this method. |
| `void` | `setPath(String path)`             Sets the path of the HTTP method. |
| `void` | `setQueryString(NameValuePair[] params)`             Sets the query string of this HTTP method. |
| `void` | `setQueryString(String queryString)`             Sets the query string of the HTTP method. |
| `void` | `setRequestHeader(Header header)`             Sets the specified request header, overwriting any previous value. |
| `void` | `setRequestHeader(String headerName, String headerValue)`             Sets the specified request header, overwriting any previous value. |
| `void` | `setStrictMode(boolean strictMode)`             **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| `void` | `setURI(URI uri)`             Sets the URI for this method. |
| `boolean` | `validate()`             Returns true the method is ready to execute, false otherwise. |

| **Method Detail** |
| --- |

### getName

```
String getName()
```

:   Obtains the name of the HTTP method as used in the HTTP request line,
    for example "GET" or "POST".

    :   **Returns:**: the name of this method

---



### getHostConfiguration

```
HostConfiguration getHostConfiguration()
```

:   **Deprecated.** *no longer applicable*

    :   Gets the host configuration for this method. The configuration specifies
        the server, port, protocol, and proxy server via which this method will
        send its HTTP request.

        :   **Returns:**: the HostConfiguration or `null` if none is set

---



### setPath

```
void setPath(String path)
```

:   Sets the path of the HTTP method.
    It is responsibility of the caller to ensure that the path is
    properly encoded (URL safe).

    :   **Parameters:**: `path` - The path of the HTTP method. The path is expected to be URL encoded.

---



### getPath

```
String getPath()
```

:   Returns the path of the HTTP method.
    Calling this method *after* the request has been executed will
    return the *actual* path, following any redirects automatically
    handled by this HTTP method.

    :   **Returns:**: the path of the HTTP method, in URL encoded form

---



### getURI

```
URI getURI()
           throws URIException
```

:   Returns the URI for this method. The URI will be absolute if the host
    configuration has been set and relative otherwise.

    :   **Returns:**: the URI for this method **Throws:**: `URIException` - if a URI cannot be constructed

---



### setURI

```
void setURI(URI uri)
            throws URIException
```

:   Sets the URI for this method.

    :   **Parameters:**: `uri` - URI to be set **Throws:**: `URIException` - if a URI cannot be set **Since:** : 3.0

---



### setStrictMode

```
void setStrictMode(boolean strictMode)
```

:   **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object))
    to exercise a more granular control over HTTP protocol strictness.*

    :   Defines how strictly the method follows the HTTP protocol specification.
        (See RFC 2616 and other relevant RFCs.) In the strict mode the method precisely
        implements the requirements of the specification, whereas in non-strict mode
        it attempts to mimic the exact behaviour of commonly used HTTP agents,
        which many HTTP servers expect.

        :   **Parameters:**: `strictMode` - true for strict mode, false otherwise **See Also:**: [`isStrictMode()`](../../../../org/apache/commons/httpclient/HttpMethod.html#isStrictMode())

---



### isStrictMode

```
boolean isStrictMode()
```

:   **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object))
    to exercise a more granular control over HTTP protocol strictness.*

    :   Returns the value of the strict mode flag.

        :   **Returns:**: true if strict mode is enabled, false otherwise **See Also:**: [`setStrictMode(boolean)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setStrictMode(boolean))

---



### setRequestHeader

```
void setRequestHeader(String headerName,
                      String headerValue)
```

:   Sets the specified request header, overwriting any
    previous value.
    Note that header-name matching is case insensitive.

    :   **Parameters:**: `headerName` - the header's name: `headerValue` - the header's value **See Also:**: [`setRequestHeader(Header)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setRequestHeader(org.apache.commons.httpclient.Header)), [`getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### setRequestHeader

```
void setRequestHeader(Header header)
```

:   Sets the specified request header, overwriting any
    previous value.
    Note that header-name matching is case insensitive.

    :   **Parameters:**: `header` - the header to be set **See Also:**: [`setRequestHeader(String,String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setRequestHeader(java.lang.String, java.lang.String)), [`getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### addRequestHeader

```
void addRequestHeader(String headerName,
                      String headerValue)
```

:   Adds the specified request header, *not* overwriting any previous value.
    If the same header is added multiple times, perhaps with different values,
    multiple instances of that header will be sent in the HTTP request.
    Note that header-name matching is case insensitive.

    :   **Parameters:**: `headerName` - the header's name: `headerValue` - the header's value **See Also:**: [`addRequestHeader(Header)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(org.apache.commons.httpclient.Header)), [`getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### addRequestHeader

```
void addRequestHeader(Header header)
```

:   Adds the specified request header, *not* overwriting any previous value.
    If the same header is added multiple times, perhaps with different values,
    multiple instances of that header will be sent in the HTTP request.
    Note that header-name matching is case insensitive.

    :   **Parameters:**: `header` - the header **See Also:**: [`addRequestHeader(String,String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(java.lang.String, java.lang.String)), [`getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### getRequestHeader

```
Header getRequestHeader(String headerName)
```

:   Gets the request header with the given name.
    If there are multiple headers with the same name,
    there values will be combined with the ',' separator as specified by RFC2616.
    Note that header-name matching is case insensitive.

    :   **Parameters:**: `headerName` - the header name **Returns:**: the header

---



### removeRequestHeader

```
void removeRequestHeader(String headerName)
```

:   Removes all request headers with the given name.
    Note that header-name matching is case insensitive.

    :   **Parameters:**: `headerName` - the header name

---



### removeRequestHeader

```
void removeRequestHeader(Header header)
```

:   Removes the given request header.

    :   **Parameters:**: `header` - the header **Since:** : 3.0

---



### getFollowRedirects

```
boolean getFollowRedirects()
```

:   Returns true if the HTTP method should automatically follow HTTP redirects
    (status code 302, etc.), false otherwise.

    :   **Returns:**: true if the method will automatically follow HTTP redirects, false otherwise

---



### setFollowRedirects

```
void setFollowRedirects(boolean followRedirects)
```

:   Sets whether or not the HTTP method should automatically follow HTTP redirects
    (status code 302, etc.)

    :   **Parameters:**: `followRedirects` - true if the method will automatically follow redirects, false otherwise.

---



### setQueryString

```
void setQueryString(String queryString)
```

:   Sets the query string of the HTTP method.
    It is responsibility of the caller to ensure that the path is
    properly encoded (URL safe). The string must not include an initial '?' character.

    :   **Parameters:**: `queryString` - the query to be used in the request, with no leading '?' character **See Also:**: [`getQueryString()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getQueryString()), [`setQueryString(NameValuePair[])`](../../../../org/apache/commons/httpclient/HttpMethod.html#setQueryString(org.apache.commons.httpclient.NameValuePair[]))

---



### setQueryString

```
void setQueryString(NameValuePair[] params)
```

:   Sets the query string of this HTTP method. The pairs are encoded as UTF-8 characters.
    To use a different charset the parameters can be encoded manually using EncodingUtil
    and set as a single String.

    :   **Parameters:**: `params` - An array of `NameValuePair`s to use as the query string. The name/value pairs will be automatically URL encoded and should not have been encoded previously. **See Also:**: [`getQueryString()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getQueryString()), [`setQueryString(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setQueryString(java.lang.String)), [`EncodingUtil.formUrlEncode(NameValuePair[], String)`](../../../../org/apache/commons/httpclient/util/EncodingUtil.html#formUrlEncode(org.apache.commons.httpclient.NameValuePair[], java.lang.String))

---



### getQueryString

```
String getQueryString()
```

:   Returns the query string of this HTTP method.

    :   **Returns:**: the query string in URL encoded form, without a leading '?'. **See Also:**: [`setQueryString(NameValuePair[])`](../../../../org/apache/commons/httpclient/HttpMethod.html#setQueryString(org.apache.commons.httpclient.NameValuePair[])), [`setQueryString(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setQueryString(java.lang.String))

---



### getRequestHeaders

```
Header[] getRequestHeaders()
```

:   Returns the current request headers for this HTTP method. The returned headers
    will be in the same order that they were added with `addRequestHeader`.
    If there are multiple request headers with the same name (e.g. `Cookie`),
    they will be returned as multiple entries in the array.

    :   **Returns:**: an array containing all of the request headers **See Also:**: [`addRequestHeader(Header)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(org.apache.commons.httpclient.Header)), [`addRequestHeader(String,String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(java.lang.String, java.lang.String))

---



### getRequestHeaders

```
Header[] getRequestHeaders(String headerName)
```

:   Returns the request headers with the given name. Note that header-name matching is
    case insensitive.

    :   **Parameters:**: `headerName` - the name of the headers to be returned. **Returns:**: an array of zero or more headers **Since:** : 3.0

---



### validate

```
boolean validate()
```

:   Returns true the method is ready to execute, false otherwise.

    :   **Returns:**: true if the method is ready to execute, false otherwise.

---



### getStatusCode

```
int getStatusCode()
```

:   Returns the status code associated with the latest response.

    :   **Returns:**: The status code from the most recent execution of this method. If the method has not yet been executed, the result is undefined.

---



### getStatusText

```
String getStatusText()
```

:   Returns the status text (or "reason phrase") associated with the latest
    response.

    :   **Returns:**: The status text from the most recent execution of this method. If the method has not yet been executed, the result is undefined.

---



### getResponseHeaders

```
Header[] getResponseHeaders()
```

:   Returns the response headers from the most recent execution of this request.

    :   **Returns:**: A newly-created array containing all of the response headers, in the order in which they appeared in the response.

---



### getResponseHeader

```
Header getResponseHeader(String headerName)
```

:   Returns the specified response header. Note that header-name matching is
    case insensitive.

    :   **Parameters:**: `headerName` - The name of the header to be returned. **Returns:**: The specified response header. If the repsonse contained multiple instances of the header, its values will be combined using the ',' separator as specified by RFC2616.

---



### getResponseHeaders

```
Header[] getResponseHeaders(String headerName)
```

:   Returns the response headers with the given name. Note that header-name matching is
    case insensitive.

    :   **Parameters:**: `headerName` - the name of the headers to be returned. **Returns:**: an array of zero or more headers **Since:** : 3.0

---



### getResponseFooters

```
Header[] getResponseFooters()
```

:   Returns the response footers from the most recent execution of this request.

    :   **Returns:**: an array containing the response footers in the order that they appeared in the response. If the response had no footers, an empty array will be returned.

---



### getResponseFooter

```
Header getResponseFooter(String footerName)
```

:   Return the specified response footer. Note that footer-name matching is
    case insensitive.

    :   **Parameters:**: `footerName` - The name of the footer. **Returns:**: The response footer.

---



### getResponseBody

```
byte[] getResponseBody()
                       throws IOException
```

:   Returns the response body of the HTTP method, if any, as an array of bytes.
    If the method has not yet been executed or the response has no body, `null`
    is returned. Note that this method does not propagate I/O exceptions.
    If an error occurs while reading the body, `null` will be returned.

    :   **Returns:**: The response body, or `null` if the body is not available. **Throws:**: `IOException` - if an I/O (transport) problem occurs

---



### getResponseBodyAsString

```
String getResponseBodyAsString()
                               throws IOException
```

:   Returns the response body of the HTTP method, if any, as a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang").
    If response body is not available or cannot be read, null is returned.
    The raw bytes in the body are converted to a `String` using the
    character encoding specified in the response's Content-Type header, or
    ISO-8859-1 if the response did not specify a character set.

    Note that this method does not propagate I/O exceptions.
    If an error occurs while reading the body, `null` will be returned.

    :   **Returns:**: The response body converted to a `String`, or `null` if the body is not available. **Throws:**: `IOException` - if an I/O (transport) problem occurs

---



### getResponseBodyAsStream

```
InputStream getResponseBodyAsStream()
                                    throws IOException
```

:   Returns the response body of the HTTP method, if any, as an InputStream.
    If the response had no body or the method has not yet been executed,
    `null` is returned. Additionally, `null` may be returned
    if [`releaseConnection()`](../../../../org/apache/commons/httpclient/HttpMethod.html#releaseConnection()) has been called or
    if this method was called previously and the resulting stream was closed.

    :   **Returns:**: The response body, or `null` if it is not available **Throws:**: `IOException` - if an I/O (transport) problem occurs

---



### hasBeenUsed

```
boolean hasBeenUsed()
```

:   Returns true if the HTTP method has been already [`executed`](../../../../org/apache/commons/httpclient/HttpMethod.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)),
    but not [`recycled`](../../../../org/apache/commons/httpclient/HttpMethod.html#recycle()).

    :   **Returns:**: true if the method has been executed, false otherwise

---



### execute

```
int execute(HttpState state,
            HttpConnection connection)
            throws HttpException,
                   IOException
```

:   Executes this method using the specified `HttpConnection` and
    `HttpState`.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information to associate with this method: `connection` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Returns:**: the integer status code if one was obtained, or -1 **Throws:**: `IOException` - If an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - If a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### abort

```
void abort()
```

:   Aborts the execution of the HTTP method.

    :   **Since:**
        :   3.0

        **See Also:**: [`execute(HttpState, HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethod.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### recycle

```
void recycle()
```

:   **Deprecated.** *no longer supported and will be removed in the future
    version of HttpClient*

    :   Recycles the HTTP method so that it can be used again.
        Note that all of the instance variables will be reset
        once this method has been called. This method will also
        release the connection being used by this HTTP method.

        :   **See Also:**: [`releaseConnection()`](../../../../org/apache/commons/httpclient/HttpMethod.html#releaseConnection())

---



### releaseConnection

```
void releaseConnection()
```

:   Releases the connection being used by this HTTP method. In particular the
    connection is used to read the response (if there is one) and will be held
    until the response has been read. If the connection can be reused by other
    HTTP methods it is NOT closed at this point.

    After this method is called, [`getResponseBodyAsStream()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getResponseBodyAsStream()) will return
    `null`, and [`getResponseBody()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getResponseBody()) and [`getResponseBodyAsString()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getResponseBodyAsString())
    *may* return `null`.

---



### addResponseFooter

```
void addResponseFooter(Header footer)
```

:   Add a footer to this method's response.

    **Note:** This method is for
    internal use only and should not be called by external clients.

    :   **Parameters:**: `footer` - the footer to add **Since:** : 2.0

---



### getStatusLine

```
StatusLine getStatusLine()
```

:   Returns the Status-Line from the most recent response for this method,
    or `null` if the method has not been executed.

    :   **Returns:**: the status line, or `null` if the method has not been executed **Since:** : 2.0

---



### getDoAuthentication

```
boolean getDoAuthentication()
```

:   Returns true if the HTTP method should automatically handle HTTP
    authentication challenges (status code 401, etc.), false otherwise

    :   **Returns:**: true if authentication challenges will be processed automatically, false otherwise. **Since:** : 2.0 **See Also:**: [`setDoAuthentication(boolean)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setDoAuthentication(boolean))

---



### setDoAuthentication

```
void setDoAuthentication(boolean doAuthentication)
```

:   Sets whether or not the HTTP method should automatically handle HTTP
    authentication challenges (status code 401, etc.)

    :   **Parameters:**: `doAuthentication` - true to process authentication challenges automatically, false otherwise. **Since:** : 2.0 **See Also:**: [`getDoAuthentication()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getDoAuthentication())

---



### getParams

```
HttpMethodParams getParams()
```

:   Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") associated with this method.

    :   **Since:**
        :   3.0

        **See Also:**: [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")

---



### setParams

```
void setParams(HttpMethodParams params)
```

:   Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") for this method.

    :   **Since:**
        :   3.0

        **See Also:**: [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")

---



### getHostAuthState

```
AuthState getHostAuthState()
```

:   Returns the target host [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth")

    :   **Returns:**: host authentication state **Since:** : 3.0

---



### getProxyAuthState

```
AuthState getProxyAuthState()
```

:   Returns the proxy [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth")

    :   **Returns:**: host authentication state **Since:** : 3.0

---



### isRequestSent

```
boolean isRequestSent()
```

:   Returns true if the HTTP has been transmitted to the target
    server in its entirety, false otherwise. This flag can be useful
    for recovery logic. If the request has not been transmitted in its entirety,
    it is safe to retry the failed method.

    :   **Returns:**: true if the request has been sent, false otherwise



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpMethod.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpHost.html "class in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpMethod.html)    [**NO FRAMES**](HttpMethod.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | **Overview** | Package | Class | Use | [**Tree**](overview-tree.html) | [**Deprecated**](deprecated-list.html) | [**Index**](index-all.html) | [**Help**](help-doc.html) | | |  |
| PREV   NEXT | [**FRAMES**](index.html?overview-summary.html)    [**NO FRAMES**](overview-summary.html) |




---



# HttpClient 3.1 API

| **Packages** | |
| --- | --- |
| **[org.apache.commons.httpclient](org/apache/commons/httpclient/package-summary.html)** | Classes and interfaces supporting the client side of the HTTP protocol. |
| **[org.apache.commons.httpclient.auth](org/apache/commons/httpclient/auth/package-summary.html)** | Provides implementation of various authentication schemes as well as utility classes that can be used to authenticate HTTP requests. |
| **[org.apache.commons.httpclient.cookie](org/apache/commons/httpclient/cookie/package-summary.html)** | Provides cookie handling in conjunction with [`Cookie`](org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient"). |
| **[org.apache.commons.httpclient.methods](org/apache/commons/httpclient/methods/package-summary.html)** | Classes implementing [`HttpMethod`](org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient") for the base HTTP methods. |
| **[org.apache.commons.httpclient.methods.multipart](org/apache/commons/httpclient/methods/multipart/package-summary.html)** | Provides Multipart support classes for the [`MultipartPostMethod`](org/apache/commons/httpclient/methods/MultipartPostMethod.html "class in org.apache.commons.httpclient.methods"). |
| **[org.apache.commons.httpclient.params](org/apache/commons/httpclient/params/package-summary.html)** | HttpClient preferences framework. |
| **[org.apache.commons.httpclient.protocol](org/apache/commons/httpclient/protocol/package-summary.html)** | Provides protocol specific socket factory handling. |
| **[org.apache.commons.httpclient.util](org/apache/commons/httpclient/util/package-summary.html)** | Provides some utility classes for use by HttpClient. |

---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | **Overview** | Package | Class | Use | [**Tree**](overview-tree.html) | [**Deprecated**](deprecated-list.html) | [**Index**](index-all.html) | [**Help**](help-doc.html) | | |  |
| PREV   NEXT | [**FRAMES**](index.html?overview-summary.html)    [**NO FRAMES**](overview-summary.html) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](../package-summary.html) | [**Class**](../../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") | **Use** | [**Tree**](../package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| PREV   NEXT | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient//class-useHttpMethodRetryHandler.html)    [**NO FRAMES**](HttpMethodRetryHandler.html) |




---



## **Uses of Interface org.apache.commons.httpclient.HttpMethodRetryHandler**

| Packages that use [HttpMethodRetryHandler](../../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") | |
| --- | --- |
| [**org.apache.commons.httpclient**](#org.apache.commons.httpclient) | Classes and interfaces supporting the client side of the HTTP protocol. |

| Uses of [HttpMethodRetryHandler](../../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") in [org.apache.commons.httpclient](../../../../../org/apache/commons/httpclient/package-summary.html) | |
| --- | --- |

| Classes in [org.apache.commons.httpclient](../../../../../org/apache/commons/httpclient/package-summary.html) that implement [HttpMethodRetryHandler](../../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") | |
| --- | --- |
| `class` | `DefaultHttpMethodRetryHandler`             The default [`HttpMethodRetryHandler`](../../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") used by [`HttpMethod`](../../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")s. |

---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../../overview-summary.html) | [**Package**](../package-summary.html) | [**Class**](../../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") | **Use** | [**Tree**](../package-tree.html) | [**Deprecated**](../../../../../deprecated-list.html) | [**Index**](../../../../../index-all.html) | [**Help**](../../../../../help-doc.html) | | |  |
| PREV   NEXT | [**FRAMES**](../../../../../index.html?org/apache/commons/httpclient//class-useHttpMethodRetryHandler.html)    [**NO FRAMES**](HttpMethodRetryHandler.html) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](overview-summary.html) | Package | Class | Use | [**Tree**](overview-tree.html) | [**Deprecated**](deprecated-list.html) | [**Index**](index-all.html) | **Help** | | |  |
| PREV   NEXT | [**FRAMES**](index.html?help-doc.html)    [**NO FRAMES**](help-doc.html) |




---



# How This API Document Is Organized

This API (Application Programming Interface) document has pages corresponding to the items in the navigation bar, described as follows.

### Overview

> The [Overview](overview-summary.html) page is the front page of this API document and provides a list of all packages with a summary for each. This page can also contain an overall description of the set of packages.

### Package

> Each package has a page that contains a list of its classes and interfaces, with a summary for each. This page can contain four categories:
>
> * Interfaces (italic)* Classes* Enums* Exceptions* Errors* Annotation Types

### Class/Interface

> Each class, interface, nested class and nested interface has its own separate page. Each of these pages has three sections consisting of a class/interface description, summary tables, and detailed member descriptions:
>
> * Class inheritance diagram* Direct Subclasses* All Known Subinterfaces* All Known Implementing Classes* Class/interface declaration* Class/interface description
>
>             * Nested Class Summary* Field Summary* Constructor Summary* Method Summary
>
>                     * Field Detail* Constructor Detail* Method Detail
>
> Each summary entry contains the first sentence from the detailed description for that item. The summary entries are alphabetical, while the detailed descriptions are in the order they appear in the source code. This preserves the logical groupings established by the programmer.

### Annotation Type

> Each annotation type has its own separate page with the following sections:
>
> * Annotation Type declaration* Annotation Type description* Required Element Summary* Optional Element Summary* Element Detail

### Enum

> Each enum has its own separate page with the following sections:
>
> * Enum declaration* Enum description* Enum Constant Summary* Enum Constant Detail

### Use

> Each documented package, class and interface has its own Use page. This page describes what packages, classes, methods, constructors and fields use any part of the given class or package. Given a class or interface A, its Use page includes subclasses of A, fields declared as A, methods that return A, and methods and constructors with parameters of type A. You can access this page by first going to the package, class or interface, then clicking on the "Use" link in the navigation bar.

### Tree (Class Hierarchy)

> There is a [Class Hierarchy](overview-tree.html) page for all packages, plus a hierarchy for each package. Each hierarchy page contains a list of classes and a list of interfaces. The classes are organized by inheritance structure starting with `java.lang.Object`. The interfaces do not inherit from `java.lang.Object`.
>
> * When viewing the Overview page, clicking on "Tree" displays the hierarchy for all packages.* When viewing a particular package, class or interface page, clicking "Tree" displays the hierarchy for only that package.

### Deprecated API

> The [Deprecated API](deprecated-list.html) page lists all of the API that have been deprecated. A deprecated API is not recommended for use, generally due to improvements, and a replacement API is usually given. Deprecated APIs may be removed in future implementations.

### Index

> The [Index](index-all.html) contains an alphabetic list of all classes, interfaces, constructors, methods, and fields.

### Prev/Next

These links take you to the next or previous class, interface, package, or related page.

### Frames/No Frames

These links show and hide the HTML frames. All pages are available with or without frames.

### Serialized Form

Each serializable or externalizable class has a description of its serialization fields and methods. This information is of interest to re-implementors, not to developers using the API. While there is no link in the navigation bar, you can get to this information by going to any serialized class and clicking "Serialized Form" in the "See also" section of the class description.

### Constant Field Values

The [Constant Field Values](constant-values.html) page lists the static final fields and their values.

*This help file applies to API documentation generated using the standard doclet.*
  


---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](overview-summary.html) | Package | Class | Use | [**Tree**](overview-tree.html) | [**Deprecated**](deprecated-list.html) | [**Index**](index-all.html) | **Help** | | |  |
| PREV   NEXT | [**FRAMES**](index.html?help-doc.html)    [**NO FRAMES**](help-doc.html) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpParser.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpRecoverableException.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpParser.html)    [**NO FRAMES**](HttpParser.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class HttpParser

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.HttpParser
```

---

``` public class HttpParser extends Object ```

A utility class for parsing http header values according to
RFC-2616 Section 4 and 19.3.

**Since:**
:   2.0beta1

**Author:**
:   Michael Becke, [Oleg Kalnichevski](mailto:oleg@ural.ru)

---

| **Method Summary** | |
| --- | --- |
| `static Header[]` | `parseHeaders(InputStream is)`             **Deprecated.** *use #parseHeaders(InputStream, String)* |
| `static Header[]` | `parseHeaders(InputStream is, String charset)`             Parses headers from the given stream. |
| `static String` | `readLine(InputStream inputStream)`             **Deprecated.** *use #readLine(InputStream, String)* |
| `static String` | `readLine(InputStream inputStream, String charset)`             Read up to "\n" from an (unchunked) input stream. |
| `static byte[]` | `readRawLine(InputStream inputStream)`             Return byte array from an (unchunked) input stream. |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Method Detail** |
| --- |

### readRawLine

```
public static byte[] readRawLine(InputStream inputStream)
                          throws IOException
```

:   Return byte array from an (unchunked) input stream.
    Stop reading when "\n" terminator encountered
    If the stream ends before the line terminator is found,
    the last part of the string will still be returned.
    If no input data available, `null` is returned.

    :   **Parameters:**: `inputStream` - the stream to read from **Returns:**: a byte array from the stream **Throws:**: `IOException` - if an I/O problem occurs

---



### readLine

```
public static String readLine(InputStream inputStream,
                              String charset)
                       throws IOException
```

:   Read up to "\n" from an (unchunked) input stream.
    If the stream ends before the line terminator is found,
    the last part of the string will still be returned.
    If no input data available, `null` is returned.

    :   **Parameters:**: `inputStream` - the stream to read from: `charset` - charset of HTTP protocol elements **Returns:**: a line from the stream **Throws:**: `IOException` - if an I/O problem occurs **Since:** : 3.0

---



### readLine

```
public static String readLine(InputStream inputStream)
                       throws IOException
```

:   **Deprecated.** *use #readLine(InputStream, String)*

    :   Read up to "\n" from an (unchunked) input stream.
        If the stream ends before the line terminator is found,
        the last part of the string will still be returned.
        If no input data available, `null` is returned

        :   **Parameters:**: `inputStream` - the stream to read from **Returns:**: a line from the stream **Throws:**: `IOException` - if an I/O problem occurs

---



### parseHeaders

```
public static Header[] parseHeaders(InputStream is,
                                    String charset)
                             throws IOException,
                                    HttpException
```

:   Parses headers from the given stream. Headers with the same name are not
    combined.

    :   **Parameters:**: `is` - the stream to read headers from: `charset` - the charset to use for reading the data **Returns:**: an array of headers in the order in which they were parsed **Throws:**: `IOException` - if an IO error occurs while reading from the stream: `HttpException` - if there is an error parsing a header value **Since:** : 3.0

---



### parseHeaders

```
public static Header[] parseHeaders(InputStream is)
                             throws IOException,
                                    HttpException
```

:   **Deprecated.** *use #parseHeaders(InputStream, String)*

    :   Parses headers from the given stream. Headers with the same name are not
        combined.

        :   **Parameters:**: `is` - the stream to read headers from **Returns:**: an array of headers in the order in which they were parsed **Throws:**: `IOException` - if an IO error occurs while reading from the stream: `HttpException` - if there is an error parsing a header value



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpParser.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpRecoverableException.html "class in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpParser.html)    [**NO FRAMES**](HttpParser.html) |
| SUMMARY: NESTED | FIELD | CONSTR | [METHOD](#method_summary) | DETAIL: FIELD | CONSTR | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](overview-summary.html) | Package | Class | Use | [**Tree**](overview-tree.html) | **Deprecated** | [**Index**](index-all.html) | [**Help**](help-doc.html) | | |  |
| PREV   NEXT | [**FRAMES**](index.html?deprecated-list.html)    [**NO FRAMES**](deprecated-list.html) |




---



## **Deprecated API**



---

**Contents**

* [Deprecated Interfaces](#interface)* [Deprecated Classes](#class)* [Deprecated Exceptions](#exception)* [Deprecated Fields](#field)* [Deprecated Methods](#method)* [Deprecated Constructors](#constructor)

| **Deprecated Interfaces** | |
| --- | --- |
| [org.apache.commons.httpclient.MethodRetryHandler](org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient")             *use [`HttpMethodRetryHandler`](org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")* |

| **Deprecated Classes** | |
| --- | --- |
| [org.apache.commons.httpclient.auth.AuthSchemeBase](org/apache/commons/httpclient/auth/AuthSchemeBase.html "class in org.apache.commons.httpclient.auth")             *No longer used* |
| [org.apache.commons.httpclient.util.DateParser](org/apache/commons/httpclient/util/DateParser.html "class in org.apache.commons.httpclient.util")             *Use [`DateUtil`](org/apache/commons/httpclient/util/DateUtil.html "class in org.apache.commons.httpclient.util")* |
| [org.apache.commons.httpclient.DefaultMethodRetryHandler](org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient")             *use [`DefaultHttpMethodRetryHandler`](org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html "class in org.apache.commons.httpclient")* |
| [org.apache.commons.httpclient.auth.HttpAuthenticator](org/apache/commons/httpclient/auth/HttpAuthenticator.html "class in org.apache.commons.httpclient.auth")             *no longer used* |
| [org.apache.commons.httpclient.auth.HttpAuthRealm](org/apache/commons/httpclient/auth/HttpAuthRealm.html "class in org.apache.commons.httpclient.auth")             *no longer used* |
| [org.apache.commons.httpclient.HttpConstants](org/apache/commons/httpclient/HttpConstants.html "class in org.apache.commons.httpclient")             *use EncodingUtil class* |
| [org.apache.commons.httpclient.methods.MultipartPostMethod](org/apache/commons/httpclient/methods/MultipartPostMethod.html "class in org.apache.commons.httpclient.methods")             *Use [`MultipartRequestEntity`](org/apache/commons/httpclient/methods/multipart/MultipartRequestEntity.html "class in org.apache.commons.httpclient.methods.multipart") in conjunction with [`PostMethod`](org/apache/commons/httpclient/methods/PostMethod.html "class in org.apache.commons.httpclient.methods") instead.* |
| [org.apache.commons.httpclient.util.URIUtil.Coder](org/apache/commons/httpclient/util/URIUtil.Coder.html "class in org.apache.commons.httpclient.util")             *use org.apache.commons.codec.net.URLCodec* |

| **Deprecated Exceptions** | |
| --- | --- |
| [org.apache.commons.httpclient.HttpRecoverableException](org/apache/commons/httpclient/HttpRecoverableException.html "class in org.apache.commons.httpclient")             *no longer used* |

| **Deprecated Fields** | |
| --- | --- |
| [org.apache.commons.httpclient.HttpsURL.\_default\_port](org/apache/commons/httpclient/HttpsURL.html#_default_port)             *Use [`HttpsURL.DEFAULT_PORT`](org/apache/commons/httpclient/HttpsURL.html#DEFAULT_PORT) instead. This one doesn't conform to the project naming conventions.* |
| [org.apache.commons.httpclient.HttpURL.\_default\_port](org/apache/commons/httpclient/HttpURL.html#_default_port)             *Use [`HttpURL.DEFAULT_PORT`](org/apache/commons/httpclient/HttpURL.html#DEFAULT_PORT) instead. This one doesn't conform to the project naming conventions.* |
| [org.apache.commons.httpclient.HttpsURL.\_default\_scheme](org/apache/commons/httpclient/HttpsURL.html#_default_scheme)             *Use [`HttpsURL.DEFAULT_SCHEME`](org/apache/commons/httpclient/HttpsURL.html#DEFAULT_SCHEME) instead. This one doesn't conform to the project naming conventions.* |
| [org.apache.commons.httpclient.HttpURL.\_default\_scheme](org/apache/commons/httpclient/HttpURL.html#_default_scheme)             *Use [`HttpURL.DEFAULT_SCHEME`](org/apache/commons/httpclient/HttpURL.html#DEFAULT_SCHEME) instead. This one doesn't conform to the project naming conventions.* |
| [org.apache.commons.httpclient.methods.multipart.Part.BOUNDARY](org/apache/commons/httpclient/methods/multipart/Part.html#BOUNDARY)             *use [`HttpMethodParams.MULTIPART_BOUNDARY`](org/apache/commons/httpclient/params/HttpMethodParams.html#MULTIPART_BOUNDARY)* |
| [org.apache.commons.httpclient.methods.multipart.Part.BOUNDARY\_BYTES](org/apache/commons/httpclient/methods/multipart/Part.html#BOUNDARY_BYTES) |
| [org.apache.commons.httpclient.cookie.CookiePolicy.COMPATIBILITY](org/apache/commons/httpclient/cookie/CookiePolicy.html#COMPATIBILITY)             *Use [`CookiePolicy.BROWSER_COMPATIBILITY`](org/apache/commons/httpclient/cookie/CookiePolicy.html#BROWSER_COMPATIBILITY)* |
| [org.apache.commons.httpclient.methods.EntityEnclosingMethod.CONTENT\_LENGTH\_AUTO](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#CONTENT_LENGTH_AUTO)             *Use [`InputStreamRequestEntity.CONTENT_LENGTH_AUTO`](org/apache/commons/httpclient/methods/InputStreamRequestEntity.html#CONTENT_LENGTH_AUTO).* |
| [org.apache.commons.httpclient.methods.EntityEnclosingMethod.CONTENT\_LENGTH\_CHUNKED](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#CONTENT_LENGTH_CHUNKED)             *Use [`EntityEnclosingMethod.setContentChunked(boolean)`](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setContentChunked(boolean)).* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.NETSCAPE\_DRAFT](org/apache/commons/httpclient/cookie/CookiePolicy.html#NETSCAPE_DRAFT)             *Use [`CookiePolicy.NETSCAPE`](org/apache/commons/httpclient/cookie/CookiePolicy.html#NETSCAPE)* |
| [org.apache.commons.httpclient.HttpState.PREEMPTIVE\_DEFAULT](org/apache/commons/httpclient/HttpState.html#PREEMPTIVE_DEFAULT)             *This field and feature will be removed following HttpClient 3.0.* |
| [org.apache.commons.httpclient.HttpState.PREEMPTIVE\_PROPERTY](org/apache/commons/httpclient/HttpState.html#PREEMPTIVE_PROPERTY)             *This field and feature will be removed following HttpClient 3.0.* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.RFC2109](org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC2109)             *Use [`CookiePolicy.RFC_2109`](org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2109)* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.RFC2965](org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC2965)             *Use [`CookiePolicy.RFC_2965`](org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2965)* |

| **Deprecated Methods** | |
| --- | --- |
| [org.apache.commons.httpclient.auth.HttpAuthenticator.authenticate(AuthScheme, HttpMethod, HttpConnection, HttpState)](org/apache/commons/httpclient/auth/HttpAuthenticator.html#authenticate(org.apache.commons.httpclient.auth.AuthScheme, org.apache.commons.httpclient.HttpMethod, org.apache.commons.httpclient.HttpConnection, org.apache.commons.httpclient.HttpState))             *use AuthScheme* |
| [org.apache.commons.httpclient.auth.BasicScheme.authenticate(Credentials, String, String)](org/apache/commons/httpclient/auth/BasicScheme.html#authenticate(org.apache.commons.httpclient.Credentials, java.lang.String, java.lang.String))             *Use [`BasicScheme.authenticate(Credentials, HttpMethod)`](org/apache/commons/httpclient/auth/BasicScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod))* |
| [org.apache.commons.httpclient.auth.DigestScheme.authenticate(Credentials, String, String)](org/apache/commons/httpclient/auth/DigestScheme.html#authenticate(org.apache.commons.httpclient.Credentials, java.lang.String, java.lang.String))             *Use [`DigestScheme.authenticate(Credentials, HttpMethod)`](org/apache/commons/httpclient/auth/DigestScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod))* |
| [org.apache.commons.httpclient.auth.AuthScheme.authenticate(Credentials, String, String)](org/apache/commons/httpclient/auth/AuthScheme.html#authenticate(org.apache.commons.httpclient.Credentials, java.lang.String, java.lang.String))             *Use [`AuthScheme.authenticate(Credentials, HttpMethod)`](org/apache/commons/httpclient/auth/AuthScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod)) Produces an authorization string for the given set of [`Credentials`](org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient"), method name and URI using the given authentication scheme in response to the actual authorization challenge.* |
| [org.apache.commons.httpclient.auth.NTLMScheme.authenticate(Credentials, String, String)](org/apache/commons/httpclient/auth/NTLMScheme.html#authenticate(org.apache.commons.httpclient.Credentials, java.lang.String, java.lang.String))             *Use [`NTLMScheme.authenticate(Credentials, HttpMethod)`](org/apache/commons/httpclient/auth/NTLMScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod))* |
| [org.apache.commons.httpclient.auth.NTLMScheme.authenticate(NTCredentials, String)](org/apache/commons/httpclient/auth/NTLMScheme.html#authenticate(org.apache.commons.httpclient.NTCredentials, java.lang.String))             *Use non-static [`NTLMScheme.authenticate(Credentials, HttpMethod)`](org/apache/commons/httpclient/auth/NTLMScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod))* |
| [org.apache.commons.httpclient.auth.NTLMScheme.authenticate(NTCredentials, String, String)](org/apache/commons/httpclient/auth/NTLMScheme.html#authenticate(org.apache.commons.httpclient.NTCredentials, java.lang.String, java.lang.String))             *Use non-static [`NTLMScheme.authenticate(Credentials, HttpMethod)`](org/apache/commons/httpclient/auth/NTLMScheme.html#authenticate(org.apache.commons.httpclient.Credentials, org.apache.commons.httpclient.HttpMethod))* |
| [org.apache.commons.httpclient.auth.BasicScheme.authenticate(UsernamePasswordCredentials)](org/apache/commons/httpclient/auth/BasicScheme.html#authenticate(org.apache.commons.httpclient.UsernamePasswordCredentials))             *Use [`BasicScheme.authenticate(UsernamePasswordCredentials, String)`](org/apache/commons/httpclient/auth/BasicScheme.html#authenticate(org.apache.commons.httpclient.UsernamePasswordCredentials, java.lang.String)) Returns a basic Authorization header value for the given [`UsernamePasswordCredentials`](org/apache/commons/httpclient/UsernamePasswordCredentials.html "class in org.apache.commons.httpclient").* |
| [org.apache.commons.httpclient.auth.HttpAuthenticator.authenticateDefault(HttpMethod, HttpConnection, HttpState)](org/apache/commons/httpclient/auth/HttpAuthenticator.html#authenticateDefault(org.apache.commons.httpclient.HttpMethod, org.apache.commons.httpclient.HttpConnection, org.apache.commons.httpclient.HttpState))             *use AuthScheme* |
| [org.apache.commons.httpclient.auth.HttpAuthenticator.authenticateProxy(AuthScheme, HttpMethod, HttpConnection, HttpState)](org/apache/commons/httpclient/auth/HttpAuthenticator.html#authenticateProxy(org.apache.commons.httpclient.auth.AuthScheme, org.apache.commons.httpclient.HttpMethod, org.apache.commons.httpclient.HttpConnection, org.apache.commons.httpclient.HttpState))             *use AuthScheme* |
| [org.apache.commons.httpclient.auth.HttpAuthenticator.authenticateProxyDefault(HttpMethod, HttpConnection, HttpState)](org/apache/commons/httpclient/auth/HttpAuthenticator.html#authenticateProxyDefault(org.apache.commons.httpclient.HttpMethod, org.apache.commons.httpclient.HttpConnection, org.apache.commons.httpclient.HttpState))             *use AuthScheme* |
| [org.apache.commons.httpclient.util.URIUtil.Coder.decode(char[], String)](org/apache/commons/httpclient/util/URIUtil.Coder.html#decode(char[], java.lang.String))             *use org.apache.commons.codec.net.URLCodec* |
| [org.apache.commons.httpclient.util.URIUtil.Coder.encode(String, BitSet, String)](org/apache/commons/httpclient/util/URIUtil.Coder.html#encode(java.lang.String, java.util.BitSet, java.lang.String))             *use org.apache.commons.codec.net.URLCodec* |
| [org.apache.commons.httpclient.HttpMethodBase.getAuthenticationRealm()](org/apache/commons/httpclient/HttpMethodBase.html#getAuthenticationRealm())             *use #getHostAuthState()* |
| [org.apache.commons.httpclient.methods.HeadMethod.getBodyCheckTimeout()](org/apache/commons/httpclient/methods/HeadMethod.html#getBodyCheckTimeout())             *Use [`HttpMethodParams`](org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| [org.apache.commons.httpclient.methods.multipart.Part.getBoundary()](org/apache/commons/httpclient/methods/multipart/Part.html#getBoundary())             *uses a constant string. Rather use [`Part.getPartBoundary()`](org/apache/commons/httpclient/methods/multipart/Part.html#getPartBoundary())* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.getCompatibilitySpec()](org/apache/commons/httpclient/cookie/CookiePolicy.html#getCompatibilitySpec())             *Use [`CookiePolicy.getCookieSpec(String)`](org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.getConnection(HostConfiguration, long)](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnection(org.apache.commons.httpclient.HostConfiguration, long))             *Use #getConnectionWithTimeout(HostConfiguration, long)* |
| [org.apache.commons.httpclient.SimpleHttpConnectionManager.getConnection(HostConfiguration, long)](org/apache/commons/httpclient/SimpleHttpConnectionManager.html#getConnection(org.apache.commons.httpclient.HostConfiguration, long))             *Use #getConnectionWithTimeout(HostConfiguration, long)* |
| [org.apache.commons.httpclient.HttpConnectionManager.getConnection(HostConfiguration, long)](org/apache/commons/httpclient/HttpConnectionManager.html#getConnection(org.apache.commons.httpclient.HostConfiguration, long))             *Use #getConnectionWithTimeout(HostConfiguration, long)* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.getConnectionsInUse()](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInUse())             *Use [`MultiThreadedHttpConnectionManager.getConnectionsInPool()`](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInPool())* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.getConnectionsInUse(HostConfiguration)](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInUse(org.apache.commons.httpclient.HostConfiguration))             *Use [`MultiThreadedHttpConnectionManager.getConnectionsInPool(HostConfiguration)`](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getConnectionsInPool(org.apache.commons.httpclient.HostConfiguration))* |
| [org.apache.commons.httpclient.HttpState.getCookiePolicy()](org/apache/commons/httpclient/HttpState.html#getCookiePolicy())             *Use [`HttpMethodParams.getCookiePolicy()`](org/apache/commons/httpclient/params/HttpMethodParams.html#getCookiePolicy()), [`HttpMethod.getParams()`](org/apache/commons/httpclient/HttpMethod.html#getParams()).* |
| [org.apache.commons.httpclient.HttpState.getCookies(String, int, String, boolean)](org/apache/commons/httpclient/HttpState.html#getCookies(java.lang.String, int, java.lang.String, boolean))             *use CookieSpec#match(String, int, String, boolean, Cookie)* |
| [org.apache.commons.httpclient.HttpState.getCredentials(String, String)](org/apache/commons/httpclient/HttpState.html#getCredentials(java.lang.String, java.lang.String))             *use #getCredentials(AuthScope)* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.getDefaultPolicy()](org/apache/commons/httpclient/cookie/CookiePolicy.html#getDefaultPolicy())             *Use [`CookiePolicy.getDefaultSpec()`](org/apache/commons/httpclient/cookie/CookiePolicy.html#getDefaultSpec())* |
| [org.apache.commons.httpclient.HttpClient.getHost()](org/apache/commons/httpclient/HttpClient.html#getHost())             *use #getHostConfiguration()* |
| [org.apache.commons.httpclient.HttpMethodBase.getHostConfiguration()](org/apache/commons/httpclient/HttpMethodBase.html#getHostConfiguration())             *no longer applicable* |
| [org.apache.commons.httpclient.HttpMethod.getHostConfiguration()](org/apache/commons/httpclient/HttpMethod.html#getHostConfiguration())             *no longer applicable* |
| [org.apache.commons.httpclient.auth.RFC2617Scheme.getID()](org/apache/commons/httpclient/auth/RFC2617Scheme.html#getID())             *no longer used* |
| [org.apache.commons.httpclient.auth.DigestScheme.getID()](org/apache/commons/httpclient/auth/DigestScheme.html#getID())             *no longer used* |
| [org.apache.commons.httpclient.auth.AuthScheme.getID()](org/apache/commons/httpclient/auth/AuthScheme.html#getID())             *no longer used* |
| [org.apache.commons.httpclient.auth.NTLMScheme.getID()](org/apache/commons/httpclient/auth/NTLMScheme.html#getID())             *no longer used* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.getMaxConnectionsPerHost()](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getMaxConnectionsPerHost())             *Use [`HttpConnectionManagerParams.getDefaultMaxConnectionsPerHost()`](org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#getDefaultMaxConnectionsPerHost()), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.getMaxTotalConnections()](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#getMaxTotalConnections())             *Use [`HttpConnectionManagerParams.getMaxTotalConnections()`](org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#getMaxTotalConnections()), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.HttpMethodBase.getMethodRetryHandler()](org/apache/commons/httpclient/HttpMethodBase.html#getMethodRetryHandler())             *use [`HttpMethodParams`](org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| [org.apache.commons.httpclient.HttpClient.getPort()](org/apache/commons/httpclient/HttpClient.html#getPort())             *use #getHostConfiguration()* |
| [org.apache.commons.httpclient.HttpMethodBase.getProxyAuthenticationRealm()](org/apache/commons/httpclient/HttpMethodBase.html#getProxyAuthenticationRealm())             *use #getProxyAuthState()* |
| [org.apache.commons.httpclient.HttpState.getProxyCredentials(String, String)](org/apache/commons/httpclient/HttpState.html#getProxyCredentials(java.lang.String, java.lang.String))             *use #getProxyCredentials(AuthScope)* |
| [org.apache.commons.httpclient.URIException.getReason()](org/apache/commons/httpclient/URIException.html#getReason())             *You should instead call [`Throwable.getMessage()`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Throwable.html#getMessage() "class or interface in java.lang").* |
| [org.apache.commons.httpclient.HttpException.getReason()](org/apache/commons/httpclient/HttpException.html#getReason())             *HttpClient no longer uses this for itself. It is only provided for compatibility with existing clients, and will be removed in a future release.* |
| [org.apache.commons.httpclient.HttpException.getReasonCode()](org/apache/commons/httpclient/HttpException.html#getReasonCode())             *HttpClient no longer uses this for itself. It is only provided for compatibility with existing clients, and will be removed in a future release.* |
| [org.apache.commons.httpclient.HttpMethodBase.getRecoverableExceptionCount()](org/apache/commons/httpclient/HttpMethodBase.html#getRecoverableExceptionCount())             *no longer used Returns the number of "recoverable" exceptions thrown and handled, to allow for monitoring the quality of the connection.* |
| [org.apache.commons.httpclient.HttpConnection.getSoTimeout()](org/apache/commons/httpclient/HttpConnection.html#getSoTimeout())             *Use [`HttpConnectionParams.getSoTimeout()`](org/apache/commons/httpclient/params/HttpConnectionParams.html#getSoTimeout()), [`HttpConnection.getParams()`](org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.getSpecByPolicy(int)](org/apache/commons/httpclient/cookie/CookiePolicy.html#getSpecByPolicy(int))             *Use [`CookiePolicy.getCookieSpec(String)`](org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.getSpecByVersion(int)](org/apache/commons/httpclient/cookie/CookiePolicy.html#getSpecByVersion(int))             *Use [`CookiePolicy.getCookieSpec(String)`](org/apache/commons/httpclient/cookie/CookiePolicy.html#getCookieSpec(java.lang.String))* |
| [org.apache.commons.httpclient.methods.ExpectContinueMethod.getUseExpectHeader()](org/apache/commons/httpclient/methods/ExpectContinueMethod.html#getUseExpectHeader())             *Use [`HttpMethodParams`](org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| [org.apache.commons.httpclient.Header.getValues()](org/apache/commons/httpclient/Header.html#getValues())             *Use #getElements* |
| [org.apache.commons.httpclient.HttpConnection.getVirtualHost()](org/apache/commons/httpclient/HttpConnection.html#getVirtualHost())             *no longer applicable* |
| [org.apache.commons.httpclient.HostConfiguration.getVirtualHost()](org/apache/commons/httpclient/HostConfiguration.html#getVirtualHost())             *use HostParams* |
| [org.apache.commons.httpclient.HttpState.isAuthenticationPreemptive()](org/apache/commons/httpclient/HttpState.html#isAuthenticationPreemptive())             *Use [`HttpClientParams.isAuthenticationPreemptive()`](org/apache/commons/httpclient/params/HttpClientParams.html#isAuthenticationPreemptive()), [`HttpClient.getParams()`](org/apache/commons/httpclient/HttpClient.html#getParams()).* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.isConnectionStaleCheckingEnabled()](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#isConnectionStaleCheckingEnabled())             *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.SimpleHttpConnectionManager.isConnectionStaleCheckingEnabled()](org/apache/commons/httpclient/SimpleHttpConnectionManager.html#isConnectionStaleCheckingEnabled())             *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.HostConfiguration.isHostSet()](org/apache/commons/httpclient/HostConfiguration.html#isHostSet())             *no longer used* |
| [org.apache.commons.httpclient.HttpMethodBase.isHttp11()](org/apache/commons/httpclient/HttpMethodBase.html#isHttp11())             *Use [`HttpMethodParams.getVersion()`](org/apache/commons/httpclient/params/HttpMethodParams.html#getVersion())* |
| [org.apache.commons.httpclient.HostConfiguration.isProxySet()](org/apache/commons/httpclient/HostConfiguration.html#isProxySet())             *no longer used* |
| [org.apache.commons.httpclient.HttpConnection.isStaleCheckingEnabled()](org/apache/commons/httpclient/HttpConnection.html#isStaleCheckingEnabled())             *Use [`HttpConnectionParams.isStaleCheckingEnabled()`](org/apache/commons/httpclient/params/HttpConnectionParams.html#isStaleCheckingEnabled()), [`HttpConnection.getParams()`](org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| [org.apache.commons.httpclient.HttpClient.isStrictMode()](org/apache/commons/httpclient/HttpClient.html#isStrictMode())             *Use [`DefaultHttpParams.getParameter(String)`](org/apache/commons/httpclient/params/DefaultHttpParams.html#getParameter(java.lang.String)) to exercise a more granular control over HTTP protocol strictness.* |
| [org.apache.commons.httpclient.HttpMethodBase.isStrictMode()](org/apache/commons/httpclient/HttpMethodBase.html#isStrictMode())             *Use [`HttpParams.setParameter(String, Object)`](org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| [org.apache.commons.httpclient.HttpMethod.isStrictMode()](org/apache/commons/httpclient/HttpMethod.html#isStrictMode())             *Use [`HttpParams.setParameter(String, Object)`](org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| [org.apache.commons.httpclient.methods.OptionsMethod.needContentLength()](org/apache/commons/httpclient/methods/OptionsMethod.html#needContentLength())             *only entity enclosing methods set content length header* |
| [org.apache.commons.httpclient.HeaderElement.parse(String)](org/apache/commons/httpclient/HeaderElement.html#parse(java.lang.String))             *Use #parseElements(String).* |
| [org.apache.commons.httpclient.HttpParser.parseHeaders(InputStream)](org/apache/commons/httpclient/HttpParser.html#parseHeaders(java.io.InputStream))             *use #parseHeaders(InputStream, String)* |
| [org.apache.commons.httpclient.HttpConnection.print(String)](org/apache/commons/httpclient/HttpConnection.html#print(java.lang.String))             *Use [`HttpConnection.print(String, String)`](org/apache/commons/httpclient/HttpConnection.html#print(java.lang.String, java.lang.String)) Writes the specified String (as bytes) to the output stream.* |
| [org.apache.commons.httpclient.HttpConnection.printLine(String)](org/apache/commons/httpclient/HttpConnection.html#printLine(java.lang.String))             *Use [`HttpConnection.printLine(String, String)`](org/apache/commons/httpclient/HttpConnection.html#printLine(java.lang.String, java.lang.String)) Writes the specified String (as bytes), followed by "\r\n".getBytes() to the output stream.* |
| [org.apache.commons.httpclient.HttpConnection.readLine()](org/apache/commons/httpclient/HttpConnection.html#readLine())             *use #readLine(String)* |
| [org.apache.commons.httpclient.HttpParser.readLine(InputStream)](org/apache/commons/httpclient/HttpParser.html#readLine(java.io.InputStream))             *use #readLine(InputStream, String)* |
| [org.apache.commons.httpclient.HttpMethodBase.recycle()](org/apache/commons/httpclient/HttpMethodBase.html#recycle())             *no longer supported and will be removed in the future version of HttpClient* |
| [org.apache.commons.httpclient.HttpMethod.recycle()](org/apache/commons/httpclient/HttpMethod.html#recycle())             *no longer supported and will be removed in the future version of HttpClient* |
| [org.apache.commons.httpclient.methods.MultipartPostMethod.recycle()](org/apache/commons/httpclient/methods/MultipartPostMethod.html#recycle())             *no longer supported and will be removed in the future version of HttpClient* |
| [org.apache.commons.httpclient.methods.GetMethod.recycle()](org/apache/commons/httpclient/methods/GetMethod.html#recycle())             *no longer supported and will be removed in the future version of HttpClient* |
| [org.apache.commons.httpclient.methods.EntityEnclosingMethod.recycle()](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#recycle())             *no longer supported and will be removed in the future version of HttpClient* |
| [org.apache.commons.httpclient.methods.HeadMethod.recycle()](org/apache/commons/httpclient/methods/HeadMethod.html#recycle())             *no longer supported and will be removed in the future version of HttpClient* |
| [org.apache.commons.httpclient.methods.TraceMethod.recycle()](org/apache/commons/httpclient/methods/TraceMethod.html#recycle())             *no longer supported and will be removed in the future version of HttpClient* |
| [org.apache.commons.httpclient.auth.HttpAuthenticator.selectAuthScheme(Header[])](org/apache/commons/httpclient/auth/HttpAuthenticator.html#selectAuthScheme(org.apache.commons.httpclient.Header[]))             *Use [`AuthChallengeParser.parseChallenges(Header[])`](org/apache/commons/httpclient/auth/AuthChallengeParser.html#parseChallenges(org.apache.commons.httpclient.Header[])) and [`AuthPolicy.getAuthScheme(String)`](org/apache/commons/httpclient/auth/AuthPolicy.html#getAuthScheme(java.lang.String))* |
| [org.apache.commons.httpclient.HttpState.setAuthenticationPreemptive(boolean)](org/apache/commons/httpclient/HttpState.html#setAuthenticationPreemptive(boolean))             *Use [`HttpClientParams.setAuthenticationPreemptive(boolean)`](org/apache/commons/httpclient/params/HttpClientParams.html#setAuthenticationPreemptive(boolean)), [`HttpClient.getParams()`](org/apache/commons/httpclient/HttpClient.html#getParams()).* |
| [org.apache.commons.httpclient.methods.HeadMethod.setBodyCheckTimeout(int)](org/apache/commons/httpclient/methods/HeadMethod.html#setBodyCheckTimeout(int))             *Use [`HttpMethodParams`](org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.setConnectionStaleCheckingEnabled(boolean)](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#setConnectionStaleCheckingEnabled(boolean))             *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.SimpleHttpConnectionManager.setConnectionStaleCheckingEnabled(boolean)](org/apache/commons/httpclient/SimpleHttpConnectionManager.html#setConnectionStaleCheckingEnabled(boolean))             *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.HttpClient.setConnectionTimeout(int)](org/apache/commons/httpclient/HttpClient.html#setConnectionTimeout(int))             *Use [`HttpConnectionParams.setConnectionTimeout(int)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setConnectionTimeout(int)), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.HttpConnection.setConnectionTimeout(int)](org/apache/commons/httpclient/HttpConnection.html#setConnectionTimeout(int))             *Use [`HttpConnectionParams.setConnectionTimeout(int)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setConnectionTimeout(int)), [`HttpConnection.getParams()`](org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| [org.apache.commons.httpclient.HttpState.setCookiePolicy(int)](org/apache/commons/httpclient/HttpState.html#setCookiePolicy(int))             *Use [`HttpMethodParams.setCookiePolicy(String)`](org/apache/commons/httpclient/params/HttpMethodParams.html#setCookiePolicy(java.lang.String)), [`HttpMethod.getParams()`](org/apache/commons/httpclient/HttpMethod.html#getParams()).* |
| [org.apache.commons.httpclient.HttpState.setCredentials(String, String, Credentials)](org/apache/commons/httpclient/HttpState.html#setCredentials(java.lang.String, java.lang.String, org.apache.commons.httpclient.Credentials))             *use #setCredentials(AuthScope, Credentials)* |
| [org.apache.commons.httpclient.cookie.CookiePolicy.setDefaultPolicy(int)](org/apache/commons/httpclient/cookie/CookiePolicy.html#setDefaultPolicy(int))             *Use [`CookiePolicy.registerCookieSpec(String, Class)`](org/apache/commons/httpclient/cookie/CookiePolicy.html#registerCookieSpec(java.lang.String, java.lang.Class))* |
| [org.apache.commons.httpclient.NTCredentials.setDomain(String)](org/apache/commons/httpclient/NTCredentials.html#setDomain(java.lang.String))             *Do not use. The NTCredentials objects should be immutable* |
| [org.apache.commons.httpclient.NTCredentials.setHost(String)](org/apache/commons/httpclient/NTCredentials.html#setHost(java.lang.String))             *Do not use. The NTCredentials objects should be immutable* |
| [org.apache.commons.httpclient.HostConfiguration.setHost(String, String, int, Protocol)](org/apache/commons/httpclient/HostConfiguration.html#setHost(java.lang.String, java.lang.String, int, org.apache.commons.httpclient.protocol.Protocol))             *#setHost(String, int, Protocol)* |
| [org.apache.commons.httpclient.HttpMethodBase.setHostConfiguration(HostConfiguration)](org/apache/commons/httpclient/HttpMethodBase.html#setHostConfiguration(org.apache.commons.httpclient.HostConfiguration))             *no longer applicable* |
| [org.apache.commons.httpclient.HttpMethodBase.setHttp11(boolean)](org/apache/commons/httpclient/HttpMethodBase.html#setHttp11(boolean))             *Use [`HttpMethodParams.setVersion(HttpVersion)`](org/apache/commons/httpclient/params/HttpMethodParams.html#setVersion(org.apache.commons.httpclient.HttpVersion))* |
| [org.apache.commons.httpclient.HttpClient.setHttpConnectionFactoryTimeout(long)](org/apache/commons/httpclient/HttpClient.html#setHttpConnectionFactoryTimeout(long))             *Use [`HttpClientParams.setConnectionManagerTimeout(long)`](org/apache/commons/httpclient/params/HttpClientParams.html#setConnectionManagerTimeout(long)), [`HttpClient.getParams()`](org/apache/commons/httpclient/HttpClient.html#getParams())* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.setMaxConnectionsPerHost(int)](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#setMaxConnectionsPerHost(int))             *Use [`HttpConnectionManagerParams.setDefaultMaxConnectionsPerHost(int)`](org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#setDefaultMaxConnectionsPerHost(int)), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.MultiThreadedHttpConnectionManager.setMaxTotalConnections(int)](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#setMaxTotalConnections(int))             *Use [`HttpConnectionManagerParams.setMaxTotalConnections(int)`](org/apache/commons/httpclient/params/HttpConnectionManagerParams.html#setMaxTotalConnections(int)), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.HttpMethodBase.setMethodRetryHandler(MethodRetryHandler)](org/apache/commons/httpclient/HttpMethodBase.html#setMethodRetryHandler(org.apache.commons.httpclient.MethodRetryHandler))             *use [`HttpMethodParams`](org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| [org.apache.commons.httpclient.UsernamePasswordCredentials.setPassword(String)](org/apache/commons/httpclient/UsernamePasswordCredentials.html#setPassword(java.lang.String))             *Do not use. The UsernamePasswordCredentials objects should be immutable* |
| [org.apache.commons.httpclient.HttpState.setProxyCredentials(String, String, Credentials)](org/apache/commons/httpclient/HttpState.html#setProxyCredentials(java.lang.String, java.lang.String, org.apache.commons.httpclient.Credentials))             *use #setProxyCredentials(AuthScope, Credentials)* |
| [org.apache.commons.httpclient.URIException.setReason(String)](org/apache/commons/httpclient/URIException.html#setReason(java.lang.String))             *Callers should instead set this via a parameter to the constructor.* |
| [org.apache.commons.httpclient.HttpException.setReason(String)](org/apache/commons/httpclient/HttpException.html#setReason(java.lang.String))             *HttpClient no longer uses this for itself. It is only provided for compatibility with existing clients, and will be removed in a future release.* |
| [org.apache.commons.httpclient.URIException.setReasonCode(int)](org/apache/commons/httpclient/URIException.html#setReasonCode(int))             *Callers should set the reason code as a parameter to the constructor.* |
| [org.apache.commons.httpclient.HttpException.setReasonCode(int)](org/apache/commons/httpclient/HttpException.html#setReasonCode(int))             *HttpClient no longer uses this for itself. It is only provided for compatibility with existing clients, and will be removed in a future release.* |
| [org.apache.commons.httpclient.methods.EntityEnclosingMethod.setRequestBody(InputStream)](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestBody(java.io.InputStream))             *use [`EntityEnclosingMethod.setRequestEntity(RequestEntity)`](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestEntity(org.apache.commons.httpclient.methods.RequestEntity))* |
| [org.apache.commons.httpclient.methods.EntityEnclosingMethod.setRequestBody(String)](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestBody(java.lang.String))             *use [`EntityEnclosingMethod.setRequestEntity(RequestEntity)`](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestEntity(org.apache.commons.httpclient.methods.RequestEntity))* |
| [org.apache.commons.httpclient.methods.EntityEnclosingMethod.setRequestContentLength(int)](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestContentLength(int))             *Use [`EntityEnclosingMethod.setContentChunked(boolean)`](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setContentChunked(boolean)) or [`EntityEnclosingMethod.setRequestEntity(RequestEntity)`](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestEntity(org.apache.commons.httpclient.methods.RequestEntity))* |
| [org.apache.commons.httpclient.methods.EntityEnclosingMethod.setRequestContentLength(long)](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestContentLength(long))             *Use [`EntityEnclosingMethod.setContentChunked(boolean)`](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setContentChunked(boolean)) or [`EntityEnclosingMethod.setRequestEntity(RequestEntity)`](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html#setRequestEntity(org.apache.commons.httpclient.methods.RequestEntity))* |
| [org.apache.commons.httpclient.HttpConnection.setSendBufferSize(int)](org/apache/commons/httpclient/HttpConnection.html#setSendBufferSize(int))             *Use [`HttpConnectionParams.setSendBufferSize(int)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setSendBufferSize(int)), [`HttpConnection.getParams()`](org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| [org.apache.commons.httpclient.HttpConnection.setSoTimeout(int)](org/apache/commons/httpclient/HttpConnection.html#setSoTimeout(int))             *Use [`HttpConnectionParams.setSoTimeout(int)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setSoTimeout(int)), [`HttpConnection.getParams()`](org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| [org.apache.commons.httpclient.HttpConnection.setStaleCheckingEnabled(boolean)](org/apache/commons/httpclient/HttpConnection.html#setStaleCheckingEnabled(boolean))             *Use [`HttpConnectionParams.setStaleCheckingEnabled(boolean)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setStaleCheckingEnabled(boolean)), [`HttpConnection.getParams()`](org/apache/commons/httpclient/HttpConnection.html#getParams()).* |
| [org.apache.commons.httpclient.HttpClient.setStrictMode(boolean)](org/apache/commons/httpclient/HttpClient.html#setStrictMode(boolean))             *Use [`DefaultHttpParams.setParameter(String, Object)`](org/apache/commons/httpclient/params/DefaultHttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| [org.apache.commons.httpclient.HttpMethodBase.setStrictMode(boolean)](org/apache/commons/httpclient/HttpMethodBase.html#setStrictMode(boolean))             *Use [`HttpParams.setParameter(String, Object)`](org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| [org.apache.commons.httpclient.HttpMethod.setStrictMode(boolean)](org/apache/commons/httpclient/HttpMethod.html#setStrictMode(boolean))             *Use [`HttpParams.setParameter(String, Object)`](org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| [org.apache.commons.httpclient.HttpClient.setTimeout(int)](org/apache/commons/httpclient/HttpClient.html#setTimeout(int))             *Use [`HttpConnectionParams.setSoTimeout(int)`](org/apache/commons/httpclient/params/HttpConnectionParams.html#setSoTimeout(int)), [`HttpConnectionManager.getParams()`](org/apache/commons/httpclient/HttpConnectionManager.html#getParams()).* |
| [org.apache.commons.httpclient.methods.ExpectContinueMethod.setUseExpectHeader(boolean)](org/apache/commons/httpclient/methods/ExpectContinueMethod.html#setUseExpectHeader(boolean))             *Use [`HttpMethodParams`](org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| [org.apache.commons.httpclient.UsernamePasswordCredentials.setUserName(String)](org/apache/commons/httpclient/UsernamePasswordCredentials.html#setUserName(java.lang.String))             *Do not use. The UsernamePasswordCredentials objects should be immutable* |
| [org.apache.commons.httpclient.HttpConnection.setVirtualHost(String)](org/apache/commons/httpclient/HttpConnection.html#setVirtualHost(java.lang.String))             *no longer applicable* |
| [org.apache.commons.httpclient.HttpConnection.shutdownOutput()](org/apache/commons/httpclient/HttpConnection.html#shutdownOutput())             *unused* |

| **Deprecated Constructors** | |
| --- | --- |
| [org.apache.commons.httpclient.auth.AuthSchemeBase(String)](org/apache/commons/httpclient/auth/AuthSchemeBase.html#AuthSchemeBase(java.lang.String))             *Use parameterless constructor and [`AuthScheme.processChallenge(String)`](org/apache/commons/httpclient/auth/AuthScheme.html#processChallenge(java.lang.String)) method* |
| [org.apache.commons.httpclient.auth.BasicScheme(String)](org/apache/commons/httpclient/auth/BasicScheme.html#BasicScheme(java.lang.String))             *Use parameterless constructor and [`AuthScheme.processChallenge(String)`](org/apache/commons/httpclient/auth/AuthScheme.html#processChallenge(java.lang.String)) method* |
| [org.apache.commons.httpclient.ConnectMethod()](org/apache/commons/httpclient/ConnectMethod.html#ConnectMethod())             *use #ConnectMethod(HttpHost); Create a connect method.* |
| [org.apache.commons.httpclient.ConnectMethod(HttpMethod)](org/apache/commons/httpclient/ConnectMethod.html#ConnectMethod(org.apache.commons.httpclient.HttpMethod))             *the wrapped method is no longer used Create a connect method wrapping the existing method* |
| [org.apache.commons.httpclient.ContentLengthInputStream(InputStream, int)](org/apache/commons/httpclient/ContentLengthInputStream.html#ContentLengthInputStream(java.io.InputStream, int))             *use [`ContentLengthInputStream.ContentLengthInputStream(InputStream, long)`](org/apache/commons/httpclient/ContentLengthInputStream.html#ContentLengthInputStream(java.io.InputStream, long)) Creates a new length limited stream* |
| [org.apache.commons.httpclient.auth.DigestScheme(String)](org/apache/commons/httpclient/auth/DigestScheme.html#DigestScheme(java.lang.String))             *Use parameterless constructor and [`AuthScheme.processChallenge(String)`](org/apache/commons/httpclient/auth/AuthScheme.html#processChallenge(java.lang.String)) method* |
| [org.apache.commons.httpclient.HttpConnection(String, int, String, String, int, Protocol)](org/apache/commons/httpclient/HttpConnection.html#HttpConnection(java.lang.String, int, java.lang.String, java.lang.String, int, org.apache.commons.httpclient.protocol.Protocol))             *use #HttpConnection(String, int, String, int, Protocol)* |
| [org.apache.commons.httpclient.NTCredentials()](org/apache/commons/httpclient/NTCredentials.html#NTCredentials())             *Do not use. Null user name, domain & host no longer allowed* |
| [org.apache.commons.httpclient.protocol.Protocol(String, SecureProtocolSocketFactory, int)](org/apache/commons/httpclient/protocol/Protocol.html#Protocol(java.lang.String, org.apache.commons.httpclient.protocol.SecureProtocolSocketFactory, int))             *Use the constructor that uses ProtocolSocketFactory, this version of the constructor is only kept for backwards API compatibility.* |
| [org.apache.commons.httpclient.auth.RFC2617Scheme(String)](org/apache/commons/httpclient/auth/RFC2617Scheme.html#RFC2617Scheme(java.lang.String))             *Use parameterless constructor and [`AuthScheme.processChallenge(String)`](org/apache/commons/httpclient/auth/AuthScheme.html#processChallenge(java.lang.String)) method* |
| [org.apache.commons.httpclient.methods.StringRequestEntity(String)](org/apache/commons/httpclient/methods/StringRequestEntity.html#StringRequestEntity(java.lang.String))             *use [`StringRequestEntity.StringRequestEntity(String, String, String)`](org/apache/commons/httpclient/methods/StringRequestEntity.html#StringRequestEntity(java.lang.String, java.lang.String, java.lang.String)) instead* |
| [org.apache.commons.httpclient.URI(char[])](org/apache/commons/httpclient/URI.html#URI(char[]))             *Use #URI(String, boolean)* |
| [org.apache.commons.httpclient.URI(char[], String)](org/apache/commons/httpclient/URI.html#URI(char[], java.lang.String))             *Use #URI(String, boolean, String)* |
| [org.apache.commons.httpclient.URI(String)](org/apache/commons/httpclient/URI.html#URI(java.lang.String))             *Use #URI(String, boolean)* |
| [org.apache.commons.httpclient.URI(String, String)](org/apache/commons/httpclient/URI.html#URI(java.lang.String, java.lang.String))             *Use #URI(String, boolean, String)* |
| [org.apache.commons.httpclient.URI(URI, String)](org/apache/commons/httpclient/URI.html#URI(org.apache.commons.httpclient.URI, java.lang.String))             *Use #URI(URI, String, boolean)* |
| [org.apache.commons.httpclient.UsernamePasswordCredentials()](org/apache/commons/httpclient/UsernamePasswordCredentials.html#UsernamePasswordCredentials())             *Do not use. Null user name no longer allowed* |

---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](overview-summary.html) | Package | Class | Use | [**Tree**](overview-tree.html) | **Deprecated** | [**Index**](index-all.html) | [**Help**](help-doc.html) | | |  |
| PREV   NEXT | [**FRAMES**](index.html?deprecated-list.html)    [**NO FRAMES**](deprecated-list.html) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
**All Classes**
  

|  |
| --- |
| [AuthChallengeException](org/apache/commons/httpclient/auth/AuthChallengeException.html "class in org.apache.commons.httpclient.auth")   [AuthChallengeParser](org/apache/commons/httpclient/auth/AuthChallengeParser.html "class in org.apache.commons.httpclient.auth")   [AuthChallengeProcessor](org/apache/commons/httpclient/auth/AuthChallengeProcessor.html "class in org.apache.commons.httpclient.auth")   [AuthenticationException](org/apache/commons/httpclient/auth/AuthenticationException.html "class in org.apache.commons.httpclient.auth")   [AuthPolicy](org/apache/commons/httpclient/auth/AuthPolicy.html "class in org.apache.commons.httpclient.auth")   [*AuthScheme*](org/apache/commons/httpclient/auth/AuthScheme.html "interface in org.apache.commons.httpclient.auth")   [AuthSchemeBase](org/apache/commons/httpclient/auth/AuthSchemeBase.html "class in org.apache.commons.httpclient.auth")   [AuthScope](org/apache/commons/httpclient/auth/AuthScope.html "class in org.apache.commons.httpclient.auth")   [AuthState](org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth")   [BasicScheme](org/apache/commons/httpclient/auth/BasicScheme.html "class in org.apache.commons.httpclient.auth")   [ByteArrayPartSource](org/apache/commons/httpclient/methods/multipart/ByteArrayPartSource.html "class in org.apache.commons.httpclient.methods.multipart")   [ByteArrayRequestEntity](org/apache/commons/httpclient/methods/ByteArrayRequestEntity.html "class in org.apache.commons.httpclient.methods")   [ChunkedInputStream](org/apache/commons/httpclient/ChunkedInputStream.html "class in org.apache.commons.httpclient")   [ChunkedOutputStream](org/apache/commons/httpclient/ChunkedOutputStream.html "class in org.apache.commons.httpclient")   [CircularRedirectException](org/apache/commons/httpclient/CircularRedirectException.html "class in org.apache.commons.httpclient")   [ConnectionPoolTimeoutException](org/apache/commons/httpclient/ConnectionPoolTimeoutException.html "class in org.apache.commons.httpclient")   [ConnectMethod](org/apache/commons/httpclient/ConnectMethod.html "class in org.apache.commons.httpclient")   [ConnectTimeoutException](org/apache/commons/httpclient/ConnectTimeoutException.html "class in org.apache.commons.httpclient")   [ContentLengthInputStream](org/apache/commons/httpclient/ContentLengthInputStream.html "class in org.apache.commons.httpclient")   [ControllerThreadSocketFactory](org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [ControllerThreadSocketFactory.SocketTask](org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.SocketTask.html "class in org.apache.commons.httpclient.protocol")   [Cookie](org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient")   [Cookie2](org/apache/commons/httpclient/cookie/Cookie2.html "class in org.apache.commons.httpclient.cookie")   [*CookieAttributeHandler*](org/apache/commons/httpclient/cookie/CookieAttributeHandler.html "interface in org.apache.commons.httpclient.cookie")   [CookieOrigin](org/apache/commons/httpclient/cookie/CookieOrigin.html "class in org.apache.commons.httpclient.cookie")   [CookiePathComparator](org/apache/commons/httpclient/cookie/CookiePathComparator.html "class in org.apache.commons.httpclient.cookie")   [CookiePolicy](org/apache/commons/httpclient/cookie/CookiePolicy.html "class in org.apache.commons.httpclient.cookie")   [*CookieSpec*](org/apache/commons/httpclient/cookie/CookieSpec.html "interface in org.apache.commons.httpclient.cookie")   [CookieSpecBase](org/apache/commons/httpclient/cookie/CookieSpecBase.html "class in org.apache.commons.httpclient.cookie")   [*CookieVersionSupport*](org/apache/commons/httpclient/cookie/CookieVersionSupport.html "interface in org.apache.commons.httpclient.cookie")   [*Credentials*](org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient")   [CredentialsNotAvailableException](org/apache/commons/httpclient/auth/CredentialsNotAvailableException.html "class in org.apache.commons.httpclient.auth")   [*CredentialsProvider*](org/apache/commons/httpclient/auth/CredentialsProvider.html "interface in org.apache.commons.httpclient.auth")   [DateParseException](org/apache/commons/httpclient/util/DateParseException.html "class in org.apache.commons.httpclient.util")   [DateParser](org/apache/commons/httpclient/util/DateParser.html "class in org.apache.commons.httpclient.util")   [DateUtil](org/apache/commons/httpclient/util/DateUtil.html "class in org.apache.commons.httpclient.util")   [DefaultHttpMethodRetryHandler](org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html "class in org.apache.commons.httpclient")   [DefaultHttpParams](org/apache/commons/httpclient/params/DefaultHttpParams.html "class in org.apache.commons.httpclient.params")   [DefaultHttpParamsFactory](org/apache/commons/httpclient/params/DefaultHttpParamsFactory.html "class in org.apache.commons.httpclient.params")   [DefaultMethodRetryHandler](org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient")   [DefaultProtocolSocketFactory](org/apache/commons/httpclient/protocol/DefaultProtocolSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [DeleteMethod](org/apache/commons/httpclient/methods/DeleteMethod.html "class in org.apache.commons.httpclient.methods")   [DigestScheme](org/apache/commons/httpclient/auth/DigestScheme.html "class in org.apache.commons.httpclient.auth")   [EncodingUtil](org/apache/commons/httpclient/util/EncodingUtil.html "class in org.apache.commons.httpclient.util")   [EntityEnclosingMethod](org/apache/commons/httpclient/methods/EntityEnclosingMethod.html "class in org.apache.commons.httpclient.methods")   [ExceptionUtil](org/apache/commons/httpclient/util/ExceptionUtil.html "class in org.apache.commons.httpclient.util")   [ExpectContinueMethod](org/apache/commons/httpclient/methods/ExpectContinueMethod.html "class in org.apache.commons.httpclient.methods")   [FilePart](org/apache/commons/httpclient/methods/multipart/FilePart.html "class in org.apache.commons.httpclient.methods.multipart")   [FilePartSource](org/apache/commons/httpclient/methods/multipart/FilePartSource.html "class in org.apache.commons.httpclient.methods.multipart")   [FileRequestEntity](org/apache/commons/httpclient/methods/FileRequestEntity.html "class in org.apache.commons.httpclient.methods")   [GetMethod](org/apache/commons/httpclient/methods/GetMethod.html "class in org.apache.commons.httpclient.methods")   [Header](org/apache/commons/httpclient/Header.html "class in org.apache.commons.httpclient")   [HeaderElement](org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient")   [HeaderGroup](org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient")   [HeadMethod](org/apache/commons/httpclient/methods/HeadMethod.html "class in org.apache.commons.httpclient.methods")   [HostConfiguration](org/apache/commons/httpclient/HostConfiguration.html "class in org.apache.commons.httpclient")   [HostParams](org/apache/commons/httpclient/params/HostParams.html "class in org.apache.commons.httpclient.params")   [HttpAuthenticator](org/apache/commons/httpclient/auth/HttpAuthenticator.html "class in org.apache.commons.httpclient.auth")   [HttpAuthRealm](org/apache/commons/httpclient/auth/HttpAuthRealm.html "class in org.apache.commons.httpclient.auth")   [HttpClient](org/apache/commons/httpclient/HttpClient.html "class in org.apache.commons.httpclient")   [HttpClientError](org/apache/commons/httpclient/HttpClientError.html "class in org.apache.commons.httpclient")   [HttpClientParams](org/apache/commons/httpclient/params/HttpClientParams.html "class in org.apache.commons.httpclient.params")   [HttpConnection](org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient")   [*HttpConnectionManager*](org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient")   [HttpConnectionManagerParams](org/apache/commons/httpclient/params/HttpConnectionManagerParams.html "class in org.apache.commons.httpclient.params")   [HttpConnectionParams](org/apache/commons/httpclient/params/HttpConnectionParams.html "class in org.apache.commons.httpclient.params")   [HttpConstants](org/apache/commons/httpclient/HttpConstants.html "class in org.apache.commons.httpclient")   [HttpContentTooLargeException](org/apache/commons/httpclient/HttpContentTooLargeException.html "class in org.apache.commons.httpclient")   [HttpException](org/apache/commons/httpclient/HttpException.html "class in org.apache.commons.httpclient")   [HttpHost](org/apache/commons/httpclient/HttpHost.html "class in org.apache.commons.httpclient")   [*HttpMethod*](org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")   [HttpMethodBase](org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient")   [HttpMethodParams](org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")   [*HttpMethodRetryHandler*](org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")   [*HttpParams*](org/apache/commons/httpclient/params/HttpParams.html "interface in org.apache.commons.httpclient.params")   [*HttpParamsFactory*](org/apache/commons/httpclient/params/HttpParamsFactory.html "interface in org.apache.commons.httpclient.params")   [HttpParser](org/apache/commons/httpclient/HttpParser.html "class in org.apache.commons.httpclient")   [HttpRecoverableException](org/apache/commons/httpclient/HttpRecoverableException.html "class in org.apache.commons.httpclient")   [HttpState](org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient")   [HttpStatus](org/apache/commons/httpclient/HttpStatus.html "class in org.apache.commons.httpclient")   [HttpsURL](org/apache/commons/httpclient/HttpsURL.html "class in org.apache.commons.httpclient")   [HttpURL](org/apache/commons/httpclient/HttpURL.html "class in org.apache.commons.httpclient")   [HttpURLConnection](org/apache/commons/httpclient/util/HttpURLConnection.html "class in org.apache.commons.httpclient.util")   [HttpVersion](org/apache/commons/httpclient/HttpVersion.html "class in org.apache.commons.httpclient")   [IdleConnectionHandler](org/apache/commons/httpclient/util/IdleConnectionHandler.html "class in org.apache.commons.httpclient.util")   [IdleConnectionTimeoutThread](org/apache/commons/httpclient/util/IdleConnectionTimeoutThread.html "class in org.apache.commons.httpclient.util")   [IgnoreCookiesSpec](org/apache/commons/httpclient/cookie/IgnoreCookiesSpec.html "class in org.apache.commons.httpclient.cookie")   [InputStreamRequestEntity](org/apache/commons/httpclient/methods/InputStreamRequestEntity.html "class in org.apache.commons.httpclient.methods")   [InvalidCredentialsException](org/apache/commons/httpclient/auth/InvalidCredentialsException.html "class in org.apache.commons.httpclient.auth")   [InvalidRedirectLocationException](org/apache/commons/httpclient/InvalidRedirectLocationException.html "class in org.apache.commons.httpclient")   [LangUtils](org/apache/commons/httpclient/util/LangUtils.html "class in org.apache.commons.httpclient.util")   [MalformedChallengeException](org/apache/commons/httpclient/auth/MalformedChallengeException.html "class in org.apache.commons.httpclient.auth")   [MalformedCookieException](org/apache/commons/httpclient/cookie/MalformedCookieException.html "class in org.apache.commons.httpclient.cookie")   [*MethodRetryHandler*](org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient")   [MultipartPostMethod](org/apache/commons/httpclient/methods/MultipartPostMethod.html "class in org.apache.commons.httpclient.methods")   [MultipartRequestEntity](org/apache/commons/httpclient/methods/multipart/MultipartRequestEntity.html "class in org.apache.commons.httpclient.methods.multipart")   [MultiThreadedHttpConnectionManager](org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html "class in org.apache.commons.httpclient")   [NameValuePair](org/apache/commons/httpclient/NameValuePair.html "class in org.apache.commons.httpclient")   [NetscapeDraftSpec](org/apache/commons/httpclient/cookie/NetscapeDraftSpec.html "class in org.apache.commons.httpclient.cookie")   [NoHttpResponseException](org/apache/commons/httpclient/NoHttpResponseException.html "class in org.apache.commons.httpclient")   [NTCredentials](org/apache/commons/httpclient/NTCredentials.html "class in org.apache.commons.httpclient")   [NTLMScheme](org/apache/commons/httpclient/auth/NTLMScheme.html "class in org.apache.commons.httpclient.auth")   [OptionsMethod](org/apache/commons/httpclient/methods/OptionsMethod.html "class in org.apache.commons.httpclient.methods")   [ParameterFormatter](org/apache/commons/httpclient/util/ParameterFormatter.html "class in org.apache.commons.httpclient.util")   [ParameterParser](org/apache/commons/httpclient/util/ParameterParser.html "class in org.apache.commons.httpclient.util")   [Part](org/apache/commons/httpclient/methods/multipart/Part.html "class in org.apache.commons.httpclient.methods.multipart")   [PartBase](org/apache/commons/httpclient/methods/multipart/PartBase.html "class in org.apache.commons.httpclient.methods.multipart")   [*PartSource*](org/apache/commons/httpclient/methods/multipart/PartSource.html "interface in org.apache.commons.httpclient.methods.multipart")   [PostMethod](org/apache/commons/httpclient/methods/PostMethod.html "class in org.apache.commons.httpclient.methods")   [Protocol](org/apache/commons/httpclient/protocol/Protocol.html "class in org.apache.commons.httpclient.protocol")   [ProtocolException](org/apache/commons/httpclient/ProtocolException.html "class in org.apache.commons.httpclient")   [*ProtocolSocketFactory*](org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol")   [ProxyClient](org/apache/commons/httpclient/ProxyClient.html "class in org.apache.commons.httpclient")   [ProxyClient.ConnectResponse](org/apache/commons/httpclient/ProxyClient.ConnectResponse.html "class in org.apache.commons.httpclient")   [ProxyHost](org/apache/commons/httpclient/ProxyHost.html "class in org.apache.commons.httpclient")   [PutMethod](org/apache/commons/httpclient/methods/PutMethod.html "class in org.apache.commons.httpclient.methods")   [RedirectException](org/apache/commons/httpclient/RedirectException.html "class in org.apache.commons.httpclient")   [ReflectionSocketFactory](org/apache/commons/httpclient/protocol/ReflectionSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [*RequestEntity*](org/apache/commons/httpclient/methods/RequestEntity.html "interface in org.apache.commons.httpclient.methods")   [RFC2109Spec](org/apache/commons/httpclient/cookie/RFC2109Spec.html "class in org.apache.commons.httpclient.cookie")   [RFC2617Scheme](org/apache/commons/httpclient/auth/RFC2617Scheme.html "class in org.apache.commons.httpclient.auth")   [RFC2965Spec](org/apache/commons/httpclient/cookie/RFC2965Spec.html "class in org.apache.commons.httpclient.cookie")   [*SecureProtocolSocketFactory*](org/apache/commons/httpclient/protocol/SecureProtocolSocketFactory.html "interface in org.apache.commons.httpclient.protocol")   [SimpleHttpConnectionManager](org/apache/commons/httpclient/SimpleHttpConnectionManager.html "class in org.apache.commons.httpclient")   [SSLProtocolSocketFactory](org/apache/commons/httpclient/protocol/SSLProtocolSocketFactory.html "class in org.apache.commons.httpclient.protocol")   [StatusLine](org/apache/commons/httpclient/StatusLine.html "class in org.apache.commons.httpclient")   [StringPart](org/apache/commons/httpclient/methods/multipart/StringPart.html "class in org.apache.commons.httpclient.methods.multipart")   [StringRequestEntity](org/apache/commons/httpclient/methods/StringRequestEntity.html "class in org.apache.commons.httpclient.methods")   [TimeoutController](org/apache/commons/httpclient/util/TimeoutController.html "class in org.apache.commons.httpclient.util")   [TimeoutController.TimeoutException](org/apache/commons/httpclient/util/TimeoutController.TimeoutException.html "class in org.apache.commons.httpclient.util")   [TraceMethod](org/apache/commons/httpclient/methods/TraceMethod.html "class in org.apache.commons.httpclient.methods")   [URI](org/apache/commons/httpclient/URI.html "class in org.apache.commons.httpclient")   [URI.DefaultCharsetChanged](org/apache/commons/httpclient/URI.DefaultCharsetChanged.html "class in org.apache.commons.httpclient")   [URI.LocaleToCharsetMap](org/apache/commons/httpclient/URI.LocaleToCharsetMap.html "class in org.apache.commons.httpclient")   [URIException](org/apache/commons/httpclient/URIException.html "class in org.apache.commons.httpclient")   [URIUtil](org/apache/commons/httpclient/util/URIUtil.html "class in org.apache.commons.httpclient.util")   [URIUtil.Coder](org/apache/commons/httpclient/util/URIUtil.Coder.html "class in org.apache.commons.httpclient.util")   [UsernamePasswordCredentials](org/apache/commons/httpclient/UsernamePasswordCredentials.html "class in org.apache.commons.httpclient") |

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | Class | Use | **Tree** | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| PREV   [**NEXT**](../../../../org/apache/commons/httpclient/auth/package-tree.html) | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/package-tree.html)    [**NO FRAMES**](package-tree.html) |




---



## Hierarchy For Package org.apache.commons.httpclient

**Package Hierarchies:**: [All Packages](../../../../overview-tree.html)

---

## Class Hierarchy

* java.lang.[**Object**](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")
  * org.apache.commons.httpclient.[**DefaultHttpMethodRetryHandler**](../../../../org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html "class in org.apache.commons.httpclient") (implements org.apache.commons.httpclient.[HttpMethodRetryHandler](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient"))* org.apache.commons.httpclient.[**DefaultMethodRetryHandler**](../../../../org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient") (implements org.apache.commons.httpclient.[MethodRetryHandler](../../../../org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient"))* org.apache.commons.httpclient.[**HeaderGroup**](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HostConfiguration**](../../../../org/apache/commons/httpclient/HostConfiguration.html "class in org.apache.commons.httpclient") (implements java.lang.[Cloneable](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Cloneable.html "class or interface in java.lang"))* org.apache.commons.httpclient.[**HttpClient**](../../../../org/apache/commons/httpclient/HttpClient.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpConnection**](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpConstants**](../../../../org/apache/commons/httpclient/HttpConstants.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpHost**](../../../../org/apache/commons/httpclient/HttpHost.html "class in org.apache.commons.httpclient") (implements java.lang.[Cloneable](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Cloneable.html "class or interface in java.lang"))
                  * org.apache.commons.httpclient.[**ProxyHost**](../../../../org/apache/commons/httpclient/ProxyHost.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpMethodBase**](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient") (implements org.apache.commons.httpclient.[HttpMethod](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient"))
                    * org.apache.commons.httpclient.[**ConnectMethod**](../../../../org/apache/commons/httpclient/ConnectMethod.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpParser**](../../../../org/apache/commons/httpclient/HttpParser.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpState**](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpStatus**](../../../../org/apache/commons/httpclient/HttpStatus.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpVersion**](../../../../org/apache/commons/httpclient/HttpVersion.html "class in org.apache.commons.httpclient") (implements java.lang.[Comparable](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Comparable.html "class or interface in java.lang")<T>)* java.io.[**InputStream**](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io") (implements java.io.[Closeable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Closeable.html "class or interface in java.io"))
                              * org.apache.commons.httpclient.[**ChunkedInputStream**](../../../../org/apache/commons/httpclient/ChunkedInputStream.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**ContentLengthInputStream**](../../../../org/apache/commons/httpclient/ContentLengthInputStream.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**MultiThreadedHttpConnectionManager**](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html "class in org.apache.commons.httpclient") (implements org.apache.commons.httpclient.[HttpConnectionManager](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient"))* org.apache.commons.httpclient.[**NameValuePair**](../../../../org/apache/commons/httpclient/NameValuePair.html "class in org.apache.commons.httpclient") (implements java.io.[Serializable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Serializable.html "class or interface in java.io"))
                                  * org.apache.commons.httpclient.[**Cookie**](../../../../org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient") (implements java.util.[Comparator](http://java.sun.com/j2se/1.5.0/docs/api/java/util/Comparator.html "class or interface in java.util")<T>, java.io.[Serializable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Serializable.html "class or interface in java.io"))* org.apache.commons.httpclient.[**Header**](../../../../org/apache/commons/httpclient/Header.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HeaderElement**](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient")* java.io.[**OutputStream**](http://java.sun.com/j2se/1.5.0/docs/api/java/io/OutputStream.html "class or interface in java.io") (implements java.io.[Closeable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Closeable.html "class or interface in java.io"), java.io.[Flushable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Flushable.html "class or interface in java.io"))
                                    * org.apache.commons.httpclient.[**ChunkedOutputStream**](../../../../org/apache/commons/httpclient/ChunkedOutputStream.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**ProxyClient**](../../../../org/apache/commons/httpclient/ProxyClient.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**ProxyClient.ConnectResponse**](../../../../org/apache/commons/httpclient/ProxyClient.ConnectResponse.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**SimpleHttpConnectionManager**](../../../../org/apache/commons/httpclient/SimpleHttpConnectionManager.html "class in org.apache.commons.httpclient") (implements org.apache.commons.httpclient.[HttpConnectionManager](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient"))* org.apache.commons.httpclient.[**StatusLine**](../../../../org/apache/commons/httpclient/StatusLine.html "class in org.apache.commons.httpclient")* java.lang.[**Throwable**](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Throwable.html "class or interface in java.lang") (implements java.io.[Serializable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Serializable.html "class or interface in java.io"))
                                              * java.lang.[**Error**](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Error.html "class or interface in java.lang")
                                                * org.apache.commons.httpclient.[**HttpClientError**](../../../../org/apache/commons/httpclient/HttpClientError.html "class in org.apache.commons.httpclient")* java.lang.[**Exception**](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Exception.html "class or interface in java.lang")
                                                  * java.io.[**IOException**](http://java.sun.com/j2se/1.5.0/docs/api/java/io/IOException.html "class or interface in java.io")
                                                    * org.apache.commons.httpclient.[**HttpException**](../../../../org/apache/commons/httpclient/HttpException.html "class in org.apache.commons.httpclient")
                                                      * org.apache.commons.httpclient.[**HttpContentTooLargeException**](../../../../org/apache/commons/httpclient/HttpContentTooLargeException.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpRecoverableException**](../../../../org/apache/commons/httpclient/HttpRecoverableException.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**ProtocolException**](../../../../org/apache/commons/httpclient/ProtocolException.html "class in org.apache.commons.httpclient")
                                                            * org.apache.commons.httpclient.[**RedirectException**](../../../../org/apache/commons/httpclient/RedirectException.html "class in org.apache.commons.httpclient")
                                                              * org.apache.commons.httpclient.[**CircularRedirectException**](../../../../org/apache/commons/httpclient/CircularRedirectException.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**InvalidRedirectLocationException**](../../../../org/apache/commons/httpclient/InvalidRedirectLocationException.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**URIException**](../../../../org/apache/commons/httpclient/URIException.html "class in org.apache.commons.httpclient")* java.io.[**InterruptedIOException**](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InterruptedIOException.html "class or interface in java.io")
                                                        * org.apache.commons.httpclient.[**ConnectTimeoutException**](../../../../org/apache/commons/httpclient/ConnectTimeoutException.html "class in org.apache.commons.httpclient")
                                                          * org.apache.commons.httpclient.[**ConnectionPoolTimeoutException**](../../../../org/apache/commons/httpclient/ConnectionPoolTimeoutException.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**NoHttpResponseException**](../../../../org/apache/commons/httpclient/NoHttpResponseException.html "class in org.apache.commons.httpclient")* java.lang.[**RuntimeException**](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/RuntimeException.html "class or interface in java.lang")
                                                      * org.apache.commons.httpclient.[**URI.DefaultCharsetChanged**](../../../../org/apache/commons/httpclient/URI.DefaultCharsetChanged.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**URI**](../../../../org/apache/commons/httpclient/URI.html "class in org.apache.commons.httpclient") (implements java.lang.[Cloneable](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Cloneable.html "class or interface in java.lang"), java.lang.[Comparable](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Comparable.html "class or interface in java.lang")<T>, java.io.[Serializable](http://java.sun.com/j2se/1.5.0/docs/api/java/io/Serializable.html "class or interface in java.io"))
                                                * org.apache.commons.httpclient.[**HttpURL**](../../../../org/apache/commons/httpclient/HttpURL.html "class in org.apache.commons.httpclient")
                                                  * org.apache.commons.httpclient.[**HttpsURL**](../../../../org/apache/commons/httpclient/HttpsURL.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**URI.LocaleToCharsetMap**](../../../../org/apache/commons/httpclient/URI.LocaleToCharsetMap.html "class in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**UsernamePasswordCredentials**](../../../../org/apache/commons/httpclient/UsernamePasswordCredentials.html "class in org.apache.commons.httpclient") (implements org.apache.commons.httpclient.[Credentials](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient"))
                                                    * org.apache.commons.httpclient.[**NTCredentials**](../../../../org/apache/commons/httpclient/NTCredentials.html "class in org.apache.commons.httpclient")

## Interface Hierarchy

* org.apache.commons.httpclient.[**Credentials**](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpConnectionManager**](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpMethod**](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**HttpMethodRetryHandler**](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")* org.apache.commons.httpclient.[**MethodRetryHandler**](../../../../org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient")

---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | Class | Use | **Tree** | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| PREV   [**NEXT**](../../../../org/apache/commons/httpclient/auth/package-tree.html) | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/package-tree.html)    [**NO FRAMES**](package-tree.html) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpMethodBase.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpMethodBase.html)    [**NO FRAMES**](HttpMethodBase.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---



## org.apache.commons.httpclient Class HttpMethodBase

```
java.lang.Object
  ![extended by ](../../../../resources/inherit.gif)org.apache.commons.httpclient.HttpMethodBase
```

**All Implemented Interfaces:**: [HttpMethod](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")

**Direct Known Subclasses:**: [ConnectMethod](../../../../org/apache/commons/httpclient/ConnectMethod.html "class in org.apache.commons.httpclient"), [DeleteMethod](../../../../org/apache/commons/httpclient/methods/DeleteMethod.html "class in org.apache.commons.httpclient.methods"), [ExpectContinueMethod](../../../../org/apache/commons/httpclient/methods/ExpectContinueMethod.html "class in org.apache.commons.httpclient.methods"), [GetMethod](../../../../org/apache/commons/httpclient/methods/GetMethod.html "class in org.apache.commons.httpclient.methods"), [HeadMethod](../../../../org/apache/commons/httpclient/methods/HeadMethod.html "class in org.apache.commons.httpclient.methods"), [OptionsMethod](../../../../org/apache/commons/httpclient/methods/OptionsMethod.html "class in org.apache.commons.httpclient.methods"), [TraceMethod](../../../../org/apache/commons/httpclient/methods/TraceMethod.html "class in org.apache.commons.httpclient.methods")

---

``` public abstract class HttpMethodBase extends Object implements HttpMethod ```

An abstract base implementation of HttpMethod.

At minimum, subclasses will need to override:

* [`getName()`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getName()) to return the approriate name for this method

When a method requires additional request headers, subclasses will typically
want to override:

* [`addRequestHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#addRequestHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))
  to write those headers

When a method expects specific response headers, subclasses may want to
override:

* [`processResponseHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#processResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))
  to handle those headers

**Version:**
:   $Revision: 1425331 $ $Date: 2012-12-22 18:29:41 +0000 (Sat, 22 Dec 2012) $

**Author:**
:   [Remy Maucherat](mailto:remm@apache.org), Rodney Waldhoff, Sean C. Sullivan, [dIon Gillard](mailto:dion@apache.org), [Jeff Dever](mailto:jsdever@apache.org), [Davanum Srinivas](mailto:dims@apache.org), Ortwin Glueck, Eric Johnson, Michael Becke, [Oleg Kalnichevski](mailto:oleg@ural.ru), [Mike Bowler](mailto:mbowler@GargoyleSoftware.com), [Gary Gregory](mailto:ggregory@seagullsw.com), Christian Kohlschuetter

---

| **Field Summary** | |
| --- | --- |
| `protected  HttpVersion` | `effectiveVersion`             HTTP protocol version used for execution of this method. |
| `protected  StatusLine` | `statusLine`             The Status-Line from the response. |



| **Constructor Summary** | |
| --- | --- |
| `HttpMethodBase()`             No-arg constructor. |
| `HttpMethodBase(String uri)`             Constructor specifying a URI. |



| **Method Summary** | |
| --- | --- |
| `void` | `abort()`             Aborts the execution of this method. |
| `protected  void` | `addCookieRequestHeader(HttpState state, HttpConnection conn)`             Generates Cookie request headers for those [`cookie`](../../../../org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient")s that match the given host, port and path. |
| `protected  void` | `addHostRequestHeader(HttpState state, HttpConnection conn)`             Generates Host request header, as long as no Host request header already exists. |
| `protected  void` | `addProxyConnectionHeader(HttpState state, HttpConnection conn)`             Generates Proxy-Connection: Keep-Alive request header when communicating via a proxy server. |
| `void` | `addRequestHeader(Header header)`             Adds the specified request header, NOT overwriting any previous value. |
| `void` | `addRequestHeader(String headerName, String headerValue)`             Adds the specified request header, NOT overwriting any previous value. |
| `protected  void` | `addRequestHeaders(HttpState state, HttpConnection conn)`             Generates all the required request [`header`](../../../../org/apache/commons/httpclient/Header.html "class in org.apache.commons.httpclient")s to be submitted via the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |
| `void` | `addResponseFooter(Header footer)`             Use this method internally to add footers. |
| `protected  void` | `addUserAgentRequestHeader(HttpState state, HttpConnection conn)`             Generates default User-Agent request header, as long as no User-Agent request header already exists. |
| `protected  void` | `checkNotUsed()`             Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the HTTP method has been already [`executed`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), but not [`recycled`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#recycle()). |
| `protected  void` | `checkUsed()`             Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the HTTP method has not been [`executed`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) since last [`recycle`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#recycle()). |
| `int` | `execute(HttpState state, HttpConnection conn)`             Executes this method using the specified `HttpConnection` and `HttpState`. |
| `protected static String` | `generateRequestLine(HttpConnection connection, String name, String requestPath, String query, String version)`             Generates HTTP request line according to the specified attributes. |
| `String` | `getAuthenticationRealm()`             **Deprecated.** *use #getHostAuthState()* |
| `protected  String` | `getContentCharSet(Header contentheader)`             Returns the character set from the Content-Type header. |
| `boolean` | `getDoAuthentication()`             Returns true if the HTTP method should automatically handle HTTP authentication challenges (status code 401, etc.), false otherwise |
| `HttpVersion` | `getEffectiveVersion()`             Returns the HTTP version used with this method (may be null if undefined, that is, the method has not been executed) |
| `boolean` | `getFollowRedirects()`             Returns true if the HTTP method should automatically follow HTTP redirects (status code 302, etc.), false otherwise. |
| `AuthState` | `getHostAuthState()`             Returns the target host [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth") |
| `HostConfiguration` | `getHostConfiguration()`             **Deprecated.** *no longer applicable* |
| `MethodRetryHandler` | `getMethodRetryHandler()`             **Deprecated.** *use [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| `abstract  String` | `getName()`             Obtains the name of the HTTP method as used in the HTTP request line, for example "GET" or "POST". |
| `HttpMethodParams` | `getParams()`             Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") associated with this method. |
| `String` | `getPath()`             Gets the path of this HTTP method. |
| `String` | `getProxyAuthenticationRealm()`             **Deprecated.** *use #getProxyAuthState()* |
| `AuthState` | `getProxyAuthState()`             Returns the proxy [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth") |
| `String` | `getQueryString()`             Gets the query string of this HTTP method. |
| `int` | `getRecoverableExceptionCount()`             **Deprecated.** *no longer used Returns the number of "recoverable" exceptions thrown and handled, to allow for monitoring the quality of the connection.* |
| `String` | `getRequestCharSet()`             Returns the character encoding of the request from the Content-Type header. |
| `Header` | `getRequestHeader(String headerName)`             Returns the specified request header. |
| `protected  HeaderGroup` | `getRequestHeaderGroup()`             Gets the [`header group`](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient") storing the request headers. |
| `Header[]` | `getRequestHeaders()`             Returns an array of the requests headers that the HTTP method currently has |
| `Header[]` | `getRequestHeaders(String headerName)`             Returns the request headers with the given name. |
| `byte[]` | `getResponseBody()`             Returns the response body of the HTTP method, if any, as an array of bytes. |
| `byte[]` | `getResponseBody(int maxlen)`             Returns the response body of the HTTP method, if any, as an array of bytes. |
| `InputStream` | `getResponseBodyAsStream()`             Returns the response body of the HTTP method, if any, as an [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io"). |
| `String` | `getResponseBodyAsString()`             Returns the response body of the HTTP method, if any, as a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang"). |
| `String` | `getResponseBodyAsString(int maxlen)`             Returns the response body of the HTTP method, if any, as a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang"). |
| `String` | `getResponseCharSet()`             Returns the character encoding of the response from the Content-Type header. |
| `long` | `getResponseContentLength()`             Return the length (in bytes) of the response body, as specified in a Content-Length header. |
| `Header` | `getResponseFooter(String footerName)`             Gets the response footer associated with the given name. |
| `Header[]` | `getResponseFooters()`             Returns an array of the response footers that the HTTP method currently has in the order in which they were read. |
| `Header` | `getResponseHeader(String headerName)`             Gets the response header associated with the given name. |
| `protected  HeaderGroup` | `getResponseHeaderGroup()`             Gets the [`header group`](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient") storing the response headers. |
| `Header[]` | `getResponseHeaders()`             Returns an array of the response headers that the HTTP method currently has in the order in which they were read. |
| `Header[]` | `getResponseHeaders(String headerName)`             Returns the response headers with the given name. |
| `protected  InputStream` | `getResponseStream()`             Returns a stream from which the body of the current response may be read. |
| `protected  HeaderGroup` | `getResponseTrailerHeaderGroup()`             Gets the [`header group`](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient") storing the response trailer headers as per RFC 2616 section 3.6.1. |
| `int` | `getStatusCode()`             Returns the response status code. |
| `StatusLine` | `getStatusLine()`             Provides access to the response status line. |
| `String` | `getStatusText()`             Returns the status text (or "reason phrase") associated with the latest response. |
| `URI` | `getURI()`             Returns the URI of the HTTP method |
| `boolean` | `hasBeenUsed()`             Returns true if the HTTP method has been already [`executed`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), but not [`recycled`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#recycle()). |
| `boolean` | `isAborted()`             Tests whether the execution of this method has been aborted |
| `protected  boolean` | `isConnectionCloseForced()`             Tests if the connection should be force-closed when no longer needed. |
| `boolean` | `isHttp11()`             **Deprecated.** *Use [`HttpMethodParams.getVersion()`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html#getVersion())* |
| `boolean` | `isRequestSent()`             Returns true if the HTTP has been transmitted to the target server in its entirety, false otherwise. |
| `boolean` | `isStrictMode()`             **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| `protected  void` | `processCookieHeaders(CookieSpec parser, Header[] headers, HttpState state, HttpConnection conn)`             This method processes the specified cookie headers. |
| `protected  void` | `processResponseBody(HttpState state, HttpConnection conn)`             This method is invoked immediately after [`readResponseBody(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) and can be overridden by sub-classes in order to provide custom body processing. |
| `protected  void` | `processResponseHeaders(HttpState state, HttpConnection conn)`             This method is invoked immediately after [`readResponseHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) and can be overridden by sub-classes in order to provide custom response headers processing. |
| `protected  void` | `processStatusLine(HttpState state, HttpConnection conn)`             This method is invoked immediately after [`readStatusLine(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readStatusLine(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) and can be overridden by sub-classes in order to provide custom response status line processing. |
| `protected  void` | `readResponse(HttpState state, HttpConnection conn)`             Reads the response from the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |
| `protected  void` | `readResponseBody(HttpState state, HttpConnection conn)`             Read the response body from the given [`HttpConnection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |
| `protected  void` | `readResponseHeaders(HttpState state, HttpConnection conn)`             Reads the response headers from the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |
| `protected  void` | `readStatusLine(HttpState state, HttpConnection conn)`             Read the status line from the given [`HttpConnection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"), setting my [`status code`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getStatusCode()) and [`status text`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getStatusText()). |
| `void` | `recycle()`             **Deprecated.** *no longer supported and will be removed in the future version of HttpClient* |
| `void` | `releaseConnection()`             Releases the connection being used by this HTTP method. |
| `void` | `removeRequestHeader(Header header)`             Removes the given request header. |
| `void` | `removeRequestHeader(String headerName)`             Remove the request header associated with the given name. |
| `protected  void` | `responseBodyConsumed()`             A response has been consumed. |
| `protected  void` | `setConnectionCloseForced(boolean b)`             Sets whether or not the connection should be force-closed when no longer needed. |
| `void` | `setDoAuthentication(boolean doAuthentication)`             Sets whether or not the HTTP method should automatically handle HTTP authentication challenges (status code 401, etc.) |
| `void` | `setFollowRedirects(boolean followRedirects)`             Sets whether or not the HTTP method should automatically follow HTTP redirects (status code 302, etc.) |
| `void` | `setHostConfiguration(HostConfiguration hostconfig)`             **Deprecated.** *no longer applicable* |
| `void` | `setHttp11(boolean http11)`             **Deprecated.** *Use [`HttpMethodParams.setVersion(HttpVersion)`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html#setVersion(org.apache.commons.httpclient.HttpVersion))* |
| `void` | `setMethodRetryHandler(MethodRetryHandler handler)`             **Deprecated.** *use [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")* |
| `void` | `setParams(HttpMethodParams params)`             Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") for this method. |
| `void` | `setPath(String path)`             Sets the path of the HTTP method. |
| `void` | `setQueryString(NameValuePair[] params)`             Sets the query string of this HTTP method. |
| `void` | `setQueryString(String queryString)`             Sets the query string of this HTTP method. |
| `void` | `setRequestHeader(Header header)`             Sets the specified request header, overwriting any previous value. |
| `void` | `setRequestHeader(String headerName, String headerValue)`             Set the specified request header, overwriting any previous value. |
| `protected  void` | `setResponseStream(InputStream responseStream)`             Sets the response stream. |
| `void` | `setStrictMode(boolean strictMode)`             **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object)) to exercise a more granular control over HTTP protocol strictness.* |
| `void` | `setURI(URI uri)`             Sets the URI for this method. |
| `protected  boolean` | `shouldCloseConnection(HttpConnection conn)`             Tests if the connection should be closed after the method has been executed. |
| `boolean` | `validate()`             Returns true the method is ready to execute, false otherwise. |
| `protected  void` | `writeRequest(HttpState state, HttpConnection conn)`              Sends the request via the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |
| `protected  boolean` | `writeRequestBody(HttpState state, HttpConnection conn)`             Writes the request body to the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |
| `protected  void` | `writeRequestHeaders(HttpState state, HttpConnection conn)`             Writes the request headers to the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |
| `protected  void` | `writeRequestLine(HttpState state, HttpConnection conn)`             Writes the request line to the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"). |

| **Methods inherited from class java.lang.[Object](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html "class or interface in java.lang")** |
| --- |
| `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait` |

| **Field Detail** |
| --- |

### statusLine

```
protected StatusLine statusLine
```

:   The Status-Line from the response.

---



### effectiveVersion

```
protected HttpVersion effectiveVersion
```

:   HTTP protocol version used for execution of this method.



| **Constructor Detail** |
| --- |

### HttpMethodBase

```
public HttpMethodBase()
```

:   No-arg constructor.

---



### HttpMethodBase

```
public HttpMethodBase(String uri)
               throws IllegalArgumentException,
                      IllegalStateException
```

:   Constructor specifying a URI.
    It is responsibility of the caller to ensure that URI elements
    (path & query parameters) are properly encoded (URL safe).

    **Parameters:**: `uri` - either an absolute or relative URI. The URI is expected to be URL-encoded **Throws:**: `IllegalArgumentException` - when URI is invalid: `IllegalStateException` - when protocol of the absolute URI is not recognised



| **Method Detail** |
| --- |

### getName

```
public abstract String getName()
```

:   Obtains the name of the HTTP method as used in the HTTP request line,
    for example "GET" or "POST".

    :   **Specified by:**: `getName` in interface `HttpMethod`
    :   **Returns:**: the name of this method

---



### getURI

```
public URI getURI()
           throws URIException
```

:   Returns the URI of the HTTP method

    :   **Specified by:**: `getURI` in interface `HttpMethod`
    :   **Returns:**: The URI **Throws:**: `URIException` - If the URI cannot be created. **See Also:**: [`HttpMethod.getURI()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getURI())

---



### setURI

```
public void setURI(URI uri)
            throws URIException
```

:   Sets the URI for this method.

    :   **Specified by:**: `setURI` in interface `HttpMethod`
    :   **Parameters:**: `uri` - URI to be set **Throws:**: `URIException` - if a URI cannot be set **Since:** : 3.0

---



### setFollowRedirects

```
public void setFollowRedirects(boolean followRedirects)
```

:   Sets whether or not the HTTP method should automatically follow HTTP redirects
    (status code 302, etc.)

    :   **Specified by:**: `setFollowRedirects` in interface `HttpMethod`
    :   **Parameters:**: `followRedirects` - true if the method will automatically follow redirects, false otherwise.

---



### getFollowRedirects

```
public boolean getFollowRedirects()
```

:   Returns true if the HTTP method should automatically follow HTTP redirects
    (status code 302, etc.), false otherwise.

    :   **Specified by:**: `getFollowRedirects` in interface `HttpMethod`
    :   **Returns:**: true if the method will automatically follow HTTP redirects, false otherwise.

---



### setHttp11

```
public void setHttp11(boolean http11)
```

:   **Deprecated.** *Use [`HttpMethodParams.setVersion(HttpVersion)`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html#setVersion(org.apache.commons.httpclient.HttpVersion))*

    :   Sets whether version 1.1 of the HTTP protocol should be used per default.

        :   **Parameters:**: `http11` - true to use HTTP/1.1, false to use 1.0

---



### getDoAuthentication

```
public boolean getDoAuthentication()
```

:   Returns true if the HTTP method should automatically handle HTTP
    authentication challenges (status code 401, etc.), false otherwise

    :   **Specified by:**: `getDoAuthentication` in interface `HttpMethod`
    :   **Returns:**: true if authentication challenges will be processed automatically, false otherwise. **Since:** : 2.0 **See Also:**: [`HttpMethod.setDoAuthentication(boolean)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setDoAuthentication(boolean))

---



### setDoAuthentication

```
public void setDoAuthentication(boolean doAuthentication)
```

:   Sets whether or not the HTTP method should automatically handle HTTP
    authentication challenges (status code 401, etc.)

    :   **Specified by:**: `setDoAuthentication` in interface `HttpMethod`
    :   **Parameters:**: `doAuthentication` - true to process authentication challenges authomatically, false otherwise. **Since:** : 2.0 **See Also:**: [`HttpMethod.getDoAuthentication()`](../../../../org/apache/commons/httpclient/HttpMethod.html#getDoAuthentication())

---



### isHttp11

```
public boolean isHttp11()
```

:   **Deprecated.** *Use [`HttpMethodParams.getVersion()`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html#getVersion())*

    :   Returns true if version 1.1 of the HTTP protocol should be
        used per default, false if version 1.0 should be used.

        :   **Returns:**: true to use HTTP/1.1, false to use 1.0

---



### setPath

```
public void setPath(String path)
```

:   Sets the path of the HTTP method.
    It is responsibility of the caller to ensure that the path is
    properly encoded (URL safe).

    :   **Specified by:**: `setPath` in interface `HttpMethod`
    :   **Parameters:**: `path` - the path of the HTTP method. The path is expected to be URL-encoded

---



### addRequestHeader

```
public void addRequestHeader(Header header)
```

:   Adds the specified request header, NOT overwriting any previous value.
    Note that header-name matching is case insensitive.

    :   **Specified by:**: `addRequestHeader` in interface `HttpMethod`
    :   **Parameters:**: `header` - the header to add to the request **See Also:**: [`HttpMethod.addRequestHeader(String,String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(java.lang.String, java.lang.String)), [`HttpMethod.getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`HttpMethod.removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### addResponseFooter

```
public void addResponseFooter(Header footer)
```

:   Use this method internally to add footers.

    :   **Specified by:**: `addResponseFooter` in interface `HttpMethod`
    :   **Parameters:**: `footer` - The footer to add.

---



### getPath

```
public String getPath()
```

:   Gets the path of this HTTP method.
    Calling this method *after* the request has been executed will
    return the *actual* path, following any redirects automatically
    handled by this HTTP method.

    :   **Specified by:**: `getPath` in interface `HttpMethod`
    :   **Returns:**: the path to request or "/" if the path is blank.

---



### setQueryString

```
public void setQueryString(String queryString)
```

:   Sets the query string of this HTTP method. The caller must ensure that the string
    is properly URL encoded. The query string should not start with the question
    mark character.

    :   **Specified by:**: `setQueryString` in interface `HttpMethod`
    :   **Parameters:**: `queryString` - the query string **See Also:**: [`EncodingUtil.formUrlEncode(NameValuePair[], String)`](../../../../org/apache/commons/httpclient/util/EncodingUtil.html#formUrlEncode(org.apache.commons.httpclient.NameValuePair[], java.lang.String))

---



### setQueryString

```
public void setQueryString(NameValuePair[] params)
```

:   Sets the query string of this HTTP method. The pairs are encoded as UTF-8 characters.
    To use a different charset the parameters can be encoded manually using EncodingUtil
    and set as a single String.

    :   **Specified by:**: `setQueryString` in interface `HttpMethod`
    :   **Parameters:**: `params` - an array of [`NameValuePair`](../../../../org/apache/commons/httpclient/NameValuePair.html "class in org.apache.commons.httpclient")s to add as query string parameters. The name/value pairs will be automcatically URL encoded **See Also:**: [`EncodingUtil.formUrlEncode(NameValuePair[], String)`](../../../../org/apache/commons/httpclient/util/EncodingUtil.html#formUrlEncode(org.apache.commons.httpclient.NameValuePair[], java.lang.String)), [`setQueryString(String)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#setQueryString(java.lang.String))

---



### getQueryString

```
public String getQueryString()
```

:   Gets the query string of this HTTP method.

    :   **Specified by:**: `getQueryString` in interface `HttpMethod`
    :   **Returns:**: The query string **See Also:**: [`HttpMethod.setQueryString(NameValuePair[])`](../../../../org/apache/commons/httpclient/HttpMethod.html#setQueryString(org.apache.commons.httpclient.NameValuePair[])), [`HttpMethod.setQueryString(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setQueryString(java.lang.String))

---



### setRequestHeader

```
public void setRequestHeader(String headerName,
                             String headerValue)
```

:   Set the specified request header, overwriting any previous value. Note
    that header-name matching is case-insensitive.

    :   **Specified by:**: `setRequestHeader` in interface `HttpMethod`
    :   **Parameters:**: `headerName` - the header's name: `headerValue` - the header's value **See Also:**: [`HttpMethod.setRequestHeader(Header)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setRequestHeader(org.apache.commons.httpclient.Header)), [`HttpMethod.getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`HttpMethod.removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### setRequestHeader

```
public void setRequestHeader(Header header)
```

:   Sets the specified request header, overwriting any previous value.
    Note that header-name matching is case insensitive.

    :   **Specified by:**: `setRequestHeader` in interface `HttpMethod`
    :   **Parameters:**: `header` - the header **See Also:**: [`HttpMethod.setRequestHeader(String,String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setRequestHeader(java.lang.String, java.lang.String)), [`HttpMethod.getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`HttpMethod.removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### getRequestHeader

```
public Header getRequestHeader(String headerName)
```

:   Returns the specified request header. Note that header-name matching is
    case insensitive. null will be returned if either
    *headerName* is null or there is no matching header for
    *headerName*.

    :   **Specified by:**: `getRequestHeader` in interface `HttpMethod`
    :   **Parameters:**: `headerName` - The name of the header to be returned. **Returns:**: The specified request header. **Since:** : 3.0

---



### getRequestHeaders

```
public Header[] getRequestHeaders()
```

:   Returns an array of the requests headers that the HTTP method currently has

    :   **Specified by:**: `getRequestHeaders` in interface `HttpMethod`
    :   **Returns:**: an array of my request headers. **See Also:**: [`HttpMethod.addRequestHeader(Header)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(org.apache.commons.httpclient.Header)), [`HttpMethod.addRequestHeader(String,String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(java.lang.String, java.lang.String))

---



### getRequestHeaders

```
public Header[] getRequestHeaders(String headerName)
```

:   **Description copied from interface: `HttpMethod`**
:   Returns the request headers with the given name. Note that header-name matching is
    case insensitive.

    :   **Specified by:**: `getRequestHeaders` in interface `HttpMethod`
    :   **Parameters:**: `headerName` - the name of the headers to be returned. **Returns:**: an array of zero or more headers **See Also:**: [`HttpMethod.getRequestHeaders(java.lang.String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeaders(java.lang.String))

---



### getRequestHeaderGroup

```
protected HeaderGroup getRequestHeaderGroup()
```

:   Gets the [`header group`](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient") storing the request headers.

    :   **Returns:**: a HeaderGroup **Since:** : 2.0beta1

---



### getResponseTrailerHeaderGroup

```
protected HeaderGroup getResponseTrailerHeaderGroup()
```

:   Gets the [`header group`](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient") storing the response trailer headers
    as per RFC 2616 section 3.6.1.

    :   **Returns:**: a HeaderGroup **Since:** : 2.0beta1

---



### getResponseHeaderGroup

```
protected HeaderGroup getResponseHeaderGroup()
```

:   Gets the [`header group`](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient") storing the response headers.

    :   **Returns:**: a HeaderGroup **Since:** : 2.0beta1

---



### getResponseHeaders

```
public Header[] getResponseHeaders(String headerName)
```

:   **Description copied from interface: `HttpMethod`**
:   Returns the response headers with the given name. Note that header-name matching is
    case insensitive.

    :   **Specified by:**: `getResponseHeaders` in interface `HttpMethod`
    :   **Parameters:**: `headerName` - the name of the headers to be returned. **Returns:**: an array of zero or more headers **Since:** : 3.0 **See Also:**: [`HttpMethod.getResponseHeaders(java.lang.String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getResponseHeaders(java.lang.String))

---



### getStatusCode

```
public int getStatusCode()
```

:   Returns the response status code.

    :   **Specified by:**: `getStatusCode` in interface `HttpMethod`
    :   **Returns:**: the status code associated with the latest response.

---



### getStatusLine

```
public StatusLine getStatusLine()
```

:   Provides access to the response status line.

    :   **Specified by:**: `getStatusLine` in interface `HttpMethod`
    :   **Returns:**: the status line object from the latest response. **Since:** : 2.0

---



### getResponseHeaders

```
public Header[] getResponseHeaders()
```

:   Returns an array of the response headers that the HTTP method currently has
    in the order in which they were read.

    :   **Specified by:**: `getResponseHeaders` in interface `HttpMethod`
    :   **Returns:**: an array of response headers.

---



### getResponseHeader

```
public Header getResponseHeader(String headerName)
```

:   Gets the response header associated with the given name. Header name
    matching is case insensitive. null will be returned if either
    *headerName* is null or there is no matching header for
    *headerName*.

    :   **Specified by:**: `getResponseHeader` in interface `HttpMethod`
    :   **Parameters:**: `headerName` - the header name to match **Returns:**: the matching header

---



### getResponseContentLength

```
public long getResponseContentLength()
```

:   Return the length (in bytes) of the response body, as specified in a
    Content-Length header.

    Return -1 when the content-length is unknown.

    :   **Returns:**: content length, if Content-Length header is available. 0 indicates that the request has no body. If Content-Length header is not present, the method returns -1.

---



### getResponseBody

```
public byte[] getResponseBody()
                       throws IOException
```

:   Returns the response body of the HTTP method, if any, as an array of bytes.
    If response body is not available or cannot be read, returns null.
    Buffers the response and this method can be called several times yielding
    the same result each time.
    Note: This will cause the entire response body to be buffered in memory. A
    malicious server may easily exhaust all the VM memory. It is strongly
    recommended, to use getResponseAsStream if the content length of the response
    is unknown or resonably large.

    :   **Specified by:**: `getResponseBody` in interface `HttpMethod`
    :   **Returns:**: The response body. **Throws:**: `IOException` - If an I/O (transport) problem occurs while obtaining the response body.

---



### getResponseBody

```
public byte[] getResponseBody(int maxlen)
                       throws IOException
```

:   Returns the response body of the HTTP method, if any, as an array of bytes.
    If response body is not available or cannot be read, returns null.
    Buffers the response and this method can be called several times yielding
    the same result each time.
    Note: This will cause the entire response body to be buffered in memory. This method is
    safe if the content length of the response is unknown, because the amount of memory used
    is limited.

    If the response is large this method involves lots of array copying and many object
    allocations, which makes it unsuitable for high-performance / low-footprint applications.
    Those applications should use [`getResponseBodyAsStream()`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getResponseBodyAsStream()).

    :   **Parameters:**: `maxlen` - the maximum content length to accept (number of bytes). **Returns:**: The response body. **Throws:**: `IOException` - If an I/O (transport) problem occurs while obtaining the response body.

---



### getResponseBodyAsStream

```
public InputStream getResponseBodyAsStream()
                                    throws IOException
```

:   Returns the response body of the HTTP method, if any, as an [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io").
    If response body is not available, returns null. If the response has been
    buffered this method returns a new stream object on every call. If the response
    has not been buffered the returned stream can only be read once.

    :   **Specified by:**: `getResponseBodyAsStream` in interface `HttpMethod`
    :   **Returns:**: The response body or `null`. **Throws:**: `IOException` - If an I/O (transport) problem occurs while obtaining the response body.

---



### getResponseBodyAsString

```
public String getResponseBodyAsString()
                               throws IOException
```

:   Returns the response body of the HTTP method, if any, as a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang").
    If response body is not available or cannot be read, returns null
    The string conversion on the data is done using the character encoding specified
    in Content-Type header. Buffers the response and this method can be
    called several times yielding the same result each time.
    Note: This will cause the entire response body to be buffered in memory. A
    malicious server may easily exhaust all the VM memory. It is strongly
    recommended, to use getResponseAsStream if the content length of the response
    is unknown or resonably large.

    :   **Specified by:**: `getResponseBodyAsString` in interface `HttpMethod`
    :   **Returns:**: The response body or `null`. **Throws:**: `IOException` - If an I/O (transport) problem occurs while obtaining the response body.

---



### getResponseBodyAsString

```
public String getResponseBodyAsString(int maxlen)
                               throws IOException
```

:   Returns the response body of the HTTP method, if any, as a [`String`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html "class or interface in java.lang").
    If response body is not available or cannot be read, returns null
    The string conversion on the data is done using the character encoding specified
    in Content-Type header. Buffers the response and this method can be
    called several times yielding the same result each time.

Note: This will cause the entire response body to be buffered in memory. This method is
safe if the content length of the response is unknown, because the amount of memory used
is limited.

If the response is large this method involves lots of array copying and many object
allocations, which makes it unsuitable for high-performance / low-footprint applications.
Those applications should use [`getResponseBodyAsStream()`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getResponseBodyAsStream()).

:   **Parameters:**: `maxlen` - the maximum content length to accept (number of bytes). Note that, depending on the encoding, this is not equal to the number of characters. **Returns:**: The response body or `null`. **Throws:**: `IOException` - If an I/O (transport) problem occurs while obtaining the response body.

---



### getResponseFooters

```
public Header[] getResponseFooters()
```

:   Returns an array of the response footers that the HTTP method currently has
    in the order in which they were read.

    :   **Specified by:**: `getResponseFooters` in interface `HttpMethod`
    :   **Returns:**: an array of footers

---



### getResponseFooter

```
public Header getResponseFooter(String footerName)
```

:   Gets the response footer associated with the given name.
    Footer name matching is case insensitive.
    null will be returned if either *footerName* is
    null or there is no matching footer for *footerName*
    or there are no footers available. If there are multiple footers
    with the same name, there values will be combined with the ',' separator
    as specified by RFC2616.

    :   **Specified by:**: `getResponseFooter` in interface `HttpMethod`
    :   **Parameters:**: `footerName` - the footer name to match **Returns:**: the matching footer

---



### setResponseStream

```
protected void setResponseStream(InputStream responseStream)
```

:   Sets the response stream.

    :   **Parameters:**: `responseStream` - The new response stream.

---



### getResponseStream

```
protected InputStream getResponseStream()
```

:   Returns a stream from which the body of the current response may be read.
    If the method has not yet been executed, if `responseBodyConsumed`
    has been called, or if the stream returned by a previous call has been closed,
    `null` will be returned.

    :   **Returns:**: the current response stream

---



### getStatusText

```
public String getStatusText()
```

:   Returns the status text (or "reason phrase") associated with the latest
    response.

    :   **Specified by:**: `getStatusText` in interface `HttpMethod`
    :   **Returns:**: The status text.

---



### setStrictMode

```
public void setStrictMode(boolean strictMode)
```

:   **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object))
    to exercise a more granular control over HTTP protocol strictness.*

    :   Defines how strictly HttpClient follows the HTTP protocol specification
        (RFC 2616 and other relevant RFCs). In the strict mode HttpClient precisely
        implements the requirements of the specification, whereas in non-strict mode
        it attempts to mimic the exact behaviour of commonly used HTTP agents,
        which many HTTP servers expect.

        :   **Specified by:**: `setStrictMode` in interface `HttpMethod`
        :   **Parameters:**: `strictMode` - true for strict mode, false otherwise **See Also:**: [`HttpMethod.isStrictMode()`](../../../../org/apache/commons/httpclient/HttpMethod.html#isStrictMode())

---



### isStrictMode

```
public boolean isStrictMode()
```

:   **Deprecated.** *Use [`HttpParams.setParameter(String, Object)`](../../../../org/apache/commons/httpclient/params/HttpParams.html#setParameter(java.lang.String, java.lang.Object))
    to exercise a more granular control over HTTP protocol strictness.*

    :   **Description copied from interface: `HttpMethod`**
    :   Returns the value of the strict mode flag.

        :   **Specified by:**: `isStrictMode` in interface `HttpMethod`
        :   **Returns:**: false **See Also:**: [`HttpMethod.setStrictMode(boolean)`](../../../../org/apache/commons/httpclient/HttpMethod.html#setStrictMode(boolean))

---



### addRequestHeader

```
public void addRequestHeader(String headerName,
                             String headerValue)
```

:   Adds the specified request header, NOT overwriting any previous value.
    Note that header-name matching is case insensitive.

    :   **Specified by:**: `addRequestHeader` in interface `HttpMethod`
    :   **Parameters:**: `headerName` - the header's name: `headerValue` - the header's value **See Also:**: [`HttpMethod.addRequestHeader(Header)`](../../../../org/apache/commons/httpclient/HttpMethod.html#addRequestHeader(org.apache.commons.httpclient.Header)), [`HttpMethod.getRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#getRequestHeader(java.lang.String)), [`HttpMethod.removeRequestHeader(String)`](../../../../org/apache/commons/httpclient/HttpMethod.html#removeRequestHeader(java.lang.String))

---



### isConnectionCloseForced

```
protected boolean isConnectionCloseForced()
```

:   Tests if the connection should be force-closed when no longer needed.

    :   **Returns:**: `true` if the connection must be closed

---



### setConnectionCloseForced

```
protected void setConnectionCloseForced(boolean b)
```

:   Sets whether or not the connection should be force-closed when no longer
    needed. This value should only be set to `true` in abnormal
    circumstances, such as HTTP protocol violations.

    :   **Parameters:**: `b` - `true` if the connection must be closed, `false` otherwise.

---



### shouldCloseConnection

```
protected boolean shouldCloseConnection(HttpConnection conn)
```

:   Tests if the connection should be closed after the method has been executed.
    The connection will be left open when using HTTP/1.1 or if Connection:
    keep-alive header was sent.

    :   **Parameters:**: `conn` - the connection in question **Returns:**: boolean true if we should close the connection.

---



### execute

```
public int execute(HttpState state,
                   HttpConnection conn)
            throws HttpException,
                   IOException
```

:   Executes this method using the specified `HttpConnection` and
    `HttpState`.

    :   **Specified by:**: `execute` in interface `HttpMethod`
    :   **Parameters:**: `state` - [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information to associate with this request. Must be non-null.: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") to used to execute this HTTP method. Must be non-null. **Returns:**: the integer status code if one was obtained, or -1 **Throws:**: `IOException` - if an I/O (transport) error occurs: `HttpException` - if a protocol exception occurs.

---



### abort

```
public void abort()
```

:   Aborts the execution of this method.

    :   **Specified by:**: `abort` in interface `HttpMethod`
    :   **Since:**
        :   3.0

        **See Also:**: [`HttpMethod.execute(HttpState, HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethod.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### hasBeenUsed

```
public boolean hasBeenUsed()
```

:   Returns true if the HTTP method has been already [`executed`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)),
    but not [`recycled`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#recycle()).

    :   **Specified by:**: `hasBeenUsed` in interface `HttpMethod`
    :   **Returns:**: true if the method has been executed, false otherwise

---



### recycle

```
public void recycle()
```

:   **Deprecated.** *no longer supported and will be removed in the future
    version of HttpClient*

    :   Recycles the HTTP method so that it can be used again.
        Note that all of the instance variables will be reset
        once this method has been called. This method will also
        release the connection being used by this HTTP method.

        :   **Specified by:**: `recycle` in interface `HttpMethod`
        :   **See Also:**: [`releaseConnection()`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#releaseConnection())

---



### releaseConnection

```
public void releaseConnection()
```

:   Releases the connection being used by this HTTP method. In particular the
    connection is used to read the response(if there is one) and will be held
    until the response has been read. If the connection can be reused by other
    HTTP methods it is NOT closed at this point.

    :   **Specified by:**: `releaseConnection` in interface `HttpMethod`
    :   **Since:**
        :   2.0

---



### removeRequestHeader

```
public void removeRequestHeader(String headerName)
```

:   Remove the request header associated with the given name. Note that
    header-name matching is case insensitive.

    :   **Specified by:**: `removeRequestHeader` in interface `HttpMethod`
    :   **Parameters:**: `headerName` - the header name

---



### removeRequestHeader

```
public void removeRequestHeader(Header header)
```

:   Removes the given request header.

    :   **Specified by:**: `removeRequestHeader` in interface `HttpMethod`
    :   **Parameters:**: `header` - the header

---



### validate

```
public boolean validate()
```

:   Returns true the method is ready to execute, false otherwise.

    :   **Specified by:**: `validate` in interface `HttpMethod`
    :   **Returns:**: This implementation always returns true.

---



### addCookieRequestHeader

```
protected void addCookieRequestHeader(HttpState state,
                                      HttpConnection conn)
                               throws IOException,
                                      HttpException
```

:   Generates Cookie request headers for those [`cookie`](../../../../org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient")s
    that match the given host, port and path.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### addHostRequestHeader

```
protected void addHostRequestHeader(HttpState state,
                                    HttpConnection conn)
                             throws IOException,
                                    HttpException
```

:   Generates Host request header, as long as no Host request
    header already exists.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### addProxyConnectionHeader

```
protected void addProxyConnectionHeader(HttpState state,
                                        HttpConnection conn)
                                 throws IOException,
                                        HttpException
```

:   Generates Proxy-Connection: Keep-Alive request header when
    communicating via a proxy server.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### addRequestHeaders

```
protected void addRequestHeaders(HttpState state,
                                 HttpConnection conn)
                          throws IOException,
                                 HttpException
```

:   Generates all the required request [`header`](../../../../org/apache/commons/httpclient/Header.html "class in org.apache.commons.httpclient")s
    to be submitted via the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    This implementation adds User-Agent, Host,
    Cookie, Authorization, Proxy-Authorization
    and Proxy-Connection headers, when appropriate.

    Subclasses may want to override this method to to add additional
    headers, and may choose to invoke this implementation (via
    super) to add the "standard" headers.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from. **See Also:**: [`writeRequestHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#writeRequestHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### addUserAgentRequestHeader

```
protected void addUserAgentRequestHeader(HttpState state,
                                         HttpConnection conn)
                                  throws IOException,
                                         HttpException
```

:   Generates default User-Agent request header, as long as no
    User-Agent request header already exists.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### checkNotUsed

```
protected void checkNotUsed()
                     throws IllegalStateException
```

:   Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the HTTP method has been already
    [`executed`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), but not [`recycled`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#recycle()).

    :   **Throws:**: `IllegalStateException` - if the method has been used and not recycled

---



### checkUsed

```
protected void checkUsed()
                  throws IllegalStateException
```

:   Throws an [`IllegalStateException`](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/IllegalStateException.html "class or interface in java.lang") if the HTTP method has not been
    [`executed`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#execute(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) since last [`recycle`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#recycle()).

    :   **Throws:**: `IllegalStateException` - if not used

---



### generateRequestLine

```
protected static String generateRequestLine(HttpConnection connection,
                                            String name,
                                            String requestPath,
                                            String query,
                                            String version)
```

:   Generates HTTP request line according to the specified attributes.

    :   **Parameters:**: `connection` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method: `name` - the method name generate a request for: `requestPath` - the path string for the request: `query` - the query string for the request: `version` - the protocol version to use (e.g. HTTP/1.0) **Returns:**: HTTP request line

---



### processResponseBody

```
protected void processResponseBody(HttpState state,
                                   HttpConnection conn)
```

:   This method is invoked immediately after
    [`readResponseBody(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) and can be overridden by
    sub-classes in order to provide custom body processing.

    This implementation does nothing.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **See Also:**: [`readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), [`readResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### processResponseHeaders

```
protected void processResponseHeaders(HttpState state,
                                      HttpConnection conn)
```

:   This method is invoked immediately after
    [`readResponseHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) and can be overridden by
    sub-classes in order to provide custom response headers processing.

    This implementation will handle the Set-Cookie and
    Set-Cookie2 headers, if any, adding the relevant cookies to
    the given [`HttpState`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient").

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **See Also:**: [`readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), [`readResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### processCookieHeaders

```
protected void processCookieHeaders(CookieSpec parser,
                                    Header[] headers,
                                    HttpState state,
                                    HttpConnection conn)
```

:   This method processes the specified cookie headers. It is invoked from
    within [`processResponseHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#processResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

    :   **Parameters:**: `headers` - cookie [`Header`](../../../../org/apache/commons/httpclient/Header.html "class in org.apache.commons.httpclient")s to be processed: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this HTTP method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method

---



### processStatusLine

```
protected void processStatusLine(HttpState state,
                                 HttpConnection conn)
```

:   This method is invoked immediately after
    [`readStatusLine(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readStatusLine(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) and can be overridden by
    sub-classes in order to provide custom response status line processing.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **See Also:**: [`readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), [`readStatusLine(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readStatusLine(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### readResponse

```
protected void readResponse(HttpState state,
                            HttpConnection conn)
                     throws IOException,
                            HttpException
```

:   Reads the response from the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    The response is processed as the following sequence of actions:

    1. [`readStatusLine(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readStatusLine(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is
       invoked to read the request line.
    2. [`processStatusLine(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#processStatusLine(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))
       is invoked, allowing the method to process the status line if
       desired.
    3. [`readResponseHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is invoked to read
       the associated headers.
    4. [`processResponseHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#processResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is invoked, allowing
       the method to process the headers if desired.
    5. [`readResponseBody(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is
       invoked to read the associated body (if any).
    6. [`processResponseBody(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#processResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is invoked, allowing the
       method to process the response body if desired.

    Subclasses may want to override one or more of the above methods to to
    customize the processing. (Or they may choose to override this method
    if dramatically different processing is required.)

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### readResponseBody

```
protected void readResponseBody(HttpState state,
                                HttpConnection conn)
                         throws IOException,
                                HttpException
```

:   Read the response body from the given [`HttpConnection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    The current implementation wraps the socket level stream with
    an appropriate stream for the type of response (chunked, content-length,
    or auto-close). If there is no response body, the connection associated
    with the request will be returned to the connection manager.

    Subclasses may want to override this method to to customize the
    processing.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from. **See Also:**: [`readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), [`processResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#processResponseBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### readResponseHeaders

```
protected void readResponseHeaders(HttpState state,
                                   HttpConnection conn)
                            throws IOException,
                                   HttpException
```

:   Reads the response headers from the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    Subclasses may want to override this method to to customize the
    processing.

    "It must be possible to combine the multiple header fields into one
    "field-name: field-value" pair, without changing the semantics of the
    message, by appending each subsequent field-value to the first, each
    separated by a comma." - HTTP/1.0 (4.3)

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from. **See Also:**: [`readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#readResponse(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), [`processResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#processResponseHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection))

---



### readStatusLine

```
protected void readStatusLine(HttpState state,
                              HttpConnection conn)
                       throws IOException,
                              HttpException
```

:   Read the status line from the given [`HttpConnection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"), setting my
    [`status code`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getStatusCode()) and [`status
    text`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getStatusText()).

    Subclasses may want to override this method to to customize the
    processing.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from. **See Also:**: [`StatusLine`](../../../../org/apache/commons/httpclient/StatusLine.html "class in org.apache.commons.httpclient")

---



### writeRequest

```
protected void writeRequest(HttpState state,
                            HttpConnection conn)
                     throws IOException,
                            HttpException
```

:   Sends the request via the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    The request is written as the following sequence of actions:

    1. [`writeRequestLine(HttpState, HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#writeRequestLine(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is invoked to
       write the request line.
    2. [`writeRequestHeaders(HttpState, HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#writeRequestHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is invoked
       to write the associated headers.
    3. \r\n is sent to close the head part of the request.
    4. [`writeRequestBody(HttpState, HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#writeRequestBody(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)) is invoked to
       write the body part of the request.

    Subclasses may want to override one or more of the above methods to to
    customize the processing. (Or they may choose to override this method
    if dramatically different processing is required.)

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### writeRequestBody

```
protected boolean writeRequestBody(HttpState state,
                                   HttpConnection conn)
                            throws IOException,
                                   HttpException
```

:   Writes the request body to the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    This method should return true if the request body was actually
    sent (or is empty), or false if it could not be sent for some
    reason.

    This implementation writes nothing and returns true.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Returns:**: true **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from.

---



### writeRequestHeaders

```
protected void writeRequestHeaders(HttpState state,
                                   HttpConnection conn)
                            throws IOException,
                                   HttpException
```

:   Writes the request headers to the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    This implementation invokes [`addRequestHeaders(HttpState,HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#addRequestHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)),
    and then writes each header to the request stream.

    Subclasses may want to override this method to to customize the
    processing.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from. **See Also:**: [`addRequestHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#addRequestHeaders(org.apache.commons.httpclient.HttpState, org.apache.commons.httpclient.HttpConnection)), [`getRequestHeaders()`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#getRequestHeaders())

---



### writeRequestLine

```
protected void writeRequestLine(HttpState state,
                                HttpConnection conn)
                         throws IOException,
                                HttpException
```

:   Writes the request line to the given [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient").

    Subclasses may want to override this method to to customize the
    processing.

    :   **Parameters:**: `state` - the [`state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") information associated with this method: `conn` - the [`connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") used to execute this HTTP method **Throws:**: `IOException` - if an I/O (transport) error occurs. Some transport exceptions can be recovered from.: `HttpException` - if a protocol exception occurs. Usually protocol exceptions cannot be recovered from. **See Also:**: [`generateRequestLine(org.apache.commons.httpclient.HttpConnection, java.lang.String, java.lang.String, java.lang.String, java.lang.String)`](../../../../org/apache/commons/httpclient/HttpMethodBase.html#generateRequestLine(org.apache.commons.httpclient.HttpConnection, java.lang.String, java.lang.String, java.lang.String, java.lang.String))

---



### getParams

```
public HttpMethodParams getParams()
```

:   Returns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") associated with this method.

    :   **Specified by:**: `getParams` in interface `HttpMethod`
    :   **Returns:**: HTTP parameters. **Since:** : 3.0 **See Also:**: [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")

---



### setParams

```
public void setParams(HttpMethodParams params)
```

:   Assigns [`HTTP protocol parameters`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params") for this method.

    :   **Specified by:**: `setParams` in interface `HttpMethod`
    :   **Since:**
        :   3.0

        **See Also:**: [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")

---



### getEffectiveVersion

```
public HttpVersion getEffectiveVersion()
```

:   Returns the HTTP version used with this method (may be null
    if undefined, that is, the method has not been executed)

    :   **Returns:**: HTTP version. **Since:** : 3.0

---



### getProxyAuthenticationRealm

```
public String getProxyAuthenticationRealm()
```

:   **Deprecated.** *use #getProxyAuthState()*

    :   Returns proxy authentication realm, if it has been used during authentication process.
        Otherwise returns null.

        :   **Returns:**: proxy authentication realm

---



### getAuthenticationRealm

```
public String getAuthenticationRealm()
```

:   **Deprecated.** *use #getHostAuthState()*

    :   Returns authentication realm, if it has been used during authentication process.
        Otherwise returns null.

        :   **Returns:**: authentication realm

---



### getContentCharSet

```
protected String getContentCharSet(Header contentheader)
```

:   Returns the character set from the Content-Type header.

    :   **Parameters:**: `contentheader` - The content header. **Returns:**: String The character set.

---



### getRequestCharSet

```
public String getRequestCharSet()
```

:   Returns the character encoding of the request from the Content-Type header.

    :   **Returns:**: String The character set.

---



### getResponseCharSet

```
public String getResponseCharSet()
```

:   Returns the character encoding of the response from the Content-Type header.

    :   **Returns:**: String The character set.

---



### getRecoverableExceptionCount

```
public int getRecoverableExceptionCount()
```

:   **Deprecated.** *no longer used
    Returns the number of "recoverable" exceptions thrown and handled, to
    allow for monitoring the quality of the connection.*

    :   **Returns:**: The number of recoverable exceptions handled by the method.

---



### responseBodyConsumed

```
protected void responseBodyConsumed()
```

:   A response has been consumed.

    The default behavior for this class is to check to see if the connection
    should be closed, and close if need be, and to ensure that the connection
    is returned to the connection manager - if and only if we are not still
    inside the execute call.

---



### getHostConfiguration

```
public HostConfiguration getHostConfiguration()
```

:   **Deprecated.** *no longer applicable*

    :   Returns the [`host configuration`](../../../../org/apache/commons/httpclient/HostConfiguration.html "class in org.apache.commons.httpclient").

        :   **Specified by:**: `getHostConfiguration` in interface `HttpMethod`
        :   **Returns:**: the host configuration

---



### setHostConfiguration

```
public void setHostConfiguration(HostConfiguration hostconfig)
```

:   **Deprecated.** *no longer applicable*

    :   Sets the [`host configuration`](../../../../org/apache/commons/httpclient/HostConfiguration.html "class in org.apache.commons.httpclient").

        :   **Parameters:**: `hostconfig` - The hostConfiguration to set

---



### getMethodRetryHandler

```
public MethodRetryHandler getMethodRetryHandler()
```

:   **Deprecated.** *use [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")*

    :   Returns the [`retry handler`](../../../../org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient") for this HTTP method

        :   **Returns:**: the methodRetryHandler

---



### setMethodRetryHandler

```
public void setMethodRetryHandler(MethodRetryHandler handler)
```

:   **Deprecated.** *use [`HttpMethodParams`](../../../../org/apache/commons/httpclient/params/HttpMethodParams.html "class in org.apache.commons.httpclient.params")*

    :   Sets the [`retry handler`](../../../../org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient") for this HTTP method

        :   **Parameters:**: `handler` - the methodRetryHandler to use when this method executed

---



### getHostAuthState

```
public AuthState getHostAuthState()
```

:   Returns the target host [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth")

    :   **Specified by:**: `getHostAuthState` in interface `HttpMethod`
    :   **Returns:**: host authentication state **Since:** : 3.0

---



### getProxyAuthState

```
public AuthState getProxyAuthState()
```

:   Returns the proxy [`authentication state`](../../../../org/apache/commons/httpclient/auth/AuthState.html "class in org.apache.commons.httpclient.auth")

    :   **Specified by:**: `getProxyAuthState` in interface `HttpMethod`
    :   **Returns:**: host authentication state **Since:** : 3.0

---



### isAborted

```
public boolean isAborted()
```

:   Tests whether the execution of this method has been aborted

    :   **Returns:**: true if the execution of this method has been aborted, false otherwise **Since:** : 3.0

---



### isRequestSent

```
public boolean isRequestSent()
```

:   Returns true if the HTTP has been transmitted to the target
    server in its entirety, false otherwise. This flag can be useful
    for recovery logic. If the request has not been transmitted in its entirety,
    it is safe to retry the failed method.

    :   **Specified by:**: `isRequestSent` in interface `HttpMethod`
    :   **Returns:**: true if the request has been sent, false otherwise



---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | [**Package**](package-summary.html) | **Class** | [**Use**](class-use/HttpMethodBase.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| [**PREV CLASS**](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")   [**NEXT CLASS**](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/HttpMethodBase.html)    [**NO FRAMES**](HttpMethodBase.html) |
| SUMMARY: NESTED | [FIELD](#field_summary) | [CONSTR](#constructor_summary) | [METHOD](#method_summary) | DETAIL: [FIELD](#field_detail) | [CONSTR](#constructor_detail) | [METHOD](#method_detail) |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.

---
|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [**Overview**](../../../../overview-summary.html) | **Package** | Class | [**Use**](package-use.html) | [**Tree**](package-tree.html) | [**Deprecated**](../../../../deprecated-list.html) | [**Index**](../../../../index-all.html) | [**Help**](../../../../help-doc.html) | | |  |
| PREV PACKAGE   [**NEXT PACKAGE**](../../../../org/apache/commons/httpclient/auth/package-summary.html) | [**FRAMES**](../../../../index.html?org/apache/commons/httpclient/package-summary.html)    [**NO FRAMES**](package-summary.html) |




---

## Package org.apache.commons.httpclient

Classes and interfaces supporting the client side of the HTTP protocol.

**See:**
  
          [**Description**](#package_description)

| **Interface Summary** | |
| --- | --- |
| **[Credentials](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient")** | Authentication credentials. |
| **[HttpConnectionManager](../../../../org/apache/commons/httpclient/HttpConnectionManager.html "interface in org.apache.commons.httpclient")** | An interface for classes that manage HttpConnections. |
| **[HttpMethod](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")** | HttpMethod interface represents a request to be sent via a [`HTTP connection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient") and a corresponding response. |
| **[HttpMethodRetryHandler](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")** | A handler for determining if an HttpMethod should be retried after a recoverable exception during execution. |
| **[MethodRetryHandler](../../../../org/apache/commons/httpclient/MethodRetryHandler.html "interface in org.apache.commons.httpclient")** | **Deprecated.** *use [`HttpMethodRetryHandler`](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient")* |

| **Class Summary** | |
| --- | --- |
| **[ChunkedInputStream](../../../../org/apache/commons/httpclient/ChunkedInputStream.html "class in org.apache.commons.httpclient")** | Transparently coalesces chunks of a HTTP stream that uses Transfer-Encoding chunked. |
| **[ChunkedOutputStream](../../../../org/apache/commons/httpclient/ChunkedOutputStream.html "class in org.apache.commons.httpclient")** | Implements HTTP chunking support. |
| **[ConnectMethod](../../../../org/apache/commons/httpclient/ConnectMethod.html "class in org.apache.commons.httpclient")** | Establishes a tunneled HTTP connection via the CONNECT method. |
| **[ContentLengthInputStream](../../../../org/apache/commons/httpclient/ContentLengthInputStream.html "class in org.apache.commons.httpclient")** | Cuts the wrapped InputStream off after a specified number of bytes. |
| **[Cookie](../../../../org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient")** | HTTP "magic-cookie" represents a piece of state information that the HTTP agent and the target server can exchange to maintain a session. |
| **[DefaultHttpMethodRetryHandler](../../../../org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html "class in org.apache.commons.httpclient")** | The default [`HttpMethodRetryHandler`](../../../../org/apache/commons/httpclient/HttpMethodRetryHandler.html "interface in org.apache.commons.httpclient") used by [`HttpMethod`](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")s. |
| **[DefaultMethodRetryHandler](../../../../org/apache/commons/httpclient/DefaultMethodRetryHandler.html "class in org.apache.commons.httpclient")** | **Deprecated.** *use [`DefaultHttpMethodRetryHandler`](../../../../org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html "class in org.apache.commons.httpclient")* |
| **[Header](../../../../org/apache/commons/httpclient/Header.html "class in org.apache.commons.httpclient")** | An HTTP header. |
| **[HeaderElement](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient")** | One element of an HTTP header's value. |
| **[HeaderGroup](../../../../org/apache/commons/httpclient/HeaderGroup.html "class in org.apache.commons.httpclient")** | A class for combining a set of headers. |
| **[HostConfiguration](../../../../org/apache/commons/httpclient/HostConfiguration.html "class in org.apache.commons.httpclient")** | Holds all of the variables needed to describe an HTTP connection to a host. |
| **[HttpClient](../../../../org/apache/commons/httpclient/HttpClient.html "class in org.apache.commons.httpclient")** | An HTTP "user-agent", containing an [`HTTP state`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient") and one or more [`HTTP connections`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient"), to which [`HTTP methods`](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient") can be applied. |
| **[HttpConnection](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient")** | An abstraction of an HTTP [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io") and [`OutputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/OutputStream.html "class or interface in java.io") pair, together with the relevant attributes. |
| **[HttpConstants](../../../../org/apache/commons/httpclient/HttpConstants.html "class in org.apache.commons.httpclient")** | **Deprecated.** *use EncodingUtil class* |
| **[HttpHost](../../../../org/apache/commons/httpclient/HttpHost.html "class in org.apache.commons.httpclient")** | Holds all of the variables needed to describe an HTTP connection to a host. |
| **[HttpMethodBase](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient")** | An abstract base implementation of HttpMethod. |
| **[HttpParser](../../../../org/apache/commons/httpclient/HttpParser.html "class in org.apache.commons.httpclient")** | A utility class for parsing http header values according to RFC-2616 Section 4 and 19.3. |
| **[HttpState](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient")** | A container for HTTP attributes that may persist from request to request, such as [`cookies`](../../../../org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient") and authentication [`credentials`](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient"). |
| **[HttpStatus](../../../../org/apache/commons/httpclient/HttpStatus.html "class in org.apache.commons.httpclient")** | Constants enumerating the HTTP status codes. |
| **[HttpsURL](../../../../org/apache/commons/httpclient/HttpsURL.html "class in org.apache.commons.httpclient")** | The HTTPS URL. |
| **[HttpURL](../../../../org/apache/commons/httpclient/HttpURL.html "class in org.apache.commons.httpclient")** | The HTTP URL. |
| **[HttpVersion](../../../../org/apache/commons/httpclient/HttpVersion.html "class in org.apache.commons.httpclient")** | HTTP version, as specified in RFC 2616. |
| **[MultiThreadedHttpConnectionManager](../../../../org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html "class in org.apache.commons.httpclient")** | Manages a set of HttpConnections for various HostConfigurations. |
| **[NameValuePair](../../../../org/apache/commons/httpclient/NameValuePair.html "class in org.apache.commons.httpclient")** | A simple class encapsulating a name/value pair. |
| **[NTCredentials](../../../../org/apache/commons/httpclient/NTCredentials.html "class in org.apache.commons.httpclient")** | [`Credentials`](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient") for use with the NTLM authentication scheme which requires additional information. |
| **[ProxyClient](../../../../org/apache/commons/httpclient/ProxyClient.html "class in org.apache.commons.httpclient")** | A client that provides [`sockets`](http://java.sun.com/j2se/1.5.0/docs/api/java/net/Socket.html "class or interface in java.net") for communicating through HTTP proxies via the HTTP CONNECT method. |
| **[ProxyClient.ConnectResponse](../../../../org/apache/commons/httpclient/ProxyClient.ConnectResponse.html "class in org.apache.commons.httpclient")** | Contains the method used to execute the connect along with the created socket. |
| **[ProxyHost](../../../../org/apache/commons/httpclient/ProxyHost.html "class in org.apache.commons.httpclient")** | Holds all of the variables needed to describe an HTTP connection to a proxy. |
| **[SimpleHttpConnectionManager](../../../../org/apache/commons/httpclient/SimpleHttpConnectionManager.html "class in org.apache.commons.httpclient")** | A connection manager that provides access to a single HttpConnection. |
| **[StatusLine](../../../../org/apache/commons/httpclient/StatusLine.html "class in org.apache.commons.httpclient")** | Represents a Status-Line as returned from a HTTP server. |
| **[URI](../../../../org/apache/commons/httpclient/URI.html "class in org.apache.commons.httpclient")** | The interface for the URI(Uniform Resource Identifiers) version of RFC 2396. |
| **[URI.LocaleToCharsetMap](../../../../org/apache/commons/httpclient/URI.LocaleToCharsetMap.html "class in org.apache.commons.httpclient")** | A mapping to determine the (somewhat arbitrarily) preferred charset for a given locale. |
| **[UsernamePasswordCredentials](../../../../org/apache/commons/httpclient/UsernamePasswordCredentials.html "class in org.apache.commons.httpclient")** | Username and password [`Credentials`](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient"). |

| **Exception Summary** | |
| --- | --- |
| **[CircularRedirectException](../../../../org/apache/commons/httpclient/CircularRedirectException.html "class in org.apache.commons.httpclient")** | Signals a circular redirect |
| **[ConnectionPoolTimeoutException](../../../../org/apache/commons/httpclient/ConnectionPoolTimeoutException.html "class in org.apache.commons.httpclient")** | A timeout while connecting waiting for an available connection from an HttpConnectionManager. |
| **[ConnectTimeoutException](../../../../org/apache/commons/httpclient/ConnectTimeoutException.html "class in org.apache.commons.httpclient")** | A timeout while connecting to an HTTP server or waiting for an available connection from an HttpConnectionManager. |
| **[HttpContentTooLargeException](../../../../org/apache/commons/httpclient/HttpContentTooLargeException.html "class in org.apache.commons.httpclient")** | Signals that the response content was larger than anticipated. |
| **[HttpException](../../../../org/apache/commons/httpclient/HttpException.html "class in org.apache.commons.httpclient")** | Signals that an HTTP or HttpClient exception has occurred. |
| **[HttpRecoverableException](../../../../org/apache/commons/httpclient/HttpRecoverableException.html "class in org.apache.commons.httpclient")** | **Deprecated.** *no longer used* |
| **[InvalidRedirectLocationException](../../../../org/apache/commons/httpclient/InvalidRedirectLocationException.html "class in org.apache.commons.httpclient")** | Signals violation of HTTP specification caused by an invalid redirect location |
| **[NoHttpResponseException](../../../../org/apache/commons/httpclient/NoHttpResponseException.html "class in org.apache.commons.httpclient")** | Signals that the target server failed to respond with a valid HTTP response. |
| **[ProtocolException](../../../../org/apache/commons/httpclient/ProtocolException.html "class in org.apache.commons.httpclient")** | Signals that an HTTP protocol violation has occurred. |
| **[RedirectException](../../../../org/apache/commons/httpclient/RedirectException.html "class in org.apache.commons.httpclient")** | Signals violation of HTTP specification caused by an invalid redirect |
| **[URI.DefaultCharsetChanged](../../../../org/apache/commons/httpclient/URI.DefaultCharsetChanged.html "class in org.apache.commons.httpclient")** | The charset-changed normal operation to represent to be required to alert to user the fact the default charset is changed. |
| **[URIException](../../../../org/apache/commons/httpclient/URIException.html "class in org.apache.commons.httpclient")** | The URI parsing and escape encoding exception. |

| **Error Summary** | |
| --- | --- |
| **[HttpClientError](../../../../org/apache/commons/httpclient/HttpClientError.html "class in org.apache.commons.httpclient")** | Signals that an error has occurred. |

## Package org.apache.commons.httpclient Description

### Classes and interfaces supporting the client side of the HTTP protocol.

The *HttpClient* component supports the client-side of
[RFC 1945 (HTTP/1.0)](http://www.w3.org/Protocols/rfc1945/rfc1945.txt) and
[RFC 2616 (HTTP/1.1)](http://www.w3.org/Protocols/rfc2616/rfc2616.txt),
several related specifications
([RFC 2109 (Cookies)](http://www.w3.org/Protocols/rfc2109/rfc2109.txt),
[RFC 2617 (HTTP Authentication)](http://www.ietf.org/rfc/rfc2617.txt),
etc.), and provides a framework by which new request types (methods) or HTTP
extensions can can be easily created or supported.

The basis for the abstraction is provided by three types:

[`HttpConnection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient")
:   represents a network connection to some HTTP host.

[`HttpMethod`](../../../../org/apache/commons/httpclient/HttpMethod.html "interface in org.apache.commons.httpclient")
:   represents a request to be made over some
    [`HttpConnection`](../../../../org/apache/commons/httpclient/HttpConnection.html "class in org.apache.commons.httpclient")
    and contains the server's response.

[`HttpState`](../../../../org/apache/commons/httpclient/HttpState.html "class in org.apache.commons.httpclient")
:   contains the HTTP attributes that may persist from
    request to request, such as cookies and authentication
    credentials.

and several simple bean-style classes:

[`Cookie`](../../../../org/apache/commons/httpclient/Cookie.html "class in org.apache.commons.httpclient")
:   represents HTTP cookie.

[`Credentials`](../../../../org/apache/commons/httpclient/Credentials.html "interface in org.apache.commons.httpclient")
:   an interface representing a set of authentication credentials.

[`Header`](../../../../org/apache/commons/httpclient/Header.html "class in org.apache.commons.httpclient")
:   represents an HTTP request or response header.

[`HeaderElement`](../../../../org/apache/commons/httpclient/HeaderElement.html "class in org.apache.commons.httpclient")
:   represents a single element of a multi-part header.

[`UsernamePasswordCredentials`](../../../../org/apache/commons/httpclient/UsernamePasswordCredentials.html "class in org.apache.commons.httpclient")
:   a username and password pair.

[`HttpClient`](../../../../org/apache/commons/httpclient/HttpClient.html "class in org.apache.commons.httpclient") provides a
simple "user-agent" implementation that will suffice for many
applications, but whose use is not required.

*HttpClient* also provides several utilities that may be
useful when extending the framework:

[`HttpMethodBase`](../../../../org/apache/commons/httpclient/HttpMethodBase.html "class in org.apache.commons.httpclient")
:   an abstract base implementation of HttpMethod,
    which may be extended to create new method types or
    to support additional protocol HTTP features.

[`HttpStatus`](../../../../org/apache/commons/httpclient/HttpStatus.html "class in org.apache.commons.httpclient")
:   an enumeration of HttpStatus codes.

[`ChunkedOutputStream`](../../../../org/apache/commons/httpclient/ChunkedOutputStream.html "class in org.apache.commons.httpclient")
:   an [`OutputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/OutputStream.html "class or interface in java.io") wrapper supporting the "chunked"
    transfer encoding.

[`ChunkedInputStream`](../../../../org/apache/commons/httpclient/ChunkedInputStream.html "class in org.apache.commons.httpclient")
:   an [`InputStream`](http://java.sun.com/j2se/1.5.0/docs/api/java/io/InputStream.html "class or interface in java.io") wrapper supporting the "chunked"
    transfer encoding.

[`URIUtil`](../../../../org/apache/commons/httpclient/util/URIUtil.html "class in org.apache.commons.httpclient.util")
:   provides utilities for encoding and decoding URI's in the
    %HH format.

#### HttpClient Configuration with Java Properties

Java properties can be set at run time with the `-Dname=value
command line arguments to the application that uses HttpClient.
These properties can also be set programaticly by calling
System.getProperties().setProperty(name, value).
This is the list of properties that HttpClient recognizes:

| Name | Type | Effect |
| --- | --- | --- |
| httpclient.useragent | String | Sets the User-Agent string to be sent on every HTTP request. |
| httpclient.authentication.preemptive | boolean | Sends authorization credentials without requiring explicit requests from the web server |

---





|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Overview | Package | Class | Use | Tree | Deprecated | Index | Help | | |  |
| PREV PACKAGE   NEXT PACKAGE | FRAMES    NO FRAMES |




---

Copyright © 2001-2008 Apache Software Foundation. All Rights Reserved.`

---
