# Apache Guacamole Manual

# Apache Guacamole Manual[#](#apache-guacamole-manual "Link to this heading")

Note

Licensed to the Apache Software Foundation (ASF) under one or more contributor
license agreements. See the [NOTICE](https://raw.githubusercontent.com/apache/guacamole-manual/master/NOTICE) file distributed with this work for
additional information regarding copyright ownership. The ASF licenses this
file to you under the Apache License, Version 2.0 (the “License”); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at:

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Getting Started

* [Introduction](introduction.html)
* [Implementation and architecture](guacamole-architecture.html)
* [Installing Guacamole](installing-guacamole.html)
* [Database setup](jdbc-auth.html)
* [Securing a Guacamole install](security.html)

Using Guacamole

* [Configuration](configuring-guacamole.html)
* [General usage](using-guacamole.html)
* [Administration](administration.html)
* [Troubleshooting](troubleshooting.html)

Extensions

* [Active Directory / LDAP](ldap-auth.html)
* [Multi-factor authentication](mfa.html)
* [Single sign-on](sso.html)
* [Retrieving secrets from a vault](vault.html)
* [External authentication](external-auth.html)
* [RADIUS](radius-auth.html)
* [Ad-hoc connections](adhoc-connections.html)
* [Login / Connection restrictions](auth-restrict.html)
* [Session recording player](recording-playback.html)

Developer's Guide

* [The Guacamole protocol](guacamole-protocol.html)
* [libguac](libguac.html)
* [guacamole-common](guacamole-common.html)
* [guacamole-common-js](guacamole-common-js.html)
* [guacamole-ext](guacamole-ext.html)
* [Adding new protocols](custom-protocols.html)
* [Custom authentication](custom-auth.html)
* [Event listeners](event-listeners.html)
* [Writing your own Guacamole application](writing-you-own-guacamole-app.html)

Appendices

* [Guacamole protocol reference](protocol-reference.html)
* [Database schema reference](jdbc-auth-schema.html)

---
# Multi-factor authentication

# Multi-factor authentication[#](#multi-factor-authentication "Link to this heading")

Multi-factor authentication (MFA) allows you to require that users verify their
identities through additional mechanisms beyond simply entering a username and
password, such as by using a mobile authenticator app. Guacamole supports the
following MFA methods:

[Duo](duo-auth.html)
:   A proprietary MFA mechanism provided by a third-party commercial company via
    their own proprietary mobile app.

[TOTP](totp-auth.html)
:   A standard, non-proprietary, widely supported algorithm for generating
    temporary authentication codes. This is the algorithm used by several common
    authenticator apps, including Google Authenticator.

If you are using a [single sign-on provider](sso.html), configuring your provider to
require MFA as part of the authentication process is also a possibility. In
this case, leveraging a dedicated Guacamole extension to provide MFA is not
necesary.

---
# Database setup for MariaDB / MySQL

## Contents

# Database setup for MariaDB / MySQL[#](#database-setup-for-mariadb-mysql "Link to this heading")

To use Guacamole with a MariaDB or MySQL database, you will need:

1. An instance of the MariaDB or MySQL database server.
2. Sufficient permission to create new databases, to create new users, and to
   grant those users permissions.
3. Network access to the database from the Guacamole server.

If this is not the case, install your database of choice now. Most
distributions will provide a convenient MariaDB or MySQL package which will set
up everything for you. If you prefer Docker, the [`mysql`](https://hub.docker.com/_/mysql)
and [`mariadb`](https://hub.docker.com/_/mariadb) Docker images are also
reasonable options. If you don’t wish to use MariaDB or MySQL, Guacamole
additionally supports:

* [PostgreSQL](postgresql-auth.html)
* [SQL Server](sqlserver-auth.html)

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Creating a new database for Guacamole[#](#creating-a-new-database-for-guacamole "Link to this heading")

It is best practice to use a dedicated database and user for the Guacamole web
application, and these instructions cover only this method.

If using the [`mariadb`](https://hub.docker.com/_/mariadb) or [`mysql`](https://hub.docker.com/_/mysql) Docker images:
:   Set the `MARIADB_DATABASE` or `MYSQL_DATABASE` environment variables
    respectively to the desired name of the database. The Docker image will
    automatically create this database when the container starts for the first
    time.

If using a native installation of MariaDB or MySQL:
:   Manually create a database for MySQL and MariaDB by executing a
    `CREATE DATABASE` query with the `mysql` client:

    ```
    CREATE DATABASE guacamole_db;
    ```

### Initializing the database[#](#initializing-the-database "Link to this heading")

Native Webapp (Tomcat)

The schema scripts necessary to initialize the MySQL version of Guacamole’s
database are provided within the `mysql/schema/` directory of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download),
which must be downloaded from [the release page for Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
and extracted first.

Running each of these scripts against the newly created database will
initialize it with Guacamole’s schema. You can run these scripts using the
standard `mysql` client, but the method of running `mysql` varies depending on
whether you are using Docker to provide your database.

If using the [`mariadb`](https://hub.docker.com/_/mariadb) or [`mysql`](https://hub.docker.com/_/mysql) Docker images:
:   The schema initialization scripts should be run against the newly created
    database by running the standard `mysql` command-line client *within the
    container*:

    ```
    $ cat schema/*.sql | docker exec -i some-mysql \
        sh -c 'mysql -u root -p"$MYSQL_ROOT_PASSWORD" guacamole_db'
    ```

If using a native installation of MariaDB or MySQL:
:   The schema initialization scripts should be run against the newly created
    database using the standard `mysql` client directly from the command-line:

    ```
    $ cat schema/*.sql | mysql -u root -p guacamole_db
    Enter password:
    $
    ```

Container (Docker)

The schema scripts necessary to initialize the MySQL version of Guacamole’s
database are provided within the `/opt/guacamole/extensions/guacamole-auth-jdbc/mysql/schema`
directory of the `guacamole/guacamole` image.

Additionally, an `initdb.sh` script is provided at `/opt/guacamole/bin/initdb.sh`
that can be used to extract the required schema initialization script:

```
$ docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --mysql > initdb.sql
```

If using the [`mariadb`](https://hub.docker.com/_/mariadb) or [`mysql`](https://hub.docker.com/_/mysql) Docker images via Docker Compose:
:
The easiest way to initialize Guacamole’s database is to use a volume mount to
map the bundled schema initialization scripts from the Guacamole container into
the database container. For example, if using Docker Compose:

1. Declare a named volume at the root level of your `docker-compose.yml`:

   ```
   volumes:
       initdb:
   ```
2. Reference the named volume within your Guacamole service, effectively
   pulling the schema initialization scripts from that container and into the
   volume:

   ```
   volumes:
       - "initdb:/opt/guacamole/extensions/guacamole-auth-jdbc/mysql/schema:ro"
   ```
3. Reference the named volume within your database service, bringing the
   schema initialization scripts into the directory used by the database
   image for one-time initialization:

   ```
   volumes:
       - "initdb:/docker-entrypoint-initdb.d:ro"
   ```

If using the [`mariadb`](https://hub.docker.com/_/mariadb) or [`mysql`](https://hub.docker.com/_/mysql) Docker images *without* Docker Compose:
:   Use the `initdb.sh` script included with the `guacamole/guacamole` image to
    send the required initialization script to the standard `mysql` command-line
    client *within the database container*:

    ```
    $ docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --mysql | \
        docker exec -i some-mysql sh -c 'mysql -u root -p"$MYSQL_ROOT_PASSWORD" guacamole_db'
    ```

If using a native installation of MariaDB or MySQL:
:   Use the `initdb.sh` script included with the `guacamole/guacamole` image to
    automatically produce the SQL required to initialize an existing database:

    ```
    $ docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --mysql | \
        mysql -u root -p guacamole_db
    ```

### Granting Guacamole access to the database[#](#granting-guacamole-access-to-the-database "Link to this heading")

For Guacamole to be able to execute queries against the database, you must
create a new user for the database and grant that user sufficient privileges to
manage the contents of all tables in the database.

If using the [`mariadb`](https://hub.docker.com/_/mariadb) or [`mysql`](https://hub.docker.com/_/mysql) Docker images:
:   Set the `MARIADB_USER` or `MYSQL_USER` environment variables respectively to
    the desired name of the dedicated user, and the `MARIADB_PASSWORD` (or
    `MYSQL_PASSWORD`) environment variable to the desired password. The Docker
    image will automatically create this user when the container starts and grant
    them full access to the Guacamole database.

If using a native installation of MariaDB or MySQL:
:   The dedicated user for Guacamole must be manually created and granted
    sufficient privileges. The user created for Guacamole needs only `SELECT`,
    `UPDATE`, `INSERT`, and `DELETE` permissions on all tables in the Guacamole
    database.

    ```
    CREATE USER 'guacamole_user' IDENTIFIED BY 'some_password';
    GRANT SELECT,INSERT,UPDATE,DELETE ON guacamole_db.* TO 'guacamole_user';
    FLUSH PRIVILEGES;
    ```

## Upgrading an existing Guacamole database[#](#upgrading-an-existing-guacamole-database "Link to this heading")

If you are upgrading from a version of Guacamole older than 1.6.0, you
may need to run one or more database schema upgrade scripts located within the
`mysql/schema/upgrade/` directory of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download)
(available from [the release page for Apache Guacamole
1.6.0](https://guacamole.apache.org/releases/1.6.0)).

Each of these scripts is named `upgrade-pre-VERSION.sql` where
`VERSION` is the version of Guacamole where those changes were introduced. They
need to be run when you are upgrading from a version of Guacamole older than
`VERSION`.

If there are no `upgrade-pre-VERSION.sql` scripts present in the
`schema/upgrade/` directory which apply to your existing Guacamole database,
then the schema has not changed between your version and the version your are
installing, and there is no need to run any database upgrade scripts.

These scripts are incremental and, when relevant, *must be run in order*. For
example, if you are upgrading an existing database from version
0.9.13-incubating to version 1.0.0, you would need to run the
`upgrade-pre-0.9.14.sql` script (because 0.9.13-incubating is older than
0.9.14), followed by the `upgrade-pre-1.0.0.sql` script (because
0.9.13-incubating is also older than 1.0.0).

## Installing/Enabling support for MariaDB/MySQL[#](#installing-enabling-support-for-mariadb-mysql "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. You should have a copy of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download) from
   earlier when you [created and initialized the database](#mysql-auth-database-creation).
2. Create the `GUACAMOLE_HOME/extensions` and `GUACAMOLE_HOME/lib` directories,
   if they do not already exist.
3. Copy `mysql/guacamole-auth-jdbc-mysql-1.6.0.jar`
   within `GUACAMOLE_HOME/extensions`.
4. Copy the JDBC driver for your database to `GUACAMOLE_HOME/lib`.
   Either of the following MySQL-compatible JDBC drivers are supported
   for connecting Guacamole with MariaDB or MySQL:

   * [MariaDB Connector/J](https://mariadb.com/kb/en/about-mariadb-connector-j/)
   * [MySQL Connector/J](http://dev.mysql.com/downloads/connector/j/) (the required `.jar` will be within a `.tar.gz` archive)

   If you do not have a specific reason to use one driver over the other, it’s
   recommended that you use the JDBC driver provided by your database vendor.
5. Configure Guacamole to use database authentication, as described below.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `MYSQL_ENABLED` environment variable:

    ```
    MYSQL_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e MYSQL_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `MYSQL_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `MYSQL_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

Important

**Older versions of MySQL Connector/J have known issues with SSL
verification.** If you experience problems connecting to SSL-secured MySQL
databases, it is recommended that you update to a current version of the
driver.

## Required configuration[#](#required-configuration "Link to this heading")

Additional configuration options must be specified for Guacamole to properly
connect to your database. These options are specific to the database being
used, and must be set correctly for authentication to work.

The options absolutely required by the database authentication extension are
relatively few and self-explanatory, describing only which database will be
used and how Guacamole will authenticate when querying that database:

Native Webapp (Tomcat)

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
mysql-database: guacamole_db
mysql-username: guacamole_user
mysql-password: some_password
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`mysql-database`
:   The name of the database that you created for Guacamole. This is given as
    “guacamole\_db” in the examples given in this chapter.

`mysql-username`
:   The username of the user that Guacamole should use to connect to the
    database. This is given as “guacamole\_user” in the examples given in this
    chapter.

`mysql-password`
:   The password Guacamole should provide when authenticating with the database.
    This is given as “some\_password” in the examples given in this chapter.

Container (Docker)

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
MYSQL_DATABASE: 'guacamole_db'
MYSQL_USERNAME: 'guacamole_user'
MYSQL_PASSWORD: 'some_password'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e MYSQL_DATABASE="guacamole_db" \
    -e MYSQL_USERNAME="guacamole_user" \
    -e MYSQL_PASSWORD="some_password" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`MYSQL_DATABASE`
:   The name of the database that you created for Guacamole. This is given as
    “guacamole\_db” in the examples given in this chapter.

`MYSQL_USERNAME`
:   The username of the user that Guacamole should use to connect to the
    database. This is given as “guacamole\_user” in the examples given in this
    chapter.

`MYSQL_PASSWORD`
:   The password Guacamole should provide when authenticating with the database.
    This is given as “some\_password” in the examples given in this chapter.

Hint

**Double-check these values.** You will not be able to sign into Guacamole
after installation if these parameters do not match the correct database name,
username, and password.

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Additional options are available to control how Guacamole connects to the
database server:

Native Webapp (Tomcat)

`mysql-hostname`
:   The hostname or IP address of the server hosting your database. If not
    specified, “localhost” will be used by default.

`mysql-port`
:   The port number of the MySQL or MariaDB database to connect to. If not
    specified, the standard MySQL / MariaDB port 3306 will be used.

`mysql-driver`
:   Controls which JDBC driver the extension attempts to load. By default, the
    installed JDBC driver will be automatically detected. Possible values are:

    mysql
    :   [The **MySQL** Connector/J JDBC driver](https://dev.mysql.com/downloads/connector/j/).

    mariadb
    :   [The **MariaDB** Connector/J JDBC driver](https://mariadb.com/kb/en/about-mariadb-connector-j/).

`mysql-server-timezone`
:   Specifies the timezone the MySQL server is configured to run in. While the
    MySQL driver attempts to auto-detect the timezone in use by the server, there
    are many cases where the timezone provided by the operating system is either
    unknown by Java, or matches multiple timezones. In these cases MySQL may
    either complain or refuse the connection unless the timezone is specified as
    part of the connection. This property allows the timezone of the server to be
    specified so that the connection can continue and the JDBC driver can
    properly translate timestamps. The property accepts timezones in the
    following formats:

    Region/Locale
    :   Well-known time zone identifiers, in the Region/Locale format, as defined
        by the [IANA time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
        such as `America/Los_Angeles`, `Africa/Johannesburg`, or `China/Shanghai`.

    GMT+/-HH:MM
    :   GMT or custom timezones specified by GMT offset, such as `GMT`, `GMT+0130`,
        `GMT+06:00`, or `GMT-9`.

`mysql-ssl-mode`
:   This property sets the SSL mode that the JDBC driver will attempt to use when
    communicating with the remote MySQL server. The values for this property
    match the standard values supported by the MySQL and MariaDB JDBC drivers:

    disabled
    :   Do not use SSL, and fail if the server requires it. For compatibility this
        will also set the legacy JDBC driver property useSSL to false.

    preferred
    :   Prefer SSL, but fall back to plain-text if an SSL connection cannot be
        negotiated. This is the default.

    required
    :   Require SSL connections, and fail if SSL cannot be negotiated. This mode
        does not perform any validition checks on the certificate in use by the
        server, the issuer, etc.

    verify-ca
    :   Require SSL connections, and check to make sure that the certificate issuer
        is known to be valid.

    verify-identity
    :   Require SSL connections, and check to make sure that the server certificate
        is issued by a known authority, and that the identity of the server
        matches the identity on the certificate.

`mysql-ssl-trust-store`
:   The file that will store trusted SSL certificates for the JDBC driver to use
    when validating CA and server certificates. This should be a JKS-formatted
    certificate store. This property is optional and defaults to Java’s normal
    trusted certificate locations, which vary based on the version of Java in
    use.

`mysql-ssl-trust-password`
:   The password to use to access the SSL trusted certificate store, if one is
    required. By default no password will be used.

`mysql-ssl-client-store`
:   The file that contains the client certificate to use when making SSL
    connections to the MySQL server. This should be a JKS-formatted certificate
    store that contains a private key and certificate pair. This property is
    optional, and by default no client certificate will be used for the SSL
    connection.

`mysql-ssl-client-password`
:   The password to use to access the client certificate store, if one is
    required. By default no password will be used.

`mysql-batch-size`
:   Controls how many objects may be retrieved from the database in a single
    query. If more objects than this number are requested, retrieval of those
    objects will be automatically and transparently split across multiple
    queries.

    By default, MySQL/MariaDB queries will retrieve no more than 1000 objects.

Container (Docker)

`MYSQL_HOSTNAME`
:   The hostname or IP address of the server hosting your database. If not
    specified, “localhost” will be used by default.

`MYSQL_PORT`
:   The port number of the MySQL or MariaDB database to connect to. If not
    specified, the standard MySQL / MariaDB port 3306 will be used.

`MYSQL_DRIVER`
:   Controls which JDBC driver the extension attempts to load. By default, the
    installed JDBC driver will be automatically detected. Possible values are:

    mysql
    :   [The **MySQL** Connector/J JDBC driver](https://dev.mysql.com/downloads/connector/j/).

    mariadb
    :   [The **MariaDB** Connector/J JDBC driver](https://mariadb.com/kb/en/about-mariadb-connector-j/).

`MYSQL_SERVER_TIMEZONE`
:   Specifies the timezone the MySQL server is configured to run in. While the
    MySQL driver attempts to auto-detect the timezone in use by the server, there
    are many cases where the timezone provided by the operating system is either
    unknown by Java, or matches multiple timezones. In these cases MySQL may
    either complain or refuse the connection unless the timezone is specified as
    part of the connection. This property allows the timezone of the server to be
    specified so that the connection can continue and the JDBC driver can
    properly translate timestamps. The property accepts timezones in the
    following formats:

    Region/Locale
    :   Well-known time zone identifiers, in the Region/Locale format, as defined
        by the [IANA time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
        such as `America/Los_Angeles`, `Africa/Johannesburg`, or `China/Shanghai`.

    GMT+/-HH:MM
    :   GMT or custom timezones specified by GMT offset, such as `GMT`, `GMT+0130`,
        `GMT+06:00`, or `GMT-9`.

`MYSQL_SSL_MODE`
:   This property sets the SSL mode that the JDBC driver will attempt to use when
    communicating with the remote MySQL server. The values for this property
    match the standard values supported by the MySQL and MariaDB JDBC drivers:

    disabled
    :   Do not use SSL, and fail if the server requires it. For compatibility this
        will also set the legacy JDBC driver property useSSL to false.

    preferred
    :   Prefer SSL, but fall back to plain-text if an SSL connection cannot be
        negotiated. This is the default.

    required
    :   Require SSL connections, and fail if SSL cannot be negotiated. This mode
        does not perform any validition checks on the certificate in use by the
        server, the issuer, etc.

    verify-ca
    :   Require SSL connections, and check to make sure that the certificate issuer
        is known to be valid.

    verify-identity
    :   Require SSL connections, and check to make sure that the server certificate
        is issued by a known authority, and that the identity of the server
        matches the identity on the certificate.

`MYSQL_SSL_TRUST_STORE`
:   The file that will store trusted SSL certificates for the JDBC driver to use
    when validating CA and server certificates. This should be a JKS-formatted
    certificate store. This property is optional and defaults to Java’s normal
    trusted certificate locations, which vary based on the version of Java in
    use.

`MYSQL_SSL_TRUST_PASSWORD`
:   The password to use to access the SSL trusted certificate store, if one is
    required. By default no password will be used.

`MYSQL_SSL_CLIENT_STORE`
:   The file that contains the client certificate to use when making SSL
    connections to the MySQL server. This should be a JKS-formatted certificate
    store that contains a private key and certificate pair. This property is
    optional, and by default no client certificate will be used for the SSL
    connection.

`MYSQL_SSL_CLIENT_PASSWORD`
:   The password to use to access the client certificate store, if one is
    required. By default no password will be used.

`MYSQL_BATCH_SIZE`
:   Controls how many objects may be retrieved from the database in a single
    query. If more objects than this number are requested, retrieval of those
    objects will be automatically and transparently split across multiple
    queries.

    By default, MySQL/MariaDB queries will retrieve no more than 1000 objects.

### Enforcing password policies[#](#enforcing-password-policies "Link to this heading")

Configuration options are available for enforcing rules intended to encourage
password complexity and regular changing of passwords. None of these options
are enabled by default, but can be selectively enabled as needed.

#### Password complexity[#](#password-complexity "Link to this heading")

Administrators can require that passwords have a certain level of complexity,
such as having both uppercase and lowercase letters (“multiple case”), at least
one digit, or at least one symbol, and can prohibit passwords from containing
the user’s own username.

With respect to password content, the database authentication defines a “digit”
as any numeric character and a “symbol” is any non-alphanumeric character. This
takes non-English languages into account, thus a digit is not simply “0”
through “9” but rather [any character defined in Unicode as
numeric](https://en.wikipedia.org/wiki/Numerals_in_Unicode), and a symbol is
any character which Unicode does not define as alphabetic or numeric.

The check for whether a password contains the user’s own username is performed
in a case-insensitive manner. For example, if the user’s username is “phil”,
the passwords “ch!0roPhil” and “PHIL-o-dendr0n” would still be prohibited.

Native Webapp (Tomcat)

`mysql-user-password-min-length`
:   The minimum length required of all user passwords, in characters. By default,
    password length is not enforced.

`mysql-user-password-require-multiple-case`
:   Whether all user passwords must have at least one lowercase character and one
    uppercase character. By default, no such restriction is imposed.

`mysql-user-password-require-symbol`
:   Whether all user passwords must have at least one non-alphanumeric character
    (symbol). By default, no such restriction is imposed.

`mysql-user-password-require-digit`
:   Whether all user passwords must have at least one numeric character (digit).
    By default, no such restriction is imposed.

`mysql-user-password-prohibit-username`
:   Whether users are prohibited from including their own username in their
    password. By default, no such restriction is imposed.

Container (Docker)

`MYSQL_USER_PASSWORD_MIN_LENGTH`
:   The minimum length required of all user passwords, in characters. By default,
    password length is not enforced.

`MYSQL_USER_PASSWORD_REQUIRE_MULTIPLE_CASE`
:   Whether all user passwords must have at least one lowercase character and one
    uppercase character. By default, no such restriction is imposed.

`MYSQL_USER_PASSWORD_REQUIRE_SYMBOL`
:   Whether all user passwords must have at least one non-alphanumeric character
    (symbol). By default, no such restriction is imposed.

`MYSQL_USER_PASSWORD_REQUIRE_DIGIT`
:   Whether all user passwords must have at least one numeric character (digit).
    By default, no such restriction is imposed.

`MYSQL_USER_PASSWORD_PROHIBIT_USERNAME`
:   Whether users are prohibited from including their own username in their
    password. By default, no such restriction is imposed.

#### Password age / expiration[#](#password-age-expiration "Link to this heading")

“Password age” refers to two separate concepts:

1. Requiring users to change their password after a certain amount of time has
   elapsed since the last password change (maximum password age).
2. Preventing users from changing their password too frequently (minimum
   password age).

While it may seem strange to prevent users from changing their password too
frequently, it does make sense if you are concerned that rapid password changes
may defeat password expiration (users could immediately change the password
back) or tracking of password history (users could cycle through passwords
until the history is exhausted and their old password is usable again).

By default, the database authentication does not apply any limits to password
age, and users with permission to change their passwords may do so as
frequently or infrequently as they wish. Password age limits can be enabled
using a pair of configuration options, each accepting values given in units of
days:

Native Webapp (Tomcat)

`mysql-user-password-min-age`
:   The minimum number of days which must elapse before a user may reset their
    password, where zero represents no limit. By default, no minimum number of
    days is required.

`mysql-user-password-max-age`
:   The maximum number of days which may elapse before a user is automatically
    required to reset their password, where zero represents no limit. By default,
    users are not automatically required to reset their password based on
    password age.

Container (Docker)

`MYSQL_USER_PASSWORD_MIN_AGE`
:   The minimum number of days which must elapse before a user may reset their
    password, where zero represents no limit. By default, no minimum number of
    days is required.

`MYSQL_USER_PASSWORD_MAX_AGE`
:   The maximum number of days which may elapse before a user is automatically
    required to reset their password, where zero represents no limit. By default,
    users are not automatically required to reset their password based on
    password age.

Important

So that administrators can always intervene in the case that a password needs
to be reset despite restrictions, the minimum age restriction does not apply to
any user with permission to administer the system.

#### Preventing password reuse[#](#preventing-password-reuse "Link to this heading")

If desired, Guacamole can keep track of each user’s most recently used
passwords, and will prohibit reuse of those passwords until the password has
been changed sufficiently many times. By default, Guacamole will not keep track
of old passwords.

Note that these passwords are hashed in the same manner as each user’s current
password. When a user’s password is changed, the hash, salt, etc. currently
stored for that user is actually just copied verbatim (along with a timestamp)
into a list of historical passwords, with older entries from this list being
automatically deleted.

Native Webapp (Tomcat)

`mysql-user-password-history-size`
:   The number of previous passwords remembered for each user, where zero
    represents no history. If set to a non-zero value, users will be restricted
    from reusing any password in their password history. Passwords are remembered
    only in hashed and salted form. By default, previous passwords are not
    remembered and no such restriction is enforced.

Container (Docker)

`MYSQL_USER_PASSWORD_HISTORY_SIZE`
:   The number of previous passwords remembered for each user, where zero
    represents no history. If set to a non-zero value, users will be restricted
    from reusing any password in their password history. Passwords are remembered
    only in hashed and salted form. By default, previous passwords are not
    remembered and no such restriction is enforced.

### Concurrent use of Guacamole connections[#](#concurrent-use-of-guacamole-connections "Link to this heading")

The database authentication module provides configuration options to restrict
concurrent use of connections and connection groups. Concurrent use can be
restricted broadly or to ensure that each individual user may only maintain a
limited number of active connections to any one connection or group.

By default, concurrent usage is unrestricted except that each user may only
have a single active connection to each connection group. This is intended to
avoid the case that a single user is able to exhaust the contents of a
connection group and effectively block others from using the same resources.

If you wish to impose an absolute limit on the number of active connections
that can be established through Guacamole, ignoring which users or connections
are involved, this can be done as well.

The default policy set through these options can be overridden later on a
per-connection basis using the administrative interface.

Native Webapp (Tomcat)

`mysql-default-max-connections`
:   The maximum number of concurrent connections to allow to any one connection,
    regardless of which user is accessing the connection, where zero denotes
    unlimited. By default, overall concurrent access to individual connections is
    not limited.

`mysql-default-max-group-connections`
:   The maximum number of concurrent connections to allow to any one connection
    group, regardless of which user is accessing the connection group, where zero
    denotes unlimited. By default, overall concurrent access to individual
    connection groups is not limited.

`mysql-default-max-connections-per-user`
:   The maximum number of concurrent connections to allow to any one connection
    by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to individual connections is not limited.

`mysql-default-max-group-connections-per-user`
:   The maximum number of concurrent connections to allow to any one connection
    group by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to connection groups is limited to one user.

`mysql-absolute-max-connections`
:   The maximum number of concurrent connections to allow overall, regardless of
    which connection or connection group is used and regardless of which user is
    accessing the connection/group, where zero denotes unlimited. By default,
    overall concurrent access to Guacamole is not limited.

Container (Docker)

`MYSQL_DEFAULT_MAX_CONNECTIONS`
:   The maximum number of concurrent connections to allow to any one connection,
    regardless of which user is accessing the connection, where zero denotes
    unlimited. By default, overall concurrent access to individual connections is
    not limited.

`MYSQL_DEFAULT_MAX_GROUP_CONNECTIONS`
:   The maximum number of concurrent connections to allow to any one connection
    group, regardless of which user is accessing the connection group, where zero
    denotes unlimited. By default, overall concurrent access to individual
    connection groups is not limited.

`MYSQL_DEFAULT_MAX_CONNECTIONS_PER_USER`
:   The maximum number of concurrent connections to allow to any one connection
    by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to individual connections is not limited.

`MYSQL_DEFAULT_MAX_GROUP_CONNECTIONS_PER_USER`
:   The maximum number of concurrent connections to allow to any one connection
    group by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to connection groups is limited to one user.

`MYSQL_ABSOLUTE_MAX_CONNECTIONS`
:   The maximum number of concurrent connections to allow overall, regardless of
    which connection or connection group is used and regardless of which user is
    accessing the connection/group, where zero denotes unlimited. By default,
    overall concurrent access to Guacamole is not limited.

### External users and connections[#](#external-users-and-connections "Link to this heading")

When [combining LDAP with a database](ldap-auth.html#ldap-and-database), or using a single
sign-on system like [OpenID Connect](openid-auth.html) or [SAML](saml-auth.html), user
accounts are not purely defined by Guacamole’s database. They are additionally
defined by the relevant external system. In some cases, such as the [LDAP
extension’s capability to retrieve connection information from the LDAP
directory](ldap-auth.html#ldap-schema-changes), connections are not purely defined by
Guacamole’s database either.

In these cases, it may be desirable to:

* Limit use of Guacamole to only those users that *do* already exist in the
  database.
* Automatically create users in the database when they have successfully
  authenticated through other means, such that extensions requiring storage
  like TOTP can be used alongside SSO solutions.
* Control whether the database logs connection usage history for connections
  that are not maintained by the database.

By default, users will be allowed access to Guacamole as long as they are
authenticated by at least one extension, no extension denies/vetoes access, and
the database will record connection history entries for all connections
regardless of whether they are maintained by the database.

Note

In all cases, users will only be able to see or interact with resources that
they have been given permission to access. This is true whether those
permissions are granted explicitly or through inheritance (from user groups).

Native Webapp (Tomcat)

`mysql-user-required`
:   Whether a user account within the database is required for authentication to
    succeed, even if the user has been authenticated via another extension. By
    default, successful authentication via any extension is sufficient, and
    database user accounts are not strictly required.

`mysql-auto-create-accounts`
:   Whether to automatically create user accounts in the database for users who
    have successfully authenticate through another extension. Users that are
    automatically created are granted `READ` permission on their own user account
    and no other explicit permissions. By default users will not be automatically
    created.

`mysql-track-external-connection-history`
:   Whether connection history records should be created for connections not
    defined in the database. By default, external connection history will be
    tracked unless this is explicitly disabled by setting this to “false”.

Container (Docker)

`MYSQL_USER_REQUIRED`
:   Whether a user account within the database is required for authentication to
    succeed, even if the user has been authenticated via another extension. By
    default, successful authentication via any extension is sufficient, and
    database user accounts are not strictly required.

`MYSQL_AUTO_CREATE_ACCOUNTS`
:   Whether to automatically create user accounts in the database for users who
    have successfully authenticate through another extension. Users that are
    automatically created are granted `READ` permission on their own user account
    and no other explicit permissions. By default users will not be automatically
    created.

`MYSQL_TRACK_EXTERNAL_CONNECTION_HISTORY`
:   Whether connection history records should be created for connections not
    defined in the database. By default, external connection history will be
    tracked unless this is explicitly disabled by setting this to “false”.

### Access window enforcment[#](#access-window-enforcment "Link to this heading")

Guacamole supports the use of access windows to limit the time periods during
which users are allowed to access the system. By default, users will be
forcibly logged out from Guacamole as soon as the access window expires,
disconnecting them from any active connections.

If you would prefer users to be allowed to remain logged in, this behavior can
be overridden using the configuration option below.

Note

Prior to [Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0),
access windows were enforced only during the login process. Access windows
restricted only when a user could log in, not whether they could remain logged
in.

Native Webapp (Tomcat)

`mysql-enforce-access-windows-for-active-sessions`
:   Whether time-based access windows should be enforced for active user sessions.
    By default, users will be logged out when an access window closes, even if
    they are currently logged in. To allow logged-in users to continue to use the
    application after an access window closes, set this to “false”. Users will
    always be prevented from logging in outside of access windows regardless of
    this setting.

Container (Docker)

`MYSQL_ENFORCE_ACCESS_WINDOWS_FOR_ACTIVE_SESSIONS`
:   Whether time-based access windows should be enforced for active user sessions.
    By default, users will be logged out when an access window closes, even if
    they are currently logged in. To allow logged-in users to continue to use the
    application after an access window closes, set this to “false”. Users will
    always be prevented from logging in outside of access windows regardless of
    this setting.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Logging in[#](#logging-in "Link to this heading")

The default Guacamole user created by the provided SQL scripts is
“`guacadmin`”, with a default password of “`guacadmin`”. Once you have verified
that the database authentication is working, **you should [change your password
immediately](using-guacamole.html#changing-password)**.

Once you have successfully logged in and changed your password, you can begin
using the web UI to create other users, groups, and connections. More detailed
instructions for doing this are given in [Guacamole’s administrative interface](administration.html).

Contents

---
# Installing Guacamole with Docker

## Contents

# Installing Guacamole with Docker[#](#installing-guacamole-with-docker "Link to this heading")

Guacamole can be deployed using Docker, removing the need to build
guacamole-server from source or configure the web application manually. The
Guacamole project provides officially-supported Docker images for both
Guacamole and guacd which are kept up-to-date with each release.

A typical Docker deployment of Guacamole will involve three separate
containers, connected over the network:

`guacamole/guacd`
:   Provides the guacd daemon, built from the released guacamole-server source
    with support for VNC, RDP, SSH, telnet, and Kubernetes.

`guacamole/guacamole`
:   Provides the Guacamole web application running within Tomcat 9.x with support
    for WebSocket. The configuration necessary to connect to guacd, MySQL,
    PostgreSQL, LDAP, etc. will be read automatically from environment variables
    when the image starts.

`mysql` or `postgresql`
:   Provides the database that Guacamole will use for authentication and storage
    of connection configuration data.

This separation is important, as it facilitates upgrades and maintains proper
separation of concerns. With the database separate from Guacamole and guacd,
those containers can be freely destroyed and recreated at will. The only
container which must persist data through upgrades is the database.

## Running the guacd Docker image[#](#running-the-guacd-docker-image "Link to this heading")

The guacd Docker image is built from the released guacamole-server source with
support for VNC, RDP, SSH, telnet, and Kubernetes. Common pitfalls like
installing the required dependencies, installing fonts for SSH, telnet, or
Kubernetes, and ensuring the FreeRDP plugins are installed to the correct
location are all taken care of. It will simply just work.

### Running guacd for use by the Guacamole Docker image[#](#running-guacd-for-use-by-the-guacamole-docker-image "Link to this heading")

When running the guacd image with the intent of connecting with a Guacamole
container, no ports need be exposed on the network. Access to these ports will
be handled automatically by Docker through the use of an isolated network:

```
$ docker run --network=some-network --name some-guacd -d guacamole/guacd
```

When run in this manner, guacd will be listening on its default port 4822, but
this port will only be available via the dedicated Docker network,
`some-network`.

The log level of guacd can be controlled with the `LOG_LEVEL` environment
variable. The default value is `info`, and can be set to any of the valid
settings for the guacd log flag (`-L`).

```
$ docker run --network=some-network --name some-guacd \
    -e LOG_LEVEL=debug -d guacamole/guacd
```

### Running guacd for use by services outside Docker[#](#running-guacd-for-use-by-services-outside-docker "Link to this heading")

If you are not going to use the Guacamole image, you can still leverage the
guacd image for ease of installation and maintenance. By exposing the guacd
port, 4822, services external to Docker will be able to access guacd.

Important

*Take great care when doing this* - guacd is a passive proxy and does not
perform any kind of authentication.

If you do not properly isolate guacd from untrusted parts of your network,
malicious users may be able to use guacd as a jumping point to other systems.

```
$ docker run --name some-guacd -d -p 4822:4822 guacamole/guacd
```

guacd will now be listening on port 4822, and Docker will expose this port on
the same server hosting Docker. Other services, such as an instance of Tomcat
running outside of Docker, will be able to connect to guacd directly.

## The Guacamole Docker image[#](#the-guacamole-docker-image "Link to this heading")

The Guacamole Docker image is built on top of a standard Tomcat 9.x image and
takes care of all configuration automatically. The configuration information
required for guacd and the various authentication mechanisms are specified with
environment variables given when the container is created.

Important

If using [PostgreSQL](postgresql-auth.html) or [MySQL](mysql-auth.html) for
authentication, *you will need to initialize the database manually*. Guacamole
will not automatically create its own tables, but SQL scripts are provided to
do this.

Once the Guacamole image is running, Guacamole will be accessible at
`http://HOSTNAME:8080/guacamole/`, where `HOSTNAME` is the hostname or
address of the machine hosting Docker. To set the path Guacamole is accessible from,
use the `WEBAPP_CONTEXT` environment variable:

`WEBAPP_CONTEXT`
:   The path Guacamole should be accessible from. If set to `ROOT` Guacamole
    will accessible from `http://HOSTNAME:8080`.

### Configuring Guacamole when using Docker[#](#configuring-guacamole-when-using-docker "Link to this heading")

When running Guacamole using Docker, the traditional approach to configuring
Guacamole by editing `guacamole.properties` is instead primarily accomplished
using environment variables. For each property that the web application or an
extension might read, the value of that property is read from a corresponding
environment variable.

Each of these environment variables are explicitly documented alongside their
original properties, but they are named consistently by transforming the
property into uppercase and replacing all dashes with underscores.

Hint

This means that even custom, third-party extensions that leverage properties
from `guacamole.properties` are automatically configurable using environment
variables within the `guacamole/guacamole` image.

### Connecting Guacamole to guacd[#](#connecting-guacamole-to-guacd "Link to this heading")

The Guacamole Docker image needs to be able to connect to guacd to establish
remote desktop connections, just like any other Guacamole deployment, however
the connection information needed by Guacamole will be provided via environment
variables.

If you will be using Docker to provide guacd, and you wish to use a dedicated
network for these services, you can just use the container name as the
hostname:

```
$ docker run --network=some-network --name some-guacamole \
    -e GUACD_HOSTNAME=some-guacamole -d -p 8080:8080 guacamole/guacamole
```

The network connection information for guacd is provided using additional
environment variables:

`GUACD_HOSTNAME`
:   The hostname of the guacd instance to use to establish remote desktop
    connections. *This is required if you are not using Docker to provide guacd.*

`GUACD_PORT`
:   The port that Guacamole should use when connecting to guacd. This environment
    variable is optional. If not provided, the standard guacd port of 4822 will
    be used.

*A connection to guacd is not the only thing required for Guacamole to work*;
some authentication mechanism needs to be configured, as well.
[MySQL](mysql-auth.html), [PostgreSQL](postgresql-auth.html), and [LDAP](ldap-auth.html) are
supported for this, and are described in more detail in the sections below. If
the required configuration options for at least one authentication mechanism
are not provided, the Guacamole image will not be able to start up, and you
will see an error.

### Running Guacamole behind a proxy[#](#running-guacamole-behind-a-proxy "Link to this heading")

To run Guacamole behind a reverse proxy, Tomcat’s
[`RemoteIpValve`](https://tomcat.apache.org/tomcat-9.0-doc/config/valve.html#Remote_IP_Valve)
must be configured as described in [Setting up the Remote IP Valve](reverse-proxy.html#tomcat-remote-ip) to ensure that the
user’s IP address can be correctly determined and logged. The Guacamole Docker
image provides environment variables for configuring this.

#### Required environment variables[#](#required-environment-variables "Link to this heading")

The following environment variable must be set in order to configure Tomcat’s
[`RemoteIpValve`](https://tomcat.apache.org/tomcat-9.0-doc/config/valve.html#Remote_IP_Valve):

`REMOTE_IP_VALVE_ENABLED`
:   Set to `true` to enable Tomcat’s [`RemoteIpValve`](https://tomcat.apache.org/tomcat-9.0-doc/config/valve.html#Remote_IP_Valve).
    **If this is not set, all other variables related to `RemoteIpValve` will be
    ignored.**

#### Optional environment variables[#](#optional-environment-variables "Link to this heading")

Additional environment variables are available to fine tune the configuration
of `RemoteIpValve`. **It is not typically necessary to set these variables.**
The default values are correct for most deployments.

`PROXY_ALLOWED_IPS_REGEX`
:   A regular expression matching only the IP addresses that should be trusted to
    send proxy headers, corresponding to the `internalProxies` attribute of
    `RemoteIpValve`. Proxy headers from other addresses will be ignored. The
    regular expression must conform to the format accepted by [Java’s `Pattern`
    class](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html),
    which is largely compatible with Perl.

    If omitted, Tomcat’s default which matches private IPv4 and IPv6 addresses
    will be used.

`PROXY_BY_HEADER`
:   The HTTP header sent by the proxy that contains the list of proxies that have
    processed the request. This corresponds to the `proxiesHeader` attribute of
    `RemoteIpValve`. By default, this will be `X-Forwarded-By`.

`PROXY_IP_HEADER`
:   The HTTP header sent by the proxy that contains the user’s browser’s IP
    address. This corresponds to the `remoteIpHeader` attribute of
    `RemoteIpValve`. By default, this will be `X-Forwarded-For`.

`PROXY_PROTOCOL_HEADER`
:   The HTTP header sent by the proxy that contains the protocol used by the
    user’s browser to connect to the proxy. This corresponds to the
    `protocolHeader` attribute of `RemoteIpValve`. By default, this will be
    `X-Forwarded-Proto`.

### Custom extensions and `GUACAMOLE_HOME`[#](#custom-extensions-and-guacamole-home "Link to this heading")

If you have your own or third-party extensions for Guacamole which are not
supported by the Guacamole Docker image, but are compatible with the version of
Guacamole within the image, you can still use them exactly as you would with a
native Guacamole installation. The Guacamole web application within the image
uses the same standard configuration paths and files.

Additionally, the `guacamole/guacamole` image provides some configuration
mechanisms for convenience:

* Configuration properties that are normally consumed by your extension via
  `guacamole.properties` can instead be specified with corresponding
  environment variables. Within the Docker image, the Guacamole web application
  will automatically read properties from environment variables that are named
  by transforming the property name into uppercase and replacing all dashes
  with underscores.
* The `GUACAMOLE_HOME` environment variable informs the image where to look for
  your configuration and defaults to `/etc/guacamole`. If you need to use a
  different location, you can simply point this variable at that location
  instead.

The image is designed to use any provided `GUACAMOLE_HOME` configuration as a
template while leaving its contents untouched. The web application will be
pointed at a temporary location whose contents have been non-destructively
copied/linked from the files you have provided. **The image does not need write
access to any custom configuration files/directories.**

### Verifying the Guacamole install[#](#verifying-the-guacamole-install "Link to this heading")

Once the Guacamole image is running, Guacamole should be accessible at
`http://HOSTNAME:8080/guacamole/` (or the path you set with
`WEBAPP_CONTEXT`), where `HOSTNAME` is the hostname or address of the machine
hosting Docker, and you *should* see a login screen.

If you cannot access Guacamole, or you do not see a login screen, check
Docker’s logs using the `docker logs` command to determine if something is
wrong. Configuration parameters may have been given incorrectly, or the
database may be improperly initialized:

```
$ docker logs some-guacamole
```

Contents

---
# Signing in with smart cards or certificates

## Contents

# Signing in with smart cards or certificates[#](#signing-in-with-smart-cards-or-certificates "Link to this heading")

Single sign-on using SSL client authentication depends on having a reverse
proxy configured to provide SSL termination for Guacamole. Unlike a standard
reverse proxy setup, however, a portion of the requests served through the
proxy will verify the client’s identity using SSL client authentication and
pass that information on to Guacamole.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## How SSL client authentication works with Guacamole[#](#how-ssl-client-authentication-works-with-guacamole "Link to this heading")

Using SSL client authentication for Guacamole involves configuring a reverse
proxy to provide SSL termination for the same instance of Guacamole at two
different domains or subdomains:

1. **A wildcard subdomain and certificate** that will be used strictly for
   performing SSL client authentication. The wildcard certificate is necessary
   to allow Guacamole to generate temporary subdomains and avoid browser
   caching of credentials.
2. **A normal domain/subdomain (and corresponding certificate)** that will be
   used for Guacamole itself and will not use SSL client authentication.

When Guacamole is configured for single sign-on using SSL client
authentication, users are presented with an additional “Certificate / Smart
Card” option at the bottom of the login screen:

![The Guacamole login screen, showing the "Certificate / Smart Card" prompt added by the SSL client authentication extension.](assets/doc_gug__images_ssl-sso-001-link.png)

If a user clicks on “Certificate / Smart Card”, Guacamole generates a temporary
subdomain to handle authentication and redirects the user to that subdomain. As
the SSL termination is configured to handle these subdomains with SSL client
authentication, the user is authenticated by the reverse proxy using that
mechanism:

![The browser prompt resulting from starting the SSL client authentication process by clicking the "Certificate / Smart Card" link, displayed in front of the Guacamole login screen.](assets/doc_gug__images_ssl-sso-002-browser-prompt.png)

The reverse proxy notifies Guacamole of the result of authentication using the
`X-Client-Verified` and `X-Client-Certificate` headers. Once the user is
authenticated (or fails to authenticate), Guacamole redirects the user back to
the primary domain and their SSL authentication result is read.

If the user successfully authenticated, their username is determined from the
certificate:

![The Guacamole home screen after successfully signing in using a smart card.](assets/doc_gug__images_ssl-sso-003-success.png)

If the user *did not* successfully authenticate, authentication with Guacamole
fails and the user sees the login screen again.

## Configuring SSL termination to use client authentication[#](#configuring-ssl-termination-to-use-client-authentication "Link to this heading")

There are two separate configurations that will need to be applied to your
reverse proxy, one for each of the domains noted above. In each case, the proxy
will need to add headers that will be consumed by Guacamole’s SSL
authentication integration.

Hint

The `*.auth.guac.example.net` and `guac.example.net` domains are used
throughout this documentation as representative placeholders. Your
configuration will differ depending on the domain your users are using to
access your instance of Guacamole.

Both the wildcard domain and normal domain that will be configured here will
need to be referenced in Guacamole’s configuration. Take note of these domains,
so that you can provide their values when configuring Guacamole later.

### Wildcard domain (performs SSL client authentication)[#](#wildcard-domain-performs-ssl-client-authentication "Link to this heading")

Since it is the wildcard domain that will actually perform SSL client
authentication (Guacamole receives the authentication result from your reverse
proxy via HTTP headers), the configuration for the wildcard domain requires
several additional changes from [the standard reverse proxy configuration for
Guacamole](reverse-proxy.html):

Enable SSL client authentication in “optional” mode
:   This will result in the reverse proxy requesting authentication, but will
    not prohibit the authentication result from being sent on to Guacamole if
    authentication fails.

Pass through the `Host` header received by the reverse proxy
:   It is the `Host` header that determines whether the request is routed to the
    reverse proxy’s handling of wildcard domain vs. normal domain, and Guacamole
    needs this information, as well, to determine context.

Include the authentication result as the value of the `X-Client-Verified` header.
:   This header must contain the value `SUCCESS` if authentication succeeded and
    may contain any other value otherwise. If authentication failed, this header
    may contain `FAILED:` followed by a human-readable description of the
    failure, and Guacamole will include that description in its logs.

    Both the Apache HTTP Server and Nginx support this format for passing on the
    result of SSL client authentication.

Include the URL-encoded client certificate in PEM format as the value `X-Client-Certificate` header.
:   Here, URL encoding is necessary to allow the certificate to be included as
    the value of an HTTP header. Both the Apache HTTP Server and Nginx support
    URL encoding of this value.

*The portions of the reverse proxy configuration which differ from [the
standard configuration](reverse-proxy.html) are highlighted below.* Your reverse
proxy configuration will need to be similarly modified to allow Guacamole to
receive and process the authentication result.

Apache HTTP Server

```
<VirtualHost *:443>

    ServerName x.auth.guac.example.net
    ServerAlias *.auth.guac.example.net

    SSLEngine on
    SSLCertificateFile "/etc/ssl/certs/_.auth.guac.example.net.crt"
    SSLCertificateKeyFile "/etc/ssl/private/_.auth.guac.example.net.key"

    SSLCACertificateFile "/etc/ssl/certs/client-auth-ca-certs.crt"
    SSLVerifyClient optional
    SSLVerifyDepth 2

    <Location /guacamole/>

        Order allow,deny
        Allow from all
        ProxyPass http://localhost:8080/guacamole/ flushpackets=on
        ProxyPassReverse http://localhost:8080/guacamole/

        ProxyPreserveHost on
        RequestHeader set X-Client-Certificate "expr=%{escape:%{SSL_CLIENT_CERT}}"
        RequestHeader set X-Client-Verified "%{SSL_CLIENT_VERIFY}s"

    </Location>

</VirtualHost>
```

Hint

The [typical `<Location /guacamole/websocket-tunnel>`
section](reverse-proxy.html#websocket-and-apache) is intentionally omitted above. This is because
SSL client authentication will be performed only via a specific, dedicated
endpoint that does not involve any tunnel, let alone the WebSocket tunnel.

Including a `<Location>` section for the `websocket-tunnel` endpoint beneath
the wildcard domain will not prevent smart card / certificate authentication
from working, but it is unnecessary for the wildcard domain.

Nginx

```
server {

    listen 443 ssl;
    server_name _.auth.guac.example.net;

    ssl_certificate /etc/ssl/certs/_.auth.guac.example.net.crt;
    ssl_certificate_key /etc/ssl/private/_.auth.guac.example.net.key;

    ssl_client_certificate /etc/ssl/certs/client-auth-ca-certs.crt;
    ssl_verify_client optional;

    location /guacamole/ {

        proxy_pass http://localhost:8080;
        proxy_buffering off;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $http_connection;
        access_log off;

        proxy_set_header Host $http_host;
        proxy_set_header X-Client-Verified $ssl_client_verify;
        proxy_set_header X-Client-Certificate $ssl_client_escaped_cert;

    }

}
```

### Normal domain (does not perform SSL client authentication)[#](#normal-domain-does-not-perform-ssl-client-authentication "Link to this heading")

Configuration of the non-wildcard, normal domain is simpler than its wildcard
counterpart, but still requires at least pass-through of the `Host` header
received by the reverse proxy. As with the wildcard domain, this is necessary
for Guacamole to determine the context of the request it received.

Apache HTTP Server

```
<VirtualHost *:443>

    ServerName guac.example.net

    SSLEngine on
    SSLCertificateFile "/etc/ssl/certs/guac.example.net.crt"
    SSLCertificateKeyFile "/etc/ssl/private/guac.example.net.key"

    <Location /guacamole/>
        Order allow,deny
        Allow from all
        ProxyPass http://localhost:8080/guacamole/ flushpackets=on
        ProxyPassReverse http://localhost:8080/guacamole/
        ProxyPreserveHost on
    </Location>

    <Location /guacamole/websocket-tunnel>
        Order allow,deny
        Allow from all
        ProxyPass ws://localhost:8080/guacamole/websocket-tunnel
        ProxyPassReverse ws://localhost:8080/guacamole/websocket-tunnel
    </Location>

</VirtualHost>
```

Nginx

```
server {

    listen 443 ssl;
    server_name guac.example.net;

    ssl_certificate /etc/ssl/certs/guac.example.net.crt;
    ssl_certificate_key /etc/ssl/private/guac.example.net.key;

    location /guacamole/ {
        proxy_pass http://localhost:8080;
        proxy_buffering off;
        proxy_http_version 1.1;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $http_connection;
        access_log off;
    }

}
```

With both the wildcard and normal domains configured, your reverse proxy should
be ready to handle SSL client authentication and pass on the results of any
authentication attempts to Guacamole in the format expected.

## Installing/Enabling the SSL client authentication extension[#](#installing-enabling-the-ssl-client-authentication-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-sso-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-sso-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `ssl/guacamole-auth-sso-ssl-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `SSL_AUTH_ENABLED` environment variable:

    ```
    SSL_AUTH_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e SSL_AUTH_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `SSL_AUTH_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `SSL_AUTH_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Required configuration[#](#required-configuration "Link to this heading")

Native Webapp (Tomcat)

Guacamole’s SSL client authentication support requires two properties which describe the domains that your reverse proxy has been configured to
use for authentication and for simply accessing Guacamole. These properties
are *absolutely required in all cases*:

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
ssl-auth-uri: https://*.auth.guac.example.net
ssl-auth-primary-uri: https://guac.example.net
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`ssl-auth-uri`
:   The URI that should be used to authenticate users with SSL/TLS client
    authentication. This must be a URI that points to THIS instance of Guacamole,
    but behind SSL termination that requires SSL/TLS client authentication.

`ssl-auth-primary-uri`
:   The URI of this instance without SSL/TLS client authentication required. This
    must be a URI that points to THIS instance of Guacamole, but behind SSL
    termination that DOES NOT require or request SSL/TLS client authentication.

Container (Docker)

Guacamole’s SSL client authentication support requires two environment variables which describe the domains that your reverse proxy has been configured to
use for authentication and for simply accessing Guacamole. These environment variables
are *absolutely required in all cases*:

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
SSL_AUTH_URI: 'https://*.auth.guac.example.net'
SSL_AUTH_PRIMARY_URI: 'https://guac.example.net'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e SSL_AUTH_URI="https://*.auth.guac.example.net" \
    -e SSL_AUTH_PRIMARY_URI="https://guac.example.net" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`SSL_AUTH_URI`
:   The URI that should be used to authenticate users with SSL/TLS client
    authentication. This must be a URI that points to THIS instance of Guacamole,
    but behind SSL termination that requires SSL/TLS client authentication.

`SSL_AUTH_PRIMARY_URI`
:   The URI of this instance without SSL/TLS client authentication required. This
    must be a URI that points to THIS instance of Guacamole, but behind SSL
    termination that DOES NOT require or request SSL/TLS client authentication.

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Native Webapp (Tomcat)

Additional optional properties are available to control how the
requests received from your reverse proxy are processed, including narrowing
the distinguished names (DNs) that should be accepted as valid:

`ssl-auth-client-certificate-header`
:   The name of the header to use to retrieve the URL-encoded client certificate
    from an HTTP request received from an SSL termination service providing
    SSL/TLS client authentication. The certificate must be in PEM format.

    By default, the `X-Client-Certificate` header will be used.

`ssl-auth-client-verified-header`
:   The name of the header to use to retrieve the verification status of the
    certificate an HTTP request received from an SSL termination service
    providing SSL/TLS client authentication.

    The value of this header must be “SUCCESS” (all uppercase) if the certificate
    was successfully verified. The full set of accepted values that your reverse
    proxy should submit for this header is:

    `SUCCESS`
    :   Client certificate verification succeeded.

    `FAILED: reason`
    :   Client certificate verification failed for the given reason (a
        human-readable description).

    `NONE`
    :   No client certificate was present.

    This matches the values used by both the Apache HTTP Server and Nginx. Any
    value not shown above is interpreted as an authentication failure.

    By default, the `X-Client-Verified` header will be used.

`ssl-auth-max-token-validity`
:   The amount of time that a temporary authentication token for SSL/TLS
    authentication may remain valid, in minutes.

    This token is used to represent the user’s asserted identity after it has
    been verified by the SSL termination service. This interval must be long
    enough to allow for network delays in receiving the token, but short enough
    that unused tokens do not consume unnecessary server resources and cannot
    potentially be guessed while the token is still valid. These tokens are
    256-bit secure random values.

    By default, tokens are valid for 5 minutes.

`ssl-auth-subject-username-attribute`
:   The LDAP attribute or attributes that may be used to represent a username
    within the subject DN of a user’s X.509 certificate. If the least-significant
    attribute of the subject DN is not one of these attributes, the certificate
    will be rejected.

    By default, any attribute is accepted (the least-significant attribute of the
    subject DN is used as the username, regardless of what attribute that may
    be).

`ssl-auth-subject-base-dn`
:   The base DN containing all valid subject DNs. If specified, only certificates
    asserting subject DNs beneath this base DN will be accepted.

    By default, all DNs are accepted.

`ssl-auth-max-domain-validity`
:   The amount of time that the temporary, unique subdomain generated for SSL/TLS
    authentication may remain valid, in minutes. This subdomain is used to ensure
    each SSL/TLS authentication attempt is fresh and does not potentially reuse a
    previous authentication attempt that was cached by the browser or OS. This
    interval must be long enough to allow for network delays in authenticating
    the user with the SSL termination service that enforces SSL/TLS client
    authentication, but short enough that an unused domain does not consume
    unnecessary server resources and cannot potentially be guessed while that
    subdomain is still valid. These subdomains are 128-bit secure random values.

    By default, generated domains are valid for 5 minutes.

Container (Docker)

Additional optional environment variables are available to control how the
requests received from your reverse proxy are processed, including narrowing
the distinguished names (DNs) that should be accepted as valid:

`SSL_AUTH_CLIENT_CERTIFICATE_HEADER`
:   The name of the header to use to retrieve the URL-encoded client certificate
    from an HTTP request received from an SSL termination service providing
    SSL/TLS client authentication. The certificate must be in PEM format.

    By default, the `X-Client-Certificate` header will be used.

`SSL_AUTH_CLIENT_VERIFIED_HEADER`
:   The name of the header to use to retrieve the verification status of the
    certificate an HTTP request received from an SSL termination service
    providing SSL/TLS client authentication.

    The value of this header must be “SUCCESS” (all uppercase) if the certificate
    was successfully verified. The full set of accepted values that your reverse
    proxy should submit for this header is:

    `SUCCESS`
    :   Client certificate verification succeeded.

    `FAILED: reason`
    :   Client certificate verification failed for the given reason (a
        human-readable description).

    `NONE`
    :   No client certificate was present.

    This matches the values used by both the Apache HTTP Server and Nginx. Any
    value not shown above is interpreted as an authentication failure.

    By default, the `X-Client-Verified` header will be used.

`SSL_AUTH_MAX_TOKEN_VALIDITY`
:   The amount of time that a temporary authentication token for SSL/TLS
    authentication may remain valid, in minutes.

    This token is used to represent the user’s asserted identity after it has
    been verified by the SSL termination service. This interval must be long
    enough to allow for network delays in receiving the token, but short enough
    that unused tokens do not consume unnecessary server resources and cannot
    potentially be guessed while the token is still valid. These tokens are
    256-bit secure random values.

    By default, tokens are valid for 5 minutes.

`SSL_AUTH_SUBJECT_USERNAME_ATTRIBUTE`
:   The LDAP attribute or attributes that may be used to represent a username
    within the subject DN of a user’s X.509 certificate. If the least-significant
    attribute of the subject DN is not one of these attributes, the certificate
    will be rejected.

    By default, any attribute is accepted (the least-significant attribute of the
    subject DN is used as the username, regardless of what attribute that may
    be).

`SSL_AUTH_SUBJECT_BASE_DN`
:   The base DN containing all valid subject DNs. If specified, only certificates
    asserting subject DNs beneath this base DN will be accepted.

    By default, all DNs are accepted.

`SSL_AUTH_MAX_DOMAIN_VALIDITY`
:   The amount of time that the temporary, unique subdomain generated for SSL/TLS
    authentication may remain valid, in minutes. This subdomain is used to ensure
    each SSL/TLS authentication attempt is fresh and does not potentially reuse a
    previous authentication attempt that was cached by the browser or OS. This
    interval must be long enough to allow for network delays in authenticating
    the user with the SSL termination service that enforces SSL/TLS client
    authentication, but short enough that an unused domain does not consume
    unnecessary server resources and cannot potentially be guessed while that
    subdomain is still valid. These subdomains are 128-bit secure random values.

    By default, generated domains are valid for 5 minutes.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# Securing a Guacamole install

# Securing a Guacamole install[#](#securing-a-guacamole-install "Link to this heading")

Secure deployment of Guacamole requires that all communication between users
and Guacamole are encrypted using SSL/TLS. We generally recommend using a
reverse proxy like Apache HTTPD or Nginx and configuring that proxy to provide
SSL termination:

[Using a reverse proxy for SSL termination](reverse-proxy.html)
:   SSL termination provides proper encryption in front of Guacamole without
    tying the configuration of SSL to the servlet container (Tomcat). This
    provides greater flexibility while reducing the overhead that otherwise might
    be imposed by implementing SSL within Java.

It is also highly recommended that you deploy some mechanism for brute-force
attack prevention. This ensures that malicious users that repeatedly try to
guess passwords will be automatically blocked:

[Securing Guacamole against brute-force attacks](auth-ban.html)
:   Guacamole provides an extension that automatically recognizes repeated
    authentication failures and blocks further attempts from the same IP address.

    This is enabled by default in the `guacamole/guacamole` Docker image.

The third-party open source project, [fail2ban](https://github.com/fail2ban/fail2ban),
is also an excellent option for blocking brute-force authentication attempts,
and has the benefit of performing its blocking at the firewall level.

---
# Using SAML for single sign-on

## Contents

# Using SAML for single sign-on[#](#using-saml-for-single-sign-on "Link to this heading")

SAML is a widely implemented and used Single Sign On (SSO) provider that allows
applications and services to authenticate in a standard way, and brokers those
authentication requests to one or more back-end authentication providers. The
SAML authentication extension allows Guacamole to redirect to a SAML Identity
Provider (IdP) for authentication and user services. This module does not
provide any capability for storing or retrieving connections, and must be
layered with other authentication extensions that provide connection
management.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling the SAML authentication extension[#](#installing-enabling-the-saml-authentication-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-sso-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-sso-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `saml/guacamole-auth-sso-saml-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `SAML_ENABLED` environment variable:

    ```
    SAML_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e SAML_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `SAML_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `SAML_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Configuration[#](#configuration "Link to this heading")

Native Webapp (Tomcat)

The SAML authentication extension provides several configuration properties to
set it up to talk to the IdP. The SAML IdP also must be configured with
Guacamole as a Service Provider (SP). Configuration of the SAML IdP is beyond
the scope of this document, and will vary widely based on the IdP in use.

`saml-idp-metadata-url`
:   The URI of the XML metadata file from the SAML Identity Provider that
    contains all of the information the SAML extension needs in order to know how
    to authenticate with the IdP. This URI can either be a remote server (e.g.
    `https://`) or a local file on the filesystem (e.g. `file://`). Often the
    metadata file contains most of the required properties for SAML
    authentication and the other parameters are not required.

`saml-idp-url`
:   The base URL of the SAML IdP. This is the URL that the SAML authentication
    extension will use to redirect when requesting SAML authentication. If the
    `saml-idp-metadata-url` property is provided, this parameter will be ignored.
    If the metadata file is not provided this property is required.

`saml-entity-id`
:   The entity ID of the Guacamole SAML client, which is generally the URL of the
    Guacamole server, but is not required to be so. This property is required if
    either the `saml-idp-metadata-url` property is not specified, or if the
    provided metadata file does not contain the SAML SP Entity ID for the
    Guacamole Client.

`saml-callback-url`
:   The URL that the IdP will use once authentication has succeeded to return to
    the Guacamole web application and provide the authentication details to the
    SAML extension. The SAML extension currently only supports callback as a POST
    operation to this callback URL. This property is required.

`saml-strict`
:   Require strict security checks during SAML logins. This will insure that
    valid certificates are present for all interactions with SAML servers and
    fail SAML authentication if security restrictions are violated. This property
    is optional, and will default to true, requiring strict security checks. This
    property should only be set to false in non-production environments during
    testing of SAML authentication.

`saml-debug`
:   Enable additional logging within the supporting SAML library that can assist
    in tracking down issues during SAML logins. This property is optional, and
    will default to false (no debugging).

`saml-compress-request`
:   Enable compression of the HTTP requests sent to the SAML IdP. This property
    is optional and will default to true (compression enabled).

`saml-compress-response`
:   Request that the SAML response returned by the IdP be compressed. This
    property is optional and will default to true (compression will be
    requested).

`saml-group-attribute`
:   The name of the attribute provided by the SAML IdP that contains group
    membership of the user. These groups will be parsed and used to map group
    membership of the user logging in, which can be used for permissions
    management within Guacamole Client, particularly when layered with other
    authentication modules. This property is optional, and defaults to “groups”.

`saml-x509-cert-path`
:   The path to a certificate that will be used to sign SAML requests before
    they are sent to the IdP, enhancing the integrity of the SAML authentication
    process. This property is optional, and, if not present, SAML requests
    will not be signed.

`saml-private-key-path`
:   The path to a private key file to use to encrypt SAML requests sent to the
    IdP, enhancing the confidentiality and integrity of the authentication
    process. This property is optional, and, if not present, SAML requests
    will not be encrypted before they are sent to the IdP.

Container (Docker)

The SAML authentication extension provides several configuration properties to
set it up to talk to the IdP. The SAML IdP also must be configured with
Guacamole as a Service Provider (SP). Configuration of the SAML IdP is beyond
the scope of this document, and will vary widely based on the IdP in use.

`SAML_IDP_METADATA_URL`
:   The URI of the XML metadata file from the SAML Identity Provider that
    contains all of the information the SAML extension needs in order to know how
    to authenticate with the IdP. This URI can either be a remote server (e.g.
    `https://`) or a local file on the filesystem (e.g. `file://`). Often the
    metadata file contains most of the required properties for SAML
    authentication and the other parameters are not required.

`SAML_IDP_URL`
:   The base URL of the SAML IdP. This is the URL that the SAML authentication
    extension will use to redirect when requesting SAML authentication. If the
    `saml-idp-metadata-url` property is provided, this parameter will be ignored.
    If the metadata file is not provided this property is required.

`SAML_ENTITY_ID`
:   The entity ID of the Guacamole SAML client, which is generally the URL of the
    Guacamole server, but is not required to be so. This property is required if
    either the `saml-idp-metadata-url` property is not specified, or if the
    provided metadata file does not contain the SAML SP Entity ID for the
    Guacamole Client.

`SAML_CALLBACK_URL`
:   The URL that the IdP will use once authentication has succeeded to return to
    the Guacamole web application and provide the authentication details to the
    SAML extension. The SAML extension currently only supports callback as a POST
    operation to this callback URL. This property is required.

`SAML_STRICT`
:   Require strict security checks during SAML logins. This will insure that
    valid certificates are present for all interactions with SAML servers and
    fail SAML authentication if security restrictions are violated. This property
    is optional, and will default to true, requiring strict security checks. This
    property should only be set to false in non-production environments during
    testing of SAML authentication.

`SAML_DEBUG`
:   Enable additional logging within the supporting SAML library that can assist
    in tracking down issues during SAML logins. This property is optional, and
    will default to false (no debugging).

`SAML_COMPRESS_REQUEST`
:   Enable compression of the HTTP requests sent to the SAML IdP. This property
    is optional and will default to true (compression enabled).

`SAML_COMPRESS_RESPONSE`
:   Request that the SAML response returned by the IdP be compressed. This
    property is optional and will default to true (compression will be
    requested).

`SAML_GROUP_ATTRIBUTE`
:   The name of the attribute provided by the SAML IdP that contains group
    membership of the user. These groups will be parsed and used to map group
    membership of the user logging in, which can be used for permissions
    management within Guacamole Client, particularly when layered with other
    authentication modules. This property is optional, and defaults to “groups”.

`SAML_X509_CERT_PATH`
:   The path to a certificate that will be used to sign SAML requests before
    they are sent to the IdP, enhancing the integrity of the SAML authentication
    process. This property is optional, and, if not present, SAML requests
    will not be signed.

`SAML_PRIVATE_KEY_PATH`
:   The path to a private key file to use to encrypt SAML requests sent to the
    IdP, enhancing the confidentiality and integrity of the authentication
    process. This property is optional, and, if not present, SAML requests
    will not be encrypted before they are sent to the IdP.

### Controlling login behavior[#](#controlling-login-behavior "Link to this heading")

Guacamole loads authentication extensions in order of priority, and evaluates
authentication attempts in this same order. This has implications for how the
Guacamole login process behaves when an SSO extension is present:

If the SSO extension has priority:
:   Users that are not yet authenticated
    will be immediately redirected to the configured identity provider. They will
    not see a Guacamole login screen.

If a non-SSO extension has priority:
:   Users that are not yet authenticated
    will be presented with a Guacamole login screen. Additionally, links to the
    configured identity provider(s) will be available for users that wish to log
    in using SSO.

The default priority of extensions is dictated by their filenames, with
extensions that sort earlier alphabetically having higher priority than others.
This can be overridden by [explicitly setting the extension
priority](configuring-guacamole.html#initial-setup).

#### Automatically redirecting all unauthenticated users[#](#automatically-redirecting-all-unauthenticated-users "Link to this heading")

To ensure users are redirected to the SAML identity provider immediately
(without a Guacamole login screen), ensure the SAML extension has priority over
all others:

```
extension-priority: saml
```

#### Presenting unauthenticated users with a login screen[#](#presenting-unauthenticated-users-with-a-login-screen "Link to this heading")

To ensure users are given a normal Guacamole login screen and have the option
to log in with traditional credentials *or* with SAML, ensure the SAML
extension does not have priority:

```
extension-priority: *, saml
```

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# Installing Guacamole natively

## Contents

# Installing Guacamole natively[#](#installing-guacamole-natively "Link to this heading")

Guacamole is separated into two pieces: guacamole-server, which provides the
guacd proxy and related libraries, and guacamole-client, which provides the
client to be served by your servlet container, usually [Apache
Tomcat](http://tomcat.apache.org/).

guacamole-client is available in binary form, but guacamole-server must be
built from source. Don’t be discouraged: building the components of Guacamole
from source is *not* as difficult as it sounds, and the build process is
automated. You just need to be sure you have the necessary tools installed
ahead of time. With the necessary dependencies in place, building Guacamole
only takes a few minutes.

## Building guacamole-server[#](#building-guacamole-server "Link to this heading")

guacamole-server contains all the native, server-side components required by
Guacamole to connect to remote desktops. It provides a common C library,
libguac, which all other native components depend on, as well as separate
libraries for each supported protocol, and guacd, the heart of Guacamole.

guacd is the proxy daemon that runs on your Guacamole server, accepts users’
connections that are tunneled through the Guacamole web application, and then
connects to remote desktops on their behalf. Building guacd creates an
executable called **guacd** which can be run manually or, if you wish,
automatically when your computer starts up.

To build guacamole-server, you will need a C compiler (such as gcc) and the
libraries that guacamole-server depends on. Some dependencies are absolutely
required, while others are optional. The presence of optional dependencies
enables additional features.

Important

Many Linux distributions separate library packages into binary and
“development” packages; *you will need to install the development packages*.
These will usually end in a “-dev” or “-devel” suffix.

### Required dependencies[#](#required-dependencies "Link to this heading")

In order to build guacamole-server, you will need Cairo, libjpeg (or
libjpeg-turbo), libpng, and libuuid (or the OSSP UUID library). These libraries
are strictly required *in all cases* - Guacamole cannot be built without them.

[Cairo](http://cairographics.org/)
:   Cairo is used by libguac for graphics rendering. Guacamole cannot function
    without Cairo installed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libcairo2-dev` |
    | Fedora / CentOS / RHEL package | `cairo-devel` |

[libjpeg-turbo](http://libjpeg-turbo.virtualgl.org/)
:   libjpeg-turbo is used by libguac to provide JPEG support. Guacamole will not
    build without this library present:

    |  |  |
    | --- | --- |
    | Debian package | `libjpeg62-turbo-dev` |
    | Ubuntu package | `libjpeg-turbo8-dev` |
    | Fedora / CentOS / RHEL package | `libjpeg-turbo-devel` |

    If libjpeg-turbo is unavailable on your platform, and you do not wish to
    build it from source, [libjpeg](http://www.ijg.org/) will work as well,
    though it will not be quite as fast:

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libjpeg62-dev` |
    | Fedora / CentOS / RHEL package | `libjpeg-devel` |

[libpng](http://www.libpng.org/pub/png/libpng.html)
:   libpng is used by libguac to write PNG images, the core image type used by
    the Guacamole protocol. Guacamole cannot function without libpng.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libpng-dev` |
    | Fedora / CentOS / RHEL package | `libpng-devel` |

    In some previous versions of Debian such as Debian 8 / Ubuntu 16.04, you need
    the `libpng12-dev` package.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libpng12-dev` |

[libtool](https://www.gnu.org/software/libtool/manual/libtool.html)
:   libtool is used during the build process. libtool creates compiled libraries
    needed for Guacamole.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libtool-bin` |
    | Fedora / CentOS / RHEL package | `libtool` |

libuuid (part of [util-linux](https://www.kernel.org/pub/linux/utils/util-linux/))
:   libuuid is used by libguac to assign unique, internal IDs to each Guacamole
    user and connection. These unique IDs are the basis for connection sharing
    support.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `uuid-dev` |
    | Fedora / CentOS / RHEL package | `libuuid-devel` |

    If libuuid is unavailable, the [OSSP UUID](http://www.ossp.org/pkg/lib/uuid/)
    library may also be used:

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libossp-uuid-dev` |
    | Fedora / CentOS / RHEL package | `uuid-devel` |

### Optional dependencies[#](#optional-dependencies "Link to this heading")

The optional dependencies of Guacamole dictate which parts of guacamole-server
will be built. This includes the support for various remote desktop protocols,
as well as any additional features of those protocols:

* VNC support depends on the libvncclient library, which is part of
  libVNCServer.
* RDP support depends on a recent version of FreeRDP (2.0.0 or higher, but
  please *not a non-release version from git*).
* SSH support depends on libssh2, OpenSSL and Pango (a font rendering and text
  layout library, used by Guacamole’s built-in terminal emulator).
* Telnet depends on libtelnet and Pango.
* Kubernetes support depends on libwebsockets, OpenSSL, and Pango.

The `guacenc` utility, provided by guacamole-server to translate screen
recordings into video, depends on FFmpeg, and will only be built if at least
the libavcodec, libavformat, libavutil, and libswscale libraries provided by
FFmpeg are installed.

Important

If you lack these dependencies, *then the features or protocols which
depend on them will not be enabled*. Please read this section
carefully before deciding not to install an optional dependency.

[FFmpeg](https://ffmpeg.org/)
:   The libavcodec, libavformat, libavutil, and libswscale libraries provided by
    FFmpeg are used by `guacenc` to encode video streams when translating
    recordings of Guacamole sessions. Without FFmpeg, the `guacenc` utility will
    simply not be built.

    If you do not wish to make graphical recordings of Guacamole sessions, or do
    not wish to translate such recordings into video, then FFmpeg is not needed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libavcodec-dev`, `libavformat-dev`, `libavutil-dev`, `libswscale-dev` |
    | Fedora / CentOS / RHEL package | `ffmpeg-devel` |

[FreeRDP](http://www.freerdp.com/)
:   FreeRDP 2.0.0 or later is required for RDP support. If you do not wish to
    build RDP support, this library is not needed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `freerdp2-dev` |
    | Fedora / CentOS / RHEL package | `freerdp-devel` |

[Pango](http://www.pango.org/)
:   Pango is a text layout library which Guacamole uses to render text for
    protocols that require a terminal (Kubernetes, SSH, and telnet). If you do
    not wish to build any terminal-based protocol support, this library is not
    needed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libpango1.0-dev` |
    | Fedora / CentOS / RHEL package | `pango-devel` |

[libssh2](http://www.libssh2.org/)
:   libssh2 is required for SSH and SFTP support. If you do not wish to build SSH
    or SFTP support, this library is not needed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libssh2-1-dev` |
    | Fedora / CentOS / RHEL package | `libssh2-devel` |

[libtelnet](https://github.com/seanmiddleditch/libtelnet)
:   libtelnet is required for telnet support. If you do not wish to build telnet
    support, this library is not needed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libtelnet-dev` |
    | Fedora / CentOS / RHEL package | `libtelnet-devel` |

[libVNCServer](http://libvnc.github.io/)
:   libVNCServer provides libvncclient, which is required for VNC support. If you
    do not wish to build VNC support, this library is not needed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libvncserver-dev` |
    | Fedora / CentOS / RHEL package | `libvncserver-devel` |

[libwebsockets](https://libwebsockets.org/)
:   libwebsockets is required for Kubernetes support. If you do not wish to build
    Kubernetes support, this library is not needed.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libwebsockets-dev` |
    | Fedora / CentOS / RHEL package | `libwebsockets-devel` |

[PulseAudio](http://www.freedesktop.org/wiki/Software/PulseAudio/)
:   PulseAudio provides libpulse, which is used by Guacamole’s VNC support to
    provide experimental audio support. If you are not going to be using the
    experimental audio support for VNC, you do not need this library.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libpulse-dev` |
    | Fedora / CentOS / RHEL package | `pulseaudio-libs-devel` |

[OpenSSL](https://www.openssl.org/)
:   OpenSSL provides support for SSL and TLS - two common encryption schemes that
    make up the majority of encrypted web traffic.

    If you have libssl installed, guacd will be built with SSL support, allowing
    communication between the web application and guacd to be encrypted. This
    library is also required for SSH support, for manipulating public/private keys,
    and for Kubernetes support, for SSL/TLS connections to the Kubernetes server.

    Without SSL support, there will be no option to encrypt communication to
    guacd, and support for SSH and Kubernetes cannot be built.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libssl-dev` |
    | Fedora / CentOS / RHEL package | `openssl-devel` |

[libvorbis](http://xiph.org/vorbis/)
:   libvorbis provides support for Ogg Vorbis - a free and open standard for
    sound compression. If installed, libguac will be built with support for Ogg
    Vorbis, and protocols supporting audio will use Ogg Vorbis compression when
    possible.

    Otherwise, sound will only be encoded as WAV (uncompressed), and will only be
    available if your browser also supports WAV.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libvorbis-dev` |
    | Fedora / CentOS / RHEL package | `libvorbis-devel` |

[libwebp](https://developers.google.com/speed/webp/)
:   libwebp is used by libguac to write WebP images. Though support for WebP is
    not mandated by the Guacamole protocol, WebP images will be used if supported
    by both the browser and by libguac.

    Lacking WebP support, Guacamole will simply use JPEG in cases that it would
    have preferred WebP.

    |  |  |
    | --- | --- |
    | Debian / Ubuntu package | `libwebp-dev` |
    | Fedora / CentOS / RHEL package | `libwebp-devel` |

### Obtaining the source code[#](#obtaining-the-source-code "Link to this heading")

You can obtain a copy of the guacamole-server source from the Guacamole project
web site. These releases are stable snapshots of the latest code which have
undergone enough testing that the Guacamole team considers them fit for public
consumption. Source downloaded from the project web site will take the form of
a `.tar.gz` archive which you can extract from the command line:

```
$ tar -xzf guacamole-server-1.6.0.tar.gz
$ cd guacamole-server-1.6.0/
$
```

If you want the absolute latest code, and don’t care that the code hasn’t been
as rigorously tested as the code in stable releases, you can also clone the
Guacamole team’s git repository on GitHub:

```
$ git clone git://github.com/apache/guacamole-server.git
Cloning into 'guacamole-server'...
remote: Counting objects: 6769, done.
remote: Compressing objects: 100% (2244/2244), done.
remote: Total 6769 (delta 3058), reused 6718 (delta 3008)
Receiving objects: 100% (6769/6769), 2.32 MiB | 777 KiB/s, done.
Resolving deltas: 100% (3058/3058), done.
$
```

### The build process[#](#the-build-process "Link to this heading")

Once the guacamole-server source has been downloaded and extracted, you need to
run `configure`. This is a shell script automatically generated by GNU
Autotools, a popular build system used by the Guacamole project for
guacamole-server. Running `configure` will determine which libraries are
available on your system and will select the appropriate components for
building depending on what you actually have installed.

Important

Source downloaded directly from git will not contain this `configure` script,
as autogenerated code is not included in the project’s repositories. If you
downloaded the code from the project’s git repositories directly, you will need
to generate `configure` manually:

```
$ cd guacamole-server/
$ autoreconf -fi
$
```

Doing this requires GNU Autotools to be installed.

Source archives downloaded from the project website contain the `configure`
script and all other necessary build files, and thus do not require GNU
Autotools to be installed on the build machine.

Once you run `configure`, you can see a listing of what libraries were found
and what it has determined should be built. Startup scripts and unit files are
provided for both traditional SysV init and systemd:

systemd

```
$ ./configure --with-systemd-dir=/usr/local/lib/systemd/system
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
...

------------------------------------------------
guacamole-server version 1.6.0
------------------------------------------------

   Library status:

     freerdp ............. yes (2.x)
     pango ............... yes
     libavcodec .......... yes
     libavformat ......... yes
     libavutil ........... yes
     libssh2 ............. yes
     libssl .............. yes
     libswscale .......... yes
     libtelnet ........... yes
     libVNCServer ........ yes
     libvorbis ........... yes
     libpulse ............ yes
     libwebsockets ....... yes
     libwebp ............. yes
     wsock32 ............. no

   Protocol support:

      Kubernetes .... yes
      RDP ........... yes
      SSH ........... yes
      Telnet ........ yes
      VNC ........... yes

   Services / tools:

      guacd ...... yes
      guacenc .... yes
      guaclog .... yes

   FreeRDP plugins: /usr/lib/freerdp2
   Init scripts: no
   Systemd units: /usr/local/lib/systemd/system

Type "make" to compile guacamole-server.

$
```

The `--with-systemd-dir=/usr/local/lib/systemd/system` shown above prepares the
build to install a systemd unit file for guacd into the
`/usr/local/lib/systemd/system` directory, such that we can later easily
configure guacd to start automatically on boot. If you do not wish guacd to
start automatically at boot, leave off the `--with-systemd-dir` option. If the
directory used by your distribution for systemd unit files differs from the
common directory shown in the example above, replace it with the proper
directory here. You may need to consult your distribution’s documentation.

Traditional init (SysV)

```
$ ./configure --with-init-dir=/etc/init.d
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
...

------------------------------------------------
guacamole-server version 1.6.0
------------------------------------------------

   Library status:

     freerdp ............. yes (2.x)
     pango ............... yes
     libavcodec .......... yes
     libavformat ......... yes
     libavutil ........... yes
     libssh2 ............. yes
     libssl .............. yes
     libswscale .......... yes
     libtelnet ........... yes
     libVNCServer ........ yes
     libvorbis ........... yes
     libpulse ............ yes
     libwebsockets ....... yes
     libwebp ............. yes
     wsock32 ............. no

   Protocol support:

      Kubernetes .... yes
      RDP ........... yes
      SSH ........... yes
      Telnet ........ yes
      VNC ........... yes

   Services / tools:

      guacd ...... yes
      guacenc .... yes
      guaclog .... yes

   FreeRDP plugins: /usr/lib/freerdp2
   Init scripts: /etc/init.d
   Systemd units: no

Type "make" to compile guacamole-server.

$
```

The `--with-init-dir=/etc/init.d` shown above prepares the build to install a
startup script for guacd into the `/etc/init.d` directory, such that we can
later easily configure guacd to start automatically on boot. If you do not wish
guacd to start automatically at boot, leave off the `--with-init-dir` option.
If the directory containing your distribution’s startup scripts differs from
the common `/etc/init.d`, replace `/etc/init.d` with the proper directory here.
You may need to consult your distribution’s documentation, or do a little
digging in `/etc`, to determine the proper location.

Here, `configure` has found everything, including all optional libraries, and
will build all protocol support, even support for Ogg Vorbis sound in RDP. If
you are missing some libraries, some of the “`yes`” answers above will read
“`no`”. If a library which is strictly required is missing, the script will
fail outright, and you will need to install the missing dependency. If, after
running `configure`, you find support for something you wanted is missing,
simply install the corresponding dependencies and run `configure` again.

Important

All protocols that require a terminal (Kubernetes, SSH, and telnet) require
that fonts are installed on the Guacamole server in order to function, as
output from the terminal cannot be rendered otherwise. Support for these
protocols will build just fine if fonts are not installed, but it will render
incorrectly or fail to connect when used:

```
Aug 23 14:09:45 my-server guacd[5606]: Unable to get font "monospace"
```

If terminal-based connections are not working and you see such a message in
syslog, you should make sure fonts are installed and try again.

Once `configure` is finished, just type “`make`” and guacamole-server will
compile:

```
$ make
Making all in src/libguac
make[1]: Entering directory `/home/mjumper/guacamole/guacamole-server/src/libguac'
...
make[1]: Leaving directory `/home/mjumper/guacamole/guacamole-server/src/protocols/vnc'
make[1]: Entering directory `/home/mjumper/guacamole/guacamole-server'
make[1]: Nothing to be done for `all-am'.
make[1]: Leaving directory `/home/mjumper/guacamole/guacamole-server'
$
```

Quite a bit of output will scroll up the screen as all the components are
compiled.

### Installation[#](#installation "Link to this heading")

Once everything finishes, all you have left to do is type “`make install`” to
install the components that were built, and then “`ldconfig`” to update your
system’s cache of installed libraries:

```
# make install
Making install in src/libguac
make[1]: Entering directory `/home/mjumper/guacamole/guacamole-server/src/libguac'
make[2]: Entering directory `/home/mjumper/guacamole/guacamole-server/src/libguac'
...
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/lib

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH' environment variable
     during linking
   - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
make[2]: Nothing to be done for `install-data-am'.
make[2]: Leaving directory `/home/mjumper/guacamole/guacamole-server/src/protocols/vnc'
make[1]: Leaving directory `/home/mjumper/guacamole/guacamole-server/src/protocols/vnc'
make[1]: Entering directory `/home/mjumper/guacamole/guacamole-server'
make[2]: Entering directory `/home/mjumper/guacamole/guacamole-server'
make[2]: Nothing to be done for `install-exec-am'.
make[2]: Nothing to be done for `install-data-am'.
make[2]: Leaving directory `/home/mjumper/guacamole/guacamole-server'
make[1]: Leaving directory `/home/mjumper/guacamole/guacamole-server'
# ldconfig
#
```

At this point, everything is installed, but guacd is not running. You will need
to run guacd in order to use Guacamole once the client components are installed
as well.

Beware that even after installing guacd and its startup script, you will likely
still have to activate the service for it to start automatically. Doing this
varies by distribution, but each distribution will have documentation
describing how to do so.

## guacamole-client[#](#guacamole-client "Link to this heading")

Important

Normally, you don’t need to build guacamole-client, as it is written in Java
and is cross-platform. You can easily obtain the latest version of
guacamole-client from the release archives of the Guacamole project web site,
including all supported extensions, without having to build it yourself.

If you do not want to build guacamole-client from source, just download
`guacamole.war` from the project web site, along with any desired extensions,
and skip ahead to [Deploying Guacamole](#deploying-guacamole).

guacamole-client contains all Java and JavaScript components of Guacamole
(guacamole, guacamole-common, guacamole-ext, and guacamole-common-js). These
components ultimately make up the web application that will serve the HTML5
Guacamole client to users that connect to your server. This web application
will then connect to guacd, part of guacamole-server, on behalf of connected
users in order to serve them any remote desktop they are authorized to access.

To compile guacamole-client, all you need is Apache Maven and a copy of the
Java JDK. Most, if not all, Linux distributions will provide packages for
these.

You can obtain a copy of the guacamole-client source from the Guacamole project
web site. These releases are stable snapshots of the latest code which have
undergone enough testing that the Guacamole team considers them fit for public
consumption. Source downloaded from the project web site will take the form of
a `.tar.gz` archive which you can extract from the command line:

```
$ tar -xzf guacamole-client-1.6.0.tar.gz
$ cd guacamole-client-1.6.0/
$
```

As with guacamole-server, if you want the absolute latest code, and don’t care
that the code hasn’t been as rigorously tested as the code in stable releases,
you can also clone the Guacamole team’s git repository on GitHub:

```
$ git clone git://github.com/apache/guacamole-client.git
Cloning into 'guacamole-client'...
remote: Counting objects: 12788, done.
remote: Compressing objects: 100% (4183/4183), done.
remote: Total 12788 (delta 3942), reused 12667 (delta 3822)
Receiving objects: 100% (12788/12788), 3.23 MiB | 799 KiB/s, done.
Resolving deltas: 100% (3942/3942), done.
$
```

Unlike guacamole-server, even if you grab the code from the git repositories,
you won’t need to run anything before building. There are no scripts that need
to be generated before building - all Maven needs is the `pom.xml` file
provided with the source and internet access for downloading dependencies.

To build guacamole-client, just run “`mvn package`”. This will invoke Maven
to automatically build and package all components, producing a single `.war`
file, which contains the entire web application:

```
$ mvn package
[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Build Order:
[INFO]
[INFO] guacamole-client                                                   [pom]
[INFO] guacamole-common                                                   [jar]
[INFO] guacamole-ext                                                      [jar]
[INFO] guacamole-common-js                                                [pom]
[INFO] guacamole                                                          [war]
[INFO] extensions                                                         [pom]
[INFO] guacamole-auth-duo                                                 [jar]
[INFO] guacamole-auth-header                                              [jar]
[INFO] guacamole-auth-jdbc                                                [pom]
[INFO] guacamole-auth-jdbc-base                                           [jar]
[INFO] guacamole-auth-jdbc-mysql                                          [jar]
[INFO] guacamole-auth-jdbc-postgresql                                     [jar]
[INFO] guacamole-auth-jdbc-sqlserver                                      [jar]
[INFO] guacamole-auth-jdbc-dist                                           [pom]
[INFO] guacamole-auth-json                                                [jar]
[INFO] guacamole-auth-ldap                                                [jar]
[INFO] guacamole-auth-quickconnect                                        [jar]
[INFO] guacamole-auth-sso                                                 [pom]
[INFO] guacamole-auth-sso-base                                            [jar]
[INFO] guacamole-auth-sso-cas                                             [jar]
[INFO] guacamole-auth-sso-openid                                          [jar]
[INFO] guacamole-auth-sso-saml                                            [jar]
[INFO] guacamole-auth-sso-dist                                            [pom]
[INFO] guacamole-auth-totp                                                [jar]
[INFO] guacamole-history-recording-storage                                [jar]
[INFO] guacamole-vault                                                    [pom]
[INFO] guacamole-vault-base                                               [jar]
[INFO] guacamole-vault-ksm                                                [jar]
[INFO] guacamole-vault-dist                                               [pom]
[INFO] guacamole-example                                                  [war]
[INFO] guacamole-playback-example                                         [war]
...
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary for guacamole-client 1.6.0:
[INFO] 
[INFO] guacamole-client ................................... SUCCESS [ 11.879 s]
[INFO] guacamole-common ................................... SUCCESS [ 15.140 s]
[INFO] guacamole-ext ...................................... SUCCESS [ 14.764 s]
[INFO] guacamole-common-js ................................ SUCCESS [ 23.530 s]
[INFO] guacamole .......................................... SUCCESS [01:09 min]
[INFO] extensions ......................................... SUCCESS [  0.601 s]
[INFO] guacamole-auth-duo ................................. SUCCESS [  6.680 s]
[INFO] guacamole-auth-header .............................. SUCCESS [  3.379 s]
[INFO] guacamole-auth-jdbc ................................ SUCCESS [  0.239 s]
[INFO] guacamole-auth-jdbc-base ........................... SUCCESS [  6.755 s]
[INFO] guacamole-auth-jdbc-mysql .......................... SUCCESS [  6.523 s]
[INFO] guacamole-auth-jdbc-postgresql ..................... SUCCESS [  4.756 s]
[INFO] guacamole-auth-jdbc-sqlserver ...................... SUCCESS [  4.600 s]
[INFO] guacamole-auth-jdbc-dist ........................... SUCCESS [  3.381 s]
[INFO] guacamole-auth-json ................................ SUCCESS [  6.449 s]
[INFO] guacamole-auth-ldap ................................ SUCCESS [ 10.611 s]
[INFO] guacamole-auth-quickconnect ........................ SUCCESS [  6.908 s]
[INFO] guacamole-auth-sso ................................. SUCCESS [  0.216 s]
[INFO] guacamole-auth-sso-base ............................ SUCCESS [  4.174 s]
[INFO] guacamole-auth-sso-cas ............................. SUCCESS [ 12.180 s]
[INFO] guacamole-auth-sso-openid .......................... SUCCESS [  5.119 s]
[INFO] guacamole-auth-sso-saml ............................ SUCCESS [  5.263 s]
[INFO] guacamole-auth-sso-dist ............................ SUCCESS [  6.400 s]
[INFO] guacamole-auth-totp ................................ SUCCESS [  9.445 s]
[INFO] guacamole-history-recording-storage ................ SUCCESS [  2.370 s]
[INFO] guacamole-vault .................................... SUCCESS [  0.177 s]
[INFO] guacamole-vault-base ............................... SUCCESS [  3.899 s]
[INFO] guacamole-vault-ksm ................................ SUCCESS [  8.084 s]
[INFO] guacamole-vault-dist ............................... SUCCESS [  3.555 s]
[INFO] guacamole-example .................................. SUCCESS [  2.363 s]
[INFO] guacamole-playback-example ......................... SUCCESS [  1.040 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  04:20 min
[INFO] Finished at: 2023-01-10T17:20:33-08:00
[INFO] ------------------------------------------------------------------------
$
```

Once the Guacamole web application is built, there will be a .war file in the
`guacamole/target/` subdirectory of the current directory (the directory you
were in when you ran mvn), ready to be deployed to a servlet container like
Tomcat.

## Deploying Guacamole[#](#deploying-guacamole "Link to this heading")

The web application portion of Guacamole is packaged as a fully self-contained
`.war` file. If you downloaded Guacamole from the main project web site, this
file will be called `guacamole.war`. Deploying this involves copying the file
into the directory your servlet container uses for `.war` files. In the case of
Tomcat, this will be `CATALINA_HOME/webapps/`. The location of `CATALINA_HOME`
will vary by how Tomcat was installed, but is commonly `/var/lib/tomcat`,
`/var/lib/tomcat9`, or similar:

```
# cp guacamole.war /var/lib/tomcat/webapps
#
```

If you have built guacamole-client from source, the required `.war` file will
be within the `guacamole/target/` directory and will contain an additional
version suffix. As Tomcat will determine the location of the web application
from the name of the `.war` file, you will likely want to rename this to simply
`guacamole.war` while copying:

```
# cp guacamole/target/guacamole-1.6.0.war /var/lib/tomcat/webapps/guacamole.war
#
```

Again, if you are using a different servlet container or if Tomcat is installed
to a different location, you will need to check the documentation of your
servlet container, distribution, or both to determine the proper location for
deploying `.war` files like `guacamole.war`.

Once the `.war` file is in place, you may need to restart Tomcat to force
Tomcat to deploy the new web application, and the guacd daemon must be started
if it isn’t running already. The command to restart Tomcat and guacd will vary
by distribution. Typically, you can do this by running the corresponding init
scripts with the “restart” option:

systemd

```
# systemctl restart tomcat9
# systemctl start guacd
```

Important

If you want Guacamole to start on boot, you will need to configure
the Tomcat and guacd services to run automatically. With systemd, this is done
using the “enable” command:

```
# systemctl enable tomcat9
# systemctl enable guacd
```

Traditional init (SysV)

```
# service tomcat9 restart
# service guacd start
```

Important

If you want Guacamole to start on boot, you will need to configure
the Tomcat and guacd services to run automatically. Your distribution
will provide documentation for doing this.

After restarting Tomcat and starting guacd, Guacamole is successfully
installed, though it will not be fully running. In its current state, it is
completely unconfigured, and further steps are required to add at least one
Guacamole user and a few connections. This is covered in
[Configuring Guacamole](configuring-guacamole.html).

### What about WebSocket?[#](#what-about-websocket "Link to this heading")

Guacamole will use WebSocket automatically if supported by the browser and your
servlet container. In the event that Guacamole cannot connect using WebSocket,
it will immediately and transparently fall back to using HTTP.

WebSocket is supported in Guacamole for Tomcat 7.0.37 or higher, Jetty 8 or
higher, and any servlet container supporting JSR 356, the standardized Java API
for WebSocket.

Contents

---
# Database setup for SQL Server

## Contents

# Database setup for SQL Server[#](#database-setup-for-sql-server "Link to this heading")

To use Guacamole with a SQL Server database, you will need:

1. An instance of the SQL Server database server.
2. Sufficient permission to create new databases, to create new users, and to
   grant those users permissions.
3. Network access to the database from the Guacamole server.

If this is not the case, you will need to install SQL Server before continuing
or use a different database. Guacamole additionally supports:

* [MariaDB / MySQL](mysql-auth.html)
* [PostgreSQL](postgresql-auth.html)

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Creating the Guacamole database[#](#creating-the-guacamole-database "Link to this heading")

It is best practice to use a dedicated database and user for the Guacamole web
application, and these instructions cover only this method.

To create the database within SQL Server, execute a `CREATE DATABASE` command
with the `sqlcmd` client:

```
$ /opt/mssql-tools/bin/sqlcmd -S localhost -U SA
Password:
1> CREATE DATABASE guacamole_db;
2> GO
1> quit
```

### Initializing the database[#](#initializing-the-database "Link to this heading")

Native Webapp (Tomcat)

The schema scripts necessary to initialize the SQL Server version of Guacamole’s
database are provided within the `sqlserver/schema/` directory of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download),
which must be downloaded from [the release page for Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
and extracted first.

Running each the two scripts in the `sqlserver/schema/` directory against the
newly created database will initialize it with Guacamole’s schema. You can run
these scripts using the standard `sqlcmd` client:

```
$ /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -d guacamole_db -i schema/001-create-schema.sql
Password:
Rule bound to data type.
The new rule has been bound to column(s) of the specified user data type.
Rule bound to data type.
The new rule has been bound to column(s) of the specified user data type.
$ /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -d guacamole_db -i schema/002-create-admin-user.sql
Password:

(1 rows affected)

(3 rows affected)

(5 rows affected)
$
```

Container (Docker)

The schema scripts necessary to initialize the SQL Server version of Guacamole’s
database are provided within the `/opt/guacamole/extensions/guacamole-auth-jdbc/sqlserver/schema`
directory of the `guacamole/guacamole` image.

Additionally, an `initdb.sh` script is provided at `/opt/guacamole/bin/initdb.sh`
that can be used to extract the required schema initialization script:

```
$ docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --sqlserver > initdb.sql
```

The resulting script can then be run using the `sqlcmd` client:

```
$ /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -d guacamole_db -i initdb.sql
```

## Granting Guacamole access to the database[#](#granting-guacamole-access-to-the-database "Link to this heading")

For Guacamole to be able to execute queries against the database, you must
create a new user for the database and grant that user sufficient privileges to
manage the contents of all tables in the database.

The user created for Guacamole needs only `SELECT`, `UPDATE`, `INSERT`, and
`DELETE` permissions on all tables in the Guacamole database. These can
permissions can be easily granted in SQL Server using the `db_datawriter` and
`db_datareader` roles:

```
$ /opt/mssql-tools/bin/sqlcmd -S localhost -U SA
Password:
1> CREATE LOGIN guacamole_user WITH PASSWORD = 'some_password';
2> GO
1> USE guacamole_db;
2> GO
1> CREATE USER guacamole_user;
2> GO
1> ALTER ROLE db_datawriter ADD MEMBER guacamole_user;
2> ALTER ROLE db_datareader ADD MEMBER guacamole_user;
3> GO
1> quit
$
```

## Upgrading an existing Guacamole database[#](#upgrading-an-existing-guacamole-database "Link to this heading")

If you are upgrading from a version of Guacamole older than 1.6.0, you
may need to run one or more database schema upgrade scripts located within the
`sqlserver/schema/upgrade/` directory of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download)
(available from [the release page for Apache Guacamole
1.6.0](https://guacamole.apache.org/releases/1.6.0)).

Each of these scripts is named `upgrade-pre-VERSION.sql` where
`VERSION` is the version of Guacamole where those changes were introduced. They
need to be run when you are upgrading from a version of Guacamole older than
`VERSION`.

If there are no `upgrade-pre-VERSION.sql` scripts present in the
`schema/upgrade/` directory which apply to your existing Guacamole database,
then the schema has not changed between your version and the version your are
installing, and there is no need to run any database upgrade scripts.

These scripts are incremental and, when relevant, *must be run in order*. For
example, if you are upgrading an existing database from version
0.9.13-incubating to version 1.0.0, you would need to run the
`upgrade-pre-0.9.14.sql` script (because 0.9.13-incubating is older than
0.9.14), followed by the `upgrade-pre-1.0.0.sql` script (because
0.9.13-incubating is also older than 1.0.0).

## Installing/Enabling support for SQL Server[#](#installing-enabling-support-for-sql-server "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. You should have a copy of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download) from
   earlier when you [created and initialized the database](#sqlserver-auth-database-creation).
2. Create the `GUACAMOLE_HOME/extensions` and `GUACAMOLE_HOME/lib` directories,
   if they do not already exist.
3. Copy `sqlserver/guacamole-auth-jdbc-sqlserver-1.6.0.jar`
   within `GUACAMOLE_HOME/extensions`.
4. Copy the JDBC driver for your database to `GUACAMOLE_HOME/lib`.
   Any of the following TDS-compatible JDBC drivers are supported for connecting
   Guacamole to SQL Server:

   * [Microsoft JDBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server)
   * [jTDS](http://jtds.sourceforge.net/)
   * [Progress DataDirect’s JDBC Driver for SQL Server](https://www.progress.com/jdbc/microsoft-sql-server)
   * Microsoft SQL Server 2000 JDBC Driver (legacy)

   If you do not have a specific reason to use one driver over the other, it’s
   recommended that you use the JDBC driver provided by your database vendor.
5. Configure Guacamole to use database authentication, as described below.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `SQLSERVER_ENABLED` environment variable:

    ```
    SQLSERVER_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e SQLSERVER_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `SQLSERVER_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `SQLSERVER_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Required configuration[#](#required-configuration "Link to this heading")

Additional configuration options must be specified for Guacamole to properly
connect to your database. These options are specific to the database being
used, and must be set correctly for authentication to work.

The options absolutely required by the database authentication extension are
relatively few and self-explanatory, describing only which database will be
used and how Guacamole will authenticate when querying that database:

Native Webapp (Tomcat)

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
sqlserver-database: guacamole_db
sqlserver-username: guacamole_user
sqlserver-password: some_password
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`sqlserver-database`
:   The name of the database that you created for Guacamole. This is given as
    “guacamole\_db” in the examples given in this chapter.

`sqlserver-username`
:   The username of the user that Guacamole should use to connect to the
    database. This is given as “guacamole\_user” in the examples given in this
    chapter.

`sqlserver-password`
:   The password Guacamole should provide when authenticating with the database.
    This is given as “some\_password” in the examples given in this chapter.

Container (Docker)

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
SQLSERVER_DATABASE: 'guacamole_db'
SQLSERVER_USERNAME: 'guacamole_user'
SQLSERVER_PASSWORD: 'some_password'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e SQLSERVER_DATABASE="guacamole_db" \
    -e SQLSERVER_USERNAME="guacamole_user" \
    -e SQLSERVER_PASSWORD="some_password" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`SQLSERVER_DATABASE`
:   The name of the database that you created for Guacamole. This is given as
    “guacamole\_db” in the examples given in this chapter.

`SQLSERVER_USERNAME`
:   The username of the user that Guacamole should use to connect to the
    database. This is given as “guacamole\_user” in the examples given in this
    chapter.

`SQLSERVER_PASSWORD`
:   The password Guacamole should provide when authenticating with the database.
    This is given as “some\_password” in the examples given in this chapter.

Hint

**Double-check these values.** You will not be able to sign into Guacamole
after installation if these parameters do not match the correct database name,
username, and password.

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Additional options are available to control how Guacamole connects to the
database server:

Native Webapp (Tomcat)

`sqlserver-hostname`
:   The hostname or IP address of the server hosting your database. If not
    specified, “localhost” will be used by default.

`sqlserver-port`
:   The port number of the SQL Server database to connect to. If not specified,
    the standard SQL Server port 1433 will be used.

`sqlserver-driver`
:   The specific TDS-compatible JDBC driver to expect to have been installed.
    Multiple JDBC drivers are available that support SQL Server. If not using the
    Microsoft driver, this property must be specified to define the driver that
    will be used. Possible values are:

    microsoft2005
    :   The current [Microsoft JDBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server),
        supporting SQL Server 2005 and later. This is the default.

    microsoft
    :   The legacy Microsoft driver for SQL Server 2000.

    jtds
    :   The open source [jTDS](http://jtds.sourceforge.net/) driver.

    datadirect
    :   [Progress DataDirect’s JDBC Driver for SQL Server](https://www.progress.com/jdbc/microsoft-sql-server).

`sqlserver-instance`
:   The instance name that the SQL Server driver should attempt to connect to, if
    not the default SQL Server instance. This instance name is configured during
    the SQL Server installation. This property is optional, and most installations
    should work without the need to specify an instance name.

`sqlserver-batch-size`
:   Controls how many objects may be retrieved from the database in a single
    query. If more objects than this number are requested, retrieval of those
    objects will be automatically and transparently split across multiple
    queries.

    By default, SQL Server queries will retrieve no more than 500 objects.

Container (Docker)

`SQLSERVER_HOSTNAME`
:   The hostname or IP address of the server hosting your database. If not
    specified, “localhost” will be used by default.

`SQLSERVER_PORT`
:   The port number of the SQL Server database to connect to. If not specified,
    the standard SQL Server port 1433 will be used.

`SQLSERVER_DRIVER`
:   The specific TDS-compatible JDBC driver to expect to have been installed.
    Multiple JDBC drivers are available that support SQL Server. If not using the
    Microsoft driver, this property must be specified to define the driver that
    will be used. Possible values are:

    microsoft2005
    :   The current [Microsoft JDBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server),
        supporting SQL Server 2005 and later. This is the default.

    microsoft
    :   The legacy Microsoft driver for SQL Server 2000.

    jtds
    :   The open source [jTDS](http://jtds.sourceforge.net/) driver.

    datadirect
    :   [Progress DataDirect’s JDBC Driver for SQL Server](https://www.progress.com/jdbc/microsoft-sql-server).

`SQLSERVER_INSTANCE`
:   The instance name that the SQL Server driver should attempt to connect to, if
    not the default SQL Server instance. This instance name is configured during
    the SQL Server installation. This property is optional, and most installations
    should work without the need to specify an instance name.

`SQLSERVER_BATCH_SIZE`
:   Controls how many objects may be retrieved from the database in a single
    query. If more objects than this number are requested, retrieval of those
    objects will be automatically and transparently split across multiple
    queries.

    By default, SQL Server queries will retrieve no more than 500 objects.

### Enforcing password policies[#](#enforcing-password-policies "Link to this heading")

Configuration options are available for enforcing rules intended to encourage
password complexity and regular changing of passwords. None of these options
are enabled by default, but can be selectively enabled as needed.

#### Password complexity[#](#password-complexity "Link to this heading")

Administrators can require that passwords have a certain level of complexity,
such as having both uppercase and lowercase letters (“multiple case”), at least
one digit, or at least one symbol, and can prohibit passwords from containing
the user’s own username.

With respect to password content, the database authentication defines a “digit”
as any numeric character and a “symbol” is any non-alphanumeric character. This
takes non-English languages into account, thus a digit is not simply “0”
through “9” but rather [any character defined in Unicode as
numeric](https://en.wikipedia.org/wiki/Numerals_in_Unicode), and a symbol is
any character which Unicode does not define as alphabetic or numeric.

The check for whether a password contains the user’s own username is performed
in a case-insensitive manner. For example, if the user’s username is “phil”,
the passwords “ch!0roPhil” and “PHIL-o-dendr0n” would still be prohibited.

Native Webapp (Tomcat)

`sqlserver-user-password-min-length`
:   The minimum length required of all user passwords, in characters. By default,
    password length is not enforced.

`sqlserver-user-password-require-multiple-case`
:   Whether all user passwords must have at least one lowercase character and one
    uppercase character. By default, no such restriction is imposed.

`sqlserver-user-password-require-symbol`
:   Whether all user passwords must have at least one non-alphanumeric character
    (symbol). By default, no such restriction is imposed.

`sqlserver-user-password-require-digit`
:   Whether all user passwords must have at least one numeric character (digit).
    By default, no such restriction is imposed.

`sqlserver-user-password-prohibit-username`
:   Whether users are prohibited from including their own username in their
    password. By default, no such restriction is imposed.

Container (Docker)

`SQLSERVER_USER_PASSWORD_MIN_LENGTH`
:   The minimum length required of all user passwords, in characters. By default,
    password length is not enforced.

`SQLSERVER_USER_PASSWORD_REQUIRE_MULTIPLE_CASE`
:   Whether all user passwords must have at least one lowercase character and one
    uppercase character. By default, no such restriction is imposed.

`SQLSERVER_USER_PASSWORD_REQUIRE_SYMBOL`
:   Whether all user passwords must have at least one non-alphanumeric character
    (symbol). By default, no such restriction is imposed.

`SQLSERVER_USER_PASSWORD_REQUIRE_DIGIT`
:   Whether all user passwords must have at least one numeric character (digit).
    By default, no such restriction is imposed.

`SQLSERVER_USER_PASSWORD_PROHIBIT_USERNAME`
:   Whether users are prohibited from including their own username in their
    password. By default, no such restriction is imposed.

#### Password age / expiration[#](#password-age-expiration "Link to this heading")

“Password age” refers to two separate concepts:

1. Requiring users to change their password after a certain amount of time has
   elapsed since the last password change (maximum password age).
2. Preventing users from changing their password too frequently (minimum
   password age).

While it may seem strange to prevent users from changing their password too
frequently, it does make sense if you are concerned that rapid password changes
may defeat password expiration (users could immediately change the password
back) or tracking of password history (users could cycle through passwords
until the history is exhausted and their old password is usable again).

By default, the database authentication does not apply any limits to password
age, and users with permission to change their passwords may do so as
frequently or infrequently as they wish. Password age limits can be enabled
using a pair of configuration options, each accepting values given in units of
days:

Native Webapp (Tomcat)

`sqlserver-user-password-min-age`
:   The minimum number of days which must elapse before a user may reset their
    password, where zero represents no limit. By default, no minimum number of
    days is required.

`sqlserver-user-password-max-age`
:   The maximum number of days which may elapse before a user is automatically
    required to reset their password, where zero represents no limit. By default,
    users are not automatically required to reset their password based on
    password age.

Container (Docker)

`SQLSERVER_USER_PASSWORD_MIN_AGE`
:   The minimum number of days which must elapse before a user may reset their
    password, where zero represents no limit. By default, no minimum number of
    days is required.

`SQLSERVER_USER_PASSWORD_MAX_AGE`
:   The maximum number of days which may elapse before a user is automatically
    required to reset their password, where zero represents no limit. By default,
    users are not automatically required to reset their password based on
    password age.

Important

So that administrators can always intervene in the case that a password needs
to be reset despite restrictions, the minimum age restriction does not apply to
any user with permission to administer the system.

#### Preventing password reuse[#](#preventing-password-reuse "Link to this heading")

If desired, Guacamole can keep track of each user’s most recently used
passwords, and will prohibit reuse of those passwords until the password has
been changed sufficiently many times. By default, Guacamole will not keep track
of old passwords.

Note that these passwords are hashed in the same manner as each user’s current
password. When a user’s password is changed, the hash, salt, etc. currently
stored for that user is actually just copied verbatim (along with a timestamp)
into a list of historical passwords, with older entries from this list being
automatically deleted.

Native Webapp (Tomcat)

`sqlserver-user-password-history-size`
:   The number of previous passwords remembered for each user, where zero
    represents no history. If set to a non-zero value, users will be restricted
    from reusing any password in their password history. Passwords are remembered
    only in hashed and salted form. By default, previous passwords are not
    remembered and no such restriction is enforced.

Container (Docker)

`SQLSERVER_USER_PASSWORD_HISTORY_SIZE`
:   The number of previous passwords remembered for each user, where zero
    represents no history. If set to a non-zero value, users will be restricted
    from reusing any password in their password history. Passwords are remembered
    only in hashed and salted form. By default, previous passwords are not
    remembered and no such restriction is enforced.

### Concurrent use of Guacamole connections[#](#concurrent-use-of-guacamole-connections "Link to this heading")

The database authentication module provides configuration options to restrict
concurrent use of connections and connection groups. Concurrent use can be
restricted broadly or to ensure that each individual user may only maintain a
limited number of active connections to any one connection or group.

By default, concurrent usage is unrestricted except that each user may only
have a single active connection to each connection group. This is intended to
avoid the case that a single user is able to exhaust the contents of a
connection group and effectively block others from using the same resources.

If you wish to impose an absolute limit on the number of active connections
that can be established through Guacamole, ignoring which users or connections
are involved, this can be done as well.

The default policy set through these options can be overridden later on a
per-connection basis using the administrative interface.

Native Webapp (Tomcat)

`sqlserver-default-max-connections`
:   The maximum number of concurrent connections to allow to any one connection,
    regardless of which user is accessing the connection, where zero denotes
    unlimited. By default, overall concurrent access to individual connections is
    not limited.

`sqlserver-default-max-group-connections`
:   The maximum number of concurrent connections to allow to any one connection
    group, regardless of which user is accessing the connection group, where zero
    denotes unlimited. By default, overall concurrent access to individual
    connection groups is not limited.

`sqlserver-default-max-connections-per-user`
:   The maximum number of concurrent connections to allow to any one connection
    by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to individual connections is not limited.

`sqlserver-default-max-group-connections-per-user`
:   The maximum number of concurrent connections to allow to any one connection
    group by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to connection groups is limited to one user.

`sqlserver-absolute-max-connections`
:   The maximum number of concurrent connections to allow overall, regardless of
    which connection or connection group is used and regardless of which user is
    accessing the connection/group, where zero denotes unlimited. By default,
    overall concurrent access to Guacamole is not limited.

Container (Docker)

`SQLSERVER_DEFAULT_MAX_CONNECTIONS`
:   The maximum number of concurrent connections to allow to any one connection,
    regardless of which user is accessing the connection, where zero denotes
    unlimited. By default, overall concurrent access to individual connections is
    not limited.

`SQLSERVER_DEFAULT_MAX_GROUP_CONNECTIONS`
:   The maximum number of concurrent connections to allow to any one connection
    group, regardless of which user is accessing the connection group, where zero
    denotes unlimited. By default, overall concurrent access to individual
    connection groups is not limited.

`SQLSERVER_DEFAULT_MAX_CONNECTIONS_PER_USER`
:   The maximum number of concurrent connections to allow to any one connection
    by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to individual connections is not limited.

`SQLSERVER_DEFAULT_MAX_GROUP_CONNECTIONS_PER_USER`
:   The maximum number of concurrent connections to allow to any one connection
    group by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to connection groups is limited to one user.

`SQLSERVER_ABSOLUTE_MAX_CONNECTIONS`
:   The maximum number of concurrent connections to allow overall, regardless of
    which connection or connection group is used and regardless of which user is
    accessing the connection/group, where zero denotes unlimited. By default,
    overall concurrent access to Guacamole is not limited.

### External users and connections[#](#external-users-and-connections "Link to this heading")

When [combining LDAP with a database](ldap-auth.html#ldap-and-database), or using a single
sign-on system like [OpenID Connect](openid-auth.html) or [SAML](saml-auth.html), user
accounts are not purely defined by Guacamole’s database. They are additionally
defined by the relevant external system. In some cases, such as the [LDAP
extension’s capability to retrieve connection information from the LDAP
directory](ldap-auth.html#ldap-schema-changes), connections are not purely defined by
Guacamole’s database either.

In these cases, it may be desirable to:

* Limit use of Guacamole to only those users that *do* already exist in the
  database.
* Automatically create users in the database when they have successfully
  authenticated through other means, such that extensions requiring storage
  like TOTP can be used alongside SSO solutions.
* Control whether the database logs connection usage history for connections
  that are not maintained by the database.

By default, users will be allowed access to Guacamole as long as they are
authenticated by at least one extension, no extension denies/vetoes access, and
the database will record connection history entries for all connections
regardless of whether they are maintained by the database.

Note

In all cases, users will only be able to see or interact with resources that
they have been given permission to access. This is true whether those
permissions are granted explicitly or through inheritance (from user groups).

Native Webapp (Tomcat)

`sqlserver-user-required`
:   Whether a user account within the database is required for authentication to
    succeed, even if the user has been authenticated via another extension. By
    default, successful authentication via any extension is sufficient, and
    database user accounts are not strictly required.

`sqlserver-auto-create-accounts`
:   Whether to automatically create user accounts in the database for users who
    have successfully authenticate through another extension. Users that are
    automatically created are granted `READ` permission on their own user account
    and no other explicit permissions. By default users will not be automatically
    created.

`sqlserver-track-external-connection-history`
:   Whether connection history records should be created for connections not
    defined in the database. By default, external connection history will be
    tracked unless this is explicitly disabled by setting this to “false”.

Container (Docker)

`SQLSERVER_USER_REQUIRED`
:   Whether a user account within the database is required for authentication to
    succeed, even if the user has been authenticated via another extension. By
    default, successful authentication via any extension is sufficient, and
    database user accounts are not strictly required.

`SQLSERVER_AUTO_CREATE_ACCOUNTS`
:   Whether to automatically create user accounts in the database for users who
    have successfully authenticate through another extension. Users that are
    automatically created are granted `READ` permission on their own user account
    and no other explicit permissions. By default users will not be automatically
    created.

`SQLSERVER_TRACK_EXTERNAL_CONNECTION_HISTORY`
:   Whether connection history records should be created for connections not
    defined in the database. By default, external connection history will be
    tracked unless this is explicitly disabled by setting this to “false”.

### Access window enforcment[#](#access-window-enforcment "Link to this heading")

Guacamole supports the use of access windows to limit the time periods during
which users are allowed to access the system. By default, users will be
forcibly logged out from Guacamole as soon as the access window expires,
disconnecting them from any active connections.

If you would prefer users to be allowed to remain logged in, this behavior can
be overridden using the configuration option below.

Note

Prior to [Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0),
access windows were enforced only during the login process. Access windows
restricted only when a user could log in, not whether they could remain logged
in.

Native Webapp (Tomcat)

`sqlserver-enforce-access-windows-for-active-sessions`
:   Whether time-based access windows should be enforced for active user sessions.
    By default, users will be logged out when an access window closes, even if
    they are currently logged in. To allow logged-in users to continue to use the
    application after an access window closes, set this to “false”. Users will
    always be prevented from logging in outside of access windows regardless of
    this setting.

Container (Docker)

`SQLSERVER_ENFORCE_ACCESS_WINDOWS_FOR_ACTIVE_SESSIONS`
:   Whether time-based access windows should be enforced for active user sessions.
    By default, users will be logged out when an access window closes, even if
    they are currently logged in. To allow logged-in users to continue to use the
    application after an access window closes, set this to “false”. Users will
    always be prevented from logging in outside of access windows regardless of
    this setting.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Logging in[#](#logging-in "Link to this heading")

The default Guacamole user created by the provided SQL scripts is
“`guacadmin`”, with a default password of “`guacadmin`”. Once you have verified
that the database authentication is working, **you should [change your password
immediately](using-guacamole.html#changing-password)**.

Once you have successfully logged in and changed your password, you can begin
using the web UI to create other users, groups, and connections. More detailed
instructions for doing this are given in [Guacamole’s administrative interface](administration.html).

Contents

---
# Using OpenID Connect for single sign-on

## Contents

# Using OpenID Connect for single sign-on[#](#using-openid-connect-for-single-sign-on "Link to this heading")

[OpenID Connect](http://openid.net/connect/) is a widely-adopted open standard
for implementing single sign-on (SSO). [Not to be confused with
OAuth](https://oauth.net/articles/authentication/), which is *not* an
authentication protocol, OpenID Connect defines an authentication protocol in
the form of a simple identity layer on top of OAuth 2.0.

Guacamole’s OpenID Connect support implements the “[implicit
flow](https://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth)”
of the OpenID Connect standard, and allows authentication of Guacamole users to
be delegated to an identity provider which implements OpenID Connect, removing
the need for users to log into Guacamole directly. This module must be layered
on top of other authentication extensions that provide connection information,
such as the [database authentication extension](jdbc-auth.html), as it only provides
user authentication.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling the OpenID Connect authentication extension[#](#installing-enabling-the-openid-connect-authentication-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-sso-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-sso-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `openid/guacamole-auth-sso-openid-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `OPENID_ENABLED` environment variable:

    ```
    OPENID_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e OPENID_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `OPENID_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `OPENID_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Required configuration[#](#required-configuration "Link to this heading")

Native Webapp (Tomcat)

Guacamole’s OpenID connect support requires several properties
which describe both the identity provider and the Guacamole deployment. These
properties are *absolutely required in all cases*, as they dictate
how Guacamole should connect to the identity provider, how it should verify the
identity provider’s response, and how the identity provider should redirect
users back to Guacamole once their identity has been confirmed:

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
openid-authorization-endpoint: https://identity-provider/auth
openid-jwks-endpoint: https://identity-provider/jwks
openid-issuer: identity-provider
openid-client-id: my-client-id
openid-redirect-uri: https://example.net/guacamole
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`openid-authorization-endpoint`
:   The authorization endpoint (URI) of the OpenID service.

    This value should be provided to you by the identity provider. For identity
    providers that implement [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html),
    this value can be retrieved from the `authorization_endpoint` property of the
    JSON file hosted at `https://identity-provider/.well-known/openid-configuration`, where
    `https://identity-provider` is the base URL of the identity provider.

`openid-jwks-endpoint`
:   The endpoint (URI) of the JWKS service which defines how received ID tokens
    ([JSON Web Tokens](https://jwt.io/) or JWTs) shall be validated.

    This value should be provided to you by the identity provider. For
    identity providers that implement [OpenID Connect
    Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html),
    this value can be retrieved from the `jwks_uri` property of the JSON
    file hosted at
    `https://identity-provider/.well-known/openid-configuration`, where
    `https://identity-provider` is the base URL of the identity provider.

`openid-issuer`
:   The issuer to expect for all received ID tokens.

    This value should be provided to you by the identity provider. For
    identity providers that implement [OpenID Connect
    Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html),
    this value can be retrieved from the `issuer` property of the JSON
    file hosted at
    `https://identity-provider/.well-known/openid-configuration`, where
    `https://identity-provider` is the base URL of the identity provider.

`openid-client-id`
:   The OpenID client ID which should be submitted to the OpenID service when
    necessary. This value is typically provided to you by the OpenID service when
    OpenID credentials are generated for your application.

`openid-redirect-uri`
:   The URI that should be submitted to the OpenID service such that they
    can redirect the authenticated user back to Guacamole after the
    authentication process is complete. This must be the full URL that a user
    would enter into their browser to access Guacamole.

Container (Docker)

Guacamole’s OpenID connect support requires several environment variables
which describe both the identity provider and the Guacamole deployment. These
environment variables are *absolutely required in all cases*, as they dictate
how Guacamole should connect to the identity provider, how it should verify the
identity provider’s response, and how the identity provider should redirect
users back to Guacamole once their identity has been confirmed:

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
OPENID_AUTHORIZATION_ENDPOINT: 'https://identity-provider/auth'
OPENID_JWKS_ENDPOINT: 'https://identity-provider/jwks'
OPENID_ISSUER: 'identity-provider'
OPENID_CLIENT_ID: 'my-client-id'
OPENID_REDIRECT_URI: 'https://example.net/guacamole'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e OPENID_AUTHORIZATION_ENDPOINT="https://identity-provider/auth" \
    -e OPENID_JWKS_ENDPOINT="https://identity-provider/jwks" \
    -e OPENID_ISSUER="identity-provider" \
    -e OPENID_CLIENT_ID="my-client-id" \
    -e OPENID_REDIRECT_URI="https://example.net/guacamole" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`OPENID_AUTHORIZATION_ENDPOINT`
:   The authorization endpoint (URI) of the OpenID service.

    This value should be provided to you by the identity provider. For identity
    providers that implement [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html),
    this value can be retrieved from the `authorization_endpoint` property of the
    JSON file hosted at `https://identity-provider/.well-known/openid-configuration`, where
    `https://identity-provider` is the base URL of the identity provider.

`OPENID_JWKS_ENDPOINT`
:   The endpoint (URI) of the JWKS service which defines how received ID tokens
    ([JSON Web Tokens](https://jwt.io/) or JWTs) shall be validated.

    This value should be provided to you by the identity provider. For
    identity providers that implement [OpenID Connect
    Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html),
    this value can be retrieved from the `jwks_uri` property of the JSON
    file hosted at
    `https://identity-provider/.well-known/openid-configuration`, where
    `https://identity-provider` is the base URL of the identity provider.

`OPENID_ISSUER`
:   The issuer to expect for all received ID tokens.

    This value should be provided to you by the identity provider. For
    identity providers that implement [OpenID Connect
    Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html),
    this value can be retrieved from the `issuer` property of the JSON
    file hosted at
    `https://identity-provider/.well-known/openid-configuration`, where
    `https://identity-provider` is the base URL of the identity provider.

`OPENID_CLIENT_ID`
:   The OpenID client ID which should be submitted to the OpenID service when
    necessary. This value is typically provided to you by the OpenID service when
    OpenID credentials are generated for your application.

`OPENID_REDIRECT_URI`
:   The URI that should be submitted to the OpenID service such that they
    can redirect the authenticated user back to Guacamole after the
    authentication process is complete. This must be the full URL that a user
    would enter into their browser to access Guacamole.

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Native Webapp (Tomcat)

Additional optional properties are available to control how claims
within received ID tokens are used to derive the user’s Guacamole username, any
associated groups, the OpenID scopes requested when user identities are
confirmed, and to control the maximum amount of time allowed for various
aspects of the conversation with the identity provider:

`openid-username-claim-type`
:   The claim type within any valid JWT that contains the authenticated user’s
    username. By default, the “`email`” claim type is used.

`openid-groups-claim-type`
:   The claim type within any valid JWT that contains the list of groups of which
    the authenticated user is a member. By default, the “`groups`” claim type is
    used.

`openid-attributes-claim-type`
:   The list of claims, separated by commas, that should be extracted from the
    JWT token and exposed as `OIDC_` attributes to use in connections. Empty by
    default.

`openid-scope`
:   The space-separated list of OpenID scopes to request. OpenID scopes determine
    the information returned within the OpenID token, and thus affect what values
    can be used as an authenticated user’s username. To be compliant with
    OpenID, at least “`openid profile`” must be requested. By default, “`openid email profile`” is used.

`openid-allowed-clock-skew`
:   The amount of clock skew tolerated for timestamp comparisons between the
    Guacamole server and OpenID service clocks, in seconds. By default, clock
    skew of up to 30 seconds is tolerated.

`openid-max-token-validity`
:   The maximum amount of time that an OpenID token should remain valid, in
    minutes. By default, each OpenID token remains valid for 300 minutes (5
    hours).

`openid-max-nonce-validity`
:   The maximum amount of time that a nonce generated by the Guacamole server
    should remain valid, in minutes. As each OpenID request has a unique nonce
    value, this imposes an upper limit on the amount of time any particular
    OpenID request can result in successful authentication within Guacamole. By
    default, each generated nonce expires after 10 minutes.

Container (Docker)

Additional optional environment variables are available to control how claims
within received ID tokens are used to derive the user’s Guacamole username, any
associated groups, the OpenID scopes requested when user identities are
confirmed, and to control the maximum amount of time allowed for various
aspects of the conversation with the identity provider:

`OPENID_USERNAME_CLAIM_TYPE`
:   The claim type within any valid JWT that contains the authenticated user’s
    username. By default, the “`email`” claim type is used.

`OPENID_GROUPS_CLAIM_TYPE`
:   The claim type within any valid JWT that contains the list of groups of which
    the authenticated user is a member. By default, the “`groups`” claim type is
    used.

`OPENID_ATTRIBUTES_CLAIM_TYPE`
:   The list of claims, separated by commas, that should be extracted from the
    JWT token and exposed as `OIDC_` attributes to use in connections. Empty by
    default.

`OPENID_SCOPE`
:   The space-separated list of OpenID scopes to request. OpenID scopes determine
    the information returned within the OpenID token, and thus affect what values
    can be used as an authenticated user’s username. To be compliant with
    OpenID, at least “`openid profile`” must be requested. By default, “`openid email profile`” is used.

`OPENID_ALLOWED_CLOCK_SKEW`
:   The amount of clock skew tolerated for timestamp comparisons between the
    Guacamole server and OpenID service clocks, in seconds. By default, clock
    skew of up to 30 seconds is tolerated.

`OPENID_MAX_TOKEN_VALIDITY`
:   The maximum amount of time that an OpenID token should remain valid, in
    minutes. By default, each OpenID token remains valid for 300 minutes (5
    hours).

`OPENID_MAX_NONCE_VALIDITY`
:   The maximum amount of time that a nonce generated by the Guacamole server
    should remain valid, in minutes. As each OpenID request has a unique nonce
    value, this imposes an upper limit on the amount of time any particular
    OpenID request can result in successful authentication within Guacamole. By
    default, each generated nonce expires after 10 minutes.

### Controlling login behavior[#](#controlling-login-behavior "Link to this heading")

Guacamole loads authentication extensions in order of priority, and evaluates
authentication attempts in this same order. This has implications for how the
Guacamole login process behaves when an SSO extension is present:

If the SSO extension has priority:
:   Users that are not yet authenticated
    will be immediately redirected to the configured identity provider. They will
    not see a Guacamole login screen.

If a non-SSO extension has priority:
:   Users that are not yet authenticated
    will be presented with a Guacamole login screen. Additionally, links to the
    configured identity provider(s) will be available for users that wish to log
    in using SSO.

The default priority of extensions is dictated by their filenames, with
extensions that sort earlier alphabetically having higher priority than others.
This can be overridden by [explicitly setting the extension
priority](configuring-guacamole.html#initial-setup).

#### Automatically redirecting all unauthenticated users[#](#automatically-redirecting-all-unauthenticated-users "Link to this heading")

To ensure users are redirected to the OpenID identity provider immediately
(without a Guacamole login screen), ensure the OpenID extension has priority
over all others:

```
extension-priority: openid
```

#### Presenting unauthenticated users with a login screen[#](#presenting-unauthenticated-users-with-a-login-screen "Link to this heading")

To ensure users are given a normal Guacamole login screen and have the option
to log in with traditional credentials *or* with OpenID, ensure the OpenID
extension does not have priority:

```
extension-priority: *, openid
```

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# Introduction

## Contents

# Introduction[#](#introduction "Link to this heading")

This book is the official Apache Guacamole manual, written by the upstream
developers of the Guacamole project. It is also the official general
documentation, with an online version available at
<http://guacamole.apache.org/>. It is a work in progress which will be
continuously updated as Guacamole changes with each release.

We decided to maintain the documentation for Guacamole as a book, as there is
an awful lot that can be done with the Guacamole web application, and even more
that can be done with the API. This book is intended to explore the
possibilities of Guacamole as an application, and to provide documentation
necessary to install, maintain, and use Guacamole.

For the sake of users and administrators, we have provided a high-level
overview of Guacamole’s architecture and technical design, as well as basic
usage instructions and installation instructions for common platforms.

For the sake of developers, we have provided a protocol reference and tutorials
for common tasks (implementing protocol support, integrating Guacamole into
your own application, etc.) to give a good starting point beyond simply looking
at the Guacamole codebase.

This particular edition of the Guacamole Manual covers Guacamole version
1.6.0. New releases which create new features or break compatibility
will result in new editions of the user’s guide, as will any necessary
corrections. As the official documentation for the project, this book will
always be freely available in its entirety online.

## What is Guacamole?[#](#what-is-guacamole "Link to this heading")

Guacamole is an HTML5 web application that provides access to desktop
environments using remote desktop protocols (such as VNC or RDP).
Guacamole is also the project that produces this web application, and
provides an API that drives it. This API can be used to power other
similar applications or services.

“Guacamole” is most commonly used to refer to the web application
produced by the Guacamole project using their API. This web application
is part of a stack that provides a protocol-agnostic remote desktop
gateway. Written in JavaScript and using only HTML5 and other standards,
the client part of Guacamole requires nothing more than a modern web
browser or web-enabled device when accessing any of the desktops served.

Historically, Guacamole was an HTML5 VNC client, and before that, a
JavaScript Telnet client called RealMint (“RealMint” is an anagram for
“terminal”), but this is no longer the case. Guacamole’s architecture
has grown to encompass remote desktop in general, and can be used as a
gateway for any number of computers. Originally a proof-of-concept,
Guacamole is now performant enough for daily use, and all Guacamole
development is done over Guacamole.

As an API, Guacamole provides a common and efficient means of streaming
text data over a JavaScript-based tunnel using either HTTP or WebSocket,
and a client implementation which supports the Guacamole protocol and
renders the remote display when combined with a Guacamole protocol
stream from the tunnel.

It provides cross-browser mouse and keyboard events, an XML-driven
on-screen keyboard, and synchronized nestable layers with
hardware-accelerated compositing. Projects that wish to provide remote
desktop support over HTML5 can leverage the years of research and
development that went into Guacamole by incorporating the API into their
application or service.

## Why use Guacamole?[#](#why-use-guacamole "Link to this heading")

The principle reason to use Guacamole is constant, world-wide,
unfettered access to your computers.

Guacamole allows access one or more desktops from anywhere remotely,
without having to install a client, particularly when installing a
client is not possible. By setting up a Guacamole server, you can
provide access to any other computer on the network from virtually any
other computer on the internet, anywhere in the world. Even mobile
phones or tablets can be used, without having to install anything.

As a true web application whose communication is over HTTP or HTTPS
only, Guacamole allows you to access your machines from anywhere without
violating the policy of your workplace, and without requiring the
installation of special clients. The presence of a proxy or corporate
firewall does not prevent Guacamole use.

## Access your computers from any device[#](#access-your-computers-from-any-device "Link to this heading")

As Guacamole requires only a reasonably-fast, standards-compliant
browser, Guacamole will run on many devices, including mobile phones and
tablets.

Guacamole is specifically designed to not care whether you have a mouse,
keyboard, touchscreen, or any combination of those.

One of the major design philosophies behind Guacamole is that it should
never assume you have a particular device (ie: a mobile phone) just
because your browser has or is missing a specific feature (ie: touch
events or a smallish screen). Guacamole’s codebase provides support for
both mouse and touch events simultaneously, without choosing one over
the other, while the interface is intended to be usable regardless of
screen size.

Barring bugs, you should be able to use Guacamole on just about any
modern device with a web browser.

## Keep a computer in the “cloud”[#](#keep-a-computer-in-the-cloud "Link to this heading")

Ignoring the buzzword, it’s often useful to have a computer that has no
dedicated physical hardware, where its processing and storage power are
handled transparently by redundant systems in some remote datacenter.

Computers hosted on virtualized hardware are more resilient to failures,
and with so many companies now offering on-demand computing resources,
Guacamole is a perfect way to access several machines that are only
accessible over the internet.

In fact, all Guacamole development is done on computers like this. This
is partly because we like the mobility, and partly because we want to
ensure Guacamole is always performant enough for daily use.

## Provide easy access to a group[#](#provide-easy-access-to-a-group "Link to this heading")

Guacamole allows you to centralize access to a large group of machines,
and specify on a per-user basis which machines are accessible. Rather
than remember a list of machines and credentials, users need only log
into a central server and click on one of the connections listed.

If you have multiple computers which you would like to access remotely,
or you are part of a group where each person has a set of machines that
they need remote access to, Guacamole is a good way to provide that
access while also ensuring that access is available from anywhere.

## Adding HTML5 remote access to your existing infrastructure[#](#adding-html5-remote-access-to-your-existing-infrastructure "Link to this heading")

As Guacamole is an API, not just a web application, the core components
and libraries provided by the Guacamole project can be used to add HTML5
remote access features to an existing application. You need not use the
main Guacamole web application; you can write (or integrate with) your
own rather easily.

If you host an on-demand computing service, adding HTML5-based remote
access allows users of your service more broad access; users need
nothing more than a web browser to see their computers’ screens.

Contents

---
# guacamole-common-js

## Contents

# guacamole-common-js[#](#guacamole-common-js "Link to this heading")

The Guacamole project provides a JavaScript API for interfacing with other
components that conform to the design of Guacamole, such as projects using
libguac or guacamole-common. This API is called guacamole-common-js.

guacamole-common-js provides a JavaScript implementation of a Guacamole client,
as well as tunneling mechanisms for getting protocol data out of JavaScript and
into guacd or the server side of a web application.

For convenience, it also provides mouse and keyboard abstraction objects that
translate JavaScript mouse, touch, and keyboard events into consistent data
that Guacamole can more easily digest. The extendable on-screen keyboard that
was developed for the Guacamole web application is also included.

## Guacamole client[#](#guacamole-client "Link to this heading")

The main benefit to using the JavaScript API is the full Guacamole client
implementation, which implements all Guacamole instructions, and makes use of
the tunnel implementations provided by both the JavaScript and Java APIs.

Using the Guacamole client is straightforward. The client, like all other
objects within the JavaScript API, is within the `Guacamole` namespace. It is
instantiated given an existing, unconnected tunnel:

```
var client = new Guacamole.Client(tunnel);
```

Once you have the client, it won’t immediately appear within the DOM. You need
to add its display element manually:

```
document.body.appendChild(client.getDisplay().getElement());
```

At this point, the client will be visible, rendering all updates as soon as
they are received through the tunnel.

```
client.connect();
```

It is possible to pass arbitrary data to the tunnel during connection which can
be used for authentication or for choosing a particular connection. When the
`connect()` function of the Guacamole client is called, it in turn calls the
`connect()` function of the tunnel originally given to the client, establishing
a connection.

Important

When creating the `Guacamole.Client`, the tunnel used must not already be
connected. The `Guacamole.Client` will call the `connect()` function for you
when its own `connect()` function is invoked. If the tunnel is already
connected when it is given to the `Guacamole.Client`, connection may not work
at all.

In general, all instructions available within the Guacamole protocol are
automatically handled by the Guacamole client, including instructions related
to audio and video. The only instructions which you must handle yourself are
“name” (used to name the connection), “clipboard” (used to update clipboard
data on the client side), and “error” (used when something goes wrong
server-side). Each of these instructions has a corresponding event handler; you
need only supply functions to handle these events. If any of these event
handlers are left unset, the corresponding instructions are simply ignored.

## HTTP tunnel[#](#http-tunnel "Link to this heading")

Both the Java and JavaScript API implement corresponding ends of an HTTP
tunnel, based on `XMLHttpRequest`.

The tunnel is a true stream - there is no polling. An initial request is made
from the JavaScript side, and this request is handled on the Java side. While
this request is open, data is streamed along the connection, and instructions
within this stream are handled as soon as they are received by the client.

While data is being streamed along this existing connection, a second
connection attempt is made. Data continues to be streamed along the original
connection until the server receives and handles the second request, at which
point the original connection closes and the stream is transferred to the new
connection.

This process repeats, alternating between active streams, thus creating an
unbroken sequence of instructions, while also allowing JavaScript to free any
memory used by the previously active connection.

The tunnel is created by supplying the relative URL to the server-side tunnel
servlet:

```
var tunnel = new Guacamole.Tunnel("tunnel");
```

Once created, the tunnel can be passed to a `Guacamole.Client` for use in a
Guacamole connection.

The tunnel actually takes care of the Guacamole protocol parsing on behalf of
the client, triggering “oninstruction” events for every instruction received,
splitting each element into elements of an array so that the client doesn’t
have to.

## Input abstraction[#](#input-abstraction "Link to this heading")

Browsers can be rather finicky when it comes to keyboard and mouse input, not
to mention touch events. There is little agreement on which keyboard events get
fired when, and what detail about the event is made available to JavaScript.
Touch and mouse events can also cause confusion, as most browsers will generate
*both* events when the user touches the screen (for compatibility with
JavaScript code that only handles mouse events), making it more difficult for
applications to support both mouse and touch independently.

The Guacamole JavaScript API abstracts mouse, keyboard, and touch interaction,
providing several helper objects which act as an abstract interface between you
and the browser events.

### Mouse[#](#mouse "Link to this heading")

Mouse event abstraction is provided by the `Guacamole.Mouse` object. Given an
arbitrary DOM element, `Guacamole.Mouse` triggers onmousedown, onmousemove, and
onmouseup events which are consistent across browsers. This object only
responds to true mouse events. Mouse events which are actually the result of
touch events are ignored.

```
var element = document.getElementById("some-arbitrary-id");
var mouse = new Guacamole.Mouse(element);

mouse.onmousedown =
mouse.onmousemove =
mouse.onmouseup   = function(state) {

    // Do something with the mouse state received ...

};
```

The handles of each event are given an instance of `Guacamole.Mouse.State`
which represents the current state of the mouse, containing the state of each
button (including the scroll wheel) as well as the X and Y coordinates of the
pointer in pixels.

### Touch[#](#touch "Link to this heading")

Touch event abstraction is provided by either `Guacamole.Touchpad` (emulates a
touchpad to generate artificial mouse events) or `Guacamole.Touchscreen`
(emulates a touchscreen, again generating artificial mouse events). Guacamole
uses the touchpad emulation, as this provides the most flexibility and
mouse-like features, including scrollwheel and clicking with different buttons,
but your preferences may differ.

```
var element = document.getElementById("some-arbitrary-id");
var touch = new Guacamole.Touchpad(element); // or Guacamole.Touchscreen

touch.onmousedown =
touch.onmousemove =
touch.onmouseup   = function(state) {

    // Do something with the mouse state received ...

};
```

Note that even though these objects are touch-specific, they still provide
mouse events. The state object given to the event handlers of each event is
still an instance of `Guacamole.Mouse.State`.

Ultimately, you could assign the same event handler to all the events of both
an instance of `Guacamole.Mouse` as well as `Guacamole.Touchscreen` or
`Guacamole.Touchpad`, and you would magically gain mouse and touch support.
This support, being driven by the needs of remote desktop, is naturally geared
around the mouse and providing a reasonable means of interacting with it. For
an actual mouse, events are translated simply and literally, while touch events
go through additional emulation and heuristics. From the perspective of the
user and the code, this is all transparent.

### Keyboard[#](#keyboard "Link to this heading")

Keyboard events in Guacamole are abstracted with the `Guacamole.Keyboard`
object as only keyup and keydown events; there is no keypress like there is in
JavaScript. Further, all the craziness of keycodes vs. scancodes vs. key
identifiers normally present across browsers is abstracted away. All your event
handlers will see is an X11 keysym, which represent every key unambiguously.
Conveniently, X11 keysyms are also what the Guacamole protocol requires, so if
you want to use `Guacamole.Keyboard` to drive key events sent over the
Guacamole protocol, everything can be connected directly.

Just like the other input abstraction objects, `Guacamole.Keyboard` requires a
DOM element as an event target. Only key events directed at this element will
be handled.

```
var keyboard = new Guacamole.Keyboard(document);

keyboard.onkeydown = function(keysym) {
    // Do something ...
};

keyboard.onkeyup = function(keysym) {
    // Do something ...
};
```

In this case, we are using `document` as the event target, thus receiving all
key events while the browser window (or tab) has focus.

## On-screen keyboard[#](#on-screen-keyboard "Link to this heading")

The Guacamole JavaScript API also provides an extendable on-screen keyboard,
`Guacamole.OnScreenKeyboard`, which requires the URL of an XML file describing
the keyboard layout. The on-screen keyboard object provides no hard-coded
layout information; the keyboard layout is described entirely within the XML
layout file.

### Keyboard layouts[#](#keyboard-layouts "Link to this heading")

The keyboard layout XML included in the Guacamole web application would be a
good place to start regarding how these layout files are written, but in
general, the keyboard is simply a set of rows or columns, denoted with `<row>`
and `<column>` tags respectively, where each can be nested within the other as
desired.

Each key is represented with a `<key>` tag, but this is not what the user sees,
nor what generates the key event. Each key contains any number of `<cap>` tags,
which represent the visible part of the key. The cap describes which X11
keysym will be sent when the key is pressed. Each cap can be associated with
any combination of arbitrary modifier flags which dictate when that cap is
active.

For example:

```
<keyboard lang="en_US" layout="example" size="5">
    <row>
        <key size="4">
            <cap modifier="shift" keysym="0xFFE1">Shift</cap>
        </key>
        <key>
            <cap>a</cap>
            <cap if="shift">A</cap>
        </key>
    </row>
</keyboard>
```

Here we have a very simple keyboard which defines only two keys: “shift” (a
modifier) and the letter “a”. When “shift” is pressed, it sets the “shift”
modifier, affecting other keys in the keyboard. The “a” key has two caps: one
lowercase (the default) and one uppercase (which requires the shift modifier to
be active).

Notice that the shift key needed the keysym explicitly specified, while the “a”
key did not. This is because the on-screen keyboard will automatically derive
the correct keysym from the text of the key cap if the text contains only a
single character.

### Displaying the keyboard[#](#displaying-the-keyboard "Link to this heading")

Once you have a keyboard layout available, adding an on-screen keyboard to your
application is simple:

```
// Add keyboard to body
var keyboard = new Guacamole.OnScreenKeyboard("path/to/layout.xml");
document.body.appendChild(keyboard.getElement());

// Set size of keyboard to 100 pixels
keyboard.resize(100);
```

Here, we have explicitly specified the width of the keyboard as 100 pixels.
Normally, you would determine this by inspecting the width of the containing
component, or by deciding on a reasonable width beforehand. Once the width is
given, the height of the keyboard is determined based on the arrangement of
each row.

### Styling the keyboard[#](#styling-the-keyboard "Link to this heading")

While the `Guacamole.OnScreenKeyboard` object will handle most of the layout,
you will still need to style everything yourself with CSS to get the elements
to render properly and the keys to change state when clicked or activated. It
defines several CSS classes, which you will need to manually style to get
things looking as desired:

`guac-keyboard`
:   This class is assigned to the root element containing the entire keyboard,
    returned by `getElement()`,

`guac-keyboard-row`
:   Assigned to the `div` elements which contain each row.

`guac-keyboard-column`
:   Assigned to the `div` elements which contain each column.

`guac-keyboard-gap`
:   Assigned to any `div` elements created as a result of `<gap>` tags in the
    keyboard layout. `<gap>` tags are intended to behave as keys with no visible
    styling or caps.

`guac-keyboard-key-container`
:   Assigned to the `div` element which contains a key, and provides that key
    with its required dimensions. It is this element that will be scaled relative
    to the size specified in the layout XML and the size given to the `resize()`
    function.

`guac-keyboard-key`
:   Assigned to the `div` element which represents the actual key, not the cap.
    This element will not directly contain text, but it will contain all caps
    that this key can have. With clever CSS rules, you can take advantage of this
    and cause inactive caps to appear on the key in a corner (for example), or
    hide them entirely.

`guac-keyboard-cap`
:   Assigned to the `div` element representing a key cap. Each cap is a child of
    its corresponding key, and it is up to the author of the CSS rules to hide or
    show or reposition each cap appropriately. Each cap will contain the display
    text defined within the `<cap>` element in the layout XML.

`guac-keyboard-requires-MODIFIER`
:   Added to the cap element when that cap requires a specific modifier.

`guac-keyboard-uses-MODIFIER`
:   Added to the key element when any cap contained within it requires a specific
    modifier.

`guac-keyboard-modifier-MODIFIER`
:   Added to and removed from the root keyboard element when a modifier key is
    activated or deactivated respectively.

`guac-keyboard-pressed`
:   Added to and removed from any key element as it is pressed and released
    respectively.

Important

The CSS rules required for the on-screen keyboard to work as expected can be
quite complex. Looking over the CSS rules used by the on-screen keyboard in the
Guacamole web application would be a good place to start to see how the
appearance of each key can be driven through the simple class changes described
above.

Inspecting the elements of an active on-screen keyboard within the Guacamole
web application with the developer tools of your favorite browser is also a
good idea.

### Handling key events[#](#handling-key-events "Link to this heading")

Key events generated by the on-screen keyboard are identical to those of
`Guacamole.Keyboard` in that they consist only of a single X11 keysym. Only
keyup and keydown events exist, as before; there is no keypress event.

```
// Assuming we have an instance of Guacamole.OnScreenKeyboard already
// called "keyboard"

keyboard.onkeydown = function(keysym) {
    // Do something ...
};

keyboard.onkeyup = function(keysym) {
    // Do something ...
};
```

Contents

---
# Installing Guacamole

# Installing Guacamole[#](#installing-guacamole "Link to this heading")

There are two supported ways of installing Guacamole:

[Installing Guacamole natively](guacamole-native.html)
:   This involves installing a servlet container like [Apache Tomcat](https://tomcat.apache.org/),
    deploying the Guacamole web application beneath Tomcat, and building at least
    guacamole-server from source.

[Installing Guacamole using Docker containers](guacamole-docker.html)
:   This involves running a pair of Docker containers using the provided
    `guacamole/guacamole` and `guacamole/guacd` Docker images.

A typical, standard installation of Guacamole is configured to [use a database
for storage and/or authentication](jdbc-auth.html). This provides the most features
and flexibility, and enables a convenient [web-based administrative
interface](administration.html).

Other, more complex authentication methods which use [LDAP](ldap-auth.html), various
[multi-factor authentication](mfa.html) and [single sign-on options](sso.html), etc. are
discussed in a separate, dedicated chapters.

Note

There is also a “default” authentication method that reads all users and
connections from a single file called [`user-mapping.xml`](configuring-guacamole.html#user-mapping). This
simpler, built-in authentication method is not intended for production use, but
rather to serve as a relatively-easy means of verifying that Guacamole has been
properly set up.

It’s reasonable to use this XML-based method for small deployments that don’t
need the full feature set of Guacamole, but **the goal should always be to
migrate to a production-ready mechanism like [using a database](jdbc-auth.html)**.
We do not recommend using `user-mapping.xml` for production or anything
public-facing.

---
# RADIUS authentication

## Contents

# RADIUS authentication[#](#radius-authentication "Link to this heading")

Guacamole supports delegating authentication to a RADIUS service, such as
FreeRADIUS, to validate username and password combinations, and to support
multi-factor authentication. This authentication method must be layered on top
of some other authentication extension, such as those available from the main
project website, in order to provide access to actual connections.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Building the RADIUS authentication extension[#](#building-the-radius-authentication-extension "Link to this heading")

The RADIUS extension depends on software that is covered by a LGPL license,
which is incompatible with the Apache 2.0 license under which Guacamole is
licensed. Due to this dependency, the Guacamole project cannot distribute
binary versions of the RADIUS extension. If you want to use this extension you
will need to build the RADIUS extension from source, either by [building
guacamole-client from source using Maven](guacamole-native.html#building-guacamole-client) or by
manually building the guacamole-client Docker image.

Native Webapp (Tomcat)

The RADIUS extension must be explicitly enabled during build time in order to
generate the binaries and resulting JAR file. This is done by adding the flag
`-Plgpl-extensions` to the Maven command line during the build, and should
result in the output below:

```
$ mvn -Plgpl-extensions clean package
[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Build Order:
[INFO] 
[INFO] guacamole-client                                                   [pom]
[INFO] guacamole-common                                                   [jar]
[INFO] guacamole-ext                                                      [jar]
...
[INFO] guacamole-auth-radius                                              [jar]
...
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary for guacamole-client 1.6.0:
[INFO] 
[INFO] guacamole-client ................................... SUCCESS [ 12.839 s]
[INFO] guacamole-common ................................... SUCCESS [ 15.446 s]
[INFO] guacamole-ext ...................................... SUCCESS [ 19.988 s]
...
[INFO] guacamole-auth-radius .............................. SUCCESS [ 10.806 s]
...
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  04:36 min
[INFO] Finished at: 2023-01-10T17:27:11-08:00
[INFO] ------------------------------------------------------------------------
$
```

After the build completes successfully, the extension will be in the
`extensions/guacamole-auth-radius/target/` directory, and will be called
`guacamole-auth-radius-1.6.0.jar`.

To install the RADIUS authentication extension, you must:

1. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
2. Copy `guacamole-auth-radius-1.6.0.jar` into `GUACAMOLE_HOME/extensions`.
3. Configure Guacamole to use RADIUS authentication, as described below.

Container (Docker)

To build a copy of the `guacamole/guacamole` Docker image with RADIUS support,
the `-Plgpl-extensions` option must be passed to the Docker build process using
the `MAVEN_ARGUMENTS` build argument. The `-DskipTests=true` argument must also
be included, as the build otherwise performs several JavaScript unit tests that
cannot run in a containerized environment:

```
$ docker build \
    --build-arg MAVEN_ARGUMENTS="-Plgpl-extensions -DskipTests=true" \
    -t guacamole/guacamole .
```

Once the build completes, you can use your copy of the `guacamole/guacamole`
image as you would the standard image provided with each Guacamole release.

## Configuration[#](#configuration "Link to this heading")

Native Webapp (Tomcat)

`radius-hostname`
:   The RADIUS server to authenticate against. If not specified, localhost will
    be used.

`radius-auth-port`
:   The RADIUS authentication port on which the RADIUS service is is listening.
    If not specified, the default of 1812 will be used.

`radius-shared-secret`
:   The shared secret to use when talking to the RADIUS server. This parameter is
    required and the extension will not load if this is not specified.

`radius-auth-protocol`
:   The authentication protocol to use when talking to the RADIUS server. This
    parameter is required for the extension to operate. Supported values are:
    pap, chap, mschapv1, mschapv2, eap-md5, eap-tls, and eap-ttls. Support for
    PEAP is implemented inside the extension, but, due to a regression in the
    JRadius implementation, it is currently broken. Also, if you specify eap-ttls
    you will also need to specify the `radius-eap-ttls-inner-protocol` parameter
    in order to properly configure the protocol used inside the EAP TTLS tunnel.

`radius-key-file`
:   The combination certificate and private key pair to use for TLS-based RADIUS
    protocols that require a client-side certificate. This parameter should specify
    the absolute path to the file. By default the extension will look for a file
    called `radius.key` in the `GUACAMOLE_HOME` directory.

`radius-key-type`
:   The file type of the keystore specified by the `radius-key-file` parameter.
    Valid keystore types are pem, jceks, jks, and pkcs12. If not specified, this
    defaults to pkcs12, the default used by the JRadius library.

`radius-key-password`
:   The password of the private key specified in the `radius-key-file` parameter.
    By default the extension will not use any password when trying to open the
    key file.

`radius-ca-file`
:   The absolute path to the file that stores the certificate authority
    certificates for encrypted connections to the RADIUS server. By default a
    file with the name ca.crt in the `GUACAMOLE_HOME` directory will be used.

`radius-ca-type`
:   The file type of the keystore used for the certificate authority. Valid
    formats are pem, jceks, jks, and pkcs12. If not specified this defaults to
    pem.

`radius-ca-password`
:   The password used to protect the certificate authority store, if any. If
    unspecified the extension will attempt to read the CA store without any
    password.

`radius-trust-all`
:   This parameter controls whether or not the RADIUS extension should trust all
    certificates or verify them against known good certificate authorities. Set
    to true to allow the RADIUS server to connect without validating
    certificates. The default is false, which causes certificates to be
    validated.

`radius-retries`
:   The number of times the client will retry the connection to the RADIUS server
    and not receive a response before giving up. By default the client will try
    the connection at most 5 times.

`radius-timeout`
:   The timeout for a RADIUS connection in seconds. By default the client will
    wait for a response from the server for at most 60 seconds.

`radius-eap-ttls-inner-protocol`
:   When EAP-TTLS is used, this parameter specifies the inner (tunneled) protocol
    to use talking to the RADIUS server. It is required when the
    `radius-auth-protocol` parameter is set to eap-ttls. If the
    `radius-auth-protocol` value is set to something other than eap-ttls, this
    parameter has no effect and will be ignored. Valid options for this are any of
    the values for `radius-auth-protocol`, except for eap-ttls.

`radius-nas-ip`
:   This property allows the server administrator to manually set an IP address
    that will be sent to the RADIUS server to identify this RADIUS client, known
    as the “Network Access Server” (NAS) IP address. When this property is not
    specified, the RADIUS extension attempts to automatically determine the IP
    address of the system on which Guacamole is running and uses that value.

Container (Docker)

`RADIUS_HOSTNAME`
:   The RADIUS server to authenticate against. If not specified, localhost will
    be used.

`RADIUS_AUTH_PORT`
:   The RADIUS authentication port on which the RADIUS service is is listening.
    If not specified, the default of 1812 will be used.

`RADIUS_SHARED_SECRET`
:   The shared secret to use when talking to the RADIUS server. This parameter is
    required and the extension will not load if this is not specified.

`RADIUS_AUTH_PROTOCOL`
:   The authentication protocol to use when talking to the RADIUS server. This
    parameter is required for the extension to operate. Supported values are:
    pap, chap, mschapv1, mschapv2, eap-md5, eap-tls, and eap-ttls. Support for
    PEAP is implemented inside the extension, but, due to a regression in the
    JRadius implementation, it is currently broken. Also, if you specify eap-ttls
    you will also need to specify the `radius-eap-ttls-inner-protocol` parameter
    in order to properly configure the protocol used inside the EAP TTLS tunnel.

`RADIUS_KEY_FILE`
:   The combination certificate and private key pair to use for TLS-based RADIUS
    protocols that require a client-side certificate. This parameter should specify
    the absolute path to the file. By default the extension will look for a file
    called `radius.key` in the `GUACAMOLE_HOME` directory.

`RADIUS_KEY_TYPE`
:   The file type of the keystore specified by the `radius-key-file` parameter.
    Valid keystore types are pem, jceks, jks, and pkcs12. If not specified, this
    defaults to pkcs12, the default used by the JRadius library.

`RADIUS_KEY_PASSWORD`
:   The password of the private key specified in the `radius-key-file` parameter.
    By default the extension will not use any password when trying to open the
    key file.

`RADIUS_CA_FILE`
:   The absolute path to the file that stores the certificate authority
    certificates for encrypted connections to the RADIUS server. By default a
    file with the name ca.crt in the `GUACAMOLE_HOME` directory will be used.

`RADIUS_CA_TYPE`
:   The file type of the keystore used for the certificate authority. Valid
    formats are pem, jceks, jks, and pkcs12. If not specified this defaults to
    pem.

`RADIUS_CA_PASSWORD`
:   The password used to protect the certificate authority store, if any. If
    unspecified the extension will attempt to read the CA store without any
    password.

`RADIUS_TRUST_ALL`
:   This parameter controls whether or not the RADIUS extension should trust all
    certificates or verify them against known good certificate authorities. Set
    to true to allow the RADIUS server to connect without validating
    certificates. The default is false, which causes certificates to be
    validated.

`RADIUS_RETRIES`
:   The number of times the client will retry the connection to the RADIUS server
    and not receive a response before giving up. By default the client will try
    the connection at most 5 times.

`RADIUS_TIMEOUT`
:   The timeout for a RADIUS connection in seconds. By default the client will
    wait for a response from the server for at most 60 seconds.

`RADIUS_EAP_TTLS_INNER_PROTOCOL`
:   When EAP-TTLS is used, this parameter specifies the inner (tunneled) protocol
    to use talking to the RADIUS server. It is required when the
    `radius-auth-protocol` parameter is set to eap-ttls. If the
    `radius-auth-protocol` value is set to something other than eap-ttls, this
    parameter has no effect and will be ignored. Valid options for this are any of
    the values for `radius-auth-protocol`, except for eap-ttls.

`RADIUS_NAS_IP`
:   This property allows the server administrator to manually set an IP address
    that will be sent to the RADIUS server to identify this RADIUS client, known
    as the “Network Access Server” (NAS) IP address. When this property is not
    specified, the RADIUS extension attempts to automatically determine the IP
    address of the system on which Guacamole is running and uses that value.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# HTTP header authentication

## Contents

# HTTP header authentication[#](#http-header-authentication "Link to this heading")

Guacamole supports delegating authentication to an arbitrary external service,
relying on the presence of an HTTP header which contains the username of the
authenticated user. This authentication method must be layered on top of some
other authentication extension, such as those available from the main project
website, in order to provide access to actual connections.

Danger

**All external requests must be properly sanitized if this extension is used.**
The chosen HTTP header must be stripped from untrusted requests, such that the
authentication service is the *only* possible source of that header.

**If such sanitization is not performed, it will be trivial for malicious users
to add this header manually, and thus gain unrestricted access.**

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling HTTP header authentication[#](#installing-enabling-http-header-authentication "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-header-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-header-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-header-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `HTTP_AUTH_ENABLED` environment variable:

    ```
    HTTP_AUTH_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e HTTP_AUTH_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `HTTP_AUTH_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `HTTP_AUTH_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Configuration (optional)[#](#configuration-optional "Link to this heading")

Native Webapp (Tomcat)

This extension has no required properties. So long as you are satisfied
with the default behavior/values noted below, this extension requires no
configuration beyond installation.

`http-auth-header`
:   The HTTP header containing the username of the authenticated user.

    This property is optional. If not specified, `REMOTE_USER` will be used by
    default. If your authentication system uses a different HTTP header you can
    use this option to override it and specify the header for Guacamole to
    expect.

Container (Docker)

This extension has no required environment variables. So long as you are satisfied
with the default behavior/values noted below, this extension requires no
configuration beyond installation.

`HTTP_AUTH_HEADER`
:   The HTTP header containing the username of the authenticated user.

    This property is optional. If not specified, `REMOTE_USER` will be used by
    default. If your authentication system uses a different HTTP header you can
    use this option to override it and specify the header for Guacamole to
    expect.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# The Guacamole protocol

## Contents

# The Guacamole protocol[#](#the-guacamole-protocol "Link to this heading")

This chapter is an overview of the Guacamole protocol, describing its design
and general use. While a few instructions and their syntax will be described
here, this is not an exhaustive list of all available instructions. The intent
is only to list the general types and usage. If you are looking for the syntax
or purpose of a specific instruction, consult the protocol reference included
with the appendices.

## Design[#](#design "Link to this heading")

The Guacamole protocol consists of instructions. Each instruction is a
comma-delimited list followed by a terminating semicolon, where the first
element of the list is the instruction opcode, and all following elements are
the arguments for that instruction:

```
OPCODE,ARG1,ARG2,ARG3,...;
```

Each element of the list has a positive decimal integer length prefix separated
by the value of the element by a period. This length denotes the number of
Unicode characters in the value of the element, which is encoded in UTF-8:

```
LENGTH.VALUE
```

Any number of complete instructions make up a message which is sent from client
to server or from server to client. Client to server instructions are generally
control instructions (for connecting or disconnecting) and events (mouse and
keyboard). Server to client instructions are generally drawing instructions
(caching, clipping, drawing images), using the client as a remote display.

For example, a complete and valid instruction for setting the display size to
1024x768 would be:

```
4.size,1.0,4.1024,3.768;
```

Here, the instruction would be decoded into four elements: “size”, the opcode
of the size instruction, “0”, the index of the default layer, “1024”, the
desired width in pixels, and “768”, the desired height in pixels.

The structure of the Guacamole protocol is important as it allows the protocol
to be streamed while also being easily parsable by JavaScript. JavaScript does
have native support for conceptually-similar structures like XML or JSON, but
neither of those formats is natively supported in a way that can be streamed;
JavaScript requires the entirety of the XML or JSON message to be available at
the time of decoding. The Guacamole protocol, on the other hand, can be parsed
as it is received, and the presence of length prefixes within each instruction
element means that the parser can quickly skip around from instruction to
instruction without having to iterate over every character.

## Handshake phase[#](#handshake-phase "Link to this heading")

The handshake phase is the phase of the protocol entered immediately upon
connection. It begins with a “select” instruction sent by the client which
tells the server which protocol will be loaded:

```
6.select,3.vnc;
```

After receiving the “select” instruction, the server will load the associated
client support and respond with its protocol version and a list of accepted
parameter names using an “args” instruction:

```
4.args,13.VERSION_1_1_0,8.hostname,4.port,8.password,13.swap-red-blue,9.read-only;
```

The protocol version is used to negotiate compatibility between differing
versions of client and server, allowing the two sides to negotiate the highest
supported version and enable or disable features associated with that version.
Older implementations of the Guacamole protocol that do not support version
negotiation will silently ignore it as if it were an unspecified connection
parameter.

Valid protocol versions are as follows:

`VERSION_1_5_0`
:   Protocol version 1.5.0 introduced two new instructions - the `msg`
    instruction, which is used to send arbitrary messages to the client, and
    the `name` handshake instruction, which allows the client to set the
    human-readable name of the user joining a connection.

`VERSION_1_3_0`
:   Protocol version 1.3.0 introduced the `require` instruction, used by the
    server to indicate that the client must provide additional arguments (such
    as a username and password).

`VERSION_1_1_0`
:   Protocol version 1.1.0 introduced support for protocol version
    negotiation, arbitrary order of the handshake instructions, and support
    for passing the timezone instruction during the handshake.

`VERSION_1_0_0`
:   This is the default version and applies to any versions prior to 1.1.0.
    Version 1.0.0 of the protocol does not support protocol negotiation, and
    requires that the handshake instructions are delivered in a certain order,
    and that they are present (even if empty).

After receiving the list of arguments, the client is required to respond with
the list of supported audio, video, and image mimetypes, the optimal display
size and resolution, and the values for all arguments available, even if blank.

```
4.size,4.1024,3.768,2.96;
5.audio,9.audio/ogg;
5.video;
5.image,9.image/png,10.image/jpeg;
8.timezone,16.America/New_York;
7.connect,13.VERSION_1_1_0,9.localhost,4.5900,0.,0.,0.;
```

For clarity, we’ve put each instruction on its own line, but in the real
protocol, no newlines exist between instructions. In fact, if there is anything
after an instruction other than the start of a new instruction, the connection
is closed.

The following are valid instructions during the handshake:

`audio`
:   The audio codec(s) supported by the client. In the example above the
    client is specifying audio/ogg as the supported codec.

`connect`
:   This is the final instruction of the handshake, terminating the handshake
    and indicating that the connection should continue. This instruction has
    as its parameters values for the connection parameters sent by the server
    in the `args` instruction. In the example above, this is connection to
    localhost on port 5900, with no values for the last three connection
    parameters.

`image`
:   The image formats that the client supports, in order of preference. The
    client in the example above is supporting both PNG and JPEG.

`name`
:   The human-readable name of the user joining the connection.

`timezone`
:   The timezone of the client, in IANA zone key format. More information on
    this instruction is available in [Configuring Guacamole](configuring-guacamole.html), under
    documentation related to the `timezone` connection parameters for the
    protocols that support it.

`video`
:   The video codec(s) supported by the client. The above example is a client
    that does not support any video codecs.

The order of the instructions sent by the client in the handshake is arbitrary,
with the exception that the final instruction, connect, will end the handshake
and attempt to start the connection.

Once these instructions have been sent by the client, the server will attempt
to initialize the connection with the parameters received and, if successful,
respond with a “ready” instruction. This instruction contains the ID of the new
client connection and marks the beginning of the interactive phase. The ID is
an arbitrary string, but is guaranteed to be unique from all other active
connections, as well as from the names of all supported protocols:

```
5.ready,37.$260d01da-779b-4ee9-afc1-c16bae885cc7;
```

The actual interactive phase begins immediately after the “ready” instruction
is sent. Drawing and event instructions pass back and forth until the
connection is closed.

### Joining an existing connection[#](#joining-an-existing-connection "Link to this heading")

Once the handshake phase has completed, that connection is considered active
and can be joined by other connections if the ID is provided instead of a
protocol name via the “select” instruction:

```
6.select,37.$260d01da-779b-4ee9-afc1-c16bae885cc7;
```

The rest of the handshake phase for a joining connection is identical. Just as
with a new connection, the restrictions or features which apply to the joining
connection are dictated by the parameter values supplied during the handshake.

## Drawing[#](#drawing "Link to this heading")

### Compositing[#](#compositing "Link to this heading")

The Guacamole protocol provides compositing operations through the use of
“channel masks”. The term “channel mask” is simply a description of the
mechanism used while designing the protocol to conceptualize and fully
enumerate all possible compositing operations based on four different sources
of image data: source image data where the destination is opaque, source image
data where the destination is transparent, destination image data where the
source is opaque, and destination image data where the source is transparent.
Assigning a binary value to each of these “channels” creates a unique integer
ID for every possible compositing operation, where these operations parallel
the operations described by Porter and Duff in their paper. As the HTML5 canvas
tag also uses Porter/Duff to describe their compositing operations (as do other
graphical APIs), the Guacamole protocol is conveniently similar to the
compositing support already present in web browsers, with some operations not
yet supported. The following operations are all implemented and known to work
correctly in all browsers:

B out A (0x02)
:   Clears the destination where the source is opaque, but otherwise draws
    nothing. This is useful for masking.

A atop B (0x06)
:   Fills with the source where the destination is opaque only.

A xor B (0x0A)
:   As with logical XOR. Note that this is a compositing operation, not a
    bitwise operation. It draws the source where the destination is
    transparent, and draws the destination where the source is transparent.

B over A (0x0B)
:   What you would typically expect when drawing, but reversed. The source
    appears only where the destination is transparent, as if you were
    attempting to draw the destination over the source, rather than the source
    over the destination.

A over B (0x0E)
:   The most common and sensible compositing operation, this draws the source
    everywhere, but includes the destination where the source is transparent.

A + B (0x0F)
:   Simply adds the components of the source image to the destination image,
    capping the result at pure white.

The following operations are all implemented, but may work incorrectly in
WebKit browsers which always include the destination image where the source is
transparent:

B in A (0x01)
:   Draws the destination only where the source is opaque, clearing anywhere
    the source or destination are transparent.

A in B (0x04)
:   Draws the source only where the destination is opaque, clearing anywhere
    the source or destination are transparent.

A out B (0x08)
:   Draws the source only where the destination is transparent, clearing
    anywhere the source or destination are opaque.

B atop A (0x09)
:   Fills with the destination where the source is opaque only.

A (0x0C)
:   Fills with the source, ignoring the destination entirely.

The following operations are defined, but not implemented, and do not exist as
operations within the HTML5 canvas:

Clear (0x00)
:   Clears all existing image data in the destination.

B (0x03)
:   Does nothing.

A xnor B (0x05)
:   Adds the source to the destination where the destination or source are
    opaque, clearing anywhere the source or destination are transparent. This
    is similar to A + B except the aspect of transparency is also additive.

(A + B) atop B (0x07)
:   Adds the source to the destination where the destination is opaque,
    preserving the destination otherwise.

(A + B) atop A (0x0D)
:   Adds the destination to the source where the source is opaque, copying the
    source otherwise.

### Image data[#](#image-data "Link to this heading")

The Guacamole protocol, like many remote desktop protocols, provides a method
of sending an arbitrary rectangle of image data and placing it either within a
buffer or in a visible rectangle of the screen. Raw image data in the Guacamole
protocol is streamed as PNG, JPEG, or WebP data over a stream allocated with
the “img” instruction. Depending on the format used, image updates sent in this
manner can be RGB or RGBA (alpha transparency) and are automatically palettized
if sent using libguac. The streaming system used for image data is generalized
and used by Guacamole for other types of streams, including audio and file
transfer. For more information about streams in the Guacamole protocol, see
[Streams and objects](#guacamole-protocol-streaming).

Image data can be sent to any specified rectangle within a layer or buffer.
Sending the data to a layer means that the image becomes immediately visible,
while sending the data to a buffer allows that data to be reused later.

### Copying image data between layers[#](#copying-image-data-between-layers "Link to this heading")

Image data can be copied from one layer or buffer into another layer or buffer.
This is often used for scrolling (where most of the result of the graphical
update is identical to the previous state) or for caching parts of an image.

Both VNC and RDP provide a means of copying a region of screen data and placing
it somewhere else within the same screen. RDP provides an additional means of
copying data to a cache, or recalling data from that cache and placing it on
the screen. Guacamole takes this concept and reduces it further, as both
on-screen and off-screen image storage is the same. The Guacamole “copy”
instruction allows you to copy a rectangle of image data, and place it within
another layer, whether that layer is the same as the source layer, a different
visible layer, or an off-screen buffer.

### Graphical primitives[#](#graphical-primitives "Link to this heading")

The Guacamole protocol provides basic graphics operations similar to those of
Cairo or the HTML5 canvas. In many cases, these primitives are useful for
remote drawing, and desirable in that they take up less bandwidth than sending
corresponding PNG images. Beware that excessive use of primitives leads to an
increase in client-side processing, which may reduce the performance of a
connected client, especially if that client is on a lower-performance machine
like a mobile phone or tablet.

### Buffers and layers[#](#buffers-and-layers "Link to this heading")

All drawing operations in the Guacamole protocol affect a layer, and each layer
has an integer index which identifies it. When this integer is negative, the
layer is not visible, and can be used for storage or caching of image data. In
this case, the layer is referred to within the code and within documentation as
a “buffer”. Layers are created automatically when they are first referenced in
an instruction.

There is one main layer which is always present called the “default layer”.
This layer has an index of 0. Resizing this layer resizes the entire remote
display. Other layers default to the size of the default layer upon creation,
while buffers are always created with a size of 0x0, automatically resizing
themselves to fit their contents.

Non-buffer layers can be moved and nested within each other. In this way,
layers provide a simple means of hardware-accelerated compositing. If you need
a window to appear above others, or you have some object which will be moving
or you need the data beneath it automatically preserved, a layer is a good way
of accomplishing this. If a layer is nested within another layer, its position
is relative to that of its parent. When the parent is moved or reordered, the
child moves with it. If the child extends beyond the parents bounds, it will
be clipped.

## Streams and objects[#](#streams-and-objects "Link to this heading")

Guacamole supports transfer of clipboard contents, audio, video, and image
data, as well as files and arbitrary named pipes.

Streams are allocated directly with instructions that associate the new stream
with particular semantics and metadata, such as the “audio” or “video”
instructions used for playing media, the “file” instruction used for file
transfer, and the “pipe” instruction for transfer of completely arbitrary data
between client and server. In some cases, the availability and semantics of
streams may be explicitly advertised using structured sets of named streams
known as “objects”.

Once a stream is allocated, data is sent along the stream in chunks using
“blob” instructions, which may be acknowledged by the receiving end by “ack”
instructions. The end of the stream is finally signalled with an “end”
instruction.

## Events[#](#events "Link to this heading")

When something changes on either side, client or server, such as a key being
pressed, the mouse moving, or clipboard data changing, an instruction
describing the event is sent.

## Disconnecting[#](#disconnecting "Link to this heading")

The server and client can end the connection at any time. There is no
requirement for the server or the client to communicate that the connection
needs to terminate. When the client or server wish to end the connection, and
the reason is known, they can use the “disconnect” or “error” instructions.

The disconnect instruction is sent by the client when it is disconnecting. This
is largely out of politeness, and the server must be written knowing that the
disconnect instruction may not always be sent in time (guacd is written this
way).

If the client does something wrong, or the server detects a problem with the
client plugin, the server sends an error instruction, including a description
of the problem in the parameters. This informs the client that the connection
is being closed.

Contents

---
# Adding new protocols

## Contents

# Adding new protocols[#](#adding-new-protocols "Link to this heading")

Guacamole’s support for multiple remote desktop protocols is provided through
plugins which guacd loads dynamically. The Guacamole API has been designed such
that protocol support is easy to create, especially when a C library exists
providing a basic client implementation.

In this tutorial, we will implement a simple “client” which renders a bouncing
ball using the Guacamole protocol. After completing the tutorial and installing
the result, you will be able to add a connection to your Guacamole
configuration using the “ball” protocol, and any users using that connection
will see a bouncing ball.

This example client plugin doesn’t actually act as a client, but this isn’t
important. The Guacamole client is really just a remote display, and this
client plugin functions as a simple example application which renders to this
display, just as Guacamole’s own VNC or RDP plugins function as VNC or RDP
clients which render to the remote display.

Each step of this tutorial is intended to exercise a new concept, while also
progressing towards the goal of a nifty bouncing ball. At the end of each step,
you will have a buildable and working client plugin.

This tutorial will use the GNU Automake build system, which is the build system
used by Guacamole for libguac, guacd, etc. There will be four files involved:

`configure.ac`
:   Used by GNU Automake to generate the `configure` script which ultimately
    serves to generate the `Makefile` which **make** will use when
    building.

`Makefile.am`
:   Used by GNU Automake and the `configure` script to generate the `Makefile`
    which **make** will use when building.

`src/ball.c`
:   The main body of code defining the bouncing ball “client”.

`src/ball.h`
:   A header file defining the structure representing the state of the bouncing
    ball (once it becomes necessary to do so).

All source files will be within the `src` subdirectory, as is common with C
projects, with build files being at the root level directory. The main
`src/ball.c` and the build-related `configure.ac` and `Makefile.am` files will
be created first, with each successive step building upon those files
iteratively, with `src/ball.h` being added when it becomes necessary. After
each step, you can build/rebuild the plugin by running **make**, and
then install it (such that guacd can find the plugin) by running **make install** and **ldconfig** as root:

```
$ make
  CC       src/ball.lo
  CCLD     libguac-client-ball.la
# make install
make[1]: Entering directory '/home/user/libguac-client-ball'
 /usr/bin/mkdir -p '/usr/local/lib'
 /bin/sh ./libtool   --mode=install /usr/bin/install -c   libguac-client-ball.la '/usr/local/lib'
...
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/lib

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the '-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the 'LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the 'LD_RUN_PATH' environment variable
     during linking
   - use the '-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to '/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
make[1]: Nothing to be done for 'install-data-am'.
make[1]: Leaving directory '/home/user/libguac-client-ball'
# ldconfig
```

Prior to the first time **make** is invoked, you will need to run the
`configure` script, which will first need to be generated using
**autoreconf**:

```
$ autoreconf -fi
libtoolize: putting auxiliary files in '.'.
libtoolize: copying file './ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'm4'.
libtoolize: copying file 'm4/libtool.m4'
libtoolize: copying file 'm4/ltoptions.m4'
libtoolize: copying file 'm4/ltsugar.m4'
libtoolize: copying file 'm4/ltversion.m4'
libtoolize: copying file 'm4/lt~obsolete.m4'
configure.ac:10: installing './compile'
configure.ac:4: installing './missing'
Makefile.am: installing './depcomp'
$ ./configure
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
...
configure: creating ./config.status
config.status: creating Makefile
config.status: executing depfiles commands
config.status: executing libtool commands
$
```

This process is almost identical to that of building guacamole-server from git,
as documented in [Building guacamole-server](guacamole-native.html#building-guacamole-server).

Important

The libguac library which is part of guacamole-server is a required dependency
of this project. *You must first install libguac, guacd, etc. by [building and
installing guacamole-server](guacamole-native.html#building-guacamole-server)*. If guacamole-server
has not been installed, and libguac is thus not present, the `configure` script
will fail with an error indicating that it could not find libguac:

```
$ ./configure
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
...
checking for guac_client_stream_png in -lguac... no
configure: error: "libguac is required for communication via "
                   "the Guacamole protocol"
$
```

You will need to install guacamole-server and then rerun `configure`.

## Minimal skeleton client[#](#minimal-skeleton-client "Link to this heading")

Very little needs to be done to implement the most basic client plugin
possible. We begin with `src/ball.c`, containing the absolute minimum required
for a client plugin:

```
#include <guacamole/client.h>

#include <stdlib.h>

/* Client plugin arguments (empty) */
const char* TUTORIAL_ARGS[] = { NULL };

int guac_client_init(guac_client* client) {

    /* This example does not implement any arguments */
    client->args = TUTORIAL_ARGS;

    return 0;

}
```

Notice the structure of this file. There is exactly one function,
`guac_client_init`, which is the entry point for all Guacamole client plugins.
Just as a typical C program has a main function which is executed when the
program is run, a Guacamole client plugin has `guac_client_init` which is
called when guacd loads the plugin when a new connection is made and your
protocol is selected.

`guac_client_init` receives a single `guac_client` which it must initialize.
Part of this initialization process involves declaring the list of arguments
that joining users can specify. While we won’t be using arguments in this
tutorial, and thus the arguments assigned above are simply an empty list, a
typical client plugin implementation would register arguments which define the
remote desktop connection and its behavior. Examples of such parameters can be
seen in the connection parameters for the protocols supported by Guacamole
out-of-the-box (see [Configuring connections](configuring-guacamole.html#connection-configuration)).

The `guac_client` instance given to `guac_client_init` will be shared by the
user that starts the connection, and any users which join the connection via
screen sharing. It lives until the connection is explicitly closed, or until
all users leave the connection.

For this project to build with GNU Automake, we a `configure.ac` file which
describes the name of the project and what it needs configuration-wise. In
this case, the project is “libguac-client-ball”, and it depends on the
“libguac” library used by guacd and all client plugins:

```
# Project information
AC_PREREQ([2.61])
AC_INIT([libguac-client-ball], [0.1.0])
AM_INIT_AUTOMAKE([-Wall -Werror foreign subdir-objects])
AM_SILENT_RULES([yes])

AC_CONFIG_MACRO_DIRS([m4])

# Check for required build tools
AC_PROG_CC
AC_PROG_CC_C99
AC_PROG_LIBTOOL

# Check for libguac
AC_CHECK_LIB([guac], [guac_client_stream_png],,
      AC_MSG_ERROR("libguac is required for communication via "
                   "the Guacamole protocol"))

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
```

We also need a `Makefile.am`, describing which files should be built and how
when building libguac-client-ball:

```
AUTOMAKE_OPTIONS = foreign

ACLOCAL_AMFLAGS = -I m4
AM_CFLAGS = -Werror -Wall -pedantic

lib_LTLIBRARIES = libguac-client-ball.la

# All source files of libguac-client-ball
libguac_client_ball_la_SOURCES = src/ball.c

# libtool versioning information
libguac_client_ball_la_LDFLAGS = -version-info 0:0:0
```

The GNU Automake files will remain largely unchanged throughout the rest of the
tutorial.

Once you have created all of the above files, you will have a functioning
client plugin. It doesn’t do anything yet, and any connection will be extremely
short-lived (the lack of any data sent by the server will lead to the client
disconnecting under the assumption that the connection has stopped responding),
but it does technically work.

## Initializing the remote display[#](#initializing-the-remote-display "Link to this heading")

Now that we have a basic functioning skeleton, we need to actually do something
with the remote display. A good first step would be simply initializing the
display - setting the remote display size and providing a basic background.

In this case, we’ll set the display to a nice default of 1024x768, and fill the
background with gray. Though the size of the display *can* be chosen based on
the size of the user’s browser window (which is provided by the user during the
[Guacamole protocol handshake](guacamole-protocol.html#guacamole-protocol-handshake), or even updated
when the window size changes (provided by the user via [“size”
instructions](protocol-reference.html#client-size-instruction "size")), we won’t be doing that here for
simplicity’s sake:

```
#include <guacamole/client.h>
#include <guacamole/protocol.h>
#include <guacamole/socket.h>
#include <guacamole/user.h>

#include <stdlib.h>

...

int ball_join_handler(guac_user* user, int argc, char** argv) {

    /* Get client associated with user */
    guac_client* client = user->client;

    /* Get user-specific socket */
    guac_socket* socket = user->socket;

    /* Send the display size */
    guac_protocol_send_size(socket, GUAC_DEFAULT_LAYER, 1024, 768);

    /* Prepare a curve which covers the entire layer */
    guac_protocol_send_rect(socket, GUAC_DEFAULT_LAYER,
            0, 0, 1024, 768);

    /* Fill curve with solid color */
    guac_protocol_send_cfill(socket,
            GUAC_COMP_OVER, GUAC_DEFAULT_LAYER,
            0x80, 0x80, 0x80, 0xFF);

    /* Mark end-of-frame */
    guac_protocol_send_sync(socket, client->last_sent_timestamp);

    /* Flush buffer */
    guac_socket_flush(socket);

    /* User successfully initialized */
    return 0;

}

int guac_client_init(guac_client* client) {

    /* This example does not implement any arguments */
    client->args = TUTORIAL_ARGS;

    /* Client-level handlers */
    client->join_handler = ball_join_handler;

    return 0;

}
```

The most important thing to notice here is the new `ball_join_handler()`
function. As it is assigned to `join_handler` of the `guac_client` given to
`guac_client_init`, users which join the connection (including the user that
opened the connection in the first place) will be passed to this function. It
is the duty of the join handler to initialize the provided `guac_user`, taking
into account any arguments received from the user during the connection
handshake (exposed through `argc` and `argv` to the join handler). We aren’t
implementing any arguments, so these values are simply ignored, but we do need
to initialize the user with respect to display state. In this case, we:

1. Send a [“size” instruction](protocol-reference.html#size-instruction "size"), initializing the display size
   to 1024x768.
2. Draw a 1024x768 gray rectangle over the display using the
   [“rect”](protocol-reference.html#rect-instruction "rect") and [“cfill”](protocol-reference.html#cfill-instruction "cfill") instructions.
3. Send a [“sync” instruction](protocol-reference.html#sync-instruction "sync"), informing the remote display
   that a frame has been completed.
4. Flush the socket, ensuring that all data written to the socket thus far is
   immediately sent to the user.

At this point, if you build, install, and connect using the plugin, you will
see a gray screen. The connection will still be extremely short-lived, however,
since the only data ever sent by the plugin is sent when the user first joins.
The lack of any data sent by the server over the remaining life of the
connection will lead to the client disconnecting under the assumption that the
connection has stopped responding. This will be rectified shortly once we add
the bouncing ball.

## Adding the ball[#](#adding-the-ball "Link to this heading")

This tutorial is about making a bouncing ball “client”, so naturally we need a
ball to bounce. While we could repeatedly draw and erase a ball on the remote
display, a more efficient technique would be to leverage Guacamole’s layers.

The remote display has a single root layer, `GUAC_DEFAULT_LAYER`, but there can
be infinitely many other child layers, which can themselves have child layers,
and so on. Each layer can be dynamically repositioned within and relative to
another layer. Because the compositing of these layers is handled by the remote
display, and is likely hardware-accelerated, this is a much better way to
repeatedly reposition something we expect to move a lot.

Since we’re finally adding the ball, and there needs to be some structure which
maintains the state of the ball, we must create a header file,
`src/ball.h`, to define this:

```
#ifndef BALL_H
#define BALL_H

#include <guacamole/layer.h>

typedef struct ball_client_data {

    guac_layer* ball;

} ball_client_data;

#endif
```

To make the build system aware of the existence of the new `src/ball.h` header
file, `Makefile.am` must be updated as well:

```
...

# All source files of libguac-client-ball
noinst_HEADERS = src/ball.h
libguac_client_ball_la_SOURCES = src/ball.c

...
```

This new structure is intended to house the client-level state of the ball,
independent of any users which join or leave the connection. The structure must
be allocated when the client begins (within `guac_client_init`), freed when the
client terminates (via a new client free handler), and must contain the layer
which represents the ball within the remote display. As this layer is part of
the remote display state, it must additionally be initialized when a user
joins, in the same way that the display overall was initialized in earlier
steps:

```
#include "ball.h"

#include <guacamole/client.h>
#include <guacamole/layer.h>
#include <guacamole/protocol.h>
#include <guacamole/socket.h>
#include <guacamole/user.h>

#include <stdlib.h>

...

int ball_join_handler(guac_user* user, int argc, char** argv) {

    /* Get client associated with user */
    guac_client* client = user->client;

    /* Get ball layer from client data */
    ball_client_data* data = (ball_client_data*) client->data;
    guac_layer* ball = data->ball;

    ...

    /* Set up ball layer */
    guac_protocol_send_size(socket, ball, 128, 128);

    /* Prepare a curve which covers the entire layer */
    guac_protocol_send_rect(socket, ball,
            0, 0, 128, 128);

    /* Fill curve with solid color */
    guac_protocol_send_cfill(socket,
            GUAC_COMP_OVER, ball,
            0x00, 0x80, 0x80, 0xFF);

    /* Mark end-of-frame */
    guac_protocol_send_sync(socket, client->last_sent_timestamp);

    /* Flush buffer */
    guac_socket_flush(socket);

    /* User successfully initialized */
    return 0;

}

int ball_free_handler(guac_client* client) {

    ball_client_data* data = (ball_client_data*) client->data;

    /* Free client-level ball layer */
    guac_client_free_layer(client, data->ball);

    /* Free client-specific data */
    free(data);

    /* Data successfully freed */
    return 0;

}

int guac_client_init(guac_client* client) {

    /* Allocate storage for client-specific data */
    ball_client_data* data = malloc(sizeof(ball_client_data));

    /* Set up client data and handlers */
    client->data = data;

    /* Allocate layer at the client level */
    data->ball = guac_client_alloc_layer(client);

    ...

    /* Client-level handlers */
    client->join_handler = ball_join_handler;
    client->free_handler = ball_free_handler;

    return 0;

}
```

The allocate/free pattern for the client-specific data and layers should be
pretty straightforward - the allocation occurs when the objects (the layer and
the structure housing it) are first needed, and the allocated objects are freed
once they are no longer needed (when the client terminates) to avoid leaking
memory. The initialization of the ball layer using the Guacamole protocol
should be familiar as well - it’s identical to the way the screen was
initialized, and involves the same instructions.

Beyond layers, Guacamole has the concept of buffers, which are identical in use
to layers except they are invisible. Buffers are used to store image data for
the sake of caching or drawing operations. We will use them later when we try
to make this tutorial prettier. If you build and install the ball client as-is
now, you will see a large gray rectangle (the root layer) with a small blue
square in the upper left corner (the ball layer).

## Making the ball bounce[#](#making-the-ball-bounce "Link to this heading")

To make the ball bounce, we need to track the ball’s state, including current
position and velocity, as well as a thread which updates the ball’s state (and
the remote display) as time progresses. The ball state and thread can be stored
alongside the ball layer in the existing client-level data structure:

```
...

#include <guacamole/layer.h>

#include <pthread.h>

typedef struct ball_client_data {

    guac_layer* ball;

    int ball_x;
    int ball_y;

    int ball_velocity_x;
    int ball_velocity_y;

    pthread_t render_thread;

} ball_client_data;

...
```

The contents of the thread will update these values at a pre-defined rate,
changing ball position with respect to velocity, and changing velocity with
respect to collisions with the display boundaries:

```
#include "ball.h"

#include <guacamole/client.h>
#include <guacamole/layer.h>
#include <guacamole/protocol.h>
#include <guacamole/socket.h>
#include <guacamole/user.h>

#include <pthread.h>
#include <stdlib.h>

...

void* ball_render_thread(void* arg) {

    /* Get data */
    guac_client* client = (guac_client*) arg;
    ball_client_data* data = (ball_client_data*) client->data;

    /* Update ball position as long as client is running */
    while (client->state == GUAC_CLIENT_RUNNING) {

        /* Sleep a bit */
        usleep(30000);

        /* Update position */
        data->ball_x += data->ball_velocity_x * 30 / 1000;
        data->ball_y += data->ball_velocity_y * 30 / 1000;

        /* Bounce if necessary */
        if (data->ball_x < 0) {
            data->ball_x = -data->ball_x;
            data->ball_velocity_x = -data->ball_velocity_x;
        }
        else if (data->ball_x >= 1024 - 128) {
            data->ball_x = (2 * (1024 - 128)) - data->ball_x;
            data->ball_velocity_x = -data->ball_velocity_x;
        }

        if (data->ball_y < 0) {
            data->ball_y = -data->ball_y;
            data->ball_velocity_y = -data->ball_velocity_y;
        }
        else if (data->ball_y >= 768 - 128) {
            data->ball_y = (2 * (768 - 128)) - data->ball_y;
            data->ball_velocity_y = -data->ball_velocity_y;
        }

        guac_protocol_send_move(client->socket, data->ball,
                GUAC_DEFAULT_LAYER, data->ball_x, data->ball_y, 0);

        /* End frame and flush socket */
        guac_client_end_frame(client);
        guac_socket_flush(client->socket);

    }

    return NULL;

}

...
```

Just as with the join handler, this thread sends a “sync” instruction to denote
the end of each frame, though here this is accomplished with
`guac_client_end_frame()`. This function sends a “sync” containing the current
timestamp, and updates the properties of the `guac_client` with the last-sent
timestamp (the value that our join handler uses to send *its* sync). Note that
we don’t redraw the whole display with each frame - we simply update the
position of the ball layer using a [“move” instruction](protocol-reference.html#move-instruction "move"), and
rely on the remote display to handle compositing on its own.

We now need to update `guac_client_init` to actually create this thread,
initialize the ball state within the structure, and store the thread for future
cleanup when the client terminates:

```
...

int ball_free_handler(guac_client* client) {

    ball_client_data* data = (ball_client_data*) client->data;

    /* Wait for render thread to terminate */
    pthread_join(data->render_thread, NULL);

    ...

}

int guac_client_init(guac_client* client) {

    ...

    /* Start ball at upper left */
    data->ball_x = 0;
    data->ball_y = 0;

    /* Move at a reasonable pace to the lower right */
    data->ball_velocity_x = 200; /* pixels per second */
    data->ball_velocity_y = 200; /* pixels per second */

    /* Start render thread */
    pthread_create(&data->render_thread, NULL, ball_render_thread, client);

    ...

}
```

The thread contains a render loop which continually checks the state property
of the `guac_client`. This property is set to `GUAC_CLIENT_RUNNING` when the
connection begins, and remains that way for the duration of the connection.
When guacd needs to terminate the connection (such as when the last user
leaves), the value will change to `GUAC_CLIENT_STOPPING`. The free handler
we’ve written can thus rely on `pthread_join()` to block until the data
previously used by the plugin is no longer being used and can safely be freed.

Once built and installed, our ball client now has a bouncing ball, albeit a
very square and plain one. Now that the display is continually updating, and
data is being continually received from the server, connected clients will no
longer automatically disconnect.

## A prettier ball[#](#a-prettier-ball "Link to this heading")

Now that we have our ball bouncing, we might as well try to make it actually
look like a ball, and try applying some of the fancier graphics features that
Guacamole offers. Guacamole provides instructions common to most 2D drawing
APIs, including HTML5’s canvas and Cairo. This means you can draw arcs, curves,
apply fill and stroke, and even use the contents of another layer or buffer as
the pattern for a fill or stroke. In complex cases involving many draw
operations, it will actually be more efficient to render to a server-side Cairo
surface and send only image data to the client, but it’s perfect for relatively
simple cases like our ball.

We will try creating a simple gray checkerboard pattern in a buffer, using that
for the background instead of the previous gray rectangle, and will modify the
ball by replacing the rectangle with an arc, in this case a full circle,
complete with stroke (border) and translucent-blue fill:

```
int ball_join_handler(guac_user* user, int argc, char** argv) {

    ...

    /* Create background tile */
    guac_layer* texture = guac_client_alloc_buffer(client);

    guac_protocol_send_rect(socket, texture, 0, 0, 64, 64);
    guac_protocol_send_cfill(socket, GUAC_COMP_OVER, texture,
            0x88, 0x88, 0x88, 0xFF);

    guac_protocol_send_rect(socket, texture, 0, 0, 32, 32);
    guac_protocol_send_cfill(socket, GUAC_COMP_OVER, texture,
            0xDD, 0xDD, 0xDD, 0xFF);

    guac_protocol_send_rect(socket, texture, 32, 32, 32, 32);
    guac_protocol_send_cfill(socket, GUAC_COMP_OVER, texture,
            0xDD, 0xDD, 0xDD, 0xFF);


    /* Prepare a curve which covers the entire layer */
    guac_protocol_send_rect(socket, GUAC_DEFAULT_LAYER,
            0, 0, 1024, 768);

     /* Fill curve with texture */
    guac_protocol_send_lfill(socket,
            GUAC_COMP_OVER, GUAC_DEFAULT_LAYER,
            texture);

    /* Set up ball layer */
    guac_protocol_send_size(socket, ball, 128, 128);

    /* Prepare a circular curve */
    guac_protocol_send_arc(socket, data->ball,
            64, 64, 62, 0, 6.28, 0);

    guac_protocol_send_close(socket, data->ball);

    /* Draw a 4-pixel black border */
    guac_protocol_send_cstroke(socket,
            GUAC_COMP_OVER, data->ball,
            GUAC_LINE_CAP_ROUND, GUAC_LINE_JOIN_ROUND, 4,
            0x00, 0x00, 0x00, 0xFF);

    /* Fill the circle with color */
    guac_protocol_send_cfill(socket,
            GUAC_COMP_OVER, data->ball,
            0x00, 0x80, 0x80, 0x80);

    /* Free texture (no longer needed) */
    guac_client_free_buffer(client, texture);

    /* Mark end-of-frame */
    guac_protocol_send_sync(socket, client->last_sent_timestamp);

    ...

}
```

Again, because we put the ball in its own layer, we don’t have to worry about
compositing it ourselves. The remote display will handle this, and will likely
do so with hardware acceleration, even though the ball is now translucent.
Build and install the ball client after this step, and you will have a rather
nice-looking bouncing ball.

## Handling the passage of time[#](#handling-the-passage-of-time "Link to this heading")

There are never any guarantees when it comes to timing, threads, and network
performance. We cannot necessarily rely on the remote display to handle updates
in a timely manner (it may be slow), nor can we rely on the network or server
to give priority to communication from guacd.

The render thread needs to be modified to take this into account, by tracking
the actual time spent within each frame, and estimating the amount of time the
client spends rendering each frame:

```
#include "ball.h"

#include <guacamole/client.h>
#include <guacamole/layer.h>
#include <guacamole/protocol.h>
#include <guacamole/socket.h>
#include <guacamole/timestamp.h>
#include <guacamole/user.h>

#include <pthread.h>
#include <stdlib.h>

...

void* ball_render_thread(void* arg) {

    ...

    /* Init time of last frame to current time */
    guac_timestamp last_frame = guac_timestamp_current();

    /* Update ball position as long as client is running */
    while (client->state == CLIENT_RUNNING) {

        /* Default to 30ms frames */
        int frame_duration = 30;

        /* Lengthen frame duration if client is lagging */
        int processing_lag = guac_client_get_processing_lag(client);
        if (processing_lag > frame_duration)
            frame_duration = processing_lag;

        /* Sleep for duration of frame, then get timestamp */
        usleep(frame_duration);
        guac_timestamp current = guac_timestamp_current();

        /* Calculate change in time */
        int delta_t = current - last_frame;

        /* Update position */
        data->ball_x += data->ball_velocity_x * delta_t / 1000;
        data->ball_y += data->ball_velocity_y * delta_t / 1000;

        ...

        /* Update timestamp */
        last_frame = current;

    }

    ...

}
```

The calculations are pretty simple. Rather than hard-code the duration of each
frame, we us a default of 30 milliseconds, lengthening the frame if Guacamole’s
built-in lag estimation determines that the client is having trouble. The
physics portion of the update no longer assumes that the frame will be exactly
30 milliseconds, instead relying on the actual time elapsed since the previous
frame.

At this point, we now have a robust Guacamole client plugin. It handles
joining/leaving users correctly, continually updates the remote display state
while taking into account variable network/server/client conditions, and cleans
up after itself when the connection finally terminates.

Contents

---
# Implementation and architecture

## Contents

# Implementation and architecture[#](#implementation-and-architecture "Link to this heading")

Guacamole is not a self-contained web application and is made up of many parts.
The web application is actually intended to be simple and minimal, with the
majority of the gruntwork performed by lower-level components.

[![_images/guac-arch.png](assets/doc_gug__images_guac-arch.png)](_images/guac-arch.png)

Users connect to a Guacamole server with their web browser. The Guacamole
client, written in JavaScript, is served to users by a webserver within the
Guacamole server. Once loaded, this client connects back to the server over
HTTP using the Guacamole protocol.

The web application deployed to the Guacamole server reads the Guacamole
protocol and forwards it to guacd, the native Guacamole proxy. This proxy
actually interprets the contents of the Guacamole protocol, connecting to any
number of remote desktop servers on behalf of the user.

The Guacamole protocol combined with guacd provide protocol agnosticism:
neither the Guacamole client nor the web application need to be aware of what
remote desktop protocol is actually being used.

## The Guacamole protocol[#](#the-guacamole-protocol "Link to this heading")

The web application does not understand any remote desktop protocol at all. It
does not contain support for VNC or RDP or any other protocol supported by the
Guacamole stack. It actually only understands the Guacamole protocol, which is
a protocol for remote display rendering and event transport. While a protocol
with those properties would naturally have the same abilities as a remote
desktop protocol, the design principles behind a remote desktop protocol and
the Guacamole protocol are different: the Guacamole protocol is not intended to
implement the features of a specific desktop environment.

As a remote display and interaction protocol, Guacamole implements a superset
of existing remote desktop protocols. Adding support for a particular remote
desktop protocol (like RDP) to Guacamole thus involves writing a middle layer
which “translates” between the remote desktop protocol and the Guacamole
protocol. Implementing such a translation is no different than implementing any
native client, except that this particular implementation renders to a remote
display rather than a local one.

The middle layer that handles this translation is guacd.

## guacd[#](#guacd "Link to this heading")

guacd is the heart of Guacamole which dynamically loads support for remote
desktop protocols (called “client plugins”) and connects them to remote
desktops based on instructions received from the web application.

guacd is a daemon process which is installed along with Guacamole and runs in
the background, listening for TCP connections from the web application. guacd
also does not understand any specific remote desktop protocol, but rather
implements just enough of the Guacamole protocol to determine which protocol
support needs to be loaded and what arguments must be passed to it. Once a
client plugin is loaded, it runs independently of guacd and has full control of
the communication between itself and the web application until the client
plugin terminates.

guacd and all client plugins depend on a common library, libguac, which makes
communication via the Guacamole protocol easier and a bit more abstract.

## The web application[#](#the-web-application "Link to this heading")

The part of Guacamole that a user actually interacts with is the web
application.

The web application, as mentioned before, does not implement any remote desktop
protocol. It relies on guacd, and implements nothing more than a spiffy web
interface and authentication layer.

We chose to implement the server side of the web application in Java, but
there’s no reason that it can’t be written in a different language. In fact,
because Guacamole is intended be an API, we encourage this.

## RealMint[#](#realmint "Link to this heading")

Guacamole is now a generalized remote desktop gateway, but this was not always
the case. Guacamole began as a purely text-based Telnet client written in
JavaScript called RealMint (“RealMint” is an anagram for “terminal”). It was
written mainly as a demonstration and, while intended to be useful, its main
claim to fame was only that it was pure JavaScript.

The tunnel used by RealMint was written in PHP. In contrast to Guacamole’s HTTP
tunnel, RealMint’s tunnel used only simple long-polling and was inefficient.
RealMint had a decent keyboard implementation which lives on now in parts of
Guacamole’s keyboard code, but this was really the extent of RealMint’s
features and usability.

Given that it was just an implementation of a legacy protocol, and that several
other JavaScript terminal emulators exist, most of which well-established and
stable, the project was dropped.

## VNC Client[#](#vnc-client "Link to this heading")

Once the developers learned of the HTML5 canvas tag, and saw that it was
already implemented in Firefox and Chrome, work started instead on a
proof-of-concept JavaScript VNC client.

This client was purely JavaScript with a Java server component, and worked by
translating VNC into an XML-based version of the same. Its development was
naturally driven by VNC’s features, and its scope was limited to forwarding a
single connection to a set of users. Although relatively slow, the
proof-of-concept worked well enough that the project needed an online place to
live, and was registered with SourceForge as “Guacamole” - an HTML5 VNC client.

As Guacamole grew and became more than a proof-of-concept, the need for speed
increased, and the old RealMint-style long polling was dropped, as was the use
of XML.

As WebSocket could not be trusted to be supported at the time, and Java had no
WebSocket standard for servlets, an equivalent HTTP-based tunnel was developed.
This tunnel is still used today if WebSocket cannot be used for any reason.

## Remote Desktop Gateway[#](#remote-desktop-gateway "Link to this heading")

A faster text-based protocol was developed which could present the features of
multiple remote desktop protocols, not just VNC. The entire system was
rearchitected into a standard daemon, guacd, and a common library, libguac,
which drove both the daemon and protocol support, which became extendable.

The scope of the project expanded from an adequate VNC client to a performant
HTML5 remote desktop gateway and general API. In its current state, Guacamole
can be used as a central gateway to access any number of machines running
different remote desktop servers. It provides extendable authentication, and in
the case you need something more specialized, a general API for HTML5-based
remote access.

Contents

---
# Guacamole protocol reference

## Contents

# Guacamole protocol reference[#](#guacamole-protocol-reference "Link to this heading")

## Drawing instructions[#](#drawing-instructions "Link to this heading")

arc[#](#arc-instruction "Link to this definition")
:   The arc instruction adds the specified arc subpath to the existing path,
    creating a new path if no path exists. The path created can be modified further
    by other path-type instructions, and finally stroked, filled, and/or closed.

    Arguments:
    :   * **layer** (*integer*) – The layer which should have the specified arc subpath added.
        * **x** (*integer*) – The X coordinate of the center of the circle containing the arc to be
          drawn.
        * **y** (*integer*) – The Y coordinate of the center of the circle containing the arc to be
          drawn.
        * **radius** (*float*) – The radius of the circle containing the arc to be drawn, in pixels.
        * **start** (*float*) – The starting angle of the arc to be drawn, in radians.
        * **end** (*float*) – The ending angle of the arc to be drawn, in radians.
        * **negative** (*integer*) – Non-zero if the arc should be drawn from START to END in order of
          decreasing angle, zero otherwise.

cfill[#](#cfill-instruction "Link to this definition")
:   Fills the current path with the specified color. This instruction completes
    the current path. Future path instructions will begin a new path.

    Arguments:
    :   * **mask** (*integer*) – The channel mask to apply when filling the current path in the
          specified layer.
        * **layer** (*integer*) – The layer whose path should be filled.
        * **r** (*integer*) – The red component of the color to use to fill the current path in the
          specified layer.
        * **g** (*integer*) – The green component of the color to use to fill the current path in the
          specified layer.
        * **b** (*integer*) – The blue component of the color to use to fill the current path in the
          specified layer.
        * **a** (*integer*) – The alpha component of the color to use to fill the current path in the
          specified layer.

clip[#](#clip-instruction "Link to this definition")
:   Applies the current path as the clipping path. Future operations will only
    draw within the current path. Note that future clip instructions will also
    be limited by this path. To set a completely new clipping path, you must
    first reset the layer with a reset instruction. If you wish to only reset
    the clipping path, but preserve the current transform matrix, push the
    layer state before setting the clipping path, and pop the layer state to
    reset.

    Arguments:
    :   **layer** (*integer*) – The layer whose clipping path should be set.

close[#](#close-instruction "Link to this definition")
:   Closes the current path by connecting the start and end points with a
    straight line.

    Arguments:
    :   **layer** (*integer*) – The layer whose path should be closed.

copy[#](#copy-instruction "Link to this definition")
:   Copies image data from the specified rectangle of the specified layer or
    buffer to a different location of another specified layer or buffer.

    Arguments:
    :   * **srclayer** (*integer*) – The index of the layer to copy image data from.
        * **srcx** (*integer*) – The X coordinate of the upper-left corner of the source rectangle
          within the source layer.
        * **srcy** (*integer*) – The Y coordinate of the upper-left corner of the source rectangle
          within the source layer.
        * **srcwidth** (*integer*) – The width of the source rectangle within the source layer.
        * **srcheight** (*integer*) – The height of the source rectangle within the source layer.
        * **mask** (*integer*) – The channel mask to apply when drawing the image data on the
          destination layer.
        * **dstlayer** (*integer*) – The index of the layer to draw the image data to.
        * **dstx** (*integer*) – The X coordinate of the upper-left corner of the destination within
          the destination layer.
        * **dsty** (*integer*) – The Y coordinate of the upper-left corner of the destination within
          the destination layer.

cstroke[#](#cstroke-instruction "Link to this definition")
:   Strokes the current path with the specified color. This instruction
    completes the current path. Future path instructions will begin a new path.

    Arguments:
    :   * **mask** (*integer*) – The channel mask to apply when stroking the current path in the
          specified layer.
        * **layer** (*integer*) – The layer whose path should be stroked.
        * **cap** (*integer*) – The index of the line cap style to use. This can be either butt (0),
          round (1), or square (2).
        * **join** (*integer*) – The index of the line join style to use. This can be either bevel
          (0), miter (1), or round (2).
        * **thickness** (*integer*) – The thickness of the stroke to draw, in pixels.
        * **r** (*integer*) – The red component of the color to use to stroke the current path in
          the specified layer.
        * **g** (*integer*) – The green component of the color to use to stroke the current path in
          the specified layer.
        * **b** (*integer*) – The blue component of the color to use to stroke the current path in
          the specified layer.
        * **a** (*integer*) – The alpha component of the color to use to stroke the current path in
          the specified layer.

cursor[#](#cursor-instruction "Link to this definition")
:   Sets the client’s cursor to the image data from the specified rectangle of
    a layer, with the specified hotspot.

    Arguments:
    :   * **x** (*integer*) – The X coordinate of the cursor’s hotspot.
        * **y** (*integer*) – The Y coordinate of the cursor’s hotspot.
        * **srclayer** (*integer*) – The index of the layer to copy image data from.
        * **srcx** (*integer*) – The X coordinate of the upper-left corner of the source rectangle
          within the source layer.
        * **srcy** (*integer*) – The Y coordinate of the upper-left corner of the source rectangle
          within the source layer.
        * **srcwidth** (*integer*) – The width of the source rectangle within the source layer.
        * **srcheight** (*integer*) – The height of the source rectangle within the source layer.

curve[#](#curve-instruction "Link to this definition")
:   Adds the specified cubic bezier curve subpath.

    Arguments:
    :   * **layer** (*integer*) – The layer which should have the specified curve subpath added.
        * **cp1x** (*integer*) – The X coordinate of the first control point of the curve.
        * **cp1y** (*integer*) – The Y coordinate of the first control point of the curve.
        * **cp2x** (*integer*) – The X coordinate of the second control point of the curve.
        * **cp2y** (*integer*) – The Y coordinate of the second control point of the curve.
        * **x** (*integer*) – The X coordinate of the endpoint of the curve.
        * **y** (*integer*) – The Y coordinate of the endpoint of the curve.

dispose[#](#dispose-instruction "Link to this definition")
:   Removes the specified layer. The specified layer will be recreated as a new
    layer if it is referenced again.

    Arguments:
    :   **layer** (*integer*) – The layer to remove.

distort[#](#distort-instruction "Link to this definition")
:   Sets the given affine transformation matrix to the layer. Unlike transform,
    this operation is independent of any previously sent transformation matrix.
    This operation can be undone by setting the layer’s transformation matrix
    to the identity matrix using distort

    Arguments:
    :   * **layer** (*integer*) – The layer to distort.
        * **a** (*float*) – The matrix value in row 1, column 1.
        * **b** (*float*) – The matrix value in row 2, column 1.
        * **c** (*float*) – The matrix value in row 1, column 2.
        * **d** (*float*) – The matrix value in row 2, column 2.
        * **e** (*float*) – The matrix value in row 1, column 3.
        * **f** (*float*) – The matrix value in row 2, column 3.

identity[#](#identity-instruction "Link to this definition")
:   Resets the transform matrix of the specified layer to the identity matrix.

    Arguments:
    :   **layer** (*integer*) – The layer whose transform matrix should be reset.

img[#](#img-instruction "Link to this definition")
:   Allocates a new stream, associating it with the metadata of an image
    update, including the image type, the destination layer, and destination
    coordinates. The contents of the image will later be sent along the stream
    with blob instructions. The full size of the image need not be known ahead
    of time.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the image being sent.
        * **mask** (*integer*) – The channel mask to apply when drawing the image data.
        * **layer** (*integer*) – The destination layer.
        * **x** (*integer*) – The X coordinate of the upper-left corner of the destination within
          the destination layer.
        * **y** (*integer*) – The Y coordinate of the upper-left corner of the destination within
          the destination layer.

lfill[#](#lfill-instruction "Link to this definition")
:   Fills the current path with a tiled pattern of the image data from the
    specified layer. This instruction completes the current path. Future path
    instructions will begin a new path.

    Arguments:
    :   * **mask** (*integer*) – The channel mask to apply when filling the current path in the
          specified layer.
        * **layer** (*integer*) – The layer whose path should be filled.
        * **srclayer** (*integer*) – The layer to use as the pattern.

line[#](#line-instruction "Link to this definition")
:   Adds the specified line subpath.

    Arguments:
    :   * **layer** (*integer*) – The layer which should have the specified line subpath added.
        * **x** (*integer*) – The X coordinate of the endpoint of the line.
        * **y** (*integer*) – The Y coordinate of the endpoint of the line.

lstroke[#](#lstroke-instruction "Link to this definition")
:   Strokes the current path with a tiled pattern of the image data from the
    specified layer. This instruction completes the current path. Future path
    instructions will begin a new path.

    Arguments:
    :   * **mask** (*integer*) – The channel mask to apply when filling the current path in the
          specified layer.
        * **layer** (*integer*) – The layer whose path should be filled.
        * **cap** (*integer*) – The index of the line cap style to use. This can be either butt (0),
          round (1), or square (2).
        * **join** (*integer*) – The index of the line join style to use. This can be either bevel
          (0), miter (1), or round (2).
        * **thickness** (*integer*) – The thickness of the stroke to draw, in pixels.
        * **srclayer** (*integer*) – The layer to use as the pattern.

move[#](#move-instruction "Link to this definition")
:   Moves the given layer to the given location within the specified parent
    layer. This operation is applicable only to layers, and cannot be applied
    to buffers (layers with negative indices). Applying this operation to the
    default layer (layer 0) also has no effect.

    Arguments:
    :   * **layer** (*integer*) – The layer to move.
        * **parent** (*integer*) – The layer that should be the parent of the given layer.
        * **x** (*integer*) – The X coordinate to move the layer to.
        * **y** (*integer*) – The Y coordinate to move the layer to.
        * **z** (*integer*) – The relative Z-ordering of this layer. Layers with larger values will
          appear above layers with smaller values.

pop[#](#pop-instruction "Link to this definition")
:   Restores the previous state of the specified layer from the stack. The
    state restored includes the transformation matrix and clipping path.

    Arguments:
    :   **layer** (*integer*) – The layer whose state should be restored.

push[#](#push-instruction "Link to this definition")
:   Saves the current state of the specified layer to the stack. The state
    saved includes the current transformation matrix and clipping path.

    Arguments:
    :   **layer** (*integer*) – The layer whose state should be saved.

rect[#](#rect-instruction "Link to this definition")
:   Adds a rectangular path to the specified layer.

    Arguments:
    :   * **mask** (*integer*) – The channel mask to apply when drawing the image data.
        * **layer** (*integer*) – The destination layer.
        * **x** (*integer*) – The X coordinate of the upper-left corner of the rectangle to draw.
        * **y** (*integer*) – The Y coordinate of the upper-left corner of the rectangle to draw.
        * **width** (*integer*) – The width of the rectangle to draw.
        * **height** (*integer*) – The width of the rectangle to draw.

reset[#](#reset-instruction "Link to this definition")
:   Resets the transformation and clip state of the layer.

    Arguments:
    :   **layer** (*integer*) – The layer whose state should be reset.

set[#](#set-instruction "Link to this definition")
:   Sets the given client-side property to the specified value. Currently there
    is only one property: miter-limit, the maximum distance between the inner
    and outer points of a miter joint, proportional to stroke width (if
    miter-limit is set to 10.0, the default, then the maximum distance between
    the points of the joint is 10 times the stroke width).

    Arguments:
    :   * **layer** (*integer*) – The layer whose property should be set.
        * **property** (*string*) – The name of the property to set.
        * **value** (*string*) – The value to set the given property to.

shade[#](#shade-instruction "Link to this definition")
:   Sets the opacity of the given layer.

    Arguments:
    :   * **layer** (*integer*) – The layer whose opacity should be set.
        * **opacity** (*integer*) – The opacity of the layer, where 0 is completely transparent, and 255
          is completely opaque.

size[#](#size-instruction "Link to this definition")
:   Sets the size of the specified layer.

    Arguments:
    :   * **layer** (*integer*) – The layer to resize.
        * **width** (*integer*) – The new width of the layer
        * **height** (*integer*) – The new height of the layer

start[#](#start-instruction "Link to this definition")
:   Starts a new subpath at the specified point.

    Arguments:
    :   * **layer** (*integer*) – The layer which should start a new subpath.
        * **x** (*integer*) – The X coordinate of the first point of the new subpath.
        * **y** (*integer*) – The Y coordinate of the first point of the new subpath.

transfer[#](#transfer-instruction "Link to this definition")
:   Transfers image data from the specified rectangle of the specified layer or
    buffer to a different location of another specified layer or buffer, using
    the specified transfer function.

    For a list of available functions, see the definition of
    `guac_transfer_function` within the [guacamole/protocol-types.h](https://github.com/apache/guacamole-server/blob/master/src/libguac/guacamole/protocol-types.h)
    header included with libguac.

    Arguments:
    :   * **srclayer** (*integer*) – The index of the layer to transfer image data from.
        * **srcx** (*integer*) – The X coordinate of the upper-left corner of the source rectangle
          within the source layer.
        * **srcy** (*integer*) – The Y coordinate of the upper-left corner of the source rectangle
          within the source layer.
        * **srcwidth** (*integer*) – The width of the source rectangle within the source layer.
        * **srcheight** (*integer*) – The height of the source rectangle within the source layer.
        * **function** (*integer*) –

          The index of the transfer function to use.

          For a list of available functions, see the definition of
          `guac_transfer_function` within the [guacamole/protocol-types.h](https://github.com/apache/guacamole-server/blob/master/src/libguac/guacamole/protocol-types.h)
          header included with libguac.
        * **dstlayer** (*integer*) – The index of the layer to draw the image data to.
        * **dstx** (*integer*) – The X coordinate of the upper-left corner of the destination within
          the destination layer.
        * **dsty** (*integer*) – The Y coordinate of the upper-left corner of the destination within
          the destination layer.

transform[#](#transform-instruction "Link to this definition")
:   Applies the specified transformation matrix to future operations. Unlike
    distort, this operation is dependent on any previously sent transformation
    matrices, and only affects future operations. This operation can be undone
    by setting the layer’s transformation matrix to the identity matrix using
    identity, but image data already drawn will not be affected.

    Arguments:
    :   * **layer** (*integer*) – The layer to apply the given transformation matrix to.
        * **a** (*float*) – The matrix value in row 1, column 1.
        * **b** (*float*) – The matrix value in row 2, column 1.
        * **c** (*float*) – The matrix value in row 1, column 2.
        * **d** (*float*) – The matrix value in row 2, column 2.
        * **e** (*float*) – The matrix value in row 1, column 3.
        * **f** (*float*) – The matrix value in row 2, column 3.

## Streaming instructions[#](#streaming-instructions "Link to this heading")

ack[#](#ack-instruction "Link to this definition")
:   The ack instruction acknowledges a received data blob, providing a status
    code and message indicating whether the operation associated with the blob
    succeeded or failed. A status code other than 0 (`SUCCESS`) implicitly
    ends the stream.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream the corresponding blob was received on.
        * **message** (*string*) – A human-readable error message. This typically is not exposed within
          any user interface, and mainly helps with debugging.
        * **status** (*integer*) – The Guacamole status code denoting success or failure. For a list of status
          codes, see the table in [Status codes](#status-codes).

argv[#](#argv-instruction "Link to this definition")
:   Allocates a new stream, associating it with the given argument (connection
    parameter) metadata. The relevant connection parameter data will later be
    sent along the stream with blob instructions. If sent by the client, this
    data will be the desired new value of the connection parameter being
    changed, and will be applied if the server supports changing that
    connection parameter while the connection is active. If sent by the server,
    this data will be the current value of a connection parameter being exposed
    to the client.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the connection parameter being sent. In most cases,
          this will be “text/plain”.
        * **name** (*string*) – The name of the connection parameter whose value is being sent.

audio[#](#audio-instruction "Link to this definition")
:   Allocates a new stream, associating it with the given audio metadata.
    Audio data will later be sent along the stream with blob instructions. The
    mimetype given must be a mimetype previously specified by the client during
    the handshake procedure. Playback will begin immediately and will continue
    as long as blobs are received along the stream.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the audio data being sent.

blob[#](#blob-instruction "Link to this definition")
:   Sends a blob of data along the given stream. This blob of data is
    arbitrary, base64-encoded data, and only has meaning to the Guacamole
    client or server through the metadata assigned to the stream when the
    stream was allocated.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream along which the given data should be sent.
        * **data** (*string*) – The base64-encoded data to send.

clipboard[#](#clipboard-instruction "Link to this definition")
:   Allocates a new stream, associating it with the given clipboard metadata.
    The clipboard data will later be sent along the stream with blob
    instructions. If sent by the client, this data will be the contents of the
    client-side clipboard. If sent by the server, this data will be the
    contents of the clipboard within the remote desktop.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the clipboard data being sent. In most cases, this
          will be “text/plain”.

end[#](#end-instruction "Link to this definition")
:   The end instruction terminates an open stream, freeing any client-side or
    server-side resources. Data sent to a terminated stream will be ignored.
    Terminating a stream with the end instruction only denotes the end of the
    stream and does not imply an error.

    Arguments:
    :   **stream** (*integer*) – The index of the stream the corresponding blob was received on.

file[#](#file-instruction "Link to this definition")
:   Allocates a new stream, associating it with the given arbitrary file
    metadata. The contents of the file will later be sent along the stream with
    blob instructions. The full size of the file need not be known ahead of
    time.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the file being sent.
        * **filename** (*string*) – The name of the file, as it would be saved on a filesystem.

msg[#](#msg-instruction "Link to this definition")
:   Sends a message from the server (guacd) to the client. The nature of these
    messages is intentionally broad and flexible - the message must include
    a numeric code that the client understands and can act on, and may also
    any number of arguments that can be used by the client in association
    with the message.

    Arguments:
    :   * **msg** (*integer*) – A numeric value indicating the message that is being passed to the client.
        * **args** (*string*) – Any number of arguments associated with the message that is being sent
          to the client.

pipe[#](#pipe-instruction "Link to this definition")
:   Allocates a new stream, associating it with the given arbitrary named pipe
    metadata. The contents of the pipe will later be sent along the stream with
    blob instructions. Pipes in the Guacamole protocol are unidirectional,
    named pipes, very similar to a UNIX FIFO or pipe. It is up to client-side
    code to handle pipe data appropriately, likely based upon the name of the
    pipe, which is arbitrary. Pipes may be opened by either the client or the
    server.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the data being sent along the pipe.
        * **name** (*string*) – The arbitrary name of the pipe, which may have special meaning to
          client-side code.

video[#](#video-instruction "Link to this definition")
:   Allocates a new stream, associating it with the given video metadata.
    Video data will later be sent along the stream with blob instructions. The
    mimetype given must be a mimetype previously specified by the client during
    the handshake procedure. Playback will begin immediately and will continue
    as long as blobs are received along the stream.

    Arguments:
    :   * **stream** (*integer*) – The index of the stream to allocate.
        * **layer** (*integer*) – The index of the layer to stream the video data into. The effect of
          other drawing operations on this layer during playback is undefined,
          as the client codec implementation may leverage any rendering
          mechanism it sees fit, including hardware decoding.
        * **mimetype** (*string*) – The mimetype of the video data being sent.

## Object instructions[#](#object-instructions "Link to this heading")

body[#](#body-instruction "Link to this definition")
:   Allocates a new stream, associating it with the name of a stream previously
    requested by a get instruction. The contents of the stream will be sent
    later with blob instructions. The full size of the stream need not be known
    ahead of time.

    Arguments:
    :   * **object** (*integer*) – The index of the object associated with this stream.
        * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the data being sent.
        * **name** (*string*) – The name of the stream associated with the object.

filesystem[#](#filesystem-instruction "Link to this definition")
:   Allocates a new object, associating it with the given arbitrary filesystem
    metadata. The contents of files and directories within the filesystem will
    later be sent along streams requested with get instructions or created with
    put instructions.

    Arguments:
    :   * **object** (*integer*) – The index of the object to allocate.
        * **name** (*string*) – The name of the filesystem.

get[#](#get-instruction "Link to this definition")
:   Requests that a new stream be created, providing read access to the object
    stream having the given name. The requested stream will be created, in
    response, with a body instruction.

    Stream names are arbitrary and dictated by the object from which they are
    requested, with the exception of the root stream of the object itself,
    which has the reserved name “`/`”. The root stream of the object has the
    mimetype “`application/vnd.glyptodon.guacamole.stream-index+json`”, and
    provides a simple JSON map of available stream names to their corresponding
    mimetypes. If the object contains a hierarchy of streams, some of these
    streams may also be
    “`application/vnd.glyptodon.guacamole.stream-index+json`”.

    For example, the ultimate content of the body stream provided in response
    to a get request for the root stream of an object containing two text
    streams, “A” and “B”, would be the following:

    ```
    {
      "A" : "text/plain",
      "B" : "text/plain"
    }
    ```

    Arguments:
    :   * **object** (*integer*) – The index of the object to request a stream from.
        * **name** (*string*) – The name of the stream being requested from the given object.

put[#](#put-instruction "Link to this definition")
:   Allocates a new stream, associating it with the given arbitrary object and
    stream name. The contents of the stream will later be sent with blob
    instructions.

    Arguments:
    :   * **object** (*integer*) – The index of the object associated with this stream.
        * **stream** (*integer*) – The index of the stream to allocate.
        * **mimetype** (*string*) – The mimetype of the data being sent.
        * **name** (*string*) – The name of the stream within the given object to which data is being
          sent.

undefine[#](#undefine-instruction "Link to this definition")
:   Undefines an existing object, allowing its index to be reused by another
    future object. The resource associated with the original object may or may
    not continue to exist - it simply no longer has an associated object.

    Arguments:
    :   **object** (*integer*) – The index of the object to undefine.

## Client handshake instructions[#](#client-handshake-instructions "Link to this heading")

audio[#](#client-audio-handshake-instruction "Link to this definition")
:   Specifies which audio mimetypes are supported by the client. Each parameter
    must be a single mimetype, listed in order of client preference, with the
    optimal mimetype being the first parameter.

connect[#](#client-connect-handshake-instruction "Link to this definition")
:   Begins the connection using the previously specified protocol with the
    given arguments. This is the last instruction sent during the handshake
    phase.

    The parameters of this instruction correspond exactly to the parameters of
    the received args instruction. If the received args instruction has, for
    example, three parameters, the responding connect instruction must also
    have three parameters.

image[#](#client-image-handshake-instruction "Link to this definition")
:   Specifies which image mimetypes are supported by the client. Each parameter
    must be a single mimetype, listed in order of client preference, with the
    optimal mimetype being the first parameter.

    It is expected that the supported mimetypes will include at least
    “image/png” and “image/jpeg”, and the server *may* safely assume that these
    mimetypes are supported, even if they are absent from the handshake.

name[#](#client-name-handshake-instruction "Link to this definition")
:   Specifies the human-readable name of the user joining a connection. A
    single, string value is expected for this, and guacd does not expect
    or require that this value be unique among other users connected to
    the server or connection. The type of name provided is completely up
    to the client implementation.

select[#](#client-select-handshake-instruction "Link to this definition")
:   Requests that the connection be made using the specified protocol, or to
    the specified existing connection. Whether a new connection is established
    or an existing connection is joined depends on whether the ID of an active
    connection is provided. The Guacamole protocol dictates that the IDs
    generated for active connections (provided during the handshake of those
    connections via the [ready instruction](#ready-instruction)) must not
    collide with any supported protocols.

    This is the first instruction sent during the handshake phase.

    Arguments:
    :   **identifier** (*string*) – The name of the protocol to use, such as “vnc” or “rdp”, or the ID of
        the active connection to be joined, as returned via the [ready
        instruction](#ready-instruction).

size[#](#client-size-handshake-instruction "Link to this definition")
:   Specifies the client’s optimal screen size and resolution.

    Arguments:
    :   * **width** (*integer*) – The optimal screen width.
        * **height** (*integer*) – The optimal screen height.
        * **dpi** (*integer*) – The optimal screen resolution, in approximate DPI.

timezone[#](#client-timezone-handshake-instruction "Link to this definition")
:   Specifies the timezone of the client system, in IANA zone key format. This
    is a single-value parameter, and may be used by protocols to set the
    timezone on the remote computer, if the remote system allows the timezone
    to be configured. This instruction is optional.

    Arguments:
    :   **timezone** (*string*)

video[#](#client-video-handshake-instruction "Link to this definition")
:   Specifies which video mimetypes are supported by the client. Each parameter
    must be a single mimetype, listed in order of client preference, with the
    optimal mimetype being the first parameter.

## Server handshake instructions[#](#server-handshake-instructions "Link to this heading")

args[#](#args-handshake-instruction "Link to this definition")
:   Reports the expected format of the argument list for the protocol requested
    by the client. This message can be sent by the server during the handshake
    phase only.

    The first parameter of this instruction will be the protocol version
    supported by the server. This is used to negotiate protocol compatibility
    between the client and the server, with the highest supported protocol by
    both sides being chosen. Versions of Guacamole prior to 1.1.0 do not
    support protocol version negotiation, and will silently ignore this
    instruction.

    The remaining parameters of the args instruction are the names of all
    connection parameters accepted by the server for the protocol selected by
    the client, in order. The client’s responding connect instruction must
    contain the values of each of these parameters in the same order.

## Control instructions[#](#control-instructions "Link to this heading")

disconnect[#](#disconnect-instruction "Link to this definition")
:   Notifies the client or server that the connection is about to be closed.
    This message can be sent during any phase, and takes no parameters.

nop[#](#nop-instruction "Link to this definition")
:   The “nop” instruction does absolutely nothing, has no parameters, and is
    universally ignored by both Guacamole clients and servers. Its main use is
    as a keep-alive signal, and may be sent by guacd, client plugins, or web
    applications when there is no activity to ensure the socket is not closed
    due to timeout.

sync[#](#sync-instruction "Link to this definition")
:   Reports that all operations as of the given server-relative timestamp have
    been completed. Both client and server are expected to occasionally send
    sync to report on current operation execution state, with the server using
    sync to denote the end of a logical frame.

    If a sync is received from the server, the client must respond with a
    corresponding sync once all previous operations have been completed, or the
    server may stop sending updates until the client catches up. For the
    client, sending a sync with a timestamp newer than any timestamp received
    from the server is an error.

    Arguments:
    :   **timestamp** (*integer*) – A valid server-relative timestamp.

## Server control instructions[#](#server-control-instructions "Link to this heading")

error[#](#error-instruction "Link to this definition")
:   Notifies the client that the connection is about to be closed due to the
    specified error. This message can be sent by the server during any phase.

    Arguments:
    :   * **message** (*string*) – An arbitrary message describing the error
        * **status** (*integer*) – The Guacamole status code describing the error. For a list of status
          codes, see the table in [Status codes](#status-codes).

log[#](#log-instruction "Link to this definition")
:   The log instruction sends an arbitrary string for debugging purposes. This
    instruction will be ignored by Guacamole clients, but can be seen in
    protocol dumps if such dumps become necessary. Sending a log instruction
    can help add context when searching for the cause of a fault in protocol
    support.

    Arguments:
    :   **message** (*string*) – An arbitrary, human-readable message.

mouse[#](#mouse-instruction "Link to this definition")
:   Reports that a user on the current connection has moved the mouse to the
    given coordinates.

    Arguments:
    :   * **x** (*integer*) – The current X coordinate of the mouse pointer.
        * **y** (*integer*) – The current Y coordinate of the mouse pointer.

ready[#](#ready-handshake-instruction "Link to this definition")
:   The ready instruction sends the ID of a new connection and marks the
    beginning of the interactive phase of a new, successful connection. The ID
    sent is a completely arbitrary string, and has no standard format. It must
    be unique from all existing and future connections and may not match the
    name of any installed protocol support.

    Arguments:
    :   **identifier** (*string*) – An arbitrary, unique identifier for the current connection. This
        identifier must be unique from all existing and future connections,
        and may not match the name of any installed protocol support (such as
        “vnc” or “rdp”).

## Input/Event instructions[#](#input-event-instructions "Link to this heading")

key[#](#client-key-instruction "Link to this definition")
:   Sends the specified key press or release event.

    Arguments:
    :   * **keysym** (*integer*) – The [X11 keysym](https://www.x.org/releases/X11R7.6/doc/xproto/x11protocol.html#keysym_encoding) of the key being
          pressed or released.
        * **pressed** (*integer*) – 0 if the key is not pressed, 1 if the key is pressed.

mouse[#](#client-mouse-instruction "Link to this definition")
:   Sends the specified mouse movement or button press or release event (or
    combination thereof).

    Arguments:
    :   * **x** (*integer*) – The current X coordinate of the mouse pointer.
        * **y** (*integer*) – The current Y coordinate of the mouse pointer.
        * **mask** (*integer*) – The button mask, representing the pressed or released status of each
          mouse button.

size[#](#client-size-instruction "Link to this definition")
:   Specifies that the client’s optimal screen size has changed from what was
    specified during the handshake, or from previously-sent “size”
    instructions.

    Arguments:
    :   * **width** (*integer*) – The new, optimal screen width.
        * **height** (*integer*) – The new, optimal screen height.

## Status codes[#](#status-codes "Link to this heading")

Several Guacamole instructions, and various other internals of the Guacamole
core, use a common set of numeric status codes. These codes denote success or
failure of operations, and can be rendered by user interfaces in a
human-readable way.

0 (`SUCCESS`)
:   The operation succeeded. No error.

256 (`UNSUPPORTED`)
:   The requested operation is unsupported.

512 (`SERVER_ERROR`)
:   An internal error occurred, and the operation could not be performed.

513 (`SERVER_BUSY`)
:   The operation could not be performed because the server is busy.

514 (`UPSTREAM_TIMEOUT`)
:   The upstream server is not responding. In most cases, the upstream server
    is the remote desktop server.

515 (`UPSTREAM_ERROR`)
:   The upstream server encountered an error. In most cases, the upstream
    server is the remote desktop server.

516 (`RESOURCE_NOT_FOUND`)
:   An associated resource, such as a file or stream, could not be found, and
    thus the operation failed.

517 (`RESOURCE_CONFLICT`)
:   A resource is already in use or locked, preventing the requested operation.

518 (`RESOURCE_CLOSED`)
:   The requested operation cannot continue because the associated resource has
    been closed.

519 (`UPSTREAM_NOT_FOUND`)
:   The upstream server does not appear to exist, or cannot be reached over the
    network. In most cases, the upstream server is the remote desktop server.

520 (`UPSTREAM_UNAVAILABLE`)
:   The upstream server is refusing to service connections. In most cases, the
    upstream server is the remote desktop server.

521 (`SESSION_CONFLICT`)
:   The session within the upstream server has ended because it conflicts with
    another session. In most cases, the upstream server is the remote desktop
    server.

522 (`SESSION_TIMEOUT`)
:   The session within the upstream server has ended because it appeared to be
    inactive. In most cases, the upstream server is the remote desktop server.

523 (`SESSION_CLOSED`)
:   The session within the upstream server has been forcibly closed. In most
    cases, the upstream server is the remote desktop server.

768 (`CLIENT_BAD_REQUEST`)
:   The parameters of the request are illegal or otherwise invalid.

769 (`CLIENT_UNAUTHORIZED`)
:   Permission was denied, because the user is not logged in. Note that the
    user may be logged into Guacamole, but still not logged in with respect to
    the remote desktop server.

771 (`CLIENT_FORBIDDEN`)
:   Permission was denied, and logging in will not solve the problem.

776 (`CLIENT_TIMEOUT`)
:   The client (usually the user of Guacamole or their browser) is taking too
    long to respond.

781 (`CLIENT_OVERRUN`)
:   The client has sent more data than the protocol allows.

783 (`CLIENT_BAD_TYPE`)
:   The client has sent data of an unexpected or illegal type.

797 (`CLIENT_TOO_MANY`)
:   The client is already using too many resources. Existing resources must be
    freed before further requests are allowed.

## Message Codes[#](#message-codes "Link to this heading")

The msg instruction must have at least one numeric argument that the client
then uses to interpret the message and determine what action, if any, it
should take based on the message. The following numeric codes are currently
implemented for this instruction.

1 (`USER_JOINED`)
:   Notifies the owner of a connection that another user has joined the
    connection. This message is expected to include two additional
    arguments: the guacd-generated UUID of the user who is joining the
    connection, and the arbitrary name of the user provided by the
    client during the handshake.

2 (`USER_LEFT`)
:   Notifies the owner of a connection that another user has left the
    connection. This message is expected to include two additional
    arguments: the guacd-generated UUID of the user who is leaving the
    connection, and the arbitrary name of the user provided by the
    client during the handshake.

Contents

---
# Database setup for PostgreSQL

## Contents

# Database setup for PostgreSQL[#](#database-setup-for-postgresql "Link to this heading")

To use Guacamole with a PostgreSQL database, you will need:

1. An instance of the PostgreSQL database server.
2. Sufficient permission to create new databases, to create new users, and to
   grant those users permissions.
3. Network access to the database from the Guacamole server.

If this is not the case, install PostgreSQL now. Most distributions will
provide a convenient PostgreSQL package which will set up everything for you.
If you prefer Docker, the [`postgres`](https://hub.docker.com/_/postgres)
Docker image is also a reasonable option. If you don’t wish to use PostgreSQL,
Guacamole additionally supports:

* [MariaDB / MySQL](mysql-auth.html)
* [SQL Server](sqlserver-auth.html)

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Creating the Guacamole database[#](#creating-the-guacamole-database "Link to this heading")

It is best practice to use a dedicated database and user for the Guacamole web
application, and these instructions cover only this method.

If using the [`postgres`](https://hub.docker.com/_/postgres) Docker image:
:   Set the `POSTGRES_DB` environment variable to the desired name of the
    database. The Docker image will automatically create this database when the
    container starts for the first time.

If using a native installation of PostgreSQL:
:   Manually create a database for PostgreSQL by executing a
    `CREATE DATABASE` query with the `psql` client:

    ```
    CREATE DATABASE guacamole_db;
    ```

### Initializing the database[#](#initializing-the-database "Link to this heading")

Native Webapp (Tomcat)

The schema scripts necessary to initialize the PostgreSQL version of Guacamole’s
database are provided within the `postgresql/schema/` directory of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download),
which must be downloaded from [the release page for Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
and extracted first.

Running each of these scripts against the newly created database will
initialize it with Guacamole’s schema. You can run these scripts using the
standard `psql` client, but the method of running `psql` varies depending on
whether you are using Docker to provide your database.

If using the [`postgres`](https://hub.docker.com/_/postgres) Docker image:
:   The schema initialization scripts should be run against the newly created
    database by running the standard `psql` command-line client *within the
    container*:

    ```
    $ cat schema/*.sql | docker exec -i some-postgresql \
        psql -U guacamole_user -d guacamole_db -f -
    ```

If using a native installation of PostgreSQL:
:   The schema initialization scripts should be run against the newly created
    database using the standard `psql` client directly from the command-line:

    ```
    $ cat schema/*.sql | psql -d guacamole_db -f -
    ```

Container (Docker)

The schema scripts necessary to initialize the PostgreSQL version of Guacamole’s
database are provided within the `/opt/guacamole/extensions/guacamole-auth-jdbc/postgresql/schema`
directory of the `guacamole/guacamole` image.

Additionally, an `initdb.sh` script is provided at `/opt/guacamole/bin/initdb.sh`
that can be used to extract the required schema initialization script:

```
$ docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --postgresql > initdb.sql
```

If using the [`postgres`](https://hub.docker.com/_/postgres) Docker image via Docker Compose:
:
The easiest way to initialize Guacamole’s database is to use a volume mount to
map the bundled schema initialization scripts from the Guacamole container into
the database container. For example, if using Docker Compose:

1. Declare a named volume at the root level of your `docker-compose.yml`:

   ```
   volumes:
       initdb:
   ```
2. Reference the named volume within your Guacamole service, effectively
   pulling the schema initialization scripts from that container and into the
   volume:

   ```
   volumes:
       - "initdb:/opt/guacamole/extensions/guacamole-auth-jdbc/postgresql/schema:ro"
   ```
3. Reference the named volume within your database service, bringing the
   schema initialization scripts into the directory used by the database
   image for one-time initialization:

   ```
   volumes:
       - "initdb:/docker-entrypoint-initdb.d:ro"
   ```

If using the [`postgres`](https://hub.docker.com/_/postgres) Docker image *without* Docker Compose:
:   Use the `initdb.sh` script included with the `guacamole/guacamole` image to
    send the required initialization script to the standard `psql` command-line
    client *within the database container*:

    ```
    $ docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --postgresql | \
        docker exec -i some-postgresql psql -U guacamole_user -d guacamole_db -f -
    ```

If using a native installation of PostgreSQL:
:   Use the `initdb.sh` script included with the `guacamole/guacamole` image to
    automatically produce the SQL required to initialize an existing database:

    ```
    $ docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --postgresql | \
        psql -d guacamole_db -f -
    ```

## Granting Guacamole access to the database[#](#granting-guacamole-access-to-the-database "Link to this heading")

For Guacamole to be able to execute queries against the database, you must
create a new user for the database and grant that user sufficient privileges to
manage the contents of all tables in the database.

If using the [`postgres`](https://hub.docker.com/_/postgres) Docker image:
:   Set the `POSTGRES_USER` environment variable to the desired name of the
    dedicated user, and the `POSTGRES_PASSWORD` environment variable to the
    desired password. The Docker image will automatically create this user when
    the container starts and grant them full access to the Guacamole database.

If using a native installation of PostgreSQL:
:   The dedicated user for Guacamole must be manually created and granted
    sufficient privileges. The user created for Guacamole needs only `SELECT`,
    `UPDATE`, `INSERT`, and `DELETE` permissions on all tables in the Guacamole
    database, as well as `SELECT` and `USAGE` permission on all sequences within
    all Guacamole tables.

    ```
    CREATE USER guacamole_user WITH PASSWORD 'some_password';
    GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA public TO guacamole_user;
    GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public TO guacamole_user;
    ```

## Upgrading an existing Guacamole database[#](#upgrading-an-existing-guacamole-database "Link to this heading")

If you are upgrading from a version of Guacamole older than 1.6.0, you
may need to run one or more database schema upgrade scripts located within the
`postgresql/schema/upgrade/` directory of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download)
(available from [the release page for Apache Guacamole
1.6.0](https://guacamole.apache.org/releases/1.6.0)).

Each of these scripts is named `upgrade-pre-VERSION.sql` where
`VERSION` is the version of Guacamole where those changes were introduced. They
need to be run when you are upgrading from a version of Guacamole older than
`VERSION`.

If there are no `upgrade-pre-VERSION.sql` scripts present in the
`schema/upgrade/` directory which apply to your existing Guacamole database,
then the schema has not changed between your version and the version your are
installing, and there is no need to run any database upgrade scripts.

These scripts are incremental and, when relevant, *must be run in order*. For
example, if you are upgrading an existing database from version
0.9.13-incubating to version 1.0.0, you would need to run the
`upgrade-pre-0.9.14.sql` script (because 0.9.13-incubating is older than
0.9.14), followed by the `upgrade-pre-1.0.0.sql` script (because
0.9.13-incubating is also older than 1.0.0).

Important

Because the permissions granted to the Guacamole-specific PostgreSQL user when
the database was first created will not automatically be granted for any new
tables and sequences, you will also need to re-grant those permissions after
applying any upgrade relevant scripts:

```
GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA public TO guacamole_user;
GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public TO guacamole_user;
```

## Installing/Enabling support for PostgreSQL[#](#installing-enabling-support-for-postgresql "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. You should have a copy of [`guacamole-auth-jdbc-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-jdbc-1.6.0.tar.gz?action=download) from
   earlier when you [created and initialized the database](#postgresql-auth-database-creation).
2. Create the `GUACAMOLE_HOME/extensions` and `GUACAMOLE_HOME/lib` directories,
   if they do not already exist.
3. Copy `postgresql/guacamole-auth-jdbc-postgresql-1.6.0.jar`
   within `GUACAMOLE_HOME/extensions`.
4. Copy the JDBC driver for your database to `GUACAMOLE_HOME/lib`.
   For PostgreSQL, the proper driver is [the JDBC driver provided by the
   PostgreSQL project](https://jdbc.postgresql.org/download/#latest-versions).
5. Configure Guacamole to use database authentication, as described below.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `POSTGRESQL_ENABLED` environment variable:

    ```
    POSTGRESQL_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e POSTGRESQL_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `POSTGRESQL_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `POSTGRESQL_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Required configuration[#](#required-configuration "Link to this heading")

Additional configuration options must be specified for Guacamole to properly
connect to your database. These options are specific to the database being
used, and must be set correctly for authentication to work.

The options absolutely required by the database authentication extension are
relatively few and self-explanatory, describing only which database will be
used and how Guacamole will authenticate when querying that database:

Native Webapp (Tomcat)

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
postgresql-database: guacamole_db
postgresql-username: guacamole_user
postgresql-password: some_password
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`postgresql-database`
:   The name of the database that you created for Guacamole. This is given as
    “guacamole\_db” in the examples given in this chapter.

`postgresql-username`
:   The username of the user that Guacamole should use to connect to the
    database. This is given as “guacamole\_user” in the examples given in this
    chapter.

`postgresql-password`
:   The password Guacamole should provide when authenticating with the database.
    This is given as “some\_password” in the examples given in this chapter.

Container (Docker)

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
POSTGRESQL_DATABASE: 'guacamole_db'
POSTGRESQL_USERNAME: 'guacamole_user'
POSTGRESQL_PASSWORD: 'some_password'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e POSTGRESQL_DATABASE="guacamole_db" \
    -e POSTGRESQL_USERNAME="guacamole_user" \
    -e POSTGRESQL_PASSWORD="some_password" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`POSTGRESQL_DATABASE`
:   The name of the database that you created for Guacamole. This is given as
    “guacamole\_db” in the examples given in this chapter.

`POSTGRESQL_USERNAME`
:   The username of the user that Guacamole should use to connect to the
    database. This is given as “guacamole\_user” in the examples given in this
    chapter.

`POSTGRESQL_PASSWORD`
:   The password Guacamole should provide when authenticating with the database.
    This is given as “some\_password” in the examples given in this chapter.

Hint

**Double-check these values.** You will not be able to sign into Guacamole
after installation if these parameters do not match the correct database name,
username, and password.

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Additional options are available to control how Guacamole connects to the
database server:

Native Webapp (Tomcat)

`postgresql-hostname`
:   The hostname or IP address of the server hosting your database. If not
    specified, “localhost” will be used by default.

`postgresql-port`
:   The port number of the PostgreSQL database to connect to. If not specified,
    the standard PostgreSQL port 5432 will be used.

`postgresql-ssl-mode`
:   This property sets the SSL mode that the JDBC extension will attempt to use
    when communicating with the remote PostgreSQL server. The values for this
    property match the standard values supported by the PostgreSQL JDBC driver:

    disable
    :   Do not use SSL, and fail if the server requires it.

    allow
    :   If the server requires encryption use it, otherwise prefer unencrypted
        connections.

    prefer
    :   Try SSL connections, first, but allow unencrypted connections if the server
        does not support SSL or if SSL negotiations fail. This is the
        default.

    require
    :   Require SSL connections, but implicitly trust all server certificates and
        authorities.

    verify-ca
    :   Require SSL connections, and verify that the server certificate is issued
        by a known certificate authority.

    verify-full
    :   Require SSL connections, verifying that the server certificate is issued
        by a known authority, and that the name on the certificate matches the name
        of the server.

`postgresql-ssl-cert-file`
:   The file containing the client certificate to be used when making an
    SSL-encrtyped connection to the PostgreSQL server, in PEM format. This
    property is optional, and will be ignored if the SSL mode is set to disable.

`postgresql-ssl-key-file`
:   The file containing the client private key to be used when making an
    SSL-encrypted connection to the PostgreSQL server, in PEM format. This
    property is optional, and will be ignored if the SSL mode is set to disable.

`postgresql-ssl-root-cert-file`
:   The file containing the root and intermedidate certificates against which the
    server certificate will be verified when making an SSL-encrypted connection
    to the PostgreSQL server. This file should contain one or more PEM-formatted
    authority certificates. This property is optional, and will only be used if
    SSL mode is set to verify-ca or verify-full.

    If SSL is set to one of the verification modes and this property is not
    specified, the JDBC driver will attempt to use the `.postgresql/root.crt`
    file from the home directory of the user running the web application server
    (e.g. Tomcat). If this property is not specified and the default file does
    not exist, the PostgreSQL JDBC driver will fail to connect to the server.

`postgresql-ssl-key-password`
:   The password that will be used to access the client private key file, if the
    client private key is encrypted. This property is optional, and is only used
    if the `postgresql-ssl-key-file` property is set and SSL is enabled.

`postgresql-default-statement-timeout`
:   The number of seconds the driver will wait for a response from the database,
    before aborting the query. A value of 0 (the default) means the timeout is
    disabled.

`postgresql-socket-timeout`
:   The number of seconds to wait for socket read operations. If reading from the
    server takes longer than this value, the connection will be closed. This can
    be used to handle network problems such as a dropped connection to the
    database. Similar to `postgresql-default-statement-timeout`, it will also
    abort queries that take too long. A value of 0 (the default) means the
    timeout is disabled.

`postgresql-batch-size`
:   Controls how many objects may be retrieved from the database in a single
    query. If more objects than this number are requested, retrieval of those
    objects will be automatically and transparently split across multiple
    queries.

    By default, PostgreSQL queries will retrieve no more than 5000 objects.

Container (Docker)

`POSTGRESQL_HOSTNAME`
:   The hostname or IP address of the server hosting your database. If not
    specified, “localhost” will be used by default.

`POSTGRESQL_PORT`
:   The port number of the PostgreSQL database to connect to. If not specified,
    the standard PostgreSQL port 5432 will be used.

`POSTGRESQL_SSL_MODE`
:   This property sets the SSL mode that the JDBC extension will attempt to use
    when communicating with the remote PostgreSQL server. The values for this
    property match the standard values supported by the PostgreSQL JDBC driver:

    disable
    :   Do not use SSL, and fail if the server requires it.

    allow
    :   If the server requires encryption use it, otherwise prefer unencrypted
        connections.

    prefer
    :   Try SSL connections, first, but allow unencrypted connections if the server
        does not support SSL or if SSL negotiations fail. This is the
        default.

    require
    :   Require SSL connections, but implicitly trust all server certificates and
        authorities.

    verify-ca
    :   Require SSL connections, and verify that the server certificate is issued
        by a known certificate authority.

    verify-full
    :   Require SSL connections, verifying that the server certificate is issued
        by a known authority, and that the name on the certificate matches the name
        of the server.

`POSTGRESQL_SSL_CERT_FILE`
:   The file containing the client certificate to be used when making an
    SSL-encrtyped connection to the PostgreSQL server, in PEM format. This
    property is optional, and will be ignored if the SSL mode is set to disable.

`POSTGRESQL_SSL_KEY_FILE`
:   The file containing the client private key to be used when making an
    SSL-encrypted connection to the PostgreSQL server, in PEM format. This
    property is optional, and will be ignored if the SSL mode is set to disable.

`POSTGRESQL_SSL_ROOT_CERT_FILE`
:   The file containing the root and intermedidate certificates against which the
    server certificate will be verified when making an SSL-encrypted connection
    to the PostgreSQL server. This file should contain one or more PEM-formatted
    authority certificates. This property is optional, and will only be used if
    SSL mode is set to verify-ca or verify-full.

    If SSL is set to one of the verification modes and this property is not
    specified, the JDBC driver will attempt to use the `.postgresql/root.crt`
    file from the home directory of the user running the web application server
    (e.g. Tomcat). If this property is not specified and the default file does
    not exist, the PostgreSQL JDBC driver will fail to connect to the server.

`POSTGRESQL_SSL_KEY_PASSWORD`
:   The password that will be used to access the client private key file, if the
    client private key is encrypted. This property is optional, and is only used
    if the `postgresql-ssl-key-file` property is set and SSL is enabled.

`POSTGRESQL_DEFAULT_STATEMENT_TIMEOUT`
:   The number of seconds the driver will wait for a response from the database,
    before aborting the query. A value of 0 (the default) means the timeout is
    disabled.

`POSTGRESQL_SOCKET_TIMEOUT`
:   The number of seconds to wait for socket read operations. If reading from the
    server takes longer than this value, the connection will be closed. This can
    be used to handle network problems such as a dropped connection to the
    database. Similar to `postgresql-default-statement-timeout`, it will also
    abort queries that take too long. A value of 0 (the default) means the
    timeout is disabled.

`POSTGRESQL_BATCH_SIZE`
:   Controls how many objects may be retrieved from the database in a single
    query. If more objects than this number are requested, retrieval of those
    objects will be automatically and transparently split across multiple
    queries.

    By default, PostgreSQL queries will retrieve no more than 5000 objects.

### Enforcing password policies[#](#enforcing-password-policies "Link to this heading")

Configuration options are available for enforcing rules intended to encourage
password complexity and regular changing of passwords. None of these options
are enabled by default, but can be selectively enabled as needed.

#### Password complexity[#](#password-complexity "Link to this heading")

Administrators can require that passwords have a certain level of complexity,
such as having both uppercase and lowercase letters (“multiple case”), at least
one digit, or at least one symbol, and can prohibit passwords from containing
the user’s own username.

With respect to password content, the database authentication defines a “digit”
as any numeric character and a “symbol” is any non-alphanumeric character. This
takes non-English languages into account, thus a digit is not simply “0”
through “9” but rather [any character defined in Unicode as
numeric](https://en.wikipedia.org/wiki/Numerals_in_Unicode), and a symbol is
any character which Unicode does not define as alphabetic or numeric.

The check for whether a password contains the user’s own username is performed
in a case-insensitive manner. For example, if the user’s username is “phil”,
the passwords “ch!0roPhil” and “PHIL-o-dendr0n” would still be prohibited.

Native Webapp (Tomcat)

`postgresql-user-password-min-length`
:   The minimum length required of all user passwords, in characters. By default,
    password length is not enforced.

`postgresql-user-password-require-multiple-case`
:   Whether all user passwords must have at least one lowercase character and one
    uppercase character. By default, no such restriction is imposed.

`postgresql-user-password-require-symbol`
:   Whether all user passwords must have at least one non-alphanumeric character
    (symbol). By default, no such restriction is imposed.

`postgresql-user-password-require-digit`
:   Whether all user passwords must have at least one numeric character (digit).
    By default, no such restriction is imposed.

`postgresql-user-password-prohibit-username`
:   Whether users are prohibited from including their own username in their
    password. By default, no such restriction is imposed.

Container (Docker)

`POSTGRESQL_USER_PASSWORD_MIN_LENGTH`
:   The minimum length required of all user passwords, in characters. By default,
    password length is not enforced.

`POSTGRESQL_USER_PASSWORD_REQUIRE_MULTIPLE_CASE`
:   Whether all user passwords must have at least one lowercase character and one
    uppercase character. By default, no such restriction is imposed.

`POSTGRESQL_USER_PASSWORD_REQUIRE_SYMBOL`
:   Whether all user passwords must have at least one non-alphanumeric character
    (symbol). By default, no such restriction is imposed.

`POSTGRESQL_USER_PASSWORD_REQUIRE_DIGIT`
:   Whether all user passwords must have at least one numeric character (digit).
    By default, no such restriction is imposed.

`POSTGRESQL_USER_PASSWORD_PROHIBIT_USERNAME`
:   Whether users are prohibited from including their own username in their
    password. By default, no such restriction is imposed.

#### Password age / expiration[#](#password-age-expiration "Link to this heading")

“Password age” refers to two separate concepts:

1. Requiring users to change their password after a certain amount of time has
   elapsed since the last password change (maximum password age).
2. Preventing users from changing their password too frequently (minimum
   password age).

While it may seem strange to prevent users from changing their password too
frequently, it does make sense if you are concerned that rapid password changes
may defeat password expiration (users could immediately change the password
back) or tracking of password history (users could cycle through passwords
until the history is exhausted and their old password is usable again).

By default, the database authentication does not apply any limits to password
age, and users with permission to change their passwords may do so as
frequently or infrequently as they wish. Password age limits can be enabled
using a pair of configuration options, each accepting values given in units of
days:

Native Webapp (Tomcat)

`postgresql-user-password-min-age`
:   The minimum number of days which must elapse before a user may reset their
    password, where zero represents no limit. By default, no minimum number of
    days is required.

`postgresql-user-password-max-age`
:   The maximum number of days which may elapse before a user is automatically
    required to reset their password, where zero represents no limit. By default,
    users are not automatically required to reset their password based on
    password age.

Container (Docker)

`POSTGRESQL_USER_PASSWORD_MIN_AGE`
:   The minimum number of days which must elapse before a user may reset their
    password, where zero represents no limit. By default, no minimum number of
    days is required.

`POSTGRESQL_USER_PASSWORD_MAX_AGE`
:   The maximum number of days which may elapse before a user is automatically
    required to reset their password, where zero represents no limit. By default,
    users are not automatically required to reset their password based on
    password age.

Important

So that administrators can always intervene in the case that a password needs
to be reset despite restrictions, the minimum age restriction does not apply to
any user with permission to administer the system.

#### Preventing password reuse[#](#preventing-password-reuse "Link to this heading")

If desired, Guacamole can keep track of each user’s most recently used
passwords, and will prohibit reuse of those passwords until the password has
been changed sufficiently many times. By default, Guacamole will not keep track
of old passwords.

Note that these passwords are hashed in the same manner as each user’s current
password. When a user’s password is changed, the hash, salt, etc. currently
stored for that user is actually just copied verbatim (along with a timestamp)
into a list of historical passwords, with older entries from this list being
automatically deleted.

Native Webapp (Tomcat)

`postgresql-user-password-history-size`
:   The number of previous passwords remembered for each user, where zero
    represents no history. If set to a non-zero value, users will be restricted
    from reusing any password in their password history. Passwords are remembered
    only in hashed and salted form. By default, previous passwords are not
    remembered and no such restriction is enforced.

Container (Docker)

`POSTGRESQL_USER_PASSWORD_HISTORY_SIZE`
:   The number of previous passwords remembered for each user, where zero
    represents no history. If set to a non-zero value, users will be restricted
    from reusing any password in their password history. Passwords are remembered
    only in hashed and salted form. By default, previous passwords are not
    remembered and no such restriction is enforced.

### Concurrent use of Guacamole connections[#](#concurrent-use-of-guacamole-connections "Link to this heading")

The database authentication module provides configuration options to restrict
concurrent use of connections and connection groups. Concurrent use can be
restricted broadly or to ensure that each individual user may only maintain a
limited number of active connections to any one connection or group.

By default, concurrent usage is unrestricted except that each user may only
have a single active connection to each connection group. This is intended to
avoid the case that a single user is able to exhaust the contents of a
connection group and effectively block others from using the same resources.

If you wish to impose an absolute limit on the number of active connections
that can be established through Guacamole, ignoring which users or connections
are involved, this can be done as well.

The default policy set through these options can be overridden later on a
per-connection basis using the administrative interface.

Native Webapp (Tomcat)

`postgresql-default-max-connections`
:   The maximum number of concurrent connections to allow to any one connection,
    regardless of which user is accessing the connection, where zero denotes
    unlimited. By default, overall concurrent access to individual connections is
    not limited.

`postgresql-default-max-group-connections`
:   The maximum number of concurrent connections to allow to any one connection
    group, regardless of which user is accessing the connection group, where zero
    denotes unlimited. By default, overall concurrent access to individual
    connection groups is not limited.

`postgresql-default-max-connections-per-user`
:   The maximum number of concurrent connections to allow to any one connection
    by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to individual connections is not limited.

`postgresql-default-max-group-connections-per-user`
:   The maximum number of concurrent connections to allow to any one connection
    group by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to connection groups is limited to one user.

`postgresql-absolute-max-connections`
:   The maximum number of concurrent connections to allow overall, regardless of
    which connection or connection group is used and regardless of which user is
    accessing the connection/group, where zero denotes unlimited. By default,
    overall concurrent access to Guacamole is not limited.

Container (Docker)

`POSTGRESQL_DEFAULT_MAX_CONNECTIONS`
:   The maximum number of concurrent connections to allow to any one connection,
    regardless of which user is accessing the connection, where zero denotes
    unlimited. By default, overall concurrent access to individual connections is
    not limited.

`POSTGRESQL_DEFAULT_MAX_GROUP_CONNECTIONS`
:   The maximum number of concurrent connections to allow to any one connection
    group, regardless of which user is accessing the connection group, where zero
    denotes unlimited. By default, overall concurrent access to individual
    connection groups is not limited.

`POSTGRESQL_DEFAULT_MAX_CONNECTIONS_PER_USER`
:   The maximum number of concurrent connections to allow to any one connection
    by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to individual connections is not limited.

`POSTGRESQL_DEFAULT_MAX_GROUP_CONNECTIONS_PER_USER`
:   The maximum number of concurrent connections to allow to any one connection
    group by the same user, where zero denotes unlimited. By default, per-user
    concurrent access to connection groups is limited to one user.

`POSTGRESQL_ABSOLUTE_MAX_CONNECTIONS`
:   The maximum number of concurrent connections to allow overall, regardless of
    which connection or connection group is used and regardless of which user is
    accessing the connection/group, where zero denotes unlimited. By default,
    overall concurrent access to Guacamole is not limited.

### External users and connections[#](#external-users-and-connections "Link to this heading")

When [combining LDAP with a database](ldap-auth.html#ldap-and-database), or using a single
sign-on system like [OpenID Connect](openid-auth.html) or [SAML](saml-auth.html), user
accounts are not purely defined by Guacamole’s database. They are additionally
defined by the relevant external system. In some cases, such as the [LDAP
extension’s capability to retrieve connection information from the LDAP
directory](ldap-auth.html#ldap-schema-changes), connections are not purely defined by
Guacamole’s database either.

In these cases, it may be desirable to:

* Limit use of Guacamole to only those users that *do* already exist in the
  database.
* Automatically create users in the database when they have successfully
  authenticated through other means, such that extensions requiring storage
  like TOTP can be used alongside SSO solutions.
* Control whether the database logs connection usage history for connections
  that are not maintained by the database.

By default, users will be allowed access to Guacamole as long as they are
authenticated by at least one extension, no extension denies/vetoes access, and
the database will record connection history entries for all connections
regardless of whether they are maintained by the database.

Note

In all cases, users will only be able to see or interact with resources that
they have been given permission to access. This is true whether those
permissions are granted explicitly or through inheritance (from user groups).

Native Webapp (Tomcat)

`postgresql-user-required`
:   Whether a user account within the database is required for authentication to
    succeed, even if the user has been authenticated via another extension. By
    default, successful authentication via any extension is sufficient, and
    database user accounts are not strictly required.

`postgresql-auto-create-accounts`
:   Whether to automatically create user accounts in the database for users who
    have successfully authenticate through another extension. Users that are
    automatically created are granted `READ` permission on their own user account
    and no other explicit permissions. By default users will not be automatically
    created.

`postgresql-track-external-connection-history`
:   Whether connection history records should be created for connections not
    defined in the database. By default, external connection history will be
    tracked unless this is explicitly disabled by setting this to “false”.

Container (Docker)

`POSTGRESQL_USER_REQUIRED`
:   Whether a user account within the database is required for authentication to
    succeed, even if the user has been authenticated via another extension. By
    default, successful authentication via any extension is sufficient, and
    database user accounts are not strictly required.

`POSTGRESQL_AUTO_CREATE_ACCOUNTS`
:   Whether to automatically create user accounts in the database for users who
    have successfully authenticate through another extension. Users that are
    automatically created are granted `READ` permission on their own user account
    and no other explicit permissions. By default users will not be automatically
    created.

`POSTGRESQL_TRACK_EXTERNAL_CONNECTION_HISTORY`
:   Whether connection history records should be created for connections not
    defined in the database. By default, external connection history will be
    tracked unless this is explicitly disabled by setting this to “false”.

### Access window enforcment[#](#access-window-enforcment "Link to this heading")

Guacamole supports the use of access windows to limit the time periods during
which users are allowed to access the system. By default, users will be
forcibly logged out from Guacamole as soon as the access window expires,
disconnecting them from any active connections.

If you would prefer users to be allowed to remain logged in, this behavior can
be overridden using the configuration option below.

Note

Prior to [Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0),
access windows were enforced only during the login process. Access windows
restricted only when a user could log in, not whether they could remain logged
in.

Native Webapp (Tomcat)

`postgresql-enforce-access-windows-for-active-sessions`
:   Whether time-based access windows should be enforced for active user sessions.
    By default, users will be logged out when an access window closes, even if
    they are currently logged in. To allow logged-in users to continue to use the
    application after an access window closes, set this to “false”. Users will
    always be prevented from logging in outside of access windows regardless of
    this setting.

Container (Docker)

`POSTGRESQL_ENFORCE_ACCESS_WINDOWS_FOR_ACTIVE_SESSIONS`
:   Whether time-based access windows should be enforced for active user sessions.
    By default, users will be logged out when an access window closes, even if
    they are currently logged in. To allow logged-in users to continue to use the
    application after an access window closes, set this to “false”. Users will
    always be prevented from logging in outside of access windows regardless of
    this setting.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Logging in[#](#logging-in "Link to this heading")

The default Guacamole user created by the provided SQL scripts is
“`guacadmin`”, with a default password of “`guacadmin`”. Once you have verified
that the database authentication is working, **you should [change your password
immediately](using-guacamole.html#changing-password)**.

Once you have successfully logged in and changed your password, you can begin
using the web UI to create other users, groups, and connections. More detailed
instructions for doing this are given in [Guacamole’s administrative interface](administration.html).

Contents

---
# Database authentication

## Contents

# Database authentication[#](#database-authentication "Link to this heading")

Guacamole supports providing authentication and storage leveraging any of the
following databases:

* [MariaDB or MySQL](mysql-auth.html)
* [PostgreSQL](postgresql-auth.html)
* [SQL Server](sqlserver-auth.html)

Using a database for authentication/storage is *highly recommended* and
provides additional features, such as the ability to use load-balancing groups,
connection sharing links, and a convenient, web-based administrative interface.

## Using a database alongside other authentication methods[#](#using-a-database-alongside-other-authentication-methods "Link to this heading")

While most authentication extensions function independently, the database
authentication can act in a subordinate role, allowing users and user groups
from other authentication extensions to be associated with connections within
the database.

**Users and groups are considered identical to those within the database if they
have the same names** (with the nature of that comparison dictated by [the
application-wide case sensitivity setting](configuring-guacamole.html#initial-setup)), and the
authentication result of another extension will be trusted if it succeeds. A
user with an account under multiple systems will thus be able to see data from
each system after successfully logging in.

Hint

For more information on using the database authentication alongside other
mechanisms, see [Associating LDAP with a database (recommended)](ldap-auth.html#ldap-and-database) within [LDAP authentication](ldap-auth.html).

Contents

---
# Troubleshooting

## Contents

# Troubleshooting[#](#troubleshooting "Link to this heading")

## It isn’t working[#](#it-isnt-working "Link to this heading")

If Guacamole isn’t working, chances are something isn’t configured properly, or
something is wrong with the network. Thankfully, Guacamole and all its
components log errors thoroughly, so the problem can usually be traced down
fairly easily if you know where to look. Troubleshooting Guacamole usually
boils down to checking either syslog or your servlet container’s logs (likely
Tomcat).

Failing all that, you can always post a question on [one of the project mailing
lists](http://guacamole.apache.org/support/#mailing-lists), or if you truly
feel you’ve discovered a bug, you can [create a new ticket in
JIRA](https://issues.apache.org/jira/browse/GUACAMOLE/). Beware that if
something isn’t working, and there are errors in the logs describing the
problem, [it is usually not a
bug](http://guacamole.apache.org/faq/#probably-not-a-bug), and the best place
to handle such things is through consulting this guide or the mailing lists.

### No graphics appear[#](#no-graphics-appear "Link to this heading")

If you *never* see any graphics appear, or you see “Connecting, waiting for
first update…” for a while and then are disconnected, the most likely cause
is a proxy.

Guacamole relies on streaming data to you over a persistent connection. If
software between Guacamole and your browser is buffering all incoming data,
such as a proxy, this data never makes it to your browser, and you will just
see it wait indefinitely. Eventually, thinking the client has disconnected,
Guacamole closes the connection, at which point the proxy finally flushes its
buffer and you see graphics! … just in time to see it disconnect.

The solution here is to either modify your proxy settings to flush packets
immediately as they are received, or to use HTTPS. Proxies are required to pass
HTTPS through untouched, and this usually solves the problem.

Even if you aren’t aware of any proxy, there may be one in place. Corporate
firewalls very often incorporate proxies. Antivirus software may buffer
incoming data until the connection is closed and the data is scanned for
viruses. Virtualization software may detect HTTP data and buffer the connection
just like a proxy. If all else fails, try HTTPS - it’s the only secure way to
do this anyway.

### Connections involving Unicode don’t work[#](#connections-involving-unicode-dont-work "Link to this heading")

If you are using Tomcat, beware that you *must* set the `URIEncoding="UTF-8"`
attribute on all connectors in your `server.xml`. If you are using a different
servlet container, you need to find out whether it requires special options to
support UTF-8 in URIs, and change the required settings to enable such support.

Without UTF-8 support enabled for URIs, Unicode characters in connection names
will not be received properly when connecting, and Guacamole will think the
connection you requested does not exist. Similarly, if you are using the
built-in administration interface, parameters involving Unicode characters will
not save properly without these options enabled.

## syslog[#](#syslog "Link to this heading")

guacd and libguac-based programs (such as all client plugins) log informational
messages and errors to syslog. Specifically, guacd uses syslog, and it exposes
this logging facility to everything it loads (client plugins), thus if the VNC
or RDP support plugins encounter errors, they log those errors over the logging
facilities exposed by guacd, in this case syslog.

Once you guacd is started, you’ll see entries like the following in syslog:

```
guacd[19663]: Guacamole proxy daemon (guacd) version 0.7.0
guacd[19663]: Unable to bind socket to host ::1, port 4823: Address family
              not supported by protocol
guacd[19663]: Successfully bound socket to host 127.0.0.1, port 4823
guacd[19663]: Exiting and passing control to PID 19665
guacd[19665]: Exiting and passing control to PID 19666
guacd[19666]: Listening on host 127.0.0.1, port 4823
```

Each entry relevant to Guacamole has the prefix “guacd”, denoting the program
that produced the entry, followed by the process ID, followed by the message.
The entries above show guacamole starting successfully and listening on a
non-default port 4823.

### guacd errors[#](#guacd-errors "Link to this heading")

#### Unable to bind socket to any addresses.[#](#unable-to-bind-socket-to-any-addresses "Link to this heading")

This means that guacd failed to start up at all because the port it wants to
listen on is already taken at all addresses attempted. The details of what
guacd tried will be listed in the log entries above this. To solve the problem,
find what port guacd was trying to listen on (the default is 4822) and check if
any other service is listening on that port.

If another service is listening on the default port, you can always specify a
non-standard port for guacd by using the `-l PORT` option (that’s a lowercase
“L”, not a number “1”), where  is the number of the port to listen on.
Beware that you will likely have to modify `guacamole.properties` so that
Guacamole knows how to connect to guacd.

#### Unable to start input thread[#](#unable-to-start-input-thread "Link to this heading")

guacd creates two threads for each connection: one that receives input from the
connected client, and the other that produces output for the client. If either
of these fails to start, the above error will be logged along with the cause.

If it is the output thread that fails to start, the message will instead read:
“Unable to start output thread”.

#### Client finished abnormally[#](#client-finished-abnormally "Link to this heading")

If the client plugin ever returns an error code, this will cause the connection
to immediately terminate, with the cause of the error specific to the plugin in
use. The cause should be detailed in the log messages above the error. If those
log messages don’t make sense, you may have found a bug.

#### Could not fork() parent[#](#could-not-fork-parent "Link to this heading")

When guacd starts up, it immediately attempts to “fork” into the background
(unless instructed otherwise). The word “fork()” above is a reference to the C
function call that does this. There are several calls to this function, each of
which might fail if system resources are lacking or something went wrong at a
low level. If you see this message, it is probably not a bug in Guacamole, but
rather a problem with the load level of your system.

This message may also appear as “Could not fork() group leader”.

#### Unable to change working directory to /[#](#unable-to-change-working-directory-to "Link to this heading")

One of the duties of guacd as it starts up is to change its working directory
to the root directory. This is to prevent locking the current directory in case
it needs to be unmounted, etc. If guacd cannot do this, this error will be
logged, along with the cause.

#### Unable to redirect standard file descriptors to /dev/null[#](#unable-to-redirect-standard-file-descriptors-to-dev-null "Link to this heading")

As guacd starts, it also has to redirect STDOUT, STDERR, and STDIN to
`/dev/null` such that attempts to use these output mechanisms do not pollute
the active console. Though guacd and client plugins will use the exposed
logging facilities (and thus syslog) rather than STDOUT or STDERR, libraries
used by client plugins are often written only from the mindset of a typical
client, and use standard output mechanisms for debug logging. Not redirecting
these would result in undesired output to the console.

If guacd cannot redirect these file descriptors for any reason, this error will
be logged, along with the cause.

#### Error parsing given address or port: HOSTNAME[#](#error-parsing-given-address-or-port-hostname "Link to this heading")

If you specified a host or port to listen on via commandline options, and that
host or port is actually invalid, you will see this error. Fix the
corresponding option and try again.

#### Error opening socket[#](#error-opening-socket "Link to this heading")

When guacd starts up, it needs to open a socket and then listen on that socket.
If it can’t even open the socket, this error will be logged, and guacd will
exit. The cause is most likely related to permissions, and is logged along with
the error.

#### Unable to resolve host[#](#unable-to-resolve-host "Link to this heading")

If the hostname you specified on the commandline cannot be found, you will see
this error. Note that this error is from guacd, and does not relate to whatever
remote desktop servers you may be trying to use; it relates only to the host
guacd is trying to listen on. Check the hostname or IP address specified on the
commandline. If that checks out, there may be a problem with your DNS or your
network.

#### Could not become a daemon[#](#could-not-become-a-daemon "Link to this heading")

In order to become a “daemon” (that is, in order to run in the background as a
system process), guacd must create and exit from several processes, redirect
file descriptors, etc. If any of these steps fails, guacd will not become a
daemon, and it will log this message and exit. The reason guacd could not
become a daemon will be in the previous error message in the logs.

#### Could not write PID file[#](#could-not-write-pid-file "Link to this heading")

guacd offers a commandline option that lets you specify a file that it should
write its process ID into, which is useful for init scripts. If you see this
error, it likely means the user guacd is running as does not have permission to
write this file. The true cause of the error will be logged in the same entry.
Check which user guacd is running as, and then check that it has write
permission to the file in question.

#### Could not listen on socket[#](#could-not-listen-on-socket "Link to this heading")

When guacd starts up, it needs to listen on the socket it just opened in order
to accept connections. If it cannot listen on the socket, clients will be
unable to connect. If, for any reason, guacd is unable to listen on the socket,
guacd will exit and log this message along with the cause, which is most likely
a low-level system resource problem.

#### Could not accept client connection[#](#could-not-accept-client-connection "Link to this heading")

When a client connects to guacd, it must accept the connection in order for
communication to ensue. If it cannot even accept the connection, no
communication between server and client will happen, and this error will be
logged. The cause of the error will be logged in the same entry. Possible
causes include permissions problems, or lack of server resources.

#### Error forking child process[#](#error-forking-child-process "Link to this heading")

When a client connects to guacd, it must create a new process to handle the
connection while the old guacd process continues to listen for new connections.
If, for any reason, guacd cannot create this process, the connection from that
client will be denied, and the cause of the error will be logged. Possible
causes include permissions problems, or lack of server resources.

#### Error closing daemon reference to child descriptor[#](#error-closing-daemon-reference-to-child-descriptor "Link to this heading")

When guacd receives a connection, and it creates a new process to handle that
connection, it gains a copy of the file descriptor that the client will use for
communication. As this connection can never be closed unless all references to
the descriptor are closed, the server must close its copy such that the client
is the only remaining holder of the file descriptor. If the server cannot close
the descriptor, it will log this error message along with the cause.

#### Error sending “sync” instruction[#](#error-sending-sync-instruction "Link to this heading")

During the course of a Guacamole session, guacd must occasionally “ping” the
client to make sure it is still alive. This ping takes the form of a “sync”
instruction, which the client is obligated to respond to as soon as it is
received. If guacd cannot send this instruction, this error will be logged,
along with the cause. Chances are the connection has simply been closed, and
this error can be ignored.

#### Error flushing output[#](#error-flushing-output "Link to this heading")

After the client plugin is finished (for the time being) with handling server
messages, the socket is automatically flushed. If the server cannot flush this
socket for some reason, such as the connection already being closed, you will
see this error. Normally, this error does not indicate a problem, but rather
that the client has simply closed the connection.

#### Error handling server messages[#](#error-handling-server-messages "Link to this heading")

While the client plugin is running, guacd will occasionally ask the plugin to
check and handle any messages that it may have received from the server it
connected to. If the client plugin fails for some reason while doing this, this
error will be logged, and the cause of the error will likely be logged in
previous log entries by the client plugin.

#### Error reading instruction[#](#error-reading-instruction "Link to this heading")

During the course of a Guacamole session, instructions are sent from client to
server which are to be handled by the client plugin. If an instruction cannot
be read, this error will be logged. Usually this means simply that the
connection was closed, but it could also indicate that the version of the
client in use is so old that it doesn’t support the current Guacamole protocol
at all. If the cause looks like the connection was closed (end of stream
reached, etc.), this log entry can be ignored. Otherwise, if the first two
numbers of the version numbers of all Guacamole components match, you have
probably found a bug.

#### Client instruction handler error[#](#client-instruction-handler-error "Link to this heading")

This error indicates that a client plugin failed inside the handler for a
specific instruction. When the server receives instructions from the client, it
then invokes specific instruction handlers within the client plugin. In
general, this error is not useful to a user or system administrator. If the
cause looks benign, such as reaching the end of a stream (the connection
closed), it can be ignored as normal. Otherwise, this error can indicate a bug
either in the client plugin or in a library used by the client plugin.

It can also indicate a problem in the remote desktop server which is causing
the client plugin to fail while communicating with it.

#### Error reading OPCODE[#](#error-reading-opcode "Link to this heading")

During the handshake of the Guacamole protocol, the server expects a very
specific sequence of instructions to be received. If the wrong instructions are
received, or the connection is abruptly closed during the handshake, the above
error will occur.

In the case that the cause is the connection closing, this is normal, and
probably just means that the client disconnected before the initial handshake
completed.

If the connection was not closed abruptly, but instead the wrong instruction
was received, this could mean either that the connecting client is from an
incompatible version of Guacamole (and thus does not know the proper handshake
procedure) or you have found a bug. Check whether all installed components came
from the same upstream release bundle.

#### Error sending “args”[#](#error-sending-args "Link to this heading")

During the handshake of the Guacamole protocol, the server must expose all
parameters used by the client plugin via the args instruction. If this cannot
be sent, you will see this error in the logs. The cause will be included in the
error message, and usually just indicates that the connection was closed during
the handshake, and thus the handshake cannot continue.

#### Error loading client plugin[#](#error-loading-client-plugin "Link to this heading")

When the client connects, it sends an instruction to guacd informing it what
protocol it wishes to use. If the corresponding client plugin cannot be found
or used for any reason, this message will appear in the logs. Normally this
indicates that the corresponding client plugin is not actually installed. The
cause listed after the error message will indicate whether this is the case.

#### Error instantiating client[#](#error-instantiating-client "Link to this heading")

After the client plugin is loaded, an initialization function provided by the
client plugin is invoked. If this function fails, then the client itself cannot
be created, and this error will be logged. Usually this indicates that one or
more of the parameters given to the client plugin are incorrect or malformed.
Check the configuration of the connection in use at the time.

### libguac-client-vnc errors[#](#libguac-client-vnc-errors "Link to this heading")

#### Error waiting for VNC message[#](#error-waiting-for-vnc-message "Link to this heading")

The VNC client plugin must wait for messages sent by the VNC server, and handle
them when they arrive. If there was an error while waiting for a message from
the VNC server, this error message will be displayed. Usually this means that
the VNC server closed the connection, or there is a problem with the VNC server
itself, but the true cause of the error will be logged.

#### Error handling VNC server message[#](#error-handling-vnc-server-message "Link to this heading")

When messages are received from the VNC server, libvncclient must handle them
and then invoke the functions of libguac-client-vnc as necessary. If
libvncclient fails during the handling of a received message, this error will
be logged, along with (hopefully) the cause. This may indicate a problem with
the VNC server, or a lack of support within libvncclient.

#### Wrong argument count received[#](#wrong-argument-count-received "Link to this heading")

The connecting client is required to send exactly the same number of arguments
as requested by the client plugin. If you see this message, it means there is a
bug in the client connecting to guacd, most likely the web application.

### libguac-client-rdp errors[#](#libguac-client-rdp-errors "Link to this heading")

#### Invalid PARAMETER[#](#invalid-parameter "Link to this heading")

If one of the parameters given, such as “width”, “height”, or “color-depth”, is
invalid (not an integer, for example), you will receive this error. Check the
parameters of the connection in use and try again.

#### Support for the CLIPRDR channel (clipboard redirection) could not be loaded[#](#support-for-the-cliprdr-channel-clipboard-redirection-could-not-be-loaded "Link to this heading")

FreeRDP provides a plugin which provides clipboard support for RDP. This plugin
is typically built into FreeRDP, but some distributions may bundle this
separately. libguac-client-rdp loads this plugin in order to support clipboard,
as well. If this plugin could not be loaded, then clipboard support will not be
available, and the reason will be logged.

#### Cannot create static channel “NAME”: failed to load “guac-common-svc” plugin for FreeRDP[#](#cannot-create-static-channel-name-failed-to-load-guac-common-svc-plugin-for-freerdp "Link to this heading")

RDP provides support for much of its feature set through static virtual
channels. Sound support, for example is provided through the “RDPSND” channel.
Device redirection for printers and drives is provided through “RDPDR”. To
support these and other static virtual channels, libguac-client-rdp builds a
plugin for FreeRDP called “guac-common-svc” which allows Guacamole to hook into
the parts of FreeRDP that support virtual channels.

If libguac-client-rdp cannot load this plugin, support for any features which
leverage static virtual channels will not work, and the reason will be logged.
A likely explanation is that libguac-client-rdp was built from source, and the
directory specified for FreeRDP’s installation location was incorrect. For
FreeRDP to be able to find plugins, those plugins must be placed in the
`freerdp2/` subdirectory of whichever directory contains the `libfreerdp2.so`
library.

#### Server requested unsupported clipboard data type[#](#server-requested-unsupported-clipboard-data-type "Link to this heading")

When clipboard support is loaded, libguac-client-rdp informs the RDP server of
all supported clipboard data types. The RDP server is required to send only
those types supported by the client. If the server decides to send an
unsupported type anyway, libguac-client-rdp ignores the data sent, and logs
this message.

#### Clipboard data missing null terminator[#](#clipboard-data-missing-null-terminator "Link to this heading")

When text is sent via a clipboard message, it is required to have a terminating
null byte. If this is not the case, the clipboard data is invalid, and
libguac-client-rdp ignores it, logging this error message.

## Servlet container logs[#](#servlet-container-logs "Link to this heading")

Your servlet container will have logs which the web application side of
Guacamole will log errors to. In the case of Tomcat, this is usually
`catalina.out` or `HOSTNAME.log` (for example, `localhost.log`).

### `user-mapping.xml` errors[#](#user-mapping-xml-errors "Link to this heading")

Errors in the relating to the `user-mapping.xml` file usually indicate that
either the XML is malformed, or the file itself cannot be found.

#### Attribute “name” required for connection tag[#](#attribute-name-required-for-connection-tag "Link to this heading")

If you specify a connection with a `<connection>` tag, it must have a
corresponding name set via the `name` attribute. If it does not, then the XML
is malformed, and this error will be logged. No users will be able to login.

#### Attribute “name” required for param tag[#](#attribute-name-required-for-param-tag "Link to this heading")

Each parameter specified with a `<param>` tag must have a corresponding name
set via the `name` attribute. If it does not, then the XML is malformed, and
this error will be logged. No users will be able to login.

#### Unexpected character data[#](#unexpected-character-data "Link to this heading")

Character data (text not within angle brackets) can only exist within the
`<param>` tag. If it exists elsewhere, then the XML is malformed, and this
error will be logged. No users will be able to login.

#### Invalid encoding type[#](#invalid-encoding-type "Link to this heading")

There are only two legal values for the `encoding` attribute of the
`<authorize>` tag: `plain` (indicating plain text) and `md5` (indicating a
value hashed with the MD5 digest). If any other value is used, then the XML is
malformed, and this error will be logged. No users will be able to login.

#### User mapping could not be read[#](#user-mapping-could-not-be-read "Link to this heading")

If for any reason the user mapping file cannot be read (the servlet container
lacks read permission for the file, the file does not exist, etc.), this error
will be logged. Check `guacamole.properties` to see where the user mapping file
is specified to exist, and then check that is both exists and is readable by
your servlet container.

### `guacamole.properties` errors[#](#guacamole-properties-errors "Link to this heading")

If a property is malformed or a required property is missing, an error
describing the problem will be logged.

#### Property PROPERTY is required[#](#property-property-is-required "Link to this heading")

If Guacamole or an extension of Guacamole requires a specific property in
`guacamole.properties`, but this property is not defined, this error will be
logged. Check which properties are required by the authentication provider (or
other extensions) in use, and then compare that against the properties within
`guacamole.properties`.

### Authentication errors[#](#authentication-errors "Link to this heading")

If someone attempts to login with invalid credentials, or someone attempts to
access a resource or connection that does not exist or they do not have access
to, errors regarding the invalid attempt will be logged.

#### Cannot connect - user not logged in[#](#cannot-connect-user-not-logged-in "Link to this heading")

A user attempted to connect using the HTTP tunnel, and while the tunnel does
exist and is attached to their session, they are not actually logged in.
Normally, this isn’t strictly possible, as a user has to have logged in for a
tunnel to be attached to their session, but as it isn’t an impossibility, this
error does exist. If you see this error, it could mean that the user logged out
at the same time that they made a connection attempt.

#### Requested configuration is not authorized[#](#requested-configuration-is-not-authorized "Link to this heading")

A user attempted to connect to a configuration with a given ID, and while that
configuration does exist, they are not authorized to use it. This could mean
that the user is trying to access things they have no privileges for, or that
they are trying to access configurations they legitimately should, but are
actually logged out.

#### User has no session[#](#user-has-no-session "Link to this heading")

A user attempted to access a page that needs data from their session, but their
session does not actually exist. This usually means the user has not logged in,
as sessions are created through the login process.

### Tunnel errors[#](#tunnel-errors "Link to this heading")

The tunnel frequently returns errors if guacd is killed, the connection is
closed, or the client abruptly closes the connection.

#### No such tunnel[#](#no-such-tunnel "Link to this heading")

An attempt was made to use a tunnel which does not actually exist. This is
usually just the JavaScript client sending a leftover message or two while it
hasn’t realized that the server has disconnected. If this error happens
consistently and is associated with Guacamole generally not working, it could
be a bug.

#### No tunnel created[#](#no-tunnel-created "Link to this heading")

A connection attempt for a specific configuration was made, but the connection
failed, and no tunnel was created. This is usually because the user was not
authorized to use that connection, and thus no tunnel was created for access to
that connection.

#### No query string provided[#](#no-query-string-provided "Link to this heading")

When the JavaScript client is communicating with the HTTP tunnel, it *must*
provide data in the query string describing whether it wants to connect, read,
or write. If this data is missing as the error indicates, there is a bug in the
HTTP tunnel.

#### Tunnel reached end of stream[#](#tunnel-reached-end-of-stream "Link to this heading")

An attempt to read from the tunnel was made, but the tunnel in question has
already reached the end of stream (the connection is closed). This is mostly an
informative error, and can be ignored.

#### Tunnel is closed[#](#tunnel-is-closed "Link to this heading")

An attempt to read from the tunnel was made, but the tunnel in question is
already closed. This can happen if the client or guacd have closed the
connection, but the client has not yet settled down and is still making read
attempts. As there can be lags between when connections close and when the
client realizes it, this can be safely ignored.

#### End of stream during initial handshake[#](#end-of-stream-during-initial-handshake "Link to this heading")

If guacd closes the connection suddenly without allowing the client to complete
the initial handshake required by the Guacamole protocol, this error will
appear in the logs. If you see this error, you should check syslog for any
errors logged by guacd to determine why it closed the connection so early.

#### Element terminator of instruction was not ‘;’ nor ‘,’[#](#element-terminator-of-instruction-was-not-nor "Link to this heading")

The Guacamole protocol imposes a strict format which requires individual parts
of instructions (called “elements”) to end with either a “;” or “,” character.
If they do not, then something has gone wrong during transmission. This usually
indicates a bug in the client plugin in use, guacd, or libguac.

#### Non-numeric character in element length[#](#non-numeric-character-in-element-length "Link to this heading")

The Guacamole protocol imposes a strict format which requires each element of
an instruction to have a length prefix, which must be composed entirely of
numeric characters (digits 0 through 9). If a non-numeric character is read,
then something has gone wrong during transmission. This usually indicates a bug
in the client plugin in use, guacd, or libguac.

Contents

---
# External authentication

# External authentication[#](#external-authentication "Link to this heading")

Important

**Support for [standard single sign-on methods (SSO)](sso.html) is also available.**
If simply looking to integrate Guacamole with an established authentication
system that provides SSO, first check whether Guacamole already supports that
SSO method.

For cases where Guacamole is embedded within an external application that
performs its own authentication, extensions are provided that allow Guacamole
to easily consume the authentication result of that external application:

[HTTP header authentication](header-auth.html)
:   Allows your external application to assert the identity of the Guacamole user
    by adding an HTTP header to authentication requests sent to Guacamole. The
    user’s username is read from the HTTP header.

    The details of any underlying connections must come from anoher extension
    that supports delegation of authentication, like [any of the supported
    databases](jdbc-auth.html).

[Encrypted, signed JSON authentication](json-auth.html)
:   Allows your external application to supply both identity and connection
    information within an encrypted, signed block of JSON. Encryption ensures
    that the JSON can be safely included where it may be visible to users, while
    signing ensures the JSON cannot be manipulated.

    Your application must be modified to sign and encrypt JSON as documented.

Hint

For more complex cases, you may wish to look into [developing your own
Guacamole extension using the extension API (“guacamole-ext”)](guacamole-ext.html).

The extension API is quite flexible. All authentication and authorization
methods supported by Guacamole out-of-the-box are actually provided through
[extensions written using this publicly documented API](https://github.com/apache/guacamole-client/tree/main/extensions).

---
# Encrypted JSON authentication

## Contents

# Encrypted JSON authentication[#](#encrypted-json-authentication "Link to this heading")

Guacamole supports delegating authentication to an arbitrary external service,
relying on receipt of JSON data which has been [signed using HMAC/SHA-256 and
encrypted with 128-bit AES in CBC mode](#generating-encrypted-json). This JSON
contains [all information describing the user being authenticated](#json-format),
as well as any connections they have access to, and is accepted only if the
configured secret key was used to sign and encrypt the data.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling the JSON authentication extension[#](#installing-enabling-the-json-authentication-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-json-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-json-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-json-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `JSON_ENABLED` environment variable:

    ```
    JSON_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e JSON_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `JSON_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `JSON_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Configuration[#](#configuration "Link to this heading")

Native Webapp (Tomcat)

To verify and decrypt the received signed and encrypted JSON, a secret key must
be generated which will be shared by both the Guacamole server and systems that
will generate the JSON data. As guacamole-auth-json uses 128-bit AES, this key
must be 128 bits.

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
json-secret-key: 4c0b569e4c96df157eee1b65dd0e4d41
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`json-secret-key`
:   The 128-bit value to use to decrypt and verify the signatures of received
    JSON data. This value must be expressed as a 32-digit hexadecimal value.

    Any 32-digit hexadecimal value will suffice as long as it is random enough to
    be impractical for a malicious user to guess. An easy way to generate such a
    key is to echo a secure passphrase through the `md5sum` utility. This is the
    technique OpenSSL itself uses to generate 128-bit keys from passphrases. For
    example:

    ```
    $ echo -n "ThisIsATest" | md5sum
    4c0b569e4c96df157eee1b65dd0e4d41
    ```

Container (Docker)

To verify and decrypt the received signed and encrypted JSON, a secret key must
be generated which will be shared by both the Guacamole server and systems that
will generate the JSON data. As guacamole-auth-json uses 128-bit AES, this key
must be 128 bits.

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
JSON_SECRET_KEY: '4c0b569e4c96df157eee1b65dd0e4d41'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e JSON_SECRET_KEY="4c0b569e4c96df157eee1b65dd0e4d41" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`JSON_SECRET_KEY`
:   The 128-bit value to use to decrypt and verify the signatures of received
    JSON data. This value must be expressed as a 32-digit hexadecimal value.

    Any 32-digit hexadecimal value will suffice as long as it is random enough to
    be impractical for a malicious user to guess. An easy way to generate such a
    key is to echo a secure passphrase through the `md5sum` utility. This is the
    technique OpenSSL itself uses to generate 128-bit keys from passphrases. For
    example:

    ```
    $ echo -n "ThisIsATest" | md5sum
    4c0b569e4c96df157eee1b65dd0e4d41
    ```

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## JSON format[#](#json-format "Link to this heading")

The general format of the JSON (prior to being encrypted, signed, and sent to
Guacamole), is as follows:

```
{

    "username" : "arbitraryUsername",
    "expires" : TIMESTAMP,
    "connections" : {

        "Connection Name" : {
            "protocol" : "PROTOCOL",
            "parameters" : {
                "name1" : "value1",
                "name2" : "value2",
                ...
            }
        },

        ...

    }

}
```

where `TIMESTAMP` is a standard UNIX epoch timestamp with millisecond
resolution (the number of milliseconds since midnight of January 1, 1970 UTC)
and `PROTOCOL` is the internal name of any of Guacamole’s supported protocols,
such as `vnc`, `rdp`, or `ssh`.

The JSON will cease to be accepted as valid after the server time passes the
timestamp. If no timestamp is specified, the data will not expire.

The top-level JSON object which must be submitted to Guacamole has the
following properties:

| Property name | Type | Description |
| --- | --- | --- |
| `username` | `string` | The unique username of the user authenticated by the JSON. If the user is anonymous, this should be the empty string (`""`). |
| `expires` | `number` | The absolute time after which the JSON should no longer be accepted, even if the signature is valid, as a standard UNIX epoch timestamp with millisecond resolution (the number of milliseconds since midnight of January 1, 1970 UTC). |
| `connections` | `object` | The set of connections which should be exposed to the user by their corresponding, unique names. If no connections will be exposed to the user, this can simply be an empty object (`{}`). |

Each normal connection defined within each submitted JSON object has the
following properties:

| Property name | Type | Description |
| --- | --- | --- |
| `id` | `string` | An optional opaque value which uniquely identifies this connection across all other connections which may be active at any given time. This property is only required if you wish to allow the connection to be shared or shadowed. |
| `protocol` | `string` | The internal name of a supported protocol, such as `vnc`, `rdp`, or `ssh`. |
| `parameters` | `object` | An object representing the connection parameter name/value pairs to apply to the connection, as documented in [Configuring connections](configuring-guacamole.html#connection-configuration). |

Connections which share or shadow other connections use a `join` property
instead of a `protocol` property, where `join` contains the value of the `id`
property of the connection being joined:

| Property name | Type | Description |
| --- | --- | --- |
| `id` | `string` | An optional opaque value which uniquely identifies this connection across all other connections which may be active at any given time. This property is only required if you wish to allow the connection to be shared or shadowed. (Yes, a connection which shadows another connection may itself be shadowed.) |
| `join` | `string` | The opaque ID given within the `id` property of the connection being joined (shared / shadowed). |
| `parameters` | `object` | An object representing the connection parameter name/value pairs to apply to the connection, as documented in [Configuring connections](configuring-guacamole.html#connection-configuration).  Most of the connection configuration is inherited from the connection being joined. In general, the only property relevant to joining connections is `read-only`. |

If a connection is configured to join another connection, that connection will
only be usable if the connection being joined is currently active. If two
connections are established having the same `id` value, only the last
connection will be joinable using the given `id`.

## Generating encrypted JSON[#](#generating-encrypted-json "Link to this heading")

To authenticate a user with the above JSON format, the JSON must be both signed
and encrypted using the same 128-bit secret key specified within Guacamole’s
configuration:

1. Generate JSON in the format described above
2. Sign the JSON using the secret key (the same 128-bit key stored within
   Guacamole’s configuration) with **HMAC/SHA-256**. Prepend the binary result
   of the signing process to the plaintext JSON that was signed.
3. Encrypt the result of (2) above using **AES in CBC mode**, with the initial
   vector (IV) set to all zero bytes.
4. Encode the encrypted result using base64.
5. POST the encrypted result to the `/api/tokens` REST endpoint as the value of
   an HTTP parameter named `data` (or include it in the URL of any Guacamole
   page as a query parameter named `data`).

   For example, if Guacamole is running on localhost at `/guacamole`, and
   `BASE64_RESULT` is the result of the above process, the equivalent run of
   the “curl” utility would be:

   ```
   $ curl --data-urlencode "data=BASE64_RESULT" http://localhost:8080/guacamole/api/tokens
   ```

   **NOTE:** Be sure to URL-encode the base64-encoded result prior to POSTing
   it to `/api/tokens` or including it in the URL. Base64 can contain both “+”
   and “=” characters, which have special meaning within URLs.

If the data is invalid in any way, if the signature does not match, if
decryption or signature verification fails, or if the submitted data has
expired, the REST service will return an invalid credentials error and fail
without user-visible explanation. Details describing the error that occurred
will be in the Tomcat logs, however.

## Reference implementation[#](#reference-implementation "Link to this heading")

The source includes a shell script, [`doc/encrypt-json.sh`](https://raw.githubusercontent.com/apache/guacamole-client/master/extensions/guacamole-auth-json/doc/encrypt-json.sh),
which uses the OpenSSL command-line utility to encrypt and sign JSON in the
manner that guacamole-auth-json requires. It is thoroughly commented and should
work well as a reference implementation, for testing, and as a point of
comparison for development. The script is run as:

```
$ ./encrypt-json.sh HEX_ENCRYPTION_KEY file-to-sign-and-encrypt.json
```

For example, if you have a file called `auth.json` containing the following:

```
{
    "username" : "test",
    "expires" : "1446323765000",
    "connections" : {
        "My Connection" : {
            "protocol" : "rdp",
            "parameters" : {
                "hostname" : "10.10.209.63",
                "port" : "3389",
                "ignore-cert": "true",
                "recording-path": "/recordings",
                "recording-name": "My-Connection-${GUAC_USERNAME}-${GUAC_DATE}-${GUAC_TIME}"
            }
        },
        "My OTHER Connection" : {
            "protocol" : "rdp",
            "parameters" : {
                "hostname" : "10.10.209.64",
                "port" : "3389",
                "ignore-cert": "true",
                "recording-path": "/recordings",
                "recording-name": "My-OTHER-Connection-${GUAC_USERNAME}-${GUAC_DATE}-${GUAC_TIME}"
            }
        }
    }
}
```

and you run:

```
$ ./encrypt-json.sh 4C0B569E4C96DF157EEE1B65DD0E4D41 auth.json
```

You will receive the following output:

```
A2Pf5Kpmm97I2DT1PifIrfU6q3yzoGcIbNXEd60WNangT8DAVjAl6luaqwhBJnCK
uqcf9ZZlRo3uDxTHvUM3eq1YvdghL0GbosOn8Mn38j2ydOMk+Cd15a8ggb4/ddt/
yIBK4DxrN7MNbouZ091KYtXC6m20E6sGzLy676BlMSg1cmsENRIihOynsSLSCvo0
diif6H7T+ZuIqF7B5SW+adGfMaHlfknlIvSpLGHhrIP4aMYE/ZU2vYNg8ez27sCS
wDBWu5lERtfCYFyU4ysjRU5Hyov+yKa+O7jcRYpw3N+fHbCg7/dxVNW07qNOKssv
pzUciGvDPUCPpa02WmPJNEBowwQireO1952/MNAI77cW2UepbljD/bwOiZl2THJz
LrENo7K5acimBa+EjWEesgn7lx/WTCF3zxR6TH1CWrQM8Et1aUK1Nf8K11xEQbTy
klyaNtCmTfyahRZ/fUPxDNrdJVpPOSELkf7RJO5tOdK/FFIFIbze3ZUyXgRq+pHY
owpgOmudDBTBlxhXiONdutRI/RZbFM/7GBMdmI8AR/401OCV3nsI4jLhukjMXH3V
f3pQg+xKMhi/QExHhDk8VTNYk7GurK4vgehn7HQ0oSGh8pGcmxB6W43cz+hyn6VQ
On6i90cSnIhRO8SysZt332LwJCDm7I+lBLaI8NVHU6bnAY1Axx5oH3YTKc4qzHls
HEAFYLkD6aHMvHkF3b798CMravjxiJV3m7hsXDbaFN6AFhn8GIkMRRrjuevfZ+q9
enWN14s24vt5OVg69DljzALobUNKUXFx69SR8EpSBvUcKq8s/OgbDpFvKbwsDY57
HGT4T0CuRIA0TGUI075uerKBNApVhuBA1BmWJIrI4JXw5MuX6pdBe+MYccO3vfo+
/frazj8rHdkDa/IbueMbvq+1ozV2+UuxrbaTrV2i4jSRgd74U0QzOh9e8Q0i7vOi
l3hnIfOfg+v1oULmZmJSeiAYWxeGvPptp+n7rNFqHGM=
```

The resulting base64 data above, if submitted using the `data` parameter to
Guacamole, will authenticate a user and grant them access to the connections
described in the JSON (at least until the expires timestamp is reached, at
which point the JSON will no longer be accepted).

Contents

---
# Writing your own Guacamole application

## Contents

# Writing your own Guacamole application[#](#writing-your-own-guacamole-application "Link to this heading")

As Guacamole is an API, one of the best ways to put Guacamole to use is by
building your own Guacamole-driven web application, integrating HTML5 remote
desktop into whatever you think needs it.

The Guacamole project provides an example of doing this called
“guacamole-example”, but this example is already completed for you, and from a
quick glance at this example, it may not be obvious just how easy it is to
integrate remote access into a web application. This tutorial will walk you
through the basic steps of building an HTML5 remote desktop application using
the Guacamole API and Maven.

## The basics[#](#the-basics "Link to this heading")

Guacamole’s architecture is made up of many components, but it’s actually
straightforward, especially from the perspective of the web application.

Guacamole has a proxy daemon, guacd, which handles communication using remote
desktop protocols, exposing those to whatever connects to it (in this case, the
web application) using the Guacamole protocol. From where the web application
is standing, it doesn’t really matter that guacd dynamically loads protocol
plugins or that it shares a common library allowing this; all that matters is
that the web application just has to connect to port 4822 (where guacd listens
by default) and use the Guacamole protocol. The architecture will take care of
the rest.

Thankfully, the Java side of the Guacamole API provides simple classes which
already implement the Guacamole protocol with the intent of tunneling it
between guacd and the JavaScript half of your web application. A typical web
application leveraging these classes needs
only the following:

1. A class which extends `GuacamoleHTTPTunnelServlet`, providing the tunnel
   between the JavaScript client (presumably using guacamole-common-js) and
   guacd.

   `GuacamoleHTTPTunnelServlet` is an abstract class which is provided by the
   Guacamole API and already implements a fully functional, HTTP-based tunnel
   which the tunneling objects already part of guacamole-common-js are written
   to connect to. This class exists to make it easy for you to use Guacamole’s
   existing and robust HTTP tunnel implementation.

   If you want to not use this class and instead use your own tunneling
   mechanism, perhaps WebSocket, this is fine; the JavaScript object mentioned
   above implements a common interface which you can also implement, and the
   Guacamole JavaScript client which is also part of guacamole-common-js will
   happily use your implementation as long as it provides that interface.
2. A web page which includes JavaScript files from guacamole-common-js and uses
   the client and tunnel objects to connect back to the web application.

   The JavaScript API provided by the Guacamole project includes a full
   implementation of the Guacamole protocol as a client, implementations of
   HTTP and WebSocket-based tunnels, and mouse/keyboard/touch input
   abstraction. Again, as the Guacamole protocol and all parts of the
   architecture are documented here, you don’t absolutely need to use these
   objects, but it will make your life easier. Mouse and keyboard support in
   JavaScript is finicky business, and the Guacamole client provided is
   well-known to work with other components in the API, being the official
   client of the project.

That’s really all there is to it.

If you want authentication, the place to implement that would be in your
extended version of `GuacamoleHTTPTunnelServlet`; this is what the Guacamole
web application does. Besides authentication, there are many other things you
could wrap around your remote desktop application, but ultimately the base of
all this is simple: you have a tunnel which allows the JavaScript client to
communicate with guacd, and you have the JavaScript client itself, with the
hard part already provided within guacamole-common-js.

## Web application skeleton[#](#web-application-skeleton "Link to this heading")

As with most tutorials, this tutorial begins with creating a project skeleton
that establishes a minimal base for the tutorial to enhance in subsequent
steps.

This tutorial will use Maven, which is the same build system used by the
upstream Guacamole project. As the Guacamole project has a Maven repository for
both the Java and JavaScript APIs, writing a Guacamole-based application using
Maven is much easier; Maven will download and use the Guacamole API
automatically.

### `pom.xml`[#](#pom-xml "Link to this heading")

All Maven projects must have a project descriptor, the `pom.xml` file, in the
root directory of the project. This file describes project dependencies and
specific build requirements. Unlike other build tools like Apache Ant or GNU
Autotools, Maven chooses convention over configuration: files within the
project must be placed in specific locations, and the project dependencies must
be fully described in the pom.xml. If this is done, the build will be handled
automatically.

The basis of this Guacamole-driven web application will be a simple HTML file
which will ultimately become the client. While the finished product will have
an HTTP tunnel written in Java, we don’t need this yet for our skeleton. We
will create a very basic, barebones Maven project containing only `index.html`
and a web application descriptor file, `web.xml`. Once these files are in
place, the project can be packaged into a `.war` file which can be deployed to
your servlet container of choice (such as Apache Tomcat).

As this skeleton will contain no Java code, it has no dependencies, and
no build requirements beyond the metadata common to any Maven project.
The `pom.xml` is thus very simple for the time being:
i

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
                             http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>org.apache.guacamole</groupId>
    <artifactId>guacamole-tutorial</artifactId>
    <packaging>war</packaging>
    <version>1.6.0</version>
    <name>guacamole-tutorial</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

</project>
```

### `WEB-INF/web.xml`[#](#web-inf-web-xml "Link to this heading")

Before the project will build, there needs to be a web application deployment
descriptor, `web.xml`. This file is required by the Java EE standard for
building the `.war` file which will contain the web application, and will be
read by the servlet container when the application is actually deployed. For
Maven to find and use this file when building the `.war`, it must be placed in
the `src/main/webapp/WEB-INF/` directory.

```
<?xml version="1.0" encoding="UTF-8"?>

<web-app version="2.5"
    xmlns="http://java.sun.com/xml/ns/javaee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
                        http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">

    <!-- Basic config -->
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
    </welcome-file-list>

</web-app>
```

### `index.html`[#](#index-html "Link to this heading")

With the `web.xml` file in place and the skeleton `pom.xml` written, the web
application will now build successfully. However, as the `web.xml` refers to a
“welcome file” called `index.html` (which will ultimately contain our client),
we need to put this in place so the servlet container will have something to
serve. This file, as well as any other future static files, belongs within
`src/main/webapp`.

For now, this file can contain anything, since the other parts of our
Guacamole-driven web application are not written yet. It is a placeholder which
we will replace later:

```
<!DOCTYPE HTML>
<html>

    <head>
        <title>Guacamole Tutorial</title>
    </head>

    <body>
        <p>Hello World</p>
    </body>

</html>
```

### Building the skeleton[#](#building-the-skeleton "Link to this heading")

Once all three of the above files are in place, the web application will build,
and can even be deployed to your servlet container. It won’t do anything yet
other than serve the `index.html` file, but it’s good to at least try building
the web application to make sure nothing is missing and all steps were followed
correctly before proceeding:

```
$ mvn package
[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Building guacamole-tutorial
[INFO]    task-segment: [package]
[INFO] ------------------------------------------------------------------------
...
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 4 seconds
[INFO] Finished at: Fri Jan 11 13:04:11 PST 2013
[INFO] Final Memory: 18M/128M
[INFO] ------------------------------------------------------------------------
$
```

Assuming you see the “`BUILD SUCCESSFUL`” message when you build the web
application, there will be a new file, `target/guacamole-tutorial-1.6.0.war`,
which can be deployed to your servlet container and tested. If you changed the
name or version of the project in the `pom.xml` file, the name of this new
`.war` file will be different, but it can still be found within `target/`.

## Adding Guacamole[#](#adding-guacamole "Link to this heading")

Once we have a functional web application built, the next step is to actually
add the references to the Guacamole API and integrate a Guacamole client into
the application.

### Updating `pom.xml`[#](#updating-pom-xml "Link to this heading")

Now that we’re adding Guacamole components to our project, we need to modify
`pom.xml` to specify which components are being used, and where they can be
obtained. With this information in place, Maven will automatically resolve
dependencies and download them as necessary during the build.

Regarding the build process itself, there are two main changes: we are now
going to be using Java, and we need the JavaScript files from
guacamole-common-js included automatically inside the `.war`.

Guacamole requires at least Java 8, thus we must add a section to the
`pom.xml` which describes the source and target Java versions:

```
    ...

    <build>
        <plugins>

            <!-- Compile using Java 8 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.3</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>

        </plugins>

    </build>

    ...
```

Including the JavaScript files from an external project like
guacamole-common-js requires using a feature of the maven war plugin called
overlays. To add an overlay containing guacamole-common-js, we add a section
describing the configuration of the Maven war plugin, listing
guacamole-common-js as an overlay:

```
    ...

    <build>
        <plugins>

            ...

            <!-- Overlay guacamole-common-js (zip) -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>2.6</version>
                <configuration>
                    <overlays>
                        <overlay>
                            <groupId>org.apache.guacamole</groupId>
                            <artifactId>guacamole-common-js</artifactId>
                            <type>zip</type>
                        </overlay>
                    </overlays>
                </configuration>
            </plugin>

        </plugins>

    </build>

    ...
```

With the build now configured, we still need to add dependencies and list the
repositories those dependencies can be downloaded from.

As this is a web application which will use the Java Servlet API, we must
explicitly include this as a dependency, as well as the Guacamole Java and
JavaScript APIs:

```
    ...

    <dependencies>

        <!-- Servlet API -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>servlet-api</artifactId>
            <version>2.5</version>
            <scope>provided</scope>
        </dependency>

        <!-- Main Guacamole library -->
        <dependency>
            <groupId>org.apache.guacamole</groupId>
            <artifactId>guacamole-common</artifactId>
            <version>1.6.0</version>
            <scope>compile</scope>
        </dependency>

        <!-- Guacamole JavaScript library -->
        <dependency>
            <groupId>org.apache.guacamole</groupId>
            <artifactId>guacamole-common-js</artifactId>
            <version>1.6.0</version>
            <type>zip</type>
            <scope>runtime</scope>
        </dependency>

    </dependencies>

    ...
```

The Java Servlet API will be provided by your servlet container, so Maven does
not need to download it during the build, and it need not exist in any Maven
repository.

With these changes, the web application will still build at this point, even
though no Java code has been written yet. You may wish to verify that
everything still works.

If the `pom.xml` was updated properly as described above, the web application
should build successfully, and the Guacamole JavaScript API should be
accessible in the `guacamole-common-js/` subdirectory of your web application
after it is deployed. A quick check that you can access
`/guacamole-tutorial-1.6.0/guacamole-common-js/all.min.js` is probably worth
the effort.

### The simplest tunnel possible[#](#the-simplest-tunnel-possible "Link to this heading")

As with the other tutorials in this book, we will keep this simple for the sake
of demonstrating the principles behind a Guacamole-based web application, and
to give developers a good idea of where to start looking when it’s time to
consult the API documentation.

It is the duty of the class extending `GuacamoleHTTPTunnelServlet` to implement
a function called `doConnect()`. This is the only function required to be
implemented, and in general it is the only function you should implement; the
other functions involved are already optimized for tunneling the Guacamole
protocol.

The `doConnect()` function returns a `GuacamoleTunnel`, which provides a
persistent communication channel for `GuacamoleHTTPTunnelServlet` to use when
talking with guacd and initiating a connection with some arbitrary remote
desktop using some arbitrary remote desktop protocol. In our simple tunnel,
this configuration will be hard-coded, and no authentication will be attempted.
Any user accessing this web application will be immediately given a functional
remote desktop, no questions asked.

Create a new file, `TutorialGuacamoleTunnelServlet.java`, defining a basic
implementation of a tunnel servlet class:

```
package org.apache.guacamole.net.example;

import javax.servlet.http.HttpServletRequest;
import org.apache.guacamole.GuacamoleException;
import org.apache.guacamole.net.GuacamoleSocket;
import org.apache.guacamole.net.GuacamoleTunnel;
import org.apache.guacamole.net.InetGuacamoleSocket;
import org.apache.guacamole.net.SimpleGuacamoleTunnel;
import org.apache.guacamole.protocol.ConfiguredGuacamoleSocket;
import org.apache.guacamole.protocol.GuacamoleConfiguration;
import org.apache.guacamole.servlet.GuacamoleHTTPTunnelServlet;

public class TutorialGuacamoleTunnelServlet
    extends GuacamoleHTTPTunnelServlet {

    @Override
    protected GuacamoleTunnel doConnect(HttpServletRequest request)
        throws GuacamoleException {

        // Create our configuration
        GuacamoleConfiguration config = new GuacamoleConfiguration();
        config.setProtocol("vnc");
        config.setParameter("hostname", "localhost");
        config.setParameter("port", "5901");
        config.setParameter("password", "potato");

        // Connect to guacd - everything is hard-coded here.
        GuacamoleSocket socket = new ConfiguredGuacamoleSocket(
                new InetGuacamoleSocket("localhost", 4822),
                config
        );

        // Return a new tunnel which uses the connected socket
        return new SimpleGuacamoleTunnel(socket);;

    }

}
```

Place this file in the `src/main/java/org/apache/guacamole/net/example`
subdirectory of the project. The initial part of this subdirectory,
`src/main/java`, is the path required by Maven, while the rest is the directory
required by Java based on the package associated with the class.

Once the class defining our tunnel is created, it must be added to the
`web.xml` such that the servlet container knows which URL maps to it. This URL
will later be given to the JavaScript client to establish the connection back
to the Guacamole server:

```
    ...

    <!-- Guacamole Tunnel Servlet -->
    <servlet>
        <description>Tunnel servlet.</description>
        <servlet-name>Tunnel</servlet-name>
        <servlet-class>
            org.apache.guacamole.net.example.TutorialGuacamoleTunnelServlet
        </servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>Tunnel</servlet-name>
        <url-pattern>/tunnel</url-pattern>
    </servlet-mapping>

    ...
```

The first section assigns a unique name, “Tunnel”, to the servlet class we just
defined. The second section maps the servlet class by it’s servlet name
(“Tunnel”) to the URL we wish to use when making HTTP requests to the servlet:
`/tunnel`. This URL is relative to the context root of the web application. In
the case of this web application, the final absolute URL will be
`/guacamole-tutorial-1.6.0/tunnel`.

### Adding the client[#](#adding-the-client "Link to this heading")

As the Guacamole JavaScript API already provides functional client and tunnel
implementations, as well as mouse and keyboard input objects, the coding
required for the “web” side of the web application is very minimal.

We must create a `Guacamole.HTTPTunnel`, connect it to our
previously-implemented tunnel servlet, and pass that tunnel to a new
`Guacamole.Client`. Once that is done, and the `connect()` function of the
client is called, communication will immediately ensue, and your remote desktop
will be visible:

```
    ...
    <body>

        <!-- Guacamole -->
        <script type="text/javascript"
            src="guacamole-common-js/all.min.js"></script>

        <!-- Display -->
        <div id="display"></div>

        <!-- Init -->
        <script type="text/javascript"> /* <![CDATA[ */

            // Get display div from document
            var display = document.getElementById("display");

            // Instantiate client, using an HTTP tunnel for communications.
            var guac = new Guacamole.Client(
                new Guacamole.HTTPTunnel("tunnel")
            );

            // Add client to display div
            display.appendChild(guac.getDisplay().getElement());
            
            // Error handler
            guac.onerror = function(error) {
                alert(error);
            };

            // Connect
            guac.connect();

            // Disconnect on close
            window.onunload = function() {
                guac.disconnect();
            }

        /* ]]> */ </script>

    </body>
    ...
```

If you build and deploy the web application now, it will work, but mouse and
keyboard input will not. This is because input is not implemented by the client
directly. The `Guacamole.Client` object only decodes the Guacamole protocol and
handles the display, providing an element which you can add manually to the
DOM. While it will also send keyboard and mouse events for you, you need to
call the respective functions manually. The Guacamole API provides keyboard and
mouse abstraction objects which make this easy.

We need only create a `Guacamole.Mouse` and `Guacamole.Keyboard`, and add event
handlers to handle their corresponding input events, calling whichever function
of the Guacamole client is appropriate to send the input event through the
tunnel to guacd:

```
        ...

        <!-- Init -->
        <script type="text/javascript"> /* <![CDATA[ */

            ...

            // Mouse
            var mouse = new Guacamole.Mouse(guac.getDisplay().getElement());

            mouse.onmousedown = 
            mouse.onmouseup   =
            mouse.onmousemove = function(mouseState) {
                guac.sendMouseState(mouseState);
            };

            // Keyboard
            var keyboard = new Guacamole.Keyboard(document);

            keyboard.onkeydown = function (keysym) {
                guac.sendKeyEvent(1, keysym);
            };

            keyboard.onkeyup = function (keysym) {
                guac.sendKeyEvent(0, keysym);
            };

        /* ]]> */ </script>

        ...
```

## Where to go from here[#](#where-to-go-from-here "Link to this heading")

At this point, we now have a fully functional Guacamole-based web application.
This web application inherits all the core functionality present in the
official Guacamole web application, including sound and video, without very
much coding.

Extending this application to provide authentication, multiple connections per
user, or a spiffy interface which is compatible with mobile is not too much of
a stretch. This is exactly how the Guacamole web application is written.
Integrating Guacamole into an existing application would be similar.

Contents

---
# Importing connections from CSV, JSON, or YAML

## Contents

# Importing connections from CSV, JSON, or YAML[#](#importing-connections-from-csv-json-or-yaml "Link to this heading")

Administrators may batch import connections and connection groups from a file,
if the underlying authentication module supports dynamic connection/group creation.
To start a batch import, click the “Import” button on the connection edit tab.

![Link to Batch Import](assets/doc_gug__images_batch-import-admin-link.png)

At this point, the interface will accept a CSV, JSON, or YAML file containing
a list of connections to be imported.

![Batch Import Start](assets/doc_gug__images_batch-import-start.png)

## Success[#](#success "Link to this heading")

On success, the batch import UI will simply display a message indicating
how many connections were imported.

![Batch Import Success](assets/doc_gug__images_batch-import-success.png)

## Failure[#](#failure "Link to this heading")

If import fails, the importer will display a list of the connections, along with
any relevant connection-specific errors, unless a file format error prevents
parsing the file into a list of connections at all.

![Batch Import Failure](assets/doc_gug__images_batch-import-failure.png)

## Import file format[#](#import-file-format "Link to this heading")

Three file types are supported for connection import: CSV, JSON, and YAML.
The same data may be specified by each file type. This must include the
connection name and protocol. Optionally, a connection group location, a list
of users and/or user groups to grant access, connection parameters, or connection
protocols may also be specified. Any users or user groups that do not exist in
the current data source will be automatically created. Note that any existing
connection permissions will not be removed for updated connections, unless
“Reset permissions” is checked.

This same file format information is available within the webapp, at the
“View Format Tips” link.

### CSV Format[#](#csv-format "Link to this heading")

A connection import CSV file has one connection record per row. Each column will
specify a connection field. At minimum the connection name and protocol must be
specified.

The CSV header for each row specifies the connection field. The connection group
ID that the connection should be imported into may be directly specified with
“parentIdentifier”, or the path to the parent group may be specified using “group”
as shown below. In most cases, there should be no conflict between fields, but if
needed, an “ (attribute)” or “ (parameter)” suffix may be added to disambiguate.
Lists of user or user group identifiers must be semicolon-separated. If present,
semicolons can be escaped with a backslash, e.g. “first;last”.

```
name,protocol,username,password,hostname,group,users,groups,guacd-encryption (attribute)
conn1,vnc,alice,pass1,conn1.web.com,ROOT,guac user 1;guac user 2,Connection 1 Users,none
conn2,rdp,bob,pass2,conn2.web.com,ROOT/Parent Group,guac user 1,,ssl
conn3,ssh,carol,pass3,conn3.web.com,ROOT/Parent Group/Child Group,guac user 2;guac user 3,,
conn4,kubernetes,,,,,,,
```

### JSON Format[#](#json-format "Link to this heading")

A connection import JSON file is a list of connection objects. At minimum the connection
name and protocol must be specified in each connection object.

The connection group ID that the connection should be imported into may be directly
specified with a “parentIdentifier” field, or the path to the parent group may be
specified using a “group” field as shown below. An array of user and user group
identifiers to grant access to may be specified per connection.

```
[
  {
    "name": "conn1",
    "protocol": "vnc",
    "parameters": { "username": "alice", "password": "pass1", "hostname": "conn1.web.com" },
    "parentIdentifier": "ROOT",
    "users": [ "guac user 1", "guac user 2" ],
    "groups": [ "Connection 1 Users" ],
    "attributes": { "guacd-encryption": "none" }
  },
  {
    "name": "conn2",
    "protocol": "rdp",
    "parameters": { "username": "bob", "password": "pass2", "hostname": "conn2.web.com" },
    "group": "ROOT/Parent Group",
    "users": [ "guac user 1" ],
    "attributes": { "guacd-encryption": "none" }
  },
  {
    "name": "conn3",
    "protocol": "ssh",
    "parameters": { "username": "carol", "password": "pass3", "hostname": "conn3.web.com" },
    "group": "ROOT/Parent Group/Child Group",
    "users": [ "guac user 2", "guac user 3" ]
  },
  {
    "name": "conn4",
    "protocol": "kubernetes"
  }
]
```

### YAML Format[#](#yaml-format "Link to this heading")

A connection import YAML file is a list of connection objects with exactly
the same structure as the JSON format.

```
---
  - name: conn1
    protocol: vnc
    parameters:
      username: alice
      password: pass1
      hostname: conn1.web.com
    group: ROOT
    users:
      - guac user 1
      - guac user 2
    groups:
    - Connection 1 Users
    attributes:
      guacd-encryption: none
  - name: conn2
    protocol: rdp
    parameters:
      username: bob
      password: pass2
      hostname: conn2.web.com
    group: ROOT/Parent Group
    users:
      - guac user 1
    attributes:
      guacd-encryption: none
  - name: conn3
    protocol: ssh
    parameters:
      username: carol
      password: pass3
      hostname: conn3.web.com
    group: ROOT/Parent Group/Child Group
    users:
      - guac user 2
      - guac user 3
  - name: conn4
    protocol: kubernetes
```

Contents

---
# Using CAS for single sign-on

## Contents

# Using CAS for single sign-on[#](#using-cas-for-single-sign-on "Link to this heading")

CAS is an open-source Single Sign On (SSO) provider that allows multiple
applications and services to authenticate against it and brokers those
authentication requests to a back-end authentication provider. This module
allows Guacamole to redirect to CAS for authentication and user services. This
module must be layered on top of other authentication extensions that provide
connection information, as it only provides user authentication.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling the CAS authentication extension[#](#installing-enabling-the-cas-authentication-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-sso-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-sso-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `cas/guacamole-auth-sso-cas-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `CAS_ENABLED` environment variable:

    ```
    CAS_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e CAS_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `CAS_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `CAS_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Required configuration[#](#required-configuration "Link to this heading")

Native Webapp (Tomcat)

Guacamole’s CAS support requires specifying two properties that
describe the CAS authentication server and the Guacamole deployment.
These properties are *absolutely required in all cases*, as they
dictate how Guacamole should connect to CAS and how CAS should redirect users
back to Guacamole once their identity has been confirmed.

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
cas-authorization-endpoint: https://cas.example.net
cas-redirect-uri: https://guac.example.net
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`cas-authorization-endpoint`
:   The URL of the CAS authentication server. This should be the full path to the
    base of the CAS installation.

`cas-redirect-uri`
:   The URI to redirect back to upon successful authentication. Normally this
    will be the full URL of your Guacamole installation.

Container (Docker)

Guacamole’s CAS support requires specifying two environment variables that
describe the CAS authentication server and the Guacamole deployment.
These environment variables are *absolutely required in all cases*, as they
dictate how Guacamole should connect to CAS and how CAS should redirect users
back to Guacamole once their identity has been confirmed.

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
CAS_AUTHORIZATION_ENDPOINT: 'https://cas.example.net'
CAS_REDIRECT_URI: 'https://guac.example.net'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e CAS_AUTHORIZATION_ENDPOINT="https://cas.example.net" \
    -e CAS_REDIRECT_URI="https://guac.example.net" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`CAS_AUTHORIZATION_ENDPOINT`
:   The URL of the CAS authentication server. This should be the full path to the
    base of the CAS installation.

`CAS_REDIRECT_URI`
:   The URI to redirect back to upon successful authentication. Normally this
    will be the full URL of your Guacamole installation.

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Native Webapp (Tomcat)

Additional optional properties are available to control how
CAS-related data is processed, including whether [CAS ClearPass](#cas-clearpass)
should be used and how user group memberships should be derived:

`cas-clearpass-key`
:   If using CAS ClearPass to pass the SSO password to Guacamole, this parameter
    specifies the private key file to use to decrypt the password. See [the section
    on ClearPass](#cas-clearpass) below.

`cas-group-attribute`
:   The CAS attribute that determines group membership, typically “memberOf”.
    This parameter is only required if using CAS to define user group memberships.
    If omitted, groups aren’t retrieved from CAS, and all other group-related
    properties for CAS are ignored.

`cas-group-format`
:   The format that CAS will use for its group names. Possible values are
    `plain`, for groups that are simple text names, or `ldap`, for groups that are
    represented as LDAP DNs. If set to `ldap`, group names are always determined
    from the last (leftmost) attribute of the DN. If omitted, `plain` is used by
    default.

    This property has no effect if cas-group-attribute is not set.

`cas-group-ldap-base-dn`
:   The base DN to require for LDAP-formatted CAS groups. If specified, only CAS
    groups beneath this DN will be included, and all other CAS groups will be
    ignored.

    This property has no effect if cas-group-format is not `ldap`.

`cas-group-ldap-attribute`
:   The LDAP attribute to require for LDAP-formatted CAS groups. If specified,
    only CAS groups that use this attribute for the name of the group will be
    included. Note that LDAP group names are *always determined from the last
    (leftmost) attribute of the DN*. Specifying this property will only have the
    effect of ignoring any groups that do not use the specified attribute to
    represent the group name.

    This property has no effect if cas-group-format is not `ldap`.

Container (Docker)

Additional optional environment variables are available to control how
CAS-related data is processed, including whether [CAS ClearPass](#cas-clearpass)
should be used and how user group memberships should be derived:

`CAS_CLEARPASS_KEY`
:   If using CAS ClearPass to pass the SSO password to Guacamole, this parameter
    specifies the private key file to use to decrypt the password. See [the section
    on ClearPass](#cas-clearpass) below.

`CAS_GROUP_ATTRIBUTE`
:   The CAS attribute that determines group membership, typically “memberOf”.
    This parameter is only required if using CAS to define user group memberships.
    If omitted, groups aren’t retrieved from CAS, and all other group-related
    properties for CAS are ignored.

`CAS_GROUP_FORMAT`
:   The format that CAS will use for its group names. Possible values are
    `plain`, for groups that are simple text names, or `ldap`, for groups that are
    represented as LDAP DNs. If set to `ldap`, group names are always determined
    from the last (leftmost) attribute of the DN. If omitted, `plain` is used by
    default.

    This property has no effect if cas-group-attribute is not set.

`CAS_GROUP_LDAP_BASE_DN`
:   The base DN to require for LDAP-formatted CAS groups. If specified, only CAS
    groups beneath this DN will be included, and all other CAS groups will be
    ignored.

    This property has no effect if cas-group-format is not `ldap`.

`CAS_GROUP_LDAP_ATTRIBUTE`
:   The LDAP attribute to require for LDAP-formatted CAS groups. If specified,
    only CAS groups that use this attribute for the name of the group will be
    included. Note that LDAP group names are *always determined from the last
    (leftmost) attribute of the DN*. Specifying this property will only have the
    effect of ignoring any groups that do not use the specified attribute to
    represent the group name.

    This property has no effect if cas-group-format is not `ldap`.

### Controlling login behavior[#](#controlling-login-behavior "Link to this heading")

Guacamole loads authentication extensions in order of priority, and evaluates
authentication attempts in this same order. This has implications for how the
Guacamole login process behaves when an SSO extension is present:

If the SSO extension has priority:
:   Users that are not yet authenticated
    will be immediately redirected to the configured identity provider. They will
    not see a Guacamole login screen.

If a non-SSO extension has priority:
:   Users that are not yet authenticated
    will be presented with a Guacamole login screen. Additionally, links to the
    configured identity provider(s) will be available for users that wish to log
    in using SSO.

The default priority of extensions is dictated by their filenames, with
extensions that sort earlier alphabetically having higher priority than others.
This can be overridden by [explicitly setting the extension
priority](configuring-guacamole.html#initial-setup).

#### Automatically redirecting all unauthenticated users[#](#automatically-redirecting-all-unauthenticated-users "Link to this heading")

To ensure users are redirected to the CAS identity provider immediately
(without a Guacamole login screen), ensure the CAS extension has priority over
all others:

```
extension-priority: cas
```

#### Presenting unauthenticated users with a login screen[#](#presenting-unauthenticated-users-with-a-login-screen "Link to this heading")

To ensure users are given a normal Guacamole login screen and have the option
to log in with traditional credentials *or* with CAS, ensure the CAS extension
does not have priority:

```
extension-priority: *, cas
```

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Using CAS ClearPass[#](#using-cas-clearpass "Link to this heading")

CAS has a function called ClearPass that can be used to cache the password used
for SSO authentication and make that available to services at a later time.
Configuring the CAS server for ClearPass is beyond the scope of this article -
more information can be found on the Apereo CAS wiki at the following URL:
<https://apereo.github.io/cas>.

Once you have CAS configured for credential caching, you need to configure the
service with a keypair for passing the credential securely. The public key gets
installed on the CAS server, while the private key gets configured with the
`cas-clearpass-key property`. The private key file needs to be in RSA PKCS8
format.

Contents

---
# Custom authentication

## Contents

# Custom authentication[#](#custom-authentication "Link to this heading")

Guacamole’s authentication layer is designed to be extendable such that users
can integrate Guacamole into existing authentication systems without having to
resort to writing their own web application around the Guacamole API.

The web application comes with a default authentication mechanism which uses an
XML file to associate users with connections. Extensions for Guacamole that
provide LDAP-based authentication or database-based authentication have also
been developed.

To demonstrate the principles involved, we will implement a very simple
authentication extension which associates a single user/password pair with a
single connection, with all this information saved in properties inside the
`guacamole.properties` file.

In general, all other authentication extensions for Guacamole will use the
principles demonstrated here. This tutorial demonstrates the simplest way to
create an authentication extension for Guacamole - an authentication extension
that does not support management of users and connections via the web
interface.

## Guacamole’s authentication model[#](#guacamoles-authentication-model "Link to this heading")

When you view any page in Guacamole, whether that be the login screen or the
client interface, the page makes an authentication attempt with the web
application, sending all available credentials. After entering your username
and password, the exact same process occurs, except the web application
receives the username and password as well.

The web application handles this authentication attempt by collecting all
credentials available and passing them to designated classes called
“authentication providers”. Given the set of credentials, authentication
providers return a context object that provides restricted access to other
users and connections, if any.

## A Guacamole extension skeleton[#](#a-guacamole-extension-skeleton "Link to this heading")

For simplicity’s sake, and because this is how things are done upstream in the
Guacamole project, we will use Maven to build our extension.

The bare minimum required for a Guacamole authentication extension is a
`pom.xml` file listing guacamole-ext as a dependency, a single .java file
implementing our stub of an authentication provider, and a `guac-manifest.json`
file describing the extension and pointing to our authentication provider
class.

In our stub, we won’t actually do any authentication yet; we’ll just
universally reject all authentication attempts by returning `null` for any
credentials given. You can verify that this is what happens by checking the
server logs.

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                        http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>org.apache.guacamole</groupId>
    <artifactId>guacamole-auth-tutorial</artifactId>
    <packaging>jar</packaging>
    <version>1.6.0</version>
    <name>guacamole-auth-tutorial</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>

            <!-- Written for Java 8 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.3</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>

        </plugins>
    </build>

    <dependencies>

        <!-- Guacamole Extension API -->
        <dependency>
            <groupId>org.apache.guacamole</groupId>
            <artifactId>guacamole-ext</artifactId>
            <version>1.6.0</version>
            <scope>provided</scope>
        </dependency>

    </dependencies>

</project>
```

We won’t need to update this `pom.xml` throughout the rest of the tutorial.
Even after adding new files, Maven will just find them and compile as
necessary.

Naturally, we need the actual authentication extension skeleton code. While
you can put this in whatever file and package you want, for the sake of this
tutorial, we will assume you are using
`org.apache.guacamole.auth.TutorialAuthenticationProvider`.

```
package org.apache.guacamole.auth;

import java.util.Map;
import org.apache.guacamole.GuacamoleException;
import org.apache.guacamole.net.auth.simple.SimpleAuthenticationProvider;
import org.apache.guacamole.net.auth.Credentials;
import org.apache.guacamole.protocol.GuacamoleConfiguration;

/**
 * Authentication provider implementation intended to demonstrate basic use
 * of Guacamole's extension API. The credentials and connection information for
 * a single user are stored directly in guacamole.properties.
 */
public class TutorialAuthenticationProvider extends SimpleAuthenticationProvider {

    @Override
    public String getIdentifier() {
        return "tutorial";
    }

    @Override
    public Map<String, GuacamoleConfiguration>
        getAuthorizedConfigurations(Credentials credentials)
        throws GuacamoleException {

        // Do nothing ... yet
        return null;        

    }

}
```

To conform with Maven, this skeleton file must be placed within
`src/main/java/org/apache/guacamole/auth` as
`TutorialAuthenticationProvider.java`.

Notice how simple the authentication provider is. The
`SimpleAuthenticationProvider` base class simplifies the
`AuthenticationProvider` interface, requiring nothing more than a unique
identifier (we will use “tutorial”) and a single getAuthorizedConfigurations()
implementation, which must return a `Map` of `GuacamoleConfiguration` each
associated with some arbitrary unique ID. This unique ID will be presented to
the user in the connection list after they log in.

For now, `getAuthorizedConfigurations()` will just return `null`. This will
cause Guacamole to report an invalid login for every attempt. Note that there
is a difference in semantics between returning an empty map and returning
`null`, as the former indicates the credentials are authorized but simply have
no associated configurations, while the latter indicates the credentials are
not authorized at all.

The only remaining piece for the overall skeleton to be complete is a
`guac-manifest.json` file. *This file is absolutely required for all Guacamole
extensions.* The `guac-manifest.json` format is described in more detail in
[guacamole-ext](guacamole-ext.html). It provides for quite a few properties, but for our
authentication extension we are mainly interested in the Guacamole version
sanity check (to make sure an extension built for the API of Guacamole version
X is not accidentally used against version Y) and telling Guacamole where to
find our authentication provider class.

The Guacamole extension format requires that `guac-manifest.json` be placed in
the root directory of the extension `.jar` file. To accomplish this with Maven,
we place it within the `src/main/resources` directory. Maven will automatically
pick it up during the build and include it within the `.jar`.

```
{

    "guacamoleVersion" : "1.6.0",

    "name"      : "Tutorial Authentication Extension",
    "namespace" : "guac-auth-tutorial",

    "authProviders" : [
        "org.apache.guacamole.auth.TutorialAuthenticationProvider"
    ]

}
```

## Building the extension[#](#building-the-extension "Link to this heading")

Once all three of the above files are in place, the extension will build, and
can even be installed within Guacamole (see [Installing the extension](#custom-auth-installing) at the
end of this chapter), even though it is just a skeleton at this point. It won’t
do anything yet other than reject all authentication attempts, but it’s good to
at least try building the extension to make sure nothing is missing and that
all steps have been followed correctly so far:

```
$ mvn package
[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Building guacamole-auth-tutorial 1.6.0
[INFO] ------------------------------------------------------------------------
...
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 2.345 s
[INFO] Finished at: 2015-12-16T13:39:00-08:00
[INFO] Final Memory: 14M/138M
[INFO] ------------------------------------------------------------------------
$
```

Assuming you see the “`BUILD SUCCESS`” message when you build the extension,
there will be a new file, `target/guacamole-auth-tutorial-1.6.0.jar`, which can
be installed within Guacamole and tested. If you changed the name or version of
the project in the `pom.xml` file, the name of this new `.jar` file will be
different, but it can still be found within `target/`.

## Configuration and authentication[#](#configuration-and-authentication "Link to this heading")

Once we receive credentials, we need to validate those credentials against the
associated properties in `guacamole.properties` (our source of authentication
information for the sake of this tutorial).

We will define four properties:

`tutorial-user`
:   The name of the only user we accept.

`tutorial-password`
:   The password we require for the user specified to be authenticated.

`tutorial-protocol`
:   The protocol of the configuration this user is authorized to use, which
    will be sent to guacd when the user logs in and selects their connection.

`tutorial-parameters`
:   A comma-delimited list of `name=value` pairs. For the sake of simplicity,
    we’ll assume there will never be any commas in the values.

If the username and password match what is stored in the file, we read the
configuration information, store it in a `GuacamoleConfiguration`, and return
the configuration within a set, telling Guacamole that this user is authorized
but only to access the configurations returned.

Upstream, we always place the properties of authentication providers in their
own class, and so we will also do that here in this tutorial, as it keeps
things organized.

```
package org.apache.guacamole.auth;

import org.apache.guacamole.properties.StringGuacamoleProperty;

/**
 * Utility class containing all properties used by the custom authentication
 * tutorial. The properties defined here must be specified within
 * guacamole.properties to configure the tutorial authentication provider.
 */
public class TutorialGuacamoleProperties {

    /**
     * This class should not be instantiated.
     */
    private TutorialGuacamoleProperties() {}

    /**
     * The only user to allow.
     */
    public static final StringGuacamoleProperty TUTORIAL_USER = 
        new StringGuacamoleProperty() {

        @Override
        public String getName() { return "tutorial-user"; }

    };

    /**
     * The password required for the specified user.
     */
    public static final StringGuacamoleProperty TUTORIAL_PASSWORD = 
        new StringGuacamoleProperty() {

        @Override
        public String getName() { return "tutorial-password"; }

    };


    /**
     * The protocol to use when connecting.
     */
    public static final StringGuacamoleProperty TUTORIAL_PROTOCOL = 
        new StringGuacamoleProperty() {

        @Override
        public String getName() { return "tutorial-protocol"; }

    };


    /**
     * All parameters associated with the connection, as a comma-delimited
     * list of name="value" 
     */
    public static final StringGuacamoleProperty TUTORIAL_PARAMETERS = 
        new StringGuacamoleProperty() {

        @Override
        public String getName() { return "tutorial-parameters"; }

    };

}
```

Normally, we would define a new type of `GuacamoleProperty` to handle the
parsing of the parameters required by `TUTORIAL_PARAMETERS`, but for the sake
of simplicity, parsing of this parameter will be embedded in the authentication
function later.

You will need to modify your existing `guacamole.properties` file, adding each
of the above properties to describe one of your available connections.

```
# Username and password
tutorial-user:     tutorial
tutorial-password: password

# Connection information
tutorial-protocol:   vnc
tutorial-parameters: hostname=localhost, port=5900
```

Once these properties and their accessor class are in place, it’s simple enough
to read the properties within `getAuthorizedConfigurations()` and authenticate
the user based on their username and password.

```
@Override
public Map<String, GuacamoleConfiguration>
    getAuthorizedConfigurations(Credentials credentials)
    throws GuacamoleException {

    // Get the Guacamole server environment
    Environment environment = LocalEnvironment.getInstance();

    // Get username from guacamole.properties
    String username = environment.getRequiredProperty(
        TutorialGuacamoleProperties.TUTORIAL_USER
    );      

    // If wrong username, fail
    if (!username.equals(credentials.getUsername()))
        return null;

    // Get password from guacamole.properties
    String password = environment.getRequiredProperty(
        TutorialGuacamoleProperties.TUTORIAL_PASSWORD
    );      

    // If wrong password, fail
    if (!password.equals(credentials.getPassword()))
        return null;

    // Successful login. Return configurations (STUB)
    return new HashMap<String, GuacamoleConfiguration>();

}
```

As is, the authentication provider will work in its current state in that the
correct username and password will authenticate the user, while an incorrect
username or password will not, but we still aren’t returning an actual map of
configurations. We need to construct the configuration based on the properties
in the `guacamole.properties` file after the user has been authenticated, and
return that configuration to the web application.

## Parsing the configuration[#](#parsing-the-configuration "Link to this heading")

The only remaining task before we have a fully-functioning authentication
provider is to actually parse the configuration from the `guacamole.properties`
file.

```
@Override
public Map<String, GuacamoleConfiguration>
    getAuthorizedConfigurations(Credentials credentials)
    throws GuacamoleException {

    // Get the Guacamole server environment
    Environment environment = LocalEnvironment.getInstance();

    // Get username from guacamole.properties
    String username = environment.getRequiredProperty(
        TutorialGuacamoleProperties.TUTORIAL_USER
    );      

    // If wrong username, fail
    if (!username.equals(credentials.getUsername()))
        return null;

    // Get password from guacamole.properties
    String password = environment.getRequiredProperty(
        TutorialGuacamoleProperties.TUTORIAL_PASSWORD
    );      

    // If wrong password, fail
    if (!password.equals(credentials.getPassword()))
        return null;

    // Successful login. Return configurations.
    Map<String, GuacamoleConfiguration> configs = 
        new HashMap<String, GuacamoleConfiguration>();

    // Create new configuration
    GuacamoleConfiguration config = new GuacamoleConfiguration();

    // Set protocol specified in properties
    config.setProtocol(environment.getRequiredProperty(
        TutorialGuacamoleProperties.TUTORIAL_PROTOCOL
    ));

    // Set all parameters, splitting at commas
    for (String parameterValue : environment.getRequiredProperty(
        TutorialGuacamoleProperties.TUTORIAL_PARAMETERS
    ).split(",\\s*")) {

        // Find the equals sign
        int equals = parameterValue.indexOf('=');
        if (equals == -1)
            throw new GuacamoleServerException("Required equals sign missing");

        // Get name and value from parameter string
        String name = parameterValue.substring(0, equals);
        String value = parameterValue.substring(equals+1);

        // Set parameter as specified
        config.setParameter(name, value);

    }

    configs.put("Tutorial Connection", config);
    return configs;

}
```

The extension is now complete and can be built as described earlier in
[Building the extension](#custom-auth-building).

## Installing the extension[#](#installing-the-extension "Link to this heading")

Guacamole extensions are self-contained `.jar` files which are installed by
being placed within `GUACAMOLE_HOME/extensions`, and this extension is no
different. As described in [Configuring Guacamole](configuring-guacamole.html), `GUACAMOLE_HOME` is a
placeholder used to refer to the directory that Guacamole uses to locate its
configuration files and extensions. Typically, this will be the `.guacamole`
directory within the home directory of the user running Tomcat.

To install your extension, ensure that the required properties have been added
to your `guacamole.properties`, copy the
`target/guacamole-auth-tutorial-1.6.0.jar` file into
`GUACAMOLE_HOME/extensions` and restart Tomcat. Guacamole will automatically
load your extension, logging an informative message that it has done so:

```
Extension "Tutorial Authentication Extension" loaded.
```

Contents

---
# Retrieving secrets from a vault

## Contents

# Retrieving secrets from a vault[#](#retrieving-secrets-from-a-vault "Link to this heading")

Guacamole supports reading secrets such as connection-specific passwords from a
key vault, automatically injecting those secrets into connection configurations
using [parameter tokens](configuring-guacamole.html#parameter-tokens) or Guacamole configuration
properties via an additional, vault-specific configuration file analogous to
`guacamole.properties`. This support is intended with multiple vault providers
in mind and currently supports [Keeper Secrets Manager (KSM)](https://www.keepersecurity.com/secrets-manager.html).

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling the vault extension[#](#installing-enabling-the-vault-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-vault-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-vault-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `ksm/guacamole-vault-ksm-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `KSM_ENABLED` environment variable:

    ```
    KSM_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e KSM_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `KSM_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `KSM_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

### Adding Guacamole to KSM[#](#adding-guacamole-to-ksm "Link to this heading")

Allowing an application like Guacamole to access secrets via KSM involves
creating an application in KSM. A KSM application is simply a means of
assigning permissions, narrowing exactly which secrets the application in
question should be able to access.

1. Log into your vault via the Keeper Security website and create at least one
   shared folder to house any secrets that should be made available to Apache
   Guacamole. These folders will be used when registering Apache Guacamole with
   KSM and functions to define exactly which secrets the application may access.
   **Secrets that are not within these shared folders will not be accessible by
   Guacamole.**

   The option for creating a shared folder is within a submenu that appears
   when you click on “Create New”:

   ![Submenu for creating new objects, including shared folders.](assets/doc_gug__images_vault-ksm-001a-create-shared-folder.png)

   No special options need to be selected for the shared folder except for
   providing a reasonable name for the folder:

   ![Shared folder creation dialog.](assets/doc_gug__images_vault-ksm-001b-create-shared-folder.png)
2. Navigate to KSM by selecting the “Secrets Manager” tab in the navigation
   sidebar on the left side of the screen:

   !["Secrets Manager" selected within the navigation sidebar.](assets/doc_gug__images_vault-ksm-002-select-ksm.png)
3. Click “Create Application” on the right ride of the toolbar near the top of
   the screen:

   !["Create Application" button in the KSM toolbar.](assets/doc_gug__images_vault-ksm-003a-create-application.png)

   The dialog that appears will prompt you to provide a name for the
   application that will access the vault, as well as the shared folder(s) that
   this application will have access to. Enter a reasonable name for the
   application, such as “Apache Guacamole”, and select the shared folder(s) you
   created for Guacamole to access:

   ![KSM application creation dialog.](assets/doc_gug__images_vault-ksm-003b-create-application.png)

   Guacamole only needs read-only access permissions to secrets, which should
   already be selected by default.

   Warning

   You should only check the “Lock external WAN IP” box if your Guacamole
   server has a static IP *and* you will be using the KSM CLI tool directly on
   that server. **If you will be running the KSM CLI tool on a separate machine
   with a different public IP address, you must not check this box.**
4. Once satisfied with the application name and parameters, click “Generate
   Token” to generate a one-time token:

   ![Application creation confirmation dialog showing the generated one-time token.](assets/doc_gug__images_vault-ksm-004-generate-token.png)

   This token can be used to generate a base64-encoded configuration blob as
   described in the following step, or it can be used directly to set a KSM
   config for a user or connection, as described in [the following section](#guac-vault-config).
5. Copy the provided one-time token using [the KSM CLI tool](https://docs.keeper.io/secrets-manager/secrets-manager/secrets-manager-command-line-interface/init-command)
   to obtain the base64-encoded configuration that must be provided to
   Guacamole with [the `ksm-config` property](#guac-vault-config). **This token
   can only be used once, but the base64 configuration can be used indefinitely
   unless manually revoked within KSM:**

   ```
   $ ./ksm init default US:_-L2NIxWdMatbyYwBnYROLlJVjeg4BzO3xZWoiDkh4U

   ewogICJjbGllbnRJZCI6ICJTR1ZzYkc4Z2RHaGxjbVVoSUZSb1pYTmxJSEJ5YjNCbGNuUnBaWE1n
   YUdGMlpTQmlaV1Z1SUcxaGJuVmhiR3g1SUhKbFpHRmpkR1ZrTGlCWGFIay9Qdz09IiwKICAicHJp
   dmF0ZUtleSI6ICJWRzhnWlc1emRYSmxJSFJvWVhRZ1lXTjBkV0ZzSUhObGJuTnBkR2wyWlNCMllX
   eDFaWE1nWVhKbElHNXZkQ0JsZUhCdmMyVmtJSFpwWVNCdmRYSWdiV0Z1ZFdGc0xpQlVhR1Y1SUcx
   aGVTQnViM1FnUVV4TUlHSmxJSE5sYm5OcGRHbDJaU0IyWVd4MVpYTXNJR0oxZENCaGRDQnNaV0Z6
   ZENCdmJtVWdjMlZsYlhNZ2RHOGdZbVV1IiwKICAiYXBwS2V5IjogIlYyVnNZMjl0WlNFZ1JXNXFi
   M2tnUVhCaFkyaGxJRWQxWVdOaGJXOXNaU0U9IiwKICAiaG9zdG5hbWUiOiAia2VlcGVyc2VjdXJp
   dHkuY29tIiwKICAic2VydmVyUHVibGljS2V5SWQiOiAiMTAiCn0K
   $
   ```

## Required configuration[#](#required-configuration "Link to this heading")

Native Webapp (Tomcat)

Guacamole requires only a single configuration property to configure secret
retrieval from KSM, `ksm-config`, which must be provided the base64
configuration value retrieved from KSM using the one-time token [obtained when
Guacamole was registered with KSM as an application as described above](#adding-guac-to-ksm).
All other properties are optional.

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
ksm-config: ewogICJjbGllbnRJZCI6ICJTR1ZzYkc4Z2RHaGxjbVVoSUZSb1pYTmxJSEJ5YjNC...
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`ksm-config`
:   The base64-encoded configuration information generated for the application
    you created within KSM to represent Apache Guacamole. The easiest way to
    obtain this value is using [the KSM CLI tool](https://docs.keeper.io/secrets-manager/secrets-manager/secrets-manager-command-line-interface/init-command).
    as described above. *This value is required.*

Container (Docker)

Guacamole requires only a single configuration property to configure secret
retrieval from KSM, `ksm-config`, which must be provided the base64
configuration value retrieved from KSM using the one-time token [obtained when
Guacamole was registered with KSM as an application as described above](#adding-guac-to-ksm).
All other environment variables are optional.

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
KSM_CONFIG: 'ewogICJjbGllbnRJZCI6ICJTR1ZzYkc4Z2RHaGxjbVVoSUZSb1pYTmxJSEJ5YjNC...'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e KSM_CONFIG="ewogICJjbGllbnRJZCI6ICJTR1ZzYkc4Z2RHaGxjbVVoSUZSb1pYTmxJSEJ5YjNC..." \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`KSM_CONFIG`
:   The base64-encoded configuration information generated for the application
    you created within KSM to represent Apache Guacamole. The easiest way to
    obtain this value is using [the KSM CLI tool](https://docs.keeper.io/secrets-manager/secrets-manager/secrets-manager-command-line-interface/init-command).
    as described above. *This value is required.*

## Additional vaults for users and connection groups[#](#additional-vaults-for-users-and-connection-groups "Link to this heading")

Native Webapp (Tomcat)

In addition to the required, application-wide vault, Guacamole can be
configured to pull secrets from separate vaults that are declared at the user
or connection group level. The configuration information for these vaults can
be set directly in the webapp, on the [connection group edit
page](administration.html#connection-group-management) and on the [user preferences
page](using-guacamole.html#preferences).

Hint

Unlike the application-wide vault (which must always be configured using a
lengthy blob of base64-encoded data), a one-time token obtained from KSM can be
used in these cases.

Because it is not necessarily desirable that users be able to provide their own
secrets for use within connections, administrators must explicitly enable this
functionality by:

1. Setting the relevant property to `true`, as described below.
2. Checking the “Allow user-provided KSM configuration” box on any connection
   that should be allowed to consume user-specific secrets.

**Secrets from a user-specific vault will not be used unless both of the above
conditions are true.**

`ksm-allow-user-config`
:   Whether or not users should be allowed to set their own KSM configuration,
    which will be used to pull secrets *only* when not already provided by the
    global or connection-group-level KSM configuration. A user-level KSM
    configuration will never be used if a matching secret is otherwise available.

Container (Docker)

In addition to the required, application-wide vault, Guacamole can be
configured to pull secrets from separate vaults that are declared at the user
or connection group level. The configuration information for these vaults can
be set directly in the webapp, on the [connection group edit
page](administration.html#connection-group-management) and on the [user preferences
page](using-guacamole.html#preferences).

Hint

Unlike the application-wide vault (which must always be configured using a
lengthy blob of base64-encoded data), a one-time token obtained from KSM can be
used in these cases.

Because it is not necessarily desirable that users be able to provide their own
secrets for use within connections, administrators must explicitly enable this
functionality by:

1. Setting the relevant property to `true`, as described below.
2. Checking the “Allow user-provided KSM configuration” box on any connection
   that should be allowed to consume user-specific secrets.

**Secrets from a user-specific vault will not be used unless both of the above
conditions are true.**

`KSM_ALLOW_USER_CONFIG`
:   Whether or not users should be allowed to set their own KSM configuration,
    which will be used to pull secrets *only* when not already provided by the
    global or connection-group-level KSM configuration. A user-level KSM
    configuration will never be used if a matching secret is otherwise available.

### Priorities of multiple vaults[#](#priorities-of-multiple-vaults "Link to this heading")

When multiple vaults apply to any connection attempt, secrets are pulled and
applied in a specific order of priority that is intended to ensure the
administrator always has ultimate control over the behavior of a connection:

1. **Application-wide vault:** Secrets are always pulled from the
   application-wide vault first (the vault provided with the `ksm-config`
   property).
2. **Connection group vault:** If a particular secret is not available within
   the application-wide vault, but the connection is within a connection group
   that has been configured with a KSM vault, the vault configured for that
   connection group is used to reattempt retrieving the secret.
3. **User-specific vault:** If a particular secret is not available within
   any other administator-controlled vault, the connection in question has
   been configured to allow user-specific vault use, and the current user has
   configured such a vault, that vault will be used to reattempt retrieving the
   secret.

By design, the application-wide vault always has the highest priority, and any
administrator-controlled vault always has priority over user-controlled vaults.

### Additional Configuration Options[#](#additional-configuration-options "Link to this heading")

Native Webapp (Tomcat)

The following additional, optional properties may be set as desired
to tailor the behavior of the KSM support:

`ksm-allow-unverified-cert`
:   Whether unverified server certificates should be accepted. If set to `true`,
    the server certificate for connections to the KSM service will be accepted even
    if they cannot be verified. **Unless you are a developer testing changes to
    the KSM vault support itself, it is unlikely that you need to set this
    property.**

`ksm-api-call-interval`
:   Specify the minimum number of milliseconds between calls to the KSM API. The
    API allows a limited number of calls per month, and calls over the included
    amount generate additional cost. Setting this property allows you to
    limit Guacamole’s impact on that cost.

`ksm-strip-windows-domains`
:   Whether or not the Windows domain should be stripped off of the username
    when usernames are retrieved from the KSM vault and placed into its own
    secret. This is optional, and by default it is false - domains will
    not be stripped from the username.

Container (Docker)

The following additional, optional environment variables may be set as desired
to tailor the behavior of the KSM support:

`KSM_ALLOW_UNVERIFIED_CERT`
:   Whether unverified server certificates should be accepted. If set to `true`,
    the server certificate for connections to the KSM service will be accepted even
    if they cannot be verified. **Unless you are a developer testing changes to
    the KSM vault support itself, it is unlikely that you need to set this
    property.**

`KSM_API_CALL_INTERVAL`
:   Specify the minimum number of milliseconds between calls to the KSM API. The
    API allows a limited number of calls per month, and calls over the included
    amount generate additional cost. Setting this property allows you to
    limit Guacamole’s impact on that cost.

`KSM_STRIP_WINDOWS_DOMAINS`
:   Whether or not the Windows domain should be stripped off of the username
    when usernames are retrieved from the KSM vault and placed into its own
    secret. This is optional, and by default it is false - domains will
    not be stripped from the username.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Retrieving connection secrets from a vault[#](#retrieving-connection-secrets-from-a-vault "Link to this heading")

Secrets for connection parameters are provided using [parameter
tokens](configuring-guacamole.html#parameter-tokens) that can be either automatically or manually defined.
Automatic tokens are [defined dynamically by Guacamole when the connection is
used](#vault-dynamic-secrets) based on other configuration values within the
connection, such as the connection’s `hostname` or `username`. Manual tokens
are injected by Guacamole based on secrets that are [statically mapped using an
additional configuration file](#vault-static-secrets).

### Automatic injection of secrets based on connection parameters[#](#automatic-injection-of-secrets-based-on-connection-parameters "Link to this heading")

Parameter tokens containing the values of secrets within a record are
automatically injected for connections whose parameter values match specific
criteria, such as having a particular `username` or `hostname`. This happens
whenever a connection is used and is fully dynamic, affecting only the state of
the connection from the perspective of the user accessing it.

Important

There are limitations to the degree that secrets can be automatically applied
based on connection parameters:

* In all cases, only unique records are considered. If multiple records match
  the criteria that applies to a particular token in the context of a
  connection, the token will not be injected for that connection.
* Automatic injection of secrets cannot currently be used with balancing
  connection groups, as the underlying connection that the balancing
  implementation will choose cannot be known before token values must be made
  available.

If automatic injection of secrets cannot work for your use case, consider using
[manually-specified secrets via `ksm-token-mapping.yml`](#vault-static-secrets).

Parameter tokens injected from KSM records take the form
`${KEEPER_CRITERIA_SECRET}`, where `CRITERIA` determines how the
applicable record is located based on the connection’s parameters and `SECRET`
determines what value is retrieved from that record.

The following `CRITERIA` names are supported:

`USER`
:   The record whose “login” field contains a username that matches the value of
    the `username` parameter of the connection. If the record has no “login” field,
    a “text” or “password” custom field will be used if the label of that field
    contains the word “username” (case-insensitive).

`SERVER`
:   The record whose “login” field contains a hostname that matches the value of
    the `hostname` parameter of the connection. If the record has no “login” field,
    a “text” or “password” custom field will be used if the label of that field
    contains the word “hostname”, “address”, or “IP address” (case-insensitive,
    ignoring any spaces between “IP” and “address”).

`GATEWAY`
:   Identical to `SERVER`, except that the value of the `gateway-hostname`
    parameter is used. This is only applicable to RDP connections.

`GATEWAY_USER`
:   Identical to `USER`, except that the value of the `gateway-username`
    parameter is used. This is only applicable to RDP connections.

The following `SECRET` types are supported:

`USERNAME`
:   The username specified by the record’s “login” field. If the field is a
    custom field, the label must contain the word “username” (case-insensitive)
    and must be a “text” or “hidden” field.

`DOMAIN`
:   The domain name of the record, either retrieved directly from the vault, or
    split out from the username if so configured in the vault. Typically this
    will apply when the username is associated with an Active Directory
    domain.

`PASSWORD`
:   The password specified by the record’s “password” or “hidden” field. If the
    field is a custom field, the label must contain the word “password”
    (case-insensitive).

`KEY`
:   The private key associated with the record. If the record has a dedicated
    key pair field, the private key from this field is used. If not, and the
    record has a single `.pem` file attached, the content of that attachment is
    used. Lacking any key pair field or attachment, any custom field that is a
    “password” or “hidden” field will be used as long as it contains the phrase
    “private key” in its label (case-insensitive, ignoring any space(s) between
    “private” and “key”).

`PASSPHRASE`
:   The passphrase associated with the record’s private key, if the record type
    has dedicated fields for these. If the record has no dedicated passphrase
    field, a “password” or “hidden” custom field will be used as long as it
    has the word “passphrase” in its label (case-insensitive).

For example, the `${KEEPER_USER_PASSWORD}` token would retrieve the password
for the user specified by the `username` parameter, and `${KEEPER_SERVER_KEY}`
would retrieve the private key for the server specified by the `hostname`
parameter.

### Manual definition of secrets[#](#manual-definition-of-secrets "Link to this heading")

Parameter tokens can be manually defined by placing a YAML file within
`GUACAMOLE_HOME` called `ksm-token-mapping.yml`. This file must contain a set
of name/value pairs where each name is the name of a token to define and each
value is [a reference to a secret in KSM using “Keeper Notation”](https://docs.keeper.io/secrets-manager/secrets-manager/about/keeper-notation).

For example, the following `ksm-token-mapping.yml` defines two parameter
tokens, `${WINDOWS_ADMIN_PASSWORD}` and `${LINUX_SERVER_KEY}`, each pulling
their values from different parts of different records in KSM:

```
WINDOWS_ADMIN_PASSWORD: keeper://odei1zeejoL7Ceiv3eig0a/field/password
LINUX_SERVER_KEY: keeper://Chah0VuPh0ohyeuL4che1o/file/idrsa.pem
```

Token substitution of other parameter tokens like `${GUAC_USERNAME}` is
performed *on the reference to the secret* to allow the reference to vary by
values that may be relevant to the connection. The values of substituted tokens
are URL-encoded before being placed into the reference in “Keeper Notation”. In
addition, the following tokens are available for use within the secret
reference:

`${CONNECTION_GROUP_NAME}`
:   The human-readable name of the connection group being used. Secrets using
    this token are only available if a user is directly connecting to a balancing
    connection group, not manually connecting to a connection within a group.

`${CONNECTION_GROUP_ID}`
:   The unique identifier of the connection group being used. Secrets using this
    token are only available if a user is directly connecting to a balancing
    connection group, not manually connecting to a connection within a group.

`${CONNECTION_NAME}`
:   The human-readable name of the connection being used. Secrets using this
    token are only available if a user is directly connecting to a connection, not
    connecting via a balancing group.

`${CONNECTION_ID}`
:   The unique identifier of the connection being used. Secrets using this token
    are only available if a user is directly connecting to a connection, not
    connecting via a balancing group.

`${CONNECTION_HOSTNAME}`
:   The value of the `hostname` parameter of the connection being used. Secrets
    using this token are only available if a user is directly connecting to a
    connection, not connecting via a balancing group.

`${CONNECTION_USERNAME}`
:   The value of the `username` parameter of the connection being used. Secrets
    using this token are only available if a user is directly connecting to a
    connection, not connecting via a balancing group.

`${USERNAME}`
:   The username of the current user, as stored with the user object representing
    that user in the system storing the relevant connection or connection group.
    This is not necessarily the same as `${GUAC_USERNAME}`, which is the username
    provided by the user as part of their credentials when they authenticated.

For example, to automatically define a token called `${LINUX_SERVER_KEY}` that
selects a private key from among several within the same record by searching
for a file named after the current user, the following YAML could be used:

```
LINUX_SERVER_KEY: keeper://Chah0VuPh0ohyeuL4che1o/file/${USERNAME}.pem
```

## Retrieving configuration properties from a vault[#](#retrieving-configuration-properties-from-a-vault "Link to this heading")

Secrets for Guacamole configuration properties are provided through [an
additional file within `GUACAMOLE_HOME` called `guacamole.properties.ksm`](#guacamole-properties-ksm).
This file is *identical* to `guacamole.properties` except that the values of properties
are [references to KSM secrets in “Keeper Notation”](https://docs.keeper.io/secrets-manager/secrets-manager/about/keeper-notation).
Secrets can be used for any Guacamole configuration property that isn’t
required to configure the KSM support.

For example, the following `guacamole.properties.ksm` defines both the
`mysql-username` and `mysql-password` properties using values from a single
record in KSM that contains a username/password pair:

```
mysql-username: keeper://iel4yeic5ahxae7Eereec7/field/login
mysql-password: keeper://iel4yeic5ahxae7Eereec7/field/password
```

Contents

---
# guacamole-common

## Contents

# guacamole-common[#](#guacamole-common "Link to this heading")

The Java API provided by the Guacamole project is called guacamole-common. It
provides a basic means of tunneling data between the JavaScript client provided
by guacamole-common-js and the native proxy daemon, guacd, and for dealing with
the Guacamole protocol. The purpose of this library is to facilitate the
creation of custom tunnels between the JavaScript client and guacd, allowing
your Guacamole-driven web application to enforce its own security model, if
any, and dictate exactly what connections are established.

## HTTP tunnel[#](#http-tunnel "Link to this heading")

The Guacamole Java API implements the HTTP tunnel using a servlet called
`GuacamoleHTTPTunnelServlet`. This servlet handles all requests coming to it
over HTTP from the JavaScript client, and translates them into connect, read,
or write requests, which each get dispatched to the `doConnect()`, `doRead()`,
and `doWrite()` functions accordingly.

Normally, you wouldn’t touch the `doRead()` and `doWrite()` functions, as these
have already been written to properly handle the requests of the JavaScript
tunnel, and if you feel the need to touch these functions, you are probably
better off writing your own tunnel implementation, although such a thing is
difficult to do in a performant way.

When developing an application based on the Guacamole API, you should use
`GuacamoleHTTPTunnelServlet` by extending it, implementing your own version of
`doConnect()`, which is the only abstract function it defines. The tutorial
later in this book demonstrating how to write a Guacamole-based web application
shows the basics of doing this, but generally, `doConnect()` is an excellent
place for authentication or other validation, as it is the responsibility of
`doConnect()` to create (or not create) the actual tunnel. If `doConnect()`
does not create the tunnel, communication between the JavaScript client and
guacd cannot take place, which is an ideal power to have as an authenticator.

The `doConnect()` function is expected to return a new `GuacamoleTunnel`, but
it is completely up to the implementation to decide how that tunnel is to be
created. The already-implemented parts of `GuacamoleHTTPTunnelServlet` then
return the unique identifier of this tunnel to the JavaScript client, allowing
its own tunnel implementation to continue to communicate with the tunnel
existing on the Java side.

Instances of `GuacamoleTunnel` are associated with a `GuacamoleSocket`, which
is the abstract interface surrounding the low-level connection to guacd.
Overall, there is a socket (`GuacamoleSocket`) which provides a TCP connection
to guacd. This socket is exposed to `GuacamoleTunnel`, which provides abstract
protocol access around what is actually (but secretly, through the abstraction
of the API) a TCP socket.

The Guacamole web application extends this tunnel servlet in order to implement
authentication at the lowest possible level, effectively prohibiting
communication between the client and any remote desktops unless they have
properly authenticated. Your own implementation can be considerably simpler,
especially if you don’t need authentication:

```
public class MyGuacamoleTunnelServlet
    extends GuacamoleHTTPTunnelServlet {

    @Override
    protected GuacamoleTunnel doConnect(HttpServletRequest request)
        throws GuacamoleException {

        // Connect to guacd here (this is a STUB)
        GuacamoleSocket socket;

        // Return a new tunnel which uses the connected socket
        return new SimpleGuacamoleTunnel(socket);

    }

}
```

## Using the Guacamole protocol[#](#using-the-guacamole-protocol "Link to this heading")

guacamole-common provides basic low-level support for the Guacamole protocol.
This low-level support is leveraged by the HTTP tunnel implementation to
satisfy the requirements of the JavaScript client implementation, as the
JavaScript client expects the handshake procedure to have already taken place.
This support exists through the `GuacamoleReader` and `GuacamoleWriter`
classes, which are similar to Java’s `Reader` and `Writer` classes, except that
they deal with the Guacamole protocol specifically, and thus have slightly
different contracts.

### `GuacamoleReader`[#](#guacamolereader "Link to this heading")

`GuacamoleReader` provides a very basic `read()` function which is required to
return one or more complete instructions in a `char` array. It also provides
the typical `available()` function, which informs you whether `read()` is
likely to block the next time it is called, and an even more abstract version
of `read()` called `readInstruction()` which returns one instruction at a time,
wrapped within a `GuacamoleInstruction` instance.

Normally, you would not need to use this class yourself. It is used by
`ConfiguredGuacamoleSocket` to complete the Guacamole protocol handshake
procedure, and it is used by `GuacamoleHTTPTunnelServlet` within `doRead()` to
implement the reading half of the tunnel.

The only concrete implementation of `GuacamoleReader` is
`ReaderGuacamoleReader`, which wraps a Java `Reader`, using that as the source
for data to parse into Guacamole instructions. Again, you would not normally
directly use this class, nor instantiate it yourself. A working, concrete
instance of `GuacamoleReader` can be retrieved from any `GuacamoleSocket` or
`GuacamoleTunnel`.

### `GuacamoleWriter`[#](#guacamolewriter "Link to this heading")

`GuacamoleWriter` provides a very basic `write()` function and a more abstract
version called `writeInstruction()` which writes instances of
`GuacamoleInstruction`. These functions are analogous to the `read()` and
`readInstruction()` functions provided by `GuacamoleReader`, and have similar
restrictions: the contract imposed by `write()` requires that written
instructions be complete.

The only concrete implementation of `GuacamoleWriter` is
`WriterGuacamoleWriter`, which wraps a Java `Writer`, using that as the
destination for Guacamole instruction data, but you would not normally directly
use this class, nor instantiate it yourself. It is used by
`ConfiguredGuacamoleSocket` to complete the Guacamole protocol handshake
procedure, and it is used by `GuacamoleHTTPTunnelServlet` within `doWrite()` to
implement the writing half of the tunnel.

If necessary, a `GuacamoleWriter` can be retrieved from any `GuacamoleSocket`
or `GuacamoleTunnel`, but in most cases, the classes provided by the Guacamole
Java API which already use `GuacamoleWriter` will be sufficient.

Contents

---
# Configuring Guacamole

## Contents

# Configuring Guacamole[#](#configuring-guacamole "Link to this heading")

After installing Guacamole, you need to configure users and connections before
Guacamole will work. This chapter covers general configuration of Guacamole and
the use of its default authentication method.

Regardless of the authentication method you use, Guacamole’s configuration
always consists of two main pieces: [a directory referred to as
`GUACAMOLE_HOME`](#guacamole-home), which is the primary search location for
configuration files, and [`guacamole.properties`](#initial-setup), the main
configuration file used by Guacamole and its extensions. If using [the Docker
images](guacamole-docker.html), these same configuration aspects are largely driven
by environment variables.

## `GUACAMOLE_HOME` (`/etc/guacamole`)[#](#guacamole-home-etc-guacamole "Link to this heading")

`GUACAMOLE_HOME` is the name given to Guacamole’s configuration directory,
which is located at `/etc/guacamole` by default. All configuration files,
extensions, etc. reside within this directory. The structure of
`GUACAMOLE_HOME` is rigorously defined, and consists of the following optional
files:

`guacamole.properties`
:   The main Guacamole configuration file. Properties within this file dictate
    how Guacamole will connect to guacd, and may configure the behavior of
    installed authentication extensions.

    When using the Docker image, or if the `enable-environment-properties`
    property has been set to `true`, properties that would normally need to be
    provided through this file can be instead provided through environment
    variables. Those environment variables are named by taking the property name,
    transforming it to uppercase, and replacing all the dashes with underscores.

`logback.xml`
:   Guacamole uses a logging system called Logback for all messages. By
    default, Guacamole will log to the console only, but you can change this
    by providing your own Logback configuration file.

`extensions/`
:   The install location for all Guacamole extensions. Guacamole will
    automatically load all `.jar` files within this directory on startup.

`lib/`
:   The search directory for libraries required by any Guacamole extensions.
    Guacamole will make the `.jar` files within this directory available to
    all extensions. If your extensions require additional libraries, such as
    database drivers, this is the proper place to put them.

### Overriding `GUACAMOLE_HOME`[#](#overriding-guacamole-home "Link to this heading")

If you cannot or do not wish to use `/etc/guacamole` for `GUACAMOLE_HOME`, the
location can be overridden through any of the following methods:

1. Creating a directory named `.guacamole`, within the home directory of *the
   user running the servlet container*. This directory will automatically be
   used for `GUACAMOLE_HOME` if it exists.
2. Specifying the full path to an alternative directory with the environment
   variable `GUACAMOLE_HOME`. *Be sure to consult the documentation for your
   servlet container to determine how to properly set environment variables.*
3. Specifying the full path to an alternative directory with the system
   property guacamole.home.

## Standard configuration options / `guacamole.properties`[#](#standard-configuration-options-guacamole-properties "Link to this heading")

The Guacamole web application uses one main configuration file called
`guacamole.properties`. This file is the common location for all configuration
properties read by Guacamole or any extension of Guacamole, including
authentication providers. If using [the Docker images](guacamole-docker.html), these
same properties are also configurable with environment variables. Both methods
of configuring Guacamole are documented here.

The `guacamole.properties` file is technically optional, but in practice will
always be used for at least some configuration options, either explicitly or
implicitly through the use of Docker images and environment variables. It is
used to provide additional configuration information for extensions, or to
reconfigure Guacamole’s standard options in situations where the defaults are
insufficient.

There are several standard configuration options that are always available for
use:

Native Webapp (Tomcat)

`api-session-timeout`
:   The amount of time, in minutes, to allow Guacamole sessions
    (authentication tokens) to remain valid despite inactivity. If omitted,
    Guacamole sessions will expire after 60 minutes of inactivity.

`api-max-request-size`
:   The maximum number of bytes to accept within the entity body of any
    particular HTTP request, where 0 indicates that no limit should be
    applied. If omitted, requests will be limited to 2097152 bytes (2 MB) by
    default. This limit does not apply to file uploads.

    If using a reverse proxy for SSL termination, *keep in mind that reverse
    proxies may enforce their own limits independently of this*. For example,
    [Nginx will enforce a 1 MB request size limit by
    default](reverse-proxy.html#nginx-file-upload-size).

`allowed-languages`
:   A comma-separated whitelist of language keys to allow as display language
    choices within the Guacamole interface. For example, to restrict Guacamole
    to only English and German, you would specify: `en, de`.

    As English is the fallback language, used whenever a translation key is
    missing from the chosen language, English should only be omitted from this
    list if you are absolutely positive that no strings are missing.

    The corresponding JSON of any built-in languages not listed here will
    still be available over HTTP, but the Guacamole interface will not use
    them, nor will they be used automatically based on local browser language.
    If omitted, all defined languages will be available.

`case-sensitivity`
:   This option allows an administrator to configure how Guacamole will
    handle case comparisons between different types of identifiers. There
    are four possible values for this setting: `enabled`, `usernames`,
    `group-names`, and `disabled`.

    Setting this to `enabled` means that Guacamole will treat both usernames
    and group names as case-sensitive. The `usernames` setting will cause
    Guacamole to treat usernames as case-sensitive, but group names as
    case-insensitive. The `group-names` setting will cause Guacamole to treat
    usernames as case-insensitive, while group names will be treated as case-
    sensitive. Finally, `disabled` will configure Guacamole to treat both
    usernames and group names as case-insensitive.

    In keeping with the behavior of Guacamole prior to the introduction of this
    configuration property, this will default to `enabled`, and case differences
    will be considered for both usernames and group names.

    Finally, whether or not various authentication systems actually process
    usernames in a case-sensitive manner is somewhat out of the control
    of Guacamole. For example, most LDAP directories do not factor case
    into queries for either usernames or group names, and enabling case-
    sensitivity in Guacamole for either usernames, group names, or both, will
    not suddenly force your LDAP directory to perform case-sensitive
    comparisons. This option controls how Guacamole handles usernames and/or
    group names of various cases, not the underlying authentication system.

`enable-environment-properties`
:   If set to “true”, Guacamole will first evaluate its environment to obtain
    the value for any given configuration property, before using a value
    specified in `guacamole.properties` or falling back to a default value. By
    enabling this option, you can easily override any other configuration
    property using an environment variable.

    When searching for a configuration property in the environment, the name
    of the property is first transformed by converting all lower case
    characters to their upper case equivalents, and by replacing all hyphen
    characters (`-`) with underscore characters (`_`). For example, the
    `guacd-hostname` property would be transformed to `GUACD_HOSTNAME` when
    searching the environment.

`extension-priority`
:   A comma-separated list of the namespaces of all extensions that should be
    loaded in a specific order. The special value `*` can be used in lieu of a
    namespace to represent all extensions that are not listed. All extensions
    explicitly listed will be sorted in the order given, while all extensions
    not explicitly listed will be sorted by their filenames.

    For example, to ensure support for SAML is loaded *first*, set this value to
    `saml`. To ensure support for SAML is loaded *last*, set this value to `*, saml`.

    If unsure which namespaces apply or the order that your extensions are
    loaded, check the Guacamole logs. The namespaces and load order of all
    installed extensions are logged by Guacamole during startup:

    ```
    ...
    23:32:06.467 [main] INFO  o.a.g.extension.ExtensionModule - Multiple extensions are installed and will be loaded in order of decreasing priority:
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [postgresql] "PostgreSQL Authentication" (/etc/guacamole/extensions/guacamole-auth-jdbc-postgresql-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [ldap] "LDAP Authentication" (/etc/guacamole/extensions/guacamole-auth-ldap-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [openid] "OpenID Authentication Extension" (/etc/guacamole/extensions/guacamole-auth-sso-openid-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [saml] "SAML Authentication Extension" (/etc/guacamole/extensions/guacamole-auth-sso-saml-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule - To change this order, set the "extension-priority" property or rename the extension files. The default priority of extensions is dictated by the sort order of their filenames.
    ...
    ```

`guacd-hostname`
:   The host the Guacamole proxy daemon (guacd) is listening on. If omitted,
    Guacamole will assume guacd is listening on localhost.

`guacd-port`
:   The port the Guacamole proxy daemon (guacd) is listening on. If omitted,
    Guacamole will assume guacd is listening on port 4822.

`guacd-ssl`
:   If set to “true”, Guacamole will require SSL/TLS encryption between the
    web application and guacd. By default, communication between the web
    application and guacd will be unencrypted.

    Note that if you enable this option, you must also configure guacd to use
    SSL via command line options. These options are documented in the manpage
    of guacd. You will need an SSL certificate and private key.

`log-level`
:   The most verbose level of log message that should be visible in the web
    application logs. By default, the highest level of verbosity that will be
    logged is `info`. In order of increasing verbosity, the available log levels
    are: `error`, `warn`, `info`, `debug`, and `trace`.

    This can also be configured by [supplying a `logback.xml`
    file](#webapp-logging), which provides greater flexibility and control. It is
    unusual to need that level of flexibility, and this simpler configuration
    option is typically sufficient.

`skip-if-unavailable`
:   A comma-separated list of the identifiers of authentication providers that
    should be allowed to fail internally without aborting the authentication
    process. For example, to request that Guacamole ignore failures due to the
    LDAP directory or MySQL server being unexpectedly down, allowing other
    authentication providers to continue functioning, set this value to
    `mysql, ldap`.

    By default, Guacamole takes a conservative approach to internal failures,
    aborting the authentication process if an internal error occurs within any
    authentication provider. Depending on the nature of the error, this may
    mean that no users can log in until the cause of the failure is dealt
    with. This configuration option may be used to explicitly inform Guacamole
    that one or more underlying systems are expected to occasionally experience
    failures, and that other functioning systems should be relied upon if they do
    fail.

Container (Docker)

`API_SESSION_TIMEOUT`
:   The amount of time, in minutes, to allow Guacamole sessions
    (authentication tokens) to remain valid despite inactivity. If omitted,
    Guacamole sessions will expire after 60 minutes of inactivity.

`API_MAX_REQUEST_SIZE`
:   The maximum number of bytes to accept within the entity body of any
    particular HTTP request, where 0 indicates that no limit should be
    applied. If omitted, requests will be limited to 2097152 bytes (2 MB) by
    default. This limit does not apply to file uploads.

    If using a reverse proxy for SSL termination, *keep in mind that reverse
    proxies may enforce their own limits independently of this*. For example,
    [Nginx will enforce a 1 MB request size limit by
    default](reverse-proxy.html#nginx-file-upload-size).

`ALLOWED_LANGUAGES`
:   A comma-separated whitelist of language keys to allow as display language
    choices within the Guacamole interface. For example, to restrict Guacamole
    to only English and German, you would specify: `en, de`.

    As English is the fallback language, used whenever a translation key is
    missing from the chosen language, English should only be omitted from this
    list if you are absolutely positive that no strings are missing.

    The corresponding JSON of any built-in languages not listed here will
    still be available over HTTP, but the Guacamole interface will not use
    them, nor will they be used automatically based on local browser language.
    If omitted, all defined languages will be available.

`CASE_SENSITIVITY`
:   This option allows an administrator to configure how Guacamole will
    handle case comparisons between different types of identifiers. There
    are four possible values for this setting: `enabled`, `usernames`,
    `group-names`, and `disabled`.

    Setting this to `enabled` means that Guacamole will treat both usernames
    and group names as case-sensitive. The `usernames` setting will cause
    Guacamole to treat usernames as case-sensitive, but group names as
    case-insensitive. The `group-names` setting will cause Guacamole to treat
    usernames as case-insensitive, while group names will be treated as case-
    sensitive. Finally, `disabled` will configure Guacamole to treat both
    usernames and group names as case-insensitive.

    In keeping with the behavior of Guacamole prior to the introduction of this
    configuration property, this will default to `enabled`, and case differences
    will be considered for both usernames and group names.

    Finally, whether or not various authentication systems actually process
    usernames in a case-sensitive manner is somewhat out of the control
    of Guacamole. For example, most LDAP directories do not factor case
    into queries for either usernames or group names, and enabling case-
    sensitivity in Guacamole for either usernames, group names, or both, will
    not suddenly force your LDAP directory to perform case-sensitive
    comparisons. This option controls how Guacamole handles usernames and/or
    group names of various cases, not the underlying authentication system.

`EXTENSION_PRIORITY`
:   A comma-separated list of the namespaces of all extensions that should be
    loaded in a specific order. The special value `*` can be used in lieu of a
    namespace to represent all extensions that are not listed. All extensions
    explicitly listed will be sorted in the order given, while all extensions
    not explicitly listed will be sorted by their filenames.

    For example, to ensure support for SAML is loaded *first*, set this value to
    `saml`. To ensure support for SAML is loaded *last*, set this value to `*, saml`.

    If unsure which namespaces apply or the order that your extensions are
    loaded, check the Guacamole logs. The namespaces and load order of all
    installed extensions are logged by Guacamole during startup:

    ```
    ...
    23:32:06.467 [main] INFO  o.a.g.extension.ExtensionModule - Multiple extensions are installed and will be loaded in order of decreasing priority:
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [postgresql] "PostgreSQL Authentication" (/etc/guacamole/extensions/guacamole-auth-jdbc-postgresql-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [ldap] "LDAP Authentication" (/etc/guacamole/extensions/guacamole-auth-ldap-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [openid] "OpenID Authentication Extension" (/etc/guacamole/extensions/guacamole-auth-sso-openid-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule -  - [saml] "SAML Authentication Extension" (/etc/guacamole/extensions/guacamole-auth-sso-saml-1.6.0.jar)
    23:32:06.468 [main] INFO  o.a.g.extension.ExtensionModule - To change this order, set the "extension-priority" property or rename the extension files. The default priority of extensions is dictated by the sort order of their filenames.
    ...
    ```

`GUACD_HOSTNAME`
:   The host the Guacamole proxy daemon (guacd) is listening on. If omitted,
    Guacamole will assume guacd is listening on localhost.

`GUACD_PORT`
:   The port the Guacamole proxy daemon (guacd) is listening on. If omitted,
    Guacamole will assume guacd is listening on port 4822.

`GUACD_SSL`
:   If set to “true”, Guacamole will require SSL/TLS encryption between the
    web application and guacd. By default, communication between the web
    application and guacd will be unencrypted.

    Note that if you enable this option, you must also configure guacd to use
    SSL via command line options. These options are documented in the manpage
    of guacd. You will need an SSL certificate and private key.

`LOG_LEVEL`
:   The most verbose level of log message that should be visible in the web
    application logs. By default, the highest level of verbosity that will be
    logged is `info`. In order of increasing verbosity, the available log levels
    are: `error`, `warn`, `info`, `debug`, and `trace`.

    This can also be configured by [supplying a `logback.xml`
    file](#webapp-logging), which provides greater flexibility and control. It is
    unusual to need that level of flexibility, and this simpler configuration
    option is typically sufficient.

`SKIP_IF_UNAVAILABLE`
:   A comma-separated list of the identifiers of authentication providers that
    should be allowed to fail internally without aborting the authentication
    process. For example, to request that Guacamole ignore failures due to the
    LDAP directory or MySQL server being unexpectedly down, allowing other
    authentication providers to continue functioning, set this value to
    `mysql, ldap`.

    By default, Guacamole takes a conservative approach to internal failures,
    aborting the authentication process if an internal error occurs within any
    authentication provider. Depending on the nature of the error, this may
    mean that no users can log in until the cause of the failure is dealt
    with. This configuration option may be used to explicitly inform Guacamole
    that one or more underlying systems are expected to occasionally experience
    failures, and that other functioning systems should be relied upon if they do
    fail.

## Logging within the web application[#](#logging-within-the-web-application "Link to this heading")

By default, Guacamole logs all messages to the console. Servlet containers like
Tomcat will automatically redirect these messages to a log file, `catalina.out`
in the case of Tomcat, which you can read through while Guacamole runs. When
using [the Docker images](guacamole-docker.html), the same logs are visible in the
Docker logs using the `docker logs` command.

Messages are logged at any of five different log levels, depending on message
importance and severity:

`error`
:   Errors are fatal conditions. An operation, described in the log message,
    was attempted but could not proceed, and the failure of this operation is
    a serious problem that needs to be addressed.

`warn`
:   Warnings are generally non-fatal conditions. The operation continued, but
    encountered noteworthy problems.

`info`
:   “Info” messages are purely informational. They may be useful or
    interesting to administrators, but are not generally critical to proper
    operation of a Guacamole server.

`debug`
:   Debug messages are highly detailed and oriented toward development. Most
    debug messages will contain stack traces and internal information that is
    useful when investigating problems within code. It is expected that debug
    messages, though verbose, will not affect performance.

`trace`
:   Trace messages are similar to debug messages in intent and verbosity, but
    are so low-level that they may affect performance due to their frequency.
    Trace-level logging is rarely necessary, and is mainly useful in providing
    highly detailed context around issues being investigated.

Guacamole logs messages using a logging framework called
[Logback](http://logback.qos.ch/) and, by default, will only log messages at
the “`info`” level or higher. If you wish to change the log level, or configure
how or where Guacamole logs messages, you can do so by providing your own
`logback.xml` file within `GUACAMOLE_HOME`. For example, to log all messages
to the console, even “`debug`” messages, you might use the following
`logback.xml`:

```
<configuration>

    <!-- Appender for debugging -->
    <appender name="GUAC-DEBUG" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Log at DEBUG level -->
    <root level="debug">
        <appender-ref ref="GUAC-DEBUG"/>
    </root>

</configuration>
```

Guacamole and the above example configure only one appender which logs to the
console, but Logback is extremely flexible and allows any number of appenders
which can each log to separate files, the console, etc. based on a number of
criteria, including the log level and the source of the message.

More thorough [documentation on configuring
Logback](http://logback.qos.ch/manual/configuration.html) is provided on the
Logback project’s web site.

## Using the default authentication[#](#using-the-default-authentication "Link to this heading")

Guacamole’s default authentication module is simple and consists of a mapping
of usernames to configurations. This authentication module comes with Guacamole
and simply reads usernames and passwords from an XML file. It is always
enabled, but will only read from the XML file if it exists, and is always last
in priority relative to any other authentication extensions.

There are other authentication modules available. The Guacamole project
provides database-backed authentication modules with the ability to manage
connections and users from the web interface, and other authentication modules
can be created using the extension API provided along with the Guacamole web
application, guacamole-ext.

### `user-mapping.xml`[#](#user-mapping-xml "Link to this heading")

The default authentication provider used by Guacamole reads all username,
password, and configuration information from a file called the “user mapping”
located at `GUACAMOLE_HOME/user-mapping.xml`. An example of a user mapping file
is included with Guacamole, and looks something like this:

```
<user-mapping>

    <!-- Per-user authentication and config information -->
    <authorize username="USERNAME" password="PASSWORD">
        <protocol>vnc</protocol>
        <param name="hostname">localhost</param>
        <param name="port">5900</param>
        <param name="password">VNCPASS</param>
    </authorize>

    <!-- Another user, but using md5 to hash the password
         (example below uses the md5 hash of "PASSWORD") -->
    <authorize
            username="USERNAME2"
            password="319f4d26e3c536b5dd871bb2c52e3178"
            encoding="md5">

        <!-- First authorized connection -->
        <connection name="localhost">
            <protocol>vnc</protocol>
            <param name="hostname">localhost</param>
            <param name="port">5901</param>
            <param name="password">VNCPASS</param>
        </connection>

        <!-- Second authorized connection -->
        <connection name="otherhost">
            <protocol>vnc</protocol>
            <param name="hostname">otherhost</param>
            <param name="port">5900</param>
            <param name="password">VNCPASS</param>
        </connection>

    </authorize>

</user-mapping>
```

Each user is specified with a corresponding `<authorize>` tag. This tag
contains all authorized connections for that user, each denoted with a
`<connection>` tag. Each `<connection>` tag contains a corresponding protocol
and set of protocol-specific parameters, specified with the `<protocol>` and
`<param>` tags respectively.

#### Adding users[#](#adding-users "Link to this heading")

When using `user-mapping.xml`, username/password pairs are specified with
`<authorize>` tags, which each have a `username` and `password` attribute. Each
`<authorize>` tag authorizes a specific username/password pair to access all
connections within the tag:

```
<authorize username="USER" password="PASS">
    ...
</authorize>
```

In the example above, the password would be listed in plaintext. If you don’t
want to do this, you can also specify your password hashed with MD5:

```
<authorize username="USER"
           password="319f4d26e3c536b5dd871bb2c52e3178"
           encoding="md5">
    ...
</authorize>
```

After modifying `user-mapping.xml`, the file will be automatically reread by
Guacamole, and your changes will take effect immediately. The newly-added user
will be able to log in - no restart of the servlet container is needed.

#### Adding connections to a user[#](#adding-connections-to-a-user "Link to this heading")

To specify a connection within an `<authorize>` tag, you can either list a
single protocol and set of parameters (specified with a `<protocol>` tag and
any number of `<param>` tags), in which case that user will have access to only
one connection named “DEFAULT”, or you can specify one or more connections with
one or more `<connection>` tags, each of which can be named and contains a
`<protocol>` tag and any number of `<param>` tags.

## Configuring connections[#](#configuring-connections "Link to this heading")

Each protocol supported by Guacamole has its own set of configuration
parameters. These parameters typically describe the hostname and port of the
remote desktop server, the credentials to use when connecting, if any, and the
size and color depth of the display. If the protocol supports file transfer,
options for enabling that functionality will be provided as well.

### VNC[#](#vnc "Link to this heading")

The VNC protocol is the simplest and first protocol supported by Guacamole.
Although generally not as fast as RDP, many VNC servers are adequate, and VNC
over Guacamole tends to be faster than VNC by itself due to decreased bandwidth
usage.

VNC support for Guacamole is provided by the libguac-client-vnc library, which
will be installed as part of guacamole-server if the required dependencies are
present during the build.

Note

In addition to the VNC-specific parameters below, Guacamole’s VNC support also
accepts the parameters of several features that Guacamole provides for multiple
protocols:

* [Disabling clipboard access](#disable-clipboard)
* [File transfer via SFTP](#common-sftp)
* [Graphical session recording](#graphical-recording)
* [Wake-on-LAN](#wake-on-lan)

#### Network parameters[#](#network-parameters "Link to this heading")

With the exception of reverse-mode VNC connections, VNC works by making
outbound network connections to a particular host which runs one or more VNC
servers. Each VNC server is associated with a display number, from which the
appropriate port number is derived.

`hostname`
:   The hostname or IP address of the VNC server Guacamole should connect to.

`port`
:   The port the VNC server is listening on, usually 5900 or 5900 + display
    number. For example, if your VNC server is serving display number 1
    (sometimes written as `:1`), your port number here would be 5901.

`autoretry`
:   The number of times to retry connecting before giving up and returning an
    error. In the case of a reverse connection, this is the number of times
    the connection process is allowed to time out.

#### Authentication[#](#authentication "Link to this heading")

The VNC standard defines only password based authentication. Other
authentication mechanisms exist, but are non-standard or proprietary.
Guacamole currently supports both standard password-only based authentication,
as well as username and password authentication.

`username`
:   The username to use when attempting authentication, if any. This parameter
    is optional.

`password`
:   The password to use when attempting authentication, if any. This parameter
    is optional.

These credentials may be requested by one of several different underlying
authentication schemes, depending on the server configuration. The libvncclient
library supports several of these, depending on the version of the library
present on the system running guacd. Notably, the MSLogonII authentication
protocol is only supported the most recent libvncclient release. If in
doubt, or you encounter issues trying to log on to certain VNC servers,
check the version of libvncclient that you’re building guacd against and
make sure it includes support for the authentication scheme of the
server to which you’re trying to connect.

#### Display settings[#](#display-settings "Link to this heading")

Many VNC servers do not allow the client to request or change the display
size, though there are some that support dynamic display size updates. However,
unlike RDP, there is no strict requirement that the VNC server honor or
support those updates, so you are at the mercy of your VNC server with respect
to display width and height and whether or not it matches that of your client.
Guacamole, by default, attempts to negotiate this support with the VNC
server and send the client (browser) display dimensions to the VNC server.

To reduce bandwidth usage, you may request that the VNC server reduce its
color depth. Guacamole will automatically detect 256-color images, but this
can be guaranteed for absolutely all graphics sent over the connection by
forcing the color depth to 8-bit. Color depth is otherwise dictated by the VNC
server.

If you are noticing problems with your VNC display, such as the lack of a mouse
cursor, the presence of multiple mouse cursors, or strange colors (such as blue
colors appearing more like orange or red), these are typically the result of
bugs or limitations within the VNC server, and additional parameters are
available to work around such issues.

`color-depth`
:   The color depth to request, in bits-per-pixel. This parameter is optional.
    If specified, this must be either 8, 16, 24, or 32. Regardless of what
    value is chosen here, if a particular update uses less than 256 colors,
    Guacamole will always send that update as a 256-color PNG.

`disable-server-input`
:   Whether or not the VNC client should ask the VNC server to disable local
    input devices when the client connects. Some VNC servers support this
    feature in order to give preference to input from the client, and to
    avoid situations where the local keyboard and/or mouse may be “fighting”
    with the remote keyboard and/or mouse for control. Note that this
    requires the remote VNC server to have this feature supported and
    enabled, and there is no guarantee that the remote system will honor
    the request. Setting this parameter to “true” will request that the
    VNC server disable the local input devices; leaving it blank or
    setting to false will not make that request. This parameter is
    optional.

`disable-display-resize`
:   Whether or not the VNC client should *not* attempt to update the
    remote (server) display with its size. By default, when Guacamole
    connects to a VNC server, it will check for server support for
    configuring the remote display size, and will attempt to send the
    size of the browser area to the server to set the remote display
    to the same size as the browser. Also, if the browser window is
    resized, Guacamole will detect the resize and send the updated
    size to the server. If the server supports dynamic resizing, it
    may adjust the display size to match the browser. If this option
    is set to true, Guacamole will disable the client-side display
    updates, and the size of the desktop will not be sent to the
    VNC server, either during initial connection or when the browser
    is resized.

`swap-red-blue`
:   If the colors of your display appear wrong (blues appear orange or red,
    etc.), it may be that your VNC server is sending image data incorrectly,
    and the red and blue components of each color are swapped. If this is the
    case, set this parameter to “true” to work around the problem. This
    parameter is optional.

`cursor`
:   If set to “remote”, the mouse pointer will be rendered remotely, and the
    local position of the mouse pointer will be indicated by a small dot. A
    remote mouse cursor will feel slower than a local cursor, but may be
    necessary if the VNC server does not support sending the cursor image to
    the client.

`encodings`
:   A space-delimited list of VNC encodings to use. The format of this
    parameter is dictated by libvncclient and thus doesn’t really follow the
    form of other Guacamole parameters. This parameter is optional, and
    libguac-client-vnc will use any supported encoding by default.

    Beware that this parameter is intended to be replaced with individual,
    encoding-specific parameters in a future release.

`read-only`
:   Whether this connection should be read-only. If set to “true”, no input
    will be accepted on the connection at all. Users will only see the desktop
    and whatever other users using that same desktop are doing. This parameter
    is optional.

`force-lossless`
:   Whether this connection should only use lossless compression for graphical
    updates. If set to “true”, lossy compression will not be used. This
    parameter is optional. By default, lossy compression will be used when
    heuristics determine that it would likely outperform lossless compression.

`compress-level`
:   Controls the level of compression requested of the VNC server when either
    tight or zlib encoding is in use, on a scale of 0 to 9, with 0 being no
    compression and 9 being the highest level of compression. Note that this
    is negotiated with the server, and ultimately the decision on the amount
    of compression that is done is up to the VNC server.

`quality-level`
:   Sets the JPEG qualit level, on a scale of 0 to 9, when the tight encoding
    is in use, with 0 being the lowest image quality (but likely improved
    compression and speed) and 9 being the highest image quality but with
    reduced compression and speed.

#### VNC Repeater[#](#vnc-repeater "Link to this heading")

There exist VNC repeaters, such as UltraVNC Repeater, which act as
intermediaries or proxies, providing a single logical VNC connection which is
then routed to another VNC server elsewhere. Additional parameters are required
to select which VNC host behind the repeater will receive the connection.

`dest-host`
:   The destination host to request when connecting to a VNC proxy such as
    UltraVNC Repeater. This is only necessary if the VNC proxy in use requires
    the connecting user to specify which VNC server to connect to. If the VNC
    proxy automatically connects to a specific server, this parameter is not
    necessary.

`dest-port`
:   The destination port to request when connecting to a VNC proxy such as
    UltraVNC Repeater. This is only necessary if the VNC proxy in use requires
    the connecting user to specify which VNC server to connect to. If the VNC
    proxy automatically connects to a specific server, this parameter is not
    necessary.

#### Reverse VNC connections[#](#reverse-vnc-connections "Link to this heading")

Guacamole supports “reverse” VNC connections, where the VNC client listens for
an incoming connection from the VNC server. When reverse VNC connections are
used, the VNC client and server switch network roles, but otherwise function as
they normally would. The VNC server still provides the remote display, and the
VNC client still provides all keyboard and mouse input.

`reverse-connect`
:   Whether reverse connection should be used. If set to “true”, instead of
    connecting to a server at a given hostname and port, guacd will listen on
    the given port for inbound connections from a VNC server.

`listen-timeout`
:   If reverse connection is in use, the maximum amount of time to wait for an
    inbound connection from a VNC server, in milliseconds. If blank, the
    default value is 5000 (five seconds).

#### Audio support (via PulseAudio)[#](#audio-support-via-pulseaudio "Link to this heading")

VNC does not provide its own support for audio, but Guacamole’s VNC support can
obtain audio through a secondary network connection to a PulseAudio server
running on the same machine as the VNC server.

Most Linux systems provide audio through a service called PulseAudio. This
service is capable of communicating over the network, and if PulseAudio is
configured to allow TCP connections, Guacamole can connect to your PulseAudio
server and combine its audio with the graphics coming over VNC.

Configuring PulseAudio for network connections requires an additional line
within the PulseAudio configuration file, usually `/etc/pulse/default.pa`:

```
load-module module-native-protocol-tcp auth-ip-acl=192.168.1.0/24 auth-anonymous=1
```

This loads the TCP module for PulseAudio, configuring it to accept connections
without authentication and *only* from the `192.168.1.0/24` subnet. You will
want to replace this value with the subnet or IP address from which guacd will
be connecting. It is possible to allow connections from absolutely anywhere,
but beware that you should only do so if the nature of your network prevents
unauthorized access:

```
load-module module-native-protocol-tcp auth-anonymous=1
```

In either case, the `auth-anonymous=1` parameter is strictly required.
Guacamole does not currently support the cookie-based authentication used by
PulseAudio for non-anonymous connections. If this parameter is omitted,
Guacamole will not be able to connect to PulseAudio.

Once the PulseAudio configuration file has been modified appropriately, restart
the PulseAudio service. PulseAudio should then begin listening on port 4713
(the default PulseAudio port) for incoming TCP connections. You can verify this
using a utility like **netstat**:

```
$ netstat -ln | grep 4713
tcp        0      0 0.0.0.0:4713            0.0.0.0:*               LISTEN
tcp6       0      0 :::4713                 :::*                    LISTEN
$
```

The following parameters are available for configuring the audio support for
VNC:

`enable-audio`
:   If set to “true”, audio support will be enabled, and a second connection
    for PulseAudio will be made in addition to the VNC connection. By default,
    audio support within VNC is disabled.

`audio-servername`
:   The name of the PulseAudio server to connect to. This will be the hostname
    of the computer providing audio for your connection via PulseAudio, most
    likely the same as the value given for the `hostname` parameter.

    If this parameter is omitted, the default PulseAudio device will be used,
    which will be the PulseAudio server running on the same machine as guacd.

#### Clipboard encoding[#](#clipboard-encoding "Link to this heading")

While Guacamole will always use UTF-8 for its own clipboard data, the VNC
standard requires that clipboard data be encoded in ISO 8859-1. As most VNC
servers will not accept data in any other format, Guacamole will translate
between UTF-8 and ISO 8859-1 when exchanging clipboard data with the VNC
server, but this behavior can be overridden with the `clipboard-encoding`
parameter.

Important

*The only clipboard encoding guaranteed to be supported by VNC servers is ISO
8859-1.* You should only override the clipboard encoding using the
`clipboard-encoding` parameter of you are absolutely positive your VNC server
supports other encodings.

`clipboard-encoding`
:   The encoding to assume for the VNC clipboard. This parameter is optional.
    By default, the standard encoding ISO 8859-1 will be used. *Only use this
    parameter if you are sure your VNC server supports other encodings beyond
    the standard ISO 8859-1.*

    Possible values are:

    ISO8859-1
    :   ISO 8859-1 is the clipboard encoding mandated by the VNC standard, and
        supports only basic Latin characters. Unless your VNC server specifies
        otherwise, this encoding is the only encoding guaranteed to work.

    UTF-8
    :   UTF-8 - the most common encoding used for Unicode. Using this encoding
        for the VNC clipboard violates the VNC specification, but some servers
        do support this. This parameter value should only be used if you know
        your VNC server supports this encoding.

    UTF-16
    :   UTF-16 - a 16-bit encoding for Unicode which is not as common as UTF-8,
        but still widely used. Using this encoding for the VNC clipboard
        violates the VNC specification. This parameter value should only be used
        if you know your VNC server supports this encoding.

    CP1252
    :   Code page 1252 - a Windows-specific encoding for Latin characters which
        is mostly a superset of ISO 8859-1, mapping some additional displayable
        characters onto what would otherwise be control characters. Using this
        encoding for the VNC clipboard violates the VNC specification. This
        parameter value should only be used if you know your VNC server supports
        this encoding.

#### Adding a VNC connection[#](#adding-a-vnc-connection "Link to this heading")

If you are using the default authentication built into Guacamole, and you wish
to grant access to a VNC connection to a particular user, you need to locate
the `<authorize>` section for that user within your `user-mapping.xml`, and add
a section like the following within it:

```
<connection name="Unique Name">
    <protocol>vnc</protocol>
    <param name="hostname">localhost</param>
    <param name="port">5901</param>
</connection>
```

If added exactly as above, a new connection named “`Unique Name`” will be
available to the user associated with the `<authorize>` section containing it.
The connection will use VNC to connect to localhost at port 5901. Naturally,
you will want to change some or all of these values.

If your VNC server requires a password, or you wish to specify other
configuration parameters (to reduce the color depth, for example), you will
need to add additional `<param>` tags accordingly.

Other authentication methods will provide documentation describing how to
configure new connections. If the authentication method in use fully implements
the features of Guacamole’s authentication API, you will be able to add a new
VNC connection easily and intuitively using the administration interface built
into Guacamole. You will not need to edit configuration files.

#### Which VNC server?[#](#which-vnc-server "Link to this heading")

The choice of VNC server can make a big difference when it comes to
performance, especially over slower networks. While many systems provide VNC
access by default, using this is often not the fastest method.

##### RealVNC or TigerVNC[#](#realvnc-or-tigervnc "Link to this heading")

RealVNC, and its derivative TigerVNC, perform quite well. In our testing, they
perform the best with Guacamole. If you are okay with having a desktop that can
only be accessed via VNC, one of these is likely your best choice. Both
optimize window movement and (depending on the application) scrolling, giving a
very responsive user experience.

##### TightVNC[#](#tightvnc "Link to this heading")

TightVNC is widely-available and performs generally as well as RealVNC or
TigerVNC. If you wish to use TightVNC with Guacamole, performance should be
just fine, but we highly recommend disabling its JPEG encoding. This is because
images transmitted to Guacamole are always encoded losslessly as PNG images.
When this operation is performed on a JPEG image, the artifacts present from
JPEG’s lossy compression reduce the compressibility of the image for PNG, thus
leading to a slower experience overall than if JPEG was simply not used to
begin with.

##### x11vnc[#](#x11vnc "Link to this heading")

The main benefit of using x11vnc is that it allows you to continue using your
desktop normally, while simultaneously exposing control of your desktop via
VNC. Performance of x11vnc is comparable to RealVNC, TigerVNC, and TightVNC. If
you need to use your desktop locally as well as via VNC, you will likely be
quite happy with x11vnc.

##### vino[#](#vino "Link to this heading")

vino is the VNC server that comes with the Gnome desktop environment, and is
enabled if you enable “desktop sharing” via the system preferences available
within Gnome. If you need to share your local desktop, we recommend using
x11vnc rather vino, as it has proven more performant and feature-complete in
our testing. If you don’t need to share a local desktop but simply need an
environment you can access remotely, using a VNC server like RealVNC, TigerVNC,
or TightVNC is a better choice.

##### QEMU or KVM[#](#qemu-or-kvm "Link to this heading")

QEMU (and thus KVM) expose the displays of virtual machines using VNC. If you
need to see the virtual monitor of your virtual machine, using this VNC
connection is really your only choice. As the VNC server built into QEMU cannot
be aware of higher-level operations like window movement, resizing, or
scrolling, those operations will tend to be sent suboptimally, and will not be
as fast as a VNC server running within the virtual machine.

If you wish to use a virtual machine for desktop access, we recommend
installing a native VNC server inside the virtual machine after the virtual
machine is set up. This will give a more responsive desktop.

### RDP[#](#rdp "Link to this heading")

The RDP protocol is more complicated than VNC and was the second protocol
officially supported by Guacamole. RDP tends to be faster than VNC due to the
use of caching, which Guacamole does take advantage of.

RDP support for Guacamole is provided by the libguac-client-rdp library, which
will be installed as part of guacamole-server if the required dependencies are
present during the build.

Note

In addition to the RDP-specific parameters below, Guacamole’s RDP support also
accepts the parameters of several features that Guacamole provides for multiple
protocols:

* [Disabling clipboard access](#disable-clipboard)
* [File transfer via SFTP](#common-sftp)
* [Graphical session recording](#graphical-recording)
* [Wake-on-LAN](#wake-on-lan)

#### Network parameters[#](#rdp-network-parameters "Link to this heading")

RDP connections require a hostname or IP address defining the
destination machine. The RDP port is defined to be 3389, and will be
this value in most cases. You only need to specify the RDP port if you
are not using port 3389.

`hostname`
:   The hostname or IP address of the RDP server Guacamole should connect to.

`port`
:   The port the RDP server is listening on. This parameter is optional. If
    this is not specified, the standard port for RDP (3389) or Hyper-V’s
    default port for VMConnect (2179) will be used, depending on the security
    mode selected.

`timeout`
:   The timeout, in seconds, to wait for the RDP server to respond before
    giving up and aborting the connection. The default is 10 seconds.

#### Authentication and security[#](#authentication-and-security "Link to this heading")

RDP provides authentication through the use of a username, password, and
optional domain. All RDP connections are encrypted.

Most RDP servers will provide a graphical login if the username, password, and
domain parameters are omitted. One notable exception to this is Network Level
Authentication, or NLA, which performs all authentication outside of a desktop
session, and thus in the absence of a graphical interface.

Servers that require NLA can be handled by Guacamole in one of two ways. The
first is to provide the username and password within the connection
configuration, either via static values or by passing through the Guacamole
credentials with [parameter tokens](#parameter-tokens) and [LDAP authentication](ldap-auth.html).
Alternatively, if credentials are not configured within the connection
configuration, Guacamole will attempt to prompt the user for the credentials
interactively, if the versions of both guacd and Guacamole Client in use
support it. If either component does not support prompting and the credentials
are not configured, NLA-based connections will fail.

`username`
:   The username to use to authenticate, if any. This parameter is optional.

`password`
:   The password to use when attempting authentication, if any. This parameter
    is optional.

`domain`
:   The domain to use when attempting authentication, if any. This parameter
    is optional.

`security`
:   The security mode to use for the RDP connection. This mode dictates how
    data will be encrypted and what type of authentication will be performed,
    if any. By default, a security mode is selected based on a negotiation
    process which determines what both the client and the server support.

    Possible values are:

    any
    :   Automatically select the security mode based on the security protocols
        supported by both the client and the server. *This is the default*.

    nla
    :   Network Level Authentication, sometimes also referred to as “hybrid” or
        CredSSP (the protocol that drives NLA). This mode uses TLS encryption
        and requires the username and password to be given in advance. Unlike
        RDP mode, the authentication step is performed before the remote desktop
        session actually starts, avoiding the need for the Windows server to
        allocate significant resources for users that may not be authorized.

        If the versions of guacd and Guacamole Client in use support prompting
        and the username, password, and domain are not specified, the user will
        be interactively prompted to enter credentials to complete NLA and
        continue the connection. Otherwise, when prompting is not supported and
        credentials are not provided, NLA connections will fail.

    nla-ext
    :   Extended Network Level Authentication. This mode is identical to NLA
        except that an additional “[Early User Authorization
        Result](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/d0e560a3-25cb-4563-8bdc-6c4cc625bbfc)”
        is required to be sent from the server to the client immediately after the
        NLA handshake is completed.

    tls
    :   RDP authentication and encryption implemented via TLS (Transport Layer
        Security). Also referred to as RDSTLS, the TLS security mode is
        primarily used in load balanced configurations where the initial RDP
        server may redirect the connection to a different RDP server.

    vmconnect
    :   Automatically select the security mode based on the security protocols
        supported by both the client and the server, limiting that negotiation
        to only the protocols known to be supported by [Hyper-V /
        VMConnect](#rdp-preconnection-pdu).

    rdp
    :   Legacy RDP encryption. This mode is generally only used for older
        Windows servers or in cases where a standard Windows login screen is
        desired. Newer versions of Windows have this mode disabled by default
        and will only accept NLA unless explicitly configured otherwise.

`ignore-cert`
:   If set to “true”, the certificate returned by the server will be ignored,
    even if that certificate cannot be validated. This is useful if you
    universally trust the server and your connection to the server, and you
    know that the server’s certificate cannot be validated (for example, if it
    is self-signed).

`cert-tofu`
:   If set to “true”, this enables FreeRDP’s “Trust on First Use” (TOFU)
    policy for certificate management, where an unknown certificate will be
    trusted the first time and added to FreeRDP’s list of known hosts, and,
    on subsequent connections, the certificate will be checked to validate
    a match. This is similar to SSH client behavior.

`cert-fingerprints`
:   A comma-separated list of certificate fingerprint and hash combinations
    that will be checked against upon connection. If the fingerprint and hash
    of the remote server’s certificate matches one of those present in this
    option, the connection will be allowed. Otherwise, if this option is
    specified, and the fingerprint and hash do not match, the connection
    will be denied. The fingerprint and hash value is identical to the
    format used by the xfreerdp command line option “/cert:fingerprint”.

`disable-auth`
:   If set to “true”, authentication will be disabled. Note that this refers
    to authentication that takes place while connecting. Any authentication
    enforced by the server over the remote desktop session (such as a login
    dialog) will still take place. By default, authentication is enabled and
    only used when requested by the server.

    If you are using NLA, authentication must be enabled by definition.

#### Clipboard normalization[#](#clipboard-normalization "Link to this heading")

Windows uses a different sequence of characters at the end of each line
compared to other operating systems. As RDP preserves the format of line
endings within the clipboard, this can cause trouble when using a non-Windows
machine to access Windows or vice versa.

If clipboard normalization is used, Guacamole will automatically translate the
line endings within clipboard data to compensate for the expectations of the
remote system.

`normalize-clipboard`
:   The type of line ending normalization to apply to text within the clipboard,
    if any. By default, line ending normalization is not applied.

    Possible values are:

    preserve
    :   Preserve all line endings within the clipboard exactly as they are,
        performing no normalization whatsoever. This is the default.

    unix
    :   Automatically transform all line endings within the clipboard to Unix-style
        line endings (LF). This format of line ending is the format used by both
        Linux and Mac.

    windows
    :   Automatically transform all line endings within the clipboard to
        Windows-style line endings (CRLF).

#### Session settings[#](#session-settings "Link to this heading")

RDP sessions will typically involve the full desktop environment of a normal
user. Alternatively, you can manually specify a program to use instead of the
RDP server’s default shell, or connect to the administrative console.

Although Guacamole is independent of keyboard layout, RDP is not. This is
because Guacamole represents keys based on what they *do* (“press the Enter
key”), while RDP uses identifiers based on the key’s location (“press the
rightmost key in the second row”). To translate between a Guacamole key event
and an RDP key event, Guacamole must know ahead of time the keyboard layout of
the RDP server.

By default, the US English qwerty keyboard will be used. If this does not match
the keyboard layout of your RDP server, keys will not be properly translated,
and you will need to explicitly choose a different layout in your connection
settings. If your keyboard layout is not supported, please notify the Guacamole
team by [opening an issue in
JIRA](https://issues.apache.org/jira/browse/GUACAMOLE).

`client-name`
:   When connecting to the RDP server, Guacamole will normally provide its own
    hostname as the name of the client. If this parameter is specified,
    Guacamole will use its value instead.

    On Windows RDP servers, this value is exposed within the session as the
    `CLIENTNAME` environment variable.

`console`
:   If set to “true”, you will be connected to the console (admin) session of
    the RDP server.

`initial-program`
:   The full path to the program to run immediately upon connecting. This
    parameter is optional.

`server-layout`
:   The server-side keyboard layout. This is the layout of the RDP server and
    has nothing to do with the keyboard layout in use on the client. *The
    Guacamole client is independent of keyboard layout.* The RDP protocol,
    however, is *not* independent of keyboard layout, and Guacamole needs to
    know the keyboard layout of the server in order to send the proper keys
    when a user is typing.

    Possible values are generally in the format
    `LANGUAGE-REGION-VARIANT`, where `LANGUAGE` is the standard
    two-letter language code for the primary language associated with the
    layout, `REGION` is a standard representation of the location that the
    keyboard is used (the two-letter country code, when possible), and
    `VARIANT` is the specific keyboard layout variant (such as “qwerty”,
    “qwertz”, or “azerty”):

    | Keyboard layout | Parameter value |
    | --- | --- |
    | Brazilian (Portuguese) | `pt-br-qwerty` |
    | English (UK) | `en-gb-qwerty` |
    | English (US) | `en-us-qwerty` |
    | French | `fr-fr-azerty` |
    | French (Belgian) | `fr-be-azerty` |
    | French (Swiss) | `fr-ch-qwertz` |
    | German | `de-de-qwertz` |
    | German (Swiss) | `de-ch-qwertz` |
    | Hungarian | `hu-hu-qwertz` |
    | Italian | `it-it-qwerty` |
    | Japanese | `ja-jp-qwerty` |
    | Norwegian | `no-no-qwerty` |
    | Spanish | `es-es-qwerty` |
    | Spanish (Latin American) | `es-latam-qwerty` |
    | Swedish | `sv-se-qwerty` |
    | Turkish-Q | `tr-tr-qwerty` |

    If you server’s keyboard layout is not yet supported, and it is not possible
    to set your server to use a supported layout, the `failsafe` layout may be used
    to force Unicode events to be used for all input, however beware that doing so
    may prevent keyboard shortcuts from working as expected.

`timezone`
:   The timezone that the client should send to the server for configuring the
    local time display of that server. The format of the timezone is in the
    standard IANA key zone format, which is the format used in UNIX/Linux.
    This will be converted by RDP into the correct format for Windows.

    The timezone is detected and will be passed to the server during the
    handshake phase of the connection, and may used by protocols, like RDP,
    that support it. This parameter can be used to override the value detected
    and passed during the handshake, or can be used in situations where guacd
    does not support passing the timezone parameter during the handshake phase
    (guacd versions prior to 1.3.0).

    Support for forwarding the client timezone varies by RDP server
    implementation. For example, with Windows, support for forwarding
    timezones is only present in Windows Server with Remote Desktop Services
    (RDS, formerly known as Terminal Services) installed. Windows Server
    installations in admin mode, along with Windows workstation versions, do
    not allow the timezone to be forwarded. Other server implementations, for
    example, xrdp, may not implement this feature at all. Consult the
    documentation for the RDP server to determine whether or not this feature
    is supported.

#### Display settings[#](#rdp-display-settings "Link to this heading")

Guacamole will automatically choose an appropriate display size for RDP
connections based on the size of the browser window and the DPI of the device.
The size of the display can be forced by specifying explicit width or height
values.

To reduce bandwidth usage, you may also request that the server reduce its
color depth. Guacamole will automatically detect 256-color images, but this can
be guaranteed for absolutely all graphics sent over the connection by forcing
the color depth to 8-bit. Color depth is otherwise dictated by the RDP server.

`color-depth`
:   The color depth to request, in bits-per-pixel. This parameter is optional.
    If specified, this must be either 8, 16, or 24. Regardless of what value
    is chosen here, if a particular update uses less than 256 colors,
    Guacamole will always send that update as a 256-color PNG.

`width`
:   The width of the display to request, in pixels. This parameter is
    optional. If this value is not specified, the width of the connecting
    client display will be used instead.

`height`
:   The height of the display to request, in pixels. This parameter is
    optional. If this value is not specified, the height of the connecting
    client display will be used instead.

`dpi`
:   The desired effective resolution of the client display, in DPI. This
    parameter is optional. If this value is not specified, the resolution and
    size of the client display will be used together to determine,
    heuristically, an appropriate resolution for the RDP session.

`resize-method`
:   The method to use to update the RDP server when the width or height of the
    client display changes. This parameter is optional. If this value is not
    specified, no action will be taken when the client display changes size.

    Normally, the display size of an RDP session is constant and can only be
    changed when initially connecting. As of RDP 8.1, the “Display Update”
    channel can be used to request that the server change the display size.
    For older RDP servers, the only option is to disconnect and reconnect with
    the new size.

    Possible values are:

    display-update
    :   Uses the “Display Update” channel added with RDP 8.1 to signal the
        server when the client display size has changed.

    reconnect
    :   Automatically disconnects the RDP session when the client display size
        has changed, and reconnects with the new size.

`force-lossless`
:   Whether this connection should only use lossless compression for graphical
    updates. If set to “true”, lossy compression will not be used. This
    parameter is optional. By default, lossy compression will be used when
    heuristics determine that it would likely outperform lossless compression.

#### Device redirection[#](#device-redirection "Link to this heading")

Device redirection refers to the use of non-display devices over RDP.
Guacamole’s RDP support currently allows redirection of audio, printing, and
disk access, some of which require additional configuration in order to
function properly.

Audio redirection will be enabled by default. If Guacamole was correctly
installed, and audio redirection is supported by your RDP server, sound should
play within remote connections without manual intervention.

Printing requires GhostScript to be installed on the Guacamole server, and
allows users to print arbitrary documents directly to PDF. When documents are
printed to the redirected printer, the user will receive a PDF of that document
within their web browser.

Guacamole provides support for file transfer over RDP by emulating a virtual
disk drive. This drive will persist on the Guacamole server, confined within
the drive path specified. If drive redirection is enabled on a Guacamole RDP
connection, users will be able to upload and download files as described in
[Guacamole’s user interface](using-guacamole.html).

`disable-audio`
:   Audio is enabled by default in both the client and in libguac-client-rdp.
    If you are concerned about bandwidth usage, or sound is causing problems,
    you can explicitly disable sound by setting this parameter to “true”.

`enable-audio-input`
:   If set to “true”, audio input support (microphone) will be enabled,
    leveraging the standard “`AUDIO_INPUT`” channel of RDP. By default, audio
    input support within RDP is disabled.

`enable-touch`
:   If set to “true”, support for multi-touch events will be enabled, leveraging
    the standard “`RDPEI`” channel of RDP. By default, direct RDP support for
    multi-touch events is disabled.

    Enabling support for multi-touch allows touch interaction with applications
    inside the RDP session, however the touch gestures available will depend on
    the level of touch support of those applications and the OS.

    If multi-touch support is not enabled, pointer-type interaction with
    applications inside the RDP session will be limited to mouse or emulated
    mouse events.

`enable-printing`
:   Printing is disabled by default, but with printing enabled, RDP users can
    print to a virtual printer that sends a PDF containing the document
    printed to the Guacamole client. Enable printing by setting this parameter
    to “true”.

    *Printing support requires GhostScript to be installed.* If guacd cannot
    find the `gs` executable when printing, the print attempt will fail.

`printer-name`
:   The name of the redirected printer device that is passed through to the
    RDP session. This is the name that the user will see in, for example, the
    Devices and Printers control panel.

    If printer redirection is not enabled, this option has no effect.

`enable-drive`
:   File transfer is disabled by default, but with file transfer enabled, RDP
    users can transfer files to and from a virtual drive which persists on the
    Guacamole server. Enable file transfer support by setting this parameter
    to “true”.

    Files will be stored in the directory specified by the “`drive-path`”
    parameter, which is required if file transfer is enabled.

`disable-download`
:   If set to true downloads from the remote server to client (browser) will
    be disabled. This includes both downloads done via the hidden Guacamole
    menu, as well as using the special “Download” folder presented to the
    remote server. The default is false, which means that downloads will be
    allowed.

    If file transfer is not enabled, this parameter is ignored.

`disable-upload`
:   If set to true, uploads from the client (browser) to the remote server
    location will be disabled. The default is false, which means uploads will
    be allowed if file transfer is enabled.

    If file transfer is not enabled, this parameter is ignored.

`drive-name`
:   The name of the filesystem used when passed through to the RDP session.
    This is the name that users will see in their Computer/My Computer area
    along with client name (for example, “Guacamole on Guacamole RDP”), and is
    also the name of the share when accessing the special `\\tsclient` network
    location.

    If file transfer is not enabled, this parameter is ignored.

`drive-path`
:   The directory on the Guacamole server in which transferred files should be
    stored. This directory must be accessible by guacd and both readable and
    writable by the user that runs guacd. *This parameter does not refer to a
    directory on the RDP server.*

    If file transfer is not enabled, this parameter is ignored.

`create-drive-path`
:   If set to “true”, and file transfer is enabled, the directory specified by
    the `drive-path` parameter will automatically be created if it does not
    yet exist. Only the final directory in the path will be created - if other
    directories earlier in the path do not exist, automatic creation will
    fail, and an error will be logged.

    By default, the directory specified by the `drive-path` parameter will not
    automatically be created, and attempts to transfer files to a non-existent
    directory will be logged as errors.

    If file transfer is not enabled, this parameter is ignored.

`console-audio`
:   If set to “true”, audio will be explicitly enabled in the console (admin)
    session of the RDP server. Setting this option to “true” only makes sense
    if the `console` parameter is also set to “true”.

`static-channels`
:   A comma-separated list of static channel names to open and expose as
    pipes. If you wish to communicate between an application running on the
    remote desktop and JavaScript, this is the best way to do it. Guacamole
    will open an outbound pipe with the name of the static channel. If
    JavaScript needs to communicate back in the other direction, it should
    respond by opening another pipe with the same name.

    Guacamole allows any number of static channels to be opened, but protocol
    restrictions of RDP limit the size of each channel name to 7 characters.

#### Preconnection PDU (Hyper-V / VMConnect)[#](#preconnection-pdu-hyper-v-vmconnect "Link to this heading")

Some RDP servers host multiple logical RDP connections behind a single server
listening on a single TCP port. To select between these logical connections, an
RDP client must send the “preconnection PDU” - a message which contains values
that uniquely identify the destination, referred to as the “RDP source”. This
mechanism is defined by the [“Session Selection
Extension](https://msdn.microsoft.com/en-us/library/cc242359.aspx) for the RDP
protocol, and is implemented by Microsoft’s Hyper-V hypervisor.

If you are using Hyper-V, you will need to specify the ID of the destination
virtual machine within the `preconnection-blob` parameter. This value can be
determined using PowerShell:

```
PS C:\> Get-VM VirtualMachineName | Select-Object Id

Id
--
ed272546-87bd-4db9-acba-e36e1a9ca20a


PS C:\>
```

The preconnection PDU is intentionally generic. While its primary use is as a
means for selecting virtual machines behind Hyper-V, other RDP servers may use
it as well. It is up to the RDP server itself to determine whether the
preconnection ID, BLOB, or both will be used, and what their values mean.

*If you do intend to use Hyper-V, beware that its built-in RDP server requires
different parameters for authentication and Guacamole’s defaults will not
work.* In most cases, you will need to do the following when connecting to
Hyper-V:

1. Specify both “`username`” and “`password`” appropriately, and set
   “`security`” to “`vmconnect`”. Selecting the “`vmconnect`” security mode
   will configure Guacamole to automatically negotiate security modes known to
   be supported by Hyper-V, and will automatically select Hyper-V’s default RDP
   port (2179).
2. If necessary, set “`ignore-cert`” to “`true`”. Hyper-V may use a self-signed
   certificate.

`preconnection-id`
:   The numeric ID of the RDP source. This is a non-negative integer value
    dictating which of potentially several logical RDP connections should be
    used. This parameter is optional, and is only required if the RDP server
    is documented as requiring it. *If using Hyper-V, this should be left
    blank.*

`preconnection-blob`
:   An arbitrary string which identifies the RDP source - one of potentially
    several logical RDP connections hosted by the same RDP server. This
    parameter is optional, and is only required if the RDP server is
    documented as requiring it, such as Hyper-V. In all cases, the meaning of
    this parameter is opaque to the RDP protocol itself and is dictated by the
    RDP server. *For Hyper-V, this will be the ID of the destination virtual
    machine.*

#### Remote desktop gateway[#](#remote-desktop-gateway "Link to this heading")

Microsoft’s remote desktop server provides an additional gateway service which
allows external connections to be forwarded to internal RDP servers which are
otherwise not accessible. If you will be using Guacamole to connect through
such a gateway, you will need to provide additional parameters describing the
connection to that gateway, as well as any required credentials.

`gateway-hostname`
:   The hostname of the remote desktop gateway that should be used as an
    intermediary for the remote desktop connection. *If omitted, a gateway
    will not be used.*

`gateway-port`
:   The port of the remote desktop gateway that should be used as an
    intermediary for the remote desktop connection. By default, this will be
    “443”.

`gateway-username`
:   The username of the user authenticating with the remote desktop gateway,
    if a gateway is being used. This is not necessarily the same as the user
    actually using the remote desktop connection.

`gateway-password`
:   The password to provide when authenticating with the remote desktop
    gateway, if a gateway is being used.

`gateway-domain`
:   The domain of the user authenticating with the remote desktop gateway, if
    a gateway is being used. This is not necessarily the same domain as the
    user actually using the remote desktop connection.

#### Load balancing and RDP connection brokers[#](#load-balancing-and-rdp-connection-brokers "Link to this heading")

If your remote desktop servers are behind a load balancer, sometimes referred
to as a “connection broker” or “TS session broker”, that balancer may require
additional information during the connection process to determine how the
incoming connection should be routed. RDP does not dictate the format of this
information; it is specific to the balancer in use.

If you are using a load balancer and are unsure whether such information is
required, *you will need to check the documentation for your balancer*. If your
balancer provides `.rdp` files for convenience, look through the contents of
those files for a string field called “loadbalanceinfo”, as that field is where
the required information/cookie would be specified.

`load-balance-info`
:   The load balancing information or cookie which should be provided to the
    connection broker. *If no connection broker is being used, this should be
    left blank.*

#### Performance flags[#](#performance-flags "Link to this heading")

RDP provides several flags which control the availability of features that
decrease performance and increase bandwidth for the sake of aesthetics, such as
wallpaper, window theming, menu effects, and smooth fonts. These features are
all disabled by default within Guacamole such that bandwidth usage is
minimized, but you can manually re-enable them on a per-connection basis if
desired.

`enable-wallpaper`
:   If set to “true”, enables rendering of the desktop wallpaper. By default,
    wallpaper will be disabled, such that unnecessary bandwidth need not be
    spent redrawing the desktop.

`enable-theming`
:   If set to “true”, enables use of theming of windows and controls. By
    default, theming within RDP sessions is disabled.

`enable-font-smoothing`
:   If set to “true”, text will be rendered with smooth edges. Text over RDP
    is rendered with rough edges by default, as this reduces the number of
    colors used by text, and thus reduces the bandwidth required for the
    connection.

`enable-full-window-drag`
:   If set to “true”, the contents of windows will be displayed as windows are
    moved. By default, the RDP server will only draw the window border while
    windows are being dragged.

`enable-desktop-composition`
:   If set to “true”, graphical effects such as transparent windows and
    shadows will be allowed. By default, such effects, if available, are
    disabled.

`enable-menu-animations`
:   If set to “true”, menu open and close animations will be allowed. Menu
    animations are disabled by default.

`disable-bitmap-caching`
:   In certain situations, particularly with RDP server implementations with
    known bugs, it is necessary to disable RDP’s built-in bitmap caching
    functionality. This parameter allows that to be controlled in a Guacamole
    session. If set to “true” the RDP bitmap cache will not be used.

`disable-offscreen-caching`
:   RDP normally maintains caches of regions of the screen that are currently
    not visible in the client in order to accelerate retrieval of those
    regions when they come into view. This parameter, when set to “true,” will
    disable caching of those regions. This is usually only useful when dealing
    with known bugs in RDP server implementations and should remain enabled in
    most circumstances.

`disable-glyph-caching`
:   In addition to screen regions, RDP maintains caches of frequently used
    symbols or fonts, collectively known as “glyphs.” As with bitmap and
    offscreen caching, certain known bugs in RDP implementations can cause
    performance issues with this enabled, and setting this parameter to “true”
    will disable that glyph caching in the RDP session.

    **Glyph caching is currently universally disabled, regardless of the value of
    this parameter, as glyph caching support is not considered stable by FreeRDP
    as of the FreeRDP 2.0.0 release. See: [GUACAMOLE-1191](https://issues.apache.org/jira/browse/GUACAMOLE-1191).**

`disable-gfx`
:   Version 1.6.0 of Guacamole introduces RDP support for the Graphics Pipeline
    Extension, or GFX, which is a way to encode remote display data that
    significantly accelerates the display of that data on the client, resulting
    in applications that are much more responsive on RDP clients. The GFX
    extension is enabled by default, as most common RDP servers support it,
    and a few actually require it. If, for some reason, you’re connecting
    to a server that does not support it, or you find it causing problems,
    this connection parameter allows you to disable support for it, falling
    back to the more basic implementation for sending graphics over RDP.

#### RemoteApp[#](#remoteapp "Link to this heading")

Recent versions of Windows provide a feature called RemoteApp which allows
individual applications to be used over RDP, without providing access to the
full desktop environment. If your RDP server has this feature enabled and
configured, you can configure Guacamole connections to use those individual
applications.

`remote-app`
:   Specifies the RemoteApp to start on the remote desktop. If supported by
    your remote desktop server, this application, and only this application,
    will be visible to the user.

    Windows requires a special notation for the names of remote applications.
    The names of remote applications must be prefixed with two vertical bars.
    For example, if you have created a remote application on your server for
    `notepad.exe` and have assigned it the name “notepad”, you would set this
    parameter to: “`||notepad`”.

`remote-app-dir`
:   The working directory, if any, for the remote application. This parameter
    has no effect if RemoteApp is not in use.

`remote-app-args`
:   The command-line arguments, if any, for the remote application. This
    parameter has no effect if RemoteApp is not in use.

#### Adding an RDP connection[#](#adding-an-rdp-connection "Link to this heading")

If you are using the default authentication built into Guacamole, and you wish
to grant access to a RDP connection to a particular user, you need to locate
the `<authorize>` section for that user within your `user-mapping.xml`, and add
a section like the following within it:

```
<connection name="Unique Name">
    <protocol>rdp</protocol>
    <param name="hostname">localhost</param>
    <param name="port">3389</param>
</connection>
```

If added exactly as above, a new connection named “`Unique Name`” will be
available to the user associated with the `<authorize>` section containing it.
The connection will use RDP to connect to localhost at port 3389. Naturally,
you will want to change some or all of these values.

If you want to login automatically rather than receive a login prompt upon
connecting, you can specify a username and password with additional `<param>`
tags. Other options are available for controlling the color depth, size of the
screen, etc.

Other authentication methods will provide documentation describing how to
configure new connections. If the authentication method in use fully implements
the features of Guacamole’s authentication API, you will be able to add a new
RDP connection easily and intuitively using the administration interface built
into Guacamole. You will not need to edit configuration files.

### SSH[#](#ssh "Link to this heading")

Unlike VNC or RDP, SSH is a text protocol. Its implementation in Guacamole is
actually a combination of a terminal emulator and SSH client, because the SSH
protocol isn’t inherently graphical. Guacamole’s SSH support emulates a
terminal on the server side, and draws the screen of this terminal remotely on
the client.

SSH support for Guacamole is provided by the libguac-client-ssh library, which
will be installed as part of guacamole-server if the required dependencies are
present during the build.

Note

In addition to the SSH-specific parameters below, Guacamole’s SSH support also
accepts the parameters of several features that Guacamole provides for multiple
protocols:

* [Disabling clipboard access](#disable-clipboard)
* [Graphical session recording](#graphical-recording)
* [Text session recording (typescripts)](#typescripts)
* [Providing terminal input directly from JavaScript](#stdin-pipe)
* [Controlling terminal behavior](#terminal-behavior)
* [Terminal display settings](#terminal-display-settings)
* [Wake-on-LAN](#wake-on-lan)

#### SSH Host Verification[#](#ssh-host-verification "Link to this heading")

By default, Guacamole does not do any verification of host identity before
establishing SSH connections. While this may be safe for private and trusted
networks, it is not ideal for large networks with unknown/untrusted systems, or
for SSH connections that traverse the Internet. The potential exists for
Man-in-the-Middle (MitM) attacks when connecting to these hosts.

Guacamole includes two methods for verifying SSH (and SFTP) server identity
that can be used to make sure that the host you are connecting to is a host
that you know and trust. The first method is by reading a file in
`GUACAMOLE_HOME` called `ssh_known_hosts`. This file should be in the format of
a standard OpenSSH `known_hosts` file. If the file is not present, no
verification is done. If the file is present, it is read in at connection time
and remote host identities are verified against the keys present in the file.

The second method for verifying host identity is by passing a connection
parameter that contains an OpenSSH known hosts entry for that specific host.
The `host-key` parameter is used for SSH connections, while the SFTP
connections associated with RDP and VNC use the `sftp-host-key` parameter. If
these parameters are not present on their respective connections no host
identity verification is performed. If the parameter is present then the
identity of the remote host is verified against the identity provided in the
parameter before a connection is established.

#### Network parameters[#](#ssh-network-parameters "Link to this heading")

SSH connections require a hostname or IP address defining the destination
machine. SSH is standardized to use port 22 and this will be the proper value
in most cases. You only need to specify the SSH port if you are not using the
standard port.

`hostname`
:   The hostname or IP address of the SSH server Guacamole should connect to.

`port`
:   The port the SSH server is listening on, usually 22. This parameter is
    optional. If this is not specified, the default of 22 will be used.

`timeout`
:   The timeout, in seconds, to wait for the SSH server to respond before
    giving up and aborting the connection. The default is 10 seconds.

`host-key`
:   The known hosts entry for the SSH server. This parameter is optional, and,
    if not provided, no verification of host identity will be done. If the
    parameter is provided the identity of the server will be checked against
    the data.

    The format of this parameter is that of a single entry from an OpenSSH
    `known_hosts` file.

    For more information, please see [SSH Host Verification](#ssh-host-verification).

`server-alive-interval`
:   By default the SSH client does not send keepalive requests to the server.
    This parameter allows you to configure the the interval in seconds at
    which the client connection sends keepalive packets to the server. The
    default is 0, which disables sending the packets. The minimum value is 2.

#### Authentication[#](#ssh-authentication "Link to this heading")

SSH provides authentication through passwords and public key authentication,
and also supports the “NONE” method.

SSH “NONE” authentication is seen occasionally in appliances and items like
network or SAN fabric switches. Generally for this authentication method you
need only provide a username.

For Guacamole to use public key authentication, it must have access to your
private key and, if applicable, its passphrase. If the private key requires a
passphrase, but no passphrase is provided, you will be prompted for the
passphrase upon connecting.

If no private key is provided, Guacamole will attempt to authenticate using a
password, reading that password from the connection parameters, if provided, or
by prompting the user directly.

`username`
:   The username to use to authenticate, if any. This parameter is optional.
    If not specified, you will be prompted for the username upon connecting.

`password`
:   The password to use when attempting authentication, if any. This parameter
    is optional. If not specified, you will be prompted for your password upon
    connecting.

`private-key`
:   The entire contents of the private key to use for public key
    authentication. If this parameter is not specified, public key
    authentication will not be used. The private key must be in OpenSSH
    format, as would be generated by the OpenSSH **ssh-keygen**
    utility.

`passphrase`
:   The passphrase to use to decrypt the private key for use in public key
    authentication. This parameter is not needed if the private key does not
    require a passphrase. If the private key requires a passphrase, but this
    parameter is not provided, the user will be prompted for the passphrase
    upon connecting.

`public-key`
:   If SSH is using certificate-based authentication, this field allows
    you to provide the Base64-encoded public key rather than having it
    extracted from the provided private key. This parameter is optional
    and there is no default value. If a value is provided it will take
    precendence, requiring that the private key match the provided
    public key, and a mis-match will result in a failure to authenticate
    using the provided private key.

#### Running a command (instead of a shell)[#](#running-a-command-instead-of-a-shell "Link to this heading")

By default, SSH sessions will start an interactive shell. The shell which will
be used is determined by the SSH server, normally by reading the user’s default
shell previously set with `chsh` or within `/etc/passwd`. If you wish to
override this and instead run a specific command, you can do so by specifying
that command in the configuration of the Guacamole SSH connection.

`command`
:   The command to execute over the SSH session, if any. This parameter is
    optional. If not specified, the SSH session will use the user’s default
    shell.

#### Internationalization/Locale settings[#](#internationalization-locale-settings "Link to this heading")

The language of the session is normally set by the SSH server. If the SSH
server allows the relevant environment variable to be set, the language can be
overridden on a per-connection basis.

`locale`
:   The specific locale to request for the SSH session. This parameter is
    optional and may be any value accepted by the `LANG` environment variable
    of the SSH server. If not specified, the SSH server’s default locale will
    be used.

    As this parameter is sent to the SSH server using the `LANG` environment
    variable, the parameter will only have an effect if the SSH server allows
    the `LANG` environment variable to be set by SSH clients.

`timezone`
:   This parameter allows you to control the timezone that is sent to the
    server over the SSH connection, which will change the way local time is
    displayed on the server.

    The mechanism used to do this over SSH connections is by setting the `TZ`
    variable on the SSH connection to the timezone specified by this
    parameter. This means that the SSH server must allow the `TZ` variable to
    be set/overriden - many SSH server implementations have this disabled by
    default. To get this to work, you may need to modify the configuration of
    the SSH server and explicitly allow for `TZ` to be set/overriden.

    The available values of this parameter are standard IANA key zone format
    timezones, and the value will be sent directly to the server in this
    format.

#### SFTP[#](#sftp "Link to this heading")

Guacamole provides support for file transfer over SSH using SFTP, the
file transfer protocol built into most SSH servers. If SFTP is enabled
on a Guacamole SSH connection, users will be able to upload and download
files as described in [Guacamole’s user interface](using-guacamole.html)

`enable-sftp`
:   Whether file transfer should be enabled. If set to “true”, the user will
    be allowed to upload or download files from the SSH server using SFTP.
    Guacamole includes the **guacctl** utility which controls file
    downloads and uploads when run on the SSH server by the user over the SSH
    connection.

`sftp-root-directory`
:   The directory to expose to connected users via Guacamole’s [file
    browser](using-guacamole.html#file-browser). If omitted, the root directory will be used by
    default.

`sftp-disable-download`
:   If set to true downloads from the remote system to the client (browser)
    will be disabled. The default is false, which means that downloads will be
    enabled.

    If SFTP is not enabled, this parameter will be ignored.

`sftp-disable-upload`
:   If set to true uploads from the client (browser) to the remote system will
    be disabled. The default is false, which means that uploads will be
    enabled.

    If SFTP is not enabled, this parameter will be ignored.

#### Adding an SSH connection[#](#adding-an-ssh-connection "Link to this heading")

If you are using the default authentication built into Guacamole, and
you wish to grant access to a SSH connection to a particular user, you
need to locate the `<authorize>` section for that user within your
`user-mapping.xml`, and add a section like the following within it:

```
<connection name="Unique Name">
    <protocol>ssh</protocol>
    <param name="hostname">localhost</param>
    <param name="port">22</param>
</connection>
```

If added exactly as above, a new connection named “`Unique Name`” will be
available to the user associated with the `<authorize>` section containing it.
The connection will use SSH to connect to localhost at port 22. Naturally, you
will want to change some or all of these values.

If you want to login automatically rather than receive a login prompt upon
connecting, you can specify a username and password with additional `<param>`
tags. Other options are available for controlling the font.

Other authentication methods will provide documentation describing how to
configure new connections.

### Telnet[#](#telnet "Link to this heading")

Telnet is a text protocol and provides similar functionality to SSH. By nature,
it is not encrypted, and does not provide support for file transfer. As far as
graphics are concerned, Guacamole’s telnet support works in the same manner as
SSH: it emulates a terminal on the server side which renders to the Guacamole
client’s display.

Telnet support for Guacamole is provided by the libguac-client-telnet library,
which will be installed as part of guacamole-server if the required
dependencies are present during the build.

Note

In addition to the telnet-specific parameters below, Guacamole’s telnet support
also accepts the parameters of several features that Guacamole provides for
multiple protocols:

* [Disabling clipboard access](#disable-clipboard)
* [Graphical session recording](#graphical-recording)
* [Text session recording (typescripts)](#typescripts)
* [Providing terminal input directly from JavaScript](#stdin-pipe)
* [Controlling terminal behavior](#terminal-behavior)
* [Terminal display settings](#terminal-display-settings)
* [Wake-on-LAN](#wake-on-lan)

#### Network parameters[#](#telnet-network-parameters "Link to this heading")

Telnet connections require a hostname or IP address defining the
destination machine. Telnet is standardized to use port 23 and this will
be the proper value in most cases. You only need to specify the telnet
port if you are not using the standard port.

`hostname`
:   The hostname or IP address of the telnet server Guacamole should connect
    to.

`port`
:   The port the telnet server is listening on, usually 23. This parameter is
    optional. If this is not specified, the default of 23 will be used.

`timeout`
:   The timeout, in seconds, to wait for the telnet server to respond before
    giving up and aborting the connecion. The default is 10 seconds.

#### Authentication[#](#telnet-authentication "Link to this heading")

Telnet does not actually provide any standard means of authentication.
Authentication over telnet depends entirely on the login process running on the
server and is interactive. To cope with this, Guacamole provides non-standard
mechanisms for automatically passing the username and entering password.
Whether these mechanisms work depends on specific login process used by your
telnet server.

The de-facto method for passing the username automatically via telnet is to
submit it via the `USER` environment variable, sent using the NEW-ENVIRON
option. This is the mechanism used by most telnet clients, typically via the
`-l` command-line option.

Passwords cannot typically be sent automatically - at least not as reliably as
the username. There is no `PASSWORD` environment variable (this would actually
be a horrible idea) nor any similar mechanism for passing the password to the
telnet login process, and most telnet clients provide no built-in support for
automatically entering the password. The best that can be done is to
heuristically detect the password prompt, and type the password on behalf of
the user when the prompt appears. The prescribed method for doing this with a
traditional command-line telnet is to use a utility like `expect`. Guacamole
provides similar functionality by searching for the password prompt with a
regular expression.

If Guacamole receives a line of text which matches the regular expression, the
password is automatically sent. If no such line is ever received, the password
is not sent, and the user must type the password manually. Pressing any key
during this process cancels the heuristic password prompt detection.

If the password prompt is not being detected properly, you can try using your
own regular expression by specifying it within the `password-regex` parameter.
The regular expression must be written in the POSIX ERE dialect (the dialect
typically used by `egrep`).

`username`
:   The username to use to authenticate, if any. This parameter is optional.
    If not specified, or not supported by the telnet server, the login process
    on the telnet server will prompt you for your credentials. For this to
    work, your telnet server must support the NEW-ENVIRON option, and the
    telnet login process must pay attention to the `USER` environment
    variable. Most telnet servers satisfy this criteria.

`password`
:   The password to use when attempting authentication, if any. This parameter
    is optional. If specified, your password will be typed on your behalf when
    the password prompt is detected.

`username-regex`
:   The regular expression to use when waiting for the username prompt. This
    parameter is optional. If not specified, a reasonable default built into
    Guacamole will be used. The regular expression must be written in the
    POSIX ERE dialect (the dialect typically used by `egrep`).

`password-regex`
:   The regular expression to use when waiting for the password prompt. This
    parameter is optional. If not specified, a reasonable default built into
    Guacamole will be used. The regular expression must be written in the
    POSIX ERE dialect (the dialect typically used by `egrep`).

`login-success-regex`
:   The regular expression to use when detecting that the login attempt has
    succeeded. This parameter is optional. If specified, the terminal display
    will not be shown to the user until text matching this regular expression
    has been received from the telnet server. The regular expression must be
    written in the POSIX ERE dialect (the dialect typically used by `egrep`).

`login-failure-regex`
:   The regular expression to use when detecting that the login attempt has
    failed. This parameter is optional. If specified, the connection will be
    closed with an explicit login failure error if text matching this regular
    expression has been received from the telnet server. The regular
    expression must be written in the POSIX ERE dialect (the dialect typically
    used by `egrep`).

#### Adding a telnet connection[#](#adding-a-telnet-connection "Link to this heading")

If you are using the default authentication built into Guacamole, and you wish
to grant access to a telnet connection to a particular user, you need to locate
the `<authorize>` section for that user within your `user-mapping.xml`, and add
a section like the following within it:

```
<connection name="Unique Name">
    <protocol>telnet</protocol>
    <param name="hostname">localhost</param>
    <param name="port">23</param>
</connection>
```

If added exactly as above, a new connection named “`Unique Name`” will be
available to the user associated with the `<authorize>` section containing it.
The connection will use telnet to connect to localhost at port 23. Naturally,
you will want to change some or all of these values.

As telnet is inherently insecure compared to SSH, you should use SSH instead
wherever possible. If Guacamole is set up to use HTTPS then communication with
the Guacamole *client* will be encrypted, but communication between guacd and
the telnet server will still be unencrypted. You should not use telnet unless
the network between guacd and the telnet server is trusted.

### Kubernetes[#](#kubernetes "Link to this heading")

Kubernetes provides an API for attaching to the console of a container over the
network. As with SSH and telnet, Guacamole’s Kubernetes support emulates a
terminal on the server side which renders to the Guacamole client’s display.

Kubernetes support for Guacamole is provided by the libguac-client-kubernetes
library, which will be installed as part of guacamole-server if the required
dependencies are present during the build.

Note

In addition to the Kubernetes-specific parameters below, Guacamole’s Kubernetes
support also accepts the parameters of several features that Guacamole provides
for multiple protocols:

* [Disabling clipboard access](#disable-clipboard)
* [Graphical session recording](#graphical-recording)
* [Text session recording (typescripts)](#typescripts)
* [Providing terminal input directly from JavaScript](#stdin-pipe)
* [Controlling terminal behavior](#terminal-behavior)
* [Terminal display settings](#terminal-display-settings)
* [Wake-on-LAN](#wake-on-lan)

#### Network/Container parameters[#](#network-container-parameters "Link to this heading")

Attaching to a Kubernetes container requires the hostname or IP address of the
Kubernetes server and the name of the pod containing the container in question.
By default, Guacamole will attach to the first container in the pod. If there
are multiple containers in the pod, you may wish to also specify the container
name.

`hostname`
:   The hostname or IP address of the Kubernetes server
    that Guacamole should connect to.

`port`
:   The port the Kubernetes server is listening on for
    API connections. *This parameter is optional.* If
    omitted, port 8080 will be used by default.

`namespace`
:   The name of the Kubernetes namespace of the pod containing the container
    being attached to. *This parameter is optional.* If omitted, the namespace
    “default” will be used.

`pod`
:   The name of the Kubernetes pod containing with the container being
    attached to.

`container`
:   The name of the container to attach to. *This parameter is optional.* If
    omitted, the first container in the pod will be used.

`exec-command`
:   The command to run within the container, with input and output attached to
    this command’s process. *This parameter is optional.* If omitted, no
    command will be run, and input/output will instead be attached to the main
    process of the container.

    When this parameter is specified, the behavior of the connection is
    analogous to running **kubectl exec**. When omitted, the behavior
    is analogous to running **kubectl attach**.

#### Authentication and SSL/TLS[#](#authentication-and-ssl-tls "Link to this heading")

If enabled, Kubernetes uses SSL/TLS for both encryption and authentication.
Standard SSL/TLS client authentication requires both a client certificate and
client key, which Guacamole will use to identify itself to the Kubernetes
server. If the certificate used by Kubernetes is self-signed or signed by a
non-standard certificate authority, the certificate for the certificate
authority will also be needed.

`use-ssl`
:   If set to “true”, SSL/TLS will be used to connect to the Kubernetes
    server. *This parameter is optional.* By default, SSL/TLS will not be
    used.

`client-cert`
:   The certificate to use if performing SSL/TLS client authentication to
    authenticate with the Kubernetes server, in PEM format. *This parameter is
    optional.* If omitted, SSL client authentication will not be performed.

`client-key`
:   The key to use if performing SSL/TLS client authentication to authenticate
    with the Kubernetes server, in PEM format. *This parameter is optional.*
    If omitted, SSL client authentication will not be performed.

`ca-cert`
:   The certificate of the certificate authority that signed the certificate
    of the Kubernetes server, in PEM format. *This parameter is optional.* If
    omitted, verification of the Kubernetes server certificate will use only
    system-wide certificate authorities.

`ignore-cert`
:   If set to “true”, the validity of the SSL/TLS certificate used by the
    Kubernetes server will be ignored if it cannot be validated. *This
    parameter is optional.* By default, SSL/TLS certificates are validated.

#### Adding a Kubernetes connection[#](#adding-a-kubernetes-connection "Link to this heading")

If you are using the default authentication built into Guacamole, and you wish
to grant access to a Kubernetes connection to a particular user, you need to
locate the `<authorize>` section for that user within your `user-mapping.xml`,
and add a section like the following within it:

```
<connection name="Unique Name">
    <protocol>kubernetes</protocol>
    <param name="hostname">localhost</param>
    <param name="pod">mypod</param>
</connection>
```

If added exactly as above, a new connection named “`Unique Name`” will be
available to the user associated with the `<authorize>` section containing it.
The connection will connect to the Kubernetes server running on localhost and
attach to the first container of the pod “mypod”.

### Common configuration options[#](#common-configuration-options "Link to this heading")

#### Disabling clipboard access[#](#disabling-clipboard-access "Link to this heading")

Guacamole provides bidirectional access to the clipboard by default for all
supported protocols. For protocols that don’t inherently provide a clipboard,
Guacamole implements its own clipboard. This behavior can be overridden on a
per-connection basis with the `disable-copy` and `disable-paste` parameters.

`disable-copy`
:   If set to “true”, text copied within the remote desktop session will not
    be accessible by the user at the browser side of the Guacamole session,
    and will be usable only within the remote desktop. This parameter is
    optional. By default, the user will be given access to the copied text.

`disable-paste`
:   If set to “true”, text copied at the browser side of the Guacamole session
    will not be accessible within the remote ddesktop session. This parameter
    is optional. By default, the user will be able to paste data from outside
    the browser within the remote desktop session.

#### File transfer via SFTP[#](#file-transfer-via-sftp "Link to this heading")

Guacamole can provide file transfer over SFTP even when the remote desktop is
otherwise being accessed through a different protocol, like VNC or RDP. If SFTP
is enabled on a Guacamole RDP connection, users will be able to upload and
download files as described in [Guacamole’s user interface](using-guacamole.html).

This support is independent of the file transfer that may be provided by the
protocol in use, like RDP’s own “drive redirection” (RDPDR), and is
particularly useful for remote desktop servers which do not support file
transfer features.

`enable-sftp`
:   Whether file transfer should be enabled. If set to “true”, the user will
    be allowed to upload or download files from the specified server using
    SFTP. If omitted, SFTP will be disabled.

`sftp-hostname`
:   The hostname or IP address of the server hosting SFTP. This parameter is
    optional. If omitted, the hostname of the remote desktop server associated
    with the connection will be used.

`sftp-port`
:   The port the SSH server providing SFTP is listening on, usually 22. This
    parameter is optional. If omitted, the standard port of 22 will be used.

`sftp-timeout`
:   The timeout, in seconds, to wait for the SFTP server to respond before
    giving up and aborting the connection. The default is 10 seconds.

`sftp-host-key`
:   The known hosts entry for the SFTP server. This parameter is optional,
    and, if not provided, no verification of SFTP host identity will be done.
    If the parameter is provided the identity of the server will be checked
    against the data.

    The format of this parameter is that of a single entry from an OpenSSH
    `known_hosts` file.

    For more information, please see [SSH Host Verification](#ssh-host-verification).

`sftp-username`
:   The username to authenticate as when connecting to the specified SSH
    server for SFTP. This parameter is optional if a username is specified for
    the remote desktop connection. If omitted, the username specified for the
    remote desktop connection will be used.

`sftp-password`
:   The password to use when authenticating with the specified SSH server for
    SFTP.

`sftp-private-key`
:   The entire contents of the private key to use for public key
    authentication. If this parameter is not specified, public key
    authentication will not be used. The private key must be in OpenSSH
    format, as would be generated by the OpenSSH **ssh-keygen**
    utility.

`sftp-passphrase`
:   The passphrase to use to decrypt the private key for use in public key
    authentication. This parameter is not needed if the private key does not
    require a passphrase.

`sftp-public-key`
:   If the SFTP connection is using key-based authentication, this field
    allows you to specify the Base64-encoded public key rather than having
    it extracted from the provided private key. This parameter is optional
    and there is no default value. If a value is provided it will take
    precendence, requiring that the private key match the provided
    public key, and a mis-match will result in a failure to authenticate
    using the provided private key.

`sftp-directory`
:   The directory to upload files to if they are simply dragged and dropped,
    and thus otherwise lack a specific upload location. This parameter is
    optional. If omitted, the default upload location of the SSH server
    providing SFTP will be used.

`sftp-root-directory`
:   The directory to expose to connected users via Guacamole’s
    [Using the file browser](using-guacamole.html#file-browser). If omitted, the root directory will be used by default.

`sftp-server-alive-interval`
:   The interval in seconds at which to send keepalive packets to the SSH
    server for the SFTP connection. This parameter is optional. If omitted,
    the default of 0 will be used, disabling sending keepalive packets. The
    minimum value is 2.

`sftp-disable-download`
:   If set to true downloads from the remote system to the client (browser)
    will be disabled. The default is false, which means that downloads will be
    enabled.

    If sftp is not enabled, this parameter will be ignored.

`sftp-disable-upload`
:   If set to true uploads from the client (browser) to the remote system will
    be disabled. The default is false, which means that uploads will be
    enabled.

    If sftp is not enabled, this parameter will be ignored.

#### Graphical session recording[#](#graphical-session-recording "Link to this heading")

Sessions of all supported protocols can be recorded graphically. These
recordings take the form of Guacamole protocol dumps and are recorded
automatically to a specified directory. Recordings can be subsequently
[played back directly in the browser from the connection history screen](recording-playback.html)
or translated to a normal video stream using the **guacenc** utility
provided with guacamole-server.

For example, to produce a video called `NAME.m4v` from the recording
“`NAME`”, you would run:

```
$ guacenc /path/to/recording/NAME
```

The **guacenc** utility has additional options for overriding default
behavior, including tweaking the output format, which are documented in detail
within the manpage:

```
$ man guacenc
```

If recording of key events is explicitly enabled using the
`recording-include-keys` parameter, recordings can also be translated into
human-readable interpretations of the keys pressed during the session using the
**guaclog** utility. The usage of **guaclog** is analogous to
**guacenc**, and results in the creation of a new text file containing
the interpreted events:

```
$ guaclog /path/to/recording/NAME
guaclog: INFO: Guacamole input log interpreter (guaclog) version 1.6.0
guaclog: INFO: 1 input file(s) provided.
guaclog: INFO: Writing input events from "/path/to/recording/NAME" to "/path/to/recording/NAME.txt" ...
guaclog: INFO: All files interpreted successfully.
$
```

Important

By default, Guacamole will not overwrite an existing recording, unless you have
enabled it to do so by use of the `recording-write-existing` connection
paramter. When the `recording-write-existing` connection parameter is not enabled,
a numeric suffix like “.1”, “.2”, “.3”, etc. will be appended to  to avoid
overwriting an existing recording. If even appending a numeric suffix does not
help, the session will simply not be recorded.

If the `recording-write-existing` parameter is enabled, then Guacamole will
overwrite the existing recording.

`recording-path`
:   The directory in which screen recording files should be created. *If a
    graphical recording needs to be created, then this parameter is required.*
    Specifying this parameter enables graphical screen recording. If this
    parameter is omitted, no graphical recording will be created.

`create-recording-path`
:   If set to “true”, the directory specified by the `recording-path`
    parameter will automatically be created if it does not yet exist. Only the
    final directory in the path will be created - if other directories earlier
    in the path do not exist, automatic creation will fail, and an error will
    be logged.

    *This parameter is optional.* By default, the directory specified by the
    `recording-path` parameter will not automatically be created, and attempts
    to create recordings within a non-existent directory will be logged as
    errors.

    This parameter only has an effect if graphical recording is enabled. If
    the `recording-path` is not specified, graphical session recording will be
    disabled, and this parameter will be ignored.

`recording-name`
:   The filename to use for any created recordings. *This parameter is
    optional.* If omitted, the value “recording” will be used instead.

    This parameter only has an effect if graphical recording is enabled. If
    the `recording-path` is not specified, graphical session recording will be
    disabled, and this parameter will be ignored.

`recording-exclude-output`
:   If set to “true”, graphical output and other data normally streamed from
    server to client will be excluded from the recording, producing a
    recording which contains only user input events. *This parameter is
    optional.* If omitted, graphical output will be included in the recording.

    This parameter only has an effect if graphical recording is enabled. If
    the `recording-path` is not specified, graphical session recording will be
    disabled, and this parameter will be ignored.

`recording-exclude-mouse`
:   If set to “true”, user mouse events will be excluded from the recording,
    producing a recording which lacks a visible mouse cursor. *This parameter
    is optional.* If omitted, mouse events will be included in the recording.

    This parameter only has an effect if graphical recording is enabled. If
    the `recording-path` is not specified, graphical session recording will be
    disabled, and this parameter will be ignored.

`recording-include-keys`
:   If set to “true”, user key events will be included in the recording. The
    recording can subsequently be passed through the **guaclog** utility
    to produce a human-readable interpretation of the keys pressed during the
    session. *This parameter is optional.* If omitted, key events will be not
    included in the recording.

    This parameter only has an effect if graphical recording is enabled. If
    the `recording-path` is not specified, graphical session recording will be
    disabled, and this parameter will be ignored.

`recording-write-exiting`
:   If set to “true”, instead of insisting on creation of a new file, and
    appending numbers until a non-existing file is found, Guacamole will
    simply write to the existing recording file, overwriting data that
    may already be present. While overwriting recordings is not generally
    desirable, this parameter is useful in situations where you want to
    try to write to a named pipe, FIFO buffer, or other special device
    that may be sending the recording data elsewhere.

    This parameter only has an effect if graphical recording is enabled. If
    the `recording-path` is not specified, graphical session recording will
    be disabled, and this parameter will be ignored.

#### Text session recording (typescripts)[#](#text-session-recording-typescripts "Link to this heading")

The full, raw text content of SSH sessions, including timing information, can
be recorded automatically to a specified directory. This recording, also known
as a “typescript”, will be written to two files within the directory specified
by `typescript-path`: `NAME`, which contains the raw text data, and
`NAME.timing`, which contains timing information, where `NAME` is the
value provided for the `typescript-name` parameter.

This format is compatible with the format used by the standard UNIX
**script** command, and can be replayed using **scriptreplay**
(if installed). For example, to replay a typescript called “`NAME`”, you would
run:

```
$ scriptreplay NAME.timing NAME
```

Important

By default, Guacamole will not overwrite an existing typescript recordings;
instead, it will append a numeric suffix like “.1”, “.2”, “.3”, etc., to
`NAME` to avoid overwriting an existing recording. If even appending a
numeric suffix does not help, the session will simply not be recorded.

However, if the `typescript-write-existing` parameter is enabled, then
Guacamole will be allowed to use the existing recording file, potentially
ovewriting any data in that file.

`typescript-path`
:   The directory in which typescript files should be created. *If a
    typescript needs to be recorded, this parameter is required.* Specifying
    this parameter enables typescript recording. If this parameter is omitted,
    no typescript will be recorded.

`create-typescript-path`
:   If set to “true”, the directory specified by the `typescript-path`
    parameter will automatically be created if it does not yet exist. Only the
    final directory in the path will be created - if other directories earlier
    in the path do not exist, automatic creation will fail, and an error will
    be logged.

    *This parameter is optional.* By default, the directory specified by the
    `typescript-path` parameter will not automatically be created, and
    attempts to record typescripts in a non-existent directory will be logged
    as errors.

    This parameter only has an effect if typescript recording is enabled. If
    the `typescript-path` is not specified, recording of typescripts will be
    disabled, and this parameter will be ignored.

`typescript-name`
:   The base filename to use when determining the names for the data and
    timing files of the typescript. *This parameter is optional.* If omitted,
    the value “typescript” will be used instead.

    Each typescript consists of two files which are created within the
    directory specified by `typescript-path`: `NAME`, which contains
    the raw text data, and `NAME.timing`, which contains timing
    information, where `NAME` is the value provided for the `typescript-name`
    parameter.

    This parameter only has an effect if typescript recording is enabled. If
    the `typescript-path` is not specified, recording of typescripts will be
    disabled, and this parameter will be ignored.

`typescript-write-existing`
:   If this parameter is set to “true”, instead of attempting to generate
    unique file names by appending incremental numbers to the typescript name,
    Guacamole will be allowed to write to an existing typescript file,
    potentially ovewriting any data in that file. While this is not
    desirable in most cases, it may be necessary in situations where the
    typescript recording is being sent to a named pipe, FIFO buffer, or
    other special device that is processing the data and sending it
    elsewhere.

    This parameter only has an effect if typescript recording is enabled. If
    the `typescript-path` is not specified, recording of typescripts will be
    disabled, and this parameter will be ignored.

#### Controlling terminal behavior[#](#controlling-terminal-behavior "Link to this heading")

In most cases, the default behavior for a terminal works without modification.
However, when connecting to certain systems, particularly operating systems
other than Linux, the terminal behavior may need to be tweaked to allow it to
operate properly. The settings in this section control that behavior.

`backspace`
:   This parameter controls the ASCII code that the backspace key sends to the
    remote system. Under most circumstances this should not need to be
    adjusted; however, if, when pressing the backspace key, you see control
    characters (often either ^? or ^H) instead of seeing the text erased, you
    may need to adjust this parameter. By default the terminal sends ASCII
    code 127 (Delete) if this option is not set.

`terminal-type`
:   This parameter sets the terminal emulator type string that is passed to
    the server. This parameter is optional. If not specified, “`linux`” is used
    as the terminal emulator type by default.

##### Providing terminal input directly from JavaScript[#](#providing-terminal-input-directly-from-javascript "Link to this heading")

If Guacamole is being used in part to automate an SSH, telnet, or other
terminal session, it can be useful to provide input directly from JavaScript as
a raw stream of data, rather than attempting to translate data into keystrokes.
This can be done through opening a pipe stream named “STDIN” within the
connection using the [`createPipeStream()`](http://guacamole.apache.org/doc/guacamole-common-js/Guacamole.Client.html#createPipeStream)
function of [`Guacamole.Client`](http://guacamole.apache.org/doc/guacamole-common-js/Guacamole.Client.html):

```
var outputStream = client.createPipeStream('text/plain', 'STDIN');
```

The resulting [`Guacamole.OutputStream`](http://guacamole.apache.org/doc/guacamole-common-js/Guacamole.OutputStream.html)
can then be used to stream data directly to the input of the terminal session,
as if typed by the user:

```
// Wrap output stream in writer
var writer = new Guacamole.StringWriter(outputStream);

// Send text
writer.sendText("hello");

// Send more text
writer.sendText("world");

// Close writer and stream
writer.sendEnd();
```

#### Terminal display settings[#](#terminal-display-settings "Link to this heading")

Guacamole’s terminal emulator (used by SSH, telnet, and Kubernetes support)
provides options for configuring the font used and its size. In this case, *the
chosen font must be installed on the server*, as it is the server that will
handle rendering of characters to the terminal display, not the client.

`color-scheme`
:   The color scheme to use for the terminal session. It consists of a
    semicolon-separated series of name-value pairs. Each name-value pair is
    separated by a colon and assigns a value to a color in the terminal
    emulator palette. For example, to use blue text on white background by
    default, and change the red color to a purple shade, you would specify:

    ```
    foreground: rgb:00/00/ff;
    background: rgb:ff/ff/ff;
    color9: rgb:80/00/80
    ```

    This format is similar to the color configuration format used by Xterm, so
    Xterm color configurations can be easily adapted for Guacamole. This
    parameter is optional. If not specified, Guacamole will render text as
    gray over a black background.

    Possible color names are:

    `foreground`
    :   Set the default foreground color.

    `background`
    :   Set the default background color.

    `colorN`
    :   Set the color at index `N` on the Xterm 256-color palette. For example,
        `color9` refers to the red color.

    Possible color values are:

    `rgb:RR/GG/BB`
    :   Use the specified color in RGB format, with each component in
        hexadecimal. For example, `rgb:ff/00/00` specifies the color red. Note
        that each hexadecimal component can be one to four digits, but the
        effective values are always zero-extended or truncated to two digits;
        for example, `rgb:f/8/0`, `rgb:f0/80/00`, and `rgb:f0f/808/00f` all
        refer to the same effective color.

    `colorN`
    :   Use the color currently assigned to index `N` on the Xterm 256-color
        palette. For example, `color9` specifies the current red color. Note
        that the color value is used rather than the color reference, so if
        `color9` is changed later in the color scheme configuration, that new
        color will not be reflected in this assignment.

    For backward compatibility, Guacamole will also accept four special values as
    the color scheme parameter:

    `black-white`
    :   Black text over a white background.

    `gray-black`
    :   Gray text over a black background. This is the default color scheme.

    `green-black`
    :   Green text over a black background.

    `white-black`
    :   White text over a black background.

`font-name`
:   The name of the font to use. This parameter is optional. If not specified,
    the default of “monospace” will be used instead.

`font-size`
:   The size of the font to use, in points. This parameter is optional. If not
    specified, the default of 12 will be used instead.

`scrollback`
:   The maximum number of rows to allow within the terminal scrollback buffer.
    This parameter is optional. If not specified, the scrollback buffer will
    be limited to a maximum of 1000 rows.

#### Wake-on-LAN[#](#wake-on-lan "Link to this heading")

Guacamole implements the support to send a “magic wake-on-lan packet” to a
remote host prior to attempting to establish a connection with the host. The
below parameters control the behavior of this functionality, which is disabled
by default.

When this functionality is enabled, Guacamole will attempt to connect to the
specified hostname or IP and the TCP port number used in the connection prior
to sending the WoL packet. If the connection succeeds, the host is determined
to be up, and the WoL packet will not be sent. After the initial WoL packet
is sent, Guacamole will wait the amount of time specified by `wol-wait-time`,
retry the connection to the host, and then send another WoL packet. This
loop will be repeated up to five times to attempt to wake the host, or
the connection will fail.

Important

There are several factors that can impact the ability of Wake-on-LAN (WoL) to
function correctly, many of which are outside the scope of Guacamole
configuration. If you are configuring WoL within Guacamole you should also be
familiar with the other components that need to be configured in order for it
to function correctly.

`wol-send-packet`
:   If set to “true”, Guacamole will attempt to send the Wake-On-LAN packet
    prior to establishing a connection. This parameter is optional. By
    default, Guacamole will not send the WoL packet. Enabling this option
    requires that the `wol-mac-addr` parameter also be configured, otherwise
    the WoL packet will not be sent.

`wol-mac-addr`
:   This parameter configures the MAC address that Guacamole will use in the
    magic WoL packet to attempt to wake the remote system. If
    `wol-send-packet` is enabled, this parameter is required or else the WoL
    packet will not be sent.

`wol-broadcast-addr`
:   This parameter configures the IPv4 broadcast address or IPv6 multicast
    address that Guacamole will send the WoL packet to in order to wake the
    host. This parameter is optional. If no value is provided, the default
    local IPv4 broadcast address (255.255.255.255) will be used.

`wol-udp-port`
:   This parameter configures the UDP port that will be set in the WoL packet.
    In most cases the UDP port isn’t processed by the system that will be
    woken up; however, there are certain cases where it is useful for the port
    to be set, as in situations where a router is listening for the packet and
    can make routing decisions depending upon the port that is used. If not
    configured the default UDP port 9 will be used.

`wol-wait-time`
:   By default after the WoL packet is sent Guacamole will attempt immediately
    to connect to the remote host. It may be desirable in certain scenarios to
    have Guacamole wait before the initial connection in order to give the
    remote system time to boot. Setting this parameter to a positive value
    will cause Guacamole to wait the specified number of seconds before
    attempting the initial connection. This parameter is optional.

### Parameter tokens[#](#parameter-tokens "Link to this heading")

The values of connection parameters can contain “tokens” which will be replaced
by Guacamole when used. These tokens allow the values of connection parameters
to vary dynamically by the user using the connection, and provide a simple
means of forwarding authentication information without storing that information
in the connection configuration itself, so long as the remote desktop
connection uses the same credentials as Guacamole.

Each token is of the form `${TOKEN_NAME}` or
`${TOKEN_NAME:MODIFIER}`, where `TOKEN_NAME` is some descriptive
name for the value the token represents, and the optional `MODIFIER` is one of
the modifiers documented below to dynamically modify the token. Tokens with no
corresponding value will never be replaced, but should you need such text
within your connection parameters, and wish to guarantee that this text will
not be replaced with a token value, you can escape the token by adding an
additional leading “$”, as in “`$${TOKEN_NAME}`”.

`${GUAC_USERNAME}`
:   The username of the current Guacamole user. When a user accesses a
    connection, this token will be dynamically replaced with the username they
    provided when logging in to Guacamole.

`${GUAC_PASSWORD}`
:   The password of the current Guacamole user. When a user accesses a
    connection, this token will be dynamically replaced with the password they
    used when logging in to Guacamole.

`${GUAC_CLIENT_ADDRESS}`
:   The IPv4 or IPv6 address of the current Guacamole user. This will be the
    address of the client side of the HTTP connection to the Guacamole server
    at the time the current user logged in.

`${GUAC_CLIENT_HOSTNAME}`
:   The hostname of the current Guacamole user. This will be the hostname of
    the client side of the HTTP connection to the Guacamole server at the time
    the current user logged in. If no such hostname can be determined, the
    IPv4 or IPv6 address will be used instead, and this token will be
    equivalent to `${GUAC_CLIENT_ADDRESS}`.

`${GUAC_DATE}`
:   The current date in the local time zone of the Guacamole server. This will
    be written in “YYYYMMDD” format, where “YYYY” is the year, “MM” is the
    month number, and “DD” is the day of the month, all zero-padded. When a
    user accesses a connection, this token will be dynamically replaced with
    the date that the connection began.

`${GUAC_TIME}`
:   The current time in the local time zone of the Guacamole server. This will
    be written in “HHMMSS” format, where “HH” is hours in 24-hour time, “MM”
    is minutes, and “SS” is seconds, all zero-padded. When a user accesses a
    connection, this token will be dynamically replaced with the time that the
    connection began.

Note that these tokens are replaced dynamically each time a connection is used.
If two different users access the same connection at the same time, both users
will be connected independently of each other using different sets of
connection parameters.

#### Token modifiers[#](#token-modifiers "Link to this heading")

At times it can be useful to use the value provided by a token, but with slight
modifications. These modifers are optionally specified at the end of the token,
separated from the token name by a colon (`:`), in the format
`${TOKEN_NAME:MODIFIER}`. The following modifiers are
currently supported:

`LOWER`
:   Convert the entire value of the token to lower-case. This can be useful in
    situations where users log in to Guacamole with a mixed-case username, but
    a remote system requires the username be lower-case.

`UPPER`
:   Convert the entire value of the token to upper-case.

#### Extension-specific tokens[#](#extension-specific-tokens "Link to this heading")

Each extension can also implement its own arbitrary tokens that can
dynamically fill in values provided by the extension. Within these
extensions, attribute names are canonicalized into a standard format
that consists of all capital letters separated by underscores.

##### CAS Extension Tokens[#](#cas-extension-tokens "Link to this heading")

The CAS extension will read attributes provided by the CAS server when a user
is authenticated and will make those attributes available as tokens. The CAS
server must be specifically configured to release certain attributes to the
client (Guacamole), and configuration of that is outside the scope of this
document. Any attribute that the CAS server is configured to release should be
available to Guacamole as a token for use within a connection. The token name
will be prepended with the `CAS_` prefix. A CAS server configured to release
attributes `firstname`, `lastname`, `email`, and `mobile` would produce the
following tokens:

* `${CAS_FIRSTNAME}`
* `${CAS_LASTNAME}`
* `${CAS_EMAIL}`
* `${CAS_MOBILE}`

##### JDBC Extension Tokens[#](#jdbc-extension-tokens "Link to this heading")

The JDBC extension provides tokens based on various details of the connection
that is in use. These tokens are based on data that should be present
for any connection in the system:

* `${JDBC_CONNECTION_ID}` - The identifier of the connection as stored in the
  database.
* `${JDBC_CONNECTION_NAME}` - The name of the connection as displayed in the
  Guacamole interface.
* `${JDBC_HOSTNAME}` - The hostname or IP address of the connection.
* `${JDBC_PROTOCOL}` - The protocol of the connection.
* `${JDBC_STARTDATE}` - The date at which the connection is established. The
  value of this field should match exactly the date that is subsequently stored
  in the connection history table.
* `${JDBC_STARTTIME}` - The time at which the connection is established. As
  with the date field, this field should match exactly the time that is
  subsequently stored in the connection history table.

##### LDAP Extension Tokens[#](#ldap-extension-tokens "Link to this heading")

The LDAP extension will read user attributes provided by the LDAP server and
specified in the `guacamole.properties` file. The attributes retrieved for a
user are configured using the `ldap-user-attributes` parameter. The user must
be able to read the attribute values from their own LDAP object. The token name
will be prepended with the `LDAP_` prefix. As an example, configuring the
following line in `guacamole.properties`:

```
ldap-user-attributes: cn, givenName, sn, mobile, mail
```

will produce the below tokens that can be used in connection parameters:

* `${LDAP_CN}`
* `${LDAP_GIVENNAME}`
* `${LDAP_SN}`
* `${LDAP_MOBILE}`
* `${LDAP_MAIL}`

##### OIDC Extension Tokens[#](#oidc-extension-tokens "Link to this heading")

The OIDC extension could extract claims provided by the IdP server when a user
is authenticated and will make those claims available as tokens. The IdP
server must be specifically configured to release certain claims to the
client (Guacamole), and configuration of that is outside the scope of this
document. The claims retrieved for a user are configured using the
`openid-attributes-claim-type` parameter. The token name will be prepended
with the `OIDC_` prefix. Multi-valued claims will not be unrolled.
As an example, configuring the following line in `guacamole.properties`:

```
openid-attributes-claim-type: firstname, lastname, email, mobile
```

will produce the below tokens that can be used in connection parameters:

* `${OIDC_FIRSTNAME}`
* `${OIDC_LASTNAME}`
* `${OIDC_EMAIL}`
* `${OIDC_MOBILE}`

### Parameter prompting[#](#parameter-prompting "Link to this heading")

In certain situations Guacamole may determine that additional information is
required in order to successfully open or continue a connection. In these
scenarios guacd will send an instruction back to the client to retrieve that
information, which will result in the user being prompted for those additional
parameters.

Currently the only parameters that will trigger this prompt to the user are
authentication requests for the RDP and VNC protocols where authenticators were
not provided as part of the connection configuration.

Important

It is important to note that requests for parameters will only be generated in
the case where that information has not already been provided as part of the
connection. **The user will never be asked for parameters that replace or
override connection parameters where values have been provided**, including
authentication information.

For example, if the configuration of a connection to a RDP server specifies a
username and password, and that username or password is incorrect and results
in an authentication failure, Guacamole will not prompt the user for additional
credentials. For RDP servers where NLA is enforced, this will result in a
connection failure. Other RDP servers may behave differently and give the user
the ability to try other credentials, but this is outside the control of
Guacamole - **Guacamole will not override pre-configured authentication values
with input from the user**.

## Configuring guacd[#](#configuring-guacd "Link to this heading")

### `guacd.conf`[#](#id12 "Link to this heading")

guacd is configured with a configuration file called `guacd.conf`, by
default located in `/etc/guacamole`. This file follows a simple,
INI-like format:

```
#
# guacd configuration file
#

[daemon]

pid_file = /var/run/guacd.pid
log_level = info

[server]

bind_host = localhost
bind_port = 4822

#
# The following parameters are valid only if
# guacd was built with SSL support.
#

[ssl]

server_certificate = /etc/ssl/certs/guacd.crt
server_key = /etc/ssl/private/guacd.key
```

Configuration options are given as parameter/value pairs, where the name of the
parameter is specified on the left side of an “`=`”, and the value is specified
on the right. Each parameter must occur within a proper section, indicated by a
section name within brackets. The names of these sections are important; it is
the pairing of a section name with a parameter that constitutes the
fully-qualified parameter being set.

For the sake of documentation and readability, comments can be added anywhere
within guacd.conf using “`#`” symbols. All text following a “`#`” until
end-of-line will be ignored.

If you need to include special characters within the value of a parameter, such
as whitespace or any of the above symbols, you can do so by placing the
parameter within double quotes:

```
[ssl]

# Whitespace is legal within double quotes ...
server_certificate = "/etc/ssl/my certs/guacd.crt"

# ... as are other special symbols
server_key = "/etc/ssl/#private/guacd.key"
```

Note that even within double quotes, some characters still have special
meaning, such as the double quote itself or newline characters. If you need to
include these, they must be “escaped” with a backslash:

```
# Parameter value containing a double quote
parameter = "some\"value"

# Parameter value containing newline characters
parameter2 = "line1\
line2\
line3"

# Parameter value containing backslashes
parameter3 = "c:\\windows\\path\\to\\file.txt"
```

Don’t worry too much about the more complex formatting examples - they are only
rarely necessary, and guacd will complain with parsing errors if the
configuration file is somehow invalid. To ensure parameter values are entered
correctly, just follow the following guidelines:

1. If the value contains no special characters, just include it as-is.
2. If the value contains any special characters (whitespace, newlines, `#`,
   `\`, or `"`), enclose the entire value within double quotes.
3. If the value is enclosed within double quotes, escape newlines, `\`, and `"`
   with a backslash.

#### `[daemon]` section[#](#daemon-section "Link to this heading")

`pid_file`
:   The name of the file in which the PID of the main guacd process should be
    written. This is mainly needed for startup scripts, which need to monitor
    the state of guacd, killing it if necessary. If this parameter is
    specified, the user running guacd must have sufficient permissions to
    create or modify the specified file, or startup will fail.

`log_level`
:   The maximum level at which guacd will log messages to syslog and, if
    running in the foreground, the console. If omitted, the default level of
    `info` will be used.

    Legal values are `trace`, `debug`, `info`, `warning`, and `error`.

#### `[server]` section[#](#server-section "Link to this heading")

`bind_host`
:   The host that guacd should bind to when listening for connections. If
    unspecified, guacd will bind to localhost, and only connections from
    within the server hosting guacd will succeed.

`bind_port`
:   The port that guacd should bind to when listening for connections. If
    unspecified, port 4822 will be used.

#### `[ssl]` section[#](#ssl-section "Link to this heading")

`server_certificate`
:   The filename of the certificate to use for SSL encryption of the Guacamole
    protocol. If this option is specified, SSL encryption will be enabled, and
    the Guacamole web application will need to be configured within
    `guacamole.properties` to use SSL as well.

`server_key`
:   The filename of the private key to use for SSL encryption of the Guacamole
    protocol. If this option is specified, SSL encryption will be enabled, and
    the Guacamole web application will need to be configured within
    `guacamole.properties` to use SSL as well.

### Command-line options[#](#command-line-options "Link to this heading")

You can also affect the configuration of guacd with command-line
options. If given, these options take precendence over the system-wide
configuration file:

`-b HOST`
:   Changes the host or address that guacd listens on.

    This corresponds to the `bind_host` parameter within the [`[server]` section
    of `guacd.conf`](#guacd-conf-server).

`-l PORT`
:   Changes the port that guacd listens on (the default is port 4822).

    This corresponds to the `bind_port` parameter within the [`[server]` section
    of `guacd.conf`](#guacd-conf-server).

`-p PIDFILE`
:   Causes guacd to write the PID of the daemon process to the specified file.
    This is useful for init scripts and is used by the provided init script.

    This corresponds to the `pid_file` parameter within the [`[daemon]` section
    of `guacd.conf`](#guacd-conf-daemon).

`-L LEVEL`
:   Sets the maximum level at which guacd will log messages to syslog and, if
    running in the foreground, the console. Legal values are `trace`, `debug`,
    `info`, `warning`, and `error`. The default value is `info`.

    This corresponds to the `log_level` parameter within the [`[daemon]` section
    of `guacd.conf`](#guacd-conf-daemon).

`-f`
:   Causes guacd to run in the foreground, rather than automatically forking
    into the background.

If guacd was built with support for SSL, data sent via the Guacamole protocol
can be encrypted with SSL if an SSL certificate and private key are given with
the following options:

`-C CERTIFICATE`
:   The filename of the certificate to use for SSL encryption of the Guacamole
    protocol. If this option is specified, SSL encryption will be enabled, and
    the Guacamole web application will need to be configured within
    `guacamole.properties` to use SSL as well.

    This corresponds to the `server_certificate` parameter within the [`[ssl]`
    section of `guacd.conf`](#guacd-conf-ssl).

`-K KEY`
:   The filename of the private key to use for SSL encryption of the Guacamole
    protocol. If this option is specified, SSL encryption will be enabled, and
    the Guacamole web application will need to be configured within
    `guacamole.properties` to use SSL as well.

    This corresponds to the `server_key` parameter within the [`[ssl]` section of
    `guacd.conf`](#guacd-conf-ssl).

Contents

---
# Guacamole’s user interface

## Contents

# Guacamole’s user interface[#](#guacamoles-user-interface "Link to this heading")

Guacamole provides access to much of the functionality of a desktop from within
your web browser. Although most people use remote desktop tools only when
absolutely necessary, we believe that Guacamole must be aimed at becoming a
primary means of accessing desktops, and the interface is thus intended to be
as seamless and unobtrusive as possible.

## Home screen[#](#home-screen "Link to this heading")

Once you have successfully logged in, you will be taken to either the Guacamole
home screen, where all available connections are listed, or directly to a
connection, if you only have access to one connection.

The home screen will contain a list of all connections to which you have
access, along with thumbnails of any recently used or active connections. If
you have access to a large number of connections and wish to quickly locate a
specific connection, you can also enter search terms within the “Filter” field
to filter the list of connections by name.

![The Guacamole home screen. The user menu and several recently-usedconnections are visible, along with one active connection.](assets/doc_gug__images_guacamole-home-screen.png)

Clicking on any connection will open that connection within the current window
or tab, but multiple connections can be used simultaneously. You can easily
navigate back to the home screen without disconnecting by using your browsers
back button or the “Home” button in the Guacamole menu. Each connection you use
will remain active until explicitly disconnected, or until you navigate away
from Guacamole entirely. Active connections can be seen as thumbnails updating
in real-time on the home screen.

### User menu[#](#user-menu "Link to this heading")

With the exception of the client screen discussed below, all Guacamole screens
contain a menu in the upper-right corner called the “user menu”. This menu
displays your username and contains several options which depend on your user’s
level of access:

Home
:   Navigates back to the home screen, if you are not already there. If you only
    have access to one connection, this will be replaced with a link to that
    connection.

Settings
:   Navigates to the settings interface, which provides access to user
    preferences such as display language. If you have access to administrative
    functions, those are found within the settings interface, as well, and are
    discussed in more detail in [Guacamole’s administrative interface](administration.html).

Logout
:   Logs out of Guacamole completely, closing all current connections and ending
    the Guacamole session.

## Client screen[#](#client-screen "Link to this heading")

Once you open a connection, you will see a real-time view of the remote
display. You can interact with this display just as you would your normal
desktop. Your mouse and keyboard will function as if they were connected
directly to the remote machine.

![Guacamole client interface, with the Guacamole menuopen.](assets/doc_gug__images_guacamole-client-interface.png)

The remote display will take up the entire browser window, with no buttons or
menus to disturb the view. With the intent of providing a seamless experience,
options specific to remote desktop are hidden within the Guacamole menu, which
can be opened as needed.

### The Guacamole menu[#](#the-guacamole-menu "Link to this heading")

The Guacamole menu is a sidebar which is hidden until explicitly shown. On a
desktop or other device which has a hardware keyboard, you can show this menu
by pressing `Ctrl`+`Alt`+`Shift`. If you are using a mobile or touchscreen
device that lacks a keyboard, you can also show the menu by swiping right from
the left edge of the screen. To hide the menu, you press `Ctrl`+`Alt`+`Shift`
again or swipe left across the screen.

The Guacamole menu provides options for:

* [Reading from (and writing to) the clipboard of the remote
  desktop](#using-the-clipboard)
* [Switching between active connections and displaying multiple connections at
  once](#client-connection-menu)
* [Navigating back to the home screen](#client-user-menu)
* [Disconnecting from the current connection entirely](#client-user-menu)
* [Sharing the current connection](#client-share-menu)
* [Uploading and downloading files](#file-transfer)
* [Zooming in and out of the remote display](#scaling-display)
* [Selecting alternative methods of typing or controlling the mouse,
  particularly for use on mobile or touchscreen devices](#touch-devices)

## Copying/pasting text[#](#copying-pasting-text "Link to this heading")

At the top of the Guacamole menu is a text area labeled “clipboard”
along with some basic instructions:

> Text copied/cut within Guacamole will appear here. Changes to the text below
> will affect the remote clipboard.

If the clipboard API is enabled, the contents of the local clipboard will
automatically be synchronized to Guacamole, and ultimately to the clipboards
of the remote systems (assuming the functionality has not been disabled. The
text area, here, functions as a manual interface to the clipboard, allowing
text to be manually manipulated - text that you type, or paste into the text
area will be available to the remote clipboard, and text that is placed on
the remote clipboard it can be seen in this text area.

For privacy and security reasons, the contents of the clipboard are initially
hidden when the Guacamole menu is opened. Instead, a banner with further
instructions is displayed:

> Click to view clipboard contents.

Upon clicking the text area, the contents of the clipboard will be shown and
may be edited or replaced. The clipboard will remain visible until the
Guacamole menu is closed.

## Switching and tiling connections[#](#switching-and-tiling-connections "Link to this heading")

If you have access to more than one connection, clicking the current connection
name at the top of the Guacamole menu will open a drop-down menu containing a
list of your other available connections:

![Connection menu with one connection selected](assets/doc_gug__images_client-connection-menu.png)

Clicking on the name of another connection in this drop-down menu will
immediately switch to that connection. The previous connection will remain
running as a thumbnail within a panel attached to the lower-right corner of the
screen. This panel updates in real-time and remains visible as long as you have
multiple active connections, even if you navigate away to another part of the
Guacamole application:

![Active connection panel](assets/doc_gug__images_client-panel.png)

Clicking on any connection within the panel will navigate back to that
connection, while clicking the “X” icon in the upper-right corner of the
connection thumbnail will immediately close the connection.

### Adding a connection to the current view[#](#adding-a-connection-to-the-current-view "Link to this heading")

Multiple connections may also be opened simultaneously within the same view by
clicking the checkboxes next to the names of those connections in the
connection menu:

![Connection menu with two connections selected](assets/doc_gug__images_client-connection-menu-multiple.png)

All connections opened in this way are automatically arranged in equally-sized
tiles to fill the available area:

![Multiple client displays in a tiled arrangement](assets/doc_gug__images_client-tiled.png)

With multiple connections displayed as tiles, keyboard interaction and the
Guacamole menu will only affect the currently focused connection, as indicated
by the blue title and border. Clicking or tapping within another connection
will change the focus and allow keyboard interaction with *that* connection.

### Typing with multiple connections[#](#typing-with-multiple-connections "Link to this heading")

By holding down `Ctrl` (to select an individual connection) or
`Shift` (to select a rectangle of connections), multiple connection may be
focused at the same time. While multiple connections are focused, each key
pressed will be broadcast across each focused connection:

![Multiple focused client displays in a tiled arrangement](assets/doc_gug__images_client-tiled-multi-focus.png)

This is particularly useful for running the same series of commands on multiple
computers. Further, since Guacamole automatically translates between the user’s
local keyboard layout and the keyboard layout of the remote server, *this will
work as expected even if the keyboard layouts of focused connections do not
match*.

## Disconnecting and navigation[#](#disconnecting-and-navigation "Link to this heading")

When you are done using the current connection, or you wish to navigate
elsewhere temporarily, options to do so are within the user menu inside the
Guacamole menu:

![The user menu within the Guacamole menu.](assets/doc_gug__images_guac-menu-disconnect.png)

The user menu within the Guacamole menu provides an additional “Disconnect”
option that allows you to explicitly close the current connection only.
Clicking “Logout” will also implicitly disconnect all active connections,
including the current connection.

Navigating back to the home screen or to the settings screen will not
disconnect you: your connection will continue running in the background while
you change settings or initiate another connection, and you can resume any
active connection by clicking on it within the home screen.

## Sharing the connection[#](#sharing-the-connection "Link to this heading")

If the Guacamole server is configured to allow connection sharing, and you have
been granted permission to share the current connection, an additional “Share”
menu will appear next to your username in the Guacamole menu. Clicking on this
menu opens a list of options for sharing the current connection.

![](assets/doc_gug__images_guac-menu-share.png)

Clicking any of the options within the “Share” menu will immediately generate a
unique share link which can be distributed to anyone, even to users which do
not otherwise have accounts within the same Guacamole system.

![](assets/doc_gug__images_guac-menu-share-link.png)

When the link is visited, that user will be given temporary access to your
connection, restricted according to the sharing option chosen. This access, and
the validity of the link overall, lasts only until you disconnect. Once the
connection is closed, the link ceases to be valid, and any users sharing the
connection with you will be disconnected.

## Transferring files[#](#transferring-files "Link to this heading")

You can transfer files back and forth between your local computer and the
remote desktop if it is supported by the underlying protocol and enabled on the
connection. Currently, Guacamole supports file transfer for VNC, RDP, and SSH,
using either the native file transfer support of the protocol or SFTP.

Files can be transferred to the remote computer by dragging and dropping the
files into your browser window, or through using the file browser located in
the Guacamole menu.

### Using the file browser[#](#using-the-file-browser "Link to this heading")

If file transfer is enabled on the connection, you will see one or more
filesystem devices listed within the Guacamole menu. Clicking on one of the
filesystems opens a file browser which lists the files and directories within
that filesystem.

![The file browser within the Guacamole menu.](assets/doc_gug__images_file-browser.png)

Double-clicking on any directory will change the current location of the file
browser to that directory, updating the list of files shown as well as the
“breadcrumbs” at the top of the file browser. Clicking on any of the directory
names listed in the breadcrumbs will bring you back to that directory, and
clicking on the drive icon on the far left will bring you all the way back to
the root level.

Downloads are initiated by double-clicking on any file shown, while uploads are
initiated by clicking the “Upload Files” button. Clicking “Upload Files” will
open a file browsing dialog where you can choose one or more files from your
local computer, ultimately uploading the selected files to the directory
currently displayed within the file browser.

The state of all file uploads can be observed within the notification dialog
that appears once an upload begins, and can be cleared once completed by
clicking the “Clear” button. Downloads are tracked through your browser’s own
download notification system.

![In-progress and completed file transfers.](assets/doc_gug__images_file-transfers.png)

When you are done browsing the filesystem and transferring files, click “Back”
to return to the Guacamole menu.

### The RDP virtual drive[#](#the-rdp-virtual-drive "Link to this heading")

RDP provides its own native support for file transfer called “drive
redirection” or “RDPDR”. Guacamole provides support for this mechanism by
emulating a virtual drive. Typically, this virtual drive will appear as a
network drive within the RDP session. Files uploaded and downloaded will be
preserved within this drive, even after disconnecting.

![The Guacamole drive within a Windows RDP session.](assets/doc_gug__images_guacamole-drive.png)

Files can be downloaded from this drive using the file browser in the Guacamole
menu or using the special “Download” folder within the virtual drive. All files
dropped into this folder will automatically begin uploading to the client, and
thus downloading through the browser.

![The Guacamole drive's "Download" folder.](assets/doc_gug__images_guacamole-drive-download.png)

### **guacctl** / **guacget**[#](#guacctl-guacget "Link to this heading")

In addition to traditional drag-and-drop and the file browser, Guacamole’s SSH
support can be used with the **guacctl** utility. The **guacctl**
utility is a simple shell script [included with Guacamole](https://raw.githubusercontent.com/apache/guacamole-server/master/bin/guacctl) which
allows you to use and configure file transfer directly from the command line
within the SSH session:

```
$ guacctl
guacctl 0.8.0, Guacamole SSH session control utility.
Usage: guacctl [OPTION] [FILE]...

    -d, --download         download each of the files listed.
    -s, --set-directory    set the destination directory for future uploaded 
                           files.
$ guacctl -d FILENAME
$ guacctl -s DIRECTORY
$
```

For convenience, you may also create a symbolic link or alias to
**guacctl** called **guacget**. When run as **guacget**,
the utility behaves as if the `--download` option were supplied and initiates a
download for each file specified on the command line.

## On-screen keyboard[#](#on-screen-keyboard "Link to this heading")

Certain key combinations are impossible to press within a web application like
Guacamole because they are reserved by the operating system
(`Ctrl`+`Alt`+`Del` or `Alt`+`Tab`, for example) or by the web browser. If
you press one of these reserved combinations, the effect will be observed
locally, not remotely, and the remote desktop will receive only some of the
keys.

Guacamole provides its own, built-in on-screen keyboard which allows keys to be
sent to the remote desktop without affecting the local system. If the device
you’re using does not have certain keys which the remote desktop depends on,
such as the arrow keys or `Ctrl`, you can use the on-screen keyboard for
this, too. You can show the on-screen keyboard by selecting the “On-screen
keyboard” option from the menu.

Clicking (or tapping) the buttons of the on-screen keyboard has the same effect
as pressing the same buttons on a real keyboard, except that the operating
system and browser will not intercept these keypresses; they will only be sent
to the remote desktop.

## Scaling the display[#](#scaling-the-display "Link to this heading")

Guacamole will default to shrinking or expanding the remote display to fit the
browser window exactly, but this is not necessarily ideal. If the remote
display is much larger than your local display, the screen may be impossible to
see or interact with. This is especially true for mobile phones, whose screens
need to be small enough to fit in the average hand.

You can scale the display on touch devices by using the familiar pinch gesture.
Place two fingers on the screen and bring them closer together to zoom out or
further apart to zoom in.

If your device lacks a touch screen, you can also control the zoom level
through the menu. The controls for zooming in and out are located at the bottom
of the menu. The current zoom level is displayed between two “-” and “+”
buttons which control the zoom level in 10% increments.

## Mobile or touch devices[#](#mobile-or-touch-devices "Link to this heading")

Guacamole is designed to work equally well across all HTML5 browsers, including
those of mobile devices. It will automatically handle input from a touch screen
or a traditional mouse (or both, if you happen to have such a gifted computer),
and provides alternative input methods for devices which lack a physical
keyboard.

### Mouse emulation[#](#mouse-emulation "Link to this heading")

In the case that your device has a touchscreen and lacks a mouse, Guacamole
will emulate a mouse for the sake of interacting with remote desktops that
expect mouse input. By default, Guacamole uses “absolute” mouse emulation. This
means that the mouse pointer is positioned at the location of each tap on the
screen.

In both absolute and relative modes, you can click-and-drag by tapping the
screen and then quickly placing your finger back down. This gesture only causes
the mouse button to press down, but does not release it again until you lift
your finger back up.

#### Absolute mode (touchscreen)[#](#absolute-mode-touchscreen "Link to this heading")

Absolute mouse emulation is the default as it tends to be what people expect
when using a touch device to interact with applications designed for mouse
input.

Each tap on the screen is translated into a left-click at that position.
Right-clicking is accomplished through pressing and holding your finger on the
screen. If parts of the remote display are off-screen, you can drag your finger
around the screen to pan the off-screen parts back into view.

Although absolute mouse emulation works generally well, a finger makes for a
very inaccurate pointing device. To address this, Guacamole also provides
“relative” mouse emulation. Relative mouse emulation provides a way to deal
with the need for accurate pointer control, when a true pointer device is not
present.

![](assets/doc_gug__images_touchscreen.png)

#### Relative mode (touchpad)[#](#relative-mode-touchpad "Link to this heading")

Guacamole’s relative mouse emulation behaves similarly to the touchpad present
on most modern laptops. You drag your finger across the display to move the
mouse pointer, and tap the display to left-click. The pointer moves relative to
the motion of your finger. Right-clicking is accomplished with a two-finger
tap, and middle-clicking with a three-finger tap. The mouse scroll wheel can be
operated by dragging two fingers up or down.

Because the relative mouse emulation reserves so many gestures for the
different mouse buttons and actions, common touch gestures like panning and
pinch-to-zoom will not work while relative mouse emulation is enabled. Instead,
the screen will automatically pan to keep the mouse pointer in view, and you
can zoom through the buttons in the menu.

![](assets/doc_gug__images_touchpad.png)

### Typing without a physical keyboard[#](#typing-without-a-physical-keyboard "Link to this heading")

Many mobile devices lack a physical keyboard entirely, and instead provide
their own on-screen keyboards. As these are not true keyboards per se and do
not produce key presses, Guacamole’s text input mode is required for typing on
these platforms.

“Text input” allows input of keystrokes based on the input of text. Choosing
“Text input” tells Guacamole to infer keystrokes by tracking text entered,
rather than relying on actual key presses. Guacamole will instead determine the
combination of keypresses necessary to produce the same pattern of input,
including deletions.

If you wish to type via an IME (input method editor), such as those required
for Chinese, Japanese, or Korean, text input mode is required for this as well.
Such IMEs function through the explicit insertion of text and do not send
traditional key presses. Using text input mode within Guacamole thus allows you
to use a locally-installed IME, without requiring the IME to be installed on
the remote desktop.

## Changing preferences[#](#changing-preferences "Link to this heading")

User preferences can be changed within the settings screen. These preferences
are stored locally within the browser, so if you use multiple computers to
access Guacamole, you can have different settings for each location. The
settings screen allows users to change the language of the Guacamole interface,
to change the default input method used by Guacamole connections, and to change
the default mouse emulation mode for if a touch device is used. If you have
sufficient permissions, you may also change your password, or administer the
system.

![Guacamole preferences screen.](assets/doc_gug__images_guacamole-preferences.png)

### Display language[#](#display-language "Link to this heading")

The Guacamole interface is currently available in English, Dutch, French,
German, Italian, and Russian. By default, Guacamole will attempt to determine
the appropriate display language by checking the language preferences of the
browser in use. If this fails, or the browser is using a language not yet
available within Guacamole, English will be used as a fallback.

If you wish to override the current display language, you can do so by
selecting a different language within the “Display language” field. The change
will take effect immediately.

### Changing your password[#](#changing-your-password "Link to this heading")

System administrators can restrict the ability of individual users to change
their own passwords, so this section may not always be available. If your
account *does* have permission, the preferences screen will contain a “Change
Password” section.

To change your password, you must provide your current password, enter the
desired new password, and click “Update Password”. You will remain logged in,
and the change will affect any future login attempt.

### Default input settings[#](#default-input-settings "Link to this heading")

Guacamole provides multiple keyboard input methods and multiple mouse emulation
modes. Many of these settings are specifically useful for touch devices, while
others are aimed mainly at traditional desktop use. By default, Guacamole will
use the keyboard and mouse modes most commonly preferred by users, but you can
change these defaults if they do not fit your tastes or your current device.

The choices available mirror those within the Guacamole menu discussed earlier
in this chapter, and changing these settings will affect the default values
selected within the Guacamole menu of future connections.

### Recent connection settings[#](#recent-connection-settings "Link to this heading")

The user interface can be configured with regard to whether recent connections
are displayed and how many are tracked. The default setting is to track the most
recent 6 connections, but you can use the checkbox to disable the recent
connections area altogether, or you can adjust the number of recent
connections kept in history from the default of 6.

Contents

---
# Using a reverse proxy for SSL termination

## Contents

# Using a reverse proxy for SSL termination[#](#using-a-reverse-proxy-for-ssl-termination "Link to this heading")

Like most web applications, Guacamole can be placed behind a reverse proxy. For
production deployments of Guacamole, this is *highly recommended*. It provides
flexibility and, if your proxy is properly configured for SSL, encryption.

Proxying isolates privileged operations within native applications that can
safely drop those privileges when no longer needed, using Java only for
unprivileged tasks. On Linux and UNIX systems, a process must be running with
root privileges to listen on any port under 1024, including the standard HTTP
and HTTPS ports (80 and 443 respectively). If the servlet container instead
listens on a higher port, such as the default port 8080, it can run as a
reduced-privilege user, allowing the reverse proxy to bear the burden of root
privileges. As a native application, the reverse proxy can make system calls to
safely drop root privileges once the port is open; a Java application like
Tomcat cannot do this.

## Preparing your servlet container[#](#preparing-your-servlet-container "Link to this heading")

Your servlet container is most likely already configured to listen for HTTP
connections on port 8080 as this is the default. If this is the case, and you
can already access Guacamole over port 8080 from a web browser, you need not
make any further changes to its configuration.

If you *have* changed this, perhaps with the intent of proxying Guacamole over
AJP, *change it back*. Using Guacamole over AJP is unsupported as it is known
to cause problems, namely:

1. WebSocket will not work over AJP, forcing Guacamole to fallback to HTTP,
   possibly resulting in reduced performance.
2. Apache 2.4.3 and older does not support the HTTP PATCH method over AJP,
   preventing the Guacamole management interface from functioning properly.

The connector entry within `conf/server.xml` should look like this:

```
<Connector port="8080" protocol="HTTP/1.1" 
           connectionTimeout="20000"
           URIEncoding="UTF-8"
           redirectPort="8443" />
```

Be sure to specify the `URIEncoding="UTF-8"` attribute as above to ensure that
connection names, user names, etc. are properly received by the web
application. If you will be creating connections that have Cyrillic, Chinese,
Japanese, or other non-Latin characters in their names or parameter values,
this attribute is required.

### Setting up the Remote IP Valve[#](#setting-up-the-remote-ip-valve "Link to this heading")

By default, when Tomcat is behind a reverse proxy, the remote IP address of the
client that it sees is that of the proxy rather than the original client. In
order to allow applications hosted within Tomcat, like Guacamole, to see the
actual IP address of the client, you have to configure both the reverse proxy
and Tomcat.

Because the remote IP address in Guacamole is used for auditing of user logins
and connections and could potentially be used for authentication, it is
important that you are either in direct control of the proxy server or you
explicitly trust it. Passing the remote IP address is done using the
`X-Forwarded-For` header, and, as with most HTTP headers, attackers can attempt
to spoof this header in order to manipulate the behavior of the web server,
gain unauthorized access to the system, or attempt to disguise the host or IP
address they are coming from.

One final caveat: This may not work as expected if there are other upstream
proxy servers between your reverse proxy and the clients access Guacamole.
Other proxies or firewalls can mask the IP address of the client, and if the
configuration of those is not within your control you may end up with multiple
clients appearing to come from the same IP address or host. Make sure you take
this into account when configuring the system and looking at the data provided.

Configuring Tomcat to pass through the remote IP address provided by the
reverse proxy in the `X-Forwarded-For` header requires the configuration of
what Tomcat calls a Valve. In this case, it is the
[`RemoteIpValve`](https://tomcat.apache.org/tomcat-8.5-doc/config/valve.html#Remote_IP_Valve)
and is configured in the `conf/server.xml` file, in the `<Host>` section:

```
<Valve className="org.apache.catalina.valves.RemoteIpValve"
               internalProxies="127\.0\.0\.1"
               remoteIpHeader="x-forwarded-for"
               remoteIpProxiesHeader="x-forwarded-by"
               protocolHeader="x-forwarded-proto" />
```

The `internalProxies` value should be set to the IP address or addresses of any
and all reverse proxy servers that will be accessing this Tomcat instance
directly. Often it is run on the same system that runs Tomcat, but in other
cases (for example, when running Docker), it may be on a different
system/container and may need to be set to the actual IP address of the reverse
proxy system.

Note that, in situations where both IPv4 and IPv6 are enabled, you may experience
inconsistency in Guacamole being able to retrieve the client IP address if you
fail to account for both IP versions in the `internalProxies` regex. This is
true even if your proxy is running on the same system as Tomcat and you only
have loopback addresses listed, but you fail to account for both IPv4 and
IPv6. Here is an example `RemoteIpValve` configuration that handles both
localhost addresses:

```
<Valve className="org.apache.catalina.valves.RemoteIpValve"
               internalProxies="127\.0\.0\.1|0:0:0:0:0:0:0:1"
               remoteIpHeader="x-forwarded-for"
               remoteIpProxiesHeader="x-forwarded-by"
               protocolHeader="x-forwarded-proto" />
```

Only proxy servers listed in the `internalProxies` or
`trustedProxies` parameters will be allowed to manipulate the remote IP address
information. The other parameters in this configuration line allow you to
control which headers coming from the proxy server(s) are used for various
remote host information. They are as follows:

`remoteIpHeader`
:   The header that is queried to learn the client IP address of the client
    that originated the request. The standard value is `X-Forwarded-For`, but
    can be configured to any header you like. The IP address in this header
    will be available to Java applications in the `request.getRemoteAddr()`
    method.

`remoteIpProxiesHeader`
:   The header that is queried to learn the IP address of the proxy server
    that forwarded the request. The default value is `X-Forwarded-By`, but can
    be configured to any header that fits your environment. This value will
    only be allowed by the valve if the proxy used is listed in the
    `trustedProxies` parameter. Otherwise this header will not be available.

`protocolHeader`
:   The header that is queried to determine the protocol that the client used
    to connect to the service. The default value is `X-Forwarded-Proto`, but
    can be configured to fit your environment.

In addition to configuring Tomcat to properly handle these headers, you also
may need to configure your reverse proxy appropriately to send the headers. You
can find instructions for this in [Nginx](#nginx) - the Apache web server passes it
through by default.

## Nginx[#](#nginx "Link to this heading")

Nginx can be used as a reverse proxy, and supports WebSocket out-of-the-box
[since version 1.3](http://nginx.com/blog/websocket-nginx/). Both Apache and
Nginx require some additional configuration for proxying of WebSocket to work
properly.

### Proxying Guacamole[#](#proxying-guacamole "Link to this heading")

Nginx does support WebSocket for proxying, but requires that the “Connection”
and “Upgrade” HTTP headers are set explicitly due to the nature of the
WebSocket protocol. From the Nginx documentation:

> NGINX supports WebSocket by allowing a tunnel to be set up between a client
> and a back-end server. For NGINX to send the Upgrade request from the client
> to the back-end server, Upgrade and Connection headers must be set
> explicitly. …

The proxy configuration belongs within a dedicated
[`location`](http://nginx.org/en/docs/http/ngx_http_core_module.html#location%3E)
block, declaring the backend hosting Guacamole and explicitly specifying the
“`Connection`” and “`Upgrade`” headers mentioned earlier:

```
location /guacamole/ {
    proxy_pass http://HOSTNAME:8080;
    proxy_buffering off;
    proxy_http_version 1.1;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $http_connection;
    access_log off;
}
```

Here, `HOSTNAME` is the hostname or IP address of the machine hosting your
servlet container, and 8080 is the port that servlet container is configured to
use. You will need to replace these values with the correct values for your
server.

Related to the `RemoteIpValve` configuration for tomcat, documented in
[Setting up the Remote IP Valve](#tomcat-remote-ip), the `proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;` line is important if you want the
`X-Forwarded-For` header to be passed through to the web application server and
available to applications running inside it.

Important

*Do not forget to specify “`proxy_buffering off`”.*

Most proxies, including Nginx, will buffer all data sent over the connection,
waiting until the connection is closed before sending that data to the client.
As Guacamole’s HTTP tunnel relies on streaming data to the client over an open
connection, excessive buffering will effectively block Guacamole connections,
rendering Guacamole useless.

*If the option “`proxy_buffering off`” is not specified, Guacamole may not
work*.

### Changing the path[#](#changing-the-path "Link to this heading")

If you wish to serve Guacamole through Nginx under a path other than
`/guacamole/`, the easiest method is to simply rename the `.war` file. For
example, if intending to server Guacamole at `/new-path/`, you would:

1. Rename `guacamole.war` to `new-path.war`.
2. Update the path within the Nginx configuration to reflect the new
   path:

   ```
   location /new-path/ {
       proxy_pass http://HOSTNAME:8080;
       proxy_buffering off;
       proxy_http_version 1.1;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection $http_connection;
       access_log off;
   }
   ```

Alternatively, the configuration can be altered slightly to handle requests at
a different location externally while still serving internal requests at
`/guacamole/`:

```
location /new-path/ {
    proxy_pass http://HOSTNAME:8080/guacamole/;
    proxy_buffering off;
    proxy_http_version 1.1;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $http_connection;
    access_log off;
}
```

### Adjusting file upload limits[#](#adjusting-file-upload-limits "Link to this heading")

When proxying Guacamole through Nginx, you may run into issues with the default
limitations that Nginx places on file uploads (1MB). The errors you receive can
be non-intuitive (permission denied, for example), but may be indicative of
these limits. The `client_max_body_size` parameter can be set within the
`location` block to configure the maximum file upload size:

```
location /guacamole/ {
    proxy_pass http://HOSTNAME:8080;
    proxy_buffering off;
    proxy_http_version 1.1;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $http_connection;
    client_max_body_size 1g;
    access_log off;
}
```

## Apache and mod\_proxy[#](#apache-and-mod-proxy "Link to this heading")

Apache supports reverse proxy configurations through
[mod\_proxy](http://httpd.apache.org/docs/2.4/mod/mod_proxy.html). Apache 2.4.5
and later also support proxying of WebSocket through a sub-module called
[mod\_proxy\_wstunnel](http://httpd.apache.org/docs/2.4/mod/mod_proxy_wstunnel.html).
Both of these modules will need to be enabled for proxying of Guacamole to work
properly.

Lacking mod\_proxy\_wstunnel, it is still possible to proxy Guacamole, but
Guacamole will be unable to use WebSocket. It will instead fallback to using
the HTTP tunnel, resulting in reduced performance.

### Proxying Guacamole[#](#proxying-with-apache "Link to this heading")

Configuring Apache to proxy HTTP requests requires using the `ProxyPass` and
`ProxyPassReverse` directives, which are provided by the mod\_proxy module.
These directives describe how HTTP traffic should be routed to the web server
behind the proxy:

```
<Location /guacamole/>
    Order allow,deny
    Allow from all
    ProxyPass http://HOSTNAME:8080/guacamole/ flushpackets=on
    ProxyPassReverse http://HOSTNAME:8080/guacamole/
</Location>
```

Here, `HOSTNAME` is the hostname or IP address of the machine hosting your
servlet container, and `8080` is the port that servlet container is configured
to use. You will need to replace these values with the correct values for your
server.

Important

*Do not forget the `flushpackets=on` option.*

Most proxies, including mod\_proxy, will buffer all data sent over the
connection, waiting until the connection is closed before sending that data to
the client. As Guacamole’s HTTP tunnel relies on streaming data to the client
over an open connection, excessive buffering will effectively block Guacamole
connections, rendering Guacamole useless.

*If the option `flushpackets=on` is not specified, Guacamole may not work*.

### Proxying the WebSocket tunnel[#](#proxying-the-websocket-tunnel "Link to this heading")

Apache will not automatically proxy WebSocket connections, but you can proxy
them separately with Apache 2.4.5 and later using mod\_proxy\_wstunnel. After
enabling mod\_proxy\_wstunnel a secondary `Location` section can be added which
explicitly proxies the Guacamole WebSocket tunnel, located at
`/guacamole/websocket-tunnel`:

```
<Location /guacamole/>
    Order allow,deny
    Allow from all
    ProxyPass http://HOSTNAME:8080/guacamole/ flushpackets=on
    ProxyPassReverse http://HOSTNAME:8080/guacamole/
</Location>

<Location /guacamole/websocket-tunnel>
    Order allow,deny
    Allow from all
    ProxyPass ws://HOSTNAME:8080/guacamole/websocket-tunnel
    ProxyPassReverse ws://HOSTNAME:8080/guacamole/websocket-tunnel
</Location>
```

Lacking this, Guacamole will still work by using normal HTTP, but network
latency will be more pronounced with respect to user input, and performance may
be lower.

Important

**The `Location` section for `/guacamole/websocket-tunnel` must be placed after
the `Location` section for the rest of Guacamole.**

Apache evaluates all Location sections, giving priority to the last section
that matches. If the `/guacamole/websocket-tunnel` section comes first, the
section for `/guacamole/` will match instead, and WebSocket will not be proxied
correctly.

### Changing the path[#](#changing-path-with-apache "Link to this heading")

If you wish to serve Guacamole through Apache under a path other than
`/guacamole/`, the easiest method is to simply rename the `.war` file. For
example, if intending to server Guacamole at `/new-path/`, you would:

1. Rename `guacamole.war` to `new-path.war`.
2. Update the paths within the Apache configuration to reflect the new path:

   ```
   <Location /new-path/>
       Order allow,deny
       Allow from all
       ProxyPass http://HOSTNAME:8080/new-path/ flushpackets=on
       ProxyPassReverse http://HOSTNAME:8080/new-path/
   </Location>

   <Location /new-path/websocket-tunnel>
       Order allow,deny
       Allow from all
       ProxyPass ws://HOSTNAME:8080/new-path/websocket-tunnel
       ProxyPassReverse ws://HOSTNAME:8080/new-path/websocket-tunnel
   </Location>
   ```

Alternatively, the configuration can be altered slightly to handle requests at
a different location externally while still serving internal requests at
`/guacamole/`:

```
<Location /new-path/>
    Order allow,deny
    Allow from all
    ProxyPass http://HOSTNAME:8080/guacamole/ flushpackets=on
    ProxyPassReverse http://HOSTNAME:8080/guacamole/
</Location>

<Location /new-path/websocket-tunnel>
    Order allow,deny
    Allow from all
    ProxyPass ws://HOSTNAME:8080/guacamole/websocket-tunnel
    ProxyPassReverse ws://HOSTNAME:8080/guacamole/websocket-tunnel
</Location>
```

### Disabling logging of tunnel requests[#](#disabling-logging-of-tunnel-requests "Link to this heading")

If WebSocket is unavailable, Guacamole will fallback to using an HTTP-based
tunnel. The Guacamole HTTP tunnel works by transferring a continuous stream of
data over multiple short-lived streams, each associated with a separate HTTP
request. By default, Apache will log each of these requests, resulting in a
rather bloated access log.

There is little value in a log file filled with identical tunnel requests, so
it is recommended to explicitly disable logging of those requests. Apache does
provide a means of matching URL patterns and setting environment variables
based on whether the URL matches. Logging can then be restricted to requests
which lack this environment variable:

```
SetEnvIf Request_URI "^/guacamole/tunnel" dontlog
CustomLog  /var/log/apache2/guac.log common env=!dontlog
```

Note that if you are serving Guacamole under a path different from
`/guacamole/`, you will need to change the value of `Request_URI` above
accordingly.

Contents

---
# Authenticating with Guacamole using single sign-on

# Authenticating with Guacamole using single sign-on[#](#authenticating-with-guacamole-using-single-sign-on "Link to this heading")

Single sign-on alows you to leverage a third-party authentication service that
can be shared by multiple applications, including Guacamole. This has the
benefit of streamlining and centralizing authentication when users would
otherwise need to maintain a distinct set of credentials for each application.
Guacamole supports the following single sign-on methods:

[CAS](cas-auth.html)
:   An open source single sign-on application that implements its own
    authentication protocol.

[OpenID Connect](openid-auth.html) and [SAML](saml-auth.html)
:   Widely supported open standards for single sign-on. It is extremely common
    for commercial identity providers to support at least one of these standards.

[Smart cards / Certificates](ssl-auth.html)
:   User identification using certificates that are installed on the user’s
    machine or within smart cards presented by the user. The user identity is
    derived from the content of the certificate presented, if valid. This
    mechanism makes use of SSL/TLS client authentication via a [reverse
    proxy](reverse-proxy.html).

Hint

OpenID Connect is commonly confused with “OAuth”, with the term “OAuth”
sometimes used incorrectly to refer to OpenID Connect.

---
# Guacamole’s administrative interface

## Contents

# Guacamole’s administrative interface[#](#guacamoles-administrative-interface "Link to this heading")

Users, user groups, connections, and active sessions can be administered from
within the web interface if the underlying authentication module supports this.
The only officially-supported authentication modules supporting this are the
database extensions, which are documented in [Database authentication](jdbc-auth.html).

If you are using the default authentication mechanism, or another
authentication extension, this chapter probably does not apply to you, and the
management options will not be visible in the Guacamole interface. If, on the
other hand, you are using one of the database authentication providers, and you
are logged in as a user with sufficient privileges, you will see management
sections listed within the settings screen:

![Sections within the Guacamole settings screen.](assets/doc_gug__images_guacamole-settings-sections.png)

Clicking any of these options will take you to a corresponding management
section where you can perform administrative tasks.

## Managing sessions[#](#managing-sessions "Link to this heading")

Clicking “Active Sessions” navigates to the session management screen. The
session management screen displays all active sessions and allows system
administrators to kill them as needed.

When any user accesses a particular remote desktop connection, a unique session
is created and will appear in the list of active sessions in the session
management screen. Each active session is displayed in a sortable table,
showing the corresponding user’s username, how long the session has been
active, the IP address of the machine from which the user is connecting, and
the name of the connection being used.

![Session management interface](assets/doc_gug__images_manage-sessions.png)

To kill one or more sessions, select the sessions by clicking their checkboxes.
Once all desired sessions have been selected, clicking “Kill Sessions” will
immediately disconnect those users from the associated connection.

### Filtering and sorting[#](#filtering-and-sorting "Link to this heading")

The table can be resorted by clicking on the column headers. Clicking any
column will resort the table by the values within that column, while clicking a
column which is already sorted will toggle between ascending and descending
order.

The content of the table can be limited through search terms specified in the
“Filter” field. Entering search terms will limit the table to only sessions
containing those terms. For example, to list only connections by the user
“guacadmin” which have been active since March, 2015, you would enter:
“guacadmin 2015-03”. Beware that if a search term needs to contain spaces, it
must be enclosed in double quotes to avoid being interpreted as multiple terms.

![](assets/doc_gug__images_session-filter-example-1.png)

If you wish to narrow the content of the table to only those connections which
originate from a particular block of IP addresses, you can do this by
specifying the block in standard CIDR notation, such “10.0.0.0/8” or
“2001:db8:1234::/48”. This will work with both IPv4 and IPv6 addresses.

![](assets/doc_gug__images_session-filter-example-2.png)

## Connection history[#](#connection-history "Link to this heading")

Clicking “History” navigates to the connection history screen. The connection
history screen displays a table of the most recent connections, including the
user that used that connection, the time the connection began, how long the
connection was used, and whether a corresponding recording is available for
viewing:

![Connection history interface with recordings](assets/doc_gug__images_history-table-with-recordings.png)

Recordings are only made for a connection if an administrator explicitly
configures the connection to produce recordings, and those recordings are only
available from this screen if the administrator explicitly configures the
connection to [store those recordings in a location dedicated for future
in-browser playback](recording-playback.html).

### Filtering and sorting[#](#filtering-history "Link to this heading")

Initially, the connection history table will display only the most recent
history records. You can page through these records to see how and when
Guacamole has been used.

Just as with the table of active sessions described earlier, the table of
history records can be resorted by clicking on the column headers or filtered
by entering search terms within the “Filter” field.

The same filtering format applies - a search term containing spaces must be
enclosed in double quotes to avoid being interpreted as multiple terms, and
only history records which contain each term will be included in the history
table. Unlike the table of active sessions, however, the filter will only take
effect once you click the “Search” button. This is due to the nature of the
connection history, as the number of records may be quite extensive.

## User management[#](#user-management "Link to this heading")

Clicking “Users” within the list of settings sections will take you to the user
management screen. Here you can add new users, edit the properties and
privileges of existing users, and view the times that each user last logged in.
If you have a large number of users, you can also enter search terms within the
“Filter” field to filter the list of users by username.

To add a new user, click the “New User” button. This will take you to a screen
where you will be allowed to enter the details of the new user, such as the
password and username. Note that, unless you specify otherwise, the new user
will have no access to any existing connections, nor any administrative
privileges, and you will need to manually set the user’s password before they
will be able to log in.

![User management interface](assets/doc_gug__images_manage-users.png)

To edit a user, just click on the user you wish to edit. You will be taken to a
screen which allows you to change the user’s password, expire their password
(such that it must be changed at next login), add or remove administrative
permissions, and add or remove read access to specific connections, sharing
profiles, or groups. If you are managing a large number of connections or
groups and wish to reduce the size of the list displayed, you can do so by
specifying search terms within the “Filter” field. Groups will be filtered by
name and connections will be filtered by name or protocol.

If you have delete permission on the user, you will also see a “Delete” button.
Clicking this button will permanently delete the user. Alternatively, if you
only wish to temporarily disable the account, checking “Login disabled” will
achieve the same effect while not removing the user entirely. If they attempt
to log in, the attempt will be rejected as if their account did not exist at
all.

![Editing a user](assets/doc_gug__images_edit-user.png)

### Editing group membership[#](#editing-group-membership "Link to this heading")

When editing a user, the groups that user is a member of may be modified within
the “Groups” section. By default, only groups that the user is already a member
of will be displayed. If you have permission to modify the user’s membership
within a group, an “X” icon will be available next to that group’s name.
Clicking the “X” will remove the user from that group, taking effect after the
user is saved.

To add users to a group, the arrow next to the list of groups must be clicked
to expand the section and reveal all available groups. Available groups may
then be checked/unchecked to modify the user’s membership within those groups:

![Editing group membership of a user](assets/doc_gug__images_edit-user-membership.png)

If you have a large number of available groups, you can also enter search terms
within the “Filter” field to filter the list of groups by name.

## User group management[#](#user-group-management "Link to this heading")

Clicking “Groups” within the list of settings sections will take you to the
user group management screen. Here you can add new groups and edit the
properties and privileges of existing groups. If you have a large number of
user groups, you can also enter search terms within the “Filter” field to
filter the list of groups by name:

![User group management interface](assets/doc_gug__images_manage-groups.png)

To add a new group, click the “New Group” button. This will take you to a
screen where you will be allowed to enter the details of the new group,
including membership and any permissions that members of the group should have.

To edit a group, just click on the group you wish to edit. You will be taken to
a screen which allows you to modify membership, add or remove administrative
permissions, and add or remove read access to specific connections, sharing
profiles, or connection groups. If you are managing a large number of
connections or groups and wish to reduce the size of the list displayed, you
can do so by specifying search terms within the “Filter” field. Connection
groups will be filtered by name and connections will be filtered by name or
protocol.

If you have delete permission on the group, you will also see a “Delete”
button. Clicking this button will permanently delete the group. Alternatively,
if you only wish to temporarily disable the effects of membership in the group,
checking “Disabled” will achieve the same effect while not removing the group
entirely.

![Editing a user group](assets/doc_gug__images_edit-user-group.png)

### Group membership of groups[#](#group-membership-of-groups "Link to this heading")

Managing the group membership of groups is more complex than that of users, as
groups may contain both users and groups, with permissions from parent groups
possibly being inherited. Parent groups, member groups, and member users, can
all be managed identically to the [group memberships of users](#user-group-membership),
with a corresponding section dedicated to each within the user group editor:

![Editing the various membership relations of a user group](assets/doc_gug__images_edit-group-memberships.png)

Note that it is ultimately up to the extension providing the group to determine
how permissions granted to that group are inherited, if at all. The [database
authentication extension](jdbc-auth.html) implements full recursive inheritance of
group permissions, with permissions granted to a group being granted to all
members/descendants of that group, regardless of how deeply those members are
nested.

## Connections and connection groups[#](#connections-and-connection-groups "Link to this heading")

Clicking “Connections” within the list of settings sections will take you to
the connection management screen. The connection management screen allows
administrators to create and edit connections, sharing profiles, and connection
groups. If you have a large number of connections, you can also enter search
terms within the “Filter” field to filter the list of connections by name or
protocol.

To add a new connection or connection group, click the “New Connection” or “New
Group” button, or the “New Connection” or “New Group” placeholders which appear
when you expand an existing connection group. These options will take you to a
screen where you will be allowed to enter the details of the new object, such
as its location, parameters, and name. This name should be descriptive, but
must also be unique with respect to other objects in the same location.

Once you click “Save”, the new object will be added, but will initially only be
usable by administrators and your current user. To grant another user access to
the new connection or connection group, you must [edit that user](#user-management)
or [a user group that the user is a member of](#user-group-management), checking
the box corresponding to the connection or connection group you created.

Connections and connection groups can also be imported en masse from files - see
the documentation for the [batch import feature](batch-import.html).

![Connection management interface](assets/doc_gug__images_manage-connections.png)

Editing connections, sharing profiles, and connection groups works identically
to editing a user. Click on the object you wish to edit, and you will be taken
to screen which allows you to edit it. The screen will display all properties
of the object, including its usage history, if applicable.

If you have delete permission on the object, you will also see a “Delete”
button. Clicking this button will permanently delete the object being edited.

![Editing a connection](assets/doc_gug__images_edit-connection.png)

### Connection organization and balancing[#](#connection-organization-and-balancing "Link to this heading")

Connection groups can be either “organizational” or “balancing”. Each group can
contain any number of other connections or groups, but the semantics of the
group change depending on the type.

An organizational group behaves exactly as a folder or directory in a file
system. It simply contains connections and other groups, but provides no other
behavior. Clicking on an organizational group within a connection list will
expand the group, revealing its contents.

A balancing group behaves as a connection. It dynamically balances load across
the connections it contains, choosing the connection with the fewest number of
active users. Unlike organizational groups, clicking on a balancing group
causes a new connection to be opened. The actual underlying connection used
depends on which connection has the least load at the time the group was
clicked, and whether session affinity is enabled on that group.

Enabling session affinity for a balancing group ensures that users are
consistently routed to the same underlying connections until they log out of
Guacamole. The load balancing behavior of the balancing group will apply only
for the first time a particular user connects to the group. If your users may
lose their desktop state if they are routed to a different underlying
connection, this option should be enabled.

![Editing a connection group](assets/doc_gug__images_edit-group.png)

### Connection sharing[#](#connection-sharing "Link to this heading")

The ability to share a connection is governed through the use of “sharing
profiles”. If a sharing profile is created for a connection, users with access
to both that connection and that sharing profile will be able to share the
connection with other users by [generating connection sharing
links](using-guacamole.html#client-share-menu), even if those users do not otherwise have user
accounts within Guacamole.

The name of the sharing profile will be presented as an option within the
[share menu](using-guacamole.html#client-share-menu) for any users with access, while the level of
access granted to users of generated share links will be dictated by the
parameters specified for the sharing profile.

Important

*The only extension which ships with Guacamole and implements enough of the
[Guacamole extension API](guacamole-ext.html) to share its connections is the
[database authentication extension](jdbc-auth.html).* If you wish to share
connections (or allow your users to share connections), you will need to use
the database authentication extension to store those connections.

If you need to use other authentication schemes, keep in mind that the database
authentication extension can be used [alongside other extensions](ldap-auth.html#ldap-and-database),
with the database handling connection storage and permissions only. Writing
your own extension which supports sharing is another alternative, though that
may be overly complicated if everything you need is already provided.

Unlike connections and groups, there is no “New Sharing Profile” button.
Sharing profiles are created through clicking the “New Sharing Profile”
placeholders which appear when connections are expanded. Just as
expanding a connection group reveals the connections or groups therein,
expanding a connection reveals the sharing profiles associated with that
connection. This holds true with both [the list of connections in the
connection management screen](#connection-management) and [the list of
connections in the user editor](#user-management).

Creating or editing a sharing profile is virtually identical to creating or
editing a connection, with the exception that not all connection parameters are
available:

![Editing a sharing profile](assets/doc_gug__images_edit-sharing-profile.png)

Contents

---
# Using Duo for multi-factor authentication

## Contents

# Using Duo for multi-factor authentication[#](#using-duo-for-multi-factor-authentication "Link to this heading")

Guacamole’s Duo authentication extension allows the third-party Duo service to
be used as an additional authentication factor for users of your Guacamole
installation. If installed, users that attempt to authenticate against
Guacamole will be sent to Duo’s service for further verification.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

Note

Guacamole’s Duo support cannot currently be used alongside [single sign-on](sso.html). If
you use Duo and need both [MFA](mfa.html) and [SSO](sso.html) support for Guacamole, you
will need to either use your SSO provider’s own Duo integration or use
[TOTP](totp-auth.html) instead of Duo.

## How Duo works with Guacamole[#](#how-duo-works-with-guacamole "Link to this heading")

Duo is strictly a service for verifying the identities of users that have
already been partially verified through another authentication method. Thus,
for Guacamole to make use of Duo, at least one other authentication mechanism
will need be configured, such as [a supported database](jdbc-auth.html) or
[LDAP](ldap-auth.html).

When a user attempts to log into Guacamole, other installed authentication
methods will be queried first:

![](assets/doc_gug__images_duo-auth-factor-1.png)

Only after authentication has succeeded with one of those methods will
Guacamole reach out to Duo to obtain additional verification of user
identity:

![](assets/doc_gug__images_duo-auth-factor-2.png)

If both the initial authentication attempt and verification through Duo
succeed, the user will be allowed in. If either mechanism fails, access
to Guacamole is denied.

## Adding Guacamole to Duo[#](#adding-guacamole-to-duo "Link to this heading")

Duo does not provide a specific integration option for Guacamole, but
Guacamole’s Duo extension uses Duo’s generic authentication API which
they refer to as the “Web SDK”. To use Guacamole with Duo, you will need
to add it as a new “Web SDK” application from within the “Applications”
tab of the admin panel of your Duo account:

![](assets/doc_gug__images_duo-add-guacamole.png)

Within the settings of the newly-added application, rename the
application to something more representative than “Web SDK”. This
application name is what will be presented to your users when they are
prompted by Duo for additional authentication:

![](assets/doc_gug__images_duo-rename-guacamole.png)

Once you’ve finished adding Guacamole as a “Web SDK” application, the
information required to configure Guacamole is listed within the application’s
“Details” section. You will need to copy the client ID, secret, and API
hostname - they will later be specified within Guacamole’s configuration:

![](assets/doc_gug__images_duo-copy-details.png)

## Installing/Enabling the Duo extension[#](#installing-enabling-the-duo-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-duo-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-duo-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-duo-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `DUO_ENABLED` environment variable:

    ```
    DUO_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e DUO_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `DUO_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `DUO_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Required configuration[#](#required-configuration "Link to this heading")

Native Webapp (Tomcat)

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
duo-api-hostname: api-XXXXXXXX.duosecurity.com
duo-client-id: XXXXXXXXXXXXXXXXXXXX
duo-client-secret: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
duo-redirect-uri: https://myguac.example.net
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`duo-api-hostname`
:   The hostname of the Duo API endpoint to be used to verify user identities.
    This will usually be in the form `api-XXXXXXXX.duosecurity.com`,
    where `XXXXXXXX` is some arbitrary alphanumeric value assigned by
    Duo. This value will have been generated by Duo when you added Guacamole as
    a “Web SDK” application, and can be found within the application details in
    the “API hostname” field. *This value is required.*

`duo-client-id`
:   The unique client ID provided for Guacamole by Duo. This value will
    have been generated by Duo when you added Guacamole as a “Web SDK”
    application, and can be found within the application details in the
    “Client ID” field. *This value is required.*

    This value was formerly known as the “integration key” in older versions of
    Duo’s “Web SDK” and was configured with the `duo-integration-key` property
    in older versions of Guacamole.

`duo-client-secret`
:   The shared secret provided for Guacamole by Duo. This value will have been
    generated by Duo when you added Guacamole as a “Web SDK” application, and can
    be found within the application details in the “Client secret” field. *This
    value is required.*

    This value was formerly known as the “secret key” in older versions of Duo’s
    “Web SDK” and was configured with the `duo-secret-key` property in older
    versions of Guacamole.

`duo-redirect-uri`
:   The URI that should be submitted to the Duo service such that they can
    redirect the authenticated user back to Guacamole after the authentication
    process is complete. This must be the full URL that a user would enter into
    their browser to access Guacamole. *This value is required.*

Container (Docker)

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
DUO_API_HOSTNAME: 'api-XXXXXXXX.duosecurity.com'
DUO_CLIENT_ID: 'XXXXXXXXXXXXXXXXXXXX'
DUO_CLIENT_SECRET: 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
DUO_REDIRECT_URI: 'https://myguac.example.net'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e DUO_API_HOSTNAME="api-XXXXXXXX.duosecurity.com" \
    -e DUO_CLIENT_ID="XXXXXXXXXXXXXXXXXXXX" \
    -e DUO_CLIENT_SECRET="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" \
    -e DUO_REDIRECT_URI="https://myguac.example.net" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`DUO_API_HOSTNAME`
:   The hostname of the Duo API endpoint to be used to verify user identities.
    This will usually be in the form `api-XXXXXXXX.duosecurity.com`,
    where `XXXXXXXX` is some arbitrary alphanumeric value assigned by
    Duo. This value will have been generated by Duo when you added Guacamole as
    a “Web SDK” application, and can be found within the application details in
    the “API hostname” field. *This value is required.*

`DUO_CLIENT_ID`
:   The unique client ID provided for Guacamole by Duo. This value will
    have been generated by Duo when you added Guacamole as a “Web SDK”
    application, and can be found within the application details in the
    “Client ID” field. *This value is required.*

    This value was formerly known as the “integration key” in older versions of
    Duo’s “Web SDK” and was configured with the `duo-integration-key` property
    in older versions of Guacamole.

`DUO_CLIENT_SECRET`
:   The shared secret provided for Guacamole by Duo. This value will have been
    generated by Duo when you added Guacamole as a “Web SDK” application, and can
    be found within the application details in the “Client secret” field. *This
    value is required.*

    This value was formerly known as the “secret key” in older versions of Duo’s
    “Web SDK” and was configured with the `duo-secret-key` property in older
    versions of Guacamole.

`DUO_REDIRECT_URI`
:   The URI that should be submitted to the Duo service such that they can
    redirect the authenticated user back to Guacamole after the authentication
    process is complete. This must be the full URL that a user would enter into
    their browser to access Guacamole. *This value is required.*

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Native Webapp (Tomcat)

The following additional, optional properties may be set as desired
to tailor the behavior of the Duo support:

`duo-auth-timeout`
:   The maximum amount of time to wait for a user to finish authenticating with
    Duo, in minutes. Any authentication attempt that takes longer than this
    amount of time will be rejected, requiring the user to reenter their
    credentials and possibly revalidate their identity with Duo. By default,
    login attempts are allowed to take up to 5 minutes.

Container (Docker)

The following additional, optional environment variables may be set as desired
to tailor the behavior of the Duo support:

`DUO_AUTH_TIMEOUT`
:   The maximum amount of time to wait for a user to finish authenticating with
    Duo, in minutes. Any authentication attempt that takes longer than this
    amount of time will be rejected, requiring the user to reenter their
    credentials and possibly revalidate their identity with Duo. By default,
    login attempts are allowed to take up to 5 minutes.

### Bypass/Enforce Duo for Specific Hosts[#](#bypass-enforce-duo-for-specific-hosts "Link to this heading")

Native Webapp (Tomcat)

By default, when the Duo module is enabled, Duo-based MFA will be enforced for
all users that attempt to log in to Guacamole, regardless of where they are
connecting from. Depending on your use case, it may be necessary to narrow this
behavior and only enforce Duo-based MFA for certain hosts and bypass it for
others.

Warning

If you will be configuring Guacamole to consider users’ IP addresses, **it is
important to make sure that Guacamole is receiving correct IP address
information for all clients**.

If Guacamole is behind a reverse proxy, such as for SSL termination, the IP
addresses of all users will appear to be the IP address of the proxy unless
additional configuration steps are taken. **Be sure to follow [the
documentation for configuring forwarding of client IP
information](reverse-proxy.html)!**

Duo-based MFA can be explicitly bypassed or enforced on a per-host basis by
providing the relevant, exhaustive list of addresses/networks using either of
the following properties:

`duo-bypass-hosts`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD NOT be required to verify themselves with Duo when
    authenticating. All other hosts in this list will required to verify against
    Duo.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and this property is effectively ignored.**

    This property is optional. By default, verification against Duo will be
    required for all users regardless of their IP address (Duo is not bypassed
    for any addresses).

`duo-enforce-hosts`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD be required to verify themselves with Duo when authenticating.
    All other hosts will not be required to verify against Duo.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and the bypass list is effectively ignored.**

    This property is optional. By default, verification against Duo will be
    required for all users regardless of their IP address (Duo is enforced for
    all addresses).

Container (Docker)

By default, when the Duo module is enabled, Duo-based MFA will be enforced for
all users that attempt to log in to Guacamole, regardless of where they are
connecting from. Depending on your use case, it may be necessary to narrow this
behavior and only enforce Duo-based MFA for certain hosts and bypass it for
others.

Warning

If you will be configuring Guacamole to consider users’ IP addresses, **it is
important to make sure that Guacamole is receiving correct IP address
information for all clients**.

If Guacamole is behind a reverse proxy, such as for SSL termination, the IP
addresses of all users will appear to be the IP address of the proxy unless
additional configuration steps are taken. **Be sure to follow [the
documentation for configuring forwarding of client IP
information](reverse-proxy.html)!**

Duo-based MFA can be explicitly bypassed or enforced on a per-host basis by
providing the relevant, exhaustive list of addresses/networks using either of
the following environment variables:

`DUO_BYPASS_HOSTS`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD NOT be required to verify themselves with Duo when
    authenticating. All other hosts in this list will required to verify against
    Duo.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and this property is effectively ignored.**

    This property is optional. By default, verification against Duo will be
    required for all users regardless of their IP address (Duo is not bypassed
    for any addresses).

`DUO_ENFORCE_HOSTS`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD be required to verify themselves with Duo when authenticating.
    All other hosts will not be required to verify against Duo.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and the bypass list is effectively ignored.**

    This property is optional. By default, verification against Duo will be
    required for all users regardless of their IP address (Duo is enforced for
    all addresses).

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# Database schema reference

## Contents

# Database schema reference[#](#database-schema-reference "Link to this heading")

If necessary, it is possible to modify the data backing the authentication
module manually by executing SQL statements against the database. In general
use, this will not be common, but if you need to bulk-insert a large number of
users or connections, or you wish to translate an existing configuration
automatically, you will need to know how everything is laid out at a high
level.

This section assumes knowledge of SQL and your chosen database, and that
whatever you need to do can be accomplished if only you had high-level
information about Guacamole’s SQL schema.

## Entities[#](#entities "Link to this heading")

Every user and user group has a corresponding entry in the `guacamole_entity`
table which serves as the basis for assignment of a unique name, permissions,
as well as relations which are common to both users and groups like group
membership. Each entity has a corresponding name which is unique across all
other entities of the same type.

If deleting a user or user group, the corresponding entity should also be
deleted. As any user or group which points to the entity will be deleted
automatically when the entity is deleted through cascading deletion, *it is
advisable to use the entity as the basis for any delete operation*.

The `guacamole_entity` table contains the following columns:

`entity_id`
:   The unique integer associated with each entity (user or user group). This
    value is generated automatically when a new entry is inserted into the
    `guacamole_entity` table and is distinct from the unique integer associated
    with the user entry in [`guacamole_user`](#jdbc-auth-schema-users) or the user
    group entry in [`guacamole_user_group`](#jdbc-auth-schema-groups).

`name`
:   The unique name associated with each user or group. This value must be
    specified manually, and must be different from any existing user or group in
    the table. The name need only be unique relative to the names of other entities
    having the same type (a user may have the same name as a group).

`type`
:   The type of this entity. This can be either `USER` or `USER_GROUP`.

## Users[#](#users "Link to this heading")

Every user has a corresponding entry in the `guacamole_user` and
[`guacamole_entity`](#jdbc-auth-schema-entities) tables. Each user has a
corresponding unique username, specified via `guacamole_entity`, and salted
password. The salted password is split into two columns: one containing the
salt, and the other containing the password hashed with SHA-256.

If deleting a user, the [corresponding entity](#jdbc-auth-schema-entities)
should also be deleted. As any user which points to the entity will be deleted
automatically when the entity is deleted through cascading deletion, *it is
advisable to use the entity as the basis for any delete operation*.

The `guacamole_user` table contains the following columns:

`user_id`
:   The unique integer associated with each user. This value is generated
    automatically when a new entry is inserted into the `guacamole_user` table.

`entity_id`
:   The value of the `entity_id` column of the `guacamole_entity` entry
    representing this user.

`password_hash`
:   The result of hashing the user’s password concatenated with the contents of
    `password_salt` using SHA-256. The salt is appended to the password prior to
    hashing.

    Although passwords set through Guacamole will always be salted, it is
    possible to use unsalted password hashes when inserted manually or through an
    external system. If `password_salt` is `NULL`, the `password_hash` will be
    handled as a simple unsalted hash of the password.

`password_salt`
:   A 32-byte random value. When a new user is created from the web interface,
    this value is randomly generated using a cryptographically-secure random
    number generator.

    This will always be set for users whose passwords are set through Guacamole,
    but it is possible to use unsalted password hashes when inserted manually or
    through an external system. If `password_salt` is `NULL`, the `password_hash`
    will be handled as a simple unsalted hash of the password.

`password_date`
:   The date (and time) that the password was last changed. When a password is
    changed via the Guacamole interface, this value is updated. This, along with
    the contents of the `guacamole_user_password_history` table, is used to
    enforce password policies.

`disabled`
:   Whether login attempts as this user account should be rejected. If this
    column is set to `TRUE` or `1`, login attempts by this user will be rejected
    as if the user did not exist. By default, user accounts are not disabled, and
    login attempts will succeed if the user provides the correct password.

`expired`
:   If set to `TRUE` or `1`, requires that the user reset their password prior to
    fully logging in. The user will be presented with a password reset form, and
    will not be allowed to log into Guacamole until the password has been changed.
    By default, user accounts are not expired, and no password reset will be
    required upon login.

`access_window_start`
:   The time of day (not date) after which this user account may be used. If
    `NULL`, this restriction does not apply. If set to non-`NULL`, attempts to log
    in after the specified time will be allowed, while attempts to log in before
    the specified time will be denied.

`access_window_end`
:   The time of day (not date) after which this user account may *not* be used.
    If `NULL`, this restriction does not apply. If set to non-`NULL`, attempts to
    log in after the specified time will be denied, while attempts to log in
    before the specified time will be allowed.

`valid_from`
:   The date (not time of day) after which this user account may be used. If
    `NULL`, this restriction does not apply. If set to non-`NULL`, attempts to
    log in after the specified date will be allowed, while attempts to log in
    before the specified date will be denied.

`valid_until`
:   The date (not time of day) after which this user account may *not* be used.
    If `NULL`, this restriction does not apply. If set to non-`NULL`, attempts to
    log in after the specified date will be denied, while attempts to log in
    before the specified date will be allowed.

`timezone`
:   The time zone to use when interpreting the `access_window_start`,
    `access_window_end`, `valid_from`, and `valid_until` values. This value may
    be any Java `TimeZone` ID, as defined by
    [`getAvailableIDs()`](http://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html#getAvailableIDs())
    though the Guacamole management interface will only present a subset of these
    time zones.

`full_name`
:   The user’s full name. Unlike the username, this name need not be unique; it
    is optional and is meant for display purposes only. Defining this value has
    no bearing on user identity, which is dictated purely by the username. User
    accounts with no associated full name should have this column set to `NULL`.

`email_address`
:   The user’s email address, if any. This value is optional, need not be unique
    relative to other defined users, and is meant for display purposes only.
    Defining this value has no bearing on user identity, which is dictated purely
    by the username. If the user has no associated email address, this column
    should be set to `NULL`.

`organization`
:   The name of the organization, company, etc. that the user is affiliated with.
    This value is optional and is meant for display purposes only. Defining this
    value has no bearing on user identity, which is dictated purely by the
    username. Users with no associated organization should have this column set
    to `NULL`.

`organizational_role`
:   The role or title of the user at the organization described by the
    organization column. This value is optional and is used for display purposes
    only. Defining this value has no bearing on user identity, which is dictated
    purely by the username. Users with no associated organization (or specific
    role/title at that organization) should have this column set to `NULL`.

Important

If you choose to manually set unsalted password hashes, please be sure you
understand the security implications of doing so.

In the event that your database is compromised, finding the password for a
*salted* hash is computationally infeasible, but finding the password for an
*unsalted* hash is often not. In many cases, the password which corresponds to
an unsalted hash can be found simply by entering the hash into a search engine
like Google.

If creating a user manually, the main complication is the salt, which must be
determined before the `INSERT` statement can be constructed, but this can be
dealt with using variables. For MySQL:

```
-- Generate salt
SET @salt = UNHEX(SHA2(UUID(), 256));

-- Create base entity entry for user
INSERT INTO guacamole_entity (name, type)
VALUES ('myuser', 'USER');

-- Create user and hash password with salt
INSERT INTO guacamole_user (
    entity_id,
    password_salt,
    password_hash,
    password_date
)
SELECT
    entity_id,
    @salt,
    UNHEX(SHA2(CONCAT('mypassword', HEX(@salt)), 256)),
    CURRENT_TIMESTAMP
FROM guacamole_entity
WHERE
    name = 'myuser'
    AND type = 'USER';
```

This sort of statement is useful for both creating new users or for changing
passwords, especially if all administrators have forgotten theirs.

If you are not using MySQL, or you are using a version of MySQL that lacks the
SHA2 function, you will need to calculate the SHA-256 value manually (by using
the `sha256sum` command, for example).

### Password history[#](#password-history "Link to this heading")

When a user’s password is changed, a copy of the previous password’s
hash and salt is made within the `guacamole_user_password_history`.
Each entry in this table is associated with the user whose password
changed, along with the date that password first applied.

Old entries within this table are automatically deleted on a per-user
basis depending on the requirements of the password policy. For example,
if the password policy has been configured to require that users not
reuse any of their previous six passwords, then there will be no more
than six entries in this table for each user.

`password_history_id`
:   The unique integer associated with each password history record. This
    value is generated automatically when a new entry is inserted into the
    `guacamole_user_password_history` table.

`user_id`
:   The value of the `user_id` column from the entry in `guacamole_user`  
    associated with the user who previously had this password.

`password_hash`
:   The hashed password specified within the `password_hash` column of  
    `guacamole_user` prior to the password being changed.

    In most cases, this will be a salted hash, though it is possible to force
    the use of unsalted hashes when making changes to the database manually or
    through an external system.

`password_salt`
:   The salt value specified within the `password_salt` column of
    `guacamole_user` prior to the password being changed.

    This will always be set for users whose passwords are set through
    Guacamole, but it is possible to use unsalted password hashes when
    inserted manually or through an external system, in which case this may be
    `NULL`.

`password_date`
:   The date (and time) that the password was set. The time that the password
    ceased being used is recorded either by the `password_date` of the next
    related entry in `guacamole_user_password_history` or `password_date` of
    `guacamole_user` (if there is no such history entry).

### Login history[#](#login-history "Link to this heading")

When a user logs in or out, a corresponding entry in the
`guacamole_user_history` table is created or updated respectively.
Each entry is associated with the user that logged in and the time their
session began. If the user has logged out, the time their session ended
is also stored.

It is very unlikely that a user will need to update this table, but
knowing the structure is potentially useful if you wish to generate a
report of Guacamole usage. The `guacamole_user_history` table has the
following columns:

`history_id`
:   The unique integer associated with each history record. This value is
    generated automatically when a new entry is inserted into the
    `guacamole_user_history` table.

`user_id`
:   The value of the `user_id` from the entry in `guacamole_user` associated
    with the user that logged in. If the user no longer exists, this will be
    `NULL`.

`username`
:   The username associated with the user at the time that they logged in.
    This username value is not guaranteed to uniquely identify a user, as the
    original user may be subsequently renamed or deleted.

`remote_host`
:   The hostname or IP address of the machine that the user logged in from, if
    known. If unknown, this will be `NULL`.

`start_date`
:   The time at which the user logged in. Despite its name, this column also
    stores time information in addition to the date.

`end_date`
:   The time at which the user logged out. If the user is still active, the
    value in this column will be `NULL`. Despite its name, this column also
    stores time information in addition to the date.

## User groups[#](#user-groups "Link to this heading")

Similar to [users](#jdbc-auth-schema-users), every user group has a
corresponding entry in the `guacamole_user_group` and
[`guacamole_entity`](#jdbc-auth-schema-entities) tables. Each user group has a
corresponding unique name specified via `guacamole_entity`.

If deleting a user group, the [corresponding entity](#jdbc-auth-schema-entities)
should also be deleted. As any user group which points to the entity will be
deleted automatically when the entity is deleted through cascading deletion,
*it is advisable to use the entity as the basis for any delete operation*.

The `guacamole_user_group` table contains the following columns:

`user_group_id`
:   The unique integer associated with each user group. This value is
    generated automatically when a new entry is inserted into the
    `guacamole_user_group` table.

`entity_id`
:   The value of the `entity_id` column of the `guacamole_entity` entry  
    representing this user group.

`disabled`
:   Whether membership within this group should be taken into account when
    determining the permissions granted to a particular user. If this column
    is set to `TRUE` or `1`, membership in this group will have no effect on
    user permissions, whether those permissions are granted to this group
    directly or indirectly through the groups that this group is a member of.
    By default, user groups are not disabled, and permissions granted to a
    user through the group will be taken into account.

Membership within a user group is dictated through entries in the
`guacamole_user_group_member` table. As both users and user groups may be
members of groups, each entry associates the containing group with the entity
of the member.

The `guacamole_user_group_member` table contains the following columns:

`user_group_id`
:   The `user_group_id` value of the user group having the specified member.

`member_entity_id`
:   The `entity_id` value of the user or user group that is a member of the
    specified group.

## Connections and parameters[#](#connections-and-parameters "Link to this heading")

Each connection has an entry in the `guacamole_connection` table, with a
one-to-many relationship to parameters, stored as name/value pairs in the
`guacamole_connection_parameter` table.

The `guacamole_connection` table is simply a pairing of a unique and
descriptive name with the protocol to be used for the connection. It contains
the following columns:

`connection_id`
:   The unique integer associated with each connection. This value is
    generated automatically when a new entry is inserted into the
    `guacamole_connection` table.

`connection_name`
:   The unique name associated with each connection. This value must be
    specified manually, and must be different from any existing connection
    name in the same connection group. References to connections in other
    tables use the value from `connection_id`, not `connection_name`.

`protocol`
:   The protocol to use with this connection. This is the name of the protocol
    that should be sent to guacd when connecting, for example “`vnc`” or
    “`rdp`”.

`parent_id`
:   The unique integer associated with the connection group containing this
    connection, or `NULL` if this connection is within the root group.

`max_connections`
:   The maximum number of concurrent connections to allow to this connection
    at any one time *regardless of user*. `NULL` will use the default value
    specified in `guacamole.properties` and a value of `0` denotes unlimited.

`max_connections_per_user`
:   The maximum number of concurrent connections to allow to this connection  
    at any one time *from a single user*. `NULL` will use the default value  
    specified in `guacamole.properties` and a value of `0` denotes unlimited.

`proxy_hostname`
:   The hostname or IP address of the Guacamole proxy daemon (guacd) which
    should be used for this connection. If `NULL`, the value defined with the
    `guacd-hostname` property in `guacamole.properties` will be used.

`proxy_port`
:   The TCP port number of the Guacamole proxy daemon (guacd) which should be
    used for this connection. If `NULL`, the value defined with the
    `guacd-port` property in `guacamole.properties` will be used.

`proxy_encryption_method`
:   The encryption method which should be used when communicating with the
    Guacamole proxy daemon (guacd) for this connection. This can be either
    `NONE`, for no encryption, or `SSL`, for SSL/TLS. If `NULL`, the
    encryption method will be dictated by the `guacd-ssl` property in
    `guacamole.properties`.

`connection_weight`
:   The weight for a connection, used for applying weighted load balancing
    algorithms when connections are part of a `BALANCING` group. This is an
    integer value, where values `1` or greater will weight the connection
    relative to other connections in that group, and values below `1` cause
    the connection to be disabled in the group. If `NULL`, the connection will
    be assigned a default weight of `1`.

`failover_only`
:   Whether this connection should be used for failover situations only, also
    known as a “hot spare”. If this column is set to `TRUE` or `1`, this
    connection will be used only when another connection within the same
    `BALANCING` connection group has failed due to an error within the remote
    desktop.

    *Connection groups will always transparently switch to the next available
    connection in the event of remote desktop failure, regardless of the value
    of this column.* This column simply dictates whether a particular
    connection should be *reserved* for such situations, and left unused
    otherwise.

    This column only has an effect on connections within `BALANCING` groups.

As there are potentially multiple parameters per connection, where the names of
each parameter are completely arbitrary and determined only by the protocol in
use, every parameter for a given connection has an entry in table
`guacamole_connection_parameter` table associated with its corresponding
connection. This table contains the following columns:

`connection_id`
:   The `connection_id` value from the connection this parameter is for.

`parameter_name`
:   The name of the parameter to set. This is the name listed in the
    documentation for the protocol specified in the associated connection.

`parameter_value`
:   The value to assign to the parameter named. While this value is an
    arbitrary string, it must conform to the requirements of the protocol as
    documented for the connection to be successful.

Adding a connection and corresponding parameters is relatively easy compared to
adding a user as there is no salt to generate nor password to hash:

```
-- Create connection
INSERT INTO guacamole_connection (connection_name, protocol) VALUES ('test', 'vnc');

-- Determine the connection_id
SELECT * FROM guacamole_connection WHERE connection_name = 'test' AND parent_id IS NULL;

-- Add parameters to the new connection
INSERT INTO guacamole_connection_parameter VALUES (1, 'hostname', 'localhost');
INSERT INTO guacamole_connection_parameter VALUES (1, 'port', '5901');
```

### Usage history[#](#usage-history "Link to this heading")

When a connection is initiated or terminated, a corresponding entry in the
`guacamole_connection_history` table is created or updated respectively. Each
entry is associated with the user using the connection, the connection itself,
the [sharing profile](#jdbc-auth-schema-sharing-profiles) in use (if the
connection is being shared), and the time the connection started. If the
connection has ended, the end time is also stored.

It is very unlikely that a user will need to update this table, but knowing the
structure is potentially useful if you wish to generate a report of Guacamole
usage. The `guacamole_connection_history` table has the following columns:

`history_id`
:   The unique integer associated with each history record. This value is
    generated automatically when a new entry is inserted into the
    `guacamole_connection_history` table.

`user_id`
:   The value of the `user_id` from the entry in `guacamole_user` associated
    with the user using the connection. If the user no longer exists, this
    will be `NULL`.

`username`
:   The username associated with the user at the time that they used the
    connection. This username value is not guaranteed to uniquely identify a
    user, as the original user may be subsequently renamed or deleted.

`connection_id`
:   The value of the `connection_id` from the entry in `guacamole_connection`
    associated the connection being used. If the connection associated with
    the history record no longer exists, this will be `NULL`.

`connection_name`
:   The name associated with the connection at the time that it was used.

`sharing_profile_id`
:   The value of the `sharing_profile_id` from the entry in
    `guacamole_sharing_profile` associated the sharing profile being used to
    access the connection. If the connection is not being shared (no sharing
    profile is being used), or if the sharing profile associated with the
    history record no longer exists, this will be `NULL`.

`sharing_profile_name`
:   The name associated with the sharing profile being used to access the
    connection at the time this history entry was recorded. If the connection
    is not being shared, this will be `NULL`.

`start_date`
:   The time at which the connection was started by the user specified.
    Despite its name, this column also stores time information in addition to
    the date.

`end_date`
:   The time at which the connection ended. If the connection is still active,
    the value in this column will be `NULL`. Despite its name, this column
    also stores time information in addition to the date.

## Sharing profiles and parameters[#](#sharing-profiles-and-parameters "Link to this heading")

Each sharing profile has an entry in the `guacamole_sharing_profile` table,
with a one-to-many relationship to parameters, stored as name/value pairs in
the `guacamole_sharing_profile_parameter` table.

The `guacamole_sharing_profile` table is simply a pairing of a unique and
descriptive name with the connection that can be shared using the sharing
profile, also known as the “primary connection”. It contains the following
columns:

`sharing_profile_id`
:   The unique integer associated with each sharing profile. This value is
    generated automatically when a new entry is inserted into the
    `guacamole_sharing_profile` table.

`sharing_profile_name`
:   The unique name associated with each sharing profile. This value must be
    specified manually, and must be different from any existing sharing
    profile name associated with the same primary connection. References to
    sharing profiles in other tables use the value from `sharing_profile_id`,
    not `sharing_profile_name`.

`primary_connection_id`
:   The unique integer associated with the primary connection. The “primary
    connection” is the connection which can be shared using this sharing
    profile.

As there are potentially multiple parameters per sharing profile, where the
names of each parameter are completely arbitrary and determined only by the
protocol associated with the primary connection, every parameter for a given
sharing profile has an entry in the `guacamole_sharing_profile_parameter` table
associated with its corresponding sharing profile. This table contains the
following columns:

`sharing_profile_id`
:   The `sharing_profile_id` value from the entry in the
    `guacamole_sharing_profile` table for the sharing profile this parameter
    applies to.

`parameter_name`
:   The name of the parameter to set. This is the name listed in the
    documentation for the protocol of the primary connection of the associated
    sharing profile.

`parameter_value`
:   The value to assign to the parameter named. While this value is an
    arbitrary string, it must conform to the requirements of the protocol as
    documented.

## Connection groups[#](#connection-groups "Link to this heading")

Each connection group has an entry in the `guacamole_connection_group` table,
with a one-to-many relationship to other groups and connections.

The `guacamole_connection_group` table is simply a pairing of a unique and
descriptive name with a group type, which can be either `ORGANIZATIONAL` or
`BALANCING`. It contains the following columns:

`connection_group_id`
:   The unique integer associated with each connection group. This value is
    generated automatically when a new entry is inserted into the
    `guacamole_connection_group` table.

`connection_group_name`
:   The unique name associated with each connection group. This value must be
    specified manually, and must be different from any existing connection
    group name in the same connection group. References to connections in
    other tables use the value from `connection_group_id`, not
    `connection_group_name`.

`type`
:   The type of this connection group. This can be either `ORGANIZATIONAL` or
    `BALANCING`.

`parent_id`
:   The unique integer associated with the connection group containing this
    connection group, or `NULL` if this connection group is within the root
    group.

`max_connections`
:   The maximum number of concurrent connections to allow to this connection
    group at any one time *regardless of user*. `NULL` will use the default
    value specified in `guacamole.properties` and a value of `0` denotes
    unlimited. This only has an effect on `BALANCING` groups.

`max_connections_per_user`
:   The maximum number of concurrent connections to allow to this connection
    group at any one time *from a single user*. `NULL` will use the default
    value specified in `guacamole.properties` and a value of `0` denotes
    unlimited. This only has an effect on `BALANCING` groups.

`enable_session_affinity`
:   Whether session affinity should apply to this connection group. If this
    column is set to `TRUE` or `1`, users will be consistently routed to the
    same underlying connection until they log out. The normal balancing
    behavior will only apply for each user’s first connection attempt during
    any one Guacamole session. By default, session affinity is not enabled,
    and connections will always be balanced across the entire connection
    group. This only has an effect on `BALANCING` groups.

Adding a connection group is even simpler than adding a new connection as there
are no associated parameters stored in a separate table:

```
-- Create connection group
INSERT INTO guacamole_connection_group (connection_group_name, type)
     VALUES ('test', 'ORGANIZATIONAL');
```

## Permissions[#](#permissions "Link to this heading")

There are several permissions tables in the schema which correspond to the
types of permissions in Guacamole’s authentication model: system permissions,
which control operations that affect the system as a whole, and permissions
which control operations that affect specific objects within the system, such
as users, connections, or groups.

### System permissions[#](#system-permissions "Link to this heading")

System permissions are defined by entries in the `guacamole_system_permission`
table. Each entry grants permission for a specific user or user group to
perform a specific system operation.

The `guacamole_system_permission` table contains the following columns:

`entity_id`
:   The value of the `entity_id` column of the entry associated with the user
    or user group owning this permission.

`permission`
:   The permission being granted. This column can have one of seven possible
    values:

    * `ADMINISTER`, which grants the ability to administer the entire
      system (essentially a wildcard permission).
    * `AUDIT`, which allows a user to see login records and connection
      history across the entire system.
    * `CREATE_CONNECTION`, which grants the ability to create connections.
    * `CREATE_CONNECTION_GROUP`, which grants the ability to create connections
      groups.
    * `CREATE_SHARING_PROFILE`, which grants the ability to create sharing
      profiles.
    * `CREATE_USER`, which grants the ability to create users.
    * `CREATE_USER_GROUP`, which grants the ability to create user groups.

### User permissions[#](#user-permissions "Link to this heading")

User permissions are defined by entries in the `guacamole_user_permission`
table. Each entry grants permission for a specific user or user group to
perform a specific operation on an existing user.

The `guacamole_user_permission` table contains the following columns:

`entity_id`
:   The value of the `entity_id` column of the entry associated with the user
    or user group owning this permission.

`affected_user_id`
:   The value of the `user_id` column of the entry associated with the user
    *affected* by this permission. This is the user that would be the object
    of the operation represented by this permission.

`permission`
:   The permission being granted. This column can have one of four possible
    values: `ADMINISTER`, which grants the ability to add or remove
    permissions which affect the user, `READ`, which grants the ability to
    read data associated with the user, `UPDATE`, which grants the ability to
    update data associated with the user, or `DELETE`, which grants the
    ability to delete the user.

### User group permissions[#](#user-group-permissions "Link to this heading")

User group permissions are defined by entries in the
`guacamole_user_group_permission` table. Each entry grants permission for a
specific user or user group to perform a specific operation on an existing user
group.

The `guacamole_user_group_permission` table contains the following columns:

`entity_id`
:   The value of the `entity_id` column of the entry associated with the user
    or user group owning this permission.

`affected_user_group_id`
:   The value of the `user_group_id` column of the entry associated with the
    user group *affected* by this permission. This is the user group that
    would be the object of the operation represented by this permission.

`permission`
:   The permission being granted. This column can have one of four possible
    values: `ADMINISTER`, which grants the ability to add or remove
    permissions which affect the user group, `READ`, which grants the ability
    to read data associated with the user group, `UPDATE`, which grants the
    ability to update data associated with the user group, or `DELETE`, which
    grants the ability to delete the user group.

### Connection permissions[#](#connection-permissions "Link to this heading")

Connection permissions are defined by entries in the
`guacamole_connection_permission` table. Each entry grants permission for a
specific user or user group to perform a specific operation on an existing
connection.

The `guacamole_connection_permission` table contains the following columns:

`entity_id`
:   The value of the `entity_id` column of the entry associated with the user
    or user group owning this permission.

`connection_id`
:   The value of the `connection_id` column of the entry associated with the
    connection affected by this permission. This is the connection that would
    be the object of the operation represented by this permission.

`permission`
:   The permission being granted. This column can have one of four possible
    values: `ADMINISTER`, which grants the ability to add or remove
    permissions which affect the connection, `READ`, which grants the ability
    to read data associated with the connection (a prerequisite for
    connecting), `UPDATE`, which grants the ability to update data associated
    with the connection, or `DELETE`, which grants the ability to delete the
    connection.

### Sharing profile permissions[#](#sharing-profile-permissions "Link to this heading")

Sharing profile permissions are defined by entries in the
`guacamole_sharing_profile_permission` table. Each entry grants permission for
a specific user or user group to perform a specific operation on an existing
sharing profile.

The `guacamole_sharing_profile_permission` table contains the following
columns:

`entity_id`
:   The value of the `entity_id` column of the entry associated with the user
    or user group owning this permission.

`sharing_profile_id`
:   The value of the `sharing_profile_id` column of the entry associated with
    the sharing profile affected by this permission. This is the sharing
    profile that would be the object of the operation represented by this
    permission.

`permission`
:   The permission being granted. This column can have one of four possible
    values: `ADMINISTER`, which grants the ability to add or remove
    permissions which affect the sharing profile, `READ`, which grants the
    ability to read data associated with the sharing profile (a prerequisite
    for using the sharing profile to share an active connection), `UPDATE`,
    which grants the ability to update data associated with the sharing
    profile, or `DELETE`, which grants the ability to delete the sharing
    profile.

### Connection group permissions[#](#connection-group-permissions "Link to this heading")

Connection group permissions are defined by entries in the
`guacamole_connection_group_permission` table. Each entry grants permission for
a specific user or user group to perform a specific operation on an existing
connection group.

The `guacamole_connection_group_permission` table contains the following
columns:

`entity_id`
:   The value of the `entity_id` column of the entry associated with the user
    or user group owning this permission.

`connection_group_id`
:   The value of the `connection_group_id` column of the entry associated with
    the connection group affected by this permission. This is the connection
    group that would be the object of the operation represented by this
    permission.

`permission`
:   The permission being granted. This column can have one of four possible
    values: `ADMINISTER`, which grants the ability to add or remove
    permissions which affect the connection group, `READ`, which grants the
    ability to read data associated with the connection group, `UPDATE`, which
    grants the ability to update data associated with the connection group, or
    `DELETE`, which grants the ability to delete the connection group (and
    implicitly its contents).

Contents

---
# Creating ad-hoc connections

## Contents

# Creating ad-hoc connections[#](#creating-ad-hoc-connections "Link to this heading")

The quickconnect extension provides a connection bar on the Guacamole Client
home page that allows users to type in the URI of a server to which they want
to connect and the client will parse the URI and immediately establish the
connection. The purpose of the extension is to allow situations where
administrators want to allow users the flexibility of establishing their own
connections without having to grant them access to edit connections or even to
have to create the connections at all, aside from typing the URI.

Important

There are several implications of using this extension that should be
well-understood by administrators prior to implementing it:

* Connections established with this extension are created in-memory and only
  persist until the Guacamole session ends.
* Connections created with this extension are not accessible to other users,
  and cannot be shared with other users.
* This extension provides no functionality for authenticating users - it does
  not allow anonymous logins, and requires that users are successfully
  authenticated by another authentication module before it can be used.
* The extension provides users the ability not only to establish connections,
  but also to set any of the parameters for a connection. There are security
  implications for this - for example, RDP file sharing can be used to pass
  through any directory available on the server running guacd to the remote
  desktop. This should be taken into consideration when enabling this extension
  and making sure that guacd is configured in a way that does not compromise
  sensitive system files by allowing access to them.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling the quickconnect extension[#](#installing-enabling-the-quickconnect-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-quickconnect-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-quickconnect-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-quickconnect-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `QUICKCONNECT_ENABLED` environment variable:

    ```
    QUICKCONNECT_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e QUICKCONNECT_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `QUICKCONNECT_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `QUICKCONNECT_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Configuration (optional)[#](#configuration-optional "Link to this heading")

Native Webapp (Tomcat)

This extension has no required properties. So long as you are satisfied
with the default behavior/values noted below, this extension requires no
configuration beyond installation.

`quickconnect-allowed-parameters`
:   An optional list of parameters that are allowed to be used by connections
    that are created and accessed via the quickconnect extension. If provided,
    only parameters in this list will be allowed.

`quickconnect-denied-parameters`
:   An optional list of parameters that are explicitly denied from being used by
    connections created and accessed via the quickconnect extension. If provided,
    any parameters in this list will be removed from the connection configuration
    when it is created, **even if those parameters are otherwise explicitly
    listed as allowed**.

Container (Docker)

This extension has no required environment variables. So long as you are satisfied
with the default behavior/values noted below, this extension requires no
configuration beyond installation.

`QUICKCONNECT_ALLOWED_PARAMETERS`
:   An optional list of parameters that are allowed to be used by connections
    that are created and accessed via the quickconnect extension. If provided,
    only parameters in this list will be allowed.

`QUICKCONNECT_DENIED_PARAMETERS`
:   An optional list of parameters that are explicitly denied from being used by
    connections created and accessed via the quickconnect extension. If provided,
    any parameters in this list will be removed from the connection configuration
    when it is created, **even if those parameters are otherwise explicitly
    listed as allowed**.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Using the quickconnect extension[#](#using-the-quickconnect-extension "Link to this heading")

The quickconnect extension provides a field on the home page that allows you to
enter a Uniform Resource Identifier (URI) to create a connection. A URI is in
the form:

`protocol://username:password@host:port/?parameters`

The `protocol` field can have any of the protocols supported by Guacamole, as
documented in [Configuring Guacamole](configuring-guacamole.html). Many of the protocols define a default
`port` value, with the exception of VNC. The `parameters` field can specify any
of the protocol-specific parameters as documented on the configuration page.

To establish a connection, simply type in a valid URI and either press “Enter”
or click the connect button. This extension will parse the URI and create a new
connection, and immediately start that connection in the current browser.

Here are a few examples of URIs:

`ssh://linux1.example.com/`
:   Connect to the server linux1.example.com using the SSH protocol on the
    default SSH port (22). This will result in prompting for both username and
    password.

`vnc://linux1.example.com:5900/`
:   Connect to the server linux1.example.com using the VNC protocol and
    specifying the port as 5900.

`rdp://localuser@windows1.example.com/?security=rdp&ignore-cert=true&disable-audio=true&enable-drive=true&drive-path=/mnt/usb`
:   Connect to the server windows1.example.com using the RDP protocol and the
    user “localuser”. This URI also specifies several RDP-specific parameters on
    the connection, including forcing security mode to RDP (security=rdp), ignoring
    any certificate errors (ignore-cert=true), disabling audio pass-through
    (disable-audio=true), and enabling filesystem redirection (enable-drive=true)
    to the /mnt/usb folder on the system running guacd (drive-path=/mnt/usb).

Contents

---
# Enforcing advanced login and connection restrictions

## Contents

# Enforcing advanced login and connection restrictions[#](#enforcing-advanced-login-and-connection-restrictions "Link to this heading")

A feature of Guacamole as of version 1.6.0 is an extension that allows you to
enforce advanced restrictions on both user logins to Guacamole as well as the
use of connections and connection groups. The extension,
`guacamole-auth-restrict`, decorates other authentication extensions that
contain user, group and/or connection information, and allows you to apply
restrictions to those objects for the time(s) that users are allowed to log
in, the hosts from which users may log in, the time(s) that certain
connections and balancing connection groups may be used, and the hosts from
which certain connections and balancing connection groups may be used. The
goal is to give administrators of a Guacamole system additional flexibility in
restricting when and from where various parts of the system may be used.

As this extension decorates underlying extensions, it must be used alongside
one that is capable of storing additional information for users, user groups,
connections, and connection groups. Currently the only extension provided
by the Guacamole project that is capable of doing this is the
[JDBC authentication extension](jdbc-auth.html).

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling support for advanced restrictions[#](#installing-enabling-support-for-advanced-restrictions "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-restrict-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-restrict-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-restrict-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `RESTRICT_ENABLED` environment variable:

    ```
    RESTRICT_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e RESTRICT_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `RESTRICT_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `RESTRICT_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Using advanced restrictions[#](#using-advanced-restrictions "Link to this heading")

Once the extension is installed and the web application restarted, an additional
section of options will appear in the administrative pages of Guacamole that
will allow administrators to configure the additional restrictions for various
objects within the Guacamole system. The new section of options looks like this:

![](assets/doc_gug__images_auth-restrict-options.png)

The next sections will cover how each restriction impacts the availability of
various objects in the system.

### User Logins[#](#user-logins "Link to this heading")

Additional settings can be applied to users and user groups that will restrict
the ability of those individual users or members of the groups to log in to
Guacamole.

#### Restricting logins based on day and time[#](#restricting-logins-based-on-day-and-time "Link to this heading")

This extension introduces the ability to restrict logins to the Guacamole
system based on the day of the week and the time of day, and to combine these
restrictions in a way that allows for flexibility in those schedules.

As an example, let’s say that you have a user or group of users whose access
you’d like to restrict to your normal working hours of 9 AM to 5 PM, any day
of the week. You would add a restriction like so:

![](assets/doc_gug__images_auth-restrict-login-business-hours.png)

However, you’ll notice that this includes all days of the week, so perhaps
you’d like to limit it to only your normal work-week, which happens to be
Monday through Friday:

![](assets/doc_gug__images_auth-restrict-login-work-week.png)

In the above image, you can see that we allow 9 to 5 every day of the week, but
then we specifically prohibit logins on Saturday and Sunday, all day, in order
to prevent the weekend logins.

These basic examples demonstrate the ways in which you can combine the allowed
and denied login times to create a schedule that supports your use case. There
is [more discussion below](#how-restrictions-are-processed) on the order in which
rules are processed and which takes precedence.

If a user attempts to log in at a time not allowed by the time-based
restrictions that apply to that user, an error will be displayed on the login
page:

![](assets/doc_gug__images_auth-restrict-login-failed-time.png)

##### A note about timezones[#](#a-note-about-timezones "Link to this heading")

Creating restrictions that involve day and time can be tricky when factoring
in the timezones of users, particulary if you have users spread out around
the world. This extension stores the restrictions in UTC, translating them
from the local timezone of the administrator. When administering these
restrictions it is important to keep in mind how those restrictions will
actually impact users.

Consider the following example that may help to clarify how this works in
practice:

* An administrator is located in the US Eastern timezone (EDT, UTC - 4).
* A user is located in the Central European timezone (CEST, UTC + 2).
* The administrator creates a restriction for the user limiting the ability of
  the user to log in between 09:00 AM and 05:00 PM every day.
* This restriction is stored in the database to allow logins every day between
  01:00 PM and 09:00 PM UTC.
* The user in the Central European timezone would actually be allowed to log in
  between 03:00 PM and 11:00 PM.

This is likely not the behavior that you want, so the restrictions entered for
the users - and connections - should be done with consideration for where the
users are located and how it will actually apply to those users.

This is further complicated by Daylight Savings Time, which is still observed
in a large portion of the world. As the database stores the restrictions in
UTC, a restriction entered by an administrator in the US Eastern Timezone
during Daylight Savings Time (Summer Time) for 09:00 AM to 05:00 PM will
shift back an hour in the non-DST period, and actually apply from 08:00 AM to
04:00 PM.

#### Restricting logins based on host[#](#restricting-logins-based-on-host "Link to this heading")

The ability to restrict logins based on the client from which a user is
attempting to log in is also provided by this extension. The fields for storing
these hosts can be filled in using three possible formats for the host:
resolveable host names, IP addresses, and/or subnets in IP CIDR notation. The
IP addresses and subnets may be either IPv4 or IPv6.

Warning

If you will be configuring Guacamole to consider users’ IP addresses, **it is
important to make sure that Guacamole is receiving correct IP address
information for all clients**.

If Guacamole is behind a reverse proxy, such as for SSL termination, the IP
addresses of all users will appear to be the IP address of the proxy unless
additional configuration steps are taken. **Be sure to follow [the
documentation for configuring forwarding of client IP
information](reverse-proxy.html)!**

Important

If you use hostnames in this field, the system running Guacamole Client MUST be
able to resolve those hostnames back to IP addresses in order to verify if the
IP address from which the user is logging in is allowed. If a hostname is
entered into either the allow or deny field, and Guacamole cannot resolve the
hostname, it will deny the login, unless it can match the user’s IP address to
some other entry in one of the lists. Thus it is very important that, if you use
hostnames, you make sure that the ability of the Guacamole system to resolve
those hostnames is consistent.

As an example, suppose that you have a group of users that you’d like to
restrict logins such that they can only log in from a specific internal
subnet - let’s say 192.168.123.0/24. You would simply put that subnet in the
allowed hosts box, and Guacamole would allow access for users to log in from IP
addresses within that subnet, but block access from all other subnets:

![](assets/doc_gug__images_auth-restrict-login-local-subnet.png)

However, let’s say that you have a router on that subnet, 192.168.123.1, and
you’d like to make sure that a user attempting to log in from a client that
appears to be coming from that router will always be denied. You can do this
like so:

![](assets/doc_gug__images_auth-restrict-login-block-router.png)

Again, as we’ll discuss [later on](#how-restrictions-are-processed), it’s
important to understand the order in which these restrictions are processed.

If a user attempts to log in from a client that is not allowed by the
host-based restrictions applied to that user, an error will be displayed
on the login page:

![](assets/doc_gug__images_auth-restrict-login-failed-host.png)

#### Users and User Groups[#](#users-and-user-groups "Link to this heading")

As has been alluded to a few times, these additional login restrictions can be
applied either to individual users, or, perhaps more helpfully, to entire
groups of users. While the
[processing order of the rules themselves](#how-restrictions-are-processed) is
important, we’ll take a moment to note, now, how restrictions work when used on
users and user groups.

First, if restrictions are applied to both users and a user group of which
that user is a member, then the restrictions placed on the user will take
precedence over those on the user group. For example, if you deny login at a
certain time to a user group, but add a rule to a member of that group to
allow logins at a time that overlaps with the deny time of the group, the login
will be allowed. Conversely, if you’ve allowed logins for a group at a
particular time, but you’ve denied a login for a specific user who is a member
of that group at a given time, the login will be denied. Similar logic applies
to the host rules that govern a user’s ability to log in.

Second, Guacamole attempts to pull all effective user groups of which a user is
a member and process the restrictions across all of those groups. This
includes nested groups, as well. The caution, here, is to be aware of what
groups you’re applying rules on and how those groups relate - if you rely on
complex group nesting within your Guacamole installation, you can end up with
very complex restriction scenarios that make it difficult to sort out when a
user can log in and when they cannot. Keeping your group nesting as simple as
possible will help avoid these situations.

### Connections and Connection Groups[#](#connections-and-connection-groups "Link to this heading")

This extension allows for the restricting the use of specific connections and/or
connection groups (of the balancing variety) based on the same criteria by
which you can restrict user logins - day/time of week and/or client address.

The examples given above for user logins can be slightly updated to see some
use-cases for connections. You might host an application through Guacamole that
you’d like to make sure is only available during your normal business hours.
Or, perhaps you have a balancing connection group that you want to make sure
is only used by users who are logging in from a certain subnet within your
firewall, and not from any public Internet clients. The user interface for
these restrictions for Connections and Connection Groups is identical to the
interface shown above for Users and User Groups.

If a restriction applies to a Connection or Connection Group that results
in access being denied to a connection, the user will receive an error
indicating that they do not have access to the connection:

![](assets/doc_gug__images_auth-restrict-connection-failed.png)

### How Restrictions are Processed[#](#how-restrictions-are-processed "Link to this heading")

When dealing with restrictions that add this level of complexity - multiple
time schedules, user and user groups, and IP addresses and subnets - it’s
important to understand how the system interprets these restrictions, how
they relate to one another, and the order in which these restrictions are
processed.

Here are a few key items to keep in mind:

* System administrators are exempt from login restriction rules. If you apply
  restrictions to either a specific user or a group, but a user who is a
  system administrator attempts to log in, the restrictions will be bypassed
  and a warning will be logged to the Guacamole log file.

  However, restrictions applied to Connection and Connection Group objects
  will apply to anyone who tries to connect, regardless of their status
  as an administrator of the system or the individual connection.
* When no additional restrictions are present, the login or connection is
  implicitly allowed.
* If only “allow” rules are added, the login or connection is implicitly
  denied if those rules are not met. For example, if a rule is added to a user
  group allowing logins between 09:00 AM and 05:00 PM, users who are members
  of that group will be allowed during that time, but denied at any other
  time, regardless of the fact that a deny rule has not been created.
* If only “deny” rules are added, the login or connection is implicitly
  allowed if those rules are not met. For example, if you add a rule to a
  connection to deny access between 06:00 PM and 12:00 AM, access to that
  connection will be allowed at any time that falls outside of the specified
  deny rule.
* Deny rules always take precedence over allow rules when there is an overlap.
  If you create a time-based login restriction that allows logins at a given
  time, and another restriction that denies logins at a certain time and these
  times overlap, the login will be denied at any time that the Deny rule
  applies, regardless of whether or not the allow rule also applies.

  Similarly, when working with the host-based restrictions, if you allow
  access to a certain IP address, but deny access to a subnet of which that IP
  address is a member, the login (or connection) will be denied.
* As mentioned above, individual user rules are processed before, and thus take
  precedence over, user group rules. If a user is explicitly allowed or denied,
  that rule will apply regardless of whether a rule on a group of which that
  user is a member would apply.
* Time-based restrictions are processed prior to host-based restrictions, but
  both will be taken into account. If a user is configured to be allowed at a
  certain time, but denied from a certain host, the login will be allowed if
  both rules allow it and denied if either the time or host rule denies it.
  The order, here, is only an issue in noting what error message the user may
  receive during login or connection attempt - if both a time restriction and
  a host restriction deny the action, then the error the user receives will
  note the time restriction.

Contents

---
# Event listeners

## Contents

# Event listeners[#](#event-listeners "Link to this heading")

Guacamole supports the delivery of event notifications to custom extensions.
Developers can use listener extensions to integrate custom handling of events
such as successful and failed authentications, and requests to connect and
disconnect tunnels to desktop environments.

A listener extension could be used, for example, to record authentication
attempts in an external database for security auditing or alerting. By
listening to tunnel lifecycle events, a listener extension could be used to
help coordinate startup and shutdown of machine resources; particularly useful
in cloud environments where minimizing running-but-idle resources is an
important cost savings measure.

For certain *vetoable* events, an event listener can even influence Guacamole’s
behavior. For example, a listener can veto a successful authentication,
effectively causing the authentication to be considered failed. Similarly, a
listener can veto a tunnel connection, effectively preventing the tunnel from
being connected to a virtual desktop resource.

Custom event listeners are packaged using the same extension mechanism used for
custom authentication providers. A single listener extension can include any
number of classes that implement the listener interface. A single extension
module can also include any combination of authentication providers and
listeners, so developers can easily combine authentication providers with
listeners designed to support them.

To demonstrate the principles involved in receiving Guacamole event
notifications, we will implement a simple listener extension that logs
authentication events. While our approach simply writes event details to the
same log used by the Guacamole web application, a listener could process these
events in arbitrary ways, limited only by the imagination and ingenuity of the
developer.

## A Guacamole listener extension skeleton[#](#a-guacamole-listener-extension-skeleton "Link to this heading")

For simplicity’s sake, and because this is how things are done upstream in the
Guacamole project, we will use Maven to build our extension.

The bare minimum required for a Guacamole listener extension is a `pom.xml`
file listing guacamole-ext as a dependency, a single `.java` file implementing
our stub of a listener, and a `guac-manifest.json` file describing the
extension and pointing to our listener class.

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                        http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>org.apache.guacamole</groupId>
    <artifactId>guacamole-listener-tutorial</artifactId>
    <packaging>jar</packaging>
    <version>1.6.0</version>
    <name>guacamole-listener-tutorial</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>

            <!-- Written for Java 8 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.3</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>

        </plugins>
    </build>

    <dependencies>

        <!-- Guacamole Extension API -->
        <dependency>
            <groupId>org.apache.guacamole</groupId>
            <artifactId>guacamole-ext</artifactId>
            <version>1.6.0</version>
            <scope>provided</scope>
        </dependency>

        <!-- Slf4j API -->
        <!-- This is needed only if your listener wants to 
                write to the Guacamole web application log -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.7</version>
            <scope>provided</scope>
        </dependency>

    </dependencies>

</project>
```

Naturally, we need the actual listener extension skeleton code. While you can
put this in whatever file and package you want, for the sake of this tutorial,
we will assume you are using `org.apache.guacamole.event.TutorialListener`.

For now, we won’t actually do anything other than log the fact that an event
notification was received. At this point, we’re just creating the skeleton for
our listener extension.

```
package org.apache.guacamole.event;

import org.apache.guacamole.GuacamoleException;
import org.apache.guacamole.net.event.listener.Listener;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * A Listener implementation intended to demonstrate basic use
 * of Guacamole's listener extension API.
 */
public class TutorialListener implements Listener {

    private static final Logger logger = 
         LoggerFactory.getLogger(TutorialListener.class);

    @Override
    public void handleEvent(Object event) throws GuacamoleException {
        logger.info("received Guacamole event notification");
    }

}
```

To conform with Maven, this skeleton file must be placed within
`src/main/java/org/apache/guacamole/event` as `TutorialListener.java`.

As you can see, implementing a listener is quite simple. There is a single
`Listener` interface to implement. All Guacamole event notifications will be
delivered to your code by invoking the handleEvent method. We will see shortly
how to use the passed event object to get the details of the event itself.

The only remaining piece for the overall skeleton to be complete is a
`guac-manifest.json` file. *This file is absolutely required for all Guacamole
extensions.* The `guac-manifest.json` format is described in more detail in
[guacamole-ext](guacamole-ext.html). It provides for quite a few properties, but for our listener
extension we are mainly interested in the Guacamole version sanity check (to
make sure an extension built for the API of Guacamole version X is not
accidentally used against version Y) and telling Guacamole where to find our
listener class.

The Guacamole extension format requires that `guac-manifest.json` be placed in
the root directory of the extension `.jar` file. To accomplish this with Maven,
we place it within the `src/main/resources` directory. Maven will automatically
pick it up during the build and include it within the `.jar`.

```
{

    "guacamoleVersion" : "1.6.0",

    "name"      : "Tutorial Listener Extension",
    "namespace" : "guac-listener-tutorial",

    "listeners" : [
        "org.apache.guacamole.event.TutorialListener"
    ]

}
```

## Building the extension[#](#building-the-extension "Link to this heading")

Once all three of the above files are in place, the extension should build
successfully even though it is just a skeleton at this point.

```
$ mvn package
[INFO] Scanning for projects...
[INFO] ---------------------------------------------------------------
[INFO] Building guacamole-listener-tutorial 1.6.0
[INFO] ---------------------------------------------------------------
...
[INFO] ---------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ---------------------------------------------------------------
[INFO] Total time: 1.297 s
[INFO] Finished at: 2017-10-08T13:12:39-04:00
[INFO] Final Memory: 19M/306M
[INFO] ---------------------------------------------------------------
$
```

Assuming you see the “`BUILD SUCCESS`” message when you build the extension,
there will be a new file, `target/guacamole-listener-tutorial-1.6.0.jar`, which
can be installed within Guacamole (see [Installing the extension](#custom-listener-installing) at the
end of this chapter). It should log event notifications that occur during, for
example, authentication attempts. If you changed the name or version of the
project in the `pom.xml` file, the name of this new `.jar` file will be
different, but it can still be found within `target/`.

## Handling events[#](#handling-events "Link to this heading")

The Guacamole `Listener` interface represents a low-level event handling API. A
listener is notified of every event generated by Guacamole. The listener must
examine the event type to determine whether the event is of interest, and if so
to dispatch the event to the appropriate entry point.

The event types that can be produced by Guacamole are described in the
`org.apache.guacamole.net.event` package of the guacamole-ext API. In this
package you will find several concrete event types as well as interfaces that
describe common characteristics of certain of event types. You can use any of
these types to distinguish the events received by your listener, and to examine
properties of an event of a given type.

Suppose we wish to log authentication success and failure events, while
ignoring all other event types. The `AuthenticationSuccessEvent` and
`AuthenticationFailureEvent` types are used to notify a listener of
authentication events. We can simply check whether a received event is of one
of these types and, if so, log an appropriate message.

```
package org.apache.guacamole.event;

import org.apache.guacamole.GuacamoleException;
import org.apache.guacamole.net.event.AuthenticationFailureEvent;
import org.apache.guacamole.net.event.AuthenticationSuccessEvent;
import org.apache.guacamole.net.event.listener.Listener;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * A Listener that logs authentication success and failure events.
 */
public class TutorialListener implements Listener {

    private static final Logger logger = 
        LoggerFactory.getLogger(TutorialListener.class);

    @Override
    public void handleEvent(Object event) throws GuacamoleException {

        if (event instanceof AuthenticationSuccessEvent) {
            logger.info("successful authentication for user {}", 
                ((AuthenticationSuccessEvent) event)
                    .getCredentials().getUsername());
        }
        else if (event instanceof AuthenticationFailureEvent) {
            logger.info("failed authentication for user {}", 
                ((AuthenticationFailureEvent) event)
                    .getCredentials().getUsername());
        }
    }

}
```

In our example, we use `instanceof` to check for the two event types of
interest to our listener. Once we have identified an event of interest, we can
safely cast the event type to access properties of the event.

The extension is now complete and can be built as described earlier in
[Building the extension](#custom-listener-building) and installed as described below in
[Installing the extension](#custom-listener-installing).

## Influencing Guacamole by event veto[#](#influencing-guacamole-by-event-veto "Link to this heading")

An implementation of the handleEvent method is permitted to throw any
`GuacamoleException`. For certain *vetoable* event types, throwing a
`GuacamoleException` serves to effectively veto the action that resulted in the
event notification. See the API documentation for guacamole-ext to learn more
about vetoable event types.

As an (admittedly contrived) example, suppose we want to prevent a user named
“guacadmin” from accessing Guacamole. For whatever reason, we don’t wish to
remove or disable the auth database entry for this user. In this case we can
use a listener to block this user, preventing access to Guacamole. In the
listener, when we get an `AuthenticationSuccessEvent` we can check to see if
the user is “guacadmin” and, if so, throw an exception to prevent this user
from logging in to Guacamole.

```
package org.apache.guacamole.event;

import org.apache.guacamole.GuacamoleException;
import org.apache.guacamole.GuacamoleSecurityException;
import org.apache.guacamole.net.event.AuthenticationFailureEvent;
import org.apache.guacamole.net.event.AuthenticationSuccessEvent;
import org.apache.guacamole.net.event.listener.Listener;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * A Listener that logs authentication success and failure events
 * and prevents the "guacadmin" user from logging in by throwing
 * a GuacamoleSecurityException.
 */
public class TutorialListener implements Listener {

    private static final Logger logger = 
        LoggerFactory.getLogger(TutorialListener.class);

    @Override
    public void handleEvent(Object event) throws GuacamoleException {

        if (event instanceof AuthenticationSuccessEvent) {
          final String username = ((AuthenticationSuccessEvent) event)
              .getCredentials().getUsername();

          if ("guacadmin".equals(username)) {
            logger.warn("user {} has been blocked", username);
            throw new GuacamoleSecurityException(
                "User '" + username + "' is currently blocked");
          }

          logger.info("successful authentication for user {}", username);
        }
        else if (event instanceof AuthenticationFailureEvent) {
            logger.info("failed authentication for user {}", 
                ((AuthenticationFailureEvent) event)
                    .getCredentials().getUsername());
        }
    }

}
```

If our Guacamole user database contains a user named “guacadmin”, and we build
and install this listener extension, we will find that an attempt to log in as
this user now results in a message in the UI indicating that the user is
blocked. If we examine the Guacamole log, we will see the message indicating
that the user was blocked. Because the successful authentication was vetoed,
Guacamole sends a subsequent authentication failure notification, which we see
logged as well.

## Installing the extension[#](#installing-the-extension "Link to this heading")

Guacamole extensions are self-contained `.jar` files which are installed by
being placed within `GUACAMOLE_HOME/extensions`, and this extension is no
different. As described in [Configuring Guacamole](configuring-guacamole.html), `GUACAMOLE_HOME` is a
placeholder used to refer to the directory that Guacamole uses to locate its
configuration files and extensions. Typically, this will be the `.guacamole`
directory within the home directory of the user running Tomcat.

To install your extension, copy the
`target/guacamole-listener-tutorial-1.6.0.jar` file into
`GUACAMOLE_HOME/extensions` and restart Tomcat. Guacamole will automatically
load your extension, logging an informative message that it has done so:

```
Extension "Tutorial Listener Extension" loaded.
```

Contents

---
# LDAP authentication

## Contents

# LDAP authentication[#](#ldap-authentication "Link to this heading")

Guacamole supports LDAP authentication via an extension available from the main
project website. This extension allows users and connections to be stored
directly within an LDAP directory. If you have a centralized authentication
system that uses LDAP, Guacamole’s LDAP support can be a good way to allow your
users to use their existing usernames and passwords to log into Guacamole.

To use the LDAP authentication extension, you will need:

1. An LDAP directory as storage for all authentication data, such as OpenLDAP.
2. The ability to modify the schema of your LDAP directory.

The instructions here assume you already have an LDAP directory installed and
working, and do not cover the initial setup of such a directory.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## How Guacamole uses LDAP[#](#how-guacamole-uses-ldap "Link to this heading")

If the LDAP extension is installed, Guacamole will authenticate users against
your LDAP server by attempting a bind as that user. The given username and
password will be submitted to the LDAP server during the bind attempt.

If the bind attempt is successful, the set of available Guacamole connections,
users, and groups are queried from the LDAP directory by executing an LDAP
query **as the bound user**. Each Guacamole connection is represented within
the directory as a special type of group: `guacConfigGroup`. Attributes
associated with the group define the protocol and parameters of the connection,
and users are allowed access to the connection only if they are associated with
that group.

This architecture has a number of benefits:

1. Your users can use their existing usernames and passwords to log into
   Guacamole.
2. You can manage Guacamole connections using the same tool that you already
   use to manage your LDAP directory, such as [Apache Directory
   Studio](https://directory.apache.org/studio/).
3. Existing security restrictions can limit visibility/accessibility of
   Guacamole connections.
4. Access to connections can easily be granted and revoked, as each connection
   is represented by a group.

Important

Though Guacamole connections can be stored within the LDAP directory, this is
not required. Connection data can alternatively be stored within a database
like MySQL or PostgreSQL as long as the LDAP username matches the username of
the database user. Configuring Guacamole to use a database for authentication
or connection storage is covered in [Database authentication](jdbc-auth.html) and later in this chapter in
[Associating LDAP with a database (recommended)](#ldap-and-database).

## Intalling/Enabling the LDAP extension[#](#intalling-enabling-the-ldap-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-ldap-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-ldap-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-ldap-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `LDAP_ENABLED` environment variable:

    ```
    LDAP_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e LDAP_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `LDAP_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `LDAP_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Preparing your LDAP directory (optional)[#](#preparing-your-ldap-directory-optional "Link to this heading")

Although your LDAP directory already provides a means of storing and
authenticating users, Guacamole also needs storage of connection configuration
data, such as hostnames and ports, and a means of associating users with
connections that they should have access to. You can do this either through
modifying the LDAP directory schema, or through using a database like MySQL or
PostgreSQL. If you do not wish to use the LDAP directory for connection
storage, skip ahead to [Associating LDAP with a database (recommended)](#ldap-and-database).

If you wish to store connection data directly within the LDAP directory, the
required modifications to the LDAP schema are made through applying one of the
provided schema files. These schema files define an additional object class,
`guacConfigGroup`, which contains all configuration information for a
particular connection, and can be associated with arbitrarily-many users and
groups. Each connection defined by a `guacConfigGroup` will be accessible only
by users who are members of that group (specified with the member attribute),
or who are members of associated groups (specified with the `seeAlso`
attribute).

Important

The instructions given for applying the Guacamole LDAP schema changes are
specific to OpenLDAP, but other LDAP implementations, including Active
Directory, will have their own methods for updating the schema.

If you are not using OpenLDAP, a standards-compliant schema file is provided
that can be used to update the schema of any LDAP directory supporting
RFC-2252. Please consult the documentation of your LDAP directory to determine
how such schema changes can be applied.

The schema files are located within the `schema/` directory of the archive
containing the LDAP extension. You will only need one of these files:

`guacConfigGroup.schema`
:   A standards-compliant file describing the schema. This file can be used with
    any LDAP directory compliant with RFC-2252.

`guacConfigGroup.ldif`
:   An LDIF file compatible with OpenLDAP. This file was automatically built from
    the provided `.schema` file for convenience.

This chapter will cover applying `guacConfigGroup.ldif` to an OpenLDAP server.
If you are not using OpenLDAP, your LDAP server should provide documentation
for modifying its schema. If this is the case, please consult the documentation
of your LDAP server before proceeding.

### Applying the schema changes to OpenLDAP[#](#applying-the-schema-changes-to-openldap "Link to this heading")

Schema changes to OpenLDAP are applied using the **ldapadd** utility
with the provided `guacConfigGroup.ldif` file:

```
# ldapadd -Q -Y EXTERNAL -H ldapi:/// -f schema/guacConfigGroup.ldif
adding new entry "cn=guacConfigGroup,cn=schema,cn=config"

#
```

If the `guacConfigGroup` object was added successfully, you should see output
as above. You can confirm the presence of the new object class using
**ldapsearch**:

```
# ldapsearch -Q -LLL -Y EXTERNAL -H ldapi:/// -b cn=schema,cn=config dn
dn: cn=schema,cn=config

dn: cn={0}core,cn=schema,cn=config

dn: cn={1}cosine,cn=schema,cn=config

dn: cn={2}nis,cn=schema,cn=config

dn: cn={3}inetorgperson,cn=schema,cn=config

dn: cn={4}guacConfigGroup,cn=schema,cn=config

#
```

## Associating LDAP with a database (recommended)[#](#associating-ldap-with-a-database-recommended "Link to this heading")

If you install both the LDAP authentication as well as support for a database
(following the instructions in [Database authentication](jdbc-auth.html)), Guacamole will automatically
attempt to authenticate against both systems whenever a user attempts to log
in. In addition to any visible objects within the LDAP directory, that user
will have access to any data associated with their account in the database, as
well as any data associated with user groups that they belong to. LDAP user
accounts and groups will be considered equivalent to database users and groups
if their unique names are identical, as determined by the attributes given for
[the `ldap-username-attribute` and `ldap-group-name-attribute`
properties](#guac-ldap-config).

Data can be manually associated with LDAP user accounts or groups by creating
corresponding users or groups within the database which each have the same
names. As long as the names are identical, a successful login attempt against
LDAP will be trusted by the database authentication, and that user’s associated
data will be visible.

If an administrator account (such as the default `guacadmin` user provided with
the database authentication) has a corresponding user in the LDAP directory
with permission to read other LDAP users and groups, the Guacamole
administrative interface will include them in the lists presented to the
administrator, and will allow connections from the database to be associated
with those users or groups directly.

## Required configuration[#](#required-configuration "Link to this heading")

Native Webapp (Tomcat)

If deploying Guacamole natively, you will need to add a section to your
`guacamole.properties` that looks like the following:

```
ldap-user-base-dn: ou=people,dc=example,dc=net
```

The properties that must be set in all cases for any Guacamole installation
using this extension are:

`ldap-user-base-dn`
:   The base of the DN for all Guacamole users. *This property is absolutely
    required in all cases.* All Guacamole users must be descendents of this base
    DN.

    If a search DN is provided (via `ldap-search-bind-dn`), then Guacamole users
    need only be somewhere within the subtree of the specified user base DN.

    If a search DN *is not* provided, then all Guacamole users must be *direct
    descendents* of this base DN, as the base DN will be appended to the username
    to derive the user’s DN. For example, if `ldap-user-base-dn` is
    “`ou=people,dc=example,dc=net`”, and `ldap-username-attribute` is “uid”, then
    a person attempting to login as “`user`” would be mapped to the following
    full DN: “`uid=user,ou=people,dc=example,dc=net`”.

Container (Docker)

If deploying Guacamole using Docker Compose, you will need to add a set of
environment variables to the `environment` section of your
`guacamole/guacamole` container that looks like the following:

```
LDAP_USER_BASE_DN: 'ou=people,dc=example,dc=net'
```

If instead deploying Guacamole by running `docker run` manually, these same
environment variables will need to be provided using the `-e` option. For
example:

```
$ docker run --name some-guacamole \
    -e LDAP_USER_BASE_DN="ou=people,dc=example,dc=net" \
    -d -p 8080:8080 guacamole/guacamole
```

The environment variables that must be set in all cases for any Docker-based
Guacamole installation using this extension are:

`LDAP_USER_BASE_DN`
:   The base of the DN for all Guacamole users. *This property is absolutely
    required in all cases.* All Guacamole users must be descendents of this base
    DN.

    If a search DN is provided (via `ldap-search-bind-dn`), then Guacamole users
    need only be somewhere within the subtree of the specified user base DN.

    If a search DN *is not* provided, then all Guacamole users must be *direct
    descendents* of this base DN, as the base DN will be appended to the username
    to derive the user’s DN. For example, if `ldap-user-base-dn` is
    “`ou=people,dc=example,dc=net`”, and `ldap-username-attribute` is “uid”, then
    a person attempting to login as “`user`” would be mapped to the following
    full DN: “`uid=user,ou=people,dc=example,dc=net`”.

## Additional configuration (optional)[#](#additional-configuration-optional "Link to this heading")

Native Webapp (Tomcat)

Additional properties may be added to `guacamole.properties` to describe how
your LDAP directory is organized and how Guacamole should connect (and bind) to
your LDAP server:

`ldap-hostname`
:   The hostname of your LDAP server. If omitted, “localhost” will be used by
    default. You will need to use a different value if your LDAP server is
    located elsewhere.

`ldap-port`
:   The port your LDAP server listens on. If omitted, the standard LDAP or LDAPS
    port will be used, depending on the encryption method specified with
    `ldap-encryption-method` (if any). Unencrypted LDAP uses the standard port of
    389, while LDAPS uses port 636. Unless you manually configured your LDAP
    server to do otherwise, your LDAP server probably listens on port 389.

`ldap-encryption-method`
:   The encryption mechanism that Guacamole should use when communicating with
    your LDAP server. Legal values are “none” for unencrypted LDAP, “ssl” for
    LDAP over SSL/TLS (commonly known as LDAPS), or “starttls” for STARTTLS. If
    omitted, encryption will not be used.

    If you do use encryption when connecting to your LDAP server, you will need
    to ensure that its certificate chain can be verified using the certificates
    in Java’s trust store, often referred to as `cacerts`. If this is not the
    case, you will need to use Java’s `keytool` utility to either add the
    necessary certificates or to create a new trust store containing those
    certificates.

    If you will be using your own trust store and not the default `cacerts`, you
    will need to specify the full path to that trust store using the system
    property `javax.net.ssl.trustStore`. Note that this is a system property and
    *not* a Guacamole property; it must be specified when starting the JVM using
    the `-D` option. Your servlet container will provide some means of specifying
    startup options for the JVM.

`ldap-ssl-protocol`
:   Configures the SSL/TLS protocol version that will be used to contact the
    LDAP server, if LDAP encryption is enabled. Legal values are “SSLv3” for
    (legacy) SSL version 3 encryption, and “TLSv1”, “TLSv1.1”, “TLSv1.2”, or
    “TLSv1.3” for the various versions of TLS, version 1.0 - 1.3. The default
    is to use the latest, TLSv1.3.

    Please note that the legacy versions of SSLv3 and TLSv1 and TLSv1.1 have
    many known vulnerabilities and attack vectors, and you should use the
    latest possible TLS version that your LDAP servers support in order
    to best protect communication between Guacamole and your LDAP servers.

`ldap-max-search-results`
:   The maximum number of search results that can be returned by a single LDAP
    query. LDAP queries which exceed this maximum will fail. *This property is
    optional.* If omitted, each LDAP query will be limited to a maximum of 1000
    results.

`ldap-search-bind-dn`
:   The DN (Distinguished Name) of the user to bind as when authenticating users
    that are attempting to log in. If specified, Guacamole will query the LDAP
    directory to determine the DN of each user that logs in. If omitted, each
    user’s DN will be derived directly using the base DN specified with
    `ldap-user-base-dn`.

    Important

    **The search DN is used only to resolve a user’s username to their
    fully qualified DN during authentication.** Any further LDAP queries for
    retrieving objects like users, groups, and connection configurations will be
    done *using the LDAP credentials of the user that logged in*.

`ldap-search-bind-password`
:   The password to provide to the LDAP server when binding as
    `ldap-search-bind-dn` to authenticate other users. This property is only used
    if ldap-search-bind-dn is specified. If omitted, but `ldap-search-bind-dn` is
    specified, Guacamole will attempt to bind with the LDAP server without a
    password.

`ldap-username-attribute`
:   The attribute or attributes which contain the username within all Guacamole
    user objects in the LDAP directory. Usually, and by default, this will simply
    be “uid”. If your LDAP directory contains users whose usernames are dictated
    by different attributes, multiple attributes can be specified here, separated
    by commas, but beware: *doing so requires that a search DN be provided with
    `ldap-search-bind-dn`*.

    If a search DN *is not* provided, then the single username attribute
    specified here will be used together with the user base DN to directly derive
    the full DN of each user. For example, if `ldap-user-base-dn` is
    “`ou=people,dc=example,dc=net`”, and `ldap-username-attribute` is “uid”, then
    a person attempting to login as “`user`” would be mapped to the following
    full DN: “`uid=user,ou=people,dc=example,dc=net`”.

`ldap-member-attribute`
:   The attribute which contains the members within all group objects in the LDAP
    directory. Usually, and by default, this will simply be “member”. If your
    LDAP directory contains groups whose members are dictated by a different
    attribute, it can be specified here.

`ldap-member-attribute-type`
:   Specify whether the attribute defined in `ldap-member-attribute` (Usually
    “member”) identifies a group member by DN or by username. Possible values:
    “dn” (the default, if not specified) or “uid”.

    Example: an LDAP server may present groups using the `groupOfNames`
    scheme:

    ```
    dn: cn=group1,ou=Groups,dc=example,dc=net
    objectClass: groupOfNames
    cn: group1
    gidNumber: 12345
    member: uid=user1,ou=People,dc=example,dc=net
    member: uid=user2,ou=People,dc=example,dc=net
    ```

    `ldap-member-attribute` is `member` and `ldap-member-attribute-type` is `dn`.

    Example: an LDAP server may present groups using the `posixGroup`
    scheme:

    ```
    dn: cn=group1,ou=Groups,dc=example,dc=net
    objectClass: posixGroup
    cn: group1
    gidNumber: 12345
    memberUid: user1
    memberUid: user2
    ```

    `ldap-member-attribute` is `memberUid` and `ldap-member-attribute-type` is
    `uid`

`ldap-user-attributes`
:   The attribute or attributes to retrieve from the LDAP directory for the
    currently logged-in user, separated by commas. If specified, the attributes
    listed here are retrieved from each authenticated user and dynamically
    applied to the parameters of that user’s connections as [parameter
    tokens](configuring-guacamole.html#parameter-tokens) with the prefix “`LDAP_`”. If omitted, LDAP user
    attributes will not be used for parameter tokens.

    When a user authenticates with LDAP and accesses a particular Guacamole
    connection, the values of these tokens will be the values of their
    corresponding attributes at the time of authentication. If the attribute has
    no value for the current user, then the corresponding token is not applied.
    If the attribute has multiple values, then the first value of the attribute
    is used.

    When converting an LDAP attribute name into a parameter token name, the name
    of the attribute is transformed into uppercase with each word separated by
    underscores, a naming convention referred to as “uppercase with underscores”
    or “[screaming snake case](https://en.wikipedia.org/wiki/Naming_convention_(programming)#Multiple-word_identifiers)”.

    For example:

    | LDAP Attribute | Parameter Token |
    | --- | --- |
    | `lowercase-with-dashes` | `${LDAP_LOWERCASE_WITH_DASHES}` |
    | `CamelCase` | `${LDAP_CAMEL_CASE}` |
    | `headlessCamelCase` | `${LDAP_HEADLESS_CAMEL_CASE}` |
    | `lettersAndNumbers1234` | `${LDAP_LETTERS_AND_NUMBERS_1234}` |
    | `aRANDOM_mixOf-3NAMINGConventions` | `${LDAP_A_RANDOM_MIX_OF_3_NAMING_CONVENTIONS}` |

    Usage of parameter tokens is discussed in more detail in
    [Configuring Guacamole](configuring-guacamole.html) in [Parameter tokens](configuring-guacamole.html#parameter-tokens).

`ldap-user-search-filter`
:   The search filter used to query the LDAP tree for users that can log into and
    be granted privileges in Guacamole. *If this property is omitted the default of
    `(objectClass=*)` will be used.*

`ldap-config-base-dn`
:   The base of the DN for all Guacamole configurations. *This property is
    optional.* If omitted, the configurations of Guacamole connections will
    simply not be queried from the LDAP directory. If specified, this base DN
    will be used when querying the configurations accessible by a user once they
    have successfully logged in.

    Each configuration is analogous to a connection. Within Guacamole’s LDAP
    support, each configuration functions as a group, having user members (via
    the `member` attribute) and optionally group members (via the `seeAlso`
    attribute), where each member of a particular configuration group will have
    access to the connection defined by that configuration.

`ldap-group-base-dn`
:   The base of the DN for all user groups that may be used by other extensions
    to define permissions or that may referenced within Guacamole configurations
    using the standard seeAlso attribute. All groups which will be used to
    control access to Guacamole configurations must be descendents of this base
    DN. *If this property is omitted, LDAP groups will have no impact on
    Guacamole group memberships, and the `seeAlso` attribute will have no effect
    on Guacamole configurations.*

`ldap-group-name-attribute`
:   The attribute or attributes which define the unique name of user groups in
    the LDAP directory. Usually, and by default, this will simply be “cn”. If
    your LDAP directory contains groups whose names are dictated by different
    attributes, multiple attributes can be specified here, separated by commas.

`ldap-group-search-filter`
:   The search filter used to query the LDAP tree for groups that may be used by
    other extensions to define permissions. *If this property is omitted the
    default of `(objectClass=*)` will be used.*

    This has an effect only if `ldap-group-base-dn` is specified.

`ldap-dereference-aliases`
:   Whether the LDAP connection follows (dereferences) aliases as it searches the
    tree. Possible values for this property are “never” (the default) so that
    aliases will never be followed, “searching” to dereference during search
    operations after the base object is located, “finding” to dereference in
    order to locate the search base, but not during the actual search, and
    “always” to always dereference aliases.

`ldap-follow-referrals`
:   Whether the LDAP module follows referrals when processing search results from
    an LDAP search. Referrals can be pointers to other parts of an LDAP tree, or
    to a different server/connection altogether. This is a boolean parameter,
    with valid options of “true” or “false.” The default is false. When disabled,
    LDAP referrals will be ignored when encountered by the Guacamole LDAP client
    and the client will move on to the next result. When enabled, the LDAP
    client will follow the referral and process results within the referral,
    subject to the maximum hops parameter below.

`ldap-max-referral-hops`
:   The maximum number of referrals that will be processed before the LDAP client
    refuses to follow any more referrals. The default is 5. If the
    `ldap-follow-referrals` property is set to false (the default), this option
    has no effect. If the `ldap-follow-referrals` option is set to true, this
    will limit the depth of referrals followed to the number specified.

`ldap-operation-timeout`
:   The timeout, in seconds, of any single LDAP operation. The default is 30
    seconds. When this timeout is reached LDAP operations will be aborted.

Container (Docker)

Additional properties may be added to `guacamole.properties` to describe how
your LDAP directory is organized and how Guacamole should connect (and bind) to
your LDAP server:

`LDAP_HOSTNAME`
:   The hostname of your LDAP server. If omitted, “localhost” will be used by
    default. You will need to use a different value if your LDAP server is
    located elsewhere.

`LDAP_PORT`
:   The port your LDAP server listens on. If omitted, the standard LDAP or LDAPS
    port will be used, depending on the encryption method specified with
    `ldap-encryption-method` (if any). Unencrypted LDAP uses the standard port of
    389, while LDAPS uses port 636. Unless you manually configured your LDAP
    server to do otherwise, your LDAP server probably listens on port 389.

`LDAP_ENCRYPTION_METHOD`
:   The encryption mechanism that Guacamole should use when communicating with
    your LDAP server. Legal values are “none” for unencrypted LDAP, “ssl” for
    LDAP over SSL/TLS (commonly known as LDAPS), or “starttls” for STARTTLS. If
    omitted, encryption will not be used.

    If you do use encryption when connecting to your LDAP server, you will need
    to ensure that its certificate chain can be verified using the certificates
    in Java’s trust store, often referred to as `cacerts`. If this is not the
    case, you will need to use Java’s `keytool` utility to either add the
    necessary certificates or to create a new trust store containing those
    certificates.

    If you will be using your own trust store and not the default `cacerts`, you
    will need to specify the full path to that trust store using the system
    property `javax.net.ssl.trustStore`. Note that this is a system property and
    *not* a Guacamole property; it must be specified when starting the JVM using
    the `-D` option. Your servlet container will provide some means of specifying
    startup options for the JVM.

`LDAP_SSL_PROTOCOL`
:   Configures the SSL/TLS protocol version that will be used to contact the
    LDAP server, if LDAP encryption is enabled. Legal values are “SSLv3” for
    (legacy) SSL version 3 encryption, and “TLSv1”, “TLSv1.1”, “TLSv1.2”, or
    “TLSv1.3” for the various versions of TLS, version 1.0 - 1.3. The default
    is to use the latest, TLSv1.3.

    Please note that the legacy versions of SSLv3 and TLSv1 and TLSv1.1 have
    many known vulnerabilities and attack vectors, and you should use the
    latest possible TLS version that your LDAP servers support in order
    to best protect communication between Guacamole and your LDAP servers.

`LDAP_MAX_SEARCH_RESULTS`
:   The maximum number of search results that can be returned by a single LDAP
    query. LDAP queries which exceed this maximum will fail. *This property is
    optional.* If omitted, each LDAP query will be limited to a maximum of 1000
    results.

`LDAP_SEARCH_BIND_DN`
:   The DN (Distinguished Name) of the user to bind as when authenticating users
    that are attempting to log in. If specified, Guacamole will query the LDAP
    directory to determine the DN of each user that logs in. If omitted, each
    user’s DN will be derived directly using the base DN specified with
    `ldap-user-base-dn`.

    Important

    **The search DN is used only to resolve a user’s username to their
    fully qualified DN during authentication.** Any further LDAP queries for
    retrieving objects like users, groups, and connection configurations will be
    done *using the LDAP credentials of the user that logged in*.

`LDAP_SEARCH_BIND_PASSWORD`
:   The password to provide to the LDAP server when binding as
    `ldap-search-bind-dn` to authenticate other users. This property is only used
    if ldap-search-bind-dn is specified. If omitted, but `ldap-search-bind-dn` is
    specified, Guacamole will attempt to bind with the LDAP server without a
    password.

`LDAP_USERNAME_ATTRIBUTE`
:   The attribute or attributes which contain the username within all Guacamole
    user objects in the LDAP directory. Usually, and by default, this will simply
    be “uid”. If your LDAP directory contains users whose usernames are dictated
    by different attributes, multiple attributes can be specified here, separated
    by commas, but beware: *doing so requires that a search DN be provided with
    `ldap-search-bind-dn`*.

    If a search DN *is not* provided, then the single username attribute
    specified here will be used together with the user base DN to directly derive
    the full DN of each user. For example, if `ldap-user-base-dn` is
    “`ou=people,dc=example,dc=net`”, and `ldap-username-attribute` is “uid”, then
    a person attempting to login as “`user`” would be mapped to the following
    full DN: “`uid=user,ou=people,dc=example,dc=net`”.

`LDAP_MEMBER_ATTRIBUTE`
:   The attribute which contains the members within all group objects in the LDAP
    directory. Usually, and by default, this will simply be “member”. If your
    LDAP directory contains groups whose members are dictated by a different
    attribute, it can be specified here.

`LDAP_MEMBER_ATTRIBUTE_TYPE`
:   Specify whether the attribute defined in `ldap-member-attribute` (Usually
    “member”) identifies a group member by DN or by username. Possible values:
    “dn” (the default, if not specified) or “uid”.

    Example: an LDAP server may present groups using the `groupOfNames`
    scheme:

    ```
    dn: cn=group1,ou=Groups,dc=example,dc=net
    objectClass: groupOfNames
    cn: group1
    gidNumber: 12345
    member: uid=user1,ou=People,dc=example,dc=net
    member: uid=user2,ou=People,dc=example,dc=net
    ```

    `ldap-member-attribute` is `member` and `ldap-member-attribute-type` is `dn`.

    Example: an LDAP server may present groups using the `posixGroup`
    scheme:

    ```
    dn: cn=group1,ou=Groups,dc=example,dc=net
    objectClass: posixGroup
    cn: group1
    gidNumber: 12345
    memberUid: user1
    memberUid: user2
    ```

    `ldap-member-attribute` is `memberUid` and `ldap-member-attribute-type` is
    `uid`

`LDAP_USER_ATTRIBUTES`
:   The attribute or attributes to retrieve from the LDAP directory for the
    currently logged-in user, separated by commas. If specified, the attributes
    listed here are retrieved from each authenticated user and dynamically
    applied to the parameters of that user’s connections as [parameter
    tokens](configuring-guacamole.html#parameter-tokens) with the prefix “`LDAP_`”. If omitted, LDAP user
    attributes will not be used for parameter tokens.

    When a user authenticates with LDAP and accesses a particular Guacamole
    connection, the values of these tokens will be the values of their
    corresponding attributes at the time of authentication. If the attribute has
    no value for the current user, then the corresponding token is not applied.
    If the attribute has multiple values, then the first value of the attribute
    is used.

    When converting an LDAP attribute name into a parameter token name, the name
    of the attribute is transformed into uppercase with each word separated by
    underscores, a naming convention referred to as “uppercase with underscores”
    or “[screaming snake case](https://en.wikipedia.org/wiki/Naming_convention_(programming)#Multiple-word_identifiers)”.

    For example:

    | LDAP Attribute | Parameter Token |
    | --- | --- |
    | `lowercase-with-dashes` | `${LDAP_LOWERCASE_WITH_DASHES}` |
    | `CamelCase` | `${LDAP_CAMEL_CASE}` |
    | `headlessCamelCase` | `${LDAP_HEADLESS_CAMEL_CASE}` |
    | `lettersAndNumbers1234` | `${LDAP_LETTERS_AND_NUMBERS_1234}` |
    | `aRANDOM_mixOf-3NAMINGConventions` | `${LDAP_A_RANDOM_MIX_OF_3_NAMING_CONVENTIONS}` |

    Usage of parameter tokens is discussed in more detail in
    [Configuring Guacamole](configuring-guacamole.html) in [Parameter tokens](configuring-guacamole.html#parameter-tokens).

`LDAP_USER_SEARCH_FILTER`
:   The search filter used to query the LDAP tree for users that can log into and
    be granted privileges in Guacamole. *If this property is omitted the default of
    `(objectClass=*)` will be used.*

`LDAP_CONFIG_BASE_DN`
:   The base of the DN for all Guacamole configurations. *This property is
    optional.* If omitted, the configurations of Guacamole connections will
    simply not be queried from the LDAP directory. If specified, this base DN
    will be used when querying the configurations accessible by a user once they
    have successfully logged in.

    Each configuration is analogous to a connection. Within Guacamole’s LDAP
    support, each configuration functions as a group, having user members (via
    the `member` attribute) and optionally group members (via the `seeAlso`
    attribute), where each member of a particular configuration group will have
    access to the connection defined by that configuration.

`LDAP_GROUP_BASE_DN`
:   The base of the DN for all user groups that may be used by other extensions
    to define permissions or that may referenced within Guacamole configurations
    using the standard seeAlso attribute. All groups which will be used to
    control access to Guacamole configurations must be descendents of this base
    DN. *If this property is omitted, LDAP groups will have no impact on
    Guacamole group memberships, and the `seeAlso` attribute will have no effect
    on Guacamole configurations.*

`LDAP_GROUP_NAME_ATTRIBUTE`
:   The attribute or attributes which define the unique name of user groups in
    the LDAP directory. Usually, and by default, this will simply be “cn”. If
    your LDAP directory contains groups whose names are dictated by different
    attributes, multiple attributes can be specified here, separated by commas.

`LDAP_GROUP_SEARCH_FILTER`
:   The search filter used to query the LDAP tree for groups that may be used by
    other extensions to define permissions. *If this property is omitted the
    default of `(objectClass=*)` will be used.*

    This has an effect only if `ldap-group-base-dn` is specified.

`LDAP_DEREFERENCE_ALIASES`
:   Whether the LDAP connection follows (dereferences) aliases as it searches the
    tree. Possible values for this property are “never” (the default) so that
    aliases will never be followed, “searching” to dereference during search
    operations after the base object is located, “finding” to dereference in
    order to locate the search base, but not during the actual search, and
    “always” to always dereference aliases.

`LDAP_FOLLOW_REFERRALS`
:   Whether the LDAP module follows referrals when processing search results from
    an LDAP search. Referrals can be pointers to other parts of an LDAP tree, or
    to a different server/connection altogether. This is a boolean parameter,
    with valid options of “true” or “false.” The default is false. When disabled,
    LDAP referrals will be ignored when encountered by the Guacamole LDAP client
    and the client will move on to the next result. When enabled, the LDAP
    client will follow the referral and process results within the referral,
    subject to the maximum hops parameter below.

`LDAP_MAX_REFERRAL_HOPS`
:   The maximum number of referrals that will be processed before the LDAP client
    refuses to follow any more referrals. The default is 5. If the
    `ldap-follow-referrals` property is set to false (the default), this option
    has no effect. If the `ldap-follow-referrals` option is set to true, this
    will limit the depth of referrals followed to the number specified.

`LDAP_OPERATION_TIMEOUT`
:   The timeout, in seconds, of any single LDAP operation. The default is 30
    seconds. When this timeout is reached LDAP operations will be aborted.

### Using multiple LDAP servers[#](#using-multiple-ldap-servers "Link to this heading")

If you have several LDAP servers that Guacamole should authenticate against, it
is possible to provide the configuration details for multiple servers by
creating or editing a YAML file within `GUACAMOLE_HOME` called
`ldap-servers.yml`. This file consists of a single list of servers (a YAML
array of objects) and any number of corresponding configuration options (the
key/value pairs within each YAML object). The available options correspond
*exactly* to the properties described above except that they lack an `ldap-`
prefix.

For example, the following `guacamole.properties`:

```
ldap-hostname: dc1.example.net
ldap-user-base-dn: ou=Users,dc=example,dc=net
ldap-username-attribute: sAMAccountName
ldap-search-bind-dn: cn=Guacamole,ou=Service Users,dc=example,dc=net
ldap-search-bind-password: SomePassword!
```

is exactly equivalent to the following `ldap-servers.yml`

```
- hostname: dc1.example.net
  user-base-dn: ou=Users,dc=example,dc=net
  username-attribute: sAMAccountName
  search-bind-dn: cn=Guacamole,ou=Service Users,dc=example,dc=net
  search-bind-password: SomePassword!
```

The benefit of using `ldap-servers.yml` is that the format allows multiple
servers to be defined, relying on the properties within `guacamole.properties`
as defaults. For example, the following `ldap-servers.yml` defines two LDAP
servers:

```
- hostname: dc1.example.net
  user-base-dn: ou=Users,dc=example,dc=net
  username-attribute: sAMAccountName
  search-bind-dn: cn=Guacamole,ou=Service Users,dc=example,dc=net
  search-bind-password: SomePassword!

- hostname: dc2.example.net
  user-base-dn: ou=Users,dc=example,dc=net
  username-attribute: sAMAccountName
  search-bind-dn: cn=Guacamole,ou=Service Users,dc=example,dc=net
  search-bind-password: SomePassword!
```

Leveraging the fact that values within `guacamole.properties` are used as the
default values for all LDAP servers in `ldap-servers.yml`, the above can be
abbreviated by moving the common options into `guacamole.properties`:

```
ldap-user-base-dn: ou=Users,dc=example,dc=net
ldap-username-attribute: sAMAccountName
ldap-search-bind-dn: cn=Guacamole,ou=Service Users,dc=example,dc=net
ldap-search-bind-password: SomePassword!
```

Leaving `ldap-servers.yml` containing, simply:

```
- hostname: dc1.example.net
- hostname: dc2.example.net
```

If multiple LDAP servers are listed within `ldap-servers.yml`, and a user
attempts to log into Guacamole, each defined LDAP server is tried, in order,
until one server successfully authenticates the user or until all servers fail.

If not all LDAP servers are relevant to all users, and it is reasonable to
determine which user is relevant to which LDAP server by the format of their
username, patterns can be specified on a per-server basis to narrow which
servers apply to which login attempts. For example:

```
- hostname: dc1.example.net
  match-usernames: COMPANYA\\(.*)

- hostname: dc2.example.net
  match-usernames: COMPANYB\\(.*)
```

The value for `match-usernames` can be any regular expression accepted by Java,
where the capturing group dictates the portion that should be considered the
user’s username with respect to Guacamole. If multiple patterns should apply to
a particular LDAP server, this can be specified with a list of patterns for
`match-usernames`:

```
- hostname: dc1.example.net
  match-usernames:
    - COMPANYA\\(.*)
    - (.*)@a\.example\.net

- hostname: dc2.example.net
  match-usernames:
    - COMPANYB\\(.*)
    - (.*)@b\.example\.net
```

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Parameter tokens[#](#parameter-tokens "Link to this heading")

In addition to [the standard parameter tokens](configuring-guacamole.html#parameter-tokens) and the
parameter tokens from other extensions, authenticating with LDAP makes the
following tokens available for use within connection configurations:

`${LDAP_ATTRIBUTE}`
:   The value of the `ATTRIBUTE` attribute of the current user’s LDAP account.
    This token will only be defined for users that have the relevant attribute
    set, and only if that attribute was explicitly configured using [the
    `ldap-user-attributes` property](#guac-ldap-config).

`${LDAP_DOMAIN}`
:   The domain of the LDAP user account of the current user. This token will be
    defined only for users that have authenticated with LDAP, and only for users
    that authenticated with a down-level login (`DOMAIN\username`) or a UPN-style
    login (`username@domain`).

Usage of parameter tokens is discussed in more detail in
[Configuring Guacamole](configuring-guacamole.html) in [Parameter tokens](configuring-guacamole.html#parameter-tokens).

## The LDAP schema[#](#the-ldap-schema "Link to this heading")

Guacamole’s LDAP support allows users and connections to be managed purely
within an LDAP directory defined in `guacamole.properties`. This is
accomplished with a minimum of changes to the standard LDAP schema - all
Guacamole users are traditional LDAP users and share the same mechanism of
authentication. The only new type of object required is a representation for
Guacamole connections, `guacConfigGroup`, which was added to your server’s
schema during the install process above.

### Users[#](#users "Link to this heading")

All Guacamole users, as far as the LDAP support is concerned, are LDAP users
with standard LDAP credentials. When a user signs in to Guacamole, their
username and password will be used to bind to the LDAP server. If this bind
operation is successful, the available connections are queried from the
directory and the user is allowed in.

### Connections and parameters[#](#connections-and-parameters "Link to this heading")

Each connection is represented by an instance of the `guacConfigGroup` object
class, an extended version of the standard LDAP `groupOfNames`, which provides
a protocol and set of parameters. Only members of the `guacConfigGroup` will
have access to the corresponding connection.

The `guacConfigGroup` object class provides two new attributes in addition to
those provided by `groupOfNames`:

`guacConfigProtocol`
:   The protocol associated with the connection, such as “`vnc`” or “`rdp`”. This
    attribute is required for every `guacConfigGroup` and can be given only once.

`guacConfigParameter`
:   The name and value of a parameter for the specified protocol. This is given
    as `name=value`, where “name” is the name of the parameter, as defined by the
    documentation for the protocol specified, and “value” is any allowed value for
    that parameter.

    This attribute can be given multiple times for the same connection.

`guacConfigProxyHostname`
:   The host name or IP address to use for connecting to guacd in order to
    establish the connection to the server. This attribute is optional and,
    if not provided, will default to the system-level configuration for
    connecting to guacd, either the default of `localhost` or the value
    defined by `guacd-hostname` in `guacamole.properties`. This attribute may
    only be specified once per connection.

`guacConfigProxyPort`
:   The TCP port to use in order to connect to guacd to establish the
    connection to the server. This attribute is optional, and, like the
    `guacConfigProxyHostname` attribute, will default to the system-level
    configuration. This attribute may be specified at most once per connection.

`guacConfigProxyEncryption`
:   The encryption method that should be used to connect to guacd in order
    to establish the connection to the server. This attribute is optional
    and will default to the system-level configuration for connecting to
    guacd. Valid values for this are `NONE` or `SSL`. This attribute may
    be specified at most once per connection.

For example, to create a new VNC connection which connects to “localhost” at
port 5900, while granting access to `user1` and `user2`, you could create an
`.ldif` file like the following:

```
dn: cn=Example Connection,ou=groups,dc=example,dc=net
objectClass: guacConfigGroup
objectClass: groupOfNames
cn: Example Connection
guacConfigProtocol: vnc
guacConfigParameter: hostname=localhost
guacConfigParameter: port=5900
guacConfigParameter: password=secret
member: cn=user1,ou=people,dc=example,dc=net
member: cn=user2,ou=people,dc=example,dc=net
```

The new connection can then be created using the **ldapadd** utility:

```
$ ldapadd -x -D cn=admin,dc=example,dc=net -W -f example-connection.ldif
Enter LDAP Password:
adding new entry "cn=Example Connection,ou=groups,dc=example,dc=net"

$
```

Where `cn=admin,dc=example,dc=net` is an administrator account with permission
to create new entries, and `example-connection.ldif` is the name of the `.ldif`
file you just created.

There is, of course, no need to use only the standard LDAP utilities to create
connections and users. There are useful graphical environments for manipulating
LDAP directories, such as [Apache Directory Studio](https://directory.apache.org/studio/),
which make many of the tasks given above much easier.

Contents

---
# guacamole-ext

## Contents

# guacamole-ext[#](#guacamole-ext "Link to this heading")

While not strictly part of the Java API provided by the Guacamole project,
guacamole-ext is an API exposed by the Guacamole web application within a
separate project such that extensions, specifically authentication providers,
can be written to tweak Guacamole to fit well in existing deployments.

Extensions to Guacamole can:

1. Provide alternative authentication methods and sources of connection/user
   data.
2. Provide event listeners that will be notified as Guacamole performs tasks
   such as authentication and tunnel connection.
3. Theme or brand Guacamole through additional CSS files and static resources.
4. Extend Guacamole’s JavaScript code by providing JavaScript that will be
   loaded automatically.
5. Add additional display languages, or alter the translation strings of
   existing languages.

## Guacamole extension format[#](#guacamole-extension-format "Link to this heading")

Guacamole extensions are standard Java `.jar` files which contain all classes,
library `.jar` files, and resources required by the extension, as well as the
Guacamole extension manifest. There is no set structure to an extension except
that:

1. The `guac-manifest.json` manifest must be in the root of the archive.
2. Any required library `.jar` files that will not be placed within
   [`GUACAMOLE_HOME/lib/`](configuring-guacamole.html#guacamole-home) must be in the root of the archive.
3. Java classes and packages for the extension itself (or for unpacked
   dependencies of the extension) will be read relative to the archive root,
   as well.

Beyond this, the semantics and locations associated with all other resources
within the extension are determined by the extension manifest alone.

### Extension manifest[#](#extension-manifest "Link to this heading")

The Guacamole extension manifest is a single JSON file, `guac-manifest.json`,
which describes the location of each resource, the type of each resource, and
the version of Guacamole that the extension was built for. The manifest can
contain the following properties:

`guacamoleVersion`
:   The version string of the Guacamole release that this extension is written
    for. *This property is required for all extensions.* The special version
    string `"*"` can be used if the extension does not depend on a particular
    version of Guacamole, but be careful - this will bypass version compatibility
    checks, and should never be used if the extension does more than basic
    theming or branding.

`name`
:   A human-readable name for the extension. *This property is required for all
    extensions.* When your extension is successfully loaded, a message
    acknowledging the successful loading of your extension by name will be
    logged.

`namespace`
:   A unique string which identifies your extension. *This property is required
    for all extensions.* This string should be unique enough that it is unlikely
    to collide with the namespace of any other extension.

    If your extension contains static resources, those resources will be served
    at a path derived from the namespace provided here.

`authProviders`
:   An array of the classnames of all `AuthenticationProvider` subclasses
    provided by this extension.

`listeners`
:   An array of the classnames of all `Listener` subclasses provided by this
    extension.

`js`
:   An array of all JavaScript files within the extension. All paths within this
    array must be relative paths, and will be interpreted relative to the root of
    the archive.

    JavaScript files declared here will be automatically loaded when the web
    application loads within the user’s browser.

`css`
:   An array of all CSS files within the extension. All paths within this array
    must be relative paths, and will be interpreted relative to the root of the
    archive.

    CSS files declared here will be automatically applied when the web
    application loads within the user’s browser.

`html`
:   An array of all HTML files within the extension that should be used to update
    or replace existing HTML within the Guacamole interface. All paths within
    this array must be relative paths, and will be interpreted relative to the
    root of the archive.

    HTML files declared here will be automatically applied to other HTML within
    the Guacamole interface when the web application loads within the user’s
    browser. The manner in which the files are applied is dictated by
    `<meta ...>` tags within those same files.

`translations`
:   An array of all translation files within the extension. All paths within this
    array must be relative paths, and will be interpreted relative to the root of
    the archive.

    Translation files declared here will be automatically added to the available
    languages. If a translation file provides a language that already exists
    within Guacamole, its strings will override the strings of the existing
    translation.

`resources`
:   An object where each property name is the name of a web resource file, and
    each value is the mimetype for that resource. All paths within this object
    must be relative paths, and will be interpreted relative to the root of the
    archive.

    Web resources declared here will be made available to the application at
    `app/ext/NAMESPACE/PATH`, where `NAMESPACE` is the value of the
    namespace property, and `PATH` is the declared web resource filename.

The only absolutely required properties are `guacamoleVersion`, `name`, and
`namespace`, as they are used to identify the extension and for compatibility
checks. The most minimal `guac-manifest.json` will look something like this:

```
{
    "guacamoleVersion" : "1.6.0",
    "name" : "My Extension",
    "namespace" : "my-extension"
}
```

This will allow the extension to load, but does absolutely nothing otherwise.
Lacking the semantic information provided by the other properties, no other
files within the extension will be used. A typical `guac-manifest.json` for an
extension providing theming or branding would be more involved:

```
{

    "guacamoleVersion" : "1.6.0",

    "name"      : "My Extension",
    "namespace" : "my-extension",

    "css" : [ "theme.css" ],

    "html" : [ "loginDisclaimer.html" ],

    "resources" : {
        "images/logo.png"   : "image/png",
        "images/cancel.png" : "image/png",
        "images/delete.png" : "image/png"
    }

}
```

### Updating existing HTML[#](#updating-existing-html "Link to this heading")

The existing HTML structure of Guacamole’s interface can be modified by
extensions through special “patch” HTML files declared by the html property in
`guac-manifest.json`. These files are HTML fragments and are identical to any
other HTML file except that they contain Guacamole-specific meta tags that
instruct Guacamole to modify its own HTML in a particular way. Each meta tag
takes the following form:

```
<meta name="NAME" content="SELECTOR">
```

where `SELECTOR` is a CSS selector that matches the elements within the
Guacamole interface that serve as a basis for the modification, and `NAME` is
any one of the following defined modifications:

`before`
:   Inserts the specified HTML immediately before any element matching the CSS
    selector.

`after`
:   Inserts the specified HTML immediately after any element matching the CSS
    selector.

`replace`
:   Replaces any element matching the CSS selector with the specified HTML.

`before-children`
:   Inserts the specified HTML immediately before the first child (if any) of any
    element matching the CSS selector. If a matching element has no children, the
    HTML simply becomes the entire contents of the matching element.

`after-children`
:   Inserts the specified HTML immediately after the last child (if any) of any
    element matching the CSS selector. If a matching element has no children, the
    HTML simply becomes the entire contents of the matching element.

`replace-children`
:   Replaces the entire contents of any element matching the CSS selector with
    the specified HTML.

For example, to add a welcome message and link to some corporate privacy policy
(a fairly common need), you would add an HTML file like the following:

```
<meta name="after" content=".login-ui .login-dialog">

<div class="welcome">
    <h2>Welcome to our Guacamole server!</h2>
    <p>
        Please be sure to read our <a href="/path/to/some/privacy.html">privacy
        policy</a> before continuing.
    </p>
</div>
```

After the extension is installed and Guacamole is restarted, the “welcome” div
and its contents will automatically be inserted directly below the login dialog
(the only element that would match `.login-ui .login-dialog`) as if they were
part of Guacamole’s HTML in the first place.

An example of an extension that modifies style and HTML components for the
purpose of providing custom “branding” of the Guacamole interface can be found
in the `doc/guacamole-branding-example` directory of the guacamole-client
source code, which can be found here:
[apache/guacamole-client](https://github.com/apache/guacamole-client/tree/master/doc/guacamole-branding-example)

## Accessing the server configuration[#](#accessing-the-server-configuration "Link to this heading")

The configuration of the Guacamole server is exposed through the `Environment`
interface, specifically the `LocalEnvironment` implementation of this
interface. Through `Environment`, you can access all properties declared within
`guacamole.properties`, determine the proper hostname/port of guacd, and access
the contents of `GUACAMOLE_HOME`.

### Custom properties[#](#custom-properties "Link to this heading")

If your extension requires generic, unstructured configuration parameters,
`guacamole.properties` is a reasonable and simple location for them. The
`Environment` interface provides direct access to `guacamole.properties` and
simple mechanisms for reading and parsing the properties therein. The value of
a property can be retrieved by calling `getProperty()`, which will return
`null` or a default value for undefined properties, or `getRequiredProperty()`,
which will throw an exception for undefined properties.

For convenience, guacamole-ext contains several pre-defined property base
classes for common types:

`BooleanGuacamoleProperty`
:   The values “true” and “false” are parsed as their corresponding `Boolean`
    values. Any other value results in a parse error.

`IntegerGuacamoleProperty`
:   Numeric strings are parsed as `Integer` values. Non-numeric strings will
    result in a parse error.

`LongGuacamoleProperty`
:   Numeric strings are parsed as `Long` values. Non-numeric strings will result
    in a parse error.

`StringGuacamoleProperty`
:   The property value is returned as an untouched `String`. No parsing is
    performed, and parse errors cannot occur.

`FileGuacamoleProperty`
:   The property is interpreted as a filename, and a new `File` pointing to that
    filename is returned. If the filename is invalid, a parse error will be
    thrown. Note that the file need not exist or be accessible for the filename
    to be valid.

To use these types, you must extend the base class, implementing the
`getName()` function to identify your property. Typically, you would declare
these properties as static members of some class containing all properties
relevant to your extension:

```
public class MyProperties {

    public static MY_PROPERTY = new IntegerGuacamoleProperty() {

        @Override
        public String getName() { return "my-property"; }

    };

}
```

Your property can then be retrieved with `getProperty()` or
`getRequiredProperty()`:

```
Integer value = environment.getProperty(MyProperties.MY_PROPERTY);
```

If you need more sophisticated parsing, you can also implement your own
property types by implementing the `GuacamoleProperty` interface. The only
functions to implement are `getName()`, which returns the name of the property,
and `parseValue()`, which parses a given string and returns its value.

### Advanced configuration[#](#advanced-configuration "Link to this heading")

If you need more structured data than provided by simple properties, you can
place completely arbitrary files in a hierarchy of your choosing anywhere
within `GUACAMOLE_HOME` as long as you avoid placing your files in directories
reserved for other purposes as described above.

The `Environment` interface exposes the location of `GUACAMOLE_HOME` through
the `getGuacamoleHome()` function. This function returns a standard Java `File`
which can then be used to locate other files or directories within
`GUACAMOLE_HOME`:

```
File myConfigFile = new File(environment.getGuacamoleHome(), "my-config.xml");
```

There is no guarantee that `GUACAMOLE_HOME` or your file will exist, and you
should verify this before proceeding further in your extension’s configuration
process, but once this is done you can simply parse your file as you see fit.

## Authentication providers[#](#authentication-providers "Link to this heading")

Guacamole’s authentication system is driven by authentication providers, which
are classes which implement the `AuthenticationProvider` interface defined by
guacamole-ext. When any page within Guacamole is visited, the following process
occurs:

1. All currently installed extensions are polled, in lexicographic order of
   their filenames, by invoking the `getAuthenticatedUser()` function with a
   `Credentials` object constructed with the contents of the HTTP request.

   The credentials given are abstract. While the `Credentials` object provides
   convenience access to a traditional username and password, *implementations
   are not required to use usernames and passwords*. The entire contents of
   the HTTP request is at your disposal, including parameters, cookies, and SSL
   information.
2. If an authentication attempt fails, the extension throws either a
   `GuacamoleInsufficientCredentialsException` (if more credentials are needed
   before validity can be determined) or `GuacamoleInvalidCredentialsException`
   (if the credentials are technically sufficient, but are invalid as
   provided). If all extensions fail to authenticate the user, the contents of
   the exception thrown by the first extension to fail are used to produce the
   user login prompt.

   *Note that this means there is no “login screen” in Guacamole per se; the
   prompt for credentials for unauthenticated users is determined purely based
   on the needs of the extension as declared within the authentication failure
   itself.*

   If an authentication attempt succeeds, the extension returns an instance of
   `AuthenticatedUser` describing the identity of the user that just
   authenticated, and no further extensions are polled.
3. If authentication has succeeded, and thus an `AuthenticatedUser` is
   available, that `AuthenticatedUser` is passed to the `getUserContext()`
   function of all extensions’ authentication providers. Each extension now has
   the opportunity to provide access to data for a user, even if that extension
   did not originally authenticate the user. If no `UserContext` is returned
   for the given `AuthenticatedUser`, then that extension has simply refused to
   provide data for that user.

   The Guacamole interface will transparently unify the data from each
   extension, providing the user with a view of all available connections. If
   the user has permission to modify or administer any objects associated with
   an extension, access to the administrative interface will be exposed as
   well, again with a unified view of all applicable objects.

Important

Because authentication is decoupled from data storage/access, *you do not need
to implement full-blown data storage if you only wish to provide an additional
authentication mechanism*. You can instead implement only the authentication
portion of an `AuthenticationProvider`, and otherwise rely on the storage and
features provided by other extensions, such as the [database authentication
extension](jdbc-auth.html).

The Guacamole web application includes a basic authentication provider
implementation which parses an XML file to determine which users exist, their
corresponding passwords, and what configurations those users have access to.
This is the part of Guacamole that reads the `user-mapping.xml` file. If you
use a custom authentication provider for your authentication, this file will
probably not be required.

The community has implemented authentication providers which access databases,
use LDAP, or even perform no authentication at all, redirecting all users to a
single configuration specified in `guacamole.properties`.

A minimal authentication provider is implemented in the tutorials later, and
the upstream authentication provider implemented within Guacamole, as well as
the authentication providers implemented by the community, are good examples
for how authentication can be extended without having to implement a whole new
web application.

### `SimpleAuthenticationProvider`[#](#simpleauthenticationprovider "Link to this heading")

The `SimpleAuthenticationProvider` class provides a much simpler means of
implementing authentication when you do not require the ability to add and
remove users and connections. It is an abstract class and requires only one
function implementation: `getAuthorizedConfigurations()`.

This function is required to return a `Map` of unique IDs to configurations,
where these configurations are all configurations accessible with the provided
credentials. As before, the credentials given are abstract. You are not
required to use usernames and passwords.

The configurations referred to by the function name are instances of
`GuacamoleConfiguration` (part of guacamole-common), which is just a wrapper
around a protocol name and set of parameter name/value pairs. The name of the
protocol to use and a set of parameters is the minimum information required for
other parts of the Guacamole API to complete the handshake required by the
Guacamole protocol.

When a class that extends `SimpleAuthenticationProvider` is asked for more
advanced operations by the web application, `SimpleAuthenticationProvider`
simply returns that there is no permission to do so. This effectively disables
all administrative functionality within the web interface.

If you choose to go the simple route, most of the rest of this chapter is
irrelevant. Permissions, security model, and various classes will be discussed
that are all handled for you automatically by `SimpleAuthenticationProvider`.

## The `UserContext`[#](#the-usercontext "Link to this heading")

The `UserContext` is the root of all data-related operations. It is used to
list, create, modify, or delete users and connections, as well as to query
available permissions. If an extension is going to provide access to data of
any sort, it must do so through the `UserContext`.

The Guacamole web application uses permissions queries against the
`UserContext` to determine what operations to present, but *beware that it is
up to the `UserContext` to actually enforce these restrictions*. The Guacamole
web application will not enforce restrictions on behalf of the `UserContext`.

The `UserContext` is the sole means of entry and the sole means of modification
available to a logged-in user. If the `UserContext` refuses to perform an
operation (by throwing an exception), the user cannot perform the operation at
all.

## `Directory` classes[#](#directory-classes "Link to this heading")

Access to objects beneath the `UserContext` is given through `Directory`
classes. These `Directory` classes are similar to Java collections, but they
also embody update and batching semantics. Objects can be retrieved from a
`Directory` using its `get()` function and added or removed with `add()` and
`remove()` respectively, but objects already in the set can also be updated by
passing an updated object to its `update()` function.

An implementation of a `Directory` can rely on these functions to define the
semantics surrounding all operations. The `add()` function is called only when
creating new objects, the `update()` function is called only when updating an
object previously retrieved with `get()`, and `remove()` is called only when
removing an existing object by its identifier.

When implementing an `AuthenticationProvider`, you must ensure that the
`UserContext` will only return `Directory` classes that automatically enforce
the permissions associated with all objects and the associated user.

## REST resources[#](#rest-resources "Link to this heading")

Arbitrary REST resources may be exposed by extensions at the
`AuthenticationProvider` level, if the resource does not require an associated
authenticated user, or at the `UserContext` level, if the resource should be
available to authenticated users only. In both cases, the REST resource is
provided through implementing the `getResource()` function, returning an object
which is annotated with JAX-RS annotations (JSR 311).

The resource returned by `getResource()` functions as the root resource,
providing access to other resources beneath itself. The root resource for the
`AuthenticationProvider` is exposed at `PATH/api/ext/IDENTIFIER`, and
the root resource for the `UserContext` is exposed at
`PATH/api/session/ext/IDENTIFIER`, where `PATH` is the path to which
Guacamole has been deployed (typically `/guacamole/`) and `IDENTIFIER` is the
unique identifier for the `AuthenticationProvider`, as returned by
`getIdentifier()`.

The behavior of extension REST resources is generally left entirely to the
implementation, with the exception that the “token” request parameter is
reserved for use by Guacamole. This parameter contains the user’s
authentication token when the user is logged in, and must be present on all
requests which require authentication. Though not relevant to REST resources
exposed at the `AuthenticationProvider` level, resources exposed at the
`UserContext` level inherently require the “token” parameter to be present, as
it is the sole means of locating the user’s session.

## Permissions[#](#permissions "Link to this heading")

The permissions system within guacamole-ext is an advisory system. It is the
means by which an authentication module describes to the web application what a
user is allowed to do. The body of permissions granted to a user describes
which objects that user can see and what they can do to those objects, and thus
suggests how the Guacamole interface should appear to that user.

*Permissions are not the means by which access is restricted*; they are purely
a means of describing access level. An implementation may internally use the
permission objects to define restrictions, but this is not required. It is up
to the implementation to enforce its own restrictions by throwing exceptions
when an operation is not allowed, and to correctly communicate the abilities of
individual users through these permissions.

The permissions available to a user are exposed through the
`SystemPermissionSet` and `ObjectPermissionSet` classes which are accessible
through the `UserContext`. These classes also serve as the means for
manipulating the permissions granted to a user.

### System permissions[#](#system-permissions "Link to this heading")

System permissions describe access to operations that manipulate the system as
a whole, rather than specific objects. This includes the creation of new
objects, as object creation directly affects the system, and per-object
controls cannot exist before the object is actually created.

`ADMINISTER`
:   The user is a super-user - the Guacamole equivalent of root. They are allowed
    to manipulate of system-level permissions and all other objects. This
    permission implies all others.

`CREATE_CONNECTION`
:   The user is allowed to create new connections. If a user has this permission,
    the management interface will display components related to connection
    creation.

`CREATE_CONNECTION_GROUP`
:   The user is allowed to create new connection groups. If a user has this
    permission, the management interface will display components related to
    connection group creation.

`CREATE_SHARING_PROFILE`
:   The user is allowed to create new sharing profiles. If a user has this
    permission, the management interface will display components related to
    sharing profile creation.

`CREATE_USER`
:   The user is allowed to create other users. If a user has this permission, the
    management interface will display components related to user creation.

### Object permissions[#](#object-permissions "Link to this heading")

Object permissions describe access to operations that affect a particular
object. Guacamole currently defines four types of objects which can be
associated with permissions: users, connections, connection groups, and sharing
profiles. Each object permission associates a single user with an action that
may be performed on a single object.

`ADMINISTER`
:   The user may grant or revoke permissions involving this object. “Involving”,
    in this case, refers to either side of the permission association, and
    includes both the user to whom the permission is granted and the object the
    permission affects.

`DELETE`
:   The user may delete this object. This is distinct from the `ADMINISTER`
    permission which deals only with permissions. A user with this permission
    will see the “Delete” button when applicable.

`READ`
:   The user may see that this object exists and read the properties of that
    object.

    Note that the implementation is *not required to divulge the true underlying
    properties of any object*. The parameters of a connection or sharing profile,
    the type or contents of a connection group, the password of a user, etc. all
    need not be exposed.

    This is particularly important from the perspective of security when it comes
    to connections, as the parameters of a connection are only truly needed when
    a connection is being modified, and likely should not be exposed otherwise.
    The actual connection operation is always performed internally by the
    authentication provider, and thus does not require client-side knowledge of
    anything beyond the connection’s existence.

`UPDATE`
:   The user may change the properties of this object.

    In the case of users, this means the user’s password can be altered.
    *Permissions are not considered properties of a user*, nor objects in their
    own right, but rather associations between a user and an action which may
    involve another object.

    The properties of a connection include its name, protocol, parent connection
    group, and parameters. The properties of a connection group include its name,
    type, parent connection group, and children. The properties of a sharing
    profile include its name, primary connection, and parameters.

## Connections[#](#connections "Link to this heading")

Guacamole connections are organized in a hierarchy made up of connection
groups, which each act as folders organizing the connections themselves. The
hierarchy is accessed through the root-level connection group, exposed by
`getRootConnectionGroup()` by the `UserContext`. The connections and connection
groups exposed beneath the root connection group must also be accessible
directly through the connection and connection group directories exposed by
`getConnectionDirectory()` and `getConnectionGroupDirectory()` of the
`UserContext`.

When a user attempts to use a connection the `connect()` of the associated
`Connection` object will be invoked. It is then up to the implementation of
this function to establish the TCP connection to guacd, perform the connection
handshake (most likely via an `InetGuacamoleSocket` wrapped within a
`ConfiguredGuacamoleSocket`), and then return a `GuacamoleTunnel` which
controls access to the established socket.

Extensions may maintain historical record of connection use via
`ConnectionRecord` objects, which are exposed both at the `Connection` level
and across all connections via the `UserContext`. Such record maintenance is
optional, and it is expected that most implementations will simply return empty
lists.

Important

If connection state will not be tracked by the extension, and the parameters
associated with the connection will be known at the time the connection object
is created, the `SimpleConnection` implementation of `Connection` can be used
to make life easier.

## Managing/sharing active connections[#](#managing-sharing-active-connections "Link to this heading")

After a connection has been established, its underlying `GuacamoleTunnel` can
be exposed by a `UserContext` through the `Directory` returned by
getActiveConnectionDirectory(). The `ActiveConnection` objects accessible
through this `Directory` are the means by which an administrator may monitor or
forcibly terminate another user’s connection, ultimately resulting in Guacamole
invoking the `close()` function of the underlying `GuacamoleTunnel`, and also
serve as the basis for screen sharing.

Screen sharing is implemented through the use of `SharingProfile` objects,
exposed through yet another `Directory` beneath the `UserContext`. Each sharing
profile is associated with a single connection that it can be used to share,
referred to as the “primary connection”. If a user has read access to a sharing
profile associated with their current connection, that sharing profile will be
displayed as an option within [the share menu of the Guacamole
menu](using-guacamole.html#client-share-menu).

The overall sharing process is as follows:

1. A user, having access to a sharing profile associated with their current
   active connection, clicks its option within the [share menu](using-guacamole.html#client-share-menu).
2. Guacamole locates the `ActiveConnection` and invokes its
   `getSharingCredentials()` function with the identifier of the sharing
   profile. The contents of the returned `UserCredentials` object is used by
   Guacamole to generate a sharing link which can be given to other users.
3. When another user visits the sharing link, the credentials embedded in the
   link are passed to the authentication providers associated with each
   installed extension. *It is up to the extension that originally provided
   those credentials to authenticate the user and provide them with access to
   the shared connection.*
4. When the user attempts to connect to the shared connection, the extension
   establishes the connection using the ID of the connection being joined.
   *This is not the connection identifier as dictated by guacamole-ext, but
   rather [the unique ID assigned by guacd as required by the Guacamole
   protocol](guacamole-protocol.html#guacamole-protocol-joining).* This ID can be retrieved from a
   `ConfiguredGuacamoleSocket` via `getConnectionID()`, and can be passed
   through a `GuacamoleConfiguration` through `setConnectionID()` (instead of
   specifying a protocol, as would be done for a brand new connection).

Contents

---
# libguac

## Contents

# libguac[#](#libguac "Link to this heading")

The C API for extending and developing with Guacamole is libguac. All native
components produced by the Guacamole project link with this library, and this
library provides the common basis for extending the native functionality of
those native components (by implementing client plugins).

libguac is used mainly for developing client plugins like libguac-client-vnc or
libguac-client-rdp, or for developing a proxy supporting the Guacamole protocol
like guacd. This chapter is intended to give an overview of how libguac is
used, and how to use it for general communication with the Guacamole protocol.

## Error handling[#](#error-handling "Link to this heading")

Most functions within libguac handle errors by returning a zero or non-zero
value, whichever is appropriate for the function at hand. If an error is
encountered, the `guac_error` variable is set appropriately, and
`guac_error_message` contains a statically-allocated human-readable string
describing the context of the error. These variables intentionally mimic the
functionality provided by `errno` and `errno.h`.

Both `guac_error` and `guac_error_message` are defined within `error.h`. A
human-readable string describing the error indicated by `guac_error` can be
retrieved using `guac_status_string()`, which is also statically allocated.

If functions defined within client plugins set `guac_error` and
`guac_error_message` appropriately when errors are encountered, the messages
logged to syslog by guacd will be more meaningful for both users and
developers.

## Client plugins[#](#client-plugins "Link to this heading")

Client plugins are libraries which follow specific conventions such that they
can be loaded dynamically by guacd. All client plugins *must*:

1. Follow a naming convention, where the name of the library is
   `libguac-client-PROTOCOL`. *This is necessary for guacd to locate
   the library for a requested protocol.*
2. Be linked against libguac, the library used by guacd to handle the Guacamole
   protocol. The structures which are given to functions invoked by guacd are
   defined by libguac, and are expected to be manipulated via the functions
   provided by libguac or as otherwise documented within the structure itself.
   *Communication between guacd and client plugins is only possible if they
   share the same core structural and functional definitions provided by
   libguac.*
3. Implement the standard entry point for client plugins, `guac_client_init()`,
   described in more detail below. It is this function which initializes the
   structures provided by guacd such that users can join and interact with the
   connection.

### Entry point[#](#entry-point "Link to this heading")

All client plugins must provide a function named `guac_client_init` which
accepts, as its sole argument, a pointer to a `guac_client` structure. This
function is similar in principle to the main() function of a C program, and it
is the responsibility of this function to initialize the provided structure as
necessary to begin the actual remote desktop connection, allow users to
join/leave, etc.

The provided `guac_client` will already have been initialized with handlers for
logging, the broadcast socket, etc. The absolutely critical pieces which must
be provided by `guac_client_init` are:

1. A handler for users which join the connection (`join_handler`). The join
   handler is also usually the most appropriate place for the actual remote
   desktop connection to be established.
2. A `NULL`-terminated set of argument names which the client plugin accepts,
   assigned to the args property of the given `guac_client`. As the handshake
   procedure is completed for each connecting user, these argument names will
   be presented as part of the handshake, and the values for those arguments
   will be passed to the join handler once the handshake completes.
3. A handler for users leaving the connection (`leave_handler`), if any
   cleanup, updates, etc. are required.
4. A handler for freeing the data associated with the `guac_client` after the
   connection has terminated (`free_handler`). If your plugin will allocate any
   data at all, implementing the free handler is necessary to avoid memory leaks.

If `guac_client_init` returns successfully, guacd will proceed with allowing
the first use to join the connection, and the rest of the plugin lifecycle
commences.

### Joining/leaving a connection[#](#joining-leaving-a-connection "Link to this heading")

Whenever a user joins a connection, including the very first user of a
connection (the user which is establishing the remote desktop connection in the
first place), the join handler of the `guac_client` will be invoked. This
handler is provided with the `guac_user` structure representing the user that
just joined, along with the arguments provided during the handshake procedure:

```
int join_handler(guac_user* user, int argc, char** argv) {
    /* Synchronize display state, init the user, etc. */
}

...

/* Within guac_client_init  */
client->join_handler = join_handler;
```

As the parameters and user information provided during the Guacamole protocol
handshake are often required to be known before the remote desktop connection
can be established, the join handler is usually the best place to create a
thread which establishes the remote desktop connection and updates the display
accordingly.

If necessary, the user which first established the connection can be
distinguished from all other users by the owner flag of `guac_user`, which will
be set to a non-zero value.

Once a user has disconnected, the leave handler of `guac_client` will be
invoked. Just as with the join handler, this handler is provided the
`guac_user` structure of the user that disconnected. The `guac_user` structure
will be freed immediately after the handler completes:

```
int leave_handler(guac_user* user) {
    /* Free user-specific data and clean up */
}

...

/* Within guac_client_init  */
client->leave_handler = leave_handler;
```

### Termination[#](#termination "Link to this heading")

Once the last user of a connection has left, guacd will begin freeing resources
allocated to that connection, invoking the free handler of the `guac_client`.
At this point, the “leave” handler has been invoked for all previous users. All
that remains is for the client plugin to free any remaining data that it
allocated, such that guacd can clean up the rest:

```
int free_handler(guac_client* client) {
    /* Disconnect, free client-specific data, etc. */
}

...

/* Within guac_client_init  */
client->free_handler = free_handler;
```

## Layers and buffers[#](#layers-and-buffers "Link to this heading")

The main operand of all drawing instructions is the layer, represented within
libguac by the `guac_layer` structure. Each `guac_layer` is normally allocated
using `guac_client_alloc_layer()` or `guac_client_alloc_buffer()`, depending on
whether a layer or buffer is desired, and freed with `guac_client_free_layer()`
or `guac_client_free_buffer()`.

Important

Care must be taken to invoke the allocate and free pairs of each type of layer
correctly. `guac_client_free_layer()` should only be used to free layers
allocated with `guac_client_alloc_layer()`, and `guac_client_free_buffer()`
should only be used to free layers allocated with `guac_client_alloc_buffer()`,
all called using the same instance of `guac_client`.

If these restrictions are not observed, the effect of invoking these functions
is undefined.

Using these layer management functions allows you to reuse existing layers or
buffers after their original purpose has expired, thus conserving resources on
the client side, as allocation of new layers within the remote client is a
relatively expensive operation.

It is through layers and buffers that Guacamole provides support for
hardware-accelerated compositing and cached updates. Creative use of layers and
buffers leads to efficient updates on the client side, which usually translates
into speed and responsiveness.

Regardless of whether you allocate new layers or buffers, there is always one
layer guaranteed to be present: the default layer, represented by libguac as
`GUAC_DEFAULT_LAYER`. If you only wish to affect the main display of the
connected client somehow, this is the layer you want to use as the operand of
your drawing instruction.

## Streams[#](#streams "Link to this heading")

In addition to drawing, the Guacamole protocol supports streaming of arbitrary
data. The main operand of all streaming instructions is the stream, represented
within libguac by the `guac_stream` structure. Each `guac_stream` exists
either at the user or client levels, depending on whether the stream is
intended to be broadcast to all users or just one, and is thus allocated using
either `guac_client_alloc_stream()` or `guac_user_alloc_stream()`.
Explicitly-allocated streams must eventually be freed with
`guac_client_free_stream()` or `guac_user_free_stream()`.

Important

Just as with layers, care must be taken to invoke the allocate and free pairs
correctly for each explicitly-allocated stream. `guac_client_free_stream()`
should only be used to free streams allocated with
`guac_client_alloc_stream()`, and `guac_user_free_stream()` should only be used
to free streams allocated with `guac_user_alloc_stream()`.

If these restrictions are not observed, the effect of invoking these functions
is undefined.

Streams are the means by which data is transmitted for clipboard (via the
[“clipboard” instruction](protocol-reference.html#clipboard-instruction "clipboard")), audio (via the [“audio”
instruction](protocol-reference.html#audio-instruction "audio")), and even the images which make up typical
drawing operations (via the [“img” instruction](protocol-reference.html#img-instruction "img")). They will
either be allocated for you, when an inbound stream is received from a user, or
allocated manually, when an outbound stream needs to be sent to a user. As with
`guac_client` and `guac_user`, each `guac_stream` has a set of handlers which
correspond to instructions received related to streams. These instructions are
documented in more detail in [Streams and objects](guacamole-protocol.html#guacamole-protocol-streaming) and
[Guacamole protocol reference](protocol-reference.html).

## Sending instructions[#](#sending-instructions "Link to this heading")

All drawing in Guacamole is accomplished through the sending of instructions to
the connected client using the Guacamole protocol. The same goes for streaming
audio, video, or file content. All features and content supported by Guacamole
ultimately reduce to one or more instructions which are part of the documented
protocol.

Most drawing using libguac is done using Cairo functions on a `cairo_surface_t`
(see the Cairo API documentation) which is later streamed to the client using
an img instruction and subsequent blob instructions, sent via
`guac_client_stream_png()`. Cairo was chosen as a dependency of libguac to
provide developers an existing and stable means of drawing to image buffers
which will ultimately be sent as easy-to-digest PNG images.

The Guacamole protocol also supports drawing primitives similar to those
present in the Cairo API and HTML5’s canvas tag. These instructions are
documented individually in the Guacamole Protocol Reference in a section
dedicated to drawing instructions, and like all Guacamole protocol
instructions, each instruction has a corresponding function in libguac
following the naming convention `guac_protocol_send_OPCODE()`.

Each protocol function takes a `guac_socket` as an argument, which is the
buffered I/O object used by libguac. For each active connection, there are two
important types of `guac_socket` instance: the broadcast socket, which exists
at the client level within the `guac_client`, and the per-user socket, which is
accessible within each `guac_user`. Data sent along the client-level broadcast
socket will be sent to all connected users beneath that `guac_client`, while
data sent along a user-level socket will be sent only to that user.

For example, to send a “size” instruction to all connected users via the
client-level broadcast socket, you could invoke:

```
guac_protocol_send_size(client->socket, GUAC_DEFAULT_LAYER, 1024, 768);
```

Or, if the instruction is only relevant to a particular user, the socket
associated with that user can be used instead:

```
guac_protocol_send_size(user->socket, GUAC_DEFAULT_LAYER, 1024, 768);
```

The sockets provided by libguac are threadsafe at the protocol level.
Instructions written to a socket by multiple threads are guaranteed to be
written atomically with respect to that socket.

## Event handling[#](#event-handling "Link to this heading")

Generally, as guacd receives instructions from the connected client, it invokes
event handlers if set within the associated `guac_user` or `guac_client`,
depending on the nature of the event. Most events are user-specific, and thus
the event handlers reside within the `guac_user` structure, but there are
client-specific events as well, such as a user joining or leaving the current
connection. Event handlers typically correspond to Guacamole protocol
instructions received over the socket by a connected user, which in turn
correspond to events which occur on the client side.

### Key events[#](#key-events "Link to this heading")

When keys are pressed or released on the client side, the client sends key
instructions to the server. These instructions are parsed and handled by
calling the key event handler installed in the `key_handler` member of the
`guac_user`. This key handler is given the keysym of the key that was changed,
and a boolean value indicating whether the key was pressed or released.

```
int key_handler(guac_user* user, int keysym, int pressed) {
    /* Do something */
}

...

/* Within the "join" handler of guac_client */
user->key_handler = key_handler;
```

### Mouse events[#](#mouse-events "Link to this heading")

When the mouse is moved, and buttons are pressed or released, the client sends
mouse instructions to the server. These instructions are parsed and handled by
calling the mouse event handler installed in the `mouse_handler` member of the
`guac_user`. This mouse handler is given the current X and Y coordinates of the
mouse pointer, as well as a mask indicating which buttons are pressed and which
are released.

```
int mouse_handler(guac_user* user, int x, int y, int button_mask) {
    /* Do something */
}

...

/* Within the "join" handler of guac_client */
user->mouse_handler = mouse_handler;
```

The file `client.h` also defines the mask of each button for convenience:

`GUAC_CLIENT_MOUSE_LEFT`
:   The left mouse button, set when pressed.

`GUAC_CLIENT_MOUSE_MIDDLE`
:   The middle mouse button, set when pressed.

`GUAC_CLIENT_MOUSE_RIGHT`
:   The right mouse button, set when pressed.

`GUAC_CLIENT_MOUSE_UP`
:   The button corresponding to one scroll in the upwards direction of the mouse
    scroll wheel, set when scrolled.

`GUAC_CLIENT_MOUSE_DOWN`
:   The button corresponding to one scroll in the downwards direction of the
    mouse scroll wheel, set when scrolled.

### Clipboard, file, and other stream events[#](#clipboard-file-and-other-stream-events "Link to this heading")

If a connected user sends data which should be sent to the clipboard of the
remote desktop, guacd will trigger the clipboard handler installed in the
`clipboard_handler` member of the `guac_user` associated with that user.

```
int clipboard_handler(guac_user* user, guac_stream* stream, char* mimetype) {
    /* Do something */
}

...

/* Within the "join" handler of guac_client */
user->clipboard_handler = clipboard_handler;
```

The handler is expected to assign further handlers to the provided
`guac_stream` as necessary, such that the [“blob”](protocol-reference.html#blob-instruction "blob") and
[“end”](protocol-reference.html#end-instruction "end") instructions received along the stream can be handled.
A similar handler is provided for received files:

```
int file_handler(guac_user* user, guac_stream* stream,
        char* mimetype, char* filename) {
    /* Do something */
}

...

/* Within the "join" handler of guac_client */
user->file_handler = file_handler;
```

This pattern continues for all other types of streams which can be received
from a user. The instruction which begins the stream has a corresponding
handler within `guac_user`, and the metadata describing that stream and
provided with the instruction is included within the parameters passed to that
handler.

These handlers are, of course, optional. If any type of stream lacks a
corresponding handler, guacd will automatically close the stream and respond
with an [“ack” instruction](protocol-reference.html#ack-instruction "ack") and appropriate error code,
informing the user’s Guacamole client that the stream is unsupported.

Contents

---
# Using TOTP for multi-factor authentication

## Contents

# Using TOTP for multi-factor authentication[#](#using-totp-for-multi-factor-authentication "Link to this heading")

Guacamole supports TOTP as a second authentication factor, layered on top of
any other authentication extension, including those available from the main
project website, providing [base requirements for key storage and
enrollment](#totp-prerequisites) are met. The TOTP authentication extension
allows users to be additionally verified against a user-specific and secret key
generated during [enrollment of their authentication device](#totp-enrollment).

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Prerequisites[#](#prerequisites "Link to this heading")

The enrollment process used by Guacamole’s TOTP support needs to be able
to store an automatically-generated key within the user’s account.
Another extension must be installed which supports storage of arbitrary
data from other extensions. *Currently the only extensions provided with
Guacamole which support this kind of storage are the [database
authentication extensions](jdbc-auth.html).*

It is thus recommended that authentication against a database be fully
configured prior to setting up TOTP. Instructions walking through the setup of
database authentication for Guacamole are provided in [Database authentication](jdbc-auth.html).

## How TOTP works with Guacamole[#](#how-totp-works-with-guacamole "Link to this heading")

Guacamole provides support for TOTP as a second authentication factor. To make
use of the TOTP authentication extension, some other authentication mechanism
will need be configured, as well. When a user attempts to log into Guacamole,
other installed authentication methods will be queried first:

![](assets/doc_gug__images_totp-auth-factor-1.png)

Only after authentication has succeeded with one of those methods will
Guacamole prompt the user to further verify their identity with an
authentication code:

![](assets/doc_gug__images_totp-auth-factor-2.png)

If both the initial authentication attempt and verification using TOTP succeed,
the user will be allowed in. If either mechanism fails, access to Guacamole is
denied.

### Enrollment[#](#enrollment "Link to this heading")

If the user does not yet have a TOTP key associated with their account (they
have not yet completed enrollment), they will be required to enroll an
authentication device after passing the first authentication factor. A QR code
containing an automatically-generated key will be presented to the user to be
scanned by their authentication app or device:

![](assets/doc_gug__images_totp-enroll.png)

If the authentication device does not support scanning QR codes for enrollment,
the details within the QR code can be revealed by clicking the “Show” link next
to the “Details” header. These values can then be entered manually:

![](assets/doc_gug__images_totp-enroll-detail.png)

Enrollment is completed once the user enters a valid authentication code
generated by their device using the provided key.

Important

If the user does not confirm/complete the enrollment process, the next time the
user logs in they will be asked to go through the enrollment process, again, and
the TOTP data will be regenerated. This means the previously-scanned QR code
and TOTP codes generated with the use of that code will be invalid.

### Reseting TOTP Data[#](#reseting-totp-data "Link to this heading")

It may become necessary for certain users to clear their TOTP key and/or force
them to re-confirm enrollment, such as in situations where a user loses their
phone and needs to reconfigure TOTP. The user’s existing TOTP key can be cleared
by checking the “Clear TOTP secret” box in the user interface and then saving the
user configuration. The next time that the user logs in, they will be given a new
key (QR code) and forced to re-enroll.

If you simply want a user to be able to re-configure an existing key, without
resetting the secret, you can un-check the box marked “TOTP key confirmed” and
save the user configuration, and the user will be presented with the QR code
at next login and asked to confirm it.

### Disabling TOTP for users or groups[#](#disabling-totp-for-users-or-groups "Link to this heading")

In versions of Guacamole prior to 1.6.0, installing and configuring the TOTP
module meant that all Guacamole users would be required to enroll in and
successfully authenticate via the TOTP factor. Starting with 1.6.0 the TOTP
requirement can be disabled on a per-user or per-group basis, allowing
administrators more flexibility in configuring the TOTP requirement.

By default all users will still be required to authenticate with TOTP, however
the requirement can be disabled by checking the “Disable TOTP” checkbox. This
can be done for an individual user account, but it can also be disabled for a
group resulting in the TOTP requirement being disabled for any members of the
group.

![](assets/doc_gug__images_totp-user-config.png)

![](assets/doc_gug__images_totp-group-config.png)

## Installing/Enabling the TOTP extension[#](#installing-enabling-the-totp-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-totp-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-totp-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-totp-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `TOTP_ENABLED` environment variable:

    ```
    TOTP_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e TOTP_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `TOTP_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `TOTP_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Configuration (optional)[#](#configuration-optional "Link to this heading")

Native Webapp (Tomcat)

With the exception of [the storage and permission requirements described
above](#totp-prerequisites), the TOTP extension should work out-of-the-box
without any additional configuration. Defaults have been chosen for all
configuration parameters such that the TOTP extension will be compatible with
Google Authenticator and similar, popular TOTP implementations.

Warning

Some TOTP applications *assume these defaults* and *silently ignore any other
values*. **Google Authenticator is such an application.** Be sure your
authenticator application supports the values you intend to use before
overriding the defaults.

`totp-issuer`
:   The human-readable name of the entity issuing user accounts. If not
    specified, “Apache Guacamole” will be used by default.

`totp-digits`
:   The number of digits which should be included in each generated TOTP code.
    Legal values are 6, 7, or 8. By default, 6-digit codes are generated.

`totp-period`
:   The duration that each generated code should remain valid, in seconds. By
    default, each code remains valid for 30 seconds.

`totp-mode`
:   The hash algorithm that should be used to generate TOTP codes. Legal values
    are “sha1”, “sha256”, and “sha512”. By default, “sha1” is used.

Container (Docker)

With the exception of [the storage and permission requirements described
above](#totp-prerequisites), the TOTP extension should work out-of-the-box
without any additional configuration. Defaults have been chosen for all
configuration parameters such that the TOTP extension will be compatible with
Google Authenticator and similar, popular TOTP implementations.

Warning

Some TOTP applications *assume these defaults* and *silently ignore any other
values*. **Google Authenticator is such an application.** Be sure your
authenticator application supports the values you intend to use before
overriding the defaults.

`TOTP_ISSUER`
:   The human-readable name of the entity issuing user accounts. If not
    specified, “Apache Guacamole” will be used by default.

`TOTP_DIGITS`
:   The number of digits which should be included in each generated TOTP code.
    Legal values are 6, 7, or 8. By default, 6-digit codes are generated.

`TOTP_PERIOD`
:   The duration that each generated code should remain valid, in seconds. By
    default, each code remains valid for 30 seconds.

`TOTP_MODE`
:   The hash algorithm that should be used to generate TOTP codes. Legal values
    are “sha1”, “sha256”, and “sha512”. By default, “sha1” is used.

### Bypass/Enforce TOTP for Specific Hosts[#](#bypass-enforce-totp-for-specific-hosts "Link to this heading")

Native Webapp (Tomcat)

By default, when the TOTP module is enabled, TOTP-based MFA will be enforced for
all users that attempt to log in to Guacamole, regardless of where they are
connecting from. Depending on your use case, it may be necessary to narrow this
behavior and only enforce TOTP-based MFA for certain hosts and bypass it for
others.

Warning

If you will be configuring Guacamole to consider users’ IP addresses, **it is
important to make sure that Guacamole is receiving correct IP address
information for all clients**.

If Guacamole is behind a reverse proxy, such as for SSL termination, the IP
addresses of all users will appear to be the IP address of the proxy unless
additional configuration steps are taken. **Be sure to follow [the
documentation for configuring forwarding of client IP
information](reverse-proxy.html)!**

TOTP-based MFA can be explicitly bypassed or enforced on a per-host basis by
providing the relevant, exhaustive list of addresses/networks using either
of the following properties:

`totp-bypass-hosts`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD NOT be required to verify themselves using TOTP when
    authenticating. All other hosts in this list will required to verify with
    TOTP.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and this property is effectively ignored.**

    This property is optional. By default, verification will be required for all
    users regardless of their IP address (TOTP is not bypassed for any
    addresses).

`totp-enforce-hosts`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD be required to verify themselves using TOTP when authenticating.
    All other hosts will not be required to verify with TOTP.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and the bypass list is effectively ignored.**

    This property is optional. By default, verification will be required for all
    users regardless of their IP address (TOTP is enforced for all addresses).

Container (Docker)

By default, when the TOTP module is enabled, TOTP-based MFA will be enforced for
all users that attempt to log in to Guacamole, regardless of where they are
connecting from. Depending on your use case, it may be necessary to narrow this
behavior and only enforce TOTP-based MFA for certain hosts and bypass it for
others.

Warning

If you will be configuring Guacamole to consider users’ IP addresses, **it is
important to make sure that Guacamole is receiving correct IP address
information for all clients**.

If Guacamole is behind a reverse proxy, such as for SSL termination, the IP
addresses of all users will appear to be the IP address of the proxy unless
additional configuration steps are taken. **Be sure to follow [the
documentation for configuring forwarding of client IP
information](reverse-proxy.html)!**

TOTP-based MFA can be explicitly bypassed or enforced on a per-host basis by
providing the relevant, exhaustive list of addresses/networks using either
of the following environment variables:

`TOTP_BYPASS_HOSTS`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD NOT be required to verify themselves using TOTP when
    authenticating. All other hosts in this list will required to verify with
    TOTP.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and this property is effectively ignored.**

    This property is optional. By default, verification will be required for all
    users regardless of their IP address (TOTP is not bypassed for any
    addresses).

`TOTP_ENFORCE_HOSTS`
:   A comma-separated list of all IP addresses and/or subnets (in CIDR notation)
    that SHOULD be required to verify themselves using TOTP when authenticating.
    All other hosts will not be required to verify with TOTP.

    **If both bypass and enforce lists are provided, the enforce list takes
    priority and the bypass list is effectively ignored.**

    This property is optional. By default, verification will be required for all
    users regardless of their IP address (TOTP is enforced for all addresses).

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# Securing Guacamole against brute-force attacks

## Contents

# Securing Guacamole against brute-force attacks[#](#securing-guacamole-against-brute-force-attacks "Link to this heading")

Version 1.6.0 of Guacamole introduces an extension that allows you to detect
and block brute-force login attacks. When installed, the extension will track
the IP addresses of failed authentication attempts. Once the threshold of
failed logins is reached for a particular IP address, further logins from that
address will be temporarily banned:

![](assets/doc_gug__images_too-many-failed-logins.png)

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## Installing/Enabling brute-force authentication detection[#](#installing-enabling-brute-force-authentication-detection "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-auth-ban-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-auth-ban-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-auth-ban-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

**This extension is enabled by default when using the Docker image.** You do
not need to do anything to use this extension with Docker unless you wish to
override the default behavior. If you *don’t* wish to use this extension, you
can disable it by setting `BAN_ENABLED` to `false`.

If deploying Guacamole using Docker Compose:
:   This is accomplished by adding the `BAN_ENABLED` environment
    variable to the `environment` section of your `guacamole/guacamole` container:

    ```
    BAN_ENABLED: "false"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   This extension can be disabled by providing the same environment variable
    using the `-e` option. For example:

    ```
    $ docker run --name some-guacamole \
        -e BAN_ENABLED="false" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `BAN_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `BAN_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

## Configuration (optional)[#](#configuration-optional "Link to this heading")

Native Webapp (Tomcat)

This extension has no required properties. So long as you are satisfied
with the default behavior/values noted below, this extension requires no
configuration beyond installation.

Default brute-force authentication detection threshold and limits[#](#id1 "Link to this table")

|  |  |
| --- | --- |
| Maximum invalid attempts (authentication failures) | 5 |
| Address ban duration | 300 (5 minutes) |
| Maximum addresses tracked | 10485670 |

`ban-max-invalid-attempts`
:   The number of authentication failures ater which the extension will block
    further logins from the client IP address. This property is optional and
    the default is 5.

`ban-address-duration`
:   The length of time for which a client IP address will be denied logins
    after the maximum authentication failures, in seconds. This property is
    optional and has a default value of 300 seconds (five minutes).

`ban-max-addresses`
:   The maximum number of client IP addresses that the extension will track
    in-memory before the oldest client IP is discarded in a Least-Recently
    Used (LRU) fashion. This property is optional and has a default value
    of 10485670 (10 million IP addresses).

Container (Docker)

This extension has no required environment variables. So long as you are satisfied
with the default behavior/values noted below, this extension requires no
configuration beyond installation.

Default brute-force authentication detection threshold and limits[#](#id2 "Link to this table")

|  |  |
| --- | --- |
| Maximum invalid attempts (authentication failures) | 5 |
| Address ban duration | 300 (5 minutes) |
| Maximum addresses tracked | 10485670 |

`BAN_MAX_INVALID_ATTEMPTS`
:   The number of authentication failures ater which the extension will block
    further logins from the client IP address. This property is optional and
    the default is 5.

`BAN_ADDRESS_DURATION`
:   The length of time for which a client IP address will be denied logins
    after the maximum authentication failures, in seconds. This property is
    optional and has a default value of 300 seconds (five minutes).

`BAN_MAX_ADDRESSES`
:   The maximum number of client IP addresses that the extension will track
    in-memory before the oldest client IP is discarded in a Least-Recently
    Used (LRU) fashion. This property is optional and has a default value
    of 10485670 (10 million IP addresses).

Important

Because the extension tracks authentication failures based on the client
IP address, it is important to make sure that Guacamole is receiving the
correct IP addresses for the clients. This is particularly noteworthy
when Guacamole is behind a reverse proxy. See the manual page on
[proxying Guacamole](reverse-proxy.html) for more details on configuring
Guacamole behind a proxy.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

Contents

---
# Viewing session recordings in-browser

## Contents

# Viewing session recordings in-browser[#](#viewing-session-recordings-in-browser "Link to this heading")

Guacamole supports [recording activity within remote desktop sessions](configuring-guacamole.html#graphical-recording)
such that it can be played back and reviewed later. Graphical recordings can be
converted to video [using the `guacenc` tool](configuring-guacamole.html#graphical-recording) (part of
[guacamole-server](guacamole-native.html#building-guacamole-server)) or can be played back directly
in the browser in their native format using Guacamole itself. This has several
benefits:

* Recordings can be played back while the session is underway.
* Recordings need not be re-encoded as traditional video, an
  intensive process that often results in a larger file.
* It is very easy to locate and play back the recording for a session when
  doing so only involves clicking a button in the connection history.

This chapter of the documentation covers installing and using the extension
that allows recordings stored on disk to be played back in the browser.

Warning

You will need to restart the Guacamole web application in order to complete
configuration. Doing this will disconnect all active users, so please:

* **Do this only at a time that you can tolerate service unavailability**, such
  as a scheduled maintenance window.
* Keep in mind that **configuration errors may prevent Guacamole from starting
  back up**.

## How recording storage and playback works[#](#how-recording-storage-and-playback-works "Link to this heading")

The Guacamole web application includes its own support for playing back
recordings from the history screen in the administration interface, but that
support cannot automatically know where those recordings are stored nor how
they are named. The extension documented here provides exactly that missing
piece, allowing the web application to find recordings on disk so long as they
are named appropriately and stored in a specific location.

Each history entry has a deterministic, internal, unique identifier called its
UUID, and all supported database backends make this UUID available ahead of
time with the `${HISTORY_UUID}` parameter token. This provides a reliable way
for data stored *outside* the database to be associated with history entries
that are otherwise stored purely *inside* the database, and it is this UUID
that the extension searches for when locating the recording for a history entry.

When a user lists the history of a connection, the recording storage extension
additionally [searches a predetermined location](#recording-storage-config) for
session recordings that match either of the following criteria:

* The recording’s filename is *identical* to the history entry UUID and is
  directly within the search path.
* The recording has any name at all and is within a directory whose filename is
  identical to the history entry UUID and is directly within the search path.

If such a recording is found, it is made available to any user that can view
the history entry. The availability of a recording is displayed as a “View”
link in the “Logs” column of the history table:

![View link in the history UI](_images/history-table-with-recordings.png)

Clicking on that link navigates to a screen with a player that loads the
recording and allows it to be played back:

![In-browser player interface](assets/doc_gug__images_recording-player-in-use.png)

Version 1.6.0 of Guacamole introduces a feature that allows for key events
in the recording to be displayed in a format similar to the guaclog utility,
making it easy for administrators to scroll or search through the output
for key events. The amount and type of data shown in this output will
depend upon the options selected when recording is enabled - for example,
keystrokes will not be available if keystroke logging has not been
enabled for a connection.

Additionally, heatmaps of screen update activity and key events (if captured)
will be displayed when the progress bar is hovered.

![Display and search key events](assets/doc_gug__images_player-key-events.png)

## Installing/Enabling the recording storage extension[#](#installing-enabling-the-recording-storage-extension "Link to this heading")

Guacamole is configured differently depending on whether Guacamole was
[installed natively](installing-guacamole.html) or [using the provided Docker
images](guacamole-docker.html). The documentation here covers both methods.

Native Webapp (Tomcat)

Native installations of Guacamole under [Apache Tomcat](https://tomcat.apache.org/)
or similar are configured by modifying the contents of `GUACAMOLE_HOME`
([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)), which is located at
`/etc/guacamole` by default and may need to be created first:

1. Download [`guacamole-history-recording-storage-1.6.0.tar.gz`](https://apache.org/dyn/closer.lua/guacamole/1.6.0/binary/guacamole-history-recording-storage-1.6.0.tar.gz?action=download) from [the release page for
   Apache Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0)
   and extract it.
2. Create the `GUACAMOLE_HOME/extensions` directory, if it does not already
   exist.
3. Copy the `guacamole-history-recording-storage-1.6.0.jar` file from the contents of the
   archive to `GUACAMOLE_HOME/extensions/`.
4. Proceed with the configuring Guacamole for the newly installed extension as
   described below. The extension will be loaded after Guacamole has been
   restarted.

Note

Download and documentation links for all officially supported extensions for a
particular version of Guacamole are always provided in the release notes for
that version. The copy of the documentation you are reading now is from [Apache
Guacamole 1.6.0](https://guacamole.apache.org/releases/1.6.0).

**If you are using a different version of Guacamole, please locate that version
within [the release archives](https://guacamole.apache.org/releases/) and
consult the documentation for that release instead.**

Container (Docker)

Docker installations of Guacamole include a bundled copy of [Apache
Tomcat](https://tomcat.apache.org/) and are configured using environment
variables. The startup process of the Docker image automatically populates
`GUACAMOLE_HOME` ([Guacamole’s configuration directory](configuring-guacamole.html#guacamole-home)) based
on the values of these variables.

If deploying Guacamole using Docker Compose:
:   You will need to add at least one relevant environment variable to the
    `environment` section of your `guacamole/guacamole` container, such as the
    `RECORDING_ENABLED` environment variable:

    ```
    RECORDING_ENABLED: "true"
    ```

If instead deploying Guacamole by running `docker run` manually:
:   The same environment variable(s) will need to be provided using the `-e`
    option. For example:

    ```
    $ docker run --name some-guacamole \
        -e RECORDING_ENABLED="true" \
        -d -p 8080:8080 guacamole/guacamole
    ```

If `RECORDING_ENABLED` is set to `false`, the extension will NOT be
installed, even if other related environment variables have been set. This can
be used to temporarily disable usage of an extension without needing to remove
all other related configuration.

You don’t strictly need to set `RECORDING_ENABLED` if other related
environment variables are provided, but the extension will be installed only if
at least *one* related environment variable is set.

### Preparing a directory for recording storage[#](#preparing-a-directory-for-recording-storage "Link to this heading")

By default, the recording storage extension will search within
`/var/lib/guacamole/recordings` for the recordings associated with a
connection. Unless you or a third-party installation tool have created this
directory, this directory will not exist and you will need to create it
manually:

```
$ mkdir -p /var/lib/guacamole/recordings
```

You can also use another directory of your own choosing if you
[override the default location using the `recording-search-path`
property](#recording-storage-config).

Important

The following steps will use `/var/lib/guacamole/recordings`, as it is a
sensible location and the default search path. If you are using a different
path, consider `/var/lib/guacamole/recordings` below to be a placeholder and
use your own path instead.

Once the path has been created, its permissions and ownerships must be modified
such that *both of the following are true*:

* The guacd service can write to the directory.
* The servlet container (typically Tomcat) can read from the directory, as well
  as read any files that are placed within the directory.

The simplest way to do this is to ensure that:

1. The directory is owned by the user that runs the guacd service and the
   *group* that runs the Tomcat service.
2. The directory has read/write/execute permissions for the user (so that guacd
   can write here), and read/execute/**setgid** permissions for the group (so
   that Tomcat can read here, and so that [any files placed here are automatically
   owned by the Tomcat user’s group](https://en.wikipedia.org/wiki/Setuid#When_set_on_a_directory)).

For example, if your guacd service runs as a dedicated `guacd` user, and your
Tomcat service runs as a user within the `tomcat` group:

```
$ chown guacd:tomcat /var/lib/guacamole/recordings
$ chmod 2750 /var/lib/guacamole/recordings
```

If set correctly, the ownerships and permissions should look like:

```
$ ls -ld /var/lib/guacamole/recordings
drwxr-s---. 1 guacd tomcat 0 Feb  5 05:43 /var/lib/guacamole/recordings/
$
```

Note

If using this extension within a Docker container, you will need to use volumes
to make an external directory available to **both** the `guacamole/guacd`
container and the `guacamole/guacamole` container.

Regardless of what users and groups are already present on the host system, the
UID and GID values that apply to permissions in this case will be the UIDs and
GIDs used by the containers. The UIDs and GIDs used by the provided Docker
images are as follows:

| Image name | User | UID | Group | GID |
| --- | --- | --- | --- | --- |
| `guacamole/guacamole` | `tomcat` | 1000 | `tomcat` | 1000 |
| `guacamole/guacd` | `guacd` | 1001 | `guacd` | 1001 |

The UID and GID values used by the containers will not necessarily align with
the values already used by your system.

## Configuration (optional)[#](#configuration-optional "Link to this heading")

Native Webapp (Tomcat)

`recording-search-path`
:   The directory to search for associated session recordings. This property is
    optional. By default, `/var/lib/guacamole/recordings` will be used.

Container (Docker)

`RECORDING_SEARCH_PATH`
:   The directory to search for associated session recordings. This property is
    optional. By default, `/var/lib/guacamole/recordings` will be used.

## Completing installation[#](#completing-installation "Link to this heading")

Native Webapp (Tomcat)

Guacamole will only reread its configuration and load newly-installed
extensions during startup, so Tomcat will need to be restarted before these
changes can take effect. Restart Tomcat and give the new functionality a try.

*You do not need to restart guacd*.

Hint

If Guacamole does not come back online after restarting Tomcat, **check the
logs**. Configuration problems may prevent Guacamole from starting up, and any
such errors will be recorded in Tomcat’s logs.

Container (Docker)

The environment variables that configure the behavior of Docker can only be set
at the time the Docker container is created. To apply these configuration
changes, you will need to recreate the container.

If your Guacamole container was deployed using Docker Compose:
:   Simply making the desired changes to your `docker-compose.yml` and running
    `docker compose up` is sufficient. Docker Compose will automatically
    recognize that the environment variables of the container have changed and
    recreate it.

If your Guacamole container was deployed manually (using `docker run`):
:   You wll need to manually use `docker rm` to remove the old container and then
    manually recreate it with `docker run` and the new environment variables.

Hint

If Guacamole does not come back online after recreating the container, **check
the Docker logs**. Configuration problems may prevent Guacamole from starting
up, and any such errors will be recorded in the Docker logs for the Guacamole
container.

## Configuring connections to use recording storage[#](#configuring-connections-to-use-recording-storage "Link to this heading")

Recordings of connections can be found by the recording storage extension as
long as those connections are configured in either of two ways, each involving
naming a file or directory with the history UUID (`${HISTORY_UUID}`).

### Option 1: Using a subdirectory named with the history UUID (RECOMMENDED)[#](#option-1-using-a-subdirectory-named-with-the-history-uuid-recommended "Link to this heading")

If the recording path of a connection is set to
`${HISTORY_PATH}/${HISTORY_UUID}` and “automatically create path” is checked,
then the recording storage extension will be able to locate the recording by
recognizing that the directory is named with the UUID:

![Configuring session recording with the path containing the history UUID](assets/doc_gug__images_recording-storage-connection-config-option1-recommended.png)

**This is the recommended method of storing recordings.** This method is the
most flexible in that it allows other recordings like typescripts to be stored
within the same directory, and it allows recordings to be given *any* name,
including names that are more human-readable, contain [`${GUAC_DATE}` or
`${GUAC_TIME}` tokens](configuring-guacamole.html#parameter-tokens), etc.

Though the web application does not currently support in-browser playback of
typescripts, server logs, or other files that might be of interest to the
administrator looking at the history of a connection, it *does* recognize these
files. Following this method will allow any future support for playback of
other types of recordings to work even for old recordings.

### Option 2: Naming the recording with the history UUID[#](#option-2-naming-the-recording-with-the-history-uuid "Link to this heading")

If the recording path of a connection is set to `${HISTORY_PATH}` and the
recording name is set to `${HISTORY_UUID}`, the recording storage extension
will be able to locate the recording by recognizing that its name is identical
to the UUID:

![Configuring session recording with the name containing the history UUID](assets/doc_gug__images_recording-storage-connection-config-option2.png)

Contents

---
PNG

   
IHDR  @     U   bKGD       pHYs  .#  .#x?v   tIME ecv    IDATxuTUwjgwK@$G>v'ȣ`tҵvO 貜5/{n=~I"o-tZPo:t+V,ż\_X2+WnfbrŮ ^!Bi1IBk(H J$@D"(H$R %D
D"HH$)D"P"H J$@D"(H$R %D
D"HH$4(hB vsM hE Áa0 =`4hr:\.4&VxM&ϳӅaD"<\_fZ
fNCu8纜N{sð
,5쬋zfj5ؽgNcͲb.o)(]NϘJNV&N{SNC&),3Q8B˔q:ņ'TG!C"X0-'},w:L!:^7d\_KNvE=Etя3=+$T[xL2\_XlԪ' 燯#b= "}V|mԜGJH,"Xj2
sgONPpOxTt,Bt::fe݊Et=Hdf7@XBAL`,}MmV^|2ȨV%)(:f;inv=2(@H J.;7݂xN\lX@v]TUX"ll %\fDV9zY^rIQEG^7|oشF`-(`5T\\_j5Fn$Ք^D
7,Ǻ"cX8u+Өy[ fL!=U
U$&.t~b>
Gޅ\*;B$R  \.WB'hj
+3 'Fq:1yCn#.E!#-מ]7[ѸE[T-D
,qm֯{%,~G1oTL~^frٞ0\N'}6'i,Q?p-'d'!!X!+lm`'oq(v]{! WY m;\_;`H(!Xiֺ#[sPAf3Zw"XQ1 \\gDzKAZψ;`SO ":\_Dz0"<\*
AoGa2gY86t:=ajߍ7߭VI1K>t;B[
B/Ӂ(:O@]$,w{aǥ
6k;kD|R^`)=R'.y+Tq]½ >q#H$)D"P"H J$@D"(H$R %D
`98DB" `!dE)ι4;όH\_џ%2¿2$';;>n.q+^Ϟ훘C3"9v8gƎ@yٮK3CvoVPpv@s9VN=p0DӠi+6
+KAH%0<"
^OVf:7`afΞgdSFmtKO^G|˾ ';4lvs:dgep^Ϙ÷'';SBZ@EѦs V1\*NMB\*F')% !ؿg -v.
E,d=ȬI^w9kyW"/7^yTϿ\_@E^7u=.ocRAtcp~UWCQtkԢHnCɣdfi;])kA&rMK\rS^t ,+nfzmRq"٬dge|9ŮmٰY?$6 ;.8v
s9|3ZPv\O%+#\*جVOsg8&Y6H.J.5k^otmJl)اnQvjoĆٺO:Yrq~FUjT>z?})KcgEDұ[\_?buPKzU#a""|D}8rW>ʬiYbւ| ~^:IO=ﹾBqw?
 0xq޾W?u48i=u?Vk?6n{Dn#-o~#q0Ll^o?}=$4&-gʪ=/HZSS A]]מs1,I \_BРi+Zv?>p: kt80?c\*!zBfmH9w3`ܟ9u0o|>VFαC86lʞY:gfODP>yއ⻳s@,FZy>z??|SQsvmۀp0yذ!z;u6aǦ]>L  p:kܜ
y
6lIGҞ\_awxf׮GDP;NGԣ?!>yrhnbX8!q8dϙ?3打Nё#,[0QaSN8s@Fn}Xbގ@a0عe- M[GQ>[֮T&~W7i]oz=.%s~dT^7>N'cxٱ7Ңm\*\_^N6OPNC\Es!<=z8?OA7CxdE8qZEޝ[سcxw~~"gO~V8t:=v}φƧ/r8]Nn~7GdYsUjrҠi+t:=woSmӡtM@u8W"i)C0lZ#Uv+B|N?L~^QX83 .LKl|%\.c]XwV+1Xd.O[LMq:(&
]Y!sgNzLkji@XDtppnOr a8΢Q>:Q1qجVvP>2 3)\$NZcp:m6Zu㤏1Ms~bǯ3771Dp<"c} Znf-t|LU@JU٬8
iڪ-wA~TJ
LAfN9nxgn <"0;=s8mج8NJ=Ť\_O~ 2&ͦo}wpOz<6hH:FIܺnW{8ػS} m;r:Y$898Xss!/7ܜlr2׸% [a0ݫM5۬V5UlqB#2=syDFb '7;0OrJ'6>C((+ރoƩU%rS#"\*̌4n\ɠl, CTjm($I׮ 4jƫMANV&.n)ykč` 8RĻpԬSL9[ngnk\_>4iٮHf7XVZ +lT&yQΟ@#`-K-ꇨy.; Mf%ܲ>b0t7GZ<h\*&T#JZuIܺhپ˂\^x\*}j6]vS~wy=c\*2KSI@E>eg$n]ϩͦnæ>CCBhܢopphnEnæ=:=0\.z#B@8XE%tz@Hh(AAfr/Cڝ{,tzB,d
~TGi.7&8$Sǎ{FRϝyGNA087AS^ckmDucNfM\_c݊E,[]@%ހ1]]X"f pQasjآ?bPnCt^ނn
Cؼv9GGSN9 \*VF^^."x\_`Wnɜte
 Ɓ0WmP-D\lV+GUK,3 a
YӿtRqE ,Ǐ$V^qq:Xmc,Co\_;(
\*Wh2zDQtؐ\sp:hI7)\.St:ty \_;Ipk
ѤB+Or^NzuoFZ
O^~{$8]C7wfOc/vEI"/\rpmgfG}K}?u}0WD71$
p-btN-v`IvJ|BUgOBBxfttz=NsOyv ;=zIzy$HH6@F.=Y|!Y:׿b!rUΞ:@^7.B0{8u0gFy4o SP0Ϝdu?|[G?ʐx:Y -WC0`ԬېY7vX".z/ޙ@WrIfz\* c|-y\_XP7dӚe'=
ZMº˥{!TQwa!Q>z-;kԜKg>@#Ԭ׈:S4,Ͼ]0urq;9[ҬM''IܲsӨg.#\(fDۈ@tlrs׬UG6QGG):y?˒?iR6Z 
656\*@xd6'c؅PgED`3(
fs0OЪuE/4<"s=ۙ$>x ?NEF{Hߛ\*ԨCL\<4hڊ`&ړeyaOEzzI>ؼfO^<&Ot3ٴz)VIXx$\*VI-!\XBȪR.$/HH$\W$h4a XrY՗""\*^R^Onvf{![`4z\_@+ 
PP
9YEf5Eh2b ESxm&NbE}dr:GSSK6y!Ԫ\_>(BnN6y9XqY%"cb1NדIv;O`TGD7<)BzZ
ɬi[ KR7Dk=no/!C,TPCB:V?tl!|~`iX"c;DI6LDb!!PB,w^DFŔx?h4D"(H$R %D
D"HH$)9#B"xº!$)מ;.>D
``41cde]@$rZܟԥuH$R ;6fSN87FH Ea꥞B6]!
#H2Bg}s!:"D
`9F7i2ςnvoHVFz#I$)W;0D"xp$i/'[4'rs$)f#q:i$D
`h2|bÅpa3D"zI|AryPs$Qy˸Zd( p8v I@R!8lY+WW,wIzqΌ2R.Tu38ɮ.i)"t^/'  H]ҥ $ɨ&H$u1ML"^U$ΑK\_$L 0&H>rzC/| %Kܿ҄j?O"H:\_&|LR"\MT . H$W4rj~N]@ k.7Y"H
:g/ 5IJ$ϲhؼ\_LFdJJ$V|9sD"U"HH$)D"P"H J$@e&}vbPZvA-".0ǀ, ua>R9}|Y?Z -%?<#HkghLEnH~Ա"MJNo4kw< 7xcx^Eh]1XX5xX ޞ]&e| `K1/pzkw~'ԩ}QnkާNGηPKԅ^ v '4廓@ VkqK`btּڿ|:WwZ{]FA`@a-iDIZ7Nt-80tu{#ڹ:|3OiOBΝ n
ps٫ok%㣵2Q"] +Ptg'e| "%UBXv%OмXC-^{Oﮂm'V\*H+ܫ `8&-j<5EiC]p
YimhF`;nQVkzj׹Eow봿D&TJ^NЪhz<b1THwRMl\*A써p,$Unhq3p
P91us#oxH-=/k\_}
QgVμ=Ņr&B{DisVk)aO:Kzj:Ze#0SLv{頽x4Û7}&߬ q)k/j6ui^{ݛU\*
'@8    IDAT^pnM^Ǯ@ggPN^ͯ\*T5m]rߵ#GL] \*~{4[5/ӼR \ஞxZf4E;^[t\_j N^Z`#U'hUF'v׳j/wM?Ӆ yz=pA^dkyre 
ԼOoǥZBjZVؽ;g@<?~mtwO٨
5xQR=sOx۬5w-jPx/ʉ8Khk7|Z+\_zv L@wm:xCͻyvͣq6ת8)
PV^,جন+eW;=+ojq#iԃP{(F=cEfÍ~5O׼`:\_Z--'ݺ^Y;ȶ@d44CMg{jvNYun&Y~HמLUI$hma\_Tn\RΫPMY"}ۤTj[x[xj/ɫv~| jȾWCRfݼP^%c4s!NԼ'o@9'\y+e+1Jj!j\_% P4;8)!%\qZk?UJ}UGkՑyXGZZu»z-5/b&t8oo^|Q;jMy\*];L՚@[xţvF,Ԫ/aawJ{{)C~vD-`ZܞZu$nOmyND/G}qr)h\_SL|KTRF|G&H\<\_P|#H\_u@DKe܃OJSHHE# D"P"H J$@D"(H$R %]\ H$R $-Q7sҤj{zHԹg)y\*vt"Pj+M\*HBPWbl
,gG]X\*/.Hd̑
7{UT"\MD^+/DR"\7o4D"Zo
҄j:E;5JˎK$If%
zi:Dr4D")\h O\,\F8Iyd uGi?;1H$O) H./ڋ[6܄nR@{(ԍ@߽ s]k\_X=)a4a i>|&nc
9@MN{WXU U²#uR
gN;J /m5뗧l:LǩlN\_~鮆w.7ҝkq\*^}/m%;HNng,mE]?ct']WMop@-(J ""Bak\n'ޖah( D:Uu]b+% Zna-:?#o}^w)"|a|׽ヅIw&Vםlֻw\II3;oQr´aV?[MرE)U'H׮-\_M[>b'|`^' 1eKrW{͇z߳g϶/&Dj°Vvޥ0xJb Dhh!!D°#ͫT\*D6xǿdDjgvМ!!Sjڿ]&ի݋B\_`N?'v+fg%K>^Un\_N|;Тo\_5AAmۦuӄ%X}ӽ,$$-bkk!TRSE-'O.Bl-L&Qj6x?P}p:7ym,zݻbWX?~uG6Bm^aE\*/pu[EMdOs?Bl:HE q,kȑ>=}a2EBBbO(+l3fPEKbw:]ܭDuh4Utoȑ"&&B'ɋu,{[`Ћ(!NxΜJ}
ҥbu>8Bq˵+/QVeU +(X'Zj zw ɓ\_~y'II3EDD DfJt0")iOM{]("Cm9={=&v!+Ch\*c(@G`]BBX+NVlt:(df(
>aYYd$\*\*«欐C^^&p?b &,SNMpf!$3gRzLTAA&qEJJ&Bbc#0Źsi(6t fqq(Z"|⟕K~~AA&"#<ǧO\_O@Q4z#<< {>}EQl6-55!qqQt:=NwM
Bӭ눍MwffVL&ёŤ;Ѐb&<{td2+>}gfaJJDFFi.(4o>!sQOѣɤfDXX0The@R
\*ŲwRѓaOcG8C&޽5|K|1"P7x ua/:tAd
X! RJgdeRv6!Y'|CRzRIlizڵ
Nc"+k9DT/ի.22,BT#W$,?p`Wfgx%XoñICX,>aji\*rs׈FF?[&^]hT$Vѱc38& !Cf\*U{EQDhh/EN"(也N!!f8-SP`c˖F
7Y+ /C&TKzzKndU06|GM|]}СOql\*wSZKо?~6mr7[?}
f-[G^b22={%((+Avƍy/E 1Jry|s
~qq^gq\&Mj3bDo֭ʉgy̝zS'''GRz%b[1mBW~"S\:vlzn;zb1jvn=zco֞t9Nl6;˗oaҤߙkݮz/ 'TO
^|p ĨQ}/\_,11jxHxjrnqqQ~VR8<ޚBԬ Lb\_|i[n<\_8ͳu\_]rK\_F<^'>R 4l
(̘1y%
˯m..5Fjn]"MFSc{r)NǼyٻ0voNbOԭ[}!M&8ج^qqҼy寀Uɑ#GFFӿ'M[ɳyٱZiΣcfT^u#S N/\QZEmٳE:{UHwe7d/ܝg{O"߽+YzzBu$::EQ$<<Ȼ\9Jb
2(
j[jfjbc\_X`:-Z@
DDb0=ۻ6^hksX@Å(|SSUo;!B1aÚ^\_r'P[ny[nys.\*gL&#
⭷⭷nOgڴE<䇤eѹ;
˥
Ю#o$ @(
Ӧ-'kՄ \_Ox収={\_\_,/[fL(n 丠 {a<\_?u
QD4M&5!g\6\b<.AA&-r g\_[rZyA0?u׵b޼6{^@4F}=gQ,#.W:v> !xǩSvhٲ%u&+FL&iNΟ`mȧ 0.רQan]ʠAב'Pf~Nti~:4ҩxSikvFdX+|-e i׮1s?C/yF+
\E)/ iK7r ^|q4; x=>rd$$Lnn99y~k%5,"<ʕ|33LPA9H^; QPe=Kdd(~Yw6m:zRTDS((2dHRb1n06lΠAױxz'twƍka.S{g^-ТEt);eD/-[6iS}[1Ԗk21Musq \*V-l޼5aTϹsiE^Q/\˔-hqClm0t<w&|Q¯\9h 5^{@{VIqh][azN'S7.╍3gre\_ .w( eP k'>(J\_˿"::cNӫv:wo)23sPNdd(1dfh3G7y衷TC+mjOijKK\_g"XBA F]ר=3ӧSLvvg#`?رӄk%wV$'\_ /[c;6m&%}ʌKC(1!;; ,B-W?~={zQV
6ٳ|49D
tڱ]ڵkLfuaw4oc￯!7Wi.(@;`cժ$&t`v>Dַ{TR=AZZkl eeUo}7ި7an~X@&9pK0ǎ'88Grh֬.ǏƧđ     IDAT#ɴmۈwOc{y1tC̙'0dHzjGnn>gٲM,]%={2\_=qѩSs6mg׷a-Z.
,v(;F||o8wnz~#{ RV}~-<(\*Uzvzs~Ȁ]u$?JXXcnݪddr6-Z`\734cfkHbbo4yl-Z4w? nB>0
fXʙ3L2w}}PfZِ"0I/p}#V;JÆlQ~urYj#&&={f(̙'7$7܇~zT^;YowEc~}{E^ޚR!22:N4mZw 6mG6O֦%-&O~QG\7fPqBѤIѪUg EFj\Ӹq-1{{㏟UƋɓ'Fu{qQvkѻw{q|lO=uϔ(@~ ZT'c^ """4 "%e
Z5B],X
>8e⡇FסCS1wl\_DE0!"4Ss n)o;7R
h7FիW,rp1ذ;id|,>D\[jr\*anѼy=Qz%Q~ua/<:P=DDEOMŻ>ubɒE#/ w}TsRrʖmŷsC8Ξ=OA(BBBKِn 33|TIjd{5:}^AA>gϦRjEt:vNK=vDF^$zΞ=Pb|pXQ@zz\*TV+p\G\bGaO>fR8L&s);
Ը:uKPjWtjQ.5-9?NTT6UL))ϊ~K  rٲ%wOPq%rg]jO񼔸];\yv%Wl}{peO='\)=J %I)(md`Bfk\*$ɵ%fYJ"H; jW޻\^""(dgpĹpZڤxg\*Vu̘E$ˎ7ߜB#F=ʖx6H"\(dC{ LR$+˿ 4([D"#6
'Q<@eڝ!\7O"\Mʦ 6qs"̝3syι瞫ӫTְ(|]%o<|}WzJ~nI1X?V; Op[H衽pV{Pq56Ꮚ5AV\@J\*ܘ 5HUz Vj
\*n
DN:mMMfW0QCˬY?1p.F vZlAq+"v {:v27SU#ٱq5;7%П\_p3?A#¼dY&П}56L1Z
|6G#IK3L4\_X]);^{6P=.đTb6n9zqV\_J{P%2aOnILx3ɄWB#i8pUՈ:=o<a0wEx~3g\_WfU\?$IhZ
PӪ:u]vH"~.vo\_0s&X;N7J
tzdBtzC)d0z٬=<EA`pL\9dtzՂ,=0=
rXk\*V`馣i3аI+
7I T KFCaA>ZݥhZlWqL 6Pv,b67juS$:=ET(h4E3\*܃ OhUCݾ(I;'U#kQ. < 1-\\*}QP][ hu:wٮ.k~\Dvu9{2I5+3okVcc֦&;D3VdXl粣lcu|<(m|֋d\_DD1j>+gX8k
FDEٓl\S,gW˸wËw1c> <Ҏ{஭[g\VrʲL5xk\6\ۣ\h,@A^[~Fh\*@K 2?4T'("Zwd[HH^hٮUM& (MZhΚ^Л}Eu`Ѱb>V\*ӝUBsM[wmI:HbBl
$aXEӋ쌫b $Fע:
Y>&Sy9U^KaYe̱3'MF瞥Nxs#g(..$/'L^PP(˥0Qr\@x/\*+sR"@RvbCZTg߬A$r"
t3mJU5q\*+Gzt~=EvZ͗ˎ)clr ]wzIaGhz
b&3"񔈂(t|}\j0M0?V7aeĈ^{ Riǽ\;(l\iu
F#F<h4:z/S@l6+ݟzģqؽ5j~ހ~\ZF#,!.,Go0bEQhٮ00=huzظZ;7aZthZvn^\_ ^ݴzfQDtVm
Fj׏a\_oUVhtpu%|5-
MXXUi
nXIٻeVc1|kOt&cӯ?2/\7\_~ĻocT!>^&N9C^{XV|R};5䅾{
m\*jicԞ-!Ӧ-g)?]0/Q}׮C]햬((2TFHAZݘ-ڒv9BKSFmDA׏z1^\*WAxDMvzo\_6уգZ,S~cbb#+33GhQDzY+yV\*(
aP^\L>lE.8#<yZ{r8z/o\_QuvQ$ (Z440׬
DՏf|Sz-ٗQ1Qa0z7EqErD֪\_ PEǿ54@o0(
?: ʠN&ހ$iZQEUK!7;S^}:rۺu/;gΊOTq`ȑYs=SU(S\\_knhY9sV4>P^1@ӴiUSPq$]P^
P
7Ǝvk LNQsTEjm17$r-[>ȪU[o؊Y(~G
HK %YJ
ܺCZlSaIa`ә>Hldܱ#&!a?^J>{
\*г\_V|7;Na\*.mFL^}i1FǠn6+]\_KEٹi#JMv7nAA/0ONGؕ͠[uuQ$w%@~#p\*k~Z+(#"(JQv׃-i4
F1M❂ JRm)9"+[^o0$>@FZ
?T-%I㘟\}NQDcr5躦sk.kn^æ =mGIhpE|PEA4e;A0(@\_]mIsűAp^&'lI
ٓTڞrlПRQu
,s1^vQI:s][ddbV-a3~Ūah?[{>7dťJitz^ܜLd'ˌ1
`$m'4mŮMk] IFc,s>y%.=ɤ3\U/9Ɉ:3 %vwL{{Z8Qr,n/)֋0=YY%Ǐу@Hp|زn\_W/~Pi
]FmY#;7A0 8ffHSq5PUJ] Ah`7F݆$IȲjA,#}@\*W:س.ʝ2yk\_|ȸɳH9)癹tDIl\*.z7v]!Iz^z~C\_n z"&}^πcxyUH]c6`(aoLӋ;7e/ZFUr>&V:s=xf눂̏'жsW^ EAaL\_+&ST b1\!\_[뚜;u~i<{ΘG~nvَl#5ı87ٳ={>Nv!lBP3yP:<܃&:`ZxgQG{RmR2I(4hֆEU=ϞƑXL&sEQ)je<е-uF'VT#` "hٲgbvrlxY{{+ g<2RQG\d!`Ee77mՁG)\_ `0zw&4mog
nZ,9qgnnQ> f;w&5pjٙL8Wt{9q ε1UA]{Pd4Zq'zv$?\*\*2\_,^Fcw&?.B2k[/2 |YCzKQ|Fղyόҋ5yz?"
W$7+o\_T3]MUu禵O[=K)&c6\_>Y/D~^>uBH#lZ(Xk$?wmaݟ~')X&$I涪a/>ő#?4Q0xxpqDtmV5ÙK(\*,`L,urqMf<<5:uII ߘ^ۻĘAIN:\A\5B.&3g{z<=g\* fM'Sՙ" P1<3?&-A!%gO]$N ZM$Qгp2
EQ|NU'$ 'C\_j5\j.w)I~9~ AtzOzF{ 8T\*F71.
W/'Q8xQ~q5Q]
`NMSa4-UfצuGr&YvAD$DI׿ү)ޑpV\*M[ς;׸'b
i)篣{]PKD
9}(K}mHKڿW
    IDAT=dgaZ][^Ց6YQxW:<ԝuCxfeϓ 9|`E8Kx@f!:qs5e"V٥z]ױkz
r&huvf\_sIrH;uV'm'c ?-L1LQy2n"t~9pF h>r3fqD笭go\LN(S4lI+i.\*\_4n\k+զ=h$pi>` 2c?? Ә@93%35h1̞6hjako=L-.+>QώdԳ7 ^bYNė`Y$
VM.Rr~]JxVRj
z8iԬ53>sM<\*Wl\*f3ԃ9\*Ur=EsجVA r5f.͑oxp첝矸ހf|PFuCEߐWe}@ӣ(SB+~|b5p$0OGWxzx^z?YySTt"BbQ\\C^>8{8Vޖme錣GO v'?, }!?CT݆h4Z#e;aMŮcI$
iVf7K%
ٙ!2VހV /\_R< Uku\R3ŅM&CZF
s% O/2.b\*.&$23|
jućlO3ɤ\8yDA,7=HK9y-Z5#F.GR. |@Ǐ|ZEO/Z\*f(q1^>xcrEEZ;w\_"9\*Tg0,dg  O(r|VMQCĉ
Q^
dffpXUPqp$5f
Sjbb@டC\T`fSC7~jR\*B+df:-!h=+ߝo?Q]nNyJBTExcj7#D}^P|0K}lGB)-d,W>Zzz
8
(>Ej"v+K}dqΒ9}Rk\_VT{TErO۴?nݐe&yo(0EW
`O!i$E=v!73EQ9~4\pdqB\) EV8̑R%9HZNƟcج6׭Bf5 (-$n1RYǆ(
pt\_"),(n(\_vz.:jRa51J3L@҈4ij뵠kە@¾DzZvZEG&C'߃.PFri2i֡( ˗ls4Z+.
koDDQ0璘$#9A|lDRVK\o. 7#Ί9븘
ǐ$P~
lb5Xf-'}Ocf2%; \_vgv!)/&Dړ~l%\:>DU,998pýɘZǌ3@a^vJBLNF. +
AI#^EFr-&m)b4 bOgqĴGRb
;VcԴATjCYxxEAy3
^dAӒ+S!J"G&2%~Q(I,m(.(yn?gSa몽yw .~IJOIӌ0<
(
~+'}ϛ3\_P{˿ӿg=@j!{߁{O8v$\<QGq}]Lo9DNF `6YH9(9Dh \*UTdvBynʖ8lJ%l+fgىnUQTqSZ06.SFލ$/\*`:\*5G֫($HJ%1J 8w  zB\jX\*2{ <<
HFJ˭-τ#~A l>\*Ax,{.#`\*4|썯ɼMGҮ{j5@p%4^Rm%: ^DQATdA ^j(`5[BLf$=~S}CW=ޓݻ/p/xO# ~ٷ-j^=u|W\hrlHvfд}4"/YV\_Ga^1
~; +ɠ(
!e`hs
2+TԡslE7P ^5XIE!^KeY{z)Bp L싹ى:Vr)Bߗb\*2#`28Re^7{b.6#FO6͑"+((-NCsx,!eF(&mvQa"+]edϠi\^2jUt@ sA QJiQd^#F$^fEFN؂FAoйQT;KNNc߾@CO&C׏|ggߋi0 Vc7\_s5E֎e.m[@e"kGy Щ0!Bv&-nҽin6kn;$=XDoϞx,YWVm?ʕP-rppkTD?T#O-=܋ }P:V Sq$UeRd;6;Ndp/TqaZرq\_
XX7nk XFwqᬿ/3"voCTWނ>t4o$6>Z?K
E dͽ}|.~؈lR
Jb EWr7 k[kƁIHX`N'q/o ?K<[/G!
:z\_҂HNf:ƹ (bt:\_IE Yq0RB\*$E"(u[d\_d/?jQfNE#h$ AԎq'GNޭY~\_'%%

4jPU7(
;EGC1;'FtN|7
,YH<Ȳ HNE3hz^ժUtZ8yb`y
WB|&(̀Muo.GQFpxޤw3By^^q
2k$jǸ~ع?$oφ
sm> 8oti@$AYUnE\*n<F\_ ;$Q+
 \0Ԯ]֭;8TvGGn\*I^459UΩҝjP|gHUsT7Ott$ֺ/Sy%lzk׮#""FCFF&ڵ
ܕ/,/gwF؇'^
JOT>N7zr>X6,غO]zWU{UC Vi}ŋPXX&9wvvyyis[ݝ".\ߵ6(;pnwެb )"McGc 9DjҫT ލDOc0?kxzzc9G>>DDDuVoCLL+V~kdbԨQ^
.\H%::x׶TBCC]f3&M"""\_\_\_ڵkGjjj[|9̙3(Z-CjWK,E@\\6)S/:t 99[ҸqDQu4m/B:u???Mݺu5{) {j۵k\_OJJr5"@
R;>O;lڶVS͊`7=O\_%;;,m۶9s&^^^XVO~Qzj֯\_O`` $$$qذa{Hʕ+iӦ+WСC߿zjwΆ
1ccǎ\_g޽ ?EaYv-7v͛i߾;w& ۷#'OUV$&^m?ٳ'6m"==p!-Z@XX> YYYlܸoooFA׮]پ};ԬY\*U\_'0n8vAhh(K.M6$$$Pre/^O?-.^y&/zzzCS \* 9@eT \_S([F\J1uUmڴŋ7ˋnݺ!2˗//E]veСRRRAe+֭[Ǒ#G8z(kצL#55ܹ3xyysam@ZZ!!!̞= }vILL$22x֭Raaalٲڷo"ꫯr9DQDiܸ
WK.e˖K~dǎ4k֌I&1eƏϹs(\_< vM6frpdffKŊ2dƍfa08~KcVǯOJxA:^<bYo&\8I;U U܁-.$66+W?3zhW9rd}wW\_}ܮ];vAdd$FcǎѳgO &MĈ#$> &LPPH"m۶矻?{,,ӥKw[lq
r}LEQp~) 'O&##WlOQƍKv<==]mnٲ ͛ǰaJ-vs@NN4nص~VZ\_Kʑ#GeY4h|vN8QyddÇsI
5j1@U;
>>^I&NXXCllkvTfjժL&ٽ{7aaa<C.lԨ5[w1vX8swfkεϑ#GhҤsBBF
\*[j8N8Aڥ³(..VZat>sN8ABBǏԩSe eY&==:u~ƍ`ZILLt] hذUĈgϞbھo>VZ7{ jժ%޽[vyc{f.+WP^rPޱjVjקMɬZ䎀6mZaOf d2QJڵk#"&;vO;v|2ci/&&&ʕ+;Zf/݉'+Ul7..N::]W|yN,$O>رc]DzF $88ԟkaϞ= df^M{C۶m1L9s6VPǏzL8HIIq٫aaaKwޡcǎѣG/'>g.\_ttt:a2.W'>]Jg$?sj; \*T^{4
Ś5k(\*\*wIygӧ;Nf͚
5bܸq~v܅'zE:t f͚۷-ZгgOtСC<y2Ze˖(VXAxx8)mƳ>\BիW`ذa̝;^xO^g̘1 Y`:zh^~eAvڗ+    IDAT$%%e-[r/ʕ+T111;1w\v؁N#++|Jn4o\_\_\_|}}6m;vW\_ 4ԑIѫW/BBB4[oŋ/HLL~-ϟwhwBΝ޽{kN>]nݍW^[ng<==7-ENwwP"
7h$IⶨZx(gY`)))TXΝ;U㧦0u4=C%14hpf3fԩՋ\*UpڵkI`ҴiSwh`Ӧ,]|/=0{`hfjZl#nx衇juNu3IOO[6w͛.j&&oITT=+V6lH^xG5+0?~~.ռsN:w|oOLd֬ ޽ QfffkN w3g$%%Ν;өS'F.W͓:d ۷5jl:tl-o
(4֢ (p#]ͥWjqL1JZ\KG.[Ybە\_>\_Yu\W bO<cejcŊf#- ##-tATI.0OB
䗜FhhuE2
uI|W7UW8rӕƥԛ[L xxx8f8#ȀFQZ[toڃ]My@aaY~{#A8Jƕp|gRr۷0'F1<qJdpE(tl/߻kj[3ZQf+Zcn2F.\X`U/í~}w
`R8
#Z(+?0zQUelf`A>ooHpiX3 ,\p(p\*;\*l
QR0qqߩ`n)D\_+^&}\_REx^IۆsM,Q~~[:umOļT.^tGQCOPP9Ҳ/""iiٜ?ve-HPQC,
kBˌyy]ӳkL&P1o"oo:u}'O~n3FŕFRR JVU-!@wQpˋt(. í(((9uJzJ~ ~lXzc\_>Fa|O(-j[`?#ķ? >'S՞7شi]6{do'/m c
0u(2]ӹ},moluv#?w4D~^H @^<
mV=O ]UDRŭliТVcT[,cXEu#l?:w-f[+iVwD\*yNqD#Y@$12&fê 8kFFQ\.:TT L{.1Z(w<lWr:nG\*6.O}XjL.DFVfȐ=܌ ϞMlj톢(x{q\_f荺$K>wofKzB"(E
"boXł~(6DDQTQJ5tHo[f?n2Mv&;w9sqΈ@l׶U\~cdfJ7H {>uNL.HHC99yV؈+H8Ea熽;?I
9lܸ3-#pg۶M5jxH \*ƉjSQm\*6{~/y(Ʊ$\*wAs"q(v
E?Kxikw``lȁ8n݂ pqɣ\_Ue}:Or4TO$X&=.茪|.c ѱƇ4f75i?8AZkPTUǷ8rh:ӞNCt;Ə%35g#Q"nMlYIDK+î)޻=x1y|wܰUUUV-XUHJٙ ȁTvm.⪡eN>zxm$7˵^EKfZ6Y94lQX]=)qR鏡C?'|X"$@2¼Ӡy ˠaV߮+!ݧMNvF^Wb/9z 8}]ZuAoFj'K5X:w윈N͚U9ifG=}Ç%p:0 ?EN8hRߒz0
(J^v> 1=J˻^GwӶ[Ks[thĖv( ;9?:ujܹ'[\*]nc%Cp.
ãPUicgҼmC.3(=w I(IU5M4HET Tݳ`Y%fQim/ۊijpsC9".9+B)yA!7+ͫ826Z
jB:϶zؘm41m^MD=ƢE d{DjѢ;/pt)%t]!?7ɯ`ټG$T+<ngge={~IiҶ!6e?kt]7vV\_ݓmvGsرaVn燏fk:"XSM)̞79Yy"<N-gy``l^Goҥo/PnUN9;t%h&I^Һss</-NkLL[a[rмC#TUM}j\t˹D8i־hUk&ѥo7px1NњupүWngݒM$7G~R=uOLHK&35.M.IX{)$Rz'2ΣE]QURY:k%7<z9^:\r{T׫u{sט({MEjjz$$V{G蚎-0]'q#
qM3!O5\~+^;NLGDYaIi4ZvlBӶ~R( ́l$屈0Oǎ=" [ssV- UˆAnv 7sS~5N&/7\_6DJDTСv23ealGf֣5uՒ'!Q$@]mG隦KPTw^Z٤UU[S6`%
dDjЫ.[SE:Ap&%e#?6V{l\*[);%䌩S\_?.#0oܸQZl,fKC6vG1z؇sĲ%p{1"ie݄ͫ
)Pqq1DG;sò5" LUh`;xU≎u^Npؘ?s)iG2ص)U- j^ƭY2g
\dYdDF/=" %`o+0rZmP?k gs]IjSٷ cST4" e ~4Lmפur/ݍ+۽9)GK}m5H㽧&g~!ZBBGTAe)y9L-K͵״]r?&au6(}h HϘ?s\_29բ\*TJF~
AVikԭVzTV/wl͒ͥፍ.cϓ`Oh8<̫֮~,#r`\_y7=ԭW
9·Z& m
X;7GD1mÅ!35ozgEQp[/~,{PQ2kt9J/^/pQ7U`ɜU'P:Yw/MO;ٺ=[pRRy4c
}Yk`CE~˼yJS.ٹyР^l٨Tzǘ6w#s}DG;ڜ\>pFglِ>/zZոt cr?y " Wmcŭb.]ҧORI3Qe2g[bQ!O0l5kZGKGelȁ
Xe6Tмq>׫P6vJ]C"?h'5jT
9ϛ<b%3
eˆ!\_禛C׽$?IɃ=HVVN/^NyvRVR=/==N{ڵmgO}Mnn>2~Dh"JD  rrrџrweT5jT+3<;%uX:?8U(t>+k]ېv~i\0'l"EefBjJez<ԛ.nwNkNike0eʯ!cK߄lǎڷeII8M%Ko ,2\*m2\k}Z{sNgJ~
ܭ[y󖰟QVR ~ݺ73LiԨ.M?-#PyÇSZsytg m|\mep=̛oY͚U.v?w^Xp3d`m{<)VGV68?Z]eߣGKAv&M>+>G&V+hĉѳx:.XZxL{H(1=l-7o4RjL2ϾԲ'S:ega,YˡC l5[z.Y5eN\_\8n?sgҦMcVS3~Q
U\*ISVN'{m
eefMseߥ$6l@#Dn5hPXa߾CdfMrr]?n#dfPJBʶmxT$
I\_4v:AF]qvEAZؽ ӪU#e=l67ôQZZ&fSi޼擐KTT
FQT=;C^E͚sՀ]a[{6eƭ\*U}<z4n\/ުТEc|}џYguu4jT-IH;rEI;wۀ-u\_\_صk?Ӻucwq=lߞnQhժ\_fpp11Q$'{MtFi{}HUMe\*;w\*RoMؾ=W\_~ߟ 7GOӗ\_+5ui꺾Zځ(u}o~Qcd:L
zt@9n]Wef۶ml6}t]\_w)Ϛ5ίl/мޥ~hU${W6q⳺\*zt]\_o\*[a{8M\_\pr={ެYh#Fܩ祥7k@WE\_SQ/ճ|(^V5=%WMh񱺮o,hz-\xzTS7t\_mTWE;RS
caOt]\_anGE99sCVMm6vIWUE\_~,SJfSu]7{I=:ک]o\_Z}Ȑt@;-(zvםN>jP>uzmtMՍ^5jTmMmw5WRNA-LQ<Oel=hSek )@Q]<g@QS ]Q,u8EQt(Pv#ҝ\JAnE3$tliYPg$#ݢsJY@N>u{֢lV7\\_Qc%a7Pvx!bZТgAVOX-Ū?hp8$Y'Qh Դ(2uu
PGY$jĨ,qzV)jQPZBdacPve$?߯Eų[{~)Pân4zQ?H; jċ˾A2@b]OU}dQKb|޷ǉ  X#?gDBbbm$pP7yuo~09 z !k:|xha,KM`#6a<&Tp$һp8qzV9g~
o:P5\`n-р㧅.9d$$\*^
q
rfaD$,&\_a#!QQmm]3\_+-T`bí½# 
HH0ABu{9Y7 Eb
M~;N>vÇ3RYo"{`d;c/['w2R7XD:'+d`I8" ^Uư)
80|Xýa؂k{IvJ8 >
^ew0
d9dkQfzÁ7vi0S5
aD Y: cub>?Zw'y8\_ڒĻ/71B=4Qŋw
)[c8TW~x&bOoqS;%NaQ\_}`|(㥩.^>/p93\gkGt^5Q߹Eߞ|lƕ\*D{As\*$WH BlKy2,WG[$
"eRGJN'q>Lc
en3w T?"h^ LR>ًE׈=c'JX Q||MJ\cV/WYrvX\\*^6Q:٦s|.\_E=@S|A{Mm}cl oUr( ŹT&#[QY EaWk{ƛʝAcD`QX/<ri:qȽ" W̋ao:gga: ƣHoK>[DB1^'l
x5 !Ԟ- ",v].oslP!L YA6N|l/rˌ[UB}x-C\_mRY`dm5;N-$O{ydb~\*P}S-
 n`-yD|s:ItsVb=.0|f߅X 5F+-үyq
"0\'!'x{3G'q^bl}5>\<݁=&qrӄd/犐.o8I7B\*+
#9
xAJ8lѶCgUwMHr'5cK"$/9tjz=DA8\_H)$$K좀w\*C3?P?KanћmLRyB$,QD!Y3\_$×Mfy>#I>S|'mB{^ 5`g9]< I+\|eTdvŧ#MDBi%!o 1Tq{$8Z7[a 4NHT,(.yqI:WBQϧ,/ͅdo&Zp\b|O2V bl>XZAځRL}w    IDAT^ HJŢ I'r[Ulo,>
,0ET5q⫽p/T]Pm 3DBHՆNq=)4v#3:A<a$c.5'G$9]?Av(>\*><@4
2N0)
c$ϗ4S$ MHqʒ;A#{Enk& ~6%>~U+f8wT5bfo $+5.&bӀG\*LL=J3 dy\_5aG:`\*$GVx)ItIU"S(Ll$Me&7C| Bm "~Nk#BZ6)'lkӀxTk\_oĿ#LDo4751¤>`V}EtS\_\_aVx)~H%@LjjIǋ1A3]¤V%Q3E38\aLi\*hD u z&'MA.L` !ǌ~j[\ZW[BHav\*\*CH,lÙ:xP\*wh%NgZ|@
١6f{:$jt
>lB%||gh!\_ђ~\0Lc]HK
U߉BX"2%@ʰ6kj/睄ĩCF(x$qcmUA SP^- 08Vضa(!qU\_zBM(t5(a%0A.M!QZ"(Z^xd9K (zyA
.z#lI!bc^o Raf|D`$Jpb^H9#I F\_1"%;{#b'FXb'gfQ1"O>]Ca\1n0(Vq{Eh\Aʄ\_0J@(m~ ~`DRy\_z#:91<z;pNad
)T#ƴ5F%o?
C,\*nM,JJW'{Eh 6?x^R1=}8et?N0>֧IsmR[}I@-ӗ1;Ϣ0Ս-Qnq".#r#cvx=-;-@L:8ZUMn&1D(Lt)G+YWNP̠TMN4ZR81sQdKH/0"$1\_g ňs^3(LX=ّ)f}&,K1\*$@A;:s\_?^
Vš6Fn㍳qK=]H[>|>4g\G^"TFAaqO1\*kf
F\_μڨb쑻{&YJʫ
}Db)\}VH
U՗p<ƞ,X{J G1(ec,LH|ň-"I4`,1Is`,o:A#1lM唗0cerPL`d
/fGZ`;Z9̋WStC#0oC0B^h:Pp;cUw\*ƂI \*{Cp|aF'67
rݧfqm)')\JTR ayߗTE 0-{KHT\*
q-,Gu^͈&!QQ`$+O;>UlFhPeΈ)Aysy.wAF('/3c1@BBVX2FۜH>pPtl`O`x!c8aL'wZj)Q6Dehw:BOs\_Q$@#T(}v0l9%$\*fI"VBۑ,^:sH@GBw1 cdɦDV}Rc^X/
0l}xAԊຮWbDiJf!W?=RA[F͒$I6Gb$u1⠻Dx}bǖy),DeA\_Bk"D9cLd 'oÞʉq(xDBHD:o+eB`^)'ɕ嬞\*Gu#x̿]rZHT/YN:s9RUB£GF}8H󻪌Ro`
#E}Rֵ16ۀ6q7!` F߅W>"DEG?e%TʏؒRqA9]Ic6SNa,|%AUzv-GЯ{rZ}TUцnq;F(!6֔a[="̺>WX,QQ[эmerZRNKHD,bRHZp$: u[%4%ɰVSA%|4D[IM 
V[ᗐ8P{X;sSw1"=׳Gad@Fڧ389-v?#[F׀C<?ǩ~s#GRG>\*O.3\*qۼVL<Qe#D\_{ oFB|I}xn^>ن׫YשY6s<7wYV<oIТQ5sbhZUU4nSYlYu/]bչuоo{FZ{oLr'T#ifez%" \_{::i|R-{p(QձMcya$g?JGW<ntB!:ۂE.Ӊic /uB!.6>;C:yLArr
b.ܖҚWj\1- ^
WC?I(
)ƤvS<aJ,}M١[C/''/R:<
uю[tjӘٟ<
ǞG/\(B^d\*QqRFm\*+(r|ӷwr+M'hN&im4oX\_$@uZ7Ϟ-<FVN 6V+Tb`nw˥8']9~W"5=[X"Xn; ի$0oFE)\9i-\.=X^cYrJTl3s8mS"
֨^qھ)ujV~jtmߴRǽ$!.|#rJT T.DQ5!-D2<^g^a@T]۰hڋ$ߦm u47>a;=^;5%pn }ZՓXh$@rO:u= MQh %^6`U +:\*J$@ I %$$$$JHHHH(!!!! PBBBB$@ Iְ{AVNGS͉)uv
T'.&|V\*dWUؘ(Tf$ɑLsL(Qx5-F:'1Nsq\_51MIEjB,(r{-7r:vo@UbHa(@:ըGN$Vl8vl%{-M8(Y$N)ΜG\_ܲkf4KG^u,k"a7>r:LXnyC\#
ᰟFTU'^{eUQWQnJB,)v\n/9I\*rɿ1q;WV|冝<W}2NR)EQw|?ls(zun-^Ex滈rҳr:֖o>,HZ}a9g(◿V}̟ot8l<tԬX Mnھ-\_v/6)upڍ׼ʾb G?y\_Xn;?}$9(w@>j.o+>c]?8vF #|7Fʧ`ga&ײΎp(!.{\_}ܮ v~`<۟pInp&1{VDNoۄWWFpޒ<gu\ү?bl<8 IEЮE2^~v(~e\~GG/ OJsF㊂ͦ2;GLu12fNIEٿGTQph=a,\_n଎-NMkѫs+^mmhZvn>SZDB\4dHNIr7N WHZ#}Ө~M|1h<n|Fd$ھ <3!rYr\T<.
b.p,-cETwE)V>l>Wz?Q]I]Rz~NZz/?blb~^?{w2;svDt׫QZ
6@Nn>W'̴|
[menJblٹg/+yٹ|͟Fr:p=Hϧw6'|wh'#}K^H®|$0q:9QClؖm)lqo(h6nOïw-2\&}3-lq)GHa΃LfX J 0L>4}MUEAQ`rsef;.=0^MjbA@yn825]eԫUkshULꯍ.rͅݱkΐ}y,.8S}RTUafrflR7GӉrXQQ\IB\z!i9EGb|/=t
f+w xe2{ $Ĳm¾j>n>1Nr\<LycPV{.{%6&
Mwsͅͨbz5/:VMѻskޟ:('J\ldIAH9ð?-qa6W()j4vi! m|wKӚel؞B3ZLLƄisQk\)nۼ\~6;90wG˕qVp9z{/\p2qԝqU\_$\_}Wp~N$KkS^[`Dkny}=xX v?B^a1H[W9by
l
lu 3$%Đ&:!A`plޱo\_
d3E,okTბCpwMIf3$#+v?@ÛGIK{u9YЁ9?m{t '7M4mP|я]׿.&uE@Tv(~\*(e/NvmTM#5#Ԍl&lZZMk<|ب(=wUcǲ
\_hjIl\*Sf.$-#<ƙ[㩻/a5||x?r߳%$90gcq:eײ&}5&;GFuzޒ0(\*h^nKz+{5I32onwd()QN{y<6gv[Miް'<ǫ٩~5#4oX(f/ZR<<ЍU{d,y5^jRm7 /\_n% 0Dxioe::'?u<4>yg+ 2ĸt\l45Yɋ}s]<vE$ޝ;#]ɶٽ7p\*\_uc>͗)qѰ^
 v=d)%\WXw0غ2IQHM7cB2hNE{^Px>CCP^~ѢqrMSE$ 0$ESN5 Tg؇pȫ|zumÍ
{\_=PvU
&{t(t]'3;7qzK$\_+yKszrrD9%XԬOC/#1.Ư2i|l~kCpJ7R5`֢5<qA#Vo݃ǫѩmcv iٸ.S߼2Fu֫V@: +ep1H/pKkCQUgߚFFt0wܮ㫦/^W"WVD4Ǯ}G8t4q\_./Iڼ2{N-"oL\*޸mUE9ӫsk&ƳxfmM|ƳoO[.,X,Q{4Z5i\MnZh'OlXՒЫ#Y9y6$n#:3oMcWrL1Eո{$?UEu[LIx5?'Gsӥ}Ct[l\*I |\,x}$sxuoԟ2
oL
c=򱩪\wfG?]$
\-m\*^i:mdde~[
Zʁ#iTM磗y::St8/|̲5F|Ȯcnpg
OQ]MLm uz}k866ϧ3b׾#|'5v\_'~ץ4iP|??.VD>{9vjUUx듟4ĸ;%wvPwW>NNE6\_g(Q:-R؜Ԝ{w<t˅x.SoNPxE.@+/w1v:Mk\FQE;^5$srmxio~PM|5AzunuV~fƽ#?W&|y2l8>TMcy<ִD׍("qޅ~%%ۤጞ8q\_\*0?÷\h"?̜<rrk OئqҲؽ'Yf #cÖ6:i׫e~r
ҪE5^%<WPoWaR3i\2Ux44r7OGnTϊrډBjdZTME!-3ꧪ\*I1亂,.89j.5&+.6׿
 ^rcgkSlJ|\4[v 1ֲ!vjAdC\LvMDeN x<^rqm$ǐ[4&ʉa=jHU\?G\*x:Y!UU
\  /SY%jU^5XWh37PKZ5[gMhMQ4nPwy@1+ifdidfӲQb;%j9ԪHꉠ8Ew<-H/ҲJ i'-#@
B!s ։xg:GbHDdJ| I %$$$$JHHHH(!!!! PBBBB$@ I %$$$$JHHHH(!!!! PBBBB$@ I')UUfSKæTtT51l6·\*\*<|b+|]|?Veׁ?l6v=;涧ǟ6OMLQWҟ)]fTyvy))bI\*iݽ@qqV1'\*I`"   IDATM6DLp&((.љ0 pteeãǚ Ydw3$\*\*.
Xo&EH%6@0Ӏ49$/ vK)uu$<Qi"E{Y\*@[^`,gKmA"R'{I
+H
#T\*Xhu?pcֲԴ WB`0 mY9 ARw@ & ɧy&c^
t ^(]
׀=3h'γr |(~-WMuNPM\_r6\QߍC>SE%~E{ a='XHm14z{ jK荑P3U)} 
%-HU?é<WH2>UAkr0y!1֚9\_L@\+X07?o@`RcJ8aj{-'ax/Iu8[5!w@GM\_Lm{0m񦱸P|4u1>j\T"1&Rıwԗ XLP߄6 u@k)BIYE\`!Q&ѓҔol$h14L< i? 5z\*t排r
% o6t l6Y &oq Ip8n5RD.PwM(3'Or߻L1 }.8D/ZBX\ԣAR>$?cu9 r0ȉ L{Q\
c0 P0ܮQ8,>g!',k櫙/j$D(t6bpMvxdTiDOcIBJ" 
 suM%T @g:v867;![z;bla`CE, @U1{G,01m:fx\_X
{jD K !r96nx\ eRM}.PV]BgfI& b.cEO@%Sa,pPXxZHKBvb,Vt\*TqIb^![a;ZX,&az?
Q߄+! M@5 T903}A8,/r8;r~B± B f;A泿'׌W23x^X=fcrk~+Me ?0V9+@ t̢ϾXI-X̑Nے )PR"sp'{&Jpq?u ^0a|=
ǹ^NwLy<U:X8k#p |Fd am.a^Ii`㸦IJ4c<%B+8SRDIl76dÍ kXv8ȵk;\_UqݏcIMϸ8w6yS>=NӏBA(P)nZ|a ms. B}LY]N#. ^>cGb@\_U/FxH;V1<aoĔW:>VSëat`FD &t!hAPP|<̝-DNP8+)s0"?6QÁ7N65M!Xܱ"0\JjuLێtcD\4É$P su;\_H\_O r'&~x.K
"C{xVqn8wt0BoP>#צҫ.'~u0|c xէHcfUkŻG
ƚաГ\_f`XSe!scَ?XIу0{6%g-CRMM?e ۅdB$9N5~F#-B]$CQmɄ#zg֎%}0\#0(m9faW
U2)ÈZ \|/kA1vfje (1\_Xŵ2g ^%m΢pE4c5|cu1Ӂ1
/TA@EZB:Q}b8
熳\ZN"kQD!9ƈjccVQAycf Wp5B
8Y| #I&\_"8##/@q;,G3ZSS҂D'nh|DR$@ I F 6    IENDB`

---
