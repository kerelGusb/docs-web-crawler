# Apache Hadoop Downstream Developer’s Guide

* [Purpose](#Purpose)
  * [Target Audience](#Target_Audience)
* [Hadoop Releases](#Hadoop_Releases)
* [Consuming Hadoop APIs](#Consuming_Hadoop_APIs)
  * [Privacy](#Privacy)
  * [Stability](#Stability)
    * [Releases and Stability](#Releases_and_Stability)
  * [Deprecation](#Deprecation)
  * [Semantic Compatibility](#Semantic_Compatibility)
  * [Compatibility Issues](#Compatibility_Issues)
* [Using the FileSystem API](#Using_the_FileSystem_API)
* [Consuming Hadoop REST APIs](#Consuming_Hadoop_REST_APIs)
* [Consuming Hadoop Output](#Consuming_Hadoop_Output)
* [Consuming Hadoop Data](#Consuming_Hadoop_Data)
* [Automating Operations with the Hadoop CLI](#Automating_Operations_with_the_Hadoop_CLI)
* [Consuming the Hadoop Web UI](#Consuming_the_Hadoop_Web_UI)
* [Working with Hadoop configurations](#Working_with_Hadoop_configurations)
  * [XML Configuration Files](#XML_Configuration_Files)
  * [Logging Configuration Files](#Logging_Configuration_Files)
  * [Other Configuration Files](#Other_Configuration_Files)
* [Using and Consuming Hadoop Artifacts](#Using_and_Consuming_Hadoop_Artifacts)
  * [Source and Configuration Files](#Source_and_Configuration_Files)
  * [Build Artifacts](#Build_Artifacts)
  * [Environment Variables](#Environment_Variables)
  * [Library Dependencies](#Library_Dependencies)
  * [Hardware and OS Dependencies](#Hardware_and_OS_Dependencies)
* [Questions](#Questions)

## Purpose

The point of this document is to provide downstream developers with a clear reference for what to expect when building applications against the Hadoop source base. This document is primarily a distillation of the [Hadoop Compatibility Guidelines](./Compatibility.html) and hence focuses on what the compatibility guarantees are for the various Hadoop interfaces across releases.

### Target Audience

The target audience for this document is any developer working on a project or application that builds or depends on Apache Hadoop, whether the dependency is on the source code itself, a build artifact, or interacting with a running system.

## Hadoop Releases

The Hadoop development community periodically produces new Hadoop releases to introduce new functionality and fix existing issues. Realeses fall into three categories:

* Major: a major release will typically include significant new functionality and generally represents the largest upgrade compatibility risk. A major release increments the first number of the release version, e.g. going from 2.8.2 to 3.0.0.
* Minor: a minor release will typically include some new functionality as well as fixes for some notable issues. A minor release should not pose much upgrade risk in most cases. A minor release increments the middle number of release version, e.g. going from 2.8.2 to 2.9.0.
* Maintenance: a maintenance release should not include any new functionality. The purpose of a maintenance release is to resolve a set of issues that are deemed by the developer community to be significant enough to be worth pushing a new release to address them. Maintenance releases should pose very little upgrade risk. A maintenance release increments the final number in the release version, e.g. going from 2.8.2 to 2.8.3.

## Consuming Hadoop APIs

When writing software that calls methods or uses classes that belong to Apache Hadoop, developers should adhere to the following guidelines. Failure to adhere to the guidelines may result in problems transitioning from one Hadoop release to another.

### Privacy

Packages, classes, and methods may be annotated with an audience annotation. The three privacy levels are: [Public](./InterfaceClassification.html#Public), [Limited-Private](./InterfaceClassification.html#Limited-Private), and [Private](./InterfaceClassification.html#Private). Downstream developers should only use packages, classes, methods, and fields that are marked as [Public](./InterfaceClassification.html#Public). Packages, classes, and methods that are not marked as [Public](./InterfaceClassification.html#Public) are considered internal to Hadoop and are intended only for consumption by other components of Hadoop.

If an element has an annotation that conflicts with it’s containing element’s annotation, then the most restrictive annotation takes precedence. For example, If a [Private](./InterfaceClassification.html#Private) method is contained in a [Public](./InterfaceClassification.html#Public) class, then the method should be treated as [Private](./InterfaceClassification.html#Private). If a [Public](./InterfaceClassification.html#Public) method is contained in a [Private](./InterfaceClassification.html#Private) class, the method should be treated as [Private](./InterfaceClassification.html#Private).

If a method has no privacy annotation, then it inherits its privacy from its class. If a class has no privacy, it inherits its privacy from its package. If a package has no privacy, it should be assumed to be [Private](./InterfaceClassification.html#Private).

### Stability

Packages, classes, and methods may be annotated with a stability annotation. There are three classes of stability: [Stable](./InterfaceClassification.html#Stable), [Evolving](./InterfaceClassification.html#Evolving), and [Unstable](./InterfaceClassification.html#Unstable). The stability annotations determine when [incompatible changes](./InterfaceClassification.html#Change-Compatibility) are allowed to be made. [Stable](./InterfaceClassification.html#Stable) means that no incompatible changes are allowed between major releases. [Evolving](./InterfaceClassification.html#Evolving) means no incompatible changes are allowed between minor releases. [Unstable](./InterfaceClassification.html#Unstable) means that incompatible changes are allowed at any time. As a downstream developer, it is best to avoid [Unstable](./InterfaceClassification.html#Unstable) APIs and where possible to prefer [Stable](./InterfaceClassification.html#Stable) ones.

If a method has no stability annotation, then it inherits its stability from its class. If a class has no stability, it inherits its stability from its package. If a package has no stability, it should be assumed to be [Unstable](./InterfaceClassification.html#Unstable).

#### Releases and Stability

Per the above rules on API stability, new releases are allowed to change APIs as follows:

| Release Type | Stable API Changes | Evolving API Changes | Unstable API Changes |
| --- | --- | --- | --- |
| Major | Allowed | Allowed | Allowed |
| Minor | Not Allowed | Allowed | Allowed |
| Maintenance | Not Allowed | Not Allowed | Allowed |

Note that a major release is *allowed* to break compatibility of any API, even though the Hadoop developer community strives to maintain compatibility as much as possible, even across major releases. Note also that an [Unstable](./InterfaceClassification.html#Unstable) API may change at any time without notice.

### Deprecation

Classes or methods that are annotated as @Deprecated are no longer safe to use. The deprecated element should continue to function, but may and likely will be removed in a subsequent release. The stability annotation will determine the earliest release when the deprecated element can be removed. A [Stable](./InterfaceClassification.html#Stable) element cannot be removed until the next major release. An [Evolving](./InterfaceClassification.html#Evolving) element cannot be removed until the next minor release. An [Unstable](./InterfaceClassification.html#Unstable) element may be removed at any time and will typically not be marked as deprecated before it is removed. [Stable](./InterfaceClassification.html#Stable) and [Evolving](./InterfaceClassification.html#Evolving) elements must be marked as deprecated for a full major or minor release (respectively) before they can be removed. For example, if a [Stable](./InterfaceClassification.html#Stable) is marked as deprecated in Hadoop 3.1, it cannot be removed until Hadoop 5.0.

### Semantic Compatibility

The Apache Hadoop developer community strives to ensure that the behavior of APIs remains consistent across releases, though changes for correctness may result in changes in behavior. The API JavaDocs are considered the primary authority for the expected behavior of an API. In cases where the JavaDocs are insufficient or missing, the unit tests are considered the fallback authority for expected behavior. Where unit tests are not present, the intended behavior should be inferred from the naming. As much as possible downstream developers should avoid looking at the source code for the API itself to determine expected behavior as that approach can create dependencies on implementation details that are not expressly held as expected behavior by the Hadoop development community.

In cases where the JavaDocs are insufficient to infer expected behavior, downstream developers are strongly encouraged to file a Hadoop JIRA to request the JavaDocs be added or improved.

Be aware that fixes done for correctness reasons may cause changes to the expected behavior of an API, though such changes are expected to be accompanied by documentation that clarifies the new behavior.

The Apache Hadoop developer community tries to maintain binary compatibility for end user applications across releases. Ideally no updates to applications will be required when upgrading to a new Hadoop release, assuming the application does not use [Private](./InterfaceClassification.html#Private), [Limited-Private](./InterfaceClassification.html#Limited-Private), or [Unstable](./InterfaceClassification.html#Unstable) APIs. MapReduce applications in particular are guaranteed binary compatibility across releases.

### Compatibility Issues

The [Hadoop Compatibility Specification](./Compatibility.html) states the standards that the Hadoop development community is expected to uphold, but for various reasons, the source code may not live up to the ideals of the [compatibility specification](./Compatibility.html).

Two common issues that a downstream developer will encounter are:

1. APIs that are needed for application development aren’t [Public](./InterfaceClassification.html#Public)
2. A [Public](./InterfaceClassification.html#Public) API on which a downstream application depends is changed unexpectedly and incompatibly.

In both of these cases, downstream developers are strongly encouraged to raise the issues with the Hadoop developer community either by sending an email to the appropriate [developer mailing list](https://hadoop.apache.org/mailing_lists.html) or [filing a JIRA](https://hadoop.apache.org/issue_tracking.html) or both. The developer community appreciates the feedback.

Downstream developers are encouraged to reach out to the Hadoop development community in any case when they encounter an issue while developing an application against Hadoop. Odds are good that if it’s an issue for one developer, it’s an issue that numerous developers have or will encounter.

## Using the FileSystem API

In the specific case of working with streams in Hadoop, e.g. `FSDataOutputStream`, an application can programmatically query for the capabilities of the stream using the methods of the [StreamCapabilities](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/StreamCapabilities.html) class. Dynamically adjusting to stream capabilities can make an applcation more robust in the face of changing implementations and environments.

## Consuming Hadoop REST APIs

The Hadoop REST APIs are a primary interface for a variety of downstream and internal applications and services. To support REST clients, the Hadoop REST APIs are versioned and will not change incompatibly within a version. Both the endpoint itself along with the list of supported parameters and the output from the endpoint are prohibited from changing incompatibly within a REST endpoint version. Note, however, that introducing new fields and other additive changes are considered compatible changes, so any consumer of the REST API should be flexible enough to ignore unknown fields.

The REST API version is a single number and has no relationship with the Hadoop version number. The version number is encoded in the endpoint URL prefixed with a ‘v’, for example ‘v1’. A new REST endpoint version may only be introduced with a minor or major release. A REST endpoint version may only be removed after being labeled as deprecated for a full major release.

## Consuming Hadoop Output

Hadoop produces a variety of outputs that could conceivably be consumed by application clients or downstream libraries. When consuming output from Hadoop, please consider the following:

* Hadoop log output is not expected to change with a maintenance release unless it resolves a correctness issue. While log output can be consumed by software directly, it is intended primarily for a human reader.
* Hadoop produces audit logs for a variety of operations. The audit logs are intended to be machine readable, though the addition of new records and fields are considered to be compatible changes. Any consumer of the audit logs should allow for unexpected records and fields. The audit log format must not change incompatibly between major releases.
* Metrics data produced by Hadoop is mostly intended for automated consumption. The metrics format may not change in an incompatible way between major releases, but new records and fields can be compatibly added at any time. Consumers of the metrics data should allow for unknown records and fields.

## Consuming Hadoop Data

Binary file formats used by Hadoop to store data, such as sequence files, HAR files, etc, are guaranteed to remain compatible between minor releases. In addition, in cases where changes are made between major releases, both backward and forward compatibility must be maintained. Note that only the sequence file format is guaranteed not to change incompatibly, not the serialized classes that are contained therein.

In addition to the data produced by operations, Hadoop maintains its state information in a variety of data stores in various formats, such as the HDFS metadata store, the YARN resource manager state store, and the YARN federation state store. All Hadoop internal data stores are considered internal and [Private](./InterfaceClassification.html#Private) to Hadoop. Downstream developers should not attempt to consume data from the Hadoop state store as the data and/or data format may change unpredictably.

## Automating Operations with the Hadoop CLI

The set of tools that make up the Hadoop command-line interface are intended both for consumption by end users and by downstream developers who are creating tools that execute the CLI tools and parse the output. For this reason the Hadoop CLI tools are treated like an interface and held stable between major releases. Between major releases, no CLI tool options will be removed or change semantically. The output from CLI tools will likewise remain the same within a major version number. Note that any change to CLI tool output is considered an incompatible change, so between major version, the CLI output will not change. Note that the CLI tool output is distinct from the log output produced by the CLI tools. Log output is not intended for automated consumption and may change at any time.

## Consuming the Hadoop Web UI

The web UIs that are exposed by Hadoop are for human consumption only. Scraping the UIs for data is not a supported use case. No effort is made to ensure any kind of compatibility between the data displayed in any of the web UIs across releases.

## Working with Hadoop configurations

Hadoop uses two primary forms of configuration files: XML configuration files and logging configuration files.

### XML Configuration Files

The XML configuration files contain a set of properties as name-value pairs. The names and meanings of the properties are defined by Hadoop and are guaranteed to be stable across minor releases. A property can only be removed in a major release and only if it has been marked as deprecated for at least a full major release. Most properties have a default value that will be used if the property is not explicitly set in the XML configuration files. The default property values will not be changed during a maintenance release. For details about the properties supported by the various Hadoop components, see the component documentation.

Downstream developers and users can add their own properties into the XML configuration files for use by their tools and applications. While Hadoop makes no formal restrictions about defining new properties, a new property that conflicts with a property defined by Hadoop can lead to unexpected and undesirable results. Users are encouraged to avoid using custom configuration property names that conflict with the namespace of Hadoop-defined properties and thus should avoid using any prefixes used by Hadoop, e.g. hadoop, io, ipc, fs, net, ftp, ha, file, dfs, mapred, mapreduce, and yarn.

### Logging Configuration Files

The log output produced by Hadoop daemons and CLIs is governed by a set of configuration files. These files control the minimum level of log message that will be output by the various components of Hadoop, as well as where and how those messages are stored. Between minor releases no changes will be made to the log configuration that reduce, eliminate, or redirect the log messages.

### Other Configuration Files

Hadoop makes use of a number of other types of configuration files in a variety of formats, such as the JSON resource profiles configuration or the XML fair scheduler configuration. No incompatible changes will be introduced to the configuration file formats within a minor release. Even between minor releases incompatible configuration file format changes will be avoided if possible.

## Using and Consuming Hadoop Artifacts

### Source and Configuration Files

As a downstream developer or consumer of Hadoop, it’s possible to access all elements of the Hadoop platform, including source code, configuration files, build artifacts, etc. While the open nature of the platform allows it, developers should not create dependencies on these internal details of Hadoop as they may change at any time. The Hadoop development community will attempt, however, to keep the existing structure stable within a major version.

The location and general structure of the Hadoop configuration files, job history information (as consumed by the job history server), and logs files generated by Hadoop will be maintained across maintenance releases.

### Build Artifacts

The build artifacts produced by the Hadoop build process, e.g. JAR files, are subject to change at any time and should not be treated as reliable, except for the client artifacts. Client artifacts and their contents will remain compatible within a major release. It is the goal of the Hadoop development community to allow application code to continue to function unchanged across minor releases and, whenever possible, across major releases. The current list of client artifacts is as follows:

* hadoop-client
* hadoop-client-api
* hadoop-client-minicluster
* hadoop-client-runtime
* hadoop-hdfs-client
* hadoop-hdfs-native-client
* hadoop-mapreduce-client-app
* hadoop-mapreduce-client-common
* hadoop-mapreduce-client-core
* hadoop-mapreduce-client-jobclient
* hadoop-mapreduce-client-nativetask
* hadoop-yarn-client

### Environment Variables

Some Hadoop components receive information through environment variables. For example, the `HADOOP_OPTS` environment variable is interpreted by most Hadoop processes as a string of additional JVM arguments to be used when starting a new JVM. Between minor releases the way Hadoop interprets environment variables will not change in an incompatible way. In other words, the same value placed into the same variable should produce the same result for all Hadoop releases within the same major version.

### Library Dependencies

Hadoop relies on a large number of third-party libraries for its operation. As much as possible the Hadoop developer community works to hide these dependencies from downstream developers. Some common libraries, such as Guava, could cause significant compatibility issues between Hadoop and downstream applications if those dependencies were exposed downstream. Nonetheless Hadoop does expose some of its dependencies, especially prior to Hadoop 3. No new dependency will be exposed by Hadoop via the client artifacts between major releases.

A common downstream anti-pattern is to use the output of `hadoop classpath` to set the downstream application’s classpath or add all third-party JARs included with Hadoop to the downstream application’s classpath. This practice creates a tight coupling between the downstream application and Hadoop’s third-party dependencies, which leads to a fragile application that is hard to maintain as Hadoop’s dependencies change. This practice is strongly discouraged.

Hadoop depends on the Java virtual machine for its operation, which can impact downstream applications. To minimize disruption, the minimum supported version of the JVM will not change between major releases of Hadoop. In the event that the current minimum supported JVM version becomes unsupported between major releases, the minimum supported JVM version may be changed in a minor release.

Hadoop also includes several native components, including compression, the container executor binary, and various native integrations. These native components introduce a set of native dependencies for Hadoop. The set of native dependencies can change in a minor release, but the Hadoop developer community will try to limit any dependency version changes to minor version changes as much as possible.

### Hardware and OS Dependencies

Hadoop is currently supported by the Hadoop developer community on Linux and Windows running on x86 and AMD processors. These OSes and processors are likely to remain supported for the foreseeable future. In the event that support plans change, the OS or processor to be dropped will be documented as deprecated for at least a full minor release, but ideally a full major release, before actually being dropped. Hadoop may function on other OSes and processor architectures, but the community may not be able to provide assistance in the event of issues.

There are no guarantees on how the minimum resources required by Hadoop daemons will change between releases, even maintenance releases. Nonetheless, the Hadoop developer community will try to avoid increasing the requirements within a minor release.

Any file systems supported Hadoop, such as through the FileSystem API, will in most cases continue to be supported throughout a major release. The only case where support for a file system can be dropped within a major version is if a clean migration path to an alternate client implementation is provided.

## Questions

For question about developing applications and projects against Apache Hadoop, please contact the developer mailing list for the relevant component(s):

* [common-dev](mailto:common-dev@hadoop.apache.org)
* [hdfs-dev](mailto:hdfs-dev@hadoop.apache.org)
* [mapreduce-dev](mailto:mapreduce-dev@hadoop.apache.org)
* [yarn-dev](mailto:yarn-dev@hadoop.apache.org)

---
# Apache Hadoop Compatibility

* [Purpose](#Purpose)
  * [Target Audience](#Target_Audience)
* [Hadoop Releases](#Hadoop_Releases)
* [Platform Dependencies](#Platform_Dependencies)
* [Network](#Network)
* [Scripting and Automation](#Scripting_and_Automation)
  * [REST APIs](#REST_APIs)
  * [Parsing Hadoop Output](#Parsing_Hadoop_Output)
  * [CLIs](#CLIs)
  * [Web UI](#Web_UI)
* [Hadoop State Data](#Hadoop_State_Data)
* [Hadoop Configurations](#Hadoop_Configurations)
  * [XML Configuration Files](#XML_Configuration_Files)
  * [Logging Configuration Files](#Logging_Configuration_Files)
  * [Other Configuration Files](#Other_Configuration_Files)
* [Hadoop Distribution](#Hadoop_Distribution)
  * [Configuration Files](#Configuration_Files)
  * [JARs, etc.](#JARs.2C_etc.)
  * [Environment Variables](#Environment_Variables)
  * [Library Dependencies](#Library_Dependencies)
  * [Hardware and OS Dependencies](#Hardware_and_OS_Dependencies)
* [Questions](#Questions)

## Purpose

This purpose of this document is to distill down the [Hadoop Compatibility Guidelines](./Compatibility.html) into the information relevant for a system administrator.

### Target Audience

The target audience is administrators who are responsible for maintaining Apache Hadoop clusters and who must plan for and execute cluster upgrades.

## Hadoop Releases

The Hadoop development community periodically produces new Hadoop releases to introduce new functionality and fix existing issues. Realeses fall into three categories:

* Major: a major release will typically include significant new functionality and generally represents the largest upgrade compatibility risk. A major release increments the first number of the release version, e.g. going from 2.8.2 to 3.0.0.
* Minor: a minor release will typically include some new functionality as well as fixes for some notable issues. A minor release should not pose much upgrade risk in most cases. A minor release increments the middle number of release version, e.g. going from 2.8.2 to 2.9.0.
* Maintenance: a maintenance release should not include any new functionality. The purpose of a maintenance release is to resolve a set of issues that are deemed by the developer community to be significant enough to be worth pushing a new release to address them. Maintenance releases should pose very little upgrade risk. A maintenance release increments the final number in the release version, e.g. going from 2.8.2 to 2.8.3.

## Platform Dependencies

The set of native components on which Hadoop depends is considered part of the Hadoop ABI. The Hadoop development community endeavors to maintain ABI compatibility to the fullest extent possible. Between minor releases the minimum supported version numbers for Hadoop’s native dependencies will not be increased unless necessary, such as for security or licensing issues. When such changes occur, the Hadoop developer community to try to keep the same major version and only update the minor version.

Hadoop depends on the Java virtual machine. The minimum supported version of the JVM will not change between major releases of Hadoop. In the event that the current minimum supported JVM version becomes unsupported between major releases, the minimum supported JVM version may be changed in a minor release.

## Network

Hadoop has dependencies on some transport level technologies, such as SSL. The minimum supported version of these dependencies will not be increased unless necessary, such as for security or licensing issues. When such changes occur, the Hadoop developer community to try to keep the same major version and only update the minor version.

Service port numbers for Hadoop will remain the same within a major version, though may be changed in a major release.

Hadoop’s internal wire protocols will be maintained as backward and forward compatible across minor releases within the same major version, both between clients and servers and between servers, with the intent of enabling rolling upgrades. Forward and backward compatibility of wire protocols across major releases may be possible and may allow for rolling upgrades under certain conditions, but no guarantees are made.

## Scripting and Automation

### REST APIs

The Hadoop REST APIs provide an easy mechanism for collecting information about the state of the Hadoop system. To support REST clients, the Hadoop REST APIs are versioned and will not change incompatibly within a version. Both the endpoint itself along with the list of supported parameters and the output from the endpoint are prohibited from changing incompatibly within a REST endpoint version. Note, however, that introducing new fields and other additive changes are considered compatible changes, so any consumer of the REST API should be flexible enough to ignore unknown fields.

The REST API version is a single number and has no relationship with the Hadoop version number. The version number is encoded in the endpoint URL prefixed with a ‘v’, for example ‘v1’. A new REST endpoint version may only be introduced with a minor or major release. A REST endpoint version may only be removed after being labeled as deprecated for a full major release.

### Parsing Hadoop Output

Hadoop produces a variety of outputs that could conceivably parsed by automated tools. When consuming output from Hadoop, please consider the following:

* Hadoop log output is not expected to change with a maintenance release unless it resolves a correctness issue. While log output can be consumed by software directly, it is intended primarily for a human reader.
* Hadoop produces audit logs for a variety of operations. The audit logs are intended to be machine readable, though the addition of new records and fields are considered to be compatible changes. Any consumer of the audit logs should allow for unexpected records and fields. The audit log format may not change incompatibly between major releases.
* Metrics data produced by Hadoop is mostly intended for automated consumption. The metrics format may not change in an incompatible way between major releases, but new records and fields can be compatibly added at any time. Consumers of the metrics data should allow for unknown records and fields.

### CLIs

Hadoop’s set of CLIs provide the ability to manage various aspects of the system as well as discover information about the system’s state. Between major releases, no CLI tool options will be removed or change semantically. The exception to that rule is CLI tools and tool options that are explicitly labeled as experimental and subject to change. The output from CLI tools will likewise remain the same within a major version number unless otherwise documented.

Note that any change to CLI tool output is considered an incompatible change, so between major versions, the CLI output will not change. Note that the CLI tool output is distinct from the log output produced by the CLI tools. Log output is not intended for automated consumption and may change at any time.

### Web UI

The web UIs that are exposed by Hadoop are for human consumption only. Scraping the UIs for data is not a supported use. No effort is made to ensure any kind of compatibility between the data displayed in any of the web UIs across releases.

## Hadoop State Data

Hadoop’s internal system state is private and should not be modified directly. The following policies govern the upgrade characteristics of the various internal state stores:

* The internal MapReduce state data will remain compatible across minor releases within the same major version to facilitate rolling upgrades while MapReduce workloads execute.
* HDFS maintains metadata about the data stored in HDFS in a private, internal format that is versioned. In the event of an incompatible change, the store’s version number will be incremented. When upgrading an existing cluster, the metadata store will automatically be upgraded if possible. After the metadata store has been upgraded, it is always possible to reverse the upgrade process.
* The AWS S3A guard kept a private, internal metadata store. Now that the feature has been removed, the store is obsolete and can be deleted.
* The YARN resource manager keeps a private, internal state store of application and scheduler information that is versioned. Incompatible changes will cause the version number to be incremented. If an upgrade requires reformatting the store, it will be indicated in the release notes.
* The YARN node manager keeps a private, internal state store of application information that is versioned. Incompatible changes will cause the version number to be incremented. If an upgrade requires reformatting the store, it will be indicated in the release notes.
* The YARN federation service keeps a private, internal state store of application and cluster information that is versioned. Incompatible changes will cause the version number to be incremented. If an upgrade requires reformatting the store, it will be indicated in the release notes.

## Hadoop Configurations

Hadoop uses two primary forms of configuration files: XML configuration files and logging configuration files.

### XML Configuration Files

The XML configuration files contain a set of properties as name-value pairs. The names and meanings of the properties are defined by Hadoop and are guaranteed to be stable across minor releases. A property can only be removed in a major release and only if it has been marked as deprecated for at least a full major release. Most properties have a default value that will be used if the property is not explicitly set in the XML configuration files. The default property values will not be changed during a maintenance releas. For details about the properties supported by the various Hadoop components, see the component documentation.

Downstream projects and users can add their own properties into the XML configuration files for use by their tools and applications. While Hadoop makes no formal restrictions about defining new properties, a new property that conflicts with a property defined by Hadoop can lead to unexpected and undesirable results. Users are encouraged to avoid using custom configuration property names that conflict with the namespace of Hadoop-defined properties and thus should avoid using any prefixes used by Hadoop, e.g. hadoop, io, ipc, fs, net, file, ftp, kfs, ha, file, dfs, mapred, mapreduce, and yarn.

### Logging Configuration Files

The log output produced by Hadoop daemons and CLIs is governed by a set of configuration files. These files control the minimum level of log message that will be output by the various components of Hadoop, as well as where and how those messages are stored. Between minor releases no changes will be made to the log configuration that reduce, eliminate, or redirect the log messages.

### Other Configuration Files

Hadoop makes use of a number of other types of configuration files in a variety of formats, such as the JSON resource profiles configuration or the XML fair scheduler configuration. No incompatible changes will be introduced to the configuration file formats within a minor release. Even between minor releases incompatible configuration file format changes will be avoided if possible.

## Hadoop Distribution

### Configuration Files

The location and general structure of the Hadoop configuration files, job history information (as consumed by the job history server), and logs files generated by Hadoop will be maintained across maintenance releases.

### JARs, etc.

The contents of the Hadoop distribution, e.g. JAR files, are subject to change at any time and should not be treated as reliable, except for the client artifacts. Client artifacts and their contents will remain compatible within a major release. It is the goal of the Hadoop development community to allow application code to continue to function unchanged across minor releases and, whenever possible, across major releases. The current list of client artifacts is as follows:

* hadoop-client
* hadoop-client-api
* hadoop-client-minicluster
* hadoop-client-runtime
* hadoop-hdfs-client
* hadoop-hdfs-native-client
* hadoop-mapreduce-client-app
* hadoop-mapreduce-client-common
* hadoop-mapreduce-client-core
* hadoop-mapreduce-client-jobclient
* hadoop-mapreduce-client-nativetask
* hadoop-yarn-client

### Environment Variables

Some Hadoop components receive information through environment variables. For example, the `HADOOP_OPTS` environment variable is interpreted by most Hadoop processes as a string of additional JVM arguments to be used when starting a new JVM. Between minor releases the way Hadoop interprets environment variables will not change in an incompatible way. In other words, the same value placed into the same variable should produce the same result for all Hadoop releases within the same major version.

### Library Dependencies

Hadoop relies on a large number of third-party libraries for its operation. As much as possible the Hadoop developer community works to hide these dependencies from downstream developers. Nonetheless Hadoop does expose some of its dependencies, especially prior to Hadoop 3. No new dependency will be exposed by Hadoop via the client artifacts between major releases.

A common downstream anti-pattern is to use the output of `hadoop classpath` to set the downstream application’s classpath or add all third-party JARs included with Hadoop to the downstream application’s classpath. This practice creates a tight coupling between the downstream application and Hadoop’s third-party dependencies, which leads to a fragile application that is hard to maintain as Hadoop’s dependencies change. This practice is strongly discouraged.

Hadoop also includes several native components, including compression, the container executor binary, and various native integrations. These native components introduce a set of native dependencies for Hadoop. The set of native dependencies can change in a minor release, but the Hadoop developer community will try to limit any dependency version changes to minor version changes as much as possible.

### Hardware and OS Dependencies

Hadoop is currently supported by the Hadoop developer community on Linux and Windows running on x86 and AMD processors. These OSes and processors are likely to remain supported for the foreseeable future. In the event that support plans change, the OS or processor to be dropped will be documented as deprecated for at least a full minor release, but ideally a full major release, before actually being dropped. Hadoop may function on other OSes and processor architectures, but the community may not be able to provide assistance in the event of issues.

There are no guarantees on how the minimum resources required by Hadoop daemons will change between releases, even maintenance releases. Nonetheless, the Hadoop developer community will try to avoid increasing the requirements within a minor release.

Any file systems supported Hadoop, such as through the FileSystem API, will in most cases continue to be supported throughout a major release. The only case where support for a file system can be dropped within a major version is if a clean migration path to an alternate client implementation is provided.

## Questions

For question about developing applications and projects against Apache Hadoop, please contact the [user mailing list](mailto:user@hadoop.apache.org).

---
# Service Level Authorization Guide

* [Purpose](#Purpose)
* [Prerequisites](#Prerequisites)
* [Overview](#Overview)
* [Configuration](#Configuration)
  * [Enable Service Level Authorization](#Enable_Service_Level_Authorization)
  * [Hadoop Services and Configuration Properties](#Hadoop_Services_and_Configuration_Properties)
  * [Access Control Lists](#Access_Control_Lists)
  * [Blocked Access Control Lists](#Blocked_Access_Control_Lists)
  * [Access Control using Lists of IP Addresses, Host Names and IP Ranges](#Access_Control_using_Lists_of_IP_Addresses.2C_Host_Names_and_IP_Ranges)
  * [Refreshing Service Level Authorization Configuration](#Refreshing_Service_Level_Authorization_Configuration)
  * [Examples](#Examples)

## Purpose

This document describes how to configure and manage Service Level Authorization for Hadoop.

## Prerequisites

Make sure Hadoop is installed, configured and setup correctly. For more information see:

* [Single Node Setup](./SingleCluster.html) for first-time users.
* [Cluster Setup](./ClusterSetup.html) for large, distributed clusters.

## Overview

Service Level Authorization is the initial authorization mechanism to ensure clients connecting to a particular Hadoop service have the necessary, pre-configured, permissions and are authorized to access the given service. For example, a MapReduce cluster can use this mechanism to allow a configured list of users/groups to submit jobs.

The `$HADOOP_CONF_DIR/hadoop-policy.xml` configuration file is used to define the access control lists for various Hadoop services.

Service Level Authorization is performed much before to other access control checks such as file-permission checks, access control on job queues etc.

## Configuration

This section describes how to configure service-level authorization via the configuration file `$HADOOP_CONF_DIR/hadoop-policy.xml`.

### Enable Service Level Authorization

By default, service-level authorization is disabled for Hadoop. To enable it set the configuration property hadoop.security.authorization to true in `$HADOOP_CONF_DIR/core-site.xml`.

### Hadoop Services and Configuration Properties

This section lists the various Hadoop services and their configuration knobs:

| Property | Service |
| --- | --- |
| security.client.protocol.acl | ACL for ClientProtocol, which is used by user code via the DistributedFileSystem. |
| security.client.datanode.protocol.acl | ACL for ClientDatanodeProtocol, the client-to-datanode protocol for block recovery. |
| security.datanode.protocol.acl | ACL for DatanodeProtocol, which is used by datanodes to communicate with the namenode. |
| security.inter.datanode.protocol.acl | ACL for InterDatanodeProtocol, the inter-datanode protocol for updating generation timestamp. |
| security.namenode.protocol.acl | ACL for NamenodeProtocol, the protocol used by the secondary namenode to communicate with the namenode. |
| security.job.client.protocol.acl | ACL for JobSubmissionProtocol, used by job clients to communciate with the resourcemanager for job submission, querying job status etc. |
| security.job.task.protocol.acl | ACL for TaskUmbilicalProtocol, used by the map and reduce tasks to communicate with the parent nodemanager. |
| security.refresh.policy.protocol.acl | ACL for RefreshAuthorizationPolicyProtocol, used by the dfsadmin and rmadmin commands to refresh the security policy in-effect. |
| security.ha.service.protocol.acl | ACL for HAService protocol used by HAAdmin to manage the active and stand-by states of namenode. |

### Access Control Lists

`$HADOOP_CONF_DIR/hadoop-policy.xml` defines an access control list for each Hadoop service. Every access control list has a simple format:

The list of users and groups are both comma separated list of names. The two lists are separated by a space.

Example: `user1,user2 group1,group2`.

Add a blank at the beginning of the line if only a list of groups is to be provided, equivalently a comma-separated list of users followed by a space or nothing implies only a set of given users.

A special value of `*` implies that all users are allowed to access the service.

If access control list is not defined for a service, the value of `security.service.authorization.default.acl` is applied. If `security.service.authorization.default.acl` is not defined, `*` is applied.

### Blocked Access Control Lists

In some cases, it is required to specify blocked access control list for a service. This specifies the list of users and groups who are not authorized to access the service. The format of the blocked access control list is same as that of access control list. The blocked access control list can be specified via `$HADOOP_CONF_DIR/hadoop-policy.xml`. The property name is derived by suffixing with “.blocked”.

Example: The property name of blocked access control list for `security.client.protocol.acl` will be `security.client.protocol.acl.blocked`

For a service, it is possible to specify both an access control list and a blocked control list. A user is authorized to access the service if the user is in the access control and not in the blocked access control list.

If blocked access control list is not defined for a service, the value of `security.service.authorization.default.acl.blocked` is applied. If `security.service.authorization.default.acl.blocked` is not defined, empty blocked access control list is applied.

### Access Control using Lists of IP Addresses, Host Names and IP Ranges

Access to a service can be controlled based on the ip address of the client accessing the service. It is possible to restrict access to a service from a set of machines by specifying a list of ip addresses, host names and ip ranges. The property name for each service is derived from the corresponding acl’s property name. If the property name of acl is security.client.protocol.acl, property name for the hosts list will be security.client.protocol.hosts.

If hosts list is not defined for a service, the value of `security.service.authorization.default.hosts` is applied. If `security.service.authorization.default.hosts` is not defined, `*` is applied.

It is possible to specify a blocked list of hosts. Only those machines which are in the hosts list, but not in the blocked hosts list will be granted access to the service. The property name is derived by suffixing with “.blocked”.

Example: The property name of blocked hosts list for `security.client.protocol.hosts` will be `security.client.protocol.hosts.blocked`

If blocked hosts list is not defined for a service, the value of `security.service.authorization.default.hosts.blocked` is applied. If `security.service.authorization.default.hosts.blocked` is not defined, empty blocked hosts list is applied.

### Refreshing Service Level Authorization Configuration

The service-level authorization configuration for the NameNode and ResourceManager can be changed without restarting either of the Hadoop master daemons. The cluster administrator can change `$HADOOP_CONF_DIR/hadoop-policy.xml` on the master nodes and instruct the NameNode and ResourceManager to reload their respective configurations via the `-refreshServiceAcl` switch to `dfsadmin` and `rmadmin` commands respectively.

Refresh the service-level authorization configuration for the NameNode:

```
   $ bin/hdfs dfsadmin -refreshServiceAcl
```

Refresh the service-level authorization configuration for the ResourceManager:

```
   $ bin/yarn rmadmin -refreshServiceAcl
```

Of course, one can use the `security.refresh.policy.protocol.acl` property in `$HADOOP_CONF_DIR/hadoop-policy.xml` to restrict access to the ability to refresh the service-level authorization configuration to certain users/groups.

### Examples

Allow only users `alice`, `bob` and users in the `mapreduce` group to submit jobs to the MapReduce cluster:

```
<property>
     <name>security.job.client.protocol.acl</name>
     <value>alice,bob mapreduce</value>
</property>
```

Allow only DataNodes running as the users who belong to the group datanodes to communicate with the NameNode:

```
<property>
     <name>security.datanode.protocol.acl</name>
     <value>datanodes</value>
</property>
```

Allow any user to talk to the HDFS cluster as a DFSClient:

```
<property>
     <name>security.client.protocol.acl</name>
     <value>*</value>
</property>
```

---
# Hadoop Service Registry

The Service registry is a service which can be deployed in a Hadoop cluster to allow deployed applications to register themselves and the means of communicating with them. Client applications can then locate services and use the binding information to connect with the services’s network-accessible endpoints, be they REST, IPC, Web UI, Zookeeper quorum+path or some other protocol. Currently, all the registry data is stored in a zookeeper cluster.

* [Architecture](hadoop-registry.html)
* [Configuration](registry-configuration.html)
* [Using the Hadoop Service registry](using-the-hadoop-service-registry.html)
* [Security](registry-security.html)
* [Registry DNS](registry-dns.html)

---
# Async Profiler Servlet for Hadoop

* [Purpose](#Purpose)
* [Prerequisites](#Prerequisites)
* [Usage](#Usage)

## Purpose

This document describes how to configure and use async profiler with Hadoop applications. Async profiler is a low overhead sampling profiler for Java that does not suffer from Safepoint bias problem. It features HotSpot-specific APIs to collect stack traces and to track memory allocations. The profiler works with OpenJDK, Oracle JDK and other Java runtimes based on the HotSpot JVM.

Hadoop profiler servlet supports Async Profiler major versions 1.x and 2.x.

## Prerequisites

Make sure Hadoop is installed, configured and setup correctly. For more information see:

* [Single Node Setup](./SingleCluster.html) for first-time users.
* [Cluster Setup](./ClusterSetup.html) for large, distributed clusters.

Go to <https://github.com/jvm-profiling-tools/async-profiler>, download a release appropriate for your platform, and install on every cluster host.

Set `ASYNC_PROFILER_HOME` in the environment (put it in hadoop-env.sh) to the root directory of the async-profiler install location, or pass it on the Hadoop daemon’s command line as a system property as `-Dasync.profiler.home=/path/to/async-profiler`.

## Usage

Once the prerequisites have been satisfied, access to the async-profiler is available by using Namenode or ResourceManager UI.

Following options from async-profiler can be specified as query paramater. \* `-e event` profiling event: cpu|alloc|lock|cache-misses etc. \* `-d duration` run profiling for ‘duration’ seconds (integer) \* `-i interval` sampling interval in nanoseconds (long) \* `-j jstackdepth` maximum Java stack depth (integer) \* `-b bufsize` frame buffer size (long) \* `-t` profile different threads separately \* `-s` simple class names instead of FQN \* `-o fmt[,fmt...]` output format: summary|traces|flat|collapsed|svg|tree|jfr|html \* `--width px` SVG width pixels (integer) \* `--height px` SVG frame height pixels (integer) \* `--minwidth px` skip frames smaller than px (double) \* `--reverse` generate stack-reversed FlameGraph / Call tree

Example: If Namenode http address is localhost:9870, and ResourceManager http address is localhost:8088, ProfileServlet running with async-profiler setup can be accessed with <http://localhost:9870/prof> and <http://localhost:8088/prof> for Namenode and ResourceManager processes respectively.

Diving deep into some params:

* To collect 10 second CPU profile of current process (returns FlameGraph svg)
* `curl http://localhost:9870/prof` (FlameGraph svg for Namenode)
* `curl http://localhost:8088/prof` (FlameGraph svg for ResourceManager)
* To collect 10 second CPU profile of pid 12345 (returns FlameGraph svg)
* `curl http://localhost:9870/prof?pid=12345` (For instance, provide pid of Datanode here)
* To collect 30 second CPU profile of pid 12345 (returns FlameGraph svg)
* `curl http://localhost:9870/prof?pid=12345&duration=30`
* To collect 1 minute CPU profile of current process and output in tree format (html)
* `curl http://localhost:9870/prof?output=tree&amp;duration=60`
* To collect 10 second heap allocation profile of current process (returns FlameGraph svg)
* `curl http://localhost:9870/prof?event=alloc`
* To collect lock contention profile of current process (returns FlameGraph svg)
* `curl http://localhost:9870/prof?event=lock`

The following event types are supported by async-profiler. Use the ‘event’ parameter to specify. Default is ‘cpu’. Not all operating systems will support all types.

Perf events:

* cpu
* page-faults
* context-switches
* cycles
* instructions
* cache-references
* cache-misses
* branches
* branch-misses
* bus-cycles
* L1-dcache-load-misses
* LLC-load-misses
* dTLB-load-misses

Java events:

* alloc
* lock

The following output formats are supported. Use the ‘output’ parameter to specify. Default is ‘flamegraph’.

Output formats:

* summary: A dump of basic profiling statistics.
* traces: Call traces.
* flat: Flat profile (top N hot methods).
* collapsed: Collapsed call traces in the format used by FlameGraph script. This is a collection of call stacks, where each line is a semicolon separated list of frames followed by a counter.
* svg: FlameGraph in SVG format.
* tree: Call tree in HTML format.
* jfr: Call traces in Java Flight Recorder format.

The ‘duration’ parameter specifies how long to collect trace data before generating output, specified in seconds. The default is 10 seconds.

---
# Enabling Dapper-like Tracing in Hadoop

* [Dapper-like Tracing in Hadoop](#Dapper-like_Tracing_in_Hadoop)
  * [HTrace](#HTrace)
  * [SpanReceivers](#SpanReceivers)
  * [Dynamic update of tracing configuration](#Dynamic_update_of_tracing_configuration)
  * [Starting tracing spans by HTrace API](#Starting_tracing_spans_by_HTrace_API)
  * [Sample code for tracing by HTrace API](#Sample_code_for_tracing_by_HTrace_API)
  * [Starting tracing spans by FileSystem Shell](#Starting_tracing_spans_by_FileSystem_Shell)
  * [Starting tracing spans by configuration for HDFS client](#Starting_tracing_spans_by_configuration_for_HDFS_client)

## Dapper-like Tracing in Hadoop

### HTrace

[HDFS-5274](https://issues.apache.org/jira/browse/HDFS-5274) added support for tracing requests through HDFS, using the open source tracing library, [Apache HTrace](http://htrace.incubator.apache.org/). Setting up tracing is quite simple, however it requires some very minor changes to your client code.

### SpanReceivers

The tracing system works by collecting information in structs called ‘Spans’. It is up to you to choose how you want to receive this information by using implementation of [SpanReceiver](http://htrace.incubator.apache.org/developer_guide.html#SpanReceivers) interface bundled with HTrace or implementing it by yourself.

[HTrace](http://htrace.incubator.apache.org/) provides options such as

* FlumeSpanReceiver
* HBaseSpanReceiver
* HTracedRESTReceiver
* ZipkinSpanReceiver

See core-default.xml for a description of HTrace configuration keys. In some cases, you will also need to add the jar containing the SpanReceiver that you are using to the classpath of Hadoop on each node. (In the example above, LocalFileSpanReceiver is included in the htrace-core4 jar which is bundled with Hadoop.)

```
    $ cp htrace-htraced/target/htrace-htraced-4.1.0-incubating.jar $HADOOP_HOME/share/hadoop/common/lib/
```

### Dynamic update of tracing configuration

You can use `hadoop trace` command to see and update the tracing configuration of each servers. You must specify IPC server address of namenode or datanode by `-host` option. You need to run the command against all servers if you want to update the configuration of all servers.

`hadoop trace -list` shows list of loaded span receivers associated with the id.

```
  $ hadoop trace -list -host 192.168.56.2:9000
  ID  CLASS
  1   org.apache.htrace.core.LocalFileSpanReceiver

  $ hadoop trace -list -host 192.168.56.2:9867
  ID  CLASS
  1   org.apache.htrace.core.LocalFileSpanReceiver
```

`hadoop trace -remove` removes span receiver from server. `-remove` options takes id of span receiver as argument.

```
  $ hadoop trace -remove 1 -host 192.168.56.2:9000
  Removed trace span receiver 1
```

`hadoop trace -add` adds span receiver to server. You need to specify the class name of span receiver as argument of `-class` option. You can specify the configuration associated with span receiver by `-Ckey=value` options.

```
  $ hadoop trace -add -class org.apache.htrace.core.LocalFileSpanReceiver -Chadoop.htrace.local.file.span.receiver.path=/tmp/htrace.out -host 192.168.56.2:9000
  Added trace span receiver 2 with configuration hadoop.htrace.local.file.span.receiver.path = /tmp/htrace.out

  $ hadoop trace -list -host 192.168.56.2:9000
  ID  CLASS
  2   org.apache.htrace.core.LocalFileSpanReceiver
```

If the cluster is Kerberized, the service principal name must be specified using `-principal` option. For example, to show list of span receivers of a namenode:

```
$ hadoop trace -list -host NN1:8020 -principal namenode/NN1@EXAMPLE.COM
```

Or, for a datanode:

```
$ hadoop trace -list -host DN2:9867 -principal datanode/DN1@EXAMPLE.COM
```

### Starting tracing spans by HTrace API

In order to trace, you will need to wrap the traced logic with **tracing span** as shown below. When there is running tracing spans, the tracing information is propagated to servers along with RPC requests.

```
    import org.apache.hadoop.hdfs.HdfsConfiguration;
    import org.apache.htrace.core.Tracer;
    import org.apache.htrace.core.TraceScope;

    ...


    ...

        TraceScope ts = tracer.newScope("Gets");
        try {
          ... // traced logic
        } finally {
          ts.close();
        }
```

### Sample code for tracing by HTrace API

The `TracingFsShell.java` shown below is the wrapper of FsShell which start tracing span before invoking HDFS shell command.

```
    import org.apache.hadoop.fs.FileSystem;
    import org.apache.hadoop.fs.Path;
    import org.apache.hadoop.conf.Configuration;
    import org.apache.hadoop.conf.Configured;
    import org.apache.hadoop.tracing.TraceUtils;
    import org.apache.hadoop.util.Tool;
    import org.apache.hadoop.util.ToolRunner;
    import org.apache.htrace.core.Tracer;
    import org.apache.htrace.core.TraceScope;
    
    public class Sample extends Configured implements Tool {
      @Override
      public int run(String argv[]) throws Exception {
        FileSystem fs = FileSystem.get(getConf());
        Tracer tracer = new Tracer.Builder("Sample").
            conf(TraceUtils.wrapHadoopConf("sample.htrace.", getConf())).
            build();
        int res = 0;
        try (TraceScope scope = tracer.newScope("sample")) {
          Thread.sleep(1000);
          fs.listStatus(new Path("/"));
        }
        tracer.close();
        return res;
      }
      
      public static void main(String argv[]) throws Exception {
        ToolRunner.run(new Sample(), argv);
      }
    }
```

You can compile and execute this code as shown below.

```
$ javac -cp `hadoop classpath` Sample.java
$ java -cp .:`hadoop classpath` Sample \
    -Dsample.htrace.span.receiver.classes=LocalFileSpanReceiver \
    -Dsample.htrace.sampler.classes=AlwaysSampler
```

### Starting tracing spans by FileSystem Shell

The FileSystem Shell can enable tracing by configuration properties.

Configure the span receivers and samplers in `core-site.xml` or command line by properties `fs.client.htrace.sampler.classes` and `fs.client.htrace.spanreceiver.classes`.

```
$ hdfs dfs -Dfs.shell.htrace.span.receiver.classes=LocalFileSpanReceiver \
           -Dfs.shell.htrace.sampler.classes=AlwaysSampler \
           -ls /
```

### Starting tracing spans by configuration for HDFS client

The DFSClient can enable tracing internally. This allows you to use HTrace with your client without modifying the client source code.

Configure the span receivers and samplers in `hdfs-site.xml` by properties `fs.client.htrace.sampler.classes` and `fs.client.htrace.spanreceiver.classes`. The value of `fs.client.htrace.sampler.classes` can be NeverSampler, AlwaysSampler or ProbabilitySampler.

* NeverSampler: HTrace is OFF for all requests to namenodes and datanodes;
* AlwaysSampler: HTrace is ON for all requests to namenodes and datanodes;
* ProbabilitySampler: HTrace is ON for some percentage% of requests to namenodes and datanodes

```
      <property>
        <name>hadoop.htrace.span.receiver.classes</name>
        <value>LocalFileSpanReceiver</value>
      </property>
      <property>
        <name>fs.client.htrace.sampler.classes</name>
        <value>ProbabilitySampler</value>
      </property>
      <property>
        <name>fs.client.htrace.sampler.fraction</name>
        <value>0.01</value>
      </property>
```

---
# Hadoop in Secure Mode

* [Introduction](#Introduction)
* [Authentication](#Authentication)
  * [End User Accounts](#End_User_Accounts)
  * [User Accounts for Hadoop Daemons](#User_Accounts_for_Hadoop_Daemons)
  * [Kerberos principals for Hadoop Daemons](#Kerberos_principals_for_Hadoop_Daemons)
    * [HDFS](#HDFS)
    * [YARN](#YARN)
    * [MapReduce JobHistory Server](#MapReduce_JobHistory_Server)
  * [Mapping from Kerberos principals to OS user accounts](#Mapping_from_Kerberos_principals_to_OS_user_accounts)
  * [Example rules](#Example_rules)
  * [Mapping from user to group](#Mapping_from_user_to_group)
  * [Proxy user](#Proxy_user)
  * [Secure DataNode](#Secure_DataNode)
* [Data confidentiality](#Data_confidentiality)
  * [Data Encryption on RPC](#Data_Encryption_on_RPC)
  * [Data Encryption on Block data transfer.](#Data_Encryption_on_Block_data_transfer.)
  * [Data Encryption on HTTP](#Data_Encryption_on_HTTP)
* [Configuration](#Configuration)
  * [Permissions for both HDFS and local fileSystem paths](#Permissions_for_both_HDFS_and_local_fileSystem_paths)
  * [Common Configurations](#Common_Configurations)
  * [NameNode](#NameNode)
  * [Secondary NameNode](#Secondary_NameNode)
  * [JournalNode](#JournalNode)
  * [DataNode](#DataNode)
  * [WebHDFS](#WebHDFS)
  * [ResourceManager](#ResourceManager)
  * [NodeManager](#NodeManager)
  * [Configuration for WebAppProxy](#Configuration_for_WebAppProxy)
  * [LinuxContainerExecutor](#LinuxContainerExecutor)
  * [MapReduce JobHistory Server](#MapReduce_JobHistory_Server)
* [Multihoming](#Multihoming)
* [Troubleshooting](#Troubleshooting)
* [Troubleshooting with KDiag](#Troubleshooting_with_KDiag)
  * [Usage](#Usage)
    * [--jaas: Require a JAAS file to be defined in java.security.auth.login.config.](#a--jaas:_Require_a_JAAS_file_to_be_defined_in_java.security.auth.login.config.)
    * [--keylen <length>: Require a minimum size for encryption keys supported by the JVM".](#a--keylen_.3Clength.3E:_Require_a_minimum_size_for_encryption_keys_supported_by_the_JVM.22.)
    * [--keytab <keytab> --principal <principal>: Log in from a keytab.](#a--keytab_.3Ckeytab.3E_--principal_.3Cprincipal.3E:_Log_in_from_a_keytab.)
    * [--nofail : Do not fail on the first problem](#a--nofail_:_Do_not_fail_on_the_first_problem)
    * [--nologin: Do not attempt to log in.](#a--nologin:_Do_not_attempt_to_log_in.)
    * [--out outfile: Write output to file.](#a--out_outfile:_Write_output_to_file.)
    * [--resource <resource> : XML configuration resource to load.](#a--resource_.3Cresource.3E_:_XML_configuration_resource_to_load.)
    * [--secure: Fail if the command is not executed on a secure cluster.](#a--secure:_Fail_if_the_command_is_not_executed_on_a_secure_cluster.)
    * [--verifyshortname <principal>: validate the short name of a principal](#a--verifyshortname_.3Cprincipal.3E:_validate_the_short_name_of_a_principal)
  * [Example](#Example)
* [References](#References)

## Introduction

In its default configuration, we expect you to make sure attackers don’t have access to your Hadoop cluster by restricting all network access. If you want any restrictions on who can remotely access data or submit work, you MUST secure authentication and access for your Hadoop cluster as described in this document.

When Hadoop is configured to run in secure mode, each Hadoop service and each user must be authenticated by Kerberos.

Forward and reverse host lookup for all service hosts must be configured correctly to allow services to authenticate with each other. Host lookups may be configured using either DNS or `/etc/hosts` files. Working knowledge of Kerberos and DNS is recommended before attempting to configure Hadoop services in Secure Mode.

Security features of Hadoop consist of [Authentication](#Authentication), [Service Level Authorization](./ServiceLevelAuth.html), [Authentication for Web Consoles](./HttpAuthentication.html) and [Data Confidentiality](#Data_confidentiality).

## Authentication

### End User Accounts

When service level authentication is turned on, end users must authenticate themselves before interacting with Hadoop services. The simplest way is for a user to authenticate interactively using the [Kerberos `kinit` command](http://web.mit.edu/kerberos/krb5-1.12/doc/user/user_commands/kinit.html "MIT Kerberos Documentation of kinit"). Programmatic authentication using Kerberos keytab files may be used when interactive login with `kinit` is infeasible.

### User Accounts for Hadoop Daemons

Ensure that HDFS and YARN daemons run as different Unix users, e.g. `hdfs` and `yarn`. Also, ensure that the MapReduce JobHistory server runs as different user such as `mapred`.

It’s recommended to have them share a Unix group, e.g. `hadoop`. See also “[Mapping from user to group](#Mapping_from_user_to_group)” for group management.

| User:Group | Daemons |
| --- | --- |
| hdfs:hadoop | NameNode, Secondary NameNode, JournalNode, DataNode |
| yarn:hadoop | ResourceManager, NodeManager |
| mapred:hadoop | MapReduce JobHistory Server |

### Kerberos principals for Hadoop Daemons

Each Hadoop Service instance must be configured with its Kerberos principal and keytab file location.

The general format of a Service principal is `ServiceName/_HOST@REALM.TLD`. e.g. `dn/_HOST@EXAMPLE.COM`.

Hadoop simplifies the deployment of configuration files by allowing the hostname component of the service principal to be specified as the `_HOST` wildcard. Each service instance will substitute `_HOST` with its own fully qualified hostname at runtime. This allows administrators to deploy the same set of configuration files on all nodes. However, the keytab files will be different.

#### HDFS

The NameNode keytab file, on each NameNode host, should look like the following:

```
$ klist -e -k -t /etc/security/keytab/nn.service.keytab
Keytab name: FILE:/etc/security/keytab/nn.service.keytab
KVNO Timestamp         Principal
   4 07/18/11 21:08:09 nn/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 nn/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 nn/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
```

The Secondary NameNode keytab file, on that host, should look like the following:

```
$ klist -e -k -t /etc/security/keytab/sn.service.keytab
Keytab name: FILE:/etc/security/keytab/sn.service.keytab
KVNO Timestamp         Principal
   4 07/18/11 21:08:09 sn/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 sn/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 sn/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
```

The DataNode keytab file, on each host, should look like the following:

```
$ klist -e -k -t /etc/security/keytab/dn.service.keytab
Keytab name: FILE:/etc/security/keytab/dn.service.keytab
KVNO Timestamp         Principal
   4 07/18/11 21:08:09 dn/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 dn/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 dn/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
```

#### YARN

The ResourceManager keytab file, on the ResourceManager host, should look like the following:

```
$ klist -e -k -t /etc/security/keytab/rm.service.keytab
Keytab name: FILE:/etc/security/keytab/rm.service.keytab
KVNO Timestamp         Principal
   4 07/18/11 21:08:09 rm/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 rm/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 rm/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
```

The NodeManager keytab file, on each host, should look like the following:

```
$ klist -e -k -t /etc/security/keytab/nm.service.keytab
Keytab name: FILE:/etc/security/keytab/nm.service.keytab
KVNO Timestamp         Principal
   4 07/18/11 21:08:09 nm/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 nm/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 nm/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
```

#### MapReduce JobHistory Server

The MapReduce JobHistory Server keytab file, on that host, should look like the following:

```
$ klist -e -k -t /etc/security/keytab/jhs.service.keytab
Keytab name: FILE:/etc/security/keytab/jhs.service.keytab
KVNO Timestamp         Principal
   4 07/18/11 21:08:09 jhs/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 jhs/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 jhs/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
   4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
```

### Mapping from Kerberos principals to OS user accounts

Hadoop maps Kerberos principals to OS user (system) accounts using rules specified by `hadoop.security.auth_to_local`. How Hadoop evaluates these rules is determined by the setting of `hadoop.security.auth_to_local.mechanism`.

In the default `hadoop` mode a Kerberos principal *must* be matched against a rule that transforms the principal to a simple form, i.e. a user account name without ‘@’ or ‘/’, otherwise a principal will not be authorized and a error will be logged. In case of the `MIT` mode the rules work in the same way as the `auth_to_local` in [Kerberos configuration file (krb5.conf)](http://web.mit.edu/Kerberos/krb5-latest/doc/admin/conf_files/krb5_conf.html) and the restrictions of `hadoop` mode do *not* apply. If you use `MIT` mode it is suggested to use the same `auth_to_local` rules that are specified in your /etc/krb5.conf as part of your default realm and keep them in sync. In both `hadoop` and `MIT` mode the rules are being applied (with the exception of `DEFAULT`) to *all* principals regardless of their specified realm. Also, note you should *not* rely on the `auth_to_local` rules as an ACL and use proper (OS) mechanisms.

Possible values for `auth_to_local` are:

* `RULE:exp` The local name will be formulated from exp. The format for exp is `[n:string](regexp)s/pattern/replacement/g`. The integer n indicates how many components the target principal should have. If this matches, then a string will be formed from string, substituting the realm of the principal for `$0` and the n’th component of the principal for `$n` (e.g., if the principal was johndoe/admin then `[2:$2$1foo]` would result in the string `adminjohndoefoo`). If this string matches regexp, then the `s//[g]` substitution command will be run over the string. The optional g will cause the substitution to be global over the string, instead of replacing only the first match in the string. As an extension to MIT, Hadoop `auth_to_local` mapping supports the **/L** flag that lowercases the returned name.
* `DEFAULT` Picks the first component of the principal name as the system user name if and only if the realm matches the `default_realm` (usually defined in /etc/krb5.conf). e.g. The default rule maps the principal `host/full.qualified.domain.name@MYREALM.TLD` to system user `host` if the default realm is `MYREALM.TLD`.

In case no rules are specified Hadoop defaults to using `DEFAULT`, which is probably *not suitable* to most of the clusters.

Please note that Hadoop does not support multiple default realms (e.g like Heimdal does). Also, Hadoop does not do a verification on mapping whether a local system account exists.

### Example rules

In a typical cluster HDFS and YARN services will be launched as the system `hdfs` and `yarn` users respectively. `hadoop.security.auth_to_local` can be configured as follows:

```
<property>
  <name>hadoop.security.auth_to_local</name>
  <value>
    RULE:[2:$1/$2@$0]([ndj]n/.*@REALM.\TLD)s/.*/hdfs/
    RULE:[2:$1/$2@$0]([rn]m/.*@REALM\.TLD)s/.*/yarn/
    RULE:[2:$1/$2@$0](jhs/.*@REALM\.TLD)s/.*/mapred/
    DEFAULT
  </value>
</property>
```

This would map any principal `nn, dn, jn` on any `host` from realm `REALM.TLD` to the local system account `hdfs`. Secondly it would map any principal `rm, nm` on any `host` from `REALM.TLD` to the local system account `yarn`. Thirdly, it would map the principal `jhs` on any `host` from realm `REALM.TLD` to the local system account `mapred`. Finally, any principal on any host from the default realm will be mapped to the user component of that principal.

Custom rules can be tested using the `hadoop kerbname` command. This command allows one to specify a principal and apply Hadoop’s current `auth_to_local` ruleset.

### Mapping from user to group

The system user to system group mapping mechanism can be configured via `hadoop.security.group.mapping`. See [Hadoop Groups Mapping](GroupsMapping.html) for details.

Practically you need to manage SSO environment using Kerberos with LDAP for Hadoop in secure mode.

### Proxy user

Some products such as Apache Oozie which access the services of Hadoop on behalf of end users need to be able to impersonate end users. See [the doc of proxy user](./Superusers.html) for details.

### Secure DataNode

Because the DataNode data transfer protocol does not use the Hadoop RPC framework, DataNodes must authenticate themselves using privileged ports which are specified by `dfs.datanode.address` and `dfs.datanode.http.address`. This authentication is based on the assumption that the attacker won’t be able to get root privileges on DataNode hosts.

When you execute the `hdfs datanode` command as root, the server process binds privileged ports at first, then drops privilege and runs as the user account specified by `HDFS_DATANODE_SECURE_USER`. This startup process uses [the jsvc program](https://commons.apache.org/proper/commons-daemon/jsvc.html "Link to Apache Commons Jsvc") installed to `JSVC_HOME`. You must specify `HDFS_DATANODE_SECURE_USER` and `JSVC_HOME` as environment variables on start up (in `hadoop-env.sh`).

As of version 2.6.0, SASL can be used to authenticate the data transfer protocol. In this configuration, it is no longer required for secured clusters to start the DataNode as root using `jsvc` and bind to privileged ports. To enable SASL on data transfer protocol, set `dfs.data.transfer.protection` in hdfs-site.xml. A SASL enabled DataNode can be started in secure mode in following two ways: 1. Set a non-privileged port for `dfs.datanode.address`. 1. Set `dfs.http.policy` to `HTTPS_ONLY` or set `dfs.datanode.http.address` to a privileged port and make sure the `HDFS_DATANODE_SECURE_USER` and `JSVC_HOME` environment variables are specified properly as environment variables on start up (in `hadoop-env.sh`).

In order to migrate an existing cluster that used root authentication to start using SASL instead, first ensure that version 2.6.0 or later has been deployed to all cluster nodes as well as any external applications that need to connect to the cluster. Only versions 2.6.0 and later of the HDFS client can connect to a DataNode that uses SASL for authentication of data transfer protocol, so it is vital that all callers have the correct version before migrating. After version 2.6.0 or later has been deployed everywhere, update configuration of any external applications to enable SASL. If an HDFS client is enabled for SASL, then it can connect successfully to a DataNode running with either root authentication or SASL authentication. Changing configuration for all clients guarantees that subsequent configuration changes on DataNodes will not disrupt the applications. Finally, each individual DataNode can be migrated by changing its configuration and restarting. It is acceptable to have a mix of some DataNodes running with root authentication and some DataNodes running with SASL authentication temporarily during this migration period, because an HDFS client enabled for SASL can connect to both.

## Data confidentiality

### Data Encryption on RPC

The data transfered between hadoop services and clients can be encrypted on the wire. Setting `hadoop.rpc.protection` to `privacy` in `core-site.xml` activates data encryption.

### Data Encryption on Block data transfer.

You need to set `dfs.encrypt.data.transfer` to `true` in the hdfs-site.xml in order to activate data encryption for data transfer protocol of DataNode.

Optionally, you may set `dfs.encrypt.data.transfer.algorithm` to either `3des` or `rc4` to choose the specific encryption algorithm. If unspecified, then the configured JCE default on the system is used, which is usually 3DES.

Setting `dfs.encrypt.data.transfer.cipher.suites` to `AES/CTR/NoPadding` activates AES encryption. By default, this is unspecified, so AES is not used. When AES is used, the algorithm specified in `dfs.encrypt.data.transfer.algorithm` is still used during an initial key exchange. The AES key bit length can be configured by setting `dfs.encrypt.data.transfer.cipher.key.bitlength` to 128, 192 or 256. The default is 128.

AES offers the greatest cryptographic strength and the best performance. At this time, 3DES and RC4 have been used more often in Hadoop clusters.

You can also set `dfs.encrypt.data.transfer.cipher.suites` to `SM4/CTR/NoPadding` to activates SM4 encryption. By default, this is unspecified. The SM4 key bit length can be configured by setting `dfs.encrypt.data.transfer.cipher.key.bitlength` to 128, 192 or 256. The default is 128.

### Data Encryption on HTTP

Data transfer between Web-console and clients are protected by using SSL(HTTPS). SSL configuration is recommended but not required to configure Hadoop security with Kerberos.

To enable SSL for web console of HDFS daemons, set `dfs.http.policy` to either `HTTPS_ONLY` or `HTTP_AND_HTTPS` in hdfs-site.xml. Note KMS and HttpFS do not respect this parameter. See [Hadoop KMS](../../hadoop-kms/index.html) and [Hadoop HDFS over HTTP - Server Setup](../../hadoop-hdfs-httpfs/ServerSetup.html) for instructions on enabling KMS over HTTPS and HttpFS over HTTPS, respectively.

To enable SSL for web console of YARN daemons, set `yarn.http.policy` to `HTTPS_ONLY` in yarn-site.xml.

To enable SSL for web console of MapReduce JobHistory server, set `mapreduce.jobhistory.http.policy` to `HTTPS_ONLY` in mapred-site.xml.

## Configuration

### Permissions for both HDFS and local fileSystem paths

The following table lists various paths on HDFS and local filesystems (on all nodes) and recommended permissions:

| Filesystem | Path | User:Group | Permissions |
| --- | --- | --- | --- |
| local | `dfs.namenode.name.dir` | hdfs:hadoop | `drwx------` |
| local | `dfs.datanode.data.dir` | hdfs:hadoop | `drwx------` |
| local | `$HADOOP_LOG_DIR` | hdfs:hadoop | `drwxrwxr-x` |
| local | `$YARN_LOG_DIR` | yarn:hadoop | `drwxrwxr-x` |
| local | `yarn.nodemanager.local-dirs` | yarn:hadoop | `drwxr-xr-x` |
| local | `yarn.nodemanager.log-dirs` | yarn:hadoop | `drwxr-xr-x` |
| local | container-executor | root:hadoop | `--Sr-s--*` |
| local | `conf/container-executor.cfg` | root:hadoop | `r-------*` |
| hdfs | `/` | hdfs:hadoop | `drwxr-xr-x` |
| hdfs | `/tmp` | hdfs:hadoop | `drwxrwxrwxt` |
| hdfs | `/user` | hdfs:hadoop | `drwxr-xr-x` |
| hdfs | `yarn.nodemanager.remote-app-log-dir` | yarn:hadoop | `drwxrwxrwxt` |
| hdfs | `mapreduce.jobhistory.intermediate-done-dir` | mapred:hadoop | `drwxrwxrwxt` |
| hdfs | `mapreduce.jobhistory.done-dir` | mapred:hadoop | `drwxr-x---` |

### Common Configurations

In order to turn on RPC authentication in hadoop, set the value of `hadoop.security.authentication` property to `"kerberos"`, and set security related settings listed below appropriately.

The following properties should be in the `core-site.xml` of all the nodes in the cluster.

| Parameter | Value | Notes |
| --- | --- | --- |
| `hadoop.security.authentication` | `kerberos` | `simple` : No authentication. (default)  `kerberos` : Enable authentication by Kerberos. |
| `hadoop.security.authorization` | `true` | Enable [RPC service-level authorization](./ServiceLevelAuth.html). |
| `hadoop.rpc.protection` | `authentication` | `authentication` : authentication only (default); `integrity` : integrity check in addition to authentication; `privacy` : data encryption in addition to integrity |
| `hadoop.security.auth_to_local` | `RULE:`*`exp1`* `RULE:`*`exp2`* *…* `DEFAULT` | The value is string containing new line characters. See [Kerberos documentation](http://web.mit.edu/Kerberos/krb5-latest/doc/admin/conf_files/krb5_conf.html) for the format of *exp*. |
| `hadoop.proxyuser.`*superuser*`.hosts` |  | comma separated hosts from which *superuser* access are allowed to impersonation. `*` means wildcard. |
| `hadoop.proxyuser.`*superuser*`.groups` |  | comma separated groups to which users impersonated by *superuser* belong. `*` means wildcard. |

### NameNode

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.block.access.token.enable` | `true` | Enable HDFS block access tokens for secure operations. |
| `dfs.namenode.kerberos.principal` | `nn/_HOST@REALM.TLD` | Kerberos principal name for the NameNode. |
| `dfs.namenode.keytab.file` | `/etc/security/keytab/nn.service.keytab` | Kerberos keytab file for the NameNode. |
| `dfs.namenode.kerberos.internal.spnego.principal` | `HTTP/_HOST@REALM.TLD` | The server principal used by the NameNode for web UI SPNEGO authentication. The SPNEGO server principal begins with the prefix `HTTP/` by convention. If the value is `'*'`, the web server will attempt to login with every principal specified in the keytab file `dfs.web.authentication.kerberos.keytab`. For most deployments this can be set to `${dfs.web.authentication.kerberos.principal}` i.e use the value of `dfs.web.authentication.kerberos.principal`. |
| `dfs.web.authentication.kerberos.keytab` | `/etc/security/keytab/spnego.service.keytab` | SPNEGO keytab file for the NameNode. In HA clusters this setting is shared with the Journal Nodes. |

The following settings allow configuring SSL access to the NameNode web UI (optional).

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.http.policy` | `HTTP_ONLY` or `HTTPS_ONLY` or `HTTP_AND_HTTPS` | `HTTPS_ONLY` turns off http access. If using SASL to authenticate data transfer protocol instead of running DataNode as root and using privileged ports, then this property must be set to `HTTPS_ONLY` to guarantee authentication of HTTP servers. (See `dfs.data.transfer.protection`.) |
| `dfs.namenode.https-address` | `0.0.0.0:9871` | This parameter is used in non-HA mode and without federation. See [HDFS High Availability](../hadoop-hdfs/HDFSHighAvailabilityWithNFS.html#Deployment) and [HDFS Federation](../hadoop-hdfs/Federation.html#Federation_Configuration) for details. |

### Secondary NameNode

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.namenode.secondary.http-address` | `0.0.0.0:9868` | HTTP web UI address for the Secondary NameNode. |
| `dfs.namenode.secondary.https-address` | `0.0.0.0:9869` | HTTPS web UI address for the Secondary NameNode. |
| `dfs.secondary.namenode.keytab.file` | `/etc/security/keytab/sn.service.keytab` | Kerberos keytab file for the Secondary NameNode. |
| `dfs.secondary.namenode.kerberos.principal` | `sn/_HOST@REALM.TLD` | Kerberos principal name for the Secondary NameNode. |
| `dfs.secondary.namenode.kerberos.internal.spnego.principal` | `HTTP/_HOST@REALM.TLD` | The server principal used by the Secondary NameNode for web UI SPNEGO authentication. The SPNEGO server principal begins with the prefix `HTTP/` by convention. If the value is `'*'`, the web server will attempt to login with every principal specified in the keytab file `dfs.web.authentication.kerberos.keytab`. For most deployments this can be set to `${dfs.web.authentication.kerberos.principal}` i.e use the value of `dfs.web.authentication.kerberos.principal`. |

### JournalNode

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.journalnode.kerberos.principal` | `jn/_HOST@REALM.TLD` | Kerberos principal name for the JournalNode. |
| `dfs.journalnode.keytab.file` | `/etc/security/keytab/jn.service.keytab` | Kerberos keytab file for the JournalNode. |
| `dfs.journalnode.kerberos.internal.spnego.principal` | `HTTP/_HOST@REALM.TLD` | The server principal used by the JournalNode for web UI SPNEGO authentication when Kerberos security is enabled. The SPNEGO server principal begins with the prefix `HTTP/` by convention. If the value is `'*'`, the web server will attempt to login with every principal specified in the keytab file `dfs.web.authentication.kerberos.keytab`. For most deployments this can be set to `${dfs.web.authentication.kerberos.principal}` i.e use the value of `dfs.web.authentication.kerberos.principal`. |
| `dfs.web.authentication.kerberos.keytab` | `/etc/security/keytab/spnego.service.keytab` | SPNEGO keytab file for the JournalNode. In HA clusters this setting is shared with the Name Nodes. |
| `dfs.journalnode.https-address` | `0.0.0.0:8481` | HTTPS web UI address for the JournalNode. |

### DataNode

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.datanode.data.dir.perm` | `700` |  |
| `dfs.datanode.address` | `0.0.0.0:1004` | Secure DataNode must use privileged port in order to assure that the server was started securely. This means that the server must be started via jsvc. Alternatively, this must be set to a non-privileged port if using SASL to authenticate data transfer protocol. (See `dfs.data.transfer.protection`.) |
| `dfs.datanode.http.address` | `0.0.0.0:1006` | Secure DataNode must use privileged port in order to assure that the server was started securely. This means that the server must be started via jsvc. |
| `dfs.datanode.https.address` | `0.0.0.0:9865` | HTTPS web UI address for the Data Node. |
| `dfs.datanode.kerberos.principal` | `dn/_HOST@REALM.TLD` | Kerberos principal name for the DataNode. |
| `dfs.datanode.keytab.file` | `/etc/security/keytab/dn.service.keytab` | Kerberos keytab file for the DataNode. |
| `dfs.encrypt.data.transfer` | `false` | set to `true` when using data encryption |
| `dfs.encrypt.data.transfer.algorithm` |  | optionally set to `3des` or `rc4` when using data encryption to control encryption algorithm |
| `dfs.encrypt.data.transfer.cipher.suites` |  | optionally set to `AES/CTR/NoPadding` to activate AES encryption when using data encryption |
| `dfs.encrypt.data.transfer.cipher.key.bitlength` |  | optionally set to `128`, `192` or `256` to control key bit length when using AES with data encryption |
| `dfs.data.transfer.protection` |  | `authentication` : authentication only; `integrity` : integrity check in addition to authentication; `privacy` : data encryption in addition to integrity This property is unspecified by default. Setting this property enables SASL for authentication of data transfer protocol. If this is enabled, then `dfs.datanode.address` must use a non-privileged port, `dfs.http.policy` must be set to `HTTPS_ONLY` and the `HDFS_DATANODE_SECURE_USER` environment variable must be undefined when starting the DataNode process. |

### WebHDFS

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.web.authentication.kerberos.principal` | `http/_HOST@REALM.TLD` | Kerberos principal name for the WebHDFS. In HA clusters this setting is commonly used by the JournalNodes for securing access to the JournalNode HTTP server with SPNEGO. |
| `dfs.web.authentication.kerberos.keytab` | `/etc/security/keytab/http.service.keytab` | Kerberos keytab file for WebHDFS. In HA clusters this setting is commonly used the JournalNodes for securing access to the JournalNode HTTP server with SPNEGO. |

### ResourceManager

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.resourcemanager.principal` | `rm/_HOST@REALM.TLD` | Kerberos principal name for the ResourceManager. |
| `yarn.resourcemanager.keytab` | `/etc/security/keytab/rm.service.keytab` | Kerberos keytab file for the ResourceManager. |
| `yarn.resourcemanager.webapp.https.address` | `${yarn.resourcemanager.hostname}:8090` | The https adddress of the RM web application for non-HA. In HA clusters, use `yarn.resourcemanager.webapp.https.address.`*rm-id* for each ResourceManager. See [ResourceManager High Availability](../../hadoop-yarn/hadoop-yarn-site/ResourceManagerHA.html#Configurations) for details. |

### NodeManager

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.nodemanager.principal` | `nm/_HOST@REALM.TLD` | Kerberos principal name for the NodeManager. |
| `yarn.nodemanager.keytab` | `/etc/security/keytab/nm.service.keytab` | Kerberos keytab file for the NodeManager. |
| `yarn.nodemanager.container-executor.class` | `org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor` | Use LinuxContainerExecutor. |
| `yarn.nodemanager.linux-container-executor.group` | `hadoop` | Unix group of the NodeManager. |
| `yarn.nodemanager.linux-container-executor.path` | `/path/to/bin/container-executor` | The path to the executable of Linux container executor. |
| `yarn.nodemanager.webapp.https.address` | `0.0.0.0:8044` | The https adddress of the NM web application. |

### Configuration for WebAppProxy

The `WebAppProxy` provides a proxy between the web applications exported by an application and an end user. If security is enabled it will warn users before accessing a potentially unsafe web application. Authentication and authorization using the proxy is handled just like any other privileged web application.

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.web-proxy.address` | `WebAppProxy` host:port for proxy to AM web apps. | `host:port` if this is the same as `yarn.resourcemanager.webapp.address` or it is not defined then the `ResourceManager` will run the proxy otherwise a standalone proxy server will need to be launched. |
| `yarn.web-proxy.keytab` | `/etc/security/keytab/web-app.service.keytab` | Kerberos keytab file for the WebAppProxy. |
| `yarn.web-proxy.principal` | `wap/_HOST@REALM.TLD` | Kerberos principal name for the WebAppProxy. |

### LinuxContainerExecutor

A `ContainerExecutor` used by YARN framework which define how any *container* launched and controlled.

The following are the available in Hadoop YARN:

| ContainerExecutor | Description |
| --- | --- |
| `DefaultContainerExecutor` | The default executor which YARN uses to manage container execution. The container process has the same Unix user as the NodeManager. |
| `LinuxContainerExecutor` | Supported only on GNU/Linux, this executor runs the containers as either the YARN user who submitted the application (when full security is enabled) or as a dedicated user (defaults to nobody) when full security is not enabled. When full security is enabled, this executor requires all user accounts to be created on the cluster nodes where the containers are launched. It uses a `setuid` executable that is included in the Hadoop distribution. The NodeManager uses this executable to launch and kill containers. The setuid executable switches to the user who has submitted the application and launches or kills the containers. For maximum security, this executor sets up restricted permissions and user/group ownership of local files and directories used by the containers such as the shared objects, jars, intermediate files, log files etc. Particularly note that, because of this, except the application owner and NodeManager, no other user can access any of the local files/directories including those localized as part of the distributed cache. |

To build the LinuxContainerExecutor executable run:

```
 $ mvn package -Dcontainer-executor.conf.dir=/etc/hadoop/
```

The path passed in `-Dcontainer-executor.conf.dir` should be the path on the cluster nodes where a configuration file for the setuid executable should be located. The executable should be installed in `$HADOOP_YARN_HOME/bin`.

The executable must have specific permissions: 6050 or `--Sr-s---` permissions user-owned by `root` (super-user) and group-owned by a special group (e.g. `hadoop`) of which the NodeManager Unix user is the group member and no ordinary application user is. If any application user belongs to this special group, security will be compromised. This special group name should be specified for the configuration property `yarn.nodemanager.linux-container-executor.group` in both `conf/yarn-site.xml` and `conf/container-executor.cfg`.

For example, let’s say that the NodeManager is run as user `yarn` who is part of the groups `users` and `hadoop`, any of them being the primary group. Let also be that `users` has both `yarn` and another user (application submitter) `alice` as its members, and `alice` does not belong to `hadoop`. Going by the above description, the setuid/setgid executable should be set 6050 or `--Sr-s---` with user-owner as `yarn` and group-owner as `hadoop` which has `yarn` as its member (and not `users` which has `alice` also as its member besides `yarn`).

The LinuxTaskController requires that paths including and leading up to the directories specified in `yarn.nodemanager.local-dirs` and `yarn.nodemanager.log-dirs` to be set 755 permissions as described above in the table on permissions on directories.

* `conf/container-executor.cfg`

The executable requires a configuration file called `container-executor.cfg` to be present in the configuration directory passed to the mvn target mentioned above.

The configuration file must be owned by the user running NodeManager (user `yarn` in the above example), group-owned by anyone and should have the permissions 0400 or `r--------` .

The executable requires following configuration items to be present in the `conf/container-executor.cfg` file. The items should be mentioned as simple key=value pairs, one per-line:

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.nodemanager.linux-container-executor.group` | `hadoop` | Unix group of the NodeManager. The group owner of the `container-executor` binary should be this group. Should be same as the value with which the NodeManager is configured. This configuration is required for validating the secure access of the `container-executor` binary. |
| `banned.users` | `hdfs,yarn,mapred,bin` | Banned users. |
| `allowed.system.users` | `foo,bar` | Allowed system users. |
| `min.user.id` | `1000` | Prevent other super-users. |

To re-cap, here are the local file-sysytem permissions required for the various paths related to the `LinuxContainerExecutor`:

| Filesystem | Path | User:Group | Permissions |
| --- | --- | --- | --- |
| local | `container-executor` | root:hadoop | `--Sr-s--*` |
| local | `conf/container-executor.cfg` | root:hadoop | `r-------*` |
| local | `yarn.nodemanager.local-dirs` | yarn:hadoop | `drwxr-xr-x` |
| local | `yarn.nodemanager.log-dirs` | yarn:hadoop | `drwxr-xr-x` |

### MapReduce JobHistory Server

| Parameter | Value | Notes |
| --- | --- | --- |
| `mapreduce.jobhistory.address` | MapReduce JobHistory Server `host:port` | Default port is 10020. |
| `mapreduce.jobhistory.keytab` | `/etc/security/keytab/jhs.service.keytab` | Kerberos keytab file for the MapReduce JobHistory Server. |
| `mapreduce.jobhistory.principal` | `jhs/_HOST@REALM.TLD` | Kerberos principal name for the MapReduce JobHistory Server. |

## Multihoming

Multihomed setups where each host has multiple hostnames in DNS (e.g. different hostnames corresponding to public and private network interfaces) may require additional configuration to get Kerberos authentication working. See [HDFS Support for Multihomed Networks](../hadoop-hdfs/HdfsMultihoming.html)

## Troubleshooting

Kerberos is hard to set up —and harder to debug. Common problems are

1. Network and DNS configuration.
2. Kerberos configuration on hosts (`/etc/krb5.conf`).
3. Keytab creation and maintenance.
4. Environment setup: JVM, user login, system clocks, etc.

The fact that the error messages from the JVM are essentially meaningless does not aid in diagnosing and fixing such problems.

Extra debugging information can be enabled for the client and for any service

Set the environment variable `HADOOP_JAAS_DEBUG` to `true`.

```
export HADOOP_JAAS_DEBUG=true
```

Edit the `log4j.properties` file to log Hadoop’s security package at `DEBUG` level.

```
log4j.logger.org.apache.hadoop.security=DEBUG
```

Enable JVM-level debugging by setting some system properties.

```
export HADOOP_OPTS="-Djava.net.preferIPv4Stack=true -Dsun.security.krb5.debug=true -Dsun.security.spnego.debug"
```

## Troubleshooting with `KDiag`

Hadoop has a tool to aid validating setup: `KDiag`

It contains a series of probes for the JVM’s configuration and the environment, dumps out some system files (`/etc/krb5.conf`, `/etc/ntp.conf`), prints out some system state and then attempts to log in to Kerberos as the current user, or a specific principal in a named keytab.

The output of the command can be used for local diagnostics, or forwarded to whoever supports the cluster.

The `KDiag` command has its own entry point; It is invoked by passing `kdiag` to `bin/hadoop` command. Accordingly, it will display the kerberos client state of the command used to invoke it.

```
hadoop kdiag
```

The command returns a status code of 0 for a successful diagnostics run. This does not imply that Kerberos is working —merely that the KDiag command did not identify any problem from its limited set of probes. In particular, as it does not attempt to connect to any remote service, it does not verify that the client is trusted by any service.

If unsuccessful, exit codes are

* -1: the command failed for an unknown reason
* 41: Unauthorized (== HTTP’s 401). KDiag detected a condition which causes Kerberos to not work. Examine the output to identify the issue.

### Usage

```
KDiag: Diagnose Kerberos Problems
  [-D key=value] : Define a configuration option.
  [--jaas] : Require a JAAS file to be defined in java.security.auth.login.config.
  [--keylen <keylen>] : Require a minimum size for encryption keys supported by the JVM. Default value : 256.
  [--keytab <keytab> --principal <principal>] : Login from a keytab as a specific principal.
  [--nofail] : Do not fail on the first problem.
  [--nologin] : Do not attempt to log in.
  [--out <file>] : Write output to a file.
  [--resource <resource>] : Load an XML configuration resource.
  [--secure] : Require the hadoop configuration to be secure.
  [--verifyshortname <principal>]: Verify the short name of the specific principal does not contain '@' or '/'
```

#### `--jaas`: Require a JAAS file to be defined in `java.security.auth.login.config`.

If `--jaas` is set, the Java system property `java.security.auth.login.config` must be set to a JAAS file; this file must exist, be a simple file of non-zero bytes, and readable by the current user. More detailed validation is not performed.

JAAS files are not needed by Hadoop itself, but some services (such as Zookeeper) do require them for secure operation.

#### `--keylen <length>`: Require a minimum size for encryption keys supported by the JVM".

If the JVM does not support this length, the command will fail.

The default value is to 256, as needed for the `AES256` encryption scheme. A JVM without the Java Cryptography Extensions installed does not support such a key length. Kerberos will not work unless configured to use an encryption scheme with a shorter key length.

#### `--keytab <keytab> --principal <principal>`: Log in from a keytab.

Log in from a keytab as the specific principal.

1. The file must contain the specific principal, including any named host. That is, there is no mapping from `_HOST` to the current hostname.
2. KDiag will log out and attempt to log back in again. This catches JVM compatibility problems which have existed in the past. (Hadoop’s Kerberos support requires use of/introspection into JVM-specific classes).

#### `--nofail` : Do not fail on the first problem

KDiag will make a best-effort attempt to diagnose all Kerberos problems, rather than stop at the first one.

This is somewhat limited; checks are made in the order which problems surface (e.g keylength is checked first), so an early failure can trigger many more problems. But it does produce a more detailed report.

#### `--nologin`: Do not attempt to log in.

Skip trying to log in. This takes precedence over the `--keytab` option, and also disables trying to log in to kerberos as the current kinited user.

This is useful when the KDiag command is being invoked within an application, as it does not set up Hadoop’s static security state —merely check for some basic Kerberos preconditions.

#### `--out outfile`: Write output to file.

```
hadoop kdiag --out out.txt
```

Much of the diagnostics information comes from the JRE (to `stderr`) and from Log4j (to `stdout`). To get all the output, it is best to redirect both these output streams to the same file, and omit the `--out` option.

```
hadoop kdiag --keytab zk.service.keytab --principal zookeeper/devix.example.org@REALM > out.txt 2>&1
```

Even there, the output of the two streams, emitted across multiple threads, can be a bit confusing. It will get easier with practise. Looking at the thread name in the Log4j output to distinguish background threads from the main thread helps at the hadoop level, but doesn’t assist in JVM-level logging.

#### `--resource <resource>` : XML configuration resource to load.

To load XML configuration files, this option can be used. As by default, the `core-default` and `core-site` XML resources are only loaded. This will help, when additional configuration files has any Kerberos related configurations.

```
hadoop kdiag --resource hbase-default.xml --resource hbase-site.xml
```

For extra logging during the operation, set the logging and `HADOOP_JAAS_DEBUG` environment variable to the values listed in “Troubleshooting”. The JVM options are automatically set in KDiag.

#### `--secure`: Fail if the command is not executed on a secure cluster.

That is: if the authentication mechanism of the cluster is explicitly or implicitly set to “simple”:

```
<property>
  <name>hadoop.security.authentication</name>
  <value>simple</value>
</property>
```

Needless to say, an application so configured cannot talk to a secure Hadoop cluster.

#### `--verifyshortname <principal>`: validate the short name of a principal

This verifies that the short name of a principal contains neither the `"@"` nor `"/"` characters.

### Example

```
hadoop kdiag \
  --nofail \
  --resource hdfs-site.xml --resource yarn-site.xml \
  --keylen 1024 \
  --keytab zk.service.keytab --principal zookeeper/devix.example.org@REALM
```

This attempts to perform all diagnostics without failing early, load in the HDFS and YARN XML resources, require a minimum key length of 1024 bytes, and log in as the principal `zookeeper/devix.example.org@REALM`, whose key must be in the keytab `zk.service.keytab`

## References

1. O’Malley O et al. [Hadoop Security Design](https://issues.apache.org/jira/secure/attachment/12428537/security-design.pdf)
2. O’Malley O, [Hadoop Security Architecture](http://www.slideshare.net/oom65/hadoop-security-architecture)
3. [Troubleshooting Kerberos on Java 7](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
4. [Troubleshooting Kerberos on Java 8](http://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
5. [Java 7 Kerberos Requirements](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
6. [Java 8 Kerberos Requirements](http://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
7. Loughran S., [Hadoop and Kerberos: The Madness beyond the Gate](https://steveloughran.gitbooks.io/kerberos_and_hadoop/content/)

---
# Hadoop: CLI MiniCluster.

* [Purpose](#Purpose)
* [Hadoop Tarball](#Hadoop_Tarball)
* [Running the MiniCluster](#Running_the_MiniCluster)

## Purpose

Using the CLI MiniCluster, users can simply start and stop a single-node Hadoop cluster with a single command, and without the need to set any environment variables or manage configuration files. The CLI MiniCluster starts both a `YARN`/`MapReduce` & `HDFS` clusters.

This is useful for cases where users want to quickly experiment with a real Hadoop cluster or test non-Java programs that rely on significant Hadoop functionality.

## Hadoop Tarball

You should be able to obtain the Hadoop tarball from the release. Also, you can directly create a tarball from the source:

```
$ mvn clean install -DskipTests
$ mvn package -Pdist -Dtar -DskipTests -Dmaven.javadoc.skip
```

The tarball should be available in `hadoop-dist/target/` directory.

## Running the MiniCluster

From inside the root directory of the extracted tarball, you can start the CLI MiniCluster using the following command:

```
$ bin/mapred minicluster -format
```

The format option is required when running the minicluster for the first time, from next time -format option isn’t required.

There are a number of command line arguments that the users can use to control which services to start, and to pass other configuration properties. The available command line arguments:

```
$ -D <property=value>    Options to pass into configuration object
$ -datanodes <arg>       How many datanodes to start (default 1)
$ -format                Format the DFS (default false)
$ -help                  Prints option help.
$ -jhsport <arg>         JobHistoryServer port (default 0--we choose)
$ -namenode <arg>        URL of the namenode (default is either the DFS
$                        cluster or a temporary dir)
$ -nnport <arg>          NameNode port (default 0--we choose)
$ -nnhttpport <arg>      NameNode HTTP port (default 0--we choose)
$ -nodemanagers <arg>    How many nodemanagers to start (default 1)
$ -nodfs                 Don't start a mini DFS cluster
$ -nomr                  Don't start a mini MR cluster
$ -rmport <arg>          ResourceManager port (default 0--we choose)
$ -writeConfig <path>    Save configuration to this XML file.
$ -writeDetails <path>   Write basic information to this JSON file.
```

To display this full list of available arguments, the user can pass the `-help` argument to the above command.

---
* Public/Stable/Replaceable
  * [hadoop\_add\_array\_param](#hadoop_add_array_param)
  * [hadoop\_add\_classpath](#hadoop_add_classpath)
  * [hadoop\_add\_client\_opts](#hadoop_add_client_opts)
  * [hadoop\_add\_colonpath](#hadoop_add_colonpath)
  * [hadoop\_add\_javalibpath](#hadoop_add_javalibpath)
  * [hadoop\_add\_ldlibpath](#hadoop_add_ldlibpath)
  * [hadoop\_add\_param](#hadoop_add_param)
  * [hadoop\_add\_profile](#hadoop_add_profile)
  * [hadoop\_array\_contains](#hadoop_array_contains)
  * [hadoop\_build\_custom\_subcmd\_var](#hadoop_build_custom_subcmd_var)
  * [hadoop\_deprecate\_envvar](#hadoop_deprecate_envvar)
  * [hadoop\_detect\_priv\_subcmd](#hadoop_detect_priv_sub.html)
  * [hadoop\_java\_exec](#hadoop_java_exec)
  * [hadoop\_java\_setup](#hadoop_java_setup)
  * [hadoop\_mkdir](#hadoop_mkdir)
  * [hadoop\_need\_reexec](#hadoop_need_reexec)
  * [hadoop\_os\_tricks](#hadoop_os_tricks)
  * [hadoop\_sort\_array](#hadoop_sort_array)
  * [hadoop\_status\_daemon](#hadoop_status_daemon)
  * [hadoop\_stop\_daemon](#hadoop_stop_daemon)
  * [hadoop\_stop\_secure\_daemon](#hadoop_stop_secure_daemon)
  * [hadoop\_subcommand\_secure\_opts](#hadoop_subcommand_secure_opts)
  * [hadoop\_translate\_cygwin\_path](#hadoop_translate_cygwin_path)
  * [hadoop\_using\_envvar](#hadoop_using_envvar)
  * [hadoop\_validate\_classname](#hadoop_validate_classname)
  * [hadoop\_verify\_confdir](#hadoop_verify_confdir)
  * [hadoop\_verify\_user\_perm](#hadoop_verify_user_perm)
  * [hadoop\_verify\_user\_resolves](#hadoop_verify_user_resolves)
* Public/Stable/Not Replaceable
  * [hadoop\_abs](#hadoop_abs)
  * [hadoop\_add\_entry](#hadoop_add_entry)
  * [hadoop\_debug](#hadoop_debug)
  * [hadoop\_delete\_entry](#hadoop_delete_entry)
  * [hadoop\_error](#hadoop_error)
  * [hadoop\_exit\_with\_usage](#hadoop_exit_with_usage)
  * [hadoop\_populate\_workers\_file](#hadoop_populate_workers_file)
  * [hadoop\_rotate\_log](#hadoop_rotate_log)
  * [hadoop\_verify\_entry](#hadoop_verify_entry)
* Public/Evolving/Replaceable
  * [hadoop\_subcommand\_opts](#hadoop_subcommand_opts)
* Private/Evolving/Replaceable
  * [hadoop\_actual\_ssh](#hadoop_actual_ssh)
  * [hadoop\_add\_common\_to\_classpath](#hadoop_add_common_to_classpath)
  * [hadoop\_add\_to\_classpath\_tools](#hadoop_add_to_classpath_tools)
  * [hadoop\_add\_to\_classpath\_userpath](#hadoop_add_to_classpath_userpath)
  * [hadoop\_common\_worker\_mode\_execute](#hadoop_common_worker_mode_execute)
  * [hadoop\_connect\_to\_hosts](#hadoop_connect_to_hosts)
  * [hadoop\_connect\_to\_hosts\_without\_pdsh](#hadoop_connect_to_hosts_without_pdsh)
  * [hadoop\_daemon\_handler](#hadoop_daemon_handler)
  * [hadoop\_do\_classpath\_subcommand](#hadoop_do_classpath_subcommand)
  * [hadoop\_exec\_hadooprc](#hadoop_exec_hadooprc)
  * [hadoop\_exec\_user\_hadoopenv](#hadoop_exec_user_hadoopenv)
  * [hadoop\_finalize](#hadoop_finalize)
  * [hadoop\_finalize\_classpath](#hadoop_finalize_classpath)
  * [hadoop\_finalize\_hadoop\_heap](#hadoop_finalize_hadoop_heap)
  * [hadoop\_finalize\_hadoop\_opts](#hadoop_finalize_hadoop_opts)
  * [hadoop\_finalize\_jpms\_opts](#hadoop_finalize_jpms_opts)
  * [hadoop\_finalize\_libpaths](#hadoop_finalize_libpaths)
  * [hadoop\_generic\_java\_subcmd\_handler](#hadoop_generic_java_subcmd_handler)
  * [hadoop\_import\_shellprofiles](#hadoop_import_shellprofiles)
  * [hadoop\_parse\_args](#hadoop_parse_args)
  * [hadoop\_privilege\_check](#hadoop_privilege_check)
  * [hadoop\_secure\_daemon\_handler](#hadoop_secure_daemon_handler)
  * [hadoop\_setup\_secure\_service](#hadoop_setup_secure_service)
  * [hadoop\_shellprofiles\_classpath](#hadoop_shellprofiles_classpath)
  * [hadoop\_shellprofiles\_finalize](#hadoop_shellprofiles_finalize)
  * [hadoop\_shellprofiles\_init](#hadoop_shellprofiles_init)
  * [hadoop\_shellprofiles\_nativelib](#hadoop_shellprofiles_nativelib)
  * [hadoop\_start\_daemon](#hadoop_start_daemon)
  * [hadoop\_start\_daemon\_wrapper](#hadoop_start_daemon_wrapper)
  * [hadoop\_start\_secure\_daemon](#hadoop_start_secure_daemon)
  * [hadoop\_start\_secure\_daemon\_wrapper](#hadoop_start_secure_daemon_wrapper)
  * [hadoop\_sudo](#hadoop_sudo)
  * [hadoop\_verify\_logdir](#hadoop_verify_logdir)
  * [hadoop\_verify\_piddir](#hadoop_verify_piddir)
  * [hadoop\_verify\_secure\_prereq](#hadoop_verify_secure_prereq)

---

## Public/Stable/Replaceable

### `hadoop_add_array_param`

* Synopsis

```
hadoop_add_array_param envvar appendstring
```

* Description

Add the `appendstring` if `checkstring` is not present in the given array

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_add_classpath`

* Synopsis

```
hadoop_add_classpath object [before|after]
```

* Description

Add a file system object (directory, file, wildcard, …) to the classpath. Optionally provide a hint as to where in the classpath it should go.

* Returns

0 = success (added or duplicate) 1 = failure (doesn’t exist or some other reason)

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_add_client_opts`

* Synopsis

```
hadoop_add_client_opts
```

* Description

Adds the HADOOP\_CLIENT\_OPTS variable to HADOOP\_OPTS if HADOOP\_SUBCMD\_SUPPORTDAEMONIZATION is false

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_add_colonpath`

* Synopsis

```
hadoop_add_colonpath envvar object [before|after]
```

* Description

Add a file system object (directory, file, wildcard, …) to the colonpath. Optionally provide a hint as to where in the colonpath it should go. Prior to adding, objects are checked for duplication and check for existence. Many other functions use this function as their base implementation including `hadoop_add_javalibpath` and `hadoop_add_ldlibpath`.

* Returns

0 = success (added or duplicate) 1 = failure (doesn’t exist or some other reason)

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_add_javalibpath`

* Synopsis

```
hadoop_add_javalibpath object [before|after]
```

* Description

Add a file system object (directory, file, wildcard, …) to the Java JNI path. Optionally provide a hint as to where in the Java JNI path it should go.

* Returns

0 = success (added or duplicate) 1 = failure (doesn’t exist or some other reason)

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_add_ldlibpath`

* Synopsis

```
hadoop_add_ldlibpath object [before|after]
```

* Description

Add a file system object (directory, file, wildcard, …) to the LD\_LIBRARY\_PATH. Optionally provide a hint as to where in the LD\_LIBRARY\_PATH it should go.

* Returns

0 = success (added or duplicate) 1 = failure (doesn’t exist or some other reason)

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_add_param`

* Synopsis

```
hadoop_add_param envvar checkstring appendstring
```

* Description

Append the `appendstring` if `checkstring` is not present in the given `envvar`

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_add_profile`

* Synopsis

```
hadoop_add_profile shellprofile
```

* Description

Register the given `shellprofile` to the Hadoop shell subsystem

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_array_contains`

* Synopsis

```
hadoop_array_contains element array
```

* Description

Check if an array has a given value

* Returns

## @returns 0 = yes

## @returns 1 = no

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_build_custom_subcmd_var`

* Synopsis

```
hadoop_build_custom_subcmd_var command subcommand customid
```

* Description

Build custom subcommand var

* Returns

string

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_deprecate_envvar`

* Synopsis

```
hadoop_deprecate_envvar oldvar newvar
```

* Description

Replace `oldvar` with `newvar` if `oldvar` exists.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_detect_priv_subcmd`

* Synopsis

```
hadoop_detect_priv_subcmd command subcommand
```

* Description

autodetect whether this is a priv subcmd by whether or not a priv user var exists and if HADOOP\_SECURE\_CLASSNAME is defined

* Returns

1 = not priv 0 = priv

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_java_exec`

* Synopsis

```
hadoop_java_exec command class [options]
```

* Description

Execute the Java `class`, passing along any `options`. Additionally, set the Java property -Dproc\_`command`.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_java_setup`

* Synopsis

```
hadoop_java_setup
```

* Description

Configure/verify ${JAVA\_HOME}

* Returns

may exit on failure conditions

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_mkdir`

* Synopsis

```
hadoop_mkdir dir
```

* Description

Create the directory ‘dir’.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_need_reexec`

* Synopsis

```
hadoop_need_reexec subcommand
```

* Description

Verify that ${USER} is allowed to execute the given subcommand.

* Returns

1 on no re-exec needed 0 on need to re-exec

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_os_tricks`

* Synopsis

```
hadoop_os_tricks
```

* Description

Routine to configure any OS-specific settings.

* Returns

may exit on failure conditions

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_sort_array`

* Synopsis

```
hadoop_sort_array arrayvar
```

* Description

Sort an array (must not contain regexps) present in the given array

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_status_daemon`

* Synopsis

```
hadoop_status_daemon pidfile
```

* Description

Determine the status of the daemon referenced by `pidfile`

* Returns

(mostly) LSB 4.1.0 compatible status

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_stop_daemon`

* Synopsis

```
hadoop_stop_daemon command pidfile
```

* Description

Stop the non-privileged `command` daemon with that that is running at `pidfile`.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_stop_secure_daemon`

* Synopsis

```
hadoop_stop_secure_daemon command daemonpidfile wrapperpidfile
```

* Description

Stop the privileged `command` daemon with that that is running at `daemonpidfile` and launched with the wrapper at `wrapperpidfile`.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_subcommand_secure_opts`

* Synopsis

```
hadoop_subcommand_secure_opts program subcommand
```

* Description

Add custom (program)\_(command)\_SECURE\_EXTRA\_OPTS to HADOOP\_OPTS. This *does not* handle the pre-3.x deprecated cases

* Returns

will exit on failure conditions

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_translate_cygwin_path`

* Synopsis

```
hadoop_translate_cygwin_path varnameref [true]
```

* Description

Converts the contents of the variable name `varnameref` into the equivalent Windows path. If the second parameter is true, then `varnameref` is treated as though it was a path list.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_using_envvar`

* Synopsis

```
hadoop_using_envvar var
```

* Description

Declare `var` being used and print its value.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_validate_classname`

* Synopsis

```
hadoop_validate_classname classname
```

* Description

Verify that a shell command was passed a valid class name

* Returns

0 = success 1 = failure w/user message

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_verify_confdir`

* Synopsis

```
hadoop_verify_confdir
```

* Description

Validate ${HADOOP\_CONF\_DIR}

* Returns

will exit on failure conditions

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_verify_user_perm`

* Synopsis

```
hadoop_verify_user_perm command subcommand
```

* Description

Verify that ${USER} is allowed to execute the given subcommand.

* Returns

return 0 on success exit 1 on failure

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

### `hadoop_verify_user_resolves`

* Synopsis

```
hadoop_verify_user_resolves userstring
```

* Description

Verify that username in a var converts to user id

* Returns

0 for success 1 for failure

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | True |

## Public/Stable/Not Replaceable

### `hadoop_abs`

* Synopsis

```
hadoop_abs fsobj
```

* Description

Given a filename or dir, return the absolute version of it This works as an alternative to readlink, which isn’t portable.

* Returns

0 success 1 failure stdout abspath

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_add_entry`

* Synopsis

```
hadoop_add_entry
```

* Description

Given variable $1 add $2 to it

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_debug`

* Synopsis

```
hadoop_debug string
```

* Description

Print a message to stderr if –debug is turned on

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_delete_entry`

* Synopsis

```
hadoop_delete_entry
```

* Description

Given variable $1 delete $2 from it

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_error`

* Synopsis

```
hadoop_error string
```

* Description

Print a message to stderr

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_exit_with_usage`

* Synopsis

```
hadoop_exit_with_usage exitcode
```

* Description

Print usage information and exit with the passed `exitcode`

* Returns

This function will always exit.

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_populate_workers_file`

* Synopsis

```
hadoop_populate_workers_file filename
```

* Description

Set the worker support information to the contents of `filename`

* Returns

will exit if file does not exist

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_rotate_log`

* Synopsis

```
hadoop_rotate_log filename [number]
```

* Description

Rotates the given `file` until `number` of files exist.

* Returns

$? will contain last mv’s return value

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

### `hadoop_verify_entry`

* Synopsis

```
hadoop_verify_entry
```

* Description

Given variable $1 determine if $2 is in it

* Returns

0 = yes, 1 = no

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Stable |
| Replaceable | False |

## Public/Evolving/Replaceable

### `hadoop_subcommand_opts`

* Synopsis

```
hadoop_subcommand_opts program subcommand
```

* Description

Add custom (program)\_(command)\_OPTS to HADOOP\_OPTS. Also handles the deprecated cases from pre-3.x.

* Returns

will exit on failure conditions

| Classification | Level |
| --- | --- |
| Audience | Public |
| Stability | Evolving |
| Replaceable | True |

## Private/Evolving/Replaceable

### `hadoop_actual_ssh`

* Synopsis

```
hadoop_actual_ssh hostname command [...]
```

* Description

Via ssh, log into `hostname` and run `command`

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_add_common_to_classpath`

* Synopsis

```
hadoop_add_common_to_classpath
```

* Description

Add the common/core Hadoop components to the environment

* Returns

## @returns 1 on failure, may exit

## @returns 0 on success

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_add_to_classpath_tools`

* Synopsis

```
hadoop_add_to_classpath_tools module
```

* Description

Run libexec/tools/module.sh to add to the classpath environment

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_add_to_classpath_userpath`

* Synopsis

```
hadoop_add_to_classpath_userpath
```

* Description

Add the user’s custom classpath settings to the environment

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_common_worker_mode_execute`

* Synopsis

```
hadoop_common_worker_mode_execute commandarray
```

* Description

Utility routine to handle –workers mode

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_connect_to_hosts`

* Synopsis

```
hadoop_connect_to_hosts command [...]
```

* Description

Connect to ${HADOOP\_WORKERS} or ${HADOOP\_WORKER\_NAMES} and execute command.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_connect_to_hosts_without_pdsh`

* Synopsis

```
hadoop_connect_to_hosts_without_pdsh command [...]
```

* Description

Connect to ${HADOOP\_WORKER\_NAMES} and execute command under the environment which does not support pdsh.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_daemon_handler`

* Synopsis

```
hadoop_daemon_handler [start|stop|status|default] command class daemonpidfile daemonoutfile [options]
```

* Description

Manage a non-privileged daemon.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_do_classpath_subcommand`

* Synopsis

```
hadoop_do_classpath_subcommand [parameters]
```

* Description

Perform the ‘hadoop classpath’, etc subcommand with the given parameters

* Returns

will print & exit with no params

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_exec_hadooprc`

* Synopsis

```
hadoop_exec_hadooprc
```

* Description

Read the user’s settings. This provides for users to run Hadoop Shell API after system bootstrap

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_exec_user_hadoopenv`

* Synopsis

```
hadoop_exec_user_hadoopenv
```

* Description

Read the user’s settings. This provides for users to override and/or append hadoop-env.sh. It is not meant as a complete system override.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_finalize`

* Synopsis

```
hadoop_finalize
```

* Description

Finish all the remaining environment settings prior to executing Java. This is a wrapper that calls the other `finalize` routines.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_finalize_classpath`

* Synopsis

```
hadoop_finalize_classpath
```

* Description

Finish Java classpath prior to execution

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_finalize_hadoop_heap`

* Synopsis

```
hadoop_finalize_hadoop_heap
```

* Description

Finish Java heap parameters prior to execution

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_finalize_hadoop_opts`

* Synopsis

```
hadoop_finalize_hadoop_opts
```

* Description

Finish configuring Hadoop specific system properties prior to executing Java

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_finalize_jpms_opts`

* Synopsis

```
hadoop_finalize_jpms_opts
```

* Description

Finish configuring JPMS that enforced for JDK 17 and higher prior to executing Java keep this list sync with hadoop-project/pom.xml extraJavaTestArgs

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_finalize_libpaths`

* Synopsis

```
hadoop_finalize_libpaths
```

* Description

Finish Java JNI paths prior to execution

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_generic_java_subcmd_handler`

* Synopsis

```
hadoop_generic_java_subcmd_handler
```

* Description

Handle subcommands from main program entries

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_import_shellprofiles`

* Synopsis

```
hadoop_import_shellprofiles
```

* Description

Import shellprofile.d content

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_parse_args`

* Synopsis

```
hadoop_parse_args [parameters, typically "$@"]
```

* Description

generic shell script option parser. sets HADOOP\_PARSE\_COUNTER to set number the caller should shift

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_privilege_check`

* Synopsis

```
hadoop_privilege_check
```

* Description

Check if we are running with priv by default, this implementation looks for EUID=0. For OSes that have true priv separation, this should be something more complex

* Returns

1 = no priv 0 = priv

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_secure_daemon_handler`

* Synopsis

```
hadoop_secure_daemon_handler [start|stop|status|default] command class daemonpidfile daemonoutfile wrapperpidfile wrapperoutfile wrappererrfile [options]
```

* Description

Manage a privileged daemon.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_setup_secure_service`

* Synopsis

```
hadoop_setup_secure_service
```

* Description
* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_shellprofiles_classpath`

* Synopsis

```
hadoop_shellprofiles_classpath
```

* Description

Apply the shell profile classpath additions

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_shellprofiles_finalize`

* Synopsis

```
hadoop_shellprofiles_finalize
```

* Description

Apply the shell profile final configuration

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_shellprofiles_init`

* Synopsis

```
hadoop_shellprofiles_init
```

* Description

Initialize the registered shell profiles

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_shellprofiles_nativelib`

* Synopsis

```
hadoop_shellprofiles_nativelib
```

* Description

Apply the shell profile native library additions

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_start_daemon`

* Synopsis

```
hadoop_start_daemon command class pidfile [options]
```

* Description

Start a non-privileged daemon in the foreground.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_start_daemon_wrapper`

* Synopsis

```
hadoop_start_daemon_wrapper command class pidfile outfile [options]
```

* Description

Start a non-privileged daemon in the background.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_start_secure_daemon`

* Synopsis

```
hadoop_start_secure_daemon command class daemonpidfile daemonoutfile daemonerrfile wrapperpidfile [options]
```

* Description

Start a privileged daemon in the foreground.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_start_secure_daemon_wrapper`

* Synopsis

```
hadoop_start_secure_daemon_wrapper command class daemonpidfile daemonoutfile wrapperpidfile warpperoutfile daemonerrfile [options]
```

* Description

Start a privileged daemon in the background.

* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_sudo`

* Synopsis

```
hadoop_sudo user commandstring
```

* Description

Execute a command via sudo when running as root if the given user is found or exit with failure if not. otherwise just run it. (This is intended to be used by the start-*/stop-* scripts.)

* Returns

exitstatus

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_verify_logdir`

* Synopsis

```
hadoop_verify_logdir
```

* Description
* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_verify_piddir`

* Synopsis

```
hadoop_verify_piddir
```

* Description
* Returns

Nothing

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

### `hadoop_verify_secure_prereq`

* Synopsis

```
hadoop_verify_secure_prereq
```

* Description

Verify that prerequisites have been met prior to excuting a privileged program.

* Returns

This routine may exit.

| Classification | Level |
| --- | --- |
| Audience | Private |
| Stability | Evolving |
| Replaceable | True |

---
* [python Example](#python_Example)
* [bash Example](#bash_Example)

# Rack Awareness

Hadoop components are rack-aware. For example, HDFS block placement will use rack awareness for fault tolerance by placing one block replica on a different rack. This provides data availability in the event of a network switch failure or partition within the cluster.

Hadoop master daemons obtain the rack id of the cluster workers by invoking either an external script or java class as specified by configuration files. Using either the java class or external script for topology, output must adhere to the java **org.apache.hadoop.net.DNSToSwitchMapping** interface. The interface expects a one-to-one correspondence to be maintained and the topology information in the format of ‘/myrack/myhost’, where ‘/’ is the topology delimiter, ‘myrack’ is the rack identifier, and ‘myhost’ is the individual host. Assuming a single /24 subnet per rack, one could use the format of ‘/192.168.100.0/192.168.100.5’ as a unique rack-host topology mapping.

To use the java class for topology mapping, the class name is specified by the **net.topology.node.switch.mapping.impl** parameter in the configuration file. An example, NetworkTopology.java, is included with the hadoop distribution and can be customized by the Hadoop administrator. Using a Java class instead of an external script has a performance benefit in that Hadoop doesn’t need to fork an external process when a new worker node registers itself.

If implementing an external script, it will be specified with the **net.topology.script.file.name** parameter in the configuration files. Unlike the java class, the external topology script is not included with the Hadoop distribution and is provided by the administrator. Hadoop will send multiple IP addresses to ARGV when forking the topology script. The number of IP addresses sent to the topology script is controlled with **net.topology.script.number.args** and defaults to 100. If **net.topology.script.number.args** was changed to 1, a topology script would get forked for each IP submitted by DataNodes and/or NodeManagers.

If **net.topology.script.file.name** or **net.topology.node.switch.mapping.impl** is not set, the rack id ‘/default-rack’ is returned for any passed IP address. While this behavior appears desirable, it can cause issues with HDFS block replication as default behavior is to write one replicated block off rack and is unable to do so as there is only a single rack named ‘/default-rack’.

## python Example

```
#!/usr/bin/python3
# this script makes assumptions about the physical environment.
#  1) each rack is its own layer 3 network with a /24 subnet, which
# could be typical where each rack has its own
#     switch with uplinks to a central core router.
#
#             +-----------+
#             |core router|
#             +-----------+
#            /             \
#   +-----------+        +-----------+
#   |rack switch|        |rack switch|
#   +-----------+        +-----------+
#   | data node |        | data node |
#   +-----------+        +-----------+
#   | data node |        | data node |
#   +-----------+        +-----------+
#
# 2) topology script gets list of IP's as input, calculates network address, and prints '/network_address/ip'.

import netaddr
import sys
sys.argv.pop(0)                                                  # discard name of topology script from argv list as we just want IP addresses

netmask = '255.255.255.0'                                        # set netmask to what's being used in your environment.  The example uses a /24

for ip in sys.argv:                                              # loop over list of datanode IP's
    address = '{0}/{1}'.format(ip, netmask)                      # format address string so it looks like 'ip/netmask' to make netaddr work
    try:
        network_address = netaddr.IPNetwork(address).network     # calculate and print network address
        print("/{0}".format(network_address))
    except:
        print("/rack-unknown")                                   # print catch-all value if unable to calculate network address
```

## bash Example

```
#!/usr/bin/env bash
# Here's a bash example to show just how simple these scripts can be
# Assuming we have flat network with everything on a single switch, we can fake a rack topology.
# This could occur in a lab environment where we have limited nodes,like 2-8 physical machines on a unmanaged switch.
# This may also apply to multiple virtual machines running on the same physical hardware.
# The number of machines isn't important, but that we are trying to fake a network topology when there isn't one.
#
#       +----------+    +--------+
#       |jobtracker|    |datanode|
#       +----------+    +--------+
#              \        /
#  +--------+  +--------+  +--------+
#  |datanode|--| switch |--|datanode|
#  +--------+  +--------+  +--------+
#              /        \
#       +--------+    +--------+
#       |datanode|    |namenode|
#       +--------+    +--------+
#
# With this network topology, we are treating each host as a rack.  This is being done by taking the last octet
# in the datanode's IP and prepending it with the word '/rack-'.  The advantage for doing this is so HDFS
# can create its 'off-rack' block copy.
# 1) 'echo $@' will echo all ARGV values to xargs.
# 2) 'xargs' will enforce that we print a single argv value per line
# 3) 'awk' will split fields on dots and append the last field to the string '/rack-'. If awk
#    fails to split on four dots, it will still print '/rack-' last field value

echo $@ | xargs -n 1 | awk -F '.' '{print "/rack-"$NF}'
```

---
# Apache Hadoop Compatibility

* [Purpose](#Purpose)
  * [Target Audience](#Target_Audience)
  * [Structure](#Structure)
  * [Notational Conventions](#Notational_Conventions)
* [Deprecation](#Deprecation)
  * [Policy](#Policy)
* [Compatibility types](#Compatibility_types)
  * [Java API](#Java_API)
    * [Use Cases](#Use_Cases)
    * [Policy](#Policy)
    * [Semantic compatibility](#Semantic_compatibility)
    * [Java Binary compatibility for end-user applications i.e. Apache Hadoop ABI](#Java_Binary_compatibility_for_end-user_applications_i.e._Apache_Hadoop_ABI)
  * [Native Dependencies](#Native_Dependencies)
    * [Policy](#Policy)
  * [Wire Protocols](#Wire_Protocols)
    * [Protocol Dependencies](#Protocol_Dependencies)
    * [Transports](#Transports)
    * [Policy](#Policy)
  * [REST APIs](#REST_APIs)
    * [Policy](#Policy)
  * [Log Output](#Log_Output)
    * [Policy](#Policy)
  * [Audit Log Output](#Audit_Log_Output)
    * [Policy](#Policy)
  * [Metrics/JMX](#Metrics.2FJMX)
    * [Policy](#Policy)
  * [File formats & Metadata](#File_formats_.26_Metadata)
    * [User-level file formats](#User-level_file_formats)
    * [System-internal data schemas](#System-internal_data_schemas)
  * [Command Line Interface (CLI)](#Command_Line_Interface_.28CLI.29)
    * [Policy](#Policy)
  * [Web UI](#Web_UI)
    * [Policy](#Policy)
  * [Functional Compatibility](#Functional_Compatibility)
    * [Policy](#Policy)
  * [Hadoop Configuration Files](#Hadoop_Configuration_Files)
    * [Policy](#Policy)
  * [Log4j Configuration Files](#Log4j_Configuration_Files)
    * [Policy](#Policy)
  * [Directory Structure](#Directory_Structure)
    * [Policy](#Policy)
  * [Java Classpath](#Java_Classpath)
    * [Policy](#Policy)
  * [Environment variables](#Environment_variables)
    * [Policy](#Policy)
  * [Build artifacts](#Build_artifacts)
    * [Policy](#Policy)
  * [Hardware/Software Requirements](#Hardware.2FSoftware_Requirements)
    * [Policies](#Policies)
* [References](#References)

## Purpose

This document captures the compatibility goals of the Apache Hadoop project. The different types of compatibility between Hadoop releases that affect Hadoop developers, downstream projects, and end-users are enumerated. For each type of compatibility this document will:

* describe the impact on downstream projects or end-users
* where applicable, call out the policy adopted by the Hadoop developers when incompatible changes are permitted.

All Hadoop interfaces are classified according to the intended audience and stability in order to maintain compatibility with previous releases. See the [Hadoop Interface Taxonomy](./InterfaceClassification.html) for details about the classifications.

### Target Audience

This document is intended for consumption by the Hadoop developer community. This document describes the lens through which changes to the Hadoop project should be viewed. In order for end users and third party developers to have confidence about cross-release compatibility, the developer community must ensure that development efforts adhere to these policies. It is the responsibility of the project committers to validate that all changes either maintain compatibility or are explicitly marked as incompatible.

Within a component Hadoop developers are free to use Private and Limited Private APIs, but when using components from a different module Hadoop developers should follow the same guidelines as third-party developers: do not use Private or Limited Private (unless explicitly allowed) interfaces and prefer instead Stable interfaces to Evolving or Unstable interfaces where possible. Where not possible, the preferred solution is to expand the audience of the API rather than introducing or perpetuating an exception to these compatibility guidelines. When working within a Maven module Hadoop developers should observe where possible the same level of restraint with regard to using components located in other Maven modules.

Above all, Hadoop developers must be mindful of the impact of their changes. Stable interfaces must not change between major releases. Evolving interfaces must not change between minor releases. New classes and components must be labeled appropriately for audience and stability. See the [Hadoop Interface Taxonomy](./InterfaceClassification.html) for details about when the various labels are appropriate. As a general rule, all new interfaces and APIs should have the most limited labels (e.g. Private Unstable) that will not inhibit the intent of the interface or API.

### Structure

This document is arranged in sections according to the various compatibility concerns. Within each section an introductory text explains what compatibility means in that section, why it’s important, and what the intent to support compatibility is. The subsequent “Policy” section then sets forth in specific terms what the governing policy is.

### Notational Conventions

The key words “MUST” “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

## Deprecation

The Java API provides a @Deprecated annotation to mark an API element as flagged for removal. The standard meaning of the annotation is that the API element should not be used and may be removed in a later version.

In all cases removing an element from an API is an incompatible change. The stability of the element SHALL determine when such a change is permissible. A [Stable](./InterfaceClassification.html#Stable) element MUST be marked as deprecated for a full major release before it can be removed and SHALL NOT be removed in a minor or maintenance release. An [Evolving](./InterfaceClassification.html#Evolving) element MUST be marked as deprecated for a full minor release before it can be removed and SHALL NOT be removed during a maintenance release. An [Unstable](./InterfaceClassification.html#Unstable) element MAY be removed at any time. When possible an [Unstable](./InterfaceClassification.html#Unstable) element SHOULD be marked as deprecated for at least one release before being removed. For example, if a method is marked as deprecated in Hadoop 2.8, it cannot be removed until Hadoop 4.0.

### Policy

[Stable](./InterfaceClassification.html#Stable) API elements MUST NOT be removed until they have been marked as deprecated (through the @Deprecated annotation or other appropriate documentation) for a full major release. In the case that an API element was introduced as deprecated (to indicate that it is a temporary measure that is intended to be removed) the API element MAY be removed in the following major release. When modifying a [Stable](./InterfaceClassification.html#Stable) API, developers SHOULD prefer introducing a new method or endpoint and deprecating the existing one to making incompatible changes to the method or endpoint.

## Compatibility types

### Java API

Developers SHOULD annotate all Hadoop interfaces and classes with the @InterfaceAudience and @InterfaceStability annotations to describe the intended audience and stability.

* @InterfaceAudience captures the intended audience. Possible values are [Public](./InterfaceClassification.html#Public) (for end users and external projects), Limited[Private](./InterfaceClassification.html#Private) (for other Hadoop components, and closely related projects like YARN, MapReduce, HBase etc.), and [Private](./InterfaceClassification.html#Private) (for intra component use).
* @InterfaceStability describes what types of interface changes are permitted. Possible values are [Stable](./InterfaceClassification.html#Stable), [Evolving](./InterfaceClassification.html#Evolving), and [Unstable](./InterfaceClassification.html#Unstable).
* @Deprecated notes that the package, class, or member variable or method could potentially be removed in the future and should not be used.

Annotations MAY be applied at the package, class, or method level. If a method has no privacy or stability annotation, it SHALL inherit its intended audience or stability level from the class to which it belongs. If a class has no privacy or stability annotation, it SHALL inherit its intended audience or stability level from the package to which it belongs. If a package has no privacy or stability annotation, it SHALL be assumed to be [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable), respectively.

In the event that an element’s audience or stability annotation conflicts with the corresponding annotation of its parent (whether explicit or inherited), the element’s audience or stability (respectively) SHALL be determined by the more restrictive annotation. For example, if a [Private](./InterfaceClassification.html#Private) method is contained in a [Public](./InterfaceClassification.html#Public) class, then the method SHALL be treated as [Private](./InterfaceClassification.html#Private). If a [Public](./InterfaceClassification.html#Public) method is contained in a [Private](./InterfaceClassification.html#Private) class, the method SHALL be treated as [Private](./InterfaceClassification.html#Private).

#### Use Cases

* [Public](./InterfaceClassification.html#Public)-[Stable](./InterfaceClassification.html#Stable) API compatibility is required to ensure end-user programs and downstream projects continue to work without modification.
* [Public](./InterfaceClassification.html#Public)-[Evolving](./InterfaceClassification.html#Evolving) API compatibility is useful to make functionality available for consumption before it is fully baked.
* Limited Private-[Stable](./InterfaceClassification.html#Stable) API compatibility is required to allow upgrade of individual components across minor releases.
* [Private](./InterfaceClassification.html#Private)-[Stable](./InterfaceClassification.html#Stable) API compatibility is required for rolling upgrades.
* [Private](./InterfaceClassification.html#Private)-[Unstable](./InterfaceClassification.html#Unstable) API compatibility allows internal components to evolve rapidly without concern for downstream consumers, and is how most interfaces should be labeled.

#### Policy

The compatibility policy SHALL be determined by the relevant package, class, or member variable or method annotations.

Note: APIs generated from the proto files MUST be compatible for rolling upgrades. See the section on wire protocol compatibility for more details. The compatibility policies for APIs and wire protocols must therefore go hand in hand.

#### Semantic compatibility

Apache Hadoop strives to ensure that the behavior of APIs remains consistent across releases, though changes for correctness may result in changes in behavior. API behavior SHALL be specified by the JavaDoc API documentation where present and complete. When JavaDoc API documentation is not available, behavior SHALL be specified by the behavior expected by the related unit tests. In cases with no JavaDoc API documentation or unit test coverage, the expected behavior is presumed to be obvious and SHOULD be assumed to be the minimum functionality implied by the interface naming. The community is in the process of specifying some APIs more rigorously and enhancing test suites to verify compliance with the specification, effectively creating a formal specification for the subset of behaviors that can be easily tested.

The behavior of any API MAY be changed to fix incorrect behavior according to the stability of the API, with such a change to be accompanied by updating existing documentation and tests and/or adding new documentation or tests.

#### Java Binary compatibility for end-user applications i.e. Apache Hadoop ABI

Apache Hadoop revisions SHOULD retain binary compatability such that end-user applications continue to work without any modifications. Minor Apache Hadoop revisions within the same major revision MUST retain compatibility such that existing MapReduce applications (e.g. end-user applications and projects such as Apache Pig, Apache Hive, et al), existing YARN applications (e.g. end-user applications and projects such as Apache Spark, Apache Tez et al), and applications that accesses HDFS directly (e.g. end-user applications and projects such as Apache HBase, Apache Flume, et al) work unmodified and without recompilation when used with any Apache Hadoop cluster within the same major release as the original build target.

For MapReduce applications in particular, i.e. applications using the org.apache.hadoop.mapred and/or org.apache.hadoop.mapreduce APIs, the developer community SHALL support binary compatibility across major releases. The MapReduce APIs SHALL be supported compatibly across major releases.

Some applications may be affected by changes to disk layouts or other internal changes. See the sections that follow for policies on how incompatible changes to non-API interfaces are handled.

### Native Dependencies

Hadoop includes several native components, including compression, the container executor binary, and various native integrations. These native components introduce a set of native dependencies for Hadoop, both at compile time and at runtime, such as cmake, gcc, zlib, etc. This set of native dependencies is part of the Hadoop ABI.

#### Policy

The minimum required versions of the native components on which Hadoop depends at compile time and/or runtime SHALL be considered [Evolving](./InterfaceClassification.html#Evolving). The minimum required versions SHOULD NOT increase between minor releases within a major version, though updates because of security issues, license issues, or other reasons MAY occur. When the native components on which Hadoop depends must be updated between minor releases within a major release, where possible the changes SHOULD only change the minor versions of the components without changing the major versions.

### Wire Protocols

Wire compatibility concerns data being transmitted “over the wire” between Hadoop processes. Hadoop uses [Protocol Buffers](https://developers.google.com/protocol-buffers/) for most RPC communication. Preserving compatibility requires prohibiting modification as described below. Non-RPC communication should be considered as well, for example using HTTP to transfer an HDFS image as part of snapshotting or transferring MapReduce map task output. The communications can be categorized as follows:

* Client-Server: communication between Hadoop clients and servers (e.g., the HDFS client to NameNode protocol, or the YARN client to ResourceManager protocol).
* Client-Server (Admin): It is worth distinguishing a subset of the Client-Server protocols used solely by administrative commands (e.g., the HAAdmin protocol) as these protocols only impact administrators who can tolerate changes that end users (which use general Client-Server protocols) cannot.
* Server-Server: communication between servers (e.g., the protocol between the DataNode and NameNode, or NodeManager and ResourceManager)

#### Protocol Dependencies

The components of Apache Hadoop may have dependencies that include their own protocols, such as Zookeeper, S3, Kerberos, etc. These protocol dependencies SHALL be treated as internal protocols and governed by the same policy.

#### Transports

In addition to compatibility of the protocols themselves, maintaining cross-version communications requires that the transports supported also be stable. The most likely source of transport changes stems from secure transports, such as SSL. Upgrading a service from SSLv2 to SSLv3 may break existing SSLv2 clients. The minimum supported major version of any transports SHOULD NOT increase between minor releases within a major version, though updates because of security issues, license issues, or other reasons MAY occur. When a transport must be updated between minor releases within a major release, where possible the changes SHOULD only change the minor versions of the components without changing the major versions.

Service ports are considered as part of the transport mechanism. Default service port numbers must be kept consistent to prevent breaking clients.

#### Policy

Hadoop wire protocols are defined in .proto (ProtocolBuffers) files. Client-Server and Server-Server protocols SHALL be classified according to the audience and stability classifications noted in their .proto files. In cases where no classifications are present, the protocols SHOULD be assumed to be [Private](./InterfaceClassification.html#Private) and [Stable](./InterfaceClassification.html#Stable).

The following changes to a .proto file SHALL be considered compatible:

* Add an optional field, with the expectation that the code deals with the field missing due to communication with an older version of the code
* Add a new rpc/method to the service
* Add a new optional request to a Message
* Rename a field
* Rename a .proto file
* Change .proto annotations that effect code generation (e.g. name of java package)

The following changes to a .proto file SHALL be considered incompatible:

* Change an rpc/method name
* Change an rpc/method parameter type or return type
* Remove an rpc/method
* Change the service name
* Change the name of a Message
* Modify a field type in an incompatible way (as defined recursively)
* Change an optional field to required
* Add or delete a required field
* Delete an optional field as long as the optional field has reasonable defaults to allow deletions

The following changes to a .proto file SHALL be considered incompatible:

* Change a field id
* Reuse an old field that was previously deleted.

Hadoop wire protocols that are not defined via .proto files SHOULD be considered to be [Private](./InterfaceClassification.html#Private) and [Stable](./InterfaceClassification.html#Stable).

In addition to the limitations imposed by being [Stable](./InterfaceClassification.html#Stable), Hadoop’s wire protocols MUST also be forward compatible across minor releases within a major version according to the following:

* Client-Server compatibility MUST be maintained so as to allow users to continue using older clients even after upgrading the server (cluster) to a later version (or vice versa). For example, a Hadoop 2.1.0 client talking to a Hadoop 2.3.0 cluster.
* Client-Server compatibility MUST be maintained so as to allow users to upgrade the client before upgrading the server (cluster). For example, a Hadoop 2.4.0 client talking to a Hadoop 2.3.0 cluster. This allows deployment of client-side bug fixes ahead of full cluster upgrades. Note that new cluster features invoked by new client APIs or shell commands will not be usable. YARN applications that attempt to use new APIs (including new fields in data structures) that have not yet been deployed to the cluster can expect link exceptions.
* Client-Server compatibility MUST be maintained so as to allow upgrading individual components without upgrading others. For example, upgrade HDFS from version 2.1.0 to 2.2.0 without upgrading MapReduce.
* Server-Server compatibility MUST be maintained so as to allow mixed versions within an active cluster so the cluster may be upgraded without downtime in a rolling fashion.

New transport mechanisms MUST only be introduced with minor or major version changes. Existing transport mechanisms MUST continue to be supported across minor versions within a major version. Default service port numbers SHALL be considered [Stable](./InterfaceClassification.html#Stable).

### REST APIs

REST API compatibility applies to the exposed REST endpoints (URLs) and response data format. Hadoop REST APIs are specifically meant for stable use by clients across releases, even major ones. For purposes of this document, an exposed PEST API is one that is documented in the public documentation. The following is a non-exhaustive list of the exposed REST APIs:

* [WebHDFS](../hadoop-hdfs/WebHDFS.html)
* [ResourceManager](../../hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html)
* [NodeManager](../../hadoop-yarn/hadoop-yarn-site/NodeManagerRest.html)
* [MR Application Master](../../hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredAppMasterRest.html)
* [History Server](../../hadoop-mapreduce-client/hadoop-mapreduce-client-hs/HistoryServerRest.html)
* [Timeline Server v1 REST API](../../hadoop-yarn/hadoop-yarn-site/TimelineServer.html)
* [Timeline Service v2 REST API](../../hadoop-yarn/hadoop-yarn-site/TimelineServiceV2.html)

Each API has an API-specific version number. Any incompatible changes MUST increment the API version number.

#### Policy

The exposed Hadoop REST APIs SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving). With respect to API version numbers, the exposed Hadoop REST APIs SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable), i.e. no incompatible changes are allowed to within an API version number. A REST API version must be labeled as deprecated for a full major release before it can be removed.

### Log Output

The Hadoop daemons and CLIs produce log output via Log4j that is intended to aid administrators and developers in understanding and troubleshooting cluster behavior. Log messages are intended for human consumption, though automation use cases are also supported.

#### Policy

All log output SHALL be considered [Public](./InterfaceClassification.html#Public) and [Unstable](./InterfaceClassification.html#Unstable). For log output, an incompatible change is one that renders a parser unable to find or recognize a line of log output.

### Audit Log Output

Several components have audit logging systems that record system information in a machine readable format. Incompatible changes to that data format may break existing automation utilities. For the audit log, an incompatible change is any change that changes the format such that existing parsers no longer can parse the logs.

#### Policy

All audit log output SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). Any change to the data format SHALL be considered an incompatible change.

### Metrics/JMX

While the Metrics API compatibility is governed by Java API compatibility, the Metrics data format exposed by Hadoop MUST be maintained as compatible for consumers of the data, e.g. for automation tasks.

#### Policy

The data format exposed via Metrics SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable).

### File formats & Metadata

User and system level data (including metadata) is stored in files of various formats. Changes to the metadata or the file formats used to store data/metadata can lead to incompatibilities between versions. Each class of file format is addressed below.

#### User-level file formats

Changes to formats that end users use to store their data can prevent them from accessing the data in later releases, and hence are important to be compatible. Examples of these formats include har, war, SequenceFileFormat, etc.

##### Policy

User-level file formats SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). User-lever file format changes SHOULD be made forward compatible across major releases and MUST be made forward compatible within a major release. The developer community SHOULD prefer the creation of a new derivative file format to making incompatible changes to an existing file format. Such new file formats MUST be created as opt-in, meaning that users must be able to continue using the existing compatible format until and unless they explicitly opt in to using the new file format.

#### System-internal data schemas

Hadoop internal data may also be stored in files or other data stores. Changing the schemas of these data stores can lead to incompatibilities.

##### MapReduce

MapReduce uses formats like I-File to store MapReduce-specific data.

###### Policy

All MapReduce-internal file formats, such as I-File format or the job history server’s jhist file format, SHALL be considered [Private](./InterfaceClassification.html#Private) and [Stable](./InterfaceClassification.html#Stable).

##### HDFS Metadata

HDFS persists metadata (the image and edit logs) in a private file format. Incompatible changes to either the format or the metadata prevent subsequent releases from reading older metadata. Incompatible changes must include a process by which existing metadata may be upgraded.

Depending on the degree of incompatibility in the changes, the following potential scenarios can arise:

* Automatic: The image upgrades automatically, no need for an explicit “upgrade”.
* Direct: The image is upgradeable, but might require one explicit release “upgrade”.
* Indirect: The image is upgradeable, but might require upgrading to intermediate release(s) first.
* Not upgradeable: The image is not upgradeable.

HDFS data nodes store data in a private directory structure. Incompatible changes to the directory structure may prevent older releases from accessing stored data. Incompatible changes must include a process by which existing data directories may be upgraded.

###### Policy

The HDFS metadata format SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Incompatible changes MUST include a process by which existing metadata may be upgraded. The upgrade process SHALL be allowed to require more than one upgrade. The upgrade process MUST allow the cluster metadata to be rolled back to the older version and its older disk format. The rollback MUST restore the original data but is not REQUIRED to restore the updated data. Any incompatible change to the format MUST result in the major version number of the schema being incremented.

The data node directory format SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Incompatible changes MUST include a process by which existing data directories may be upgraded. The upgrade process SHALL be allowed to require more than one upgrade. The upgrade process MUST allow the data directories to be rolled back to the older layout.

##### AWS S3A Guard Metadata

The S3Guard metastore used to store metadata in DynamoDB tables; as such it had to maintain a compatibility strategy. Now that S3Guard is removed, the tables are not needed.

Applications configured to use an S3A metadata store other than the “null” store will fail.

##### YARN Resource Manager State Store

The YARN resource manager stores information about the cluster state in an external state store for use in fail over and recovery. If the schema used for the state store data does not remain compatible, the resource manager will not be able to recover its state and will fail to start. The state store data schema includes a version number that indicates compatibility.

###### Policy

The YARN resource manager state store data schema SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Any incompatible change to the schema MUST result in the major version number of the schema being incremented. Any compatible change to the schema MUST result in the minor version number being incremented.

##### YARN Node Manager State Store

The YARN node manager stores information about the node state in an external state store for use in recovery. If the schema used for the state store data does not remain compatible, the node manager will not be able to recover its state and will fail to start. The state store data schema includes a version number that indicates compatibility.

###### Policy

The YARN node manager state store data schema SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Any incompatible change to the schema MUST result in the major version number of the schema being incremented. Any compatible change to the schema MUST result in the minor version number being incremented.

##### YARN Federation State Store

The YARN resource manager federation service stores information about the federated clusters, running applications, and routing policies in an external state store for use in replication and recovery. If the schema used for the state store data does not remain compatible, the federation service will fail to initialize. The state store data schema includes a version number that indicates compatibility.

###### Policy

The YARN federation service state store data schema SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Any incompatible change to the schema MUST result in the major version number of the schema being incremented. Any compatible change to the schema MUST result in the minor version number being incremented.

### Command Line Interface (CLI)

The Hadoop command line programs may be used either directly via the system shell or via shell scripts. The CLIs include both the user-facing commands, such as the hdfs command or the yarn command, and the admin-facing commands, such as the scripts used to start and stop daemons. Changing the path of a command, removing or renaming command line options, the order of arguments, or the command return codes and output break compatibility and adversely affect users.

#### Policy

All Hadoop CLI paths, usage, and output SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable) unless documented as experimental and subject to change.

Note that the CLI output SHALL be considered distinct from the log output generated by the Hadoop CLIs. The latter SHALL be governed by the policy on log output. Note also that for CLI output, all changes SHALL be considered incompatible changes.

### Web UI

Web UI, particularly the content and layout of web pages, changes could potentially interfere with attempts to screen scrape the web pages for information. The Hadoop Web UI pages, however, are not meant to be scraped, e.g. for automation purposes. Users are expected to use REST APIs to programmatically access cluster information.

#### Policy

The Hadoop Web UI SHALL be considered [Public](./InterfaceClassification.html#Public) and [Unstable](./InterfaceClassification.html#Unstable).

### Functional Compatibility

Users depend on the behavior of a Hadoop cluster remaining consistent across releases. Changes which cause unexpectedly different behaviors from the cluster can lead to frustration and long adoption cycles. No new configuration should be added which changes the behavior of an existing cluster, assuming the cluster’s configuration files remain unchanged. For any new settings that are defined, care should be taken to ensure that the new setting does not change the behavior of existing clusters.

#### Policy

Changes to existing functionality MUST NOT change the default behavior or the meaning of existing configuration settings between maintenance releases within the same minor version, regardless of whether the changes arise from changes to the system or logic or to internal or external default configuration values.

Changes to existing functionality SHOULD NOT change the default behavior or the meaning of existing configuration settings between minor releases within the same major version, though changes, such as to fix correctness or security issues, may require incompatible behavioral changes. Where possible such behavioral changes SHOULD be off by default.

### Hadoop Configuration Files

Users use Hadoop-defined properties to configure and provide hints to Hadoop and custom properties to pass information to jobs. Users are encouraged to avoid using custom configuration property names that conflict with the namespace of Hadoop-defined properties and should avoid using any prefixes used by Hadoop, e.g. hadoop, io, ipc, fs, net, file, ftp, kfs, ha, file, dfs, mapred, mapreduce, and yarn.

In addition to properties files, Hadoop uses other configuration files to set system behavior, such as the fair scheduler configuration file or the resource profiles configuration file.

#### Policy

Hadoop-defined properties (names and meanings) SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). The units implied by a Hadoop-defined property MUST NOT change, even across major versions. Default values of Hadoop-defined properties SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving).

Hadoop configuration files that are not governed by the above rules about Hadoop-defined properties SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). The definition of an incompatible change depends on the particular configuration file format, but the general rule is that a compatible change will allow a configuration file that was valid before the change to remain valid after the change.

### Log4j Configuration Files

The log output produced by Hadoop daemons and CLIs is governed by a set of configuration files. These files control the minimum level of log message that will be output by the various components of Hadoop, as well as where and how those messages are stored.

#### Policy

All Log4j configurations SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving).

### Directory Structure

Source code, artifacts (source and tests), user logs, configuration files, output, and job history are all stored on disk on either the local file system or HDFS. Changing the directory structure of these user-accessible files can break compatibility, even in cases where the original path is preserved via symbolic links (such as when the path is accessed by a servlet that is configured to not follow symbolic links).

#### Policy

The layout of source code and build artifacts SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable). Within a major version, the developer community SHOULD preserve the overall directory structure, though individual files MAY be added, moved, or deleted with no warning.

The directory structure of configuration files, user logs, and job history SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving).

### Java Classpath

Hadoop provides several client artifacts that applications use to interact with the system. These artifacts typically have their own dependencies on common libraries. In the cases where these dependencies are exposed to end user applications or downstream consumers (i.e. not [shaded](https://stackoverflow.com/questions/13620281/what-is-the-maven-shade-plugin-used-for-and-why-would-you-want-to-relocate-java)) changes to these dependencies can be disruptive. Developers are strongly encouraged to avoid exposing dependencies to clients by using techniques such as [shading](https://stackoverflow.com/questions/13620281/what-is-the-maven-shade-plugin-used-for-and-why-would-you-want-to-relocate-java).

With regard to dependencies, adding a dependency is an incompatible change, whereas removing a dependency is a compatible change.

Some user applications built against Hadoop may add all Hadoop JAR files (including Hadoop’s library dependencies) to the application’s classpath. Adding new dependencies or updating the versions of existing dependencies may interfere with those in applications’ classpaths and hence their correct operation. Users are therefore discouraged from adopting this practice.

#### Policy

The set of dependencies exposed by the Hadoop client artifacts SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). Any dependencies that are not exposed to clients (either because they are shaded or only exist in non-client artifacts) SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable)

### Environment variables

Users and related projects often utilize the environment variables exported by Hadoop (e.g. HADOOP\_CONF\_DIR). Removing or renaming environment variables can therefore impact end user applications.

#### Policy

The environment variables consumed by Hadoop and the environment variables made accessible to applications through YARN SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving). The developer community SHOULD limit changes to major releases.

### Build artifacts

Hadoop uses Maven for project management. Changes to the contents of generated artifacts can impact existing user applications.

#### Policy

The contents of Hadoop test artifacts SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable). Test artifacts include all JAR files generated from test source code and all JAR files that include “tests” in the file name.

The Hadoop client artifacts SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). Client artifacts are the following:

* hadoop-client
* hadoop-client-api
* hadoop-client-minicluster
* hadoop-client-runtime
* hadoop-hdfs-client
* hadoop-hdfs-native-client
* hadoop-mapreduce-client-app
* hadoop-mapreduce-client-common
* hadoop-mapreduce-client-core
* hadoop-mapreduce-client-hs
* hadoop-mapreduce-client-hs-plugins
* hadoop-mapreduce-client-jobclient
* hadoop-mapreduce-client-nativetask
* hadoop-mapreduce-client-shuffle
* hadoop-yarn-client

All other build artifacts SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable).

### Hardware/Software Requirements

To keep up with the latest advances in hardware, operating systems, JVMs, and other software, new Hadoop releases may include features that require newer hardware, operating systems releases, or JVM versions than previous Hadoop releases. For a specific environment, upgrading Hadoop might require upgrading other dependent software components.

#### Policies

* Hardware
  * Architecture: Intel and AMD are the processor architectures currently supported by the community. The community has no plans to restrict Hadoop to specific architectures, but MAY have family-specific optimizations. Support for any processor architecture SHOULD NOT be dropped without first being documented as deprecated for a full major release and MUST NOT be dropped without first being deprecated for at least a full minor release.
  * Minimum resources: While there are no guarantees on the minimum resources required by Hadoop daemons, the developer community SHOULD avoid increasing requirements within a minor release.
* Operating Systems: The community SHOULD maintain the same minimum OS requirements (OS kernel versions) within a minor release. Currently GNU/Linux and Microsoft Windows are the OSes officially supported by the community, while Apache Hadoop is known to work reasonably well on other OSes such as Apple MacOSX, Solaris, etc. Support for any OS SHOULD NOT be dropped without first being documented as deprecated for a full major release and MUST NOT be dropped without first being deprecated for at least a full minor release.
* The JVM requirements SHALL NOT change across minor releases within the same major release unless the JVM version in question becomes unsupported. The JVM version requirement MAY be different for different operating systems or even operating system releases.
* File systems supported by Hadoop, e.g. through the FileSystem API, SHOULD not become unsupported between minor releases within a major version unless a migration path to an alternate client implementation is available.

## References

Here are some relevant JIRAs and pages related to the topic:

* The evolution of this document - [HADOOP-9517](https://issues.apache.org/jira/browse/HADOOP-9517)
* Annotations for interfaces as per interface classification schedule - [HADOOP-7391](https://issues.apache.org/jira/browse/HADOOP-7391) [Hadoop Interface Classification](./InterfaceClassification.html)
* Compatibility for Hadoop 1.x releases - [HADOOP-5071](https://issues.apache.org/jira/browse/HADOOP-5071)
* The [Hadoop Roadmap](http://wiki.apache.org/hadoop/Roadmap) page that captures other release policies

---
# Hadoop Cluster Setup

* [Purpose](#Purpose)
* [Prerequisites](#Prerequisites)
* [Installation](#Installation)
* [Configuring Hadoop in Non-Secure Mode](#Configuring_Hadoop_in_Non-Secure_Mode)
  * [Configuring Environment of Hadoop Daemons](#Configuring_Environment_of_Hadoop_Daemons)
  * [Configuring the Hadoop Daemons](#Configuring_the_Hadoop_Daemons)
* [Monitoring Health of NodeManagers](#Monitoring_Health_of_NodeManagers)
* [Slaves File](#Slaves_File)
* [Hadoop Rack Awareness](#Hadoop_Rack_Awareness)
* [Logging](#Logging)
* [Operating the Hadoop Cluster](#Operating_the_Hadoop_Cluster)
  * [Hadoop Startup](#Hadoop_Startup)
  * [Hadoop Shutdown](#Hadoop_Shutdown)
* [Web Interfaces](#Web_Interfaces)

## Purpose

This document describes how to install and configure Hadoop clusters ranging from a few nodes to extremely large clusters with thousands of nodes. To play with Hadoop, you may first want to install it on a single machine (see [Single Node Setup](./SingleCluster.html)).

This document does not cover advanced topics such as High Availability.

*Important*: all production Hadoop clusters use Kerberos to authenticate callers and secure access to HDFS data as well as restriction access to computation services (YARN etc.).

These instructions do not cover integration with any Kerberos services, -everyone bringing up a production cluster should include connecting to their organisation’s Kerberos infrastructure as a key part of the deployment.

See [Security](./SecureMode.html) for details on how to secure a cluster.

## Prerequisites

* Install Java. See the [Hadoop Wiki](https://cwiki.apache.org/confluence/display/HADOOP/Hadoop+Java+Versions) for known good versions.
* Download a stable version of Hadoop from Apache mirrors.

## Installation

Installing a Hadoop cluster typically involves unpacking the software on all the machines in the cluster or installing it via a packaging system as appropriate for your operating system. It is important to divide up the hardware into functions.

Typically one machine in the cluster is designated as the NameNode and another machine as the ResourceManager, exclusively. These are the masters. Other services (such as Web App Proxy Server and MapReduce Job History server) are usually run either on dedicated hardware or on shared infrastructure, depending upon the load.

The rest of the machines in the cluster act as both DataNode and NodeManager. These are the workers.

## Configuring Hadoop in Non-Secure Mode

Hadoop’s Java configuration is driven by two types of important configuration files:

* Read-only default configuration - `core-default.xml`, `hdfs-default.xml`, `yarn-default.xml` and `mapred-default.xml`.
* Site-specific configuration - `etc/hadoop/core-site.xml`, `etc/hadoop/hdfs-site.xml`, `etc/hadoop/yarn-site.xml` and `etc/hadoop/mapred-site.xml`.

Additionally, you can control the Hadoop scripts found in the bin/ directory of the distribution, by setting site-specific values via the `etc/hadoop/hadoop-env.sh` and `etc/hadoop/yarn-env.sh`.

To configure the Hadoop cluster you will need to configure the `environment` in which the Hadoop daemons execute as well as the `configuration parameters` for the Hadoop daemons.

HDFS daemons are NameNode, SecondaryNameNode, and DataNode. YARN daemons are ResourceManager, NodeManager, and WebAppProxy. If MapReduce is to be used, then the MapReduce Job History Server will also be running. For large installations, these are generally running on separate hosts.

### Configuring Environment of Hadoop Daemons

Administrators should use the `etc/hadoop/hadoop-env.sh` and optionally the `etc/hadoop/mapred-env.sh` and `etc/hadoop/yarn-env.sh` scripts to do site-specific customization of the Hadoop daemons’ process environment.

At the very least, you must specify the `JAVA_HOME` so that it is correctly defined on each remote node.

Administrators can configure individual daemons using the configuration options shown below in the table:

| Daemon | Environment Variable |
| --- | --- |
| NameNode | HDFS\_NAMENODE\_OPTS |
| DataNode | HDFS\_DATANODE\_OPTS |
| Secondary NameNode | HDFS\_SECONDARYNAMENODE\_OPTS |
| ResourceManager | YARN\_RESOURCEMANAGER\_OPTS |
| NodeManager | YARN\_NODEMANAGER\_OPTS |
| WebAppProxy | YARN\_PROXYSERVER\_OPTS |
| Map Reduce Job History Server | MAPRED\_HISTORYSERVER\_OPTS |

For example, To configure Namenode to use parallelGC and a 4GB Java Heap, the following statement should be added in hadoop-env.sh :

```
  export HDFS_NAMENODE_OPTS="-XX:+UseParallelGC -Xmx4g"
```

See `etc/hadoop/hadoop-env.sh` for other examples.

Other useful configuration parameters that you can customize include:

* `HADOOP_PID_DIR` - The directory where the daemons’ process id files are stored.
* `HADOOP_LOG_DIR` - The directory where the daemons’ log files are stored. Log files are automatically created if they don’t exist.
* `HADOOP_HEAPSIZE_MAX` - The maximum amount of memory to use for the Java heapsize. Units supported by the JVM are also supported here. If no unit is present, it will be assumed the number is in megabytes. By default, Hadoop will let the JVM determine how much to use. This value can be overriden on a per-daemon basis using the appropriate `_OPTS` variable listed above. For example, setting `HADOOP_HEAPSIZE_MAX=1g` and `HADOOP_NAMENODE_OPTS="-Xmx5g"` will configure the NameNode with 5GB heap.

In most cases, you should specify the `HADOOP_PID_DIR` and `HADOOP_LOG_DIR` directories such that they can only be written to by the users that are going to run the hadoop daemons. Otherwise there is the potential for a symlink attack.

It is also traditional to configure `HADOOP_HOME` in the system-wide shell environment configuration. For example, a simple script inside `/etc/profile.d`:

```
  HADOOP_HOME=/path/to/hadoop
  export HADOOP_HOME
```

### Configuring the Hadoop Daemons

This section deals with important parameters to be specified in the given configuration files:

* `etc/hadoop/core-site.xml`

| Parameter | Value | Notes |
| --- | --- | --- |
| `fs.defaultFS` | NameNode URI | <hdfs://host:port/> |
| `io.file.buffer.size` | 131072 | Size of read/write buffer used in SequenceFiles. |

* `etc/hadoop/hdfs-site.xml`
* Configurations for NameNode:

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.namenode.name.dir` | Path on the local filesystem where the NameNode stores the namespace and transactions logs persistently. | If this is a comma-delimited list of directories then the name table is replicated in all of the directories, for redundancy. |
| `dfs.hosts` / `dfs.hosts.exclude` | List of permitted/excluded DataNodes. | If necessary, use these files to control the list of allowable datanodes. |
| `dfs.blocksize` | 268435456 | HDFS blocksize of 256MB for large file-systems. |
| `dfs.namenode.handler.count` | 100 | More NameNode server threads to handle RPCs from large number of DataNodes. |

* Configurations for DataNode:

| Parameter | Value | Notes |
| --- | --- | --- |
| `dfs.datanode.data.dir` | Comma separated list of paths on the local filesystem of a `DataNode` where it should store its blocks. | If this is a comma-delimited list of directories, then data will be stored in all named directories, typically on different devices. |

* `etc/hadoop/yarn-site.xml`
* Configurations for ResourceManager and NodeManager:

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.acl.enable` | `true` / `false` | Enable ACLs? Defaults to *false*. |
| `yarn.admin.acl` | Admin ACL | ACL to set admins on the cluster. ACLs are of for *comma-separated-usersspacecomma-separated-groups*. Defaults to special value of **\*** which means *anyone*. Special value of just *space* means no one has access. |
| `yarn.log-aggregation-enable` | *false* | Configuration to enable or disable log aggregation |

* Configurations for ResourceManager:

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.resourcemanager.address` | `ResourceManager` host:port for clients to submit jobs. | *host:port* If set, overrides the hostname set in `yarn.resourcemanager.hostname`. |
| `yarn.resourcemanager.scheduler.address` | `ResourceManager` host:port for ApplicationMasters to talk to Scheduler to obtain resources. | *host:port* If set, overrides the hostname set in `yarn.resourcemanager.hostname`. |
| `yarn.resourcemanager.resource-tracker.address` | `ResourceManager` host:port for NodeManagers. | *host:port* If set, overrides the hostname set in `yarn.resourcemanager.hostname`. |
| `yarn.resourcemanager.admin.address` | `ResourceManager` host:port for administrative commands. | *host:port* If set, overrides the hostname set in `yarn.resourcemanager.hostname`. |
| `yarn.resourcemanager.webapp.address` | `ResourceManager` web-ui host:port. | *host:port* If set, overrides the hostname set in `yarn.resourcemanager.hostname`. |
| `yarn.resourcemanager.hostname` | `ResourceManager` host. | *host* Single hostname that can be set in place of setting all `yarn.resourcemanager*address` resources. Results in default ports for ResourceManager components. |
| `yarn.resourcemanager.scheduler.class` | `ResourceManager` Scheduler class. | `CapacityScheduler` (recommended), `FairScheduler` (also recommended), or `FifoScheduler`. Use a fully qualified class name, e.g., `org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler`. |
| `yarn.scheduler.minimum-allocation-mb` | Minimum limit of memory to allocate to each container request at the `Resource Manager`. | In MBs |
| `yarn.scheduler.maximum-allocation-mb` | Maximum limit of memory to allocate to each container request at the `Resource Manager`. | In MBs |
| `yarn.resourcemanager.nodes.include-path` / `yarn.resourcemanager.nodes.exclude-path` | List of permitted/excluded NodeManagers. | If necessary, use these files to control the list of allowable NodeManagers. |

* Configurations for NodeManager:

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.nodemanager.resource.memory-mb` | Resource i.e. available physical memory, in MB, for given `NodeManager` | Defines total available resources on the `NodeManager` to be made available to running containers |
| `yarn.nodemanager.vmem-pmem-ratio` | Maximum ratio by which virtual memory usage of tasks may exceed physical memory | The virtual memory usage of each task may exceed its physical memory limit by this ratio. The total amount of virtual memory used by tasks on the NodeManager may exceed its physical memory usage by this ratio. |
| `yarn.nodemanager.local-dirs` | Comma-separated list of paths on the local filesystem where intermediate data is written. | Multiple paths help spread disk i/o. |
| `yarn.nodemanager.log-dirs` | Comma-separated list of paths on the local filesystem where logs are written. | Multiple paths help spread disk i/o. |
| `yarn.nodemanager.log.retain-seconds` | *10800* | Default time (in seconds) to retain log files on the NodeManager Only applicable if log-aggregation is disabled. |
| `yarn.nodemanager.remote-app-log-dir` | */logs* | HDFS directory where the application logs are moved on application completion. Need to set appropriate permissions. Only applicable if log-aggregation is enabled. |
| `yarn.nodemanager.remote-app-log-dir-suffix` | *logs* | Suffix appended to the remote log dir. Logs will be aggregated to ${yarn.nodemanager.remote-app-log-dir}/${user}/${thisParam} Only applicable if log-aggregation is enabled. |
| `yarn.nodemanager.aux-services` | mapreduce\_shuffle | Shuffle service that needs to be set for Map Reduce applications. |
| `yarn.nodemanager.env-whitelist` | Environment properties to be inherited by containers from NodeManagers | For mapreduce application in addition to the default values HADOOP\_MAPRED\_HOME should to be added. Property value should JAVA\_HOME,HADOOP\_COMMON\_HOME,HADOOP\_HDFS\_HOME,HADOOP\_CONF\_DIR,CLASSPATH\_PREPEND\_DISTCACHE,HADOOP\_YARN\_HOME,HADOOP\_HOME,PATH,LANG,TZ,HADOOP\_MAPRED\_HOME |

* Configurations for History Server (Needs to be moved elsewhere):

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.log-aggregation.retain-seconds` | *-1* | How long to keep aggregation logs before deleting them. -1 disables. Be careful, set this too small and you will spam the name node. |
| `yarn.log-aggregation.retain-check-interval-seconds` | *-1* | Time between checks for aggregated log retention. If set to 0 or a negative value then the value is computed as one-tenth of the aggregated log retention time. Be careful, set this too small and you will spam the name node. |

* `etc/hadoop/mapred-site.xml`
* Configurations for MapReduce Applications:

| Parameter | Value | Notes |
| --- | --- | --- |
| `mapreduce.framework.name` | yarn | Execution framework set to Hadoop YARN. |
| `mapreduce.map.memory.mb` | 1536 | Larger resource limit for maps. |
| `mapreduce.map.java.opts` | -Xmx1024M | Larger heap-size for child jvms of maps. |
| `mapreduce.reduce.memory.mb` | 3072 | Larger resource limit for reduces. |
| `mapreduce.reduce.java.opts` | -Xmx2560M | Larger heap-size for child jvms of reduces. |
| `mapreduce.task.io.sort.mb` | 512 | Higher memory-limit while sorting data for efficiency. |
| `mapreduce.task.io.sort.factor` | 100 | More streams merged at once while sorting files. |
| `mapreduce.reduce.shuffle.parallelcopies` | 50 | Higher number of parallel copies run by reduces to fetch outputs from very large number of maps. |

* Configurations for MapReduce JobHistory Server:

| Parameter | Value | Notes |
| --- | --- | --- |
| `mapreduce.jobhistory.address` | MapReduce JobHistory Server *host:port* | Default port is 10020. |
| `mapreduce.jobhistory.webapp.address` | MapReduce JobHistory Server Web UI *host:port* | Default port is 19888. |
| `mapreduce.jobhistory.intermediate-done-dir` | /mr-history/tmp | Directory where history files are written by MapReduce jobs. |
| `mapreduce.jobhistory.done-dir` | /mr-history/done | Directory where history files are managed by the MR JobHistory Server. |

## Monitoring Health of NodeManagers

Hadoop provides a mechanism by which administrators can configure the NodeManager to run an administrator supplied script periodically to determine if a node is healthy or not.

Administrators can determine if the node is in a healthy state by performing any checks of their choice in the script. If the script detects the node to be in an unhealthy state, it must print a line to standard output beginning with the string ERROR. The NodeManager spawns the script periodically and checks its output. If the script’s output contains the string ERROR, as described above, the node’s status is reported as `unhealthy` and the node is black-listed by the ResourceManager. No further tasks will be assigned to this node. However, the NodeManager continues to run the script, so that if the node becomes healthy again, it will be removed from the blacklisted nodes on the ResourceManager automatically. The node’s health along with the output of the script, if it is unhealthy, is available to the administrator in the ResourceManager web interface. The time since the node was healthy is also displayed on the web interface.

The following parameters can be used to control the node health monitoring script in `etc/hadoop/yarn-site.xml`.

| Parameter | Value | Notes |
| --- | --- | --- |
| `yarn.nodemanager.health-checker.script.path` | Node health script | Script to check for node’s health status. |
| `yarn.nodemanager.health-checker.script.opts` | Node health script options | Options for script to check for node’s health status. |
| `yarn.nodemanager.health-checker.interval-ms` | Node health script interval | Time interval for running health script. |
| `yarn.nodemanager.health-checker.script.timeout-ms` | Node health script timeout interval | Timeout for health script execution. |

The health checker script is not supposed to give ERROR if only some of the local disks become bad. NodeManager has the ability to periodically check the health of the local disks (specifically checks nodemanager-local-dirs and nodemanager-log-dirs) and after reaching the threshold of number of bad directories based on the value set for the config property yarn.nodemanager.disk-health-checker.min-healthy-disks, the whole node is marked unhealthy and this info is sent to resource manager also. The boot disk is either raided or a failure in the boot disk is identified by the health checker script.

## Slaves File

List all worker hostnames or IP addresses in your `etc/hadoop/workers` file, one per line. Helper scripts (described below) will use the `etc/hadoop/workers` file to run commands on many hosts at once. It is not used for any of the Java-based Hadoop configuration. In order to use this functionality, ssh trusts (via either passphraseless ssh or some other means, such as Kerberos) must be established for the accounts used to run Hadoop.

## Hadoop Rack Awareness

Many Hadoop components are rack-aware and take advantage of the network topology for performance and safety. Hadoop daemons obtain the rack information of the workers in the cluster by invoking an administrator configured module. See the [Rack Awareness](./RackAwareness.html) documentation for more specific information.

It is highly recommended configuring rack awareness prior to starting HDFS.

## Logging

Hadoop uses the [Apache log4j](http://logging.apache.org/log4j/2.x/) via the Apache Commons Logging framework for logging. Edit the `etc/hadoop/log4j.properties` file to customize the Hadoop daemons’ logging configuration (log-formats and so on).

## Operating the Hadoop Cluster

Once all the necessary configuration is complete, distribute the files to the `HADOOP_CONF_DIR` directory on all the machines. This should be the same directory on all machines.

In general, it is recommended that HDFS and YARN run as separate users. In the majority of installations, HDFS processes execute as ‘hdfs’. YARN is typically using the ‘yarn’ account.

### Hadoop Startup

To start a Hadoop cluster you will need to start both the HDFS and YARN cluster.

The first time you bring up HDFS, it must be formatted. Format a new distributed filesystem as *hdfs*:

```
[hdfs]$ $HADOOP_HOME/bin/hdfs namenode -format
```

Start the HDFS NameNode with the following command on the designated node as *hdfs*:

```
[hdfs]$ $HADOOP_HOME/bin/hdfs --daemon start namenode
```

Start a HDFS DataNode with the following command on each designated node as *hdfs*:

```
[hdfs]$ $HADOOP_HOME/bin/hdfs --daemon start datanode
```

If `etc/hadoop/workers` and ssh trusted access is configured (see [Single Node Setup](./SingleCluster.html)), all of the HDFS processes can be started with a utility script. As *hdfs*:

```
[hdfs]$ $HADOOP_HOME/sbin/start-dfs.sh
```

Start the YARN with the following command, run on the designated ResourceManager as *yarn*:

```
[yarn]$ $HADOOP_HOME/bin/yarn --daemon start resourcemanager
```

Run a script to start a NodeManager on each designated host as *yarn*:

```
[yarn]$ $HADOOP_HOME/bin/yarn --daemon start nodemanager
```

Start a standalone WebAppProxy server. Run on the WebAppProxy server as *yarn*. If multiple servers are used with load balancing it should be run on each of them:

```
[yarn]$ $HADOOP_HOME/bin/yarn --daemon start proxyserver
```

If `etc/hadoop/workers` and ssh trusted access is configured (see [Single Node Setup](./SingleCluster.html)), all of the YARN processes can be started with a utility script. As *yarn*:

```
[yarn]$ $HADOOP_HOME/sbin/start-yarn.sh
```

Start the MapReduce JobHistory Server with the following command, run on the designated server as *mapred*:

```
[mapred]$ $HADOOP_HOME/bin/mapred --daemon start historyserver
```

### Hadoop Shutdown

Stop the NameNode with the following command, run on the designated NameNode as *hdfs*:

```
[hdfs]$ $HADOOP_HOME/bin/hdfs --daemon stop namenode
```

Run a script to stop a DataNode as *hdfs*:

```
[hdfs]$ $HADOOP_HOME/bin/hdfs --daemon stop datanode
```

If `etc/hadoop/workers` and ssh trusted access is configured (see [Single Node Setup](./SingleCluster.html)), all of the HDFS processes may be stopped with a utility script. As *hdfs*:

```
[hdfs]$ $HADOOP_HOME/sbin/stop-dfs.sh
```

Stop the ResourceManager with the following command, run on the designated ResourceManager as *yarn*:

```
[yarn]$ $HADOOP_HOME/bin/yarn --daemon stop resourcemanager
```

Run a script to stop a NodeManager on a worker as *yarn*:

```
[yarn]$ $HADOOP_HOME/bin/yarn --daemon stop nodemanager
```

If `etc/hadoop/workers` and ssh trusted access is configured (see [Single Node Setup](./SingleCluster.html)), all of the YARN processes can be stopped with a utility script. As *yarn*:

```
[yarn]$ $HADOOP_HOME/sbin/stop-yarn.sh
```

Stop the WebAppProxy server. Run on the WebAppProxy server as *yarn*. If multiple servers are used with load balancing it should be run on each of them:

```
[yarn]$ $HADOOP_HOME/bin/yarn stop proxyserver
```

Stop the MapReduce JobHistory Server with the following command, run on the designated server as *mapred*:

```
[mapred]$ $HADOOP_HOME/bin/mapred --daemon stop historyserver
```

## Web Interfaces

Once the Hadoop cluster is up and running check the web-ui of the components as described below:

| Daemon | Web Interface | Notes |
| --- | --- | --- |
| NameNode | <http://nn_host:port/> | Default HTTP port is 9870. |
| ResourceManager | <http://rm_host:port/> | Default HTTP port is 8088. |
| MapReduce JobHistory Server | <http://jhs_host:port/> | Default HTTP port is 19888. |

---
# Native Libraries Guide

* [Overview](#Overview)
* [Native Hadoop Library](#Native_Hadoop_Library)
* [Usage](#Usage)
* [Components](#Components)
* [Supported Platforms](#Supported_Platforms)
* [Download](#Download)
* [Build](#Build)
* [Runtime](#Runtime)
* [Check](#Check)
* [Native Shared Libraries](#Native_Shared_Libraries)

## Overview

This guide describes the native hadoop library and includes a small discussion about native shared libraries.

Note: Depending on your environment, the term “native libraries” could refer to all \*.so’s you need to compile; and, the term “native compression” could refer to all \*.so’s you need to compile that are specifically related to compression. Currently, however, this document only addresses the native hadoop library (`libhadoop.so`). The document for libhdfs library (`libhdfs.so`) is [here](../hadoop-hdfs/LibHdfs.html).

## Native Hadoop Library

Hadoop has native implementations of certain components for performance reasons and for non-availability of Java implementations. These components are available in a single, dynamically-linked native library called the native hadoop library. On the \*nix platforms the library is named `libhadoop.so`.

## Usage

It is fairly easy to use the native hadoop library:

1. Review the components.
2. Review the supported platforms.
3. Either download a hadoop release, which will include a pre-built version of the native hadoop library, or build your own version of the native hadoop library. Whether you download or build, the name for the library is the same: libhadoop.so
4. Install the compression codec development packages (>zlib-1.2, >gzip-1.2):
   * If you download the library, install one or more development packages - whichever compression codecs you want to use with your deployment.
   * If you build the library, it is mandatory to install both development packages.
5. Check the runtime log files.

## Components

The native hadoop library includes various components:

* Compression Codecs (bzip2, lz4, zlib)
* Native IO utilities for [HDFS Short-Circuit Local Reads](../hadoop-hdfs/ShortCircuitLocalReads.html) and [Centralized Cache Management in HDFS](../hadoop-hdfs/CentralizedCacheManagement.html)
* CRC32 checksum implementation

## Supported Platforms

The native hadoop library is supported on \*nix platforms only. The library does not to work with Cygwin or the Mac OS X platform.

The native hadoop library is mainly used on the GNU/Linus platform and has been tested on these distributions:

* RHEL4/Fedora
* Ubuntu
* Gentoo

On all the above distributions a 32/64 bit native hadoop library will work with a respective 32/64 bit jvm.

## Download

The pre-built 32-bit i386-Linux native hadoop library is available as part of the hadoop distribution and is located in the `lib/native` directory. You can download the hadoop distribution from Hadoop Common Releases.

Be sure to install the zlib and/or gzip development packages - whichever compression codecs you want to use with your deployment.

## Build

The native hadoop library is written in ANSI C and is built using the GNU autotools-chain (autoconf, autoheader, automake, autoscan, libtool). This means it should be straight-forward to build the library on any platform with a standards-compliant C compiler and the GNU autotools-chain (see the supported platforms).

The packages you need to install on the target platform are:

* C compiler (e.g. GNU C Compiler)
* GNU Autools Chain: autoconf, automake, libtool
* zlib-development package (stable version >= 1.2.0)
* openssl-development package(e.g. libssl-dev)

Once you installed the prerequisite packages use the standard hadoop pom.xml file and pass along the native flag to build the native hadoop library:

```
   $ mvn package -Pdist,native -DskipTests -Dtar
```

You should see the newly-built library in:

```
   $ hadoop-dist/target/hadoop-3.6.0-SNAPSHOT/lib/native
```

Please note the following:

* It is mandatory to install both the zlib and gzip development packages on the target platform in order to build the native hadoop library; however, for deployment it is sufficient to install just one package if you wish to use only one codec.
* It is necessary to have the correct 32/64 libraries for zlib, depending on the 32/64 bit jvm for the target platform, in order to build and deploy the native hadoop library.

## Runtime

The bin/hadoop script ensures that the native hadoop library is on the library path via the system property: `-Djava.library.path=<path>`

During runtime, check the hadoop log files for your MapReduce tasks.

* If everything is all right, then: `DEBUG util.NativeCodeLoader - Trying to load the custom-built native-hadoop library...` `INFO util.NativeCodeLoader - Loaded the native-hadoop library`
* If something goes wrong, then: `WARN util.NativeCodeLoader - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable`

## Check

NativeLibraryChecker is a tool to check whether native libraries are loaded correctly. You can launch NativeLibraryChecker as follows:

```
   $ hadoop checknative -a
   14/12/06 01:30:45 WARN bzip2.Bzip2Factory: Failed to load/initialize native-bzip2 library system-native, will use pure-Java version
   14/12/06 01:30:45 INFO zlib.ZlibFactory: Successfully loaded & initialized native-zlib library
   Native library checking:
   hadoop: true /home/ozawa/hadoop/lib/native/libhadoop.so.1.0.0
   zlib:   true /lib/x86_64-linux-gnu/libz.so.1
   zstd: true /usr/lib/libzstd.so.1
   lz4:    true revision:99
   bzip2:  false
```

## Native Shared Libraries

You can load any native shared library using DistributedCache for distributing and symlinking the library files.

This example shows you how to distribute a shared library in Unix-like systems, mylib.so, and load it from a MapReduce task.

1. First copy the library to the HDFS: `bin/hadoop fs -copyFromLocal libmyexample.so.1 /libraries/libmyexample.so.1`
2. The job launching program should contain the following: `DistributedCache.createSymlink(conf);` `DistributedCache.addCacheFile("hdfs://host:port/libraries/libmyexample.so.1#libmyexample.so", conf);`
3. The MapReduce task can contain: `System.loadLibrary("myexample");`

Note: If you downloaded or built the native hadoop library, you don’t need to use DistibutedCache to make the library available to your MapReduce tasks.

---
# Deprecated Properties

The following table lists the configuration property names that are deprecated in this version of Hadoop, and their replacements.

| **Deprecated property name** | **New property name** |
| --- | --- |
| create.empty.dir.if.nonexist | mapreduce.jobcontrol.createdir.ifnotexist |
| dfs.access.time.precision | dfs.namenode.accesstime.precision |
| dfs.backup.address | dfs.namenode.backup.address |
| dfs.backup.http.address | dfs.namenode.backup.http-address |
| dfs.balance.bandwidthPerSec | dfs.datanode.balance.bandwidthPerSec |
| dfs.block.size | dfs.blocksize |
| dfs.data.dir | dfs.datanode.data.dir |
| dfs.datanode.max.xcievers | dfs.datanode.max.transfer.threads |
| dfs.df.interval | fs.df.interval |
| dfs.encryption.key.provider.uri | hadoop.security.key.provider.path |
| dfs.federation.nameservice.id | dfs.nameservice.id |
| dfs.federation.nameservices | dfs.nameservices |
| dfs.http.address | dfs.namenode.http-address |
| dfs.https.address | dfs.namenode.https-address |
| dfs.https.client.keystore.resource | dfs.client.https.keystore.resource |
| dfs.https.need.client.auth | dfs.client.https.need-auth |
| dfs.max.objects | dfs.namenode.max.objects |
| dfs.max-repl-streams | dfs.namenode.replication.max-streams |
| dfs.name.dir | dfs.namenode.name.dir |
| dfs.name.dir.restore | dfs.namenode.name.dir.restore |
| dfs.name.edits.dir | dfs.namenode.edits.dir |
| dfs.permissions | dfs.permissions.enabled |
| dfs.permissions.supergroup | dfs.permissions.superusergroup |
| dfs.read.prefetch.size | dfs.client.read.prefetch.size |
| dfs.replication.considerLoad | dfs.namenode.redundancy.considerLoad |
| dfs.namenode.replication.considerLoad | dfs.namenode.redundancy.considerLoad |
| dfs.namenode.replication.considerLoad.factor | dfs.namenode.redundancy.considerLoad.factor |
| dfs.replication.interval | dfs.namenode.redundancy.interval |
| dfs.namenode.replication.interval | dfs.namenode.redundancy.interval |
| dfs.replication.min | dfs.namenode.replication.min |
| dfs.replication.pending.timeout.sec | dfs.namenode.reconstruction.pending.timeout-sec |
| dfs.namenode.replication.pending.timeout-sec | dfs.namenode.reconstruction.pending.timeout-sec |
| dfs.safemode.extension | dfs.namenode.safemode.extension |
| dfs.safemode.threshold.pct | dfs.namenode.safemode.threshold-pct |
| dfs.secondary.http.address | dfs.namenode.secondary.http-address |
| dfs.socket.timeout | dfs.client.socket-timeout |
| dfs.umaskmode | fs.permissions.umask-mode |
| dfs.web.ugi | hadoop.http.staticuser.user |
| dfs.write.packet.size | dfs.client-write-packet-size |
| fs.checkpoint.dir | dfs.namenode.checkpoint.dir |
| fs.checkpoint.edits.dir | dfs.namenode.checkpoint.edits.dir |
| fs.checkpoint.period | dfs.namenode.checkpoint.period |
| fs.default.name | fs.defaultFS |
| fs.s3a.server-side-encryption-key | fs.s3a.server-side-encryption.key |
| hadoop.configured.node.mapping | net.topology.configured.node.mapping |
| hadoop.native.lib | io.native.lib.available |
| hadoop.pipes.command-file.keep | mapreduce.pipes.commandfile.preserve |
| hadoop.pipes.executable.interpretor | mapreduce.pipes.executable.interpretor |
| hadoop.pipes.executable | mapreduce.pipes.executable |
| hadoop.pipes.java.mapper | mapreduce.pipes.isjavamapper |
| hadoop.pipes.java.recordreader | mapreduce.pipes.isjavarecordreader |
| hadoop.pipes.java.recordwriter | mapreduce.pipes.isjavarecordwriter |
| hadoop.pipes.java.reducer | mapreduce.pipes.isjavareducer |
| hadoop.pipes.partitioner | mapreduce.pipes.partitioner |
| heartbeat.recheck.interval | dfs.namenode.heartbeat.recheck-interval |
| httpfs.authentication.kerberos.keytab | hadoop.http.authentication.kerberos.keytab |
| httpfs.authentication.kerberos.principal | hadoop.http.authentication.kerberos.principal |
| httpfs.authentication.signature.secret.file | hadoop.http.authentication.signature.secret.file |
| httpfs.authentication.type | hadoop.http.authentication.type |
| io.bytes.per.checksum | dfs.bytes-per-checksum |
| io.sort.factor | mapreduce.task.io.sort.factor |
| io.sort.mb | mapreduce.task.io.sort.mb |
| io.sort.spill.percent | mapreduce.map.sort.spill.percent |
| jobclient.completion.poll.interval | mapreduce.client.completion.pollinterval |
| jobclient.output.filter | mapreduce.client.output.filter |
| jobclient.progress.monitor.poll.interval | mapreduce.client.progressmonitor.pollinterval |
| job.end.notification.url | mapreduce.job.end-notification.url |
| job.end.retry.attempts | mapreduce.job.end-notification.retry.attempts |
| job.end.retry.interval | mapreduce.job.end-notification.retry.interval |
| job.local.dir | mapreduce.job.local.dir |
| keep.failed.task.files | mapreduce.task.files.preserve.failedtasks |
| keep.task.files.pattern | mapreduce.task.files.preserve.filepattern |
| key.value.separator.in.input.line | mapreduce.input.keyvaluelinerecordreader.key.value.separator |
| map.input.file | mapreduce.map.input.file |
| map.input.length | mapreduce.map.input.length |
| map.input.start | mapreduce.map.input.start |
| map.output.key.field.separator | mapreduce.map.output.key.field.separator |
| map.output.key.value.fields.spec | mapreduce.fieldsel.map.output.key.value.fields.spec |
| mapred.acls.enabled | mapreduce.cluster.acls.enabled |
| mapred.binary.partitioner.left.offset | mapreduce.partition.binarypartitioner.left.offset |
| mapred.binary.partitioner.right.offset | mapreduce.partition.binarypartitioner.right.offset |
| mapred.cache.archives | mapreduce.job.cache.archives |
| mapred.cache.archives.timestamps | mapreduce.job.cache.archives.timestamps |
| mapred.cache.files | mapreduce.job.cache.files |
| mapred.cache.files.timestamps | mapreduce.job.cache.files.timestamps |
| mapred.cache.localArchives | mapreduce.job.cache.local.archives |
| mapred.cache.localFiles | mapreduce.job.cache.local.files |
| mapred.child.tmp | mapreduce.task.tmp.dir |
| mapred.cluster.map.memory.mb | mapreduce.cluster.mapmemory.mb |
| mapred.cluster.max.map.memory.mb | mapreduce.jobtracker.maxmapmemory.mb |
| mapred.cluster.max.reduce.memory.mb | mapreduce.jobtracker.maxreducememory.mb |
| mapred.cluster.reduce.memory.mb | mapreduce.cluster.reducememory.mb |
| mapred.committer.job.setup.cleanup.needed | mapreduce.job.committer.setup.cleanup.needed |
| mapred.compress.map.output | mapreduce.map.output.compress |
| mapred.data.field.separator | mapreduce.fieldsel.data.field.separator |
| mapred.debug.out.lines | mapreduce.task.debugout.lines |
| mapred.inmem.merge.threshold | mapreduce.reduce.merge.inmem.threshold |
| mapred.input.dir.formats | mapreduce.input.multipleinputs.dir.formats |
| mapred.input.dir.mappers | mapreduce.input.multipleinputs.dir.mappers |
| mapred.input.dir | mapreduce.input.fileinputformat.inputdir |
| mapred.input.pathFilter.class | mapreduce.input.pathFilter.class |
| mapred.jar | mapreduce.job.jar |
| mapred.job.classpath.archives | mapreduce.job.classpath.archives |
| mapred.job.classpath.files | mapreduce.job.classpath.files |
| mapred.job.id | mapreduce.job.id |
| mapred.job.map.memory.mb | mapreduce.map.memory.mb |
| mapred.job.name | mapreduce.job.name |
| mapred.job.priority | mapreduce.job.priority |
| mapred.job.queue.name | mapreduce.job.queuename |
| mapred.job.reduce.input.buffer.percent | mapreduce.reduce.input.buffer.percent |
| mapred.job.reduce.markreset.buffer.percent | mapreduce.reduce.markreset.buffer.percent |
| mapred.job.reduce.memory.mb | mapreduce.reduce.memory.mb |
| mapred.job.reduce.total.mem.bytes | mapreduce.reduce.memory.totalbytes |
| mapred.job.reuse.jvm.num.tasks | mapreduce.job.jvm.numtasks |
| mapred.job.shuffle.input.buffer.percent | mapreduce.reduce.shuffle.input.buffer.percent |
| mapred.job.shuffle.merge.percent | mapreduce.reduce.shuffle.merge.percent |
| mapred.job.tracker | mapreduce.jobtracker.address |
| mapred.job.tracker.persist.jobstatus.active | mapreduce.jobtracker.persist.jobstatus.active |
| mapred.job.tracker.retire.jobs | mapreduce.jobtracker.retirejobs |
| mapred.join.expr | mapreduce.join.expr |
| mapred.join.keycomparator | mapreduce.join.keycomparator |
| mapred.lazy.output.format | mapreduce.output.lazyoutputformat.outputformat |
| mapred.line.input.format.linespermap | mapreduce.input.lineinputformat.linespermap |
| mapred.linerecordreader.maxlength | mapreduce.input.linerecordreader.line.maxlength |
| mapred.local.dir | mapreduce.cluster.local.dir |
| mapred.map.child.env | mapreduce.map.env |
| mapred.map.child.java.opts | mapreduce.map.java.opts |
| mapred.map.child.log.level | mapreduce.map.log.level |
| mapred.map.max.attempts | mapreduce.map.maxattempts |
| mapred.map.output.compression.codec | mapreduce.map.output.compress.codec |
| mapred.mapoutput.key.class | mapreduce.map.output.key.class |
| mapred.mapoutput.value.class | mapreduce.map.output.value.class |
| mapred.mapper.regex.group | mapreduce.mapper.regexmapper..group |
| mapred.mapper.regex | mapreduce.mapper.regex |
| mapred.map.task.debug.script | mapreduce.map.debug.script |
| mapred.map.tasks | mapreduce.job.maps |
| mapred.map.tasks.speculative.execution | mapreduce.map.speculative |
| mapred.max.map.failures.percent | mapreduce.map.failures.maxpercent |
| mapred.max.reduce.failures.percent | mapreduce.reduce.failures.maxpercent |
| mapred.max.split.size | mapreduce.input.fileinputformat.split.maxsize |
| mapred.max.tracker.failures | mapreduce.job.maxtaskfailures.per.tracker |
| mapred.merge.recordsBeforeProgress | mapreduce.task.merge.progress.records |
| mapred.min.split.size | mapreduce.input.fileinputformat.split.minsize |
| mapred.min.split.size.per.node | mapreduce.input.fileinputformat.split.minsize.per.node |
| mapred.min.split.size.per.rack | mapreduce.input.fileinputformat.split.minsize.per.rack |
| mapred.output.compression.codec | mapreduce.output.fileoutputformat.compress.codec |
| mapred.output.compression.type | mapreduce.output.fileoutputformat.compress.type |
| mapred.output.compress | mapreduce.output.fileoutputformat.compress |
| mapred.output.dir | mapreduce.output.fileoutputformat.outputdir |
| mapred.output.key.class | mapreduce.job.output.key.class |
| mapred.output.key.comparator.class | mapreduce.job.output.key.comparator.class |
| mapred.output.value.class | mapreduce.job.output.value.class |
| mapred.output.value.groupfn.class | mapreduce.job.output.group.comparator.class |
| mapred.permissions.supergroup | mapreduce.cluster.permissions.supergroup |
| mapred.pipes.user.inputformat | mapreduce.pipes.inputformat |
| mapred.reduce.child.env | mapreduce.reduce.env |
| mapred.reduce.child.java.opts | mapreduce.reduce.java.opts |
| mapred.reduce.child.log.level | mapreduce.reduce.log.level |
| mapred.reduce.max.attempts | mapreduce.reduce.maxattempts |
| mapred.reduce.parallel.copies | mapreduce.reduce.shuffle.parallelcopies |
| mapred.reduce.slowstart.completed.maps | mapreduce.job.reduce.slowstart.completedmaps |
| mapred.reduce.task.debug.script | mapreduce.reduce.debug.script |
| mapred.reduce.tasks | mapreduce.job.reduces |
| mapred.reduce.tasks.speculative.execution | mapreduce.reduce.speculative |
| mapred.seqbinary.output.key.class | mapreduce.output.seqbinaryoutputformat.key.class |
| mapred.seqbinary.output.value.class | mapreduce.output.seqbinaryoutputformat.value.class |
| mapred.shuffle.connect.timeout | mapreduce.reduce.shuffle.connect.timeout |
| mapred.shuffle.read.timeout | mapreduce.reduce.shuffle.read.timeout |
| mapred.skip.attempts.to.start.skipping | mapreduce.task.skip.start.attempts |
| mapred.skip.map.auto.incr.proc.count | mapreduce.map.skip.proc-count.auto-incr |
| mapred.skip.map.max.skip.records | mapreduce.map.skip.maxrecords |
| mapred.skip.on | mapreduce.job.skiprecords |
| mapred.skip.out.dir | mapreduce.job.skip.outdir |
| mapred.skip.reduce.auto.incr.proc.count | mapreduce.reduce.skip.proc-count.auto-incr |
| mapred.skip.reduce.max.skip.groups | mapreduce.reduce.skip.maxgroups |
| mapred.speculative.execution.slowNodeThreshold | mapreduce.job.speculative.slownodethreshold |
| mapred.speculative.execution.slowTaskThreshold | mapreduce.job.speculative.slowtaskthreshold |
| mapred.speculative.execution.speculativeCap | mapreduce.job.speculative.speculativecap |
| mapred.submit.replication | mapreduce.client.submit.file.replication |
| mapred.system.dir | mapreduce.jobtracker.system.dir |
| mapred.task.cache.levels | mapreduce.jobtracker.taskcache.levels |
| mapred.task.id | mapreduce.task.attempt.id |
| mapred.task.is.map | mapreduce.task.ismap |
| mapred.task.partition | mapreduce.task.partition |
| mapred.task.profile | mapreduce.task.profile |
| mapred.task.profile.maps | mapreduce.task.profile.maps |
| mapred.task.profile.params | mapreduce.task.profile.params |
| mapred.task.profile.reduces | mapreduce.task.profile.reduces |
| mapred.task.timeout | mapreduce.task.timeout |
| mapred.tasktracker.indexcache.mb | mapreduce.reduce.shuffle.indexcache.mb |
| mapreduce.tasktracker.indexcache.mb | mapreduce.reduce.shuffle.indexcache.mb |
| mapred.tasktracker.map.tasks.maximum | mapreduce.tasktracker.map.tasks.maximum |
| mapred.tasktracker.memory\_calculator\_plugin | mapreduce.tasktracker.resourcecalculatorplugin |
| mapred.tasktracker.memorycalculatorplugin | mapreduce.tasktracker.resourcecalculatorplugin |
| mapred.temp.dir | mapreduce.cluster.temp.dir |
| mapred.text.key.comparator.options | mapreduce.partition.keycomparator.options |
| mapred.text.key.partitioner.options | mapreduce.partition.keypartitioner.options |
| mapred.textoutputformat.separator | mapreduce.output.textoutputformat.separator |
| mapred.tip.id | mapreduce.task.id |
| mapreduce.combine.class | mapreduce.job.combine.class |
| mapreduce.inputformat.class | mapreduce.job.inputformat.class |
| mapreduce.job.counters.limit | mapreduce.job.counters.max |
| mapreduce.map.class | mapreduce.job.map.class |
| mapreduce.outputformat.class | mapreduce.job.outputformat.class |
| mapreduce.partitioner.class | mapreduce.job.partitioner.class |
| mapreduce.reduce.class | mapreduce.job.reduce.class |
| mapred.used.genericoptionsparser | mapreduce.client.genericoptionsparser.used |
| mapred.userlog.limit.kb | mapreduce.task.userlog.limit.kb |
| mapred.working.dir | mapreduce.job.working.dir |
| mapred.work.output.dir | mapreduce.task.output.dir |
| min.num.spills.for.combine | mapreduce.map.combine.minspills |
| reduce.output.key.value.fields.spec | mapreduce.fieldsel.reduce.output.key.value.fields.spec |
| security.job.submission.protocol.acl | security.job.client.protocol.acl |
| security.task.umbilical.protocol.acl | security.job.task.protocol.acl |
| sequencefile.filter.class | mapreduce.input.sequencefileinputfilter.class |
| sequencefile.filter.frequency | mapreduce.input.sequencefileinputfilter.frequency |
| sequencefile.filter.regex | mapreduce.input.sequencefileinputfilter.regex |
| session.id | dfs.metrics.session-id |
| slave.host.name | dfs.datanode.hostname |
| topology.node.switch.mapping.impl | net.topology.node.switch.mapping.impl |
| topology.script.file.name | net.topology.script.file.name |
| topology.script.number.args | net.topology.script.number.args |
| user.name | mapreduce.job.user.name |
| yarn.app.mapreduce.yarn.app.mapreduce.client-am.ipc.max-retries-on-timeouts | yarn.app.mapreduce.client-am.ipc.max-retries-on-timeouts |
| yarn.client.app-submission.poll-interval | yarn.client.application-client-protocol.poll-timeout-ms |

The following table lists additional changes to some configuration properties:

| **Deprecated property name** | **New property name** |
| --- | --- |
| mapred.create.symlink | NONE - symlinking is always on |
| mapreduce.job.cache.symlink.create | NONE - symlinking is always on |
| io.native.lib.available | NONE - Always use native libraries if available. |

---
# Fair Call Queue Guide

* [Purpose](#Purpose)
* [Prerequisites](#Prerequisites)
* [Overview](#Overview)
* [Design Details](#Design_Details)
  * [Cost-based Fair Call Queue](#Cost-based_Fair_Call_Queue)
* [Configuration](#Configuration)
  * [Configuration Prefixes](#Configuration_Prefixes)
  * [Full List of Configurations](#Full_List_of_Configurations)
  * [Example Configuration](#Example_Configuration)

## Purpose

This document describes how to configure and manage the Fair Call Queue for Hadoop.

## Prerequisites

Make sure Hadoop is installed, configured and setup correctly. For more information see:

* [Single Node Setup](./SingleCluster.html) for first-time users.
* [Cluster Setup](./ClusterSetup.html) for large, distributed clusters.

## Overview

Hadoop server components, in particular the HDFS NameNode, experience very heavy RPC load from clients. By default, all client requests are routed through a first-in, first-out queue and serviced in the order they arrive. This means that a single user submitting a very large number of requests can easily overwhelm the service, causing degraded service for all other users. The Fair Call Queue, and related components, aim to mitigate this impact.

## Design Details

There are a few components in the IPC stack which have a complex interplay, each with their own tuning parameters. The image below presents a schematic overview of their interactions, which will be explained below.

![FairCallQueue Overview](assets/hadoop_hadoop-project-dist_hadoop-common_images_faircallqueue-overview.png)

In the following explanation, **bolded** words refer to named entities or configurables.

When a client makes a request to an IPC server, this request first lands in a **listen queue**. **Reader** threads remove requests from this queue and pass them to a configurable **RpcScheduler** to be assigned a priority and placed into a **call queue**; this is where FairCallQueue sits as a pluggable implementation (the other existing implementation being a FIFO queue). **Handler** threads accept requests out of the call queue, process them, and respond to the client.

The implementation of RpcScheduler used with FairCallQueue by default is **DecayRpcScheduler**, which maintains a count of requests received for each user. This count *decays* over time; every **sweep period** (5s by default), the number of requests per user is multiplied by a **decay factor** (0.5 by default). This maintains a weighted/rolling average of request count per user. Every time that a sweep is performed, the call counts for all known users are ranked from highest to lowest. Each user is assigned a **priority** (0-3 by default, with 0 being highest priority) based on the proportion of calls originating from that user. The default **priority thresholds** are (0.125, 0.25, 0.5), meaning that users whose calls make up more than 50% of the total (there can be at most one such user) are placed into the lowest priority, users whose calls make up between 25% and 50% of the total are in the 2nd lowest, users whose calls make up between 12.5% and 25% are in the 2nd highest priority, and all other users are placed in the highest priority. At the end of the sweep, each known user has a cached priority which will be used until the next sweep; new users which appear between sweeps will have their priority calculated on-the-fly.

Within FairCallQueue, there are multiple **priority queues**, each of which is designated a **weight**. When a request arrives at the call queue, the request is placed into one of these priority queues based on the current priority assigned to the call (by the RpcScheduler). When a handler thread attempts to fetch an item from the call queue, which queue it pulls from is decided via an **RpcMultiplexer**; currently this is hard-coded to be a **WeightedRoundRobinMultiplexer**. The WRRM serves requests from queues based on their weights; the default weights for the default 4 priority levels are (8, 4, 2, 1). Thus, the WRRM would serve 8 requests from the highest priority queue, 4 from the second highest, 2 from the third highest, 1 from the lowest, then serve 8 more from the highest priority queue, and so on.

In addition to the priority-weighting mechanisms discussed above, there is also a configurable **backoff** mechanism, in which the server will throw an exception to the client rather than handling it; the client is expected to wait some time (i.e., via exponential backoff) before trying again. Typically, backoff is triggered when a request is attempted to be placed in a priority queue (of FCQ) when that queue is full. This helps to push back further on impactful clients, reducing load, and can have substantial benefit. There is also a feature, **backoff by response time**, which will cause requests in lower priority levels to back off if requests in higher priority levels are being serviced too slowly. For example, if the response time threshold for priority 1 is set to be 10 seconds, but the average response time in that queue is 12 seconds, an incoming request at priority levels 2 or lower would receive a backoff exception, while requests at priority levels 0 and 1 would proceed as normal. The intent is to force heavier clients to back off when overall system load is heavy enough to cause high priority clients to be impacted.

The discussion above refers to the **user** of a request when discussing how to group together requests for throttling. This is configurable via the **identity provider**, which defaults to the **UserIdentityProvider**. The user identity provider simply uses the username of the client submitting the request. However, a custom identity provider can be used to performing throttling based on other groupings, or using an external identity provider.

If particular users submit important requests and you don’t want to limit them, you can set them up as the **service-users**. They are always scheduled into the high-priority queue and won’t be included in the priority computation of normal user calls.

### Cost-based Fair Call Queue

Though the fair call queue itself does a good job of mitigating the impact from users who submit a very high *number* of requests, it does not take account into how expensive each request is to process. Thus, when considering the HDFS NameNode, a user who submits 1000 “getFileInfo” requests would be prioritized the same as a user who submits 1000 “listStatus” requests on some very large directory, or a user who submits 1000 “mkdir” requests, which are more expensive as they require an exclusive lock on the namesystem. To account for the *cost* of an operation when considering the prioritization of user requests, there is a “cost-based” extension to the Fair Call Queue which uses the aggregate processing time of a user’s operations to determine how that user should be prioritized. By default, queue time (time spent waiting to be processed) and lock wait time (time spent waiting to acquire a lock) is not considered in the cost, time spent processing without a lock is neutrally (1x) weighted, time spent processing with a shared lock is weighted 10x higher, and time spent processing with an exclusive lock is weighted 100x higher. This attempts to prioritize users based on the actual load they place on the server. To enable this feature, set the `costprovder.impl` configuration to `org.apache.hadoop.ipc.WeightedTimeCostProvider` as described below.

## Configuration

This section describes how to configure the fair call queue.

### Configuration Prefixes

All call queue-related configurations are relevant to only a single IPC server. This allows for a single configuration file to be used to configure different components, or even different IPC servers within a component, to have uniquely configured call queues. Each configuration is prefixed with `ipc.<port_number>`, where `<port_number>` is the port used by the IPC server to be configured. For example, `ipc.8020.callqueue.impl` will adjust the call queue implementation for the IPC server running at port 8020. For the remainder of this section, this prefix will be omitted.

### Full List of Configurations

| Configuration Key | Applicable Component | Description | Default |
| --- | --- | --- | --- |
| backoff.enable | General | Whether or not to enable client backoff when a queue is full. | false |
| callqueue.impl | General | The fully qualified name of a class to use as the implementation of a call queue. Use `org.apache.hadoop.ipc.FairCallQueue` for the Fair Call Queue. | `java.util.concurrent.LinkedBlockingQueue` (FIFO queue) |
| callqueue.capacity.weights | General | The capacity allocation weights among all subqueues. A postive int array whose length is equal to the `scheduler.priority.levels` is expected where each int is the relative weight out of total capacity. i.e. if a queue with capacity weight `w`, its queue capacity is `capacity * w/sum(weights)` |
| scheduler.impl | General | The fully qualified name of a class to use as the implementation of the scheduler. Use `org.apache.hadoop.ipc.DecayRpcScheduler` in conjunction with the Fair Call Queue. | `org.apache.hadoop.ipc.DefaultRpcScheduler` (no-op scheduler)   If using FairCallQueue, defaults to `org.apache.hadoop.ipc.DecayRpcScheduler` |
| scheduler.priority.levels | RpcScheduler, CallQueue | How many priority levels to use within the scheduler and call queue. | 4 |
| faircallqueue.multiplexer.weights | WeightedRoundRobinMultiplexer | How much weight to give to each priority queue. This should be a comma-separated list of length equal to the number of priority levels. | Weights descend by a factor of 2 (e.g., for 4 levels: `8,4,2,1`) |
| identity-provider.impl | DecayRpcScheduler | The identity provider mapping user requests to their identity. | org.apache.hadoop.ipc.UserIdentityProvider |
| cost-provider.impl | DecayRpcScheduler | The cost provider mapping user requests to their cost. To enable determination of cost based on processing time, use `org.apache.hadoop.ipc.WeightedTimeCostProvider`. | org.apache.hadoop.ipc.DefaultCostProvider |
| decay-scheduler.period-ms | DecayRpcScheduler | How frequently the decay factor should be applied to the operation counts of users. Higher values have less overhead, but respond less quickly to changes in client behavior. | 5000 |
| decay-scheduler.decay-factor | DecayRpcScheduler | When decaying the operation counts of users, the multiplicative decay factor to apply. Higher values will weight older operations more strongly, essentially giving the scheduler a longer memory, and penalizing heavy clients for a longer period of time. | 0.5 |
| decay-scheduler.thresholds | DecayRpcScheduler | The client load threshold, as an integer percentage, for each priority queue. Clients producing less load, as a percent of total operations, than specified at position *i* will be given priority *i*. This should be a comma-separated list of length equal to the number of priority levels minus 1 (the last is implicitly 100). | Thresholds ascend by a factor of 2 (e.g., for 4 levels: `13,25,50`) |
| decay-scheduler.backoff.responsetime.enable | DecayRpcScheduler | Whether or not to enable the backoff by response time feature. | false |
| decay-scheduler.backoff.responsetime.thresholds | DecayRpcScheduler | The response time thresholds, as time durations, for each priority queue. If the average response time for a queue is above this threshold, backoff will occur in lower priority queues. This should be a comma-separated list of length equal to the number of priority levels. | Threshold increases by 10s per level (e.g., for 4 levels: `10s,20s,30s,40s`) |
| decay-scheduler.metrics.top.user.count | DecayRpcScheduler | The number of top (i.e., heaviest) users to emit metric information about. | 10 |
| decay-scheduler.service-users | DecayRpcScheduler | Service users will always be scheduled into the highest-priority queue and won’t be included in the priority computation of normal user calls. They are specified as a comma-separated list. |  |
| weighted-cost.lockshared | WeightedTimeCostProvider | The weight multiplier to apply to the time spent in the processing phase which holds a shared (read) lock. | 10 |
| weighted-cost.lockexclusive | WeightedTimeCostProvider | The weight multiplier to apply to the time spent in the processing phase which holds an exclusive (write) lock. | 100 |
| weighted-cost.{handler,lockfree,response} | WeightedTimeCostProvider | The weight multiplier to apply to the time spent in the processing phases which do not involve holding a lock. See `org.apache.hadoop.ipc.ProcessingDetails.Timing` for more details on each phase. | 1 |

### Example Configuration

This is an example of configuration an IPC server at port 8020 to use `FairCallQueue` with the `DecayRpcScheduler` and only 2 priority levels. The heaviest 10% of users are penalized heavily, given only 1% of the total requests processed.

```
<property>
     <name>ipc.8020.callqueue.impl</name>
     <value>org.apache.hadoop.ipc.FairCallQueue</value>
</property>
<property>
     <name>ipc.8020.callqueue.capacity.weights</name>
     <value>7,3</value>
</property>
<property>
     <name>ipc.8020.scheduler.impl</name>
     <value>org.apache.hadoop.ipc.DecayRpcScheduler</value>
</property>
<property>
     <name>ipc.8020.scheduler.priority.levels</name>
     <value>2</value>
</property>
<property>
     <name>ipc.8020.faircallqueue.multiplexer.weights</name>
     <value>99,1</value>
</property>
<property>
     <name>ipc.8020.decay-scheduler.thresholds</name>
     <value>90</value>
</property>
```

---
# Hadoop Commands Guide

* [Overview](#Overview)
  * [Shell Options](#Shell_Options)
  * [Generic Options](#Generic_Options)
* [User Commands](#User_Commands)
  * [archive](#archive)
  * [checknative](#checknative)
  * [classpath](#classpath)
  * [conftest](#conftest)
  * [credential](#credential)
  * [distch](#distch)
  * [distcp](#distcp)
  * [dtutil](#dtutil)
  * [fs](#fs)
  * [gridmix](#gridmix)
  * [jar](#jar)
  * [jnipath](#jnipath)
  * [kerbname](#kerbname)
  * [kdiag](#kdiag)
  * [key](#key)
  * [kms](#kms)
  * [version](#version)
  * [CLASSNAME](#CLASSNAME)
  * [envvars](#envvars)
* [Administration Commands](#Administration_Commands)
  * [daemonlog](#daemonlog)
* [Files](#Files)
  * [etc/hadoop/hadoop-env.sh](#etc.2Fhadoop.2Fhadoop-env.sh)
  * [etc/hadoop/hadoop-user-functions.sh](#etc.2Fhadoop.2Fhadoop-user-functions.sh)
  * [~/.hadooprc](#a.7E.2F.hadooprc)

## Overview

All of the Hadoop commands and subprojects follow the same basic structure:

Usage: `shellcommand [SHELL_OPTIONS] [COMMAND] [GENERIC_OPTIONS] [COMMAND_OPTIONS]`

| FIELD | Description |
| --- | --- |
| shellcommand | The command of the project being invoked. For example, Hadoop common uses `hadoop`, HDFS uses `hdfs`, and YARN uses `yarn`. |
| SHELL\_OPTIONS | Options that the shell processes prior to executing Java. |
| COMMAND | Action to perform. |
| GENERIC\_OPTIONS | The common set of options supported by multiple commands. |
| COMMAND\_OPTIONS | Various commands with their options are described in this documention for the Hadoop common sub-project. HDFS and YARN are covered in other documents. |

### Shell Options

All of the shell commands will accept a common set of options. For some commands, these options are ignored. For example, passing `---hostnames` on a command that only executes on a single host will be ignored.

| SHELL\_OPTION | Description |
| --- | --- |
| `--buildpaths` | Enables developer versions of jars. |
| `--config confdir` | Overwrites the default Configuration directory. Default is `$HADOOP_HOME/etc/hadoop`. |
| `--daemon mode` | If the command supports daemonization (e.g., `hdfs namenode`), execute in the appropriate mode. Supported modes are `start` to start the process in daemon mode, `stop` to stop the process, and `status` to determine the active status of the process. `status` will return an [LSB-compliant](http://refspecs.linuxbase.org/LSB_3.0.0/LSB-generic/LSB-generic/iniscrptact.html) result code. If no option is provided, commands that support daemonization will run in the foreground. For commands that do not support daemonization, this option is ignored. |
| `--debug` | Enables shell level configuration debugging information |
| `--help` | Shell script usage information. |
| `--hostnames` | When `--workers` is used, override the workers file with a space delimited list of hostnames where to execute a multi-host subcommand. If `--workers` is not used, this option is ignored. |
| `--hosts` | When `--workers` is used, override the workers file with another file that contains a list of hostnames where to execute a multi-host subcommand. If `--workers` is not used, this option is ignored. |
| `--loglevel loglevel` | Overrides the log level. Valid log levels are FATAL, ERROR, WARN, INFO, DEBUG, and TRACE. Default is INFO. |
| `--workers` | If possible, execute this command on all hosts in the `workers` file. |

### Generic Options

Many subcommands honor a common set of configuration options to alter their behavior:

| GENERIC\_OPTION | Description |
| --- | --- |
| `-archives <comma separated list of archives>` | Specify comma separated archives to be unarchived on the compute machines. Applies only to job. |
| `-conf <configuration file>` | Specify an application configuration file. |
| `-D <property>=<value>` | Use value for given property. |
| `-files <comma separated list of files>` | Specify comma separated files to be copied to the map reduce cluster. Applies only to job. |
| `-fs <file:///> or <hdfs://namenode:port>` | Specify default filesystem URL to use. Overrides ‘fs.defaultFS’ property from configurations. |
| `-jt <local> or <resourcemanager:port>` | Specify a ResourceManager. Applies only to job. |
| `-libjars <comma separated list of jars>` | Specify comma separated jar files to include in the classpath. Applies only to job. |

# Hadoop Common Commands

All of these commands are executed from the `hadoop` shell command. They have been broken up into [User Commands](#User_Commands) and [Administration Commands](#Administration_Commands).

## User Commands

Commands useful for users of a hadoop cluster.

### `archive`

Creates a hadoop archive. More information can be found at [Hadoop Archives Guide](../../hadoop-archives/HadoopArchives.html).

### `checknative`

Usage: `hadoop checknative [-a] [-h]`

| COMMAND\_OPTION | Description |
| --- | --- |
| `-a` | Check all libraries are available. |
| `-h` | print help |

This command checks the availability of the Hadoop native code. See [Native Libaries](./NativeLibraries.html) for more information. By default, this command only checks the availability of libhadoop.

### `classpath`

Usage: `hadoop classpath [--glob |--jar <path> |-h |--help]`

| COMMAND\_OPTION | Description |
| --- | --- |
| `--glob` | expand wildcards |
| `--jar` *path* | write classpath as manifest in jar named *path* |
| `-h`, `--help` | print help |

Prints the class path needed to get the Hadoop jar and the required libraries. If called without arguments, then prints the classpath set up by the command scripts, which is likely to contain wildcards in the classpath entries. Additional options print the classpath after wildcard expansion or write the classpath into the manifest of a jar file. The latter is useful in environments where wildcards cannot be used and the expanded classpath exceeds the maximum supported command line length.

### `conftest`

Usage: `hadoop conftest [-conffile <path>]...`

| COMMAND\_OPTION | Description |
| --- | --- |
| `-conffile` | Path of a configuration file or directory to validate |
| `-h`, `--help` | print help |

Validates configuration XML files. If the `-conffile` option is not specified, the files in `${HADOOP_CONF_DIR}` whose name end with .xml will be verified. If specified, that path will be verified. You can specify either a file or directory, and if a directory specified, the files in that directory whose name end with `.xml` will be verified. You can specify `-conffile` option multiple times.

The validation is fairly minimal: the XML is parsed and duplicate and empty property names are checked for. The command does not support XInclude; if you using that to pull in configuration items, it will declare the XML file invalid.

### `credential`

Usage: `hadoop credential <subcommand> [options]`

| COMMAND\_OPTION | Description |
| --- | --- |
| create *alias* [-provider *provider-path*] [-strict] [-value *credential-value*] | Prompts the user for a credential to be stored as the given alias. The *hadoop.security.credential.provider.path* within the core-site.xml file will be used unless a `-provider` is indicated. The `-strict` flag will cause the command to fail if the provider uses a default password. Use `-value` flag to supply the credential value (a.k.a. the alias password) instead of being prompted. |
| delete *alias* [-provider *provider-path*] [-strict] [-f] | Deletes the credential with the provided alias. The *hadoop.security.credential.provider.path* within the core-site.xml file will be used unless a `-provider` is indicated. The `-strict` flag will cause the command to fail if the provider uses a default password. The command asks for confirmation unless `-f` is specified |
| list [-provider *provider-path*] [-strict] | Lists all of the credential aliases The *hadoop.security.credential.provider.path* within the core-site.xml file will be used unless a `-provider` is indicated. The `-strict` flag will cause the command to fail if the provider uses a default password. |
| check *alias* [-provider *provider-path*] [-strict] | Check the password for the given alias. The *hadoop.security.credential.provider.path* within the core-site.xml file will be used unless a `-provider` is indicated. The `-strict` flag will cause the command to fail if the provider uses a default password. |

Command to manage credentials, passwords and secrets within credential providers.

The CredentialProvider API in Hadoop allows for the separation of applications and how they store their required passwords/secrets. In order to indicate a particular provider type and location, the user must provide the *hadoop.security.credential.provider.path* configuration element in core-site.xml or use the command line option `-provider` on each of the following commands. This provider path is a comma-separated list of URLs that indicates the type and location of a list of providers that should be consulted. For example, the following path: `user:///,jceks://file/tmp/test.jceks,jceks://hdfs@nn1.example.com/my/path/test.jceks`

indicates that the current user’s credentials file should be consulted through the User Provider, that the local file located at `/tmp/test.jceks` is a Java Keystore Provider and that the file located within HDFS at `nn1.example.com/my/path/test.jceks` is also a store for a Java Keystore Provider.

When utilizing the credential command it will often be for provisioning a password or secret to a particular credential store provider. In order to explicitly indicate which provider store to use the `-provider` option should be used. Otherwise, given a path of multiple providers, the first non-transient provider will be used. This may or may not be the one that you intended.

Providers frequently require that a password or other secret is supplied. If the provider requires a password and is unable to find one, it will use a default password and emit a warning message that the default password is being used. If the `-strict` flag is supplied, the warning message becomes an error message and the command returns immediately with an error status.

Example: `hadoop credential list -provider jceks://file/tmp/test.jceks`

### `distch`

Usage: `hadoop distch [-f urilist_url] [-i] [-log logdir] path:owner:group:permissions`

| COMMAND\_OPTION | Description |
| --- | --- |
| `-f` | List of objects to change |
| `-i` | Ignore failures |
| `-log` | Directory to log output |

Change the ownership and permissions on many files at once.

### `distcp`

Copy file or directories recursively. More information can be found at [Hadoop DistCp Guide](../../hadoop-distcp/DistCp.html).

### `dtutil`

Usage: `hadoop dtutil [-keytab` *keytab\_file* `-principal` *principal\_name* `]` *subcommand* `[-format (java|protobuf)] [-alias` *alias* `] [-renewer` *renewer* `]` *filename…*

Utility to fetch and manage hadoop delegation tokens inside credentials files. It is intended to replace the simpler command `fetchdt`. There are multiple subcommands, each with their own flags and options.

For every subcommand that writes out a file, the `-format` option will specify the internal format to use. `java` is the legacy format that matches `fetchdt`. The default is `protobuf`.

For every subcommand that connects to a service, convenience flags are provided to specify the kerberos principal name and keytab file to use for auth.

| SUBCOMMAND | Description |
| --- | --- |
| `print`     `[-alias` *alias* `]`     *filename* `[` *filename2* `...]` | Print out the fields in the tokens contained in *filename* (and *filename2* …).   If *alias* is specified, print only tokens matching *alias*. Otherwise, print all tokens. |
| `get` *URL*     `[-service` *scheme* `]`     `[-format (java|protobuf)]`     `[-alias` *alias* `]`     `[-renewer` *renewer* `]`     *filename* | Fetch a token from service at *URL* and place it in *filename*.   *URL* is required and must immediately follow `get`.  *URL* is the service URL, e.g. *hdfs://localhost:9000*.   *alias* will overwrite the service field in the token.   It is intended for hosts that have external and internal names, e.g. *firewall.com:14000*.   *filename* should come last and is the name of the token file.   It will be created if it does not exist. Otherwise, token(s) are added to existing file.   The `-service` flag should only be used with a URL which starts with `http` or `https`.   The following are equivalent: *hdfs://localhost:9000/* vs. *http://localhost:9000* `-service` *hdfs* |
| `append`     `[-format (java|protobuf)]`     *filename* *filename2* `[` *filename3* `...]` | Append the contents of the first N filenames onto the last filename.   When tokens with common service fields are present in multiple files, earlier files’ tokens are overwritten.   That is, tokens present in the last file are always preserved. |
| `remove -alias` *alias*     `[-format (java|protobuf)]`     *filename* `[` *filename2* `...]` | From each file specified, remove the tokens matching *alias* and write out each file using specified format.   *alias* must be specified. |
| `cancel -alias` *alias*     `[-format (java|protobuf)]`     *filename* `[` *filename2* `...]` | Just like `remove`, except the tokens are also cancelled using the service specified in the token object.   *alias* must be specified. |
| `renew -alias` *alias*     `[-format (java|protobuf)]`     *filename* `[` *filename2* `...]` | For each file specified, renew the tokens matching *alias* and write out each file using specified format.   *alias* must be specified. |
| `import` *base64*     `[-alias` *alias* `]`     *filename* | Import a token from a base64 token.   *alias* will overwrite the service field in the token. |

### `fs`

This command is documented in the [File System Shell Guide](./FileSystemShell.html). It is a synonym for `hdfs dfs` when HDFS is in use.

### `gridmix`

Gridmix is a benchmark tool for Hadoop cluster. More information can be found in the [Gridmix Guide](../../hadoop-gridmix/GridMix.html).

### `jar`

Usage: `hadoop jar <jar> [mainClass] args...`

Runs a jar file.

Use [`yarn jar`](../../hadoop-yarn/hadoop-yarn-site/YarnCommands.html#jar) to launch YARN applications instead.

### `jnipath`

Usage: `hadoop jnipath`

Print the computed java.library.path.

### `kerbname`

Usage: `hadoop kerbname principal`

Convert the named principal via the auth\_to\_local rules to the Hadoop user name.

Example: `hadoop kerbname user@EXAMPLE.COM`

### `kdiag`

Usage: `hadoop kdiag`

Diagnose Kerberos Problems

### `key`

Usage: `hadoop key <subcommand> [options]`

| COMMAND\_OPTION | Description |
| --- | --- |
| create *keyname* [-cipher *cipher*] [-size *size*] [-description *description*] [-attr *attribute=value*] [-provider *provider*] [-strict] [-help] | Creates a new key for the name specified by the *keyname* argument within the provider specified by the `-provider` argument. The `-strict` flag will cause the command to fail if the provider uses a default password. You may specify a cipher with the `-cipher` argument. The default cipher is currently “AES/CTR/NoPadding”. The default keysize is 128. You may specify the requested key length using the `-size` argument. Arbitrary attribute=value style attributes may be specified using the `-attr` argument. `-attr` may be specified multiple times, once per attribute. |
| roll *keyname* [-provider *provider*] [-strict] [-help] | Creates a new version for the specified key within the provider indicated using the `-provider` argument. The `-strict` flag will cause the command to fail if the provider uses a default password. |
| delete *keyname* [-provider *provider*] [-strict] [-f] [-help] | Deletes all versions of the key specified by the *keyname* argument from within the provider specified by `-provider`. The `-strict` flag will cause the command to fail if the provider uses a default password. The command asks for user confirmation unless `-f` is specified. |
| list [-provider *provider*] [-strict] [-metadata] [-help] | Displays the keynames contained within a particular provider as configured in core-site.xml or specified with the `-provider` argument. The `-strict` flag will cause the command to fail if the provider uses a default password. `-metadata` displays the metadata. |
| check *keyname* [-provider *provider*] [-strict] [-help] | Check password of the *keyname* contained within a particular provider as configured in core-site.xml or specified with the `-provider` argument. The `-strict` flag will cause the command to fail if the provider uses a default password. |

| -help | Prints usage of this command |

Manage keys via the KeyProvider. For details on KeyProviders, see the [Transparent Encryption Guide](../hadoop-hdfs/TransparentEncryption.html).

Providers frequently require that a password or other secret is supplied. If the provider requires a password and is unable to find one, it will use a default password and emit a warning message that the default password is being used. If the `-strict` flag is supplied, the warning message becomes an error message and the command returns immediately with an error status.

NOTE: Some KeyProviders (e.g. org.apache.hadoop.crypto.key.JavaKeyStoreProvider) do not support uppercase key names.

NOTE: Some KeyProviders do not directly execute a key deletion (e.g. performs a soft-delete instead, or delay the actual deletion, to prevent mistake). In these cases, one may encounter errors when creating/deleting a key with the same name after deleting it. Please check the underlying KeyProvider for details.

### `kms`

Usage: `hadoop kms`

Run KMS, the Key Management Server.

### `version`

Usage: `hadoop version`

Prints the version.

### `CLASSNAME`

Usage: `hadoop CLASSNAME`

Runs the class named `CLASSNAME`. The class must be part of a package.

### `envvars`

Usage: `hadoop envvars`

Display computed Hadoop environment variables.

## Administration Commands

Commands useful for administrators of a hadoop cluster.

### `daemonlog`

Usage:

```
hadoop daemonlog -getlevel <host:port> <classname> [-protocol (http|https)]
hadoop daemonlog -setlevel <host:port> <classname> <level> [-protocol (http|https)]
```

| COMMAND\_OPTION | Description |
| --- | --- |
| `-getlevel` *host:port* *classname* [-protocol (http|https)] | Prints the log level of the log identified by a qualified *classname*, in the daemon running at *host:port*. The `-protocol` flag specifies the protocol for connection. |
| `-setlevel` *host:port* *classname* *level* [-protocol (http|https)] | Sets the log level of the log identified by a qualified *classname*, in the daemon running at *host:port*. The `-protocol` flag specifies the protocol for connection. |

Get/Set the log level for a Log identified by a qualified class name in the daemon dynamically. By default, the command sends a HTTP request, but this can be overridden by using argument `-protocol https` to send a HTTPS request.

Example:

```
$ bin/hadoop daemonlog -setlevel 127.0.0.1:9870 org.apache.hadoop.hdfs.server.namenode.NameNode DEBUG
$ bin/hadoop daemonlog -getlevel 127.0.0.1:9871 org.apache.hadoop.hdfs.server.namenode.NameNode -protocol https
```

Note that the setting is not permanent and will be reset when the daemon is restarted. This command works by sending a HTTP/HTTPS request to the daemon’s internal Jetty servlet, so it supports the following daemons:

* Common
  * key management server
* HDFS
  * name node
  * secondary name node
  * data node
  * journal node
  * HttpFS server
* YARN
  * resource manager
  * node manager
  * Timeline server

## Files

### **etc/hadoop/hadoop-env.sh**

This file stores the global settings used by all Hadoop shell commands.

### **etc/hadoop/hadoop-user-functions.sh**

This file allows for advanced users to override some shell functionality.

### **~/.hadooprc**

This stores the personal environment for an individual user. It is processed after the hadoop-env.sh and hadoop-user-functions.sh files and can contain the same settings.

---
# Hadoop Interface Taxonomy: Audience and Stability Classification

* [Motivation](#Motivation)
* [Interface Classification](#Interface_Classification)
  * [Audience](#Audience)
    * [Private](#Private)
    * [Limited-Private](#Limited-Private)
    * [Public](#Public)
  * [Change Compatibility](#Change_Compatibility)
  * [Stability](#Stability)
    * [Stable](#Stable)
    * [Evolving](#Evolving)
    * [Unstable](#Unstable)
    * [Deprecated](#Deprecated)
* [How are the Classifications Recorded?](#How_are_the_Classifications_Recorded.3F)
* [FAQ](#FAQ)

## Motivation

The interface taxonomy classification provided here is for guidance to developers and users of interfaces. The classification guides a developer to declare the targeted audience or users of an interface and also its stability.

* Benefits to the user of an interface: Knows which interfaces to use or not use and their stability.
* Benefits to the developer: to prevent accidental changes of interfaces and hence accidental impact on users or other components or system. This is particularly useful in large systems with many developers who may not all have a shared state/history of the project.

## Interface Classification

Hadoop adopts the following interface classification, this classification was derived from the OpenSolaris taxonomy and, to some extent, from taxonomy used inside Yahoo. Interfaces have two main attributes: Audience and Stability.

### Audience

Audience denotes the potential consumers of the interface. While many interfaces are internal/private to the implementation, other are public/external interfaces that are meant for wider consumption by applications and/or clients. For example, in posix, libc is an external or public interface, while large parts of the kernel are internal or private interfaces. Also, some interfaces are targeted towards other specific subsystems.

Identifying the audience of an interface helps define the impact of breaking it. For instance, it might be okay to break the compatibility of an interface whose audience is a small number of specific subsystems. On the other hand, it is probably not okay to break a protocol interface that millions of Internet users depend on.

Hadoop uses the following kinds of audience in order of increasing/wider visibility:

> Hadoop doesn’t have a Company-Private classification, which is meant for APIs which are intended to be used by other projects within the company, since it doesn’t apply to opensource projects. Also, certain APIs are annotated as @VisibleForTesting (from com.google.common .annotations.VisibleForTesting) - these are meant to be used strictly for unit tests and should be treated as “Private” APIs.

#### Private

A Private interface is for internal use within the project (such as HDFS or MapReduce) and should not be used by applications or by other projects. Most interfaces of a project are Private (also referred to as project-private). Unless an interface is intentionally exposed for external consumption, it should be marked Private.

#### Limited-Private

A Limited-Private interface is used by a specified set of projects or systems (typically closely related projects). Other projects or systems should not use the interface. Changes to the interface will be communicated/negotiated with the specified projects. For example, in the Hadoop project, some interfaces are LimitedPrivate{HDFS, MapReduce} in that they are private to the HDFS and MapReduce projects.

#### Public

A Public interface is for general use by any application.

### Change Compatibility

Changes to an API fall into two broad categories: compatible and incompatible. A compatible change is a change that meets the following criteria:

* no existing capabilities are removed,
* no existing capabilities are modified in a way that prevents their use by clients that were constructed to use the interface prior to the change, and
* no capabilities are added that require changes to clients that were constructed to use the interface prior to the change.

Any change that does not meet these three criteria is an incompatible change. Stated simply a compatible change will not break existing clients. These examples are compatible changes:

* adding a method to a Java class,
* adding an optional parameter to a RESTful web service, or
* adding a tag to an XML document.
* making the audience annotation of an interface more broad (e.g. from Private to Public) or the change compatibility annotation more restrictive (e.g. from Evolving to Stable)

These examples are incompatible changes:

* removing a method from a Java class,
* adding a method to a Java interface,
* adding a required parameter to a RESTful web service, or
* renaming a field in a JSON document.
* making the audience annotation of an interface less broad (e.g. from Public to Limited Private) or the change compatibility annotation more restrictive (e.g. from Evolving to Unstable)

### Stability

Stability denotes how stable an interface is and when compatible and incompatible changes to the interface are allowed. Hadoop APIs have the following levels of stability.

#### Stable

A Stable interface is exposed as a preferred means of communication. A Stable interface is expected not to change incompatibly within a major release and hence serves as a safe development target. A Stable interface may evolve compatibly between minor releases.

Incompatible changes allowed: major (X.0.0) Compatible changes allowed: maintenance (x.y.Z)

#### Evolving

An Evolving interface is typically exposed so that users or external code can make use of a feature before it has stabilized. The expectation that an interface should “eventually” stabilize and be promoted to Stable, however, is not a requirement for the interface to be labeled as Evolving.

Incompatible changes are allowed for Evolving interface only at minor releases.

Incompatible changes allowed: minor (x.Y.0) Compatible changes allowed: maintenance (x.y.Z)

#### Unstable

An Unstable interface is one for which no compatibility guarantees are made. An Unstable interface is not necessarily unstable. An unstable interface is typically exposed because a user or external code needs to access an interface that is not intended for consumption. The interface is exposed as an Unstable interface to state clearly that even though the interface is exposed, it is not the preferred access path, and no compatibility guarantees are made for it.

Unless there is a reason to offer a compatibility guarantee on an interface, whether it is exposed or not, it should be labeled as Unstable. Private interfaces also should be Unstable in most cases.

Incompatible changes to Unstable interfaces are allowed at any time.

Incompatible changes allowed: maintenance (x.y.Z) Compatible changes allowed: maintenance (x.y.Z)

#### Deprecated

A Deprecated interface could potentially be removed in the future and should not be used. Even so, a Deprecated interface will continue to function until it is removed. When a Deprecated interface can be removed depends on whether it is also Stable, Evolving, or Unstable.

## How are the Classifications Recorded?

How will the classification be recorded for Hadoop APIs?

* Each interface or class will have the audience and stability recorded using annotations in the org.apache.hadoop.classification package.
* The javadoc generated by the maven target javadoc:javadoc lists only the public API.
* One can derive the audience of java classes and java interfaces by the audience of the package in which they are contained. Hence it is useful to declare the audience of each java package as public or private (along with the private audience variations).

How will the classification be recorded for other interfaces, such as CLIs?

* See the [Hadoop Compatibility](Compatibility.html) page for details.

## FAQ

* Why aren’t the java scopes (private, package private and public) good enough?

  * Java’s scoping is not very complete. One is often forced to make a class public in order for other internal components to use it. It also does not have friends or sub-package-private like C++.
* But I can easily access a Private interface if it is Java public. Where is the protection and control?

  * The purpose of this classification scheme is not providing absolute access control. Its purpose is to communicate to users and developers. One can access private implementation functions in libc; however if they change the internal implementation details, the application will break and one will receive little sympathy from the folks who are supplying libc. When using a non-public interface, the risks are understood.
* Why bother declaring the stability of a Private interface? Aren’t Private interfaces always Unstable?

  * Private interfaces are not always Unstable. In the cases where they are Stable they capture internal properties of the system and can communicate these properties to its internal users and to developers of the interface.
    * e.g. In HDFS, NN-DN protocol is Private but Stable and can help implement rolling upgrades. The stability annotation communicates that this interface should not be changed in incompatible ways even though it is Private.
    * e.g. In HDFS, FSImage the Stabile designation provides more flexible rollback.
* What is the harm in applications using a Private interface that is Stable? How is it different from a Public Stable interface?

  * While a Private interface marked as Stable is targeted to change only at major releases, it may break at other times if the providers of that interface also are willing to change the internal consumers of that interface. Further, a Public Stable interface is less likely to break even at major releases (even though it is allowed to break compatibility) because the impact of the change is larger. If you use a Private interface (regardless of its stability) you run the risk of incompatibility.
* Why bother with Limited-Private? Isn’t it giving special treatment to some projects? That is not fair.

  * Most interfaces should be Public or Private. An interface should be Private unless it is explicitly intended for general use.
  * Limited-Private is for interfaces that are not intended for general use. They are exposed to related projects that need special hooks. Such a classification has a cost to both the supplier and consumer of the interface. Both will have to work together if ever there is a need to break the interface in the future; for example the supplier and the consumers will have to work together to get coordinated releases of their respective projects. This contract should not be taken lightly–use Private if possible; if the interface is really for general use for all applications then use Public. Always remember that making an interface Public comes with large burden of responsibility. Sometimes Limited-Private is just right.
  * A good example of a Limited-Private interface is BlockLocations. This interface is a fairly low-level interface that is exposed to MapReduce and HBase. The interface is likely to change down the road, and at that time the release effort will have to be coordinated with the MapReduce development team. While MapReduce and HDFS are always released in sync today, that policy may change down the road.
  * If you have a Limited-Private interface with many projects listed then the interface is probably a good candidate to be made Public.
* Let’s treat all Private interfaces as Limited-Private for all of Hadoop. What is the harm if projects in the Hadoop family have access to private classes?

  * There used to be many cases in the code where one project depended on the internal implementation details of another. A significant effort went into cleaning up those issues. Opening up all interfaces as Limited-Private for all of Hadoop would open the door to reintroducing such coupling issues.
* Aren’t all Public interfaces Stable?

  * One may mark a Public interface as Evolving in its early days. Here one is promising to make an effort to make compatible changes but may need to break it at minor releases.
  * One example of a Public interface that is Unstable is where one is providing an implementation of a standards-body based interface that is still under development. For example, many companies, in an attempt to be first to market, have provided implementations of a new NFS protocol even when the protocol was not fully completed by IETF. The implementor cannot evolve the interface in a fashion that causes least disruption because the stability is controlled by the standards body. Hence it is appropriate to label the interface as Unstable.

---
# Hadoop: Setting up a Single Node Cluster.

* [Purpose](#Purpose)
* [Prerequisites](#Prerequisites)
  * [Supported Platforms](#Supported_Platforms)
  * [Required Software](#Required_Software)
  * [Installing Software](#Installing_Software)
* [Download](#Download)
* [Prepare to Start the Hadoop Cluster](#Prepare_to_Start_the_Hadoop_Cluster)
* [Standalone Operation](#Standalone_Operation)
* [Pseudo-Distributed Operation](#Pseudo-Distributed_Operation)
  * [Configuration](#Configuration)
  * [Setup passphraseless ssh](#Setup_passphraseless_ssh)
  * [Execution](#Execution)
  * [YARN on a Single Node](#YARN_on_a_Single_Node)
* [Fully-Distributed Operation](#Fully-Distributed_Operation)
* [Hadoop in Docker containers](#Hadoop_in_Docker_containers)

## Purpose

This document describes how to set up and configure a single-node Hadoop installation so that you can quickly perform simple operations using Hadoop MapReduce and the Hadoop Distributed File System (HDFS).

*Important*: all production Hadoop clusters use Kerberos to authenticate callers and secure access to HDFS data as well as restriction access to computation services (YARN etc.).

These instructions do not cover integration with any Kerberos services, -everyone bringing up a production cluster should include connecting to their organisation’s Kerberos infrastructure as a key part of the deployment.

See [Security](./SecureMode.html) for details on how to secure a cluster.

## Prerequisites

### Supported Platforms

* GNU/Linux is supported as a development and production platform. Hadoop has been demonstrated on GNU/Linux clusters with 2000 nodes.

### Required Software

Required software for Linux include:

1. Java™ must be installed. Recommended Java versions are described at [HadoopJavaVersions](https://cwiki.apache.org/confluence/display/HADOOP/Hadoop+Java+Versions).
2. ssh must be installed and sshd must be running to use the Hadoop scripts that manage remote Hadoop daemons if the optional start and stop scripts are to be used. Additionally, it is recommmended that pdsh also be installed for better ssh resource management.

### Installing Software

If your cluster doesn’t have the requisite software you will need to install it.

For example on Ubuntu Linux:

```
  $ sudo apt-get install ssh
  $ sudo apt-get install pdsh
```

## Download

To get a Hadoop distribution, download a recent stable release from one of the [Apache Download Mirrors](http://www.apache.org/dyn/closer.cgi/hadoop/common/).

## Prepare to Start the Hadoop Cluster

Unpack the downloaded Hadoop distribution. In the distribution, edit the file `etc/hadoop/hadoop-env.sh` to define some parameters as follows:

```
  # set to the root of your Java installation
  export JAVA_HOME=/usr/java/latest
```

Try the following command:

```
  $ bin/hadoop
```

This will display the usage documentation for the hadoop script.

Now you are ready to start your Hadoop cluster in one of the three supported modes:

* [Local (Standalone) Mode](#Standalone_Operation)
* [Pseudo-Distributed Mode](#Pseudo-Distributed_Operation)
* [Fully-Distributed Mode](#Fully-Distributed_Operation)

## Standalone Operation

By default, Hadoop is configured to run in a non-distributed mode, as a single Java process. This is useful for debugging.

The following example copies the unpacked conf directory to use as input and then finds and displays every match of the given regular expression. Output is written to the given output directory.

```
  $ mkdir input
  $ cp etc/hadoop/*.xml input
  $ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.6.0-SNAPSHOT.jar grep input output 'dfs[a-z.]+'
  $ cat output/*
```

## Pseudo-Distributed Operation

Hadoop can also be run on a single-node in a pseudo-distributed mode where each Hadoop daemon runs in a separate Java process.

### Configuration

Use the following:

etc/hadoop/core-site.xml:

```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

etc/hadoop/hdfs-site.xml:

```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

### Setup passphraseless ssh

Now check that you can ssh to the localhost without a passphrase:

```
  $ ssh localhost
```

If you cannot ssh to localhost without a passphrase, execute the following commands:

```
  $ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
  $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
  $ chmod 0600 ~/.ssh/authorized_keys
```

### Execution

The following instructions are to run a MapReduce job locally. If you want to execute a job on YARN, see [YARN on Single Node](#YARN_on_a_Single_Node).

1. Format the filesystem:

   ```
     $ bin/hdfs namenode -format
   ```
2. Start NameNode daemon and DataNode daemon:

   ```
     $ sbin/start-dfs.sh
   ```

   The hadoop daemon log output is written to the `$HADOOP_LOG_DIR` directory (defaults to `$HADOOP_HOME/logs`).
3. Browse the web interface for the NameNode; by default it is available at:

   * NameNode - `http://localhost:9870/`
4. Make the HDFS directories required to execute MapReduce jobs:

   ```
     $ bin/hdfs dfs -mkdir -p /user/<username>
   ```
5. Copy the input files into the distributed filesystem:

   ```
     $ bin/hdfs dfs -mkdir input
     $ bin/hdfs dfs -put etc/hadoop/*.xml input
   ```
6. Run some of the examples provided:

   ```
     $ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.6.0-SNAPSHOT.jar grep input output 'dfs[a-z.]+'
   ```
7. Examine the output files: Copy the output files from the distributed filesystem to the local filesystem and examine them:

   ```
     $ bin/hdfs dfs -get output output
     $ cat output/*
   ```

   or

   View the output files on the distributed filesystem:

   ```
     $ bin/hdfs dfs -cat output/*
   ```
8. When you’re done, stop the daemons with:

   ```
     $ sbin/stop-dfs.sh
   ```

### YARN on a Single Node

You can run a MapReduce job on YARN in a pseudo-distributed mode by setting a few parameters and running ResourceManager daemon and NodeManager daemon in addition.

The following instructions assume that 1. ~ 4. steps of [the above instructions](#Execution) are already executed.

1. Configure parameters as follows:

   `etc/hadoop/mapred-site.xml`:

   ```
   <configuration>
       <property>
           <name>mapreduce.framework.name</name>
           <value>yarn</value>
       </property>
       <property>
           <name>mapreduce.application.classpath</name>
           <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
       </property>
   </configuration>
   ```

   `etc/hadoop/yarn-site.xml`:

   ```
   <configuration>
       <property>
           <name>yarn.nodemanager.aux-services</name>
           <value>mapreduce_shuffle</value>
       </property>
       <property>
           <name>yarn.nodemanager.env-whitelist</name>
           <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
       </property>
   </configuration>
   ```
2. Start ResourceManager daemon and NodeManager daemon:

   ```
     $ sbin/start-yarn.sh
   ```
3. Browse the web interface for the ResourceManager; by default it is available at:

   * ResourceManager - `http://localhost:8088/`
4. Run a MapReduce job.
5. When you’re done, stop the daemons with:

   ```
     $ sbin/stop-yarn.sh
   ```

## Fully-Distributed Operation

For information on setting up fully-distributed, non-trivial clusters see [Cluster Setup](./ClusterSetup.html).

## Hadoop in Docker containers

For information on setting up hadoop in docker, using either official releases or the main source code, check [Hadoop Docker](./HadoopDocker.html).

---
# CredentialProvider API Guide

* [Overview](#Overview)
* [Usage](#Usage)
  * [Usage Overview](#Usage_Overview)
  * [Credential Management](#Credential_Management)
    * [The hadoop credential Command](#The_hadoop_credential_Command)
    * [Provider Types](#Provider_Types)
    * [Keystore Passwords](#Keystore_Passwords)
    * [Disabling fallback to plain text](#Disabling_fallback_to_plain_text)

## Overview

The CredentialProvider API is an SPI framework for plugging in extensible credential providers. Credential providers are used to separate the use of sensitive tokens, secrets and passwords from the details of their storage and management. The ability to choose various storage mechanisms for protecting these credentials allows us to keep such sensitive assets out of clear text, away from prying eyes and potentially to be managed by third party solutions.

This document aims to describe the design of the CredentialProvider API, the out of the box implementations, where they are used and how to adopt their use.

## Usage

### Usage Overview

Let’s provide a quick overview of the use of the credential provider framework for protecting passwords or other sensitive tokens in hadoop.

##### Why is it used?

There are certain deployments that are very sensitive to how sensitive tokens like passwords are stored and managed within the cluster. For instance, there may be security best practices and policies in place that require such things to never be stored in clear text, for example. Enterprise deployments may be required to use a preferred solution for managing credentials and we need a way to plug in integrations for them.

##### General Usage Pattern

There are numerous places within the Hadoop project and ecosystem that can leverage the credential provider API today and the number continues to grow. In general, the usage pattern consists of the same requirements and flow.

1. Provision credentials within provider specific stores. This provisioning may be accomplished through the hadoop credential command or possibly through provider specific management tools.
2. Configure the credential provider path property. The provider path property `hadoop.security.credential.provider.path` is a comma separated list of one or more credential provider URIs that is traversed while trying to resolve a credential alias.
   * This property may be configured within core-site.xml or a component specific configuration file that is merged with core-site.xml.
   * For command line interfaces, such as that for DistCp, the property can be added with a hadoop system property (“-D *property=value*”) and dynamically added to the Configuration.
3. Features or components that leverage the new [Configuration.getPassword](../../api/org/apache/hadoop/conf/Configuration.html#getPassword-java.lang.String-) method to resolve their credentials will automatically pick up support for the credential provider API.
   * By using the same property names as are used for existing clear text passwords, this mechanism allows for the migration to credential providers while providing backward compatibility for clear text.
   * The entire credential provider path is interrogated before falling back to clear text passwords in config.
4. Features or components that do not use Hadoop’s `org.apache.hadoop.conf.Configuration` class for configuration or have other internal uses for the credential providers may choose to use the `CredentialProvider` API itself. An example of its use can be found within [Configuration.getPassword](../../api/org/apache/hadoop/conf/Configuration.html#getPassword-java.lang.String-) and within its unit tests.

##### Provision Credentials

Example: `ssl.server.keystore.password`

```
hadoop credential create ssl.server.keystore.password -value 123 \
  -provider localjceks://file/home/lmccay/aws.jceks
```

The alias names are the same as the configuration properties that were used to get the credentials from the `Configuration.get()` methods.

##### Configuring the Provider Path

Now, we need to make sure that this provisioned credential store is known at runtime by the [Configuration.getPassword](../../api/org/apache/hadoop/conf/Configuration.html#getPassword-java.lang.String-) method. If there is no credential provider path configuration then `Configuration.getPassword()` will skip the credential provider API interrogation. So, it is important that the following be configured within `core-site.xml` or your component’s equivalent.

```
<property>
  <name>hadoop.security.credential.provider.path</name>
  <value>localjceks://file/home/lmccay/aws.jceks</value>
  <description>Path to interrogate for protected credentials.</description>
</property>
```

A couple additional things to note about the provider path:

1. The scheme is used to indicate the type of provider in the above case the `localjceks` provider does not have a dependency on the Hadoop FileSystem APIs. and is needed sometimes to avoid a recursive dependency. Another provider represented by `jceks`, does use the Hadoop FileSystem APIs and can support keystores provisioned within HDFS or other compatible filesystems. A third provider type is the `user` type. This provider can manage credentials stored within the Credentials file for a process.
2. The path configuration accepts a comma separated path of providers or credential stores. The [Configuration.getPassword](../../api/org/apache/hadoop/conf/Configuration.html#getPassword-java.lang.String-) method will query each of the providers, in order until it resolves the alias or exhausts the list. Depending on the runtime needs for credentials, we may need to configure a chain of providers to check.

In summary, first, provision the credentials into a provider then configure the provider for use by a feature or component and it will often just be picked up through the use of the [Configuration.getPassword](../../api/org/apache/hadoop/conf/Configuration.html#getPassword-java.lang.String-) method.

##### Supported Features

| Feature\Component | Description | Link |
| --- | --- | --- |
| LDAPGroupsMapping | LDAPGroupsMapping is used to look up the groups for a given user in LDAP. The CredentialProvider API is used to protect the LDAP bind password and those needed for SSL. | [LDAP Groups Mapping](GroupsMapping.html#LDAP_Groups_Mapping) |
| SSL Passwords | FileBasedKeyStoresFactory leverages the credential provider API in order to resolve the SSL related passwords. | TODO |
| HDFS | DFSUtil uses `Configuration.getPassword()` use the credential provider API and/or fallback to the clear text value stored in `ssl-server.xml`. Zookeeper-based federation state store and failover controller use Configuration.getPassword to get the Zookeeper authentication info, with fallback provided to clear text auth info. | TODO |
| YARN | WebAppUtils uptakes the use of the credential provider API through the new method on Configuration called getPassword. This provides an alternative to storing the passwords in clear text within the ssl-server.xml file while maintaining backward compatibility. Zookeeper based resource manager state store uses Configuration.getPassword to get the Zookeeper authentication info, with fallback provided to clear text auth info. | TODO |
| KMS | Uses HttpServer2.loadSSLConfiguration that leverages Configuration.getPassword to read SSL related credentials. They may be resolved through Credential Provider and/or from the clear text in the config when allowed. | [KMS](../../hadoop-kms/index.html) |
| HttpFS | Uses HttpServer2.loadSSLConfiguration that leverages Configuration.getPassword to read SSL related credentials. They may be resolved through Credential Provider and/or from the clear text in the config when allowed. | [HttpFS Server Setup](../../hadoop-hdfs-httpfs/ServerSetup.html) |
| AWS   S3A | Uses `Configuration.getPassword` to get the S3 credentials. They may be resolved through the credential provider API or from the config for backward compatibility. | [AWS S3/S3A Usage](../../hadoop-aws/tools/hadoop-aws/index.html) |
| Azure   WASB | Uses `Configuration.getPassword` to get the WASB credentials. They may be resolved through the credential provider API or from the config for backward compatibility. | [Azure WASB Usage](../../hadoop-azure/index.html) |
| Azure   ADLS | Uses `Configuration.getPassword` to get the ADLS credentials. They may be resolved through the credential provider API or from the config for backward compatibility. | [Azure ADLS Usage](../../hadoop-azure-datalake/index.html) |
| Apache   Accumulo | The trace.password property is used by the Tracer to authenticate with Accumulo and persist the traces in the trace table. The credential provider API is used to acquire the trace.password from a provider or from configuration for backward compatibility. | TODO |
| Apache   Slider | A capability has been added to Slider to prompt the user for needed passwords and store them using CredentialProvider so they can be retrieved by an app later. | TODO |
| Apache   Hive | Protection of the metastore password, SSL related passwords and JDO string password has been added through the use of the Credential Provider API | TODO |
| Apache   HBase | The HBase RESTServer is using the new Configuration.getPassword method so that the credential provider API will be checked first then fall back to clear text - when allowed. | TODO |
| Apache   Oozie | Protects SSL, email and JDBC passwords using the credential provider API. | TODO |
| Apache   Ranger | Protects database, trust and keystore passwords using the credential provider API. | TODO |

### Credential Management

#### The `hadoop credential` Command

Usage: `hadoop credential <subcommand> [options]`

See the command options detail in the [Commands Manual](CommandsManual.html#credential)

The credential command can be for provisioning a password or secret to a particular credential store provider. In order to explicitly indicate which provider store to use the `-provider` option should be used.

Example: `hadoop credential create ssl.server.keystore.password -provider jceks://file/tmp/test.jceks`

In order to indicate a particular provider type and location, the user must provide the `hadoop.security.credential.provider.path` configuration element in core-site.xml or use the command line option `-provider` on each of the credential management commands. This provider path is a comma-separated list of URLs that indicates the type and location of a list of providers that should be consulted. For example, the following path: `user:///,jceks://file/tmp/test.jceks,jceks://hdfs@nn1.example.com/my/path/test.jceks` indicates that the current user’s credentials file should be consulted through the User Provider, that the local file located at `/tmp/test.jceks` is a Java Keystore Provider and that the file located within HDFS at `nn1.example.com/my/path/test.jceks` is also a store for a Java Keystore Provider.

#### Provider Types

1. The `UserProvider`, which is represented by the provider URI `user:///`, is used to retrieve credentials from a user’s Credentials file. This file is used to store various tokens, secrets and passwords that are needed by executing jobs and applications.
2. The `JavaKeyStoreProvider`, which is represented by the provider URI `jceks://SCHEME/path-to-keystore`, is used to retrieve credentials from a Java keystore file in a filesystem `<SCHEME>` The underlying use of the Hadoop filesystem API allows credentials to be stored on the local filesystem or within cluster stores.
3. The `LocalJavaKeyStoreProvider`, which is represented by the provider URI `localjceks://file/path-to-keystore`, is used to access credentials from a Java keystore that must be stored on the local filesystem. This is needed for credentials that would result in a recursive dependency on accessing HDFS. Anytime that your credential is required to gain access to HDFS we can’t depend on getting a credential out of HDFS to do so.
4. The `BouncyCastleFIPSKeyStoreProvider`, which is represented by the provider URI `bcfks://SCHEME/path-to-keystore`, is used to retrieve credentials from a Bouncy Castle FIPS keystore file in a file system `<SCHEME>` The underlying use of the Hadoop filesystem API allows credentials to be stored on the local filesystem or within cluster stores.
5. The `LocalBcouncyCastleFIPSKeyStoreProvider`, which is represented by the provider URI `localbcfks://file/path-to-keystore`, is used to access credentials from a Bouncy Castle FIPS keystore that must be stored on the local filesystem. This is needed for credentials that would result in a recursive dependency on accessing HDFS. Anytime that your credential is required to gain access to HDFS we can’t depend on getting a credential out of HDFS to do so.

When credentials are stored in a filesystem, the following rules apply:

* Credentials stored in local `localjceks://` or `localbcfks://` files are loaded in the process reading in the configuration. For use in a YARN application, this means that they must be visible across the entire cluster, in the local filesystems of the hosts.
* Credentials stored with the `jceks://` or `bcfks://` provider can be stored in the cluster filesystem, and so visible across the cluster —but not in the filesystem which requires the specific credentials for their access.

To wrap filesystem URIs with a `jceks` URI follow these steps. Bouncy Castle FIPS provider follows a similar step by replacing `jceks` with `bcfks` along with OS/JDK level FIPS provider configured.

1. Take a filesystem URI such as `hdfs://namenode:9001/users/alice/secrets.jceks`
2. Place `jceks://` in front of the URL: `jceks://hdfs://namenode:9001/users/alice/secrets.jceks`
3. Replace the second `://` string with an `@` symbol: `jceks://hdfs@namenode:9001/users/alice/secrets.jceks`

*Examples*

For a local filesystem, a path such as `file:///tmp/secrets.jceks` would become: `jceks://file/tmp/secrets.jceks`

| Path URI | jceks URI |
| --- | --- |
| `hdfs://namenode.example.org:9001/user/alice/secret.jceks` | `jceks://hdfs@namenode.example.org:9001/user/alice/secret.jceks` |
| `file:///tmp/secrets.jceks` | `jceks://file/tmp/secret.jceks` |
| `s3a://container1/secrets/secret.jceks` | `jceks://s3a@container1/secrets/secret.jceks` |
| `wasb://account@container/secret.jceks` | `jceks://wasb@account@container/secret.jceks` |
| `abfs://account@container/secret.jceks` | `jceks://abfs@account@container/secret.jceks` |
| `https://user:pass@service/secret.jceks?token=aia` | `jceks://https@user:pass@service/secret.jceks?token=aia` |

Note that to avoid infinite recursion, filesystems such as `abfs`, `s3a`, `adls` and `wasb` explicitly exclude keystores stored on paths in their own filesystem schemes, even if they are stored in a container which uses a different set of credentials from those being looked up.

As an example, you cannot use credentials stored in `s3a://shared/secrets/secret.jceks` to read the credentials for the container `s3a://private/` .

#### Keystore Passwords

Keystores in Java are generally protected by passwords. The primary method of protection of the keystore-based credential providers are OS-level file permissions and any other policy based access protection that may exist for the target filesystem. While the password is not a primary source of protection, it is very important to understand the mechanics required and options available for managing these passwords. It is also very important to understand all the parties that will need access to the password used to protect the keystores in order to consume them at runtime.

##### Options

| Option | Description | Notes |
| --- | --- | --- |
| Default password | This is a harcoded password of “none”. | This is a hardcoded password in an open source project and as such has obvious disadvantages. However, the mechanics section will show that it is simpler and consequently nearly as secure as the other more complex options. |
| Environment variable | `HADOOP_CREDSTORE_PASSWORD` | This option uses an environment variable to communicate the password that should be used when interrogating all of the keystores that are configured in the `hadoop.security.credential.provider.path` configuration property. All of the keystore based providers in the path will need to be protected by the same password. |
| Password-file | `hadoop.security.credstore.java-keystore-provider.password-file` | This option uses a “side file” that has its location configured in the `hadoop.security.credstore.java-keystore-provider.password-file` configuration property to communicate the password that should be used when interrogating all of the keystores that are configured in the `hadoop.security.credential.provider.path` configuration property. |

##### Mechanics

Extremely important to consider that *all* of the runtime consumers of the credential being protected (mapreduce jobs/applications) will need to have access to the password used to protect the keystore providers. Communicating this password can be done a number of ways and they are described in the Options section above.

| Keystore Password | Description | Sync Required | Clear Text | File Permissions |
| --- | --- | --- | --- | --- |
| Default Password | Hardcoded password is the default. Essentially, when using the default password for all keystore-based credential stores, we are leveraging the file permissions to protect the credential store and the keystore password is just a formality of persisting the keystore. | No | Yes | No (documented) |
| Environment Variable | The `HADOOP_CREDSTORE_PASSWORD` environment variable must be set to the custom password for all keystores that may be configured in the provider path of any process that needs to access credentials from a keystore-based credential provider. There is only one env variable for the entire path of comma-separated providers. It is difficult to know the passwords required for each keystore and it is suggested that the same be used for all keystore-based credential providers to avoid this issue. Setting the environment variable will likely require it to be set from a script or some other clear text storage mechanism. Environment variables for running processes are available from various unix commands. | Yes | Yes | No |
| Password File | `hadoop.security.credstore.java-keystore-provider.password-file` configuration property must be set to the location of the “side file” that contains the custom password for all keystores that may be configured in the provider path. Any process that needs to access credentials from a keystore-based credential provider will need to have this configuration property set to the appropriate file location. There is only one password-file for the entire path of comma separated providers. It is difficult to know the passwords required for each keystore and it is therefore suggested that the same be used for all keystore-based credential providers to avoid this issue. Password-files are additional files that need to be managed, store the password in clear text and need file permissions to be set such that only those that need access to them have it. If file permissions are set inappropriately the password to access the keystores is available in clear text. | Yes | Yes | Yes |

The use of the default password means that no additional communication/synchronization to runtime consumers needs to be done. The default password is known but file permissions are the primary protection of the keystore.

When file permissions are thwarted, unlike “side files”, there are no standard tools that can expose the protected credentials - even with the password known. Keytool requires a password that is six characters or more and doesn’t know how to retrieve general secrets from a keystore. It is also limited to PKI keypairs. Editors will not reveal the secrets stored within the keystore, nor will `cat`, `more` or any other standard tools. This is why the keystore providers are better than “side file” storage of credentials.

That said, it is trivial for someone to write code to access the credentials stored within a keystore-based credential provider using the API. Again, when using the default password, the password is merely a formality of persisting the keystore. The *only* protection is file permissions and OS level access policy.

Users may decide to use a password “side file” to store the password for the keystores themselves and this is supported. It is just really important to be aware of the mechanics required for this level of correctness.

#### Disabling fallback to plain text

The `Credentials.getPassword()` operation falls back to using entries in the configuration XML files if there are no credential providers, or if a key cannot be found.

This action can be disabled by changing the configuration option `hadoop.security.credential.clear-text-fallback` from `true` to `false`:

```
<property>
  <name>hadoop.security.credential.clear-text-fallback</name>
  <value>false</value>
  <description>
    true or false to indicate whether or not to fall back to storing credential
    password as clear text. The default value is true. This property only works
    when the password can't not be found from credential providers.
  </description>
</property>
```

Once set, *all configuration options looked up via the `getPassword()` API must be served via a credential provider*.

---
xml version="1.0"?
xml-stylesheet type="text/xsl" href="configuration.xsl"?







hadoop.common.configuration.version
3.0.0
version of this configuration file

hadoop.tmp.dir
/tmp/hadoop-${user.name}
A base for other temporary directories.

hadoop.http.filter.initializers
org.apache.hadoop.http.lib.StaticUserWebFilter
A comma separated list of class names. Each class in the list
must extend org.apache.hadoop.http.FilterInitializer. The corresponding
Filter will be initialized. Then, the Filter will be applied to all user
facing jsp and servlet web pages. The ordering of the list defines the
ordering of the filters.

hadoop.http.idle\_timeout.ms
60000

NN/JN/DN Server connection timeout in milliseconds.

hadoop.http.metrics.enabled
true

If true, set Jetty's StatisticsHandler to HTTP server to collect
HTTP layer metrics and register them to Hadoop metrics system.

hadoop.http.jmx.nan-filter.enabled
false

The REST API of the JMX interface can return with NaN values
if the attribute represent a 0.0/0.0 value.
Some JSON parser by default can not parse json attributes like foo:NaN.
If this filter is enabled the NaN values will be converted to 0.0 values,
to make json parse less complicated.


hadoop.security.authorization
false
Is service-level authorization enabled?

security.service.authorization.default.acl


Define the default acl for the Hadoop service if the acl of Hadoop
service is not defined in hadoop-policy.xml. If not set, `\*` is applied
meaning that all users are allowed to access the service. The list of
users and groups are both comma-separated list of names separated by
a space. Example: `user1,user2 group1,group2`.

security.service.authorization.default.acl.blocked


This property specifies the list of users and groups who are not
authorized to access Hadoop service.

hadoop.security.instrumentation.requires.admin
false

Indicates if administrator ACLs are required to access
instrumentation servlets (JMX, METRICS, CONF, STACKS, PROF).

hadoop.security.authentication
simple
Possible values are simple (no authentication), and kerberos

hadoop.security.group.mapping
org.apache.hadoop.security.JniBasedUnixGroupsMappingWithFallback

Class for user to group mapping (get groups for a given user) for ACL.
The default implementation,
org.apache.hadoop.security.JniBasedUnixGroupsMappingWithFallback,
will determine if the Java Native Interface (JNI) is available. If JNI is
available the implementation will use the API within hadoop to resolve a
list of groups for a user. If JNI is not available then the shell
implementation, ShellBasedUnixGroupsMapping, is used. This implementation
shells out to the Linux/Unix environment with the
`bash -c groups` command to resolve a list of groups for a user.

hadoop.security.dns.interface

The name of the Network Interface from which the service should determine
its host name for Kerberos login. e.g. eth2. In a multi-homed environment,
the setting can be used to affect the \_HOST substitution in the service
Kerberos principal. If this configuration value is not set, the service
will use its default hostname as returned by
InetAddress.getLocalHost().getCanonicalHostName().
Most clusters will not require this setting.

hadoop.security.dns.nameserver

The host name or IP address of the name server (DNS) which a service Node
should use to determine its own host name for Kerberos Login. Requires
hadoop.security.dns.interface.
Most clusters will not require this setting.

hadoop.security.resolver.impl
org.apache.hadoop.net.DNSDomainNameResolver

The resolver implementation used to resolve FQDN for Kerberos

hadoop.security.dns.log-slow-lookups.enabled
false

Time name lookups (via SecurityUtil) and log them if they exceed the
configured threshold.

hadoop.security.dns.log-slow-lookups.threshold.ms
1000

If slow lookup logging is enabled, this threshold is used to decide if a
lookup is considered slow enough to be logged.

hadoop.security.groups.cache.secs
300

This is the config controlling the validity of the entries in the cache
containing the user->group mapping. When this duration has expired,
then the implementation of the group mapping provider is invoked to get
the groups of the user and then cached back.

hadoop.security.groups.negative-cache.secs
30

Expiration time for entries in the the negative user-to-group mapping
caching, in seconds. This is useful when invalid users are retrying
frequently. It is suggested to set a small value for this expiration, since
a transient error in group lookup could temporarily lock out a legitimate
user.
Set this to zero or negative value to disable negative user-to-group caching.

hadoop.security.groups.cache.warn.after.ms
5000

If looking up a single user to group takes longer than this amount of
milliseconds, we will log a warning message.

hadoop.security.groups.cache.background.reload
false

Whether to reload expired user->group mappings using a background thread
pool. If set to true, a pool of
hadoop.security.groups.cache.background.reload.threads is created to
update the cache in the background.

hadoop.security.groups.cache.background.reload.threads
3

Only relevant if hadoop.security.groups.cache.background.reload is true.
Controls the number of concurrent background user->group cache entry
refreshes. Pending refresh requests beyond this value are queued and
processed when a thread is free.

hadoop.security.groups.shell.command.timeout
0s

Used by the ShellBasedUnixGroupsMapping class, this property controls how
long to wait for the underlying shell command that is run to fetch groups.
Expressed in seconds (e.g. 10s, 1m, etc.), if the running command takes
longer than the value configured, the command is aborted and the groups
resolver would return a result of no groups found. A value of 0s (default)
would mean an infinite wait (i.e. wait until the command exits on its own).

hadoop.security.group.mapping.ldap.ctx.factory.class


Used to specify the fully qualified class name of the initial context
factory when connecting to an LDAP server. The default value is
"com.sun.jndi.ldap.LdapCtxFactory", but set to null now to avoid
LifecycleExecutionException with JDK 11(see HADOOP-15941).

hadoop.security.group.mapping.ldap.connection.timeout.ms
60000

This property is the connection timeout (in milliseconds) for LDAP
operations. If the LDAP provider doesn't establish a connection within the
specified period, it will abort the connect attempt. Non-positive value
means no LDAP connection timeout is specified in which case it waits for the
connection to establish until the underlying network times out.

hadoop.security.group.mapping.ldap.read.timeout.ms
60000

This property is the read timeout (in milliseconds) for LDAP
operations. If the LDAP provider doesn't get a LDAP response within the
specified period, it will abort the read attempt. Non-positive value
means no read timeout is specified in which case it waits for the response
infinitely.

hadoop.security.group.mapping.ldap.num.attempts
3

This property is the number of attempts to be made for LDAP operations.
If this limit is exceeded, LdapGroupsMapping will return an empty
group list.

hadoop.security.group.mapping.ldap.num.attempts.before.failover
3

This property is the number of attempts to be made for LDAP operations
using a single LDAP instance. If multiple LDAP servers are configured
and this number of failed operations is reached, we will switch to the
next LDAP server. The configuration for the overall number of attempts
will still be respected, failover will thus be performed only if this
property is less than hadoop.security.group.mapping.ldap.num.attempts.

hadoop.security.group.mapping.ldap.url


The URL of the LDAP server(s) to use for resolving user groups when using
the LdapGroupsMapping user to group mapping. Supports configuring multiple
LDAP servers via a comma-separated list.

hadoop.security.group.mapping.ldap.ssl
false

Whether or not to use SSL when connecting to the LDAP server.

hadoop.security.group.mapping.ldap.ssl.keystore


File path to the SSL keystore that contains the SSL certificate required
by the LDAP server.

hadoop.security.group.mapping.ldap.ssl.keystore.password.file


The path to a file containing the password of the LDAP SSL keystore. If
the password is not configured in credential providers and the property
hadoop.security.group.mapping.ldap.ssl.keystore.password is not set,
LDAPGroupsMapping reads password from the file.
IMPORTANT: This file should be readable only by the Unix user running
the daemons and should be a local file.

hadoop.security.group.mapping.ldap.ssl.keystore.password


The password of the LDAP SSL keystore. this property name is used as an
alias to get the password from credential providers. If the password can
not be found and hadoop.security.credential.clear-text-fallback is true
LDAPGroupsMapping uses the value of this property for password.

hadoop.security.group.mapping.ldap.conversion.rule
none

The rule is applied on the group names received from LDAP when
RuleBasedLdapGroupsMapping is configured.
Supported rules are "to\_upper", "to\_lower" and "none".
to\_upper: This will convert all the group names to uppercase.
to\_lower: This will convert all the group names to lowercase.
none: This will retain the source formatting, this is default value.

hadoop.security.credential.clear-text-fallback
true

true or false to indicate whether or not to fall back to storing credential
password as clear text. The default value is true. This property only works
when the password can't not be found from credential providers.

hadoop.security.credential.provider.path


A comma-separated list of URLs that indicates the type and
location of a list of providers that should be consulted.

hadoop.security.credstore.java-keystore-provider.password-file


The path to a file containing the custom password for all keystores
that may be configured in the provider path.

hadoop.security.group.mapping.ldap.ssl.truststore


File path to the SSL truststore that contains the root certificate used to
sign the LDAP server's certificate. Specify this if the LDAP server's
certificate is not signed by a well known certificate authority.

hadoop.security.group.mapping.ldap.ssl.truststore.password.file


The path to a file containing the password of the LDAP SSL truststore.
IMPORTANT: This file should be readable only by the Unix user running
the daemons.

hadoop.security.group.mapping.ldap.bind.users


Aliases of users to be used to bind as when connecting to the LDAP
server(s). Each alias will have to have its distinguished name and
password specified through:
hadoop.security.group.mapping.ldap.bind.user
and a password configuration such as:
hadoop.security.group.mapping.ldap.bind.password.alias
For example, if:
hadoop.security.group.mapping.ldap.bind.users=alias1,alias2
then the following configuration is valid:
hadoop.security.group.mapping.ldap.bind.users.alias1.bind.user=bindUser1
hadoop.security.group.mapping.ldap.bind.users.alias1.bind.password.alias=
bindPasswordAlias1
hadoop.security.group.mapping.ldap.bind.users.alias2.bind.user=bindUser2
hadoop.security.group.mapping.ldap.bind.users.alias2.bind.password.alias=
bindPasswordAlias2

hadoop.security.group.mapping.ldap.bind.user


The distinguished name of the user to bind as when connecting to the LDAP
server. This may be left blank if the LDAP server supports anonymous binds.

hadoop.security.group.mapping.ldap.bind.password.alias


The alias of the bind user to be used to get the password from credential
providers. If the alias is empty, property
hadoop.security.group.mapping.ldap.bind.password is used instead.

hadoop.security.group.mapping.ldap.bind.password.file


The path to a file containing the password of the bind user. If
the password is not configured in credential providers and the property
hadoop.security.group.mapping.ldap.bind.password is not set,
LDAPGroupsMapping reads password from the file.
IMPORTANT: This file should be readable only by the Unix user running
the daemons and should be a local file.

hadoop.security.group.mapping.ldap.bind.password


The password of the bind user. this property name is used as an
alias to get the password from credential providers. If the password can
not be found and hadoop.security.credential.clear-text-fallback is true
LDAPGroupsMapping uses the value of this property for password.

hadoop.security.group.mapping.ldap.base


The search base for the LDAP connection. This is a distinguished name,
and will typically be the root of the LDAP directory.

hadoop.security.group.mapping.ldap.userbase


The search base for the LDAP connection for user search query. This is a
distinguished name, and its the root of the LDAP directory for users.
If not set, hadoop.security.group.mapping.ldap.base is used.

hadoop.security.group.mapping.ldap.groupbase


The search base for the LDAP connection for group search . This is a
distinguished name, and its the root of the LDAP directory for groups.
If not set, hadoop.security.group.mapping.ldap.base is used.

hadoop.security.group.mapping.ldap.search.filter.user
(&(objectClass=user)(sAMAccountName={0}))

An additional filter to use when searching for LDAP users. The default will
usually be appropriate for Active Directory installations. If connecting to
an LDAP server with a non-AD schema, this should be replaced with
(&(objectClass=inetOrgPerson)(uid={0}). {0} is a special string used to
denote where the username fits into the filter.
If the LDAP server supports posixGroups, Hadoop can enable the feature by
setting the value of this property to "posixAccount" and the value of
the hadoop.security.group.mapping.ldap.search.filter.group property to
"posixGroup".

hadoop.security.group.mapping.ldap.search.filter.group
(objectClass=group)

An additional filter to use when searching for LDAP groups. This should be
changed when resolving groups against a non-Active Directory installation.
See the description of hadoop.security.group.mapping.ldap.search.filter.user
to enable posixGroups support.

hadoop.security.group.mapping.ldap.search.attr.memberof


The attribute of the user object that identifies its group objects. By
default, Hadoop makes two LDAP queries per user if this value is empty. If
set, Hadoop will attempt to resolve group names from this attribute,
instead of making the second LDAP query to get group objects. The value
should be 'memberOf' for an MS AD installation.

hadoop.security.group.mapping.ldap.search.attr.member
member

The attribute of the group object that identifies the users that are
members of the group. The default will usually be appropriate for
any LDAP installation.

hadoop.security.group.mapping.ldap.search.attr.group.name
cn

The attribute of the group object that identifies the group name. The
default will usually be appropriate for all LDAP systems.

hadoop.security.group.mapping.ldap.search.group.hierarchy.levels
0

The number of levels to go up the group hierarchy when determining
which groups a user is part of. 0 Will represent checking just the
group that the user belongs to. Each additional level will raise the
time it takes to execute a query by at most
hadoop.security.group.mapping.ldap.directory.search.timeout.
The default will usually be appropriate for all LDAP systems.

hadoop.security.group.mapping.ldap.posix.attr.uid.name
uidNumber

The attribute of posixAccount to use when groups for membership.
Mostly useful for schemas wherein groups have memberUids that use an
attribute other than uidNumber.

hadoop.security.group.mapping.ldap.posix.attr.gid.name
gidNumber

The attribute of posixAccount indicating the group id.

hadoop.security.group.mapping.ldap.directory.search.timeout
10000

The attribute applied to the LDAP SearchControl properties to set a
maximum time limit when searching and awaiting a result.
Set to 0 if infinite wait period is desired.
Default is 10 seconds. Units in milliseconds.

hadoop.security.group.mapping.ldap.group.search.filter.pattern


Comma separated values that needs to be substituted in the group search
filter during group lookup. The values are substituted in the order they
appear in the list, the first value will replace {0} the second {1} and
so on.

hadoop.security.group.mapping.providers


Comma separated of names of other providers to provide user to group
mapping. Used by CompositeGroupsMapping.

hadoop.security.group.mapping.providers.combined
true

true or false to indicate whether groups from the providers are combined or
not. The default value is true. If true, then all the providers will be
tried to get groups and all the groups are combined to return as the final
results. Otherwise, providers are tried one by one in the configured list
order, and if any groups are retrieved from any provider, then the groups
will be returned without trying the left ones.

hadoop.security.service.user.name.key


For those cases where the same RPC protocol is implemented by multiple
servers, this configuration is required for specifying the principal
name to use for the service when the client wishes to make an RPC call.

fs.azure.user.agent.prefix
unknown

WASB passes User-Agent header to the Azure back-end. The default value
contains WASB version, Java Runtime version, Azure Client library version,
and the value of the configuration option fs.azure.user.agent.prefix.

hadoop.security.uid.cache.secs
14400

This is the config controlling the validity of the entries in the cache
containing the userId to userName and groupId to groupName used by
NativeIO getFstat().

hadoop.service.shutdown.timeout
30s

Timeout to wait for each shutdown operation to complete.
If a hook takes longer than this time to complete, it will be interrupted,
so the service will shutdown. This allows the service shutdown
to recover from a blocked operation.
Some shutdown hooks may need more time than this, for example when
a large amount of data needs to be uploaded to an object store.
In this situation: increase the timeout.
The minimum duration of the timeout is 1 second, "1s".

hadoop.rpc.protection
authentication
A comma-separated list of protection values for secured sasl
connections. Possible values are authentication, integrity and privacy.
authentication means authentication only and no integrity or privacy;
integrity implies authentication and integrity are enabled; and privacy
implies all of authentication, integrity and privacy are enabled.
hadoop.security.saslproperties.resolver.class can be used to override
the hadoop.rpc.protection for a connection at the server side.

hadoop.security.saslproperties.resolver.class

SaslPropertiesResolver used to resolve the QOP used for a
connection. If not specified, the full set of values specified in
hadoop.rpc.protection is used while determining the QOP used for the
connection. If a class is specified, then the QOP values returned by
the class will be used while determining the QOP used for the connection.

hadoop.security.sasl.mechanism
DIGEST-MD5

The SASL mechanism used in Hadoop.

hadoop.security.sasl.CustomizedCallbackHandler.class


Some security provider may define a new javax.security.auth.callback.Callback.
This property allows users to configure a customized callback handler.

hadoop.security.sensitive-config-keys

secret$
password$
ssl.keystore.pass$
fs.s3a.server-side-encryption.key
fs.s3a.\*.server-side-encryption.key
fs.s3a.encryption.algorithm
fs.s3a.encryption.key
fs.s3a.encryption.context
fs.s3a.secret.key
fs.s3a.\*.secret.key
fs.s3a.session.key
fs.s3a.\*.session.key
fs.s3a.session.token
fs.s3a.\*.session.token
fs.azure.account.key.\*
fs.azure.oauth2.\*
fs.adl.oauth2.\*
fs.gs.encryption.\*
fs.gs.proxy.\*
fs.gs.auth.\*
credential$
oauth.\*secret
oauth.\*password
oauth.\*token
hadoop.security.sensitive-config-keys
A comma-separated or multi-line list of regular expressions to
match configuration keys that should be redacted where appropriate, for
example, when logging modified properties during a reconfiguration,
private credentials should not be logged.

hadoop.security.token.service.use\_ip
true

Controls whether tokens always use IP addresses.
DNS changes will not be detected if this option is enabled.
Existing client connections that break will always reconnect
to the IP of the original host. New clients will connect
to the host's new IP but fail to locate a token.
Disabling this option will allow existing and new clients
to detect an IP change and continue to locate the new host's token.
In secure multi-homed environments, this parameter will need to
be set to false on both cluster servers and clients (see HADOOP-7733).
If it is not set correctly, the symptom will be inability to
submit an application to YARN from an external client
(with error "client host not a member of the Hadoop cluster"),
or even from an in-cluster client if server failover occurs.

hadoop.workaround.non.threadsafe.getpwuid
true
Some operating systems or authentication modules are known to
have broken implementations of getpwuid\_r and getpwgid\_r, such that these
calls are not thread-safe. Symptoms of this problem include JVM crashes
with a stack trace inside these functions. If your system exhibits this
issue, enable this configuration parameter to include a lock around the
calls as a workaround.
An incomplete list of some systems known to have this issue is available
at http://wiki.apache.org/hadoop/KnownBrokenPwuidImplementations

hadoop.kerberos.kinit.command
kinit
Used to periodically renew Kerberos credentials when provided
to Hadoop. The default setting assumes that kinit is in the PATH of users
running the Hadoop client. Change this to the absolute path to kinit if this
is not the case.

hadoop.kerberos.min.seconds.before.relogin
60
The minimum time between relogin attempts for Kerberos, in
seconds.

hadoop.kerberos.keytab.login.autorenewal.enabled
false
Used to enable automatic renewal of keytab based kerberos login.
By default the automatic renewal is disabled for keytab based kerberos login.

hadoop.security.auth\_to\_local

Maps kerberos principals to local user names

hadoop.security.auth\_to\_local.mechanism
hadoop
The mechanism by which auth\_to\_local rules are evaluated.
If set to 'hadoop' it will not allow resulting local user names to have
either '@' or '/'. If set to 'MIT' it will follow MIT evaluation rules
and the restrictions of 'hadoop' do not apply.

hadoop.token.files


A comma-separated list of token cache files that have delegation tokens
for hadoop service

hadoop.tokens


A comma-separated list of delegation tokens from base64 encoding
for hadoop service.


io.file.buffer.size
4096
The size of buffer for use in sequence files.
The size of this buffer should probably be a multiple of hardware
page size (4096 on Intel x86), and it determines how much data is
buffered during read and write operations. Must be greater than zero.

io.skip.checksum.errors
false
If true, when a checksum error is encountered while
reading a sequence file, entries are skipped, instead of throwing an
exception.

io.compression.codecs

A comma-separated list of the compression codec classes that can
be used for compression/decompression. In addition to any classes specified
with this property (which take precedence), codec classes on the classpath
are discovered using a Java ServiceLoader.

io.compression.codec.bzip2.library
system-native
The native-code library to be used for compression and
decompression by the bzip2 codec. This library could be specified
either by by name or the full pathname. In the former case, the
library is located by the dynamic linker, usually searching the
directories specified in the environment variable LD\_LIBRARY\_PATH.
The value of "system-native" indicates that the default system
library should be used. To indicate that the algorithm should
operate entirely in Java, specify "java-builtin".

io.compression.codec.lz4.buffersize
262144

Internal buffer size for Lz4 compressor/decompressors.

io.compression.codec.lz4.use.lz4hc
false

Enable lz4hc(slow but with high compression ratio) for lz4 compression.

io.compression.codec.lzo.buffersize
65536

Internal buffer size for Lzo compressor/decompressors.

io.compression.codec.lzo.class
org.apache.hadoop.io.compress.LzoCodec

Codec class that implements Lzo compression algorithm.

io.compression.codec.snappy.buffersize
262144

Internal buffer size for Snappy compressor/decompressors.

io.compression.codec.zstd.buffersize
0

Indicate ZStandard buffer size. The default value 0 means use the
recommended zstd buffer size that the library recommends.

io.compression.codec.zstd.level
3

Indicate ZStandard compression level. The higher the compression level,
the higher the compression ratio and memory usage, but the slower the
compression and decompression speed.

io.serializations
org.apache.hadoop.io.serializer.WritableSerialization, org.apache.hadoop.io.serializer.avro.AvroSpecificSerialization, org.apache.hadoop.io.serializer.avro.AvroReflectSerialization
A list of serialization classes that can be used for
obtaining serializers and deserializers.

io.seqfile.local.dir
${hadoop.tmp.dir}/io/local
The local directory where sequence file stores intermediate
data files during merge. May be a comma-separated list of
directories on different devices in order to spread disk i/o.
Directories that do not exist are ignored.

io.map.index.skip
0
Number of index entries to skip between each entry.
Zero by default. Setting this to values larger than zero can
facilitate opening large MapFiles using less memory.

io.map.index.interval
128

MapFile consist of two files - data file (tuples) and index file
(keys). For every io.map.index.interval records written in the
data file, an entry (record-key, data-file-position) is written
in the index file. This is to allow for doing binary search later
within the index file to look up records by their keys and get their
closest positions in the data file.

io.erasurecode.codec.rs.rawcoders
rs\_native,rs\_java

Comma separated raw coder implementations for the rs codec. The earlier
factory is prior to followings in case of failure of creating raw coders.

io.erasurecode.codec.rs-legacy.rawcoders
rs-legacy\_java

Comma separated raw coder implementations for the rs-legacy codec. The earlier
factory is prior to followings in case of failure of creating raw coders.

io.erasurecode.codec.xor.rawcoders
xor\_native,xor\_java

Comma separated raw coder implementations for the xor codec. The earlier
factory is prior to followings in case of failure of creating raw coders.

io.erasurecode.codec.native.enabled
true

Used to decide whether to enable native codec. If set to false, native codec
would not be created and ISA-L support would be disabled. Recommend to set to
false when your CPU does not support ISA-L.

hadoop.security.secret-manager.key-generator.algorithm
HmacSHA1

The configuration key specifying the KeyGenerator algorithm used in SecretManager
for generating secret keys. The algorithm must be a KeyGenerator algorithm supported by
the Java Cryptography Architecture (JCA). Common examples include "HmacSHA1",
"HmacSHA256", and "HmacSHA512".

hadoop.security.secret-manager.key-length
64

The configuration key specifying the key length of the generated secret keys
in SecretManager. The key length must be appropriate for the algorithm.
For example, longer keys are generally more secure but may not be supported
by all algorithms.


fs.defaultFS
file:///
The name of the default file system. A URI whose
scheme and authority determine the FileSystem implementation. The
uri's scheme determines the config property (fs.SCHEME.impl) naming
the FileSystem implementation class. The uri's authority is used to
determine the host, port, etc. for a filesystem.

fs.trash.interval
0
Number of minutes after which the checkpoint
gets deleted. If zero, the trash feature is disabled.
This option may be configured both on the server and the
client. If trash is disabled server side then the client
side configuration is checked. If trash is enabled on the
server side then the value configured on the server is
used and the client configuration value is ignored.

fs.trash.checkpoint.interval
0
Number of minutes between trash checkpoints.
Should be smaller or equal to fs.trash.interval. If zero,
the value is set to the value of fs.trash.interval.
Every time the checkpointer runs it creates a new checkpoint
out of current and removes checkpoints created more than
fs.trash.interval minutes ago.

fs.trash.clean.trashroot.enable
false
Whether clean some directories and files
in Trash home which are not under checkpoint directory.

fs.protected.directories

A comma-separated list of directories which cannot
be deleted or renamed even by the superuser unless they are empty. This
setting can be used to guard important system directories
against accidental deletion due to administrator error.

fs.AbstractFileSystem.file.impl
org.apache.hadoop.fs.local.LocalFs
The AbstractFileSystem for file: uris.

fs.AbstractFileSystem.har.impl
org.apache.hadoop.fs.HarFs
The AbstractFileSystem for har: uris.

fs.AbstractFileSystem.hdfs.impl
org.apache.hadoop.fs.Hdfs
The FileSystem for hdfs: uris.

fs.AbstractFileSystem.viewfs.impl
org.apache.hadoop.fs.viewfs.ViewFs
The AbstractFileSystem for view file system for viewfs: uris
(ie client side mount table:).

fs.viewfs.rename.strategy
SAME\_MOUNTPOINT
Allowed rename strategy to rename between multiple mountpoints.
Allowed values are SAME\_MOUNTPOINT,SAME\_TARGET\_URI\_ACROSS\_MOUNTPOINT and
SAME\_FILESYSTEM\_ACROSS\_MOUNTPOINT.

fs.viewfs.overload.scheme.target.hdfs.impl
org.apache.hadoop.hdfs.DistributedFileSystem
The DistributedFileSystem for view file system overload scheme
when child file system and ViewFSOverloadScheme's schemes are hdfs.

fs.viewfs.overload.scheme.target.s3a.impl
org.apache.hadoop.fs.s3a.S3AFileSystem
The S3AFileSystem for view file system overload scheme when
child file system and ViewFSOverloadScheme's schemes are s3a.

fs.viewfs.overload.scheme.target.ofs.impl
org.apache.hadoop.fs.ozone.RootedOzoneFileSystem
The RootedOzoneFileSystem for view file system overload scheme
when child file system and ViewFSOverloadScheme's schemes are ofs.

fs.viewfs.overload.scheme.target.o3fs.impl
org.apache.hadoop.fs.ozone.OzoneFileSystem
The OzoneFileSystem for view file system overload scheme when
child file system and ViewFSOverloadScheme's schemes are o3fs.

fs.viewfs.overload.scheme.target.ftp.impl
org.apache.hadoop.fs.ftp.FTPFileSystem
The FTPFileSystem for view file system overload scheme when
child file system and ViewFSOverloadScheme's schemes are ftp.

fs.viewfs.overload.scheme.target.webhdfs.impl
org.apache.hadoop.hdfs.web.WebHdfsFileSystem
The WebHdfsFileSystem for view file system overload scheme when
child file system and ViewFSOverloadScheme's schemes are webhdfs.

fs.viewfs.overload.scheme.target.swebhdfs.impl
org.apache.hadoop.hdfs.web.SWebHdfsFileSystem
The SWebHdfsFileSystem for view file system overload scheme when
child file system and ViewFSOverloadScheme's schemes are swebhdfs.

fs.viewfs.overload.scheme.target.file.impl
org.apache.hadoop.fs.LocalFileSystem
The LocalFileSystem for view file system overload scheme when
child file system and ViewFSOverloadScheme's schemes are file.

fs.viewfs.overload.scheme.target.abfs.impl
org.apache.hadoop.fs.azurebfs.AzureBlobFileSystem
The AzureBlobFileSystem for view file system overload scheme
when child file system and ViewFSOverloadScheme's schemes are abfs.

fs.viewfs.overload.scheme.target.abfss.impl
org.apache.hadoop.fs.azurebfs.SecureAzureBlobFileSystem
The SecureAzureBlobFileSystem for view file system overload
scheme when child file system and ViewFSOverloadScheme's schemes are abfss.

fs.viewfs.overload.scheme.target.wasb.impl
org.apache.hadoop.fs.azure.NativeAzureFileSystem
The NativeAzureFileSystem for view file system overload scheme
when child file system and ViewFSOverloadScheme's schemes are wasb.

fs.viewfs.overload.scheme.target.oss.impl
org.apache.hadoop.fs.aliyun.oss.AliyunOSSFileSystem
The AliyunOSSFileSystem for view file system overload scheme
when child file system and ViewFSOverloadScheme's schemes are oss.

fs.viewfs.overload.scheme.target.http.impl
org.apache.hadoop.fs.http.HttpFileSystem
The HttpFileSystem for view file system overload scheme
when child file system and ViewFSOverloadScheme's schemes are http.

fs.viewfs.overload.scheme.target.gs.impl
org.apache.hadoop.fs.gs.GoogleHadoopFileSystem
The GoogleHadoopFS/Google Cloud Storage file system for view
file system overload scheme when child file system and ViewFSOverloadScheme's
schemes are gs.

fs.viewfs.overload.scheme.target.https.impl
org.apache.hadoop.fs.http.HttpsFileSystem
The HttpsFileSystem for view file system overload scheme
when child file system and ViewFSOverloadScheme's schemes are https.

fs.file.impl


Specify the implementation class used for accessing the file system. It
is a fully qualified class name, including both the package name and the
class name.

fs.creation.parallel.count
64

This property sets a a semaphore to throttle the number of FileSystem
instances which can be created simultaneously. This is designed to reduce
the impact of many threads in an application calling FileSystem#get() on
a filesystem which takes time to instantiate -for example to an object
where HTTPS connections are set up during initialization. Many threads
trying to do this may create spurious delays by conflicting for access
to synchronized blocks, when simply limiting the parallelism diminishes
the conflict, so speeds up all threads trying to access the store. If a
service appears to be blocking on all threads initializing connections to
abfs, s3a or store, try a smaller (possibly significantly smaller) value.

fs.AbstractFileSystem.ftp.impl
org.apache.hadoop.fs.ftp.FtpFs
The FileSystem for Ftp: uris.

fs.ftp.impl
org.apache.hadoop.fs.ftp.FTPFileSystem
The implementation class of the FTP FileSystem

fs.AbstractFileSystem.webhdfs.impl
org.apache.hadoop.fs.WebHdfs
The FileSystem for webhdfs: uris.

fs.AbstractFileSystem.swebhdfs.impl
org.apache.hadoop.fs.SWebHdfs
The FileSystem for swebhdfs: uris.

fs.ftp.host
0.0.0.0
FTP filesystem connects to this server

fs.ftp.host.port
21

FTP filesystem connects to fs.ftp.host on this port

fs.ftp.data.connection.mode
ACTIVE\_LOCAL\_DATA\_CONNECTION\_MODE
Set the FTPClient's data connection mode based on configuration.
Valid values are ACTIVE\_LOCAL\_DATA\_CONNECTION\_MODE,
PASSIVE\_LOCAL\_DATA\_CONNECTION\_MODE and PASSIVE\_REMOTE\_DATA\_CONNECTION\_MODE.

fs.ftp.transfer.mode
BLOCK\_TRANSFER\_MODE

Set FTP's transfer mode based on configuration. Valid values are
STREAM\_TRANSFER\_MODE, BLOCK\_TRANSFER\_MODE and COMPRESSED\_TRANSFER\_MODE.

fs.ftp.timeout
0

FTP filesystem's timeout in seconds.

fs.df.interval
60000
Disk usage statistics refresh interval in msec.

fs.du.interval
600000
File space usage statistics refresh interval in msec.

fs.file.checksum.verify
true

Should data read through the local filesystem (file://) URLs be verified aginst
the checksums stored in the associated checksum files?
Setting this to false skips loading the checksum files, reading data in checksum-aligned
blocks and verifying checksums. This may improve performance
when reading data, though it pushes the responsibility of detecting errors
into the file formats themselves, or the underlying storage system.
Even when verification is enabled, files without associated checksum files
.$FILENAME.crc are never verified.
When fs.file.checksum.verify is false, vector reads of data will always return
buffers that are the buffers allocated through the buffer allocator
passed in to the API call and not sliced subsets thereof.

fs.automatic.close
true
By default, FileSystem instances are automatically closed at program
exit using a JVM shutdown hook. Setting this property to false disables this
behavior. This is an advanced option that should only be used by server applications
requiring a more carefully orchestrated shutdown sequence.

fs.iostatistics.logging.level
debug

Logging level for IOStatistics.

fs.iostatistics.thread.level.enabled
true

Enable IOStatisticsContext support for thread level.

fs.s3a.access.key
AWS access key ID used by S3A file system. Omit for IAM role-based or provider-based authentication.

fs.s3a.secret.key
AWS secret key used by S3A file system. Omit for IAM role-based or provider-based authentication.

fs.s3a.session.token
Session token, when using org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider
as one of the providers.

fs.s3a.aws.credentials.provider

org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider,
org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider,
software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider,
org.apache.hadoop.fs.s3a.auth.IAMInstanceCredentialsProvider

Comma-separated class names of credential provider classes which implement
software.amazon.awssdk.auth.credentials.AwsCredentialsProvider.
When S3A delegation tokens are not enabled, this list will be used
to directly authenticate with S3 and other AWS services.
When S3A Delegation tokens are enabled, depending upon the delegation
token binding it may be used
to communicate wih the STS endpoint to request session/role
credentials.
org.apache.hadoop.fs.s3a.auth.ProfileAWSCredentialsProvider is also supported, but is not enabled by default.

fs.s3a.security.credential.provider.path


Optional comma separated list of credential providers, a list
which is prepended to that set in hadoop.security.credential.provider.path

fs.s3a.assumed.role.arn


AWS ARN for the role to be assumed.
Required if the fs.s3a.aws.credentials.provider contains
org.apache.hadoop.fs.s3a.AssumedRoleCredentialProvider

fs.s3a.assumed.role.session.name


Session name for the assumed role, must be valid characters according to
the AWS APIs.
Only used if AssumedRoleCredentialProvider is the AWS credential provider.
If not set, one is generated from the current Hadoop/Kerberos username.

fs.s3a.assumed.role.policy


JSON policy to apply to the role.
Only used if AssumedRoleCredentialProvider is the AWS credential provider.

fs.s3a.assumed.role.session.duration
30m

Duration of assumed roles before a refresh is attempted.
Used when session tokens are requested.
Range: 15m to 1h

fs.s3a.assumed.role.sts.endpoint


AWS Security Token Service Endpoint.
If unset, uses the default endpoint.
Only used if AssumedRoleCredentialProvider is the AWS credential provider.
Used by the AssumedRoleCredentialProvider and in Session and Role delegation
tokens.

fs.s3a.assumed.role.sts.endpoint.region


AWS Security Token Service Endpoint's region;
Needed if fs.s3a.assumed.role.sts.endpoint points to an endpoint
other than the default one and the v4 signature is used.
Used by the AssumedRoleCredentialProvider and in Session and Role delegation
tokens.

fs.s3a.assumed.role.credentials.provider
org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider

List of credential providers to authenticate with the STS endpoint and
retrieve short-lived role credentials.
Only used if AssumedRoleCredentialProvider is the AWS credential provider.
If unset, uses "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider".

fs.s3a.delegation.token.binding


The name of a class to provide delegation tokens support in S3A.
If unset: delegation token support is disabled.
Note: for job submission to actually collect these tokens,
Kerberos must be enabled.
Bindings available in hadoop-aws are:
org.apache.hadoop.fs.s3a.auth.delegation.SessionTokenBinding
org.apache.hadoop.fs.s3a.auth.delegation.FullCredentialsTokenBinding
org.apache.hadoop.fs.s3a.auth.delegation.RoleTokenBinding

fs.s3a.connection.maximum
500
Controls the maximum number of simultaneous connections to S3.
This must be bigger than the value of fs.s3a.threads.max so as to stop
threads being blocked waiting for new HTTPS connections.
Why not equal? The AWS SDK transfer manager also uses these connections.

fs.s3a.connection.ssl.enabled
true
Enables or disables SSL connections to AWS services.
Also sets the default port to use for the s3a proxy settings,
when not explicitly set in fs.s3a.proxy.port.

fs.s3a.endpoint
AWS S3 endpoint to connect to. An up-to-date list is
provided in the AWS Documentation: regions and endpoints. Without this
property, the standard region (s3.amazonaws.com) is assumed.

fs.s3a.path.style.access
false
Enable S3 path style access ie disabling the default virtual hosting behaviour.
Useful for S3A-compliant storage providers as it removes the need to set up DNS for virtual hosting.

fs.s3a.proxy.host
Hostname of the (optional) proxy server for S3 connections.

fs.s3a.proxy.port
Proxy server port. If this property is not set
but fs.s3a.proxy.host is, port 80 or 443 is assumed (consistent with
the value of fs.s3a.connection.ssl.enabled).

fs.s3a.proxy.username
Username for authenticating with proxy server.

fs.s3a.proxy.password
Password for authenticating with proxy server.

fs.s3a.proxy.domain
Domain for authenticating with proxy server.

fs.s3a.proxy.workstation
Workstation for authenticating with proxy server.

fs.s3a.attempts.maximum
5

Number of times the AWS client library should retry errors before
escalating to the S3A code: {@value}.
The S3A connector does its own selective retries; the only time the AWS
SDK operations are not wrapped is during multipart copy via the AWS SDK
transfer manager.

fs.s3a.connection.establish.timeout
30s
Socket connection setup timeout in milliseconds; this will be retried
more than once.

fs.s3a.connection.timeout
200s
Socket connection timeout.

fs.s3a.connection.ttl
5m
Expiry time for any active connection.

fs.s3a.socket.send.buffer
8192
Socket send buffer hint to amazon connector. Represented in bytes.

fs.s3a.socket.recv.buffer
8192
Socket receive buffer hint to amazon connector. Represented in bytes.

fs.s3a.paging.maximum
5000
How many keys to request from S3 when doing
directory listings at a time.

fs.s3a.threads.max
96
The total number of threads available in the filesystem for data
uploads \*or any other queued filesystem operation\*.

fs.s3a.threads.keepalivetime
60s
Number of seconds a thread can be idle before being
terminated.

fs.s3a.max.total.tasks
32
The number of operations which can be queued for execution.
This is in addition to the number of active threads in fs.s3a.threads.max.

fs.s3a.executor.capacity
16
The maximum number of submitted tasks which is a single
operation (e.g. rename(), delete()) may submit simultaneously for
execution -excluding the IO-heavy block uploads, whose capacity
is set in "fs.s3a.fast.upload.active.blocks"
All tasks are submitted to the shared thread pool whose size is
set in "fs.s3a.threads.max"; the value of capacity should be less than that
of the thread pool itself, as the goal is to stop a single operation
from overloading that thread pool.

fs.s3a.multipart.size
64M
How big (in bytes) to split upload or copy operations up into.
A suffix from the set {K,M,G,T,P} may be used to scale the numeric value.

fs.s3a.multipart.threshold
128M
How big (in bytes) to split upload or copy operations up into.
This also controls the partition size in renamed files, as rename() involves
copying the source file(s).
A suffix from the set {K,M,G,T,P} may be used to scale the numeric value.

fs.s3a.multiobjectdelete.enable
true
When enabled, multiple single-object delete requests are replaced by
a single 'delete multiple objects'-request, reducing the number of requests.
Beware: legacy S3-compatible object stores might not support this request.

fs.s3a.acl.default
Set a canned ACL for newly created and copied objects. Value may be Private,
PublicRead, PublicReadWrite, AuthenticatedRead, LogDeliveryWrite, BucketOwnerRead,
or BucketOwnerFullControl.
If set, caller IAM role must have "s3:PutObjectAcl" permission on the bucket.

fs.s3a.multipart.purge
false
Deprecated. True if you want to purge existing multipart uploads that may not have been
completed/aborted correctly. The corresponding purge age is defined in
fs.s3a.multipart.purge.age.
If set, when the filesystem is instantiated then all outstanding uploads
older than the purge age will be terminated -across the entire bucket.
This will impact multipart uploads by other applications and users. so should
be used sparingly, with an age value chosen to stop failed uploads, without
breaking ongoing operations.

fs.s3a.multipart.purge.age
24h
Deprecated. Minimum age in seconds of multipart uploads to purge
on startup if "fs.s3a.multipart.purge" is true

fs.s3a.encryption.algorithm
Specify a server-side encryption or client-side
encryption algorithm for s3a: file system. Unset by default. It supports the
following values: 'AES256' (for SSE-S3), 'SSE-KMS', 'DSSE-KMS', 'SSE-C', and 'CSE-KMS'

fs.s3a.encryption.key
Specific encryption key to use if fs.s3a.encryption.algorithm
has been set to 'SSE-KMS', 'DSSE-KMS', 'SSE-C' or 'CSE-KMS'. In the case of SSE-C
, the value of this property should be the Base64 encoded key. If you are
using SSE-KMS and leave this property empty, you'll be using your default's
S3 KMS key, otherwise you should set this property to the specific KMS key
id. In case of 'CSE-KMS' this value needs to be the AWS-KMS Key ID
generated from AWS console.

fs.s3a.encryption.context
Specific encryption context to use if fs.s3a.encryption.algorithm
has been set to 'SSE-KMS' or 'DSSE-KMS'. The value of this property is a set
of non-secret comma-separated key-value pairs of additional contextual
information about the data that are separated by equal operator (=).

fs.s3a.signing-algorithm
Override the default signing algorithm so legacy
implementations can still be used

fs.s3a.accesspoint.required
false
Require that all S3 access is made through Access Points and not through
buckets directly. If enabled, use per-bucket overrides to allow bucket access to a specific set
of buckets.

fs.s3a.block.size
32M
Block size to use when reading files using s3a: file system.
A suffix from the set {K,M,G,T,P} may be used to scale the numeric value.

fs.s3a.buffer.dir
${env.LOCAL\_DIRS:-${hadoop.tmp.dir}}/s3a
Comma separated list of directories that will be used to buffer file
uploads to.
Yarn container path will be used as default value on yarn applications,
otherwise fall back to hadoop.tmp.dir

fs.s3a.fast.upload.buffer
disk

The buffering mechanism to for data being written.
Values: disk, array, bytebuffer.
"disk" will use the directories listed in fs.s3a.buffer.dir as
the location(s) to save data prior to being uploaded.
"array" uses arrays in the JVM heap
"bytebuffer" uses off-heap memory within the JVM.
Both "array" and "bytebuffer" will consume memory in a single stream up to the number
of blocks set by:
fs.s3a.multipart.size \* fs.s3a.fast.upload.active.blocks.
If using either of these mechanisms, keep this value low
The total number of threads performing work across all threads is set by
fs.s3a.threads.max, with fs.s3a.max.total.tasks values setting the number of queued
work items.

fs.s3a.fast.upload.active.blocks
4

Maximum Number of blocks a single output stream can have
active (uploading, or queued to the central FileSystem
instance's pool of queued operations.
This stops a single stream overloading the shared thread pool.

fs.s3a.readahead.range
64K
Bytes to read ahead during a seek() before closing and
re-opening the S3 HTTP connection. This option will be overridden if
any call to setReadahead() is made to an open stream.
A suffix from the set {K,M,G,T,P} may be used to scale the numeric value.

fs.s3a.user.agent.prefix


Sets a custom value that will be prepended to the User-Agent header sent in
HTTP requests to the S3 back-end by S3AFileSystem. The User-Agent header
always includes the Hadoop version number followed by a string generated by
the AWS SDK. An example is "User-Agent: Hadoop 2.8.0, aws-sdk-java/1.10.6".
If this optional property is set, then its value is prepended to create a
customized User-Agent. For example, if this configuration property was set
to "MyApp", then an example of the resulting User-Agent would be
"User-Agent: MyApp, Hadoop 2.8.0, aws-sdk-java/1.10.6".

fs.s3a.impl
org.apache.hadoop.fs.s3a.S3AFileSystem
The implementation class of the S3A Filesystem

fs.s3a.retry.limit
7

Number of times to retry any repeatable S3 client request on failure,
excluding throttling requests.

fs.s3a.retry.interval
500ms

Initial retry interval when retrying operations for any reason other
than S3 throttle errors.

fs.s3a.retry.throttle.limit
20

Number of times to retry any throttled request.

fs.s3a.retry.throttle.interval
100ms

Initial between retry attempts on throttled requests, +/- 50%. chosen at random.
i.e. for an intial value of 3000ms, the initial delay would be in the range 1500ms to 4500ms.
Backoffs are exponential; again randomness is used to avoid the thundering heard problem.
500ms is the default value used by the AWS S3 Retry policy.

fs.s3a.committer.name
file

Committer to create for output to S3A, one of:
"file", "directory", "partitioned", "magic".

fs.s3a.committer.magic.enabled
true

Enable support in the S3A filesystem for the "Magic" committer.

fs.s3a.committer.threads
8

Number of threads in committers for parallel operations on files
(upload, commit, abort, delete...)

fs.s3a.committer.staging.tmp.path
tmp/staging

Path in the cluster filesystem for temporary data.
This is for HDFS, not the local filesystem.
It is only for the summary data of each file, not the actual
data being committed.
Using an unqualified path guarantees that the full path will be
generated relative to the home directory of the user creating the job,
hence private (assuming home directory permissions are secure).

fs.s3a.committer.staging.unique-filenames
true

Option for final files to have a unique name through job attempt info,
or the value of fs.s3a.committer.staging.uuid
When writing data with the "append" conflict option, this guarantees
that new data will not overwrite any existing data.

fs.s3a.committer.staging.conflict-mode
append

Staging committer conflict resolution policy.
Supported: "fail", "append", "replace".

fs.s3a.committer.abort.pending.uploads
true

Should the committers abort all pending uploads to the destination
directory?
Set to false if more than one job is writing to the same directory tree.

fs.s3a.select.enabled
true
Is S3 Select enabled?

fs.s3a.select.input.csv.comment.marker
#
In S3 Select queries: the marker for comment lines in CSV files

fs.s3a.select.input.csv.record.delimiter
\n
In S3 Select queries over CSV files: the record delimiter.
\t is remapped to the TAB character, \r to CR \n to newline. \\ to \
and \" to "

fs.s3a.select.input.csv.field.delimiter
,
In S3 Select queries over CSV files: the field delimiter.
\t is remapped to the TAB character, \r to CR \n to newline. \\ to \
and \" to "

fs.s3a.select.input.csv.quote.character
"
In S3 Select queries over CSV files: quote character.
\t is remapped to the TAB character, \r to CR \n to newline. \\ to \
and \" to "

fs.s3a.select.input.csv.quote.escape.character
\\
In S3 Select queries over CSV files: quote escape character.
\t is remapped to the TAB character, \r to CR \n to newline. \\ to \
and \" to "

fs.s3a.select.input.csv.header
none
In S3 Select queries over CSV files: what is the role of the header? One of "none", "ignore" and "use"

fs.s3a.select.input.compression
none
In S3 Select queries, the source compression
algorithm. One of: "none" and "gzip"

fs.s3a.select.output.csv.quote.fields
always

In S3 Select queries: should fields in generated CSV Files be quoted?
One of: "always", "asneeded".

fs.s3a.select.output.csv.quote.character
"

In S3 Select queries: the quote character for generated CSV Files.

fs.s3a.select.output.csv.quote.escape.character
\\

In S3 Select queries: the quote escape character for generated CSV Files.

fs.s3a.select.output.csv.record.delimiter
\n

In S3 Select queries: the record delimiter for generated CSV Files.

fs.s3a.select.output.csv.field.delimiter
,

In S3 Select queries: the field delimiter for generated CSV Files.

fs.s3a.select.errors.include.sql
false

Include the SQL statement in errors: this is useful for development but
may leak security and Personally Identifying Information in production,
so must be disabled there.

fs.AbstractFileSystem.s3a.impl
org.apache.hadoop.fs.s3a.S3A
The implementation class of the S3A AbstractFileSystem.

fs.s3a.list.version
2

Select which version of the S3 SDK's List Objects API to use. Currently
support 2 (default) and 1 (older API).

fs.s3a.etag.checksum.enabled
false

Should calls to getFileChecksum() return the etag value of the remote
object.
WARNING: if enabled, distcp operations between HDFS and S3 will fail unless
-skipcrccheck is set.

fs.s3a.change.detection.source
etag

Select which S3 object attribute to use for change detection.
Currently support 'etag' for S3 object eTags and 'versionid' for
S3 object version IDs. Use of version IDs requires object versioning to be
enabled for each S3 bucket utilized. Object versioning is disabled on
buckets by default. When version ID is used, the buckets utilized should
have versioning enabled before any data is written.

fs.s3a.change.detection.mode
server

Determines how change detection is applied to alert to inconsistent S3
objects read during or after an overwrite. Value 'server' indicates to apply
the attribute constraint directly on GetObject requests to S3. Value 'client'
means to do a client-side comparison of the attribute value returned in the
response. Value 'server' would not work with third-party S3 implementations
that do not support these constraints on GetObject. Values 'server' and
'client' generate RemoteObjectChangedException when a mismatch is detected.
Value 'warn' works like 'client' but generates only a warning. Value 'none'
will ignore change detection completely.

fs.s3a.change.detection.version.required
true

Determines if S3 object version attribute defined by
fs.s3a.change.detection.source should be treated as required. If true and the
referred attribute is unavailable in an S3 GetObject response,
NoVersionAttributeException is thrown. Setting to 'true' is encouraged to
avoid potential for inconsistent reads with third-party S3 implementations or
against S3 buckets that have object versioning disabled.

fs.s3a.ssl.channel.mode
default\_jsse

If secure connections to S3 are enabled, configures the SSL
implementation used to encrypt connections to S3. Supported values are:
"default\_jsse", "default\_jsse\_with\_gcm", "default", and "openssl".
"default\_jsse" uses the Java Secure Socket Extension package (JSSE).
However, when running on Java 8, the GCM cipher is removed from the list
of enabled ciphers. This is due to performance issues with GCM in Java 8.
"default\_jsse\_with\_gcm" uses the JSSE with the default list of cipher
suites. "default\_jsse\_with\_gcm" is equivalent to the behavior prior to
this feature being introduced. "default" attempts to use OpenSSL rather
than the JSSE for SSL encryption, if OpenSSL libraries cannot be loaded,
it falls back to the "default\_jsse" behavior. "openssl" attempts to use
OpenSSL as well, but fails if OpenSSL libraries cannot be loaded.

fs.s3a.downgrade.syncable.exceptions
true

Warn but continue when applications use Syncable.hsync when writing
to S3A.


fs.s3a.audit.enabled
true

Should auditing of S3A requests be enabled?


fs.AbstractFileSystem.wasb.impl
org.apache.hadoop.fs.azure.Wasb
AbstractFileSystem implementation class of wasb://

fs.AbstractFileSystem.wasbs.impl
org.apache.hadoop.fs.azure.Wasbs
AbstractFileSystem implementation class of wasbs://

fs.wasb.impl
org.apache.hadoop.fs.azure.NativeAzureFileSystem
The implementation class of the Native Azure Filesystem

fs.wasbs.impl
org.apache.hadoop.fs.azure.NativeAzureFileSystem$Secure
The implementation class of the Secure Native Azure Filesystem

fs.azure.secure.mode
false

Config flag to identify the mode in which fs.azure.NativeAzureFileSystem needs
to run under. Setting it "true" would make fs.azure.NativeAzureFileSystem use
SAS keys to communicate with Azure storage.

fs.abfs.impl
org.apache.hadoop.fs.azurebfs.AzureBlobFileSystem
The implementation class of the Azure Blob Filesystem

fs.abfss.impl
org.apache.hadoop.fs.azurebfs.SecureAzureBlobFileSystem
The implementation class of the Secure Azure Blob Filesystem

fs.AbstractFileSystem.abfs.impl
org.apache.hadoop.fs.azurebfs.Abfs
AbstractFileSystem implementation class of abfs://

fs.AbstractFileSystem.abfss.impl
org.apache.hadoop.fs.azurebfs.Abfss
AbstractFileSystem implementation class of abfss://

fs.azure.local.sas.key.mode
false

Works in conjuction with fs.azure.secure.mode. Setting this config to true
results in fs.azure.NativeAzureFileSystem using the local SAS key generation
where the SAS keys are generating in the same process as fs.azure.NativeAzureFileSystem.
If fs.azure.secure.mode flag is set to false, this flag has no effect.

fs.azure.sas.expiry.period
90d

The default value to be used for expiration period for SAS keys generated.
Can use the following suffix (case insensitive):
ms(millis), s(sec), m(min), h(hour), d(day)
to specify the time (such as 2s, 2m, 1h, etc.).

fs.azure.authorization
false

Config flag to enable authorization support in WASB. Setting it to "true" enables
authorization support to WASB. Currently WASB authorization requires a remote service
to provide authorization that needs to be specified via fs.azure.authorization.remote.service.url
configuration

fs.azure.authorization.caching.enable
true

Config flag to enable caching of authorization results and saskeys in WASB.
This flag is relevant only when fs.azure.authorization is enabled.

fs.azure.saskey.usecontainersaskeyforallaccess
true

Use container saskey for access to all blobs within the container.
Blob-specific saskeys are not used when this setting is enabled.
This setting provides better performance compared to blob-specific saskeys.

fs.azure.buffer.dir
${env.LOCAL\_DIRS:-${hadoop.tmp.dir}}/abfs
Directory path for buffer files needed to upload data blocks
in AbfsOutputStream.
Yarn container path will be used as default value on yarn applications,
otherwise fall back to hadoop.tmp.dir 

fs.azure.enable.readahead
true
Enabled readahead/prefetching in AbfsInputStream.

io.seqfile.compress.blocksize
1000000
The minimum block size for compression in block compressed
SequenceFiles.

io.mapfile.bloom.size
1048576
The size of BloomFilter-s used in BloomMapFile. Each time this many
keys is appended the next BloomFilter will be created (inside a DynamicBloomFilter).
Larger values minimize the number of filters, which slightly increases the performance,
but may waste too much space if the total number of keys is usually much smaller
than this number.

io.mapfile.bloom.error.rate
0.005
The rate of false positives in BloomFilter-s used in BloomMapFile.
As this value decreases, the size of BloomFilter-s increases exponentially. This
value is the probability of encountering false positives (default is 0.5%).

hadoop.util.hash.type
murmur
The default implementation of Hash. Currently this can take one of the
two values: 'murmur' to select MurmurHash and 'jenkins' to select JenkinsHash.


ipc.client.async.calls.max
100

Define the maximum number of outstanding async calls.
If negative, there is no limit on the number of outstanding async calls.

ipc.client.idlethreshold
4000
Defines the threshold number of connections after which
connections will be inspected for idleness.

ipc.client.connection.idle-scan-interval.ms
10000

Indicate how often the server scans for idle connections.

ipc.client.kill.max
10
Defines the maximum number of clients to disconnect in one go.

ipc.client.connection.maxidletime
10000
The maximum time in msec after which a client will bring down the
connection to the server.

ipc.client.connect.max.retries
10
Indicates the number of retries a client will make to establish
a server connection.

ipc.client.connect.retry.interval
1000
Indicates the number of milliseconds a client will wait for
before retrying to establish a server connection.

ipc.client.connect.timeout
20000
Indicates the number of milliseconds a client will wait for the
socket to establish a server connection.

ipc.client.connect.max.retries.on.timeouts
45
Indicates the number of retries a client will make on socket timeout
to establish a server connection.

ipc.client.connect.max.retries.on.sasl
5

The maximum retries on SASL connection failures in RPC client.

ipc.client.tcpnodelay
true
Use TCP\_NODELAY flag to bypass Nagle's algorithm transmission delays.

ipc.client.low-latency
false
Use low-latency QoS markers for IPC connections.

ipc.client.ping
true
Send a ping to the server when timeout on reading the response,
if set to true. If no failure is detected, the client retries until at least
a byte is read or the time given by ipc.client.rpc-timeout.ms is passed.

ipc.ping.interval
60000
Timeout on waiting response from server, in milliseconds.
The client will send ping when the interval is passed without receiving bytes,
if ipc.client.ping is set to true.

ipc.client.rpc-timeout.ms
120000
Timeout on waiting response from server, in milliseconds.
If this rpc-timeout is 0, it means no timeout. If this rpc-timeout is greater
than 0, and ipc.client.ping is set to true, and this rpc-timeout is greater than
the value of ipc.ping.interval, the effective value of the rpc-timeout is
rounded up to multiple of ipc.ping.interval.

ipc.server.tcpnodelay
true

If true then disable Nagle's Algorithm.

ipc.server.handler.queue.size
100

Indicates how many calls per handler are allowed in the queue. This value can
determine the maximum call queue size by multiplying the number of handler threads.

ipc.server.max.response.size
1048576

The maximum size when large IPC handler response buffer is reset.

ipc.server.metrics.update.runner.interval
5000

To configure scheduling of server metrics update thread. This config is
used to indicate initial delay and delay between each execution of the
metric update runnable thread.

ipc.server.listen.queue.size
256
Indicates the length of the listen queue for servers accepting
client connections.

ipc.server.log.slow.rpc
false
This setting is useful to troubleshoot performance issues for
various services. If this value is set to true then we log requests that
fall into 99th percentile as well as increment RpcSlowCalls counter.

ipc.server.log.slow.rpc.threshold.ms
0
The threshold in milliseconds for logging slow rpc when ipc.server.log.slow.rpc is enabled.
Besides of being much slower than other RPC requests, an RPC request has to take at least the threshold value
defined by this property before it can be considered as slow. By default, this threshold is set to 0 (disabled).

ipc.server.purge.interval
15
Define how often calls are cleaned up in the server.
The default is 15 minutes. The unit is minutes.

ipc.server.read.connection-queue.size
100

Number of pending connections that may be queued per socket reader.

ipc.server.read.threadpool.size
1

Indicates the number of threads in RPC server reading from the socket.

ipc.maximum.data.length
134217728
This indicates the maximum IPC message length (bytes) that can be
accepted by the server. Messages larger than this value are rejected by the
immediately to avoid possible OOMs. This setting should rarely need to be
changed.

ipc.maximum.response.length
134217728
This indicates the maximum IPC message length (bytes) that can be
accepted by the client. Messages larger than this value are rejected
immediately to avoid possible OOMs. This setting should rarely need to be
changed. Set to 0 to disable.

ipc.server.reuseaddr
true
Enables the SO\_REUSEADDR TCP option on the server.
Useful if BindException often prevents a certain service to be restarted
because the server side is stuck in TIME\_WAIT state.

ipc.[port\_number].callqueue.overflow.trigger.failover
false

Enable callqueue overflow trigger failover for stateless servers.

ipc.callqueue.overflow.trigger.failover
false

This property is used as fallback property in case
"ipc.[port\_number].callqueue.overflow.trigger.failover" is not defined.
It determines whether or not to enable callqueue overflow trigger failover for stateless servers.









ipc.[port\_number].backoff.enable
false
Whether or not to enable client backoff when a queue is full.

ipc.backoff.enable
false

This property is used as fallback property in case
"ipc.[port\_number].backoff.enable" is not defined.
It determines whether or not to enable client backoff when
a queue is full.

ipc.[port\_number].callqueue.impl
java.util.concurrent.LinkedBlockingQueue
The fully qualified name of a class to use as the implementation
of a call queue. The default implementation is
java.util.concurrent.LinkedBlockingQueue (FIFO queue).
Use org.apache.hadoop.ipc.FairCallQueue for the Fair Call Queue.

ipc.callqueue.impl
java.util.concurrent.LinkedBlockingQueue

The fully qualified name of a class to use as the implementation
of a call queue. The default implementation is
java.util.concurrent.LinkedBlockingQueue (FIFO queue).
Use org.apache.hadoop.ipc.FairCallQueue for the Fair Call Queue.
This config is fallback config for ipc.[port\_number].callqueue.impl.
If call queue is not defined at port level, this default
config is used and hence, this is fallback config to
config with port.

ipc.[port\_number].scheduler.impl
org.apache.hadoop.ipc.DefaultRpcScheduler
The fully qualified name of a class to use as the
implementation of the scheduler. The default implementation is
org.apache.hadoop.ipc.DefaultRpcScheduler (no-op scheduler) when not using
FairCallQueue. If using FairCallQueue, defaults to
org.apache.hadoop.ipc.DecayRpcScheduler. Use
org.apache.hadoop.ipc.DecayRpcScheduler in conjunction with the Fair Call
Queue.

ipc.scheduler.impl
org.apache.hadoop.ipc.DefaultRpcScheduler

The fully qualified name of a class to use as the
implementation of the scheduler. The default implementation is
org.apache.hadoop.ipc.DefaultRpcScheduler (no-op scheduler) when
not using FairCallQueue. If using FairCallQueue, defaults to
org.apache.hadoop.ipc.DecayRpcScheduler. Use
org.apache.hadoop.ipc.DecayRpcScheduler in conjunction
with the Fair Call Queue.
This config is fallback config for ipc.[port\_number].scheduler.impl.
If scheduler queue is not defined at port level, this default
config is used and hence, this is fallback config to
config with port.

ipc.[port\_number].callqueue.capacity.weights


When FairCallQueue is enabled, user can specify capacity allocation
among all sub-queues via this property. The value of this config is
a comma-separated list of positive integers, each of which specifies
the weight associated with the sub-queue at that index. This list
length should be IPC scheduler priority levels, defined by
"scheduler.priority.levels". By default, each sub-queue is associated
with weight 1, i.e., all sub-queues are allocated with the same capacity.

ipc.[port\_number].scheduler.priority.levels
4
How many priority levels to use within the scheduler and call
queue. This property applies to RpcScheduler and CallQueue.

ipc.[port\_number].faircallqueue.multiplexer.weights
8,4,2,1
How much weight to give to each priority queue. This should be
a comma-separated list of length equal to the number of priority levels.
Weights descend by a factor of 2 (e.g., for 4 levels: 8,4,2,1).
This property applies to WeightedRoundRobinMultiplexer.

ipc.[port\_number].identity-provider.impl
org.apache.hadoop.ipc.UserIdentityProvider
The identity provider mapping user requests to their identity.
This property applies to DecayRpcScheduler.

ipc.identity-provider.impl
org.apache.hadoop.ipc.UserIdentityProvider

This property is used as fallback property in case
"ipc.[port\_number].identity-provider.impl" is not defined.
The identity provider mapping user requests to their identity.
This property applies to DecayRpcScheduler.

ipc.[port\_number].cost-provider.impl
org.apache.hadoop.ipc.DefaultCostProvider
The cost provider mapping user requests to their cost. To
enable determination of cost based on processing time, use
org.apache.hadoop.ipc.WeightedTimeCostProvider.
This property applies to DecayRpcScheduler.

ipc.cost-provider.impl
org.apache.hadoop.ipc.DefaultCostProvider

This property is used as fallback property in case
"ipc.[port\_number].cost-provider.impl" is not defined.
The cost provider mapping user requests to their cost. To
enable determination of cost based on processing time, use
org.apache.hadoop.ipc.WeightedTimeCostProvider.
This property applies to DecayRpcScheduler.

ipc.[port\_number].decay-scheduler.period-ms
5000
How frequently the decay factor should be applied to the
operation counts of users. Higher values have less overhead, but respond
less quickly to changes in client behavior.
This property applies to DecayRpcScheduler.

ipc.[port\_number].decay-scheduler.decay-factor
0.5
When decaying the operation counts of users, the multiplicative
decay factor to apply. Higher values will weight older operations more
strongly, essentially giving the scheduler a longer memory, and penalizing
heavy clients for a longer period of time.
This property applies to DecayRpcScheduler.

ipc.[port\_number].decay-scheduler.thresholds
13,25,50
The client load threshold, as an integer percentage, for each
priority queue. Clients producing less load, as a percent of total
operations, than specified at position i will be given priority i. This
should be a comma-separated list of length equal to the number of priority
levels minus 1 (the last is implicitly 100).
Thresholds ascend by a factor of 2 (e.g., for 4 levels: 13,25,50).
This property applies to DecayRpcScheduler.

ipc.[port\_number].decay-scheduler.backoff.responsetime.enable
false
Whether or not to enable the backoff by response time feature.
This property applies to DecayRpcScheduler.

ipc.[port\_number].decay-scheduler.backoff.responsetime.thresholds
10s,20s,30s,40s
The response time thresholds, as time durations, for each
priority queue. If the average response time for a queue is above this
threshold, backoff will occur in lower priority queues. This should be a
comma-separated list of length equal to the number of priority levels.
Threshold increases by 10s per level (e.g., for 4 levels: 10s,20s,30s,40s)
This property applies to DecayRpcScheduler.

ipc.[port\_number].decay-scheduler.metrics.top.user.count
10
The number of top (i.e., heaviest) users to emit metric
information about. This property applies to DecayRpcScheduler.

ipc.[port\_number].decay-scheduler.service-users

Service users will always be scheduled into the highest-priority
queue and won't be included in the priority computation of normal user
calls. They are specified as a comma-separated list.

ipc.[port\_number].weighted-cost.lockshared
10
The weight multiplier to apply to the time spent in the
processing phase which holds a shared (read) lock.
This property applies to WeightedTimeCostProvider.

ipc.[port\_number].weighted-cost.lockexclusive
100
The weight multiplier to apply to the time spent in the
processing phase which holds an exclusive (write) lock.
This property applies to WeightedTimeCostProvider.

ipc.[port\_number].weighted-cost.handler
1
The weight multiplier to apply to the time spent in the
HANDLER phase which do not involve holding a lock.
See org.apache.hadoop.ipc.ProcessingDetails.Timing for more details on
this phase. This property applies to WeightedTimeCostProvider.

ipc.[port\_number].weighted-cost.lockfree
1
The weight multiplier to apply to the time spent in the
LOCKFREE phase which do not involve holding a lock.
See org.apache.hadoop.ipc.ProcessingDetails.Timing for more details on
this phase. This property applies to WeightedTimeCostProvider.

ipc.[port\_number].weighted-cost.response
1
The weight multiplier to apply to the time spent in the
RESPONSE phase which do not involve holding a lock.
See org.apache.hadoop.ipc.ProcessingDetails.Timing for more details on
this phase. This property applies to WeightedTimeCostProvider.


hadoop.security.impersonation.provider.class

A class which implements ImpersonationProvider interface, used to
authorize whether one user can impersonate a specific user.
If not specified, the DefaultImpersonationProvider will be used.
If a class is specified, then that class will be used to determine
the impersonation capability.

hadoop.rpc.socket.factory.class.default
org.apache.hadoop.net.StandardSocketFactory
 Default SocketFactory to use. This parameter is expected to be
formatted as "package.FactoryClassName".

hadoop.rpc.socket.factory.class.ClientProtocol

 SocketFactory to use to connect to a DFS. If null or empty, use
hadoop.rpc.socket.class.default. This socket factory is also used by
DFSClient to create sockets to DataNodes.

hadoop.socks.server

 Address (host:port) of the SOCKS server to be used by the
SocksSocketFactory.


net.topology.node.switch.mapping.impl
org.apache.hadoop.net.ScriptBasedMapping
 The default implementation of the DNSToSwitchMapping. It
invokes a script specified in net.topology.script.file.name to resolve
node names. If the value for net.topology.script.file.name is not set, the
default value of DEFAULT\_RACK is returned for all node names.

net.topology.impl
org.apache.hadoop.net.NetworkTopology
 The default implementation of NetworkTopology which is classic three layer one.

net.topology.script.file.name

 The script name that should be invoked to resolve DNS names to
NetworkTopology names. Example: the script would take host.foo.bar as an
argument, and return /rack1 as the output.

net.topology.script.number.args
100
 The max number of args that the script configured with
net.topology.script.file.name should be run with. Each arg is an
IP address.

net.topology.table.file.name

 The file name for a topology file, which is used when the
net.topology.node.switch.mapping.impl property is set to
org.apache.hadoop.net.TableMapping. The file format is a two column text
file, with columns separated by whitespace. The first column is a DNS or
IP address and the second column specifies the rack where the address maps.
If no entry corresponding to a host in the cluster is found, then
/default-rack is assumed.

net.topology.configured.node.mapping


Key to define the node mapping as a comma-delimited list of host=rack
mappings. e.g. host1=r1,host2=r1,host3=r2. Important: spaces not trimmed
and are considered significant.

net.topology.dependency.script.file.name


Key to the dependency script filename.


file.stream-buffer-size
4096
The size of buffer to stream files.
The size of this buffer should probably be a multiple of hardware
page size (4096 on Intel x86), and it determines how much data is
buffered during read and write operations.

file.bytes-per-checksum
512
The number of bytes per checksum. Must not be larger than
file.stream-buffer-size

file.client-write-packet-size
65536
Packet size for clients to write

file.blocksize
67108864
Block size

file.replication
1
Replication factor


ftp.stream-buffer-size
4096
The size of buffer to stream files.
The size of this buffer should probably be a multiple of hardware
page size (4096 on Intel x86), and it determines how much data is
buffered during read and write operations.

ftp.bytes-per-checksum
512
The number of bytes per checksum. Must not be larger than
ftp.stream-buffer-size

ftp.client-write-packet-size
65536
Packet size for clients to write

ftp.blocksize
67108864
Block size

ftp.replication
3
Replication factor


tfile.io.chunk.size
1048576

Value chunk size in bytes. Default to
1MB. Values of the length less than the chunk size is
guaranteed to have known value length in read time (See also
TFile.Reader.Scanner.Entry.isValueLengthKnown()).

tfile.fs.output.buffer.size
262144

Buffer size used for FSDataOutputStream in bytes.

tfile.fs.input.buffer.size
262144

Buffer size used for FSDataInputStream in bytes.


hadoop.http.authentication.type
simple

Defines authentication used for Oozie HTTP endpoint.
Supported values are: simple | kerberos | #AUTHENTICATION\_HANDLER\_CLASSNAME#

hadoop.http.authentication.token.validity
36000

Indicates how long (in seconds) an authentication token is valid before it has
to be renewed.

hadoop.http.authentication.signature.secret.file
${user.home}/hadoop-http-auth-signature-secret

The signature secret for signing the authentication tokens.
A different secret should be used for each service.

hadoop.http.authentication.cookie.domain


The domain to use for the HTTP cookie that stores the authentication token.
In order to authentiation to work correctly across all Hadoop nodes web-consoles
the domain must be correctly set.
IMPORTANT: when using IP addresses, browsers ignore cookies with domain settings.
For this setting to work properly all nodes in the cluster must be configured
to generate URLs with hostname.domain names on it.

hadoop.http.authentication.simple.anonymous.allowed
true

Indicates if anonymous requests are allowed when using 'simple' authentication.

hadoop.http.authentication.kerberos.principal
HTTP/\_HOST@LOCALHOST

Indicates the Kerberos principal to be used for HTTP endpoint.
The principal MUST start with 'HTTP/' as per Kerberos HTTP SPNEGO specification.

hadoop.http.authentication.kerberos.keytab
${user.home}/hadoop.keytab

Location of the keytab file with the credentials for the principal.
Referring to the same keytab file Oozie uses for its Kerberos credentials for Hadoop.

hadoop.http.authentication.kerberos.endpoint.whitelist


The comma-separated list of the endpoints that skips Kerberos
authentication. The endpoint must start with '/' and must not
contain special characters afterwards. This parameter is for
the monitoring tools that do not support Kerberos authentication.
Administrator must configure this parameter very carefully
because it allows unauthenticated access to the daemons.


hadoop.http.cross-origin.enabled
false
Enable/disable the cross-origin (CORS) filter.

hadoop.http.cross-origin.allowed-origins
\*
Comma separated list of origins that are allowed for web services
needing cross-origin (CORS) support. If a value in the list contains an
asterix (\*), a regex pattern, escaping any dots ('.' -> '\.') and replacing
the asterix such that it captures any characters ('\*' -> '.\*'), is generated.
Values prefixed with 'regex:' are interpreted directly as regular expressions,
e.g. use the expression 'regex:https?:\/\/foo\.bar:([0-9]+)?' to allow any
origin using the 'http' or 'https' protocol in the domain 'foo.bar' on any
port. The use of simple wildcards ('\*') is discouraged, and only available for
backward compatibility.

hadoop.http.cross-origin.allowed-methods
GET,POST,HEAD
Comma separated list of methods that are allowed for web
services needing cross-origin (CORS) support.

hadoop.http.cross-origin.allowed-headers
X-Requested-With,Content-Type,Accept,Origin
Comma separated list of headers that are allowed for web
services needing cross-origin (CORS) support.

hadoop.http.cross-origin.max-age
1800
The number of seconds a pre-flighted request can be cached
for web services needing cross-origin (CORS) support.

dfs.ha.fencing.methods


List of fencing methods to use for service fencing. May contain
builtin methods (eg shell, sshfence and powershell) or user-defined method.

dfs.ha.fencing.ssh.connect-timeout
30000

SSH connection timeout, in milliseconds, to use with the builtin
sshfence fencer.

dfs.ha.fencing.ssh.private-key-files


The SSH private key files to use with the builtin sshfence fencer.

ha.zookeeper.quorum

A list of ZooKeeper server addresses, separated by commas, that are
to be used by the ZKFailoverController in automatic failover.

ha.zookeeper.session-timeout.ms
10000

The session timeout to use when the ZKFC connects to ZooKeeper.
Setting this value to a lower value implies that server crashes
will be detected more quickly, but risks triggering failover too
aggressively in the case of a transient error or network blip.

ha.zookeeper.parent-znode
/hadoop-ha

The ZooKeeper znode under which the ZK failover controller stores
its information. Note that the nameservice ID is automatically
appended to this znode, so it is not normally necessary to
configure this, even in a federated environment.

ha.zookeeper.acl
world:anyone:rwcda

A comma-separated list of ZooKeeper ACLs to apply to the znodes
used by automatic failover. These ACLs are specified in the same
format as used by the ZooKeeper CLI.
If the ACL itself contains secrets, you may instead specify a
path to a file, prefixed with the '@' symbol, and the value of
this configuration will be loaded from within.

ha.zookeeper.auth


A comma-separated list of ZooKeeper authentications to add when
connecting to ZooKeeper. These are specified in the same format
as used by the "addauth" command in the ZK CLI. It is
important that the authentications specified here are sufficient
to access znodes with the ACL specified in ha.zookeeper.acl.
If the auths contain secrets, you may instead specify a
path to a file, prefixed with the '@' symbol, and the value of
this configuration will be loaded from within.


hadoop.http.staticuser.user
dr.who

The user name to filter as, on static web filters
while rendering content. An example use is the HDFS
web UI (user to be used for browsing files).


hadoop.ssl.keystores.factory.class
org.apache.hadoop.security.ssl.FileBasedKeyStoresFactory

The keystores factory to use for retrieving certificates.

hadoop.ssl.require.client.cert
false
Whether client certificates are required

hadoop.ssl.hostname.verifier
DEFAULT

The hostname verifier to provide for HttpsURLConnections.
Valid values are: DEFAULT, STRICT, STRICT\_IE6, DEFAULT\_AND\_LOCALHOST and
ALLOW\_ALL

hadoop.ssl.server.conf
ssl-server.xml

Resource file from which ssl server keystore information will be extracted.
This file is looked up in the classpath, typically it should be in Hadoop
conf/ directory.

hadoop.ssl.client.conf
ssl-client.xml

Resource file from which ssl client keystore information will be extracted
This file is looked up in the classpath, typically it should be in Hadoop
conf/ directory.

hadoop.ssl.enabled.protocols
TLSv1.2

The supported SSL protocols. The parameter will only be used from
DatanodeHttpServer.
Starting from Hadoop 3.3.0, TLSv1.3 is supported with Java 11 Runtime.

hadoop.jetty.logs.serve.aliases
true

Enable/Disable aliases serving from jetty

fs.permissions.umask-mode
022

The umask used when creating files and directories.
Can be in octal or in symbolic. Examples are:
"022" (octal for u=rwx,g=r-x,o=r-x in symbolic),
or "u=rwx,g=rwx,o=" (symbolic for 007 in octal).


ha.health-monitor.connect-retry-interval.ms
1000

How often to retry connecting to the service.

ha.health-monitor.check-interval.ms
1000

How often to check the service.

ha.health-monitor.sleep-after-disconnect.ms
1000

How long to sleep after an unexpected RPC error.

ha.health-monitor.rpc.connect.max.retries
1

The number of retries on connect error when establishing RPC proxy
connection to NameNode, used for monitorHealth() calls.

ha.health-monitor.rpc-timeout.ms
45000

Timeout for the actual monitorHealth() calls.

ha.failover-controller.new-active.rpc-timeout.ms
60000

Timeout that the FC waits for the new active to become active

ha.failover-controller.graceful-fence.rpc-timeout.ms
5000

Timeout that the FC waits for the old active to go to standby

ha.failover-controller.graceful-fence.connection.retries
1

FC connection retries for graceful fencing

ha.failover-controller.active-standby-elector.zk.op.retries
3

The number of zookeeper operation retry times in ActiveStandbyElector

ha.failover-controller.cli-check.rpc-timeout.ms
20000

Timeout that the CLI (manual) FC waits for monitorHealth, getServiceState

ipc.client.fallback-to-simple-auth-allowed
false

When a client is configured to attempt a secure connection, but attempts to
connect to an insecure server, that server may instruct the client to
switch to SASL SIMPLE (unsecure) authentication. This setting controls
whether or not the client will accept this instruction from the server.
When false (the default), the client will not allow the fallback to SIMPLE
authentication, and will abort the connection.

fs.client.resolve.remote.symlinks
true

Whether to resolve symlinks when accessing a remote Hadoop filesystem.
Setting this to false causes an exception to be thrown upon encountering
a symlink. This setting does not apply to local filesystems, which
automatically resolve local symlinks.

nfs.exports.allowed.hosts
\* rw

By default, the export can be mounted by any client. The value string
contains machine name and access privilege, separated by whitespace
characters. The machine name format can be a single host, a Java regular
expression, or an IPv4 address. The access privilege uses rw or ro to
specify read/write or read-only access of the machines to exports. If the
access privilege is not provided, the default is read-only. Entries are separated by ";".
For example: "192.168.0.0/22 rw ; host.\*\.example\.com ; host1.test.org ro;".
Only the NFS gateway needs to restart after this property is updated.

hadoop.user.group.static.mapping.overrides
dr.who=;

Static mapping of user to groups. This will override the groups if
available in the system for the specified user. In other words, groups
look-up will not happen for these users, instead groups mapped in this
configuration will be used.
Mapping should be in this format.
user1=group1,group2;user2=;user3=group2;
Default, "dr.who=;" will consider "dr.who" as user without groups.

hadoop.user.group.metrics.percentiles.intervals


A comma-delimited list of integers denoting the desired rollover
intervals (in seconds) for percentile latency metrics on the Namenode
and Datanode for each user in the group. By default, percentile
latency metrics are disabled.

rpc.metrics.quantile.enable
false

Setting this property to true and rpc.metrics.percentiles.intervals
to a comma-separated list of the granularity in seconds, the
50/75/90/95/99th percentile latency for rpc queue/processing time in
milliseconds are added to rpc metrics.

rpc.metrics.timeunit
MILLISECONDS

This property is used to configure timeunit for various RPC Metrics
e.g rpcQueueTime, rpcLockWaitTime, rpcProcessingTime,
deferredRpcProcessingTime. In the absence of this property,
default timeunit used is milliseconds.
The value of this property should match to any one value of enum:
java.util.concurrent.TimeUnit.
Some of the valid values: NANOSECONDS, MICROSECONDS, MILLISECONDS,
SECONDS etc.

rpc.metrics.percentiles.intervals


A comma-separated list of the granularity in seconds for the metrics which
describe the 50/75/90/95/99th percentile latency for rpc queue/processing
time. The metrics are outputted if rpc.metrics.quantile.enable is set to
true.

hadoop.security.crypto.codec.classes.EXAMPLECIPHERSUITE


The prefix for a given crypto codec, contains a comma-separated
list of implementation classes for a given crypto codec (eg EXAMPLECIPHERSUITE).
The first implementation will be used if available, others are fallbacks.

hadoop.security.crypto.codec.classes.aes.ctr.nopadding
org.apache.hadoop.crypto.OpensslAesCtrCryptoCodec, org.apache.hadoop.crypto.JceAesCtrCryptoCodec

Comma-separated list of crypto codec implementations for AES/CTR/NoPadding.
The first implementation will be used if available, others are fallbacks.

hadoop.security.crypto.codec.classes.sm4.ctr.nopadding
org.apache.hadoop.crypto.OpensslSm4CtrCryptoCodec, org.apache.hadoop.crypto.JceSm4CtrCryptoCodec

Comma-separated list of crypto codec implementations for SM4/CTR/NoPadding.
The first implementation will be used if available, others are fallbacks.

hadoop.security.openssl.engine.id


The Openssl provided an engine mechanism that allow to specify third-party software
encryption library or hardware encryption device for encryption. The engine ID could
be vendor defined and will be passed to openssl, more info please see:
https://github.com/openssl/openssl/blob/master/README.ENGINE

hadoop.security.crypto.cipher.suite
AES/CTR/NoPadding

Cipher suite for crypto codec.

hadoop.security.crypto.jce.provider


The JCE provider name used in CryptoCodec.
If this value is set, the corresponding provider must be added to the provider list.
The provider may be added statically in the java.security file, or
dynamically by calling the java.security.Security.addProvider(..) method, or
automatically (only for org.bouncycastle.jce.provider.BouncyCastleProvider)
by setting "hadoop.security.crypto.jce.provider.auto-add" to true

hadoop.security.crypto.jce.provider.auto-add
true

Automatically add the org.bouncycastle.jce.provider.BouncyCastleProvider
when the value in "hadoop.security.crypto.jce.provider" is set
to BouncyCastleProvider.PROVIDER\_NAME.

hadoop.security.crypto.jceks.key.serialfilter

Enhanced KeyStore Mechanisms in JDK 8u171 introduced jceks.key.serialFilter.
If jceks.key.serialFilter is configured, the JCEKS KeyStore uses it during
the deserialization of the encrypted Key object stored inside a
SecretKeyEntry.
If jceks.key.serialFilter is not configured it will cause an error when
recovering keystore file in KeyProviderFactory when recovering key from
keystore file using JDK 8u171 or newer. The filter pattern uses the same
format as jdk.serialFilter.
The value of this property will be used as the following:
1. The value of jceks.key.serialFilter system property takes precedence
over the value of this property.
2. In the absence of jceks.key.serialFilter system property the value of
this property will be set as the value of jceks.key.serialFilter.
3. If the value of this property and jceks.key.serialFilter system
property has not been set, org.apache.hadoop.crypto.key.KeyProvider
sets a default value for jceks.key.serialFilter.

hadoop.security.crypto.buffer.size
8192

The buffer size used by CryptoInputStream and CryptoOutputStream.

hadoop.security.java.secure.random.algorithm
SHA1PRNG

The java secure random algorithm.

hadoop.security.secure.random.impl
org.apache.hadoop.crypto.random.OpensslSecureRandom

Implementation of secure random.

hadoop.security.random.device.file.path
/dev/urandom

OS security random device file path.

hadoop.security.key.provider.path

The KeyProvider to use when managing zone keys, and interacting with
encryption keys when reading and writing to an encryption zone.
For hdfs clients, the provider path will be same as namenode's
provider path.

hadoop.security.key.default.bitlength
128

The length (bits) of keys we want the KeyProvider to produce. Key length
defines the upper-bound on an algorithm's security, ideally, it would
coincide with the lower-bound on an algorithm's security.

hadoop.security.key.default.cipher
AES/CTR/NoPadding

This indicates the algorithm that be used by KeyProvider for generating
key, and will be converted to CipherSuite when creating encryption zone.

fs.har.impl.disable.cache
true
Don't cache 'har' filesystem instances.


hadoop.security.kms.client.authentication.retry-count
1

Number of time to retry connecting to KMS on authentication failure

hadoop.security.kms.client.encrypted.key.cache.size
500

Size of the EncryptedKeyVersion cache Queue for each key

hadoop.security.kms.client.encrypted.key.cache.low-watermark
0.3f

If size of the EncryptedKeyVersion cache Queue falls below the
low watermark, this cache queue will be scheduled for a refill

hadoop.security.kms.client.encrypted.key.cache.num.refill.threads
2

Number of threads to use for refilling depleted EncryptedKeyVersion
cache Queues

hadoop.security.kms.client.encrypted.key.cache.expiry
43200000

Cache expiry time for a Key, after which the cache Queue for this
key will be dropped. Default = 12hrs

hadoop.security.kms.client.timeout
60

Sets value for KMS client connection timeout, and the read timeout
to KMS servers.

hadoop.security.kms.client.failover.sleep.base.millis
100

Expert only. The time to wait, in milliseconds, between failover
attempts increases exponentially as a function of the number of
attempts made so far, with a random factor of +/- 50%. This option
specifies the base value used in the failover calculation. The
first failover will retry immediately. The 2nd failover attempt
will delay at least hadoop.security.client.failover.sleep.base.millis
milliseconds. And so on.

hadoop.security.kms.client.failover.sleep.max.millis
2000

Expert only. The time to wait, in milliseconds, between failover
attempts increases exponentially as a function of the number of
attempts made so far, with a random factor of +/- 50%. This option
specifies the maximum value to wait between failovers.
Specifically, the time between two failover attempts will not
exceed +/- 50% of hadoop.security.client.failover.sleep.max.millis
milliseconds.

hadoop.security.kms.client.failover.max.retries


Default value is the number of providers specified.

hadoop.security.kerberos.ticket.cache.path


Path to the Kerberos ticket cache. Setting this will force
UserGroupInformation to use only this ticket cache file when
creating a FileSystem instance.

ipc.server.max.connections
0
The maximum number of concurrent connections a server is allowed
to accept. If this limit is exceeded, incoming connections will first fill
the listen queue and then may go to an OS-specific listen overflow queue.
The client may fail or timeout, but the server can avoid running out of file
descriptors using this feature. 0 means no limit.


hadoop.registry.zk.root
/registry

The root zookeeper node for the registry

hadoop.registry.zk.session.timeout.ms
60000

Zookeeper session timeout in milliseconds

hadoop.registry.zk.connection.timeout.ms
15000

Zookeeper connection timeout in milliseconds

hadoop.registry.zk.retry.times
5

Zookeeper connection retry count before failing

hadoop.registry.zk.retry.interval.ms
1000


hadoop.registry.zk.retry.ceiling.ms
60000

Zookeeper retry limit in milliseconds, during
exponential backoff.
This places a limit even
if the retry times and interval limit, combined
with the backoff policy, result in a long retry
period

hadoop.registry.zk.quorum
localhost:2181

List of hostname:port pairs defining the
zookeeper quorum binding for the registry

hadoop.registry.secure
false

Key to set if the registry is secure. Turning it on
changes the permissions policy from "open access"
to restrictions on kerberos with the option of
a user adding one or more auth key pairs down their
own tree.

hadoop.registry.system.acls
sasl:yarn@, sasl:mapred@, sasl:hdfs@

A comma separated list of Zookeeper ACL identifiers with
system access to the registry in a secure cluster.
These are given full access to all entries.
If there is an "@" at the end of a SASL entry it
instructs the registry client to append the default kerberos domain.

hadoop.registry.kerberos.realm


The kerberos realm: used to set the realm of
system principals which do not declare their realm,
and any other accounts that need the value.
If empty, the default realm of the running process
is used.
If neither are known and the realm is needed, then the registry
service/client will fail.

hadoop.registry.jaas.context
Client

Key to define the JAAS context. Used in secure
mode

hadoop.shell.missing.defaultFs.warning
false

Enable hdfs shell commands to display warnings if (fs.defaultFS) property
is not set.

hadoop.shell.safely.delete.limit.num.files
100
Used by -safely option of hadoop fs shell -rm command to avoid
accidental deletion of large directories. When enabled, the -rm command
requires confirmation if the number of files to be deleted is greater than
this limit. The default limit is 100 files. The warning is disabled if
the limit is 0 or the -safely is not specified in -rm command.

fs.client.htrace.sampler.classes

The class names of the HTrace Samplers to use for Hadoop
filesystem clients.

hadoop.htrace.span.receiver.classes

The class names of the Span Receivers to use for Hadoop.

hadoop.http.logs.enabled
true

Enable the "/logs" endpoint on all Hadoop daemons, which serves local
logs, but may be considered a security risk due to it listing the contents
of a directory.

fs.client.resolve.topology.enabled
false
Whether the client machine will use the class specified by
property net.topology.node.switch.mapping.impl to compute the network
distance between itself and remote machines of the FileSystem. Additional
properties might need to be configured depending on the class specified
in net.topology.node.switch.mapping.impl. For example, if
org.apache.hadoop.net.ScriptBasedMapping is used, a valid script file
needs to be specified in net.topology.script.file.name.


fs.adl.impl
org.apache.hadoop.fs.adl.AdlFileSystem

fs.AbstractFileSystem.adl.impl
org.apache.hadoop.fs.adl.Adl

adl.feature.ownerandgroup.enableupn
false

When true : User and Group in FileStatus/AclStatus response is
represented as user friendly name as per Azure AD profile.
When false (default) : User and Group in FileStatus/AclStatus
response is represented by the unique identifier from Azure AD
profile (Object ID as GUID).
For optimal performance, false is recommended.

fs.adl.oauth2.access.token.provider.type
ClientCredential

Defines Azure Active Directory OAuth2 access token provider type.
Supported types are ClientCredential, RefreshToken, MSI, DeviceCode,
and Custom.
The ClientCredential type requires property fs.adl.oauth2.client.id,
fs.adl.oauth2.credential, and fs.adl.oauth2.refresh.url.
The RefreshToken type requires property fs.adl.oauth2.client.id and
fs.adl.oauth2.refresh.token.
The MSI type reads optional property fs.adl.oauth2.msi.port, if specified.
The DeviceCode type requires property
fs.adl.oauth2.devicecode.clientapp.id.
The Custom type requires property fs.adl.oauth2.access.token.provider.

fs.adl.oauth2.client.id

The OAuth2 client id.

fs.adl.oauth2.credential

The OAuth2 access key.

fs.adl.oauth2.refresh.url

The OAuth2 token endpoint.

fs.adl.oauth2.refresh.token

The OAuth2 refresh token.

fs.adl.oauth2.access.token.provider


The class name of the OAuth2 access token provider.

fs.adl.oauth2.msi.port


The localhost port for the MSI token service. This is the port specified
when creating the Azure VM. The default, if this setting is not specified,
is 50342.
Used by MSI token provider.

fs.adl.oauth2.devicecode.clientapp.id


The app id of the AAD native app in whose context the auth request
should be made.
Used by DeviceCode token provider.

adl.http.timeout
-1

Base timeout (in milliseconds) for HTTP requests from the ADL SDK. Values
of zero or less cause the SDK default to be used instead.

adl.ssl.channel.mode


Valid inputs are OpenSSL, Default\_JSE and Default (case insensitive).
If config is missing or is invalid, SSL Channel mode will be set to Default.
When OpenSSL, SSL socket connections are created in OpenSSL mode.
When Default\_JSE, SSL socket connections are created in the default JSE mode.
When Default, SSL socket connections are attempted with OpenSSL
and will fallback to Default\_JSE mode if OpenSSL is not available at runtime.


hadoop.caller.context.enabled
false
When the feature is enabled, additional fields are written into
name-node audit log records for auditing coarse granularity operations.

hadoop.caller.context.max.size
128
The maximum bytes a caller context string can have. If the
passed caller context is longer than this maximum bytes, client will
truncate it before sending to server. Note that the server may have a
different maximum size, and will truncate the caller context to the
maximum size it allows.

hadoop.caller.context.signature.max.size
40

The caller's signature (optional) is for offline validation. If the
signature exceeds the maximum allowed bytes in server, the caller context
will be abandoned, in which case the caller context will not be recorded
in audit logs.

hadoop.caller.context.separator
,

The separator is for context which maybe contain many fields. For example,
if the separator is ',', and there are two key/value fields in context,
in which case the context string is "key1:value1,key2:value2". The
separator should not contain '\t', '\n', '='.


seq.io.sort.mb
100

The total amount of buffer memory to use while sorting files,
while using SequenceFile.Sorter, in megabytes. By default,
gives each merge stream 1MB, which should minimize seeks.

seq.io.sort.factor
100

The number of streams to merge at once while sorting
files using SequenceFile.Sorter.
This determines the number of open file handles.

hadoop.zk.address

Host:Port of the ZooKeeper server to be used.

hadoop.zk.num-retries
1000
Number of tries to connect to ZooKeeper.

hadoop.zk.retry-interval-ms
1000
Retry interval in milliseconds when connecting to ZooKeeper.

hadoop.zk.timeout-ms
10000
ZooKeeper session timeout in milliseconds. Session expiration
is managed by the ZooKeeper cluster itself, not by the client. This value is
used by the cluster to determine when the client's session expires.
Expirations happens when the cluster does not hear from the client within
the specified session timeout period (i.e. no heartbeat).

hadoop.zk.acl
world:anyone:rwcda
ACL's to be used for ZooKeeper znodes.

hadoop.zk.auth

Specify the auths to be used for the ACL's specified in hadoop.zk.acl.
This takes a comma-separated list of authentication mechanisms, each of the
form 'scheme:auth' (the same syntax used for the 'addAuth' command in
the ZK CLI).

hadoop.zk.server.principal


Principal name for zookeeper servers.

hadoop.zk.kerberos.principal


Kerberos principal name for zookeeper connection.

hadoop.zk.kerberos.keytab


Kerberos keytab for zookeeper connection.

hadoop.zk.ssl.enabled

Enable SSL/TLS encryption for the ZooKeeper communication.
Note: this setting overrides dfs.ha.zkfc.client.ssl.enabled,
yarn.resourcemanager.zk-client-ssl.enabled and also
hadoop.kms.authentication.zk-dt-secret-manager.ssl.enabled in order to unify the SSL based
Zookeeper access across Hadoop. Leaving this property empty ensures that service specific
enablement can be done separately.

hadoop.zk.ssl.keystore.location

Keystore location for ZooKeeper client connection over SSL.

hadoop.zk.ssl.keystore.password

Keystore password for ZooKeeper client connection over SSL.

hadoop.zk.ssl.truststore.location

Truststore location for ZooKeeper client connection over SSL.

hadoop.zk.ssl.truststore.password

Truststore password for ZooKeeper client connection over SSL.

hadoop.system.tags
YARN,HDFS,NAMENODE,DATANODE,REQUIRED,SECURITY,KERBEROS,PERFORMANCE,CLIENT
,SERVER,DEBUG,DEPRECATED,COMMON,OPTIONAL

Deprecated. Please use hadoop.tags.system instead.

hadoop.tags.system
YARN,HDFS,NAMENODE,DATANODE,REQUIRED,SECURITY,KERBEROS,PERFORMANCE,CLIENT
,SERVER,DEBUG,DEPRECATED,COMMON,OPTIONAL

A comma-separated list of system tags to group related properties together.

hadoop.tags.custom


A comma-separated list of custom tags to group related properties together.

ipc.client.bind.wildcard.addr
false
When set to true Clients will bind socket to wildcard
address. (i.e 0.0.0.0)

hadoop.domainname.resolver.impl
org.apache.hadoop.net.DNSDomainNameResolver
The implementation of DomainNameResolver used for service (NameNodes,
RBF Routers etc) discovery. The default implementation
org.apache.hadoop.net.DNSDomainNameResolver returns all IP addresses associated
with the input domain name of the services by querying the underlying DNS.

dfs.client.ignore.namenode.default.kms.uri
false

Ignore KMS default URI returned from NameNode.
When set to true, kms uri is searched in the following order:
1. If there is a mapping in Credential's secrets map for namenode uri.
2. Fallback to local conf. (i.e hadoop.security.key.provider.path)
If client choose to ignore KMS uri provided by NameNode then client
should set KMS URI using 'hadoop.security.key.provider.path' to access
the right KMS for encrypted files.

hadoop.prometheus.endpoint.enabled
false

If set to true, prometheus compatible metric page on the HTTP servers
is enabled via '/prom' endpoint.

fs.getspaceused.classname


The class that can tell estimate much space is used in a directory.
There are four impl classes that being supported:
org.apache.hadoop.fs.DU(default), org.apache.hadoop.fs.WindowsGetSpaceUsed
org.apache.hadoop.fs.DFCachingGetSpaceUsed and
org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.ReplicaCachingGetSpaceUsed.
And the ReplicaCachingGetSpaceUsed impl class only used in HDFS module.

fs.getspaceused.jitterMillis
60000

fs space usage statistics refresh jitter in msec.

hadoop.http.sni.host.check.enabled
false

Enable Server Name Indication (SNI) host check for HTTPS enabled server.

hadoop.metrics.jvm.use-thread-mxbean
false

Whether or not ThreadMXBean is used for getting thread info in JvmMetrics,
ThreadGroup approach is preferred for better performance.

fs.AbstractFileSystem.ofs.impl
org.apache.hadoop.fs.ozone.RootedOzFs
The AbstractFileSystem for Rooted Ozone
FileSystem ofs uri

fs.AbstractFileSystem.o3fs.impl
org.apache.hadoop.fs.ozone.OzFs
The AbstractFileSystem for Ozone FileSystem o3fs uri

fs.hdfs.impl.disable.cache
false
Whether disable cached hdfs filesystem instances or not.
If false, return a cached hdfs fileSystem instance to the caller if exists.
If true, a new hdfs fileSystem instance will be created,
initialized with the configuration and URI, cached and returned to the caller,
it is slower than using cached hdfs filesystme instances.

hadoop.security.hostname.cache.expire-interval.seconds
0
The expiration time in seconds for cached hostname resolutions.
This cache is used to avoid repeated resolution for hostname.
A shorter interval may provide more up-to-date resolutions,
while a longer interval reduces lookup overhead.
If the value is less than or equal to 0, the cache is disabled entirely.

fs.gs.impl
org.apache.hadoop.fs.gs.GoogleHadoopFileSystem
The FileSystem for gs: uris.

fs.AbstractFileSystem.gs.impl
org.apache.hadoop.fs.gs.Gs
The AbstractFileSystem for gs: uris.

fs.gs.project.id

Google Cloud Project ID with access to Google Cloud Storage buckets.
Required only for list buckets and create bucket operations.

fs.gs.working.dir
/

The directory relative gs: uris resolve in inside the default bucket.

fs.gs.rewrite.max.chunk.size
512m

Maximum size of object chunk that will be rewritten in a single rewrite
request when fs.gs.copy.with.rewrite.enable is set to true.

fs.gs.bucket.delete.enable
false

If true, recursive delete on a path that refers to a Cloud Storage bucket
itself or delete on that path when it is empty will result in deletion of
the bucket itself. If false, any operation that normally would have
deleted the bucket will be ignored. Setting to false preserves the typical
behavior of rm -rf / which translates to deleting everything inside of
root, but without clobbering the filesystem authority corresponding to that
root path in the process.

fs.gs.block.size
64m

The reported block size of the file system. This does not change any
behavior of the connector or the underlying Google Cloud Storage objects.
However, it will affect the number of splits Hadoop MapReduce uses for a
given input.

fs.gs.create.items.conflict.check.enable
true

Enables a check that ensures that conflicting directories do not exist when
creating files and conflicting files do not exist when creating directories.

fs.gs.marker.file.pattern

If set, files that match specified pattern are copied last during folder
rename operation.

fs.gs.auth.type
COMPUTE\_ENGINE

What type of authentication mechanism to use for Google Cloud Storage
access. Valid values: APPLICATION\_DEFAULT, COMPUTE\_ENGINE,
SERVICE\_ACCOUNT\_JSON\_KEYFILE, UNAUTHENTICATED, USER\_CREDENTIALS.

fs.gs.auth.service.account.json.keyfile

The path to the JSON keyfile for the service account when fs.gs.auth.type
property is set to SERVICE\_ACCOUNT\_JSON\_KEYFILE. The file must exist at
the same path on all nodes

fs.gs.auth.client.id

The OAuth2 client ID.

fs.gs.auth.client.secret

The OAuth2 client secret.

fs.gs.auth.refresh.token

The refresh token.

fs.gs.inputstream.support.gzip.encoding.enable
false

If set to false then reading files with GZIP content encoding (HTTP header
Content-Encoding: gzip) will result in failure (IOException is thrown).
This feature is disabled by default because processing of
GZIP encoded files is inefficient and error-prone in Hadoop and Spark.

fs.gs.outputstream.buffer.size
8m

Write buffer size used by the file system API to send the data to be
uploaded to Cloud Storage upload thread via pipes. The various pipe types
are documented below.

fs.gs.outputstream.sync.min.interval
0

Output stream configuration that controls the minimum interval between
consecutive syncs. This allows to avoid getting rate-limited by Google Cloud
Storage. Default is 0 - no wait between syncs. Note that hflush() will
be no-op if called more frequently than minimum sync interval and hsync()
will block until an end of a min sync interval.

fs.gs.inputstream.fadvise
AUTO

Tunes reading objects behavior to optimize HTTP GET requests for various use
cases. Valid values: SEQUENTIAL, RANDOM, AUTO, AUTO\_RANDOM.

fs.gs.fadvise.request.track.count
3

Self adaptive fadvise mode uses distance between the served requests to
decide the access pattern. This property controls how many such requests
need to be tracked. It is used when AUTO\_RANDOM is selected.

fs.gs.inputstream.inplace.seek.limit
8m

If forward seeks are within this many bytes of the current position, seeks
are performed by reading and discarding bytes in-place rather than opening a
new underlying stream.

fs.gs.inputstream.min.range.request.size
2m

Minimum size in bytes of the read range for Cloud Storage request when
opening a new stream to read an object.

fs.obs.impl
org.apache.hadoop.fs.obs.OBSFileSystem
The FileSystem for obs: uris.

---
# Unix Shell Guide

* [Important End-User Environment Variables](#Important_End-User_Environment_Variables)
  * [HADOOP\_CLIENT\_OPTS](#HADOOP_CLIENT_OPTS)
  * [(command)\_(subcommand)\_OPTS](#a.28command.29_.28subcommand.29_OPTS)
  * [HADOOP\_CLASSPATH](#HADOOP_CLASSPATH)
  * [Auto-setting of Variables](#Auto-setting_of_Variables)
* [Administrator Environment](#Administrator_Environment)
  * [(command)\_(subcommand)\_OPTS](#a.28command.29_.28subcommand.29_OPTS)
  * [(command)\_(subcommand)\_USER](#a.28command.29_.28subcommand.29_USER)
* [Developer and Advanced Administrator Environment](#Developer_and_Advanced_Administrator_Environment)
  * [Shell Profiles](#Shell_Profiles)
  * [Shell API](#Shell_API)
  * [User-level API Access](#User-level_API_Access)
  * [Dynamic Subcommands](#Dynamic_Subcommands)
  * [Running with Privilege (Secure Mode)](#Running_with_Privilege_.28Secure_Mode.29)

Much of Apache Hadoop’s functionality is controlled via [the shell](CommandsManual.html). There are several ways to modify the default behavior of how these commands execute.

## Important End-User Environment Variables

Apache Hadoop has many environment variables that control various aspects of the software. (See `hadoop-env.sh` and related files.) Some of these environment variables are dedicated to helping end users manage their runtime.

### `HADOOP_CLIENT_OPTS`

This environment variable is used for all end-user, non-daemon operations. It can be used to set any Java options as well as any Apache Hadoop options via a system property definition. For example:

```
HADOOP_CLIENT_OPTS="-Xmx1g -Dhadoop.socks.server=localhost:4000" hadoop fs -ls /tmp
```

will increase the memory and send this command via a SOCKS proxy server.

NOTE: If ‘YARN\_CLIENT\_OPTS’ is defined, it will replace ‘HADOOP\_CLIENT\_OPTS’ when commands are run with ‘yarn’.

### `(command)_(subcommand)_OPTS`

It is also possible to set options on a per subcommand basis. This allows for one to create special options for particular cases. The first part of the pattern is the command being used, but all uppercase. The second part of the command is the subcommand being used. Then finally followed by the string `_OPT`.

For example, to configure `mapred distcp` to use a 2GB heap, one would use:

```
MAPRED_DISTCP_OPTS="-Xmx2g"
```

These options will appear *after* `HADOOP_CLIENT_OPTS` during execution and will generally take precedence.

### `HADOOP_CLASSPATH`

NOTE: Site-wide settings should be configured via a shellprofile entry and permanent user-wide settings should be configured via ${HOME}/.hadooprc using the `hadoop_add_classpath` function. See below for more information.

The Apache Hadoop scripts have the capability to inject more content into the classpath of the running command by setting this environment variable. It should be a colon delimited list of directories, files, or wildcard locations.

```
HADOOP_CLASSPATH=${HOME}/lib/myjars/*.jar hadoop classpath
```

A user can provides hints to the location of the paths via the `HADOOP_USER_CLASSPATH_FIRST` variable. Setting this to any value will tell the system to try and push these paths near the front.

### Auto-setting of Variables

If a user has a common set of settings, they can be put into the `${HOME}/.hadoop-env` file. This file is always read to initialize and override any variables that the user may want to customize. It uses bash syntax, similar to the `.bashrc` file:

For example:

```
#
# my custom Apache Hadoop settings!
#

HADOOP_CLIENT_OPTS="-Xmx1g"
MAPRED_DISTCP_OPTS="-Xmx2g"
HADOOP_DISTCP_OPTS="-Xmx2g"
```

The `.hadoop-env` file can also be used to extend functionality and teach Apache Hadoop new tricks. For example, to run hadoop commands accessing the server referenced in the environment variable `${HADOOP_SERVER}`, the following in the `.hadoop-env` will do just that:

```
if [[ -n ${HADOOP_SERVER} ]]; then
  HADOOP_CONF_DIR=/etc/hadoop.${HADOOP_SERVER}
fi
```

One word of warning: not all of Unix Shell API routines are available or work correctly in `.hadoop-env`. See below for more information on `.hadooprc`.

## Administrator Environment

In addition to the various XML files, there are two key capabilities for administrators to configure Apache Hadoop when using the Unix Shell:

* Many environment variables that impact how the system operates. This guide will only highlight some key ones. There is generally more information in the various `*-env.sh` files.
* Supplement or do some platform-specific changes to the existing scripts. Apache Hadoop provides the capabilities to do function overrides so that the existing code base may be changed in place without all of that work. Replacing functions is covered later under the Shell API documentation.

### `(command)_(subcommand)_OPTS`

By far, the most important are the series of `_OPTS` variables that control how daemons work. These variables should contain all of the relevant settings for those daemons.

Similar to the user commands above, all daemons will honor the `(command)_(subcommand)_OPTS` pattern. It is generally recommended that these be set in `hadoop-env.sh` to guarantee that the system will know which settings it should use on restart. Unlike user-facing subcommands, daemons will *NOT* honor `HADOOP_CLIENT_OPTS`.

In addition, daemons that run in an extra security mode also support `(command)_(subcommand)_SECURE_EXTRA_OPTS`. These options are *supplemental* to the generic `*_OPTS` and will appear after, therefore generally taking precedence.

### `(command)_(subcommand)_USER`

Apache Hadoop provides a way to do a user check per-subcommand. While this method is easily circumvented and should not be considered a security-feature, it does provide a mechanism by which to prevent accidents. For example, setting `HDFS_NAMENODE_USER=hdfs` will make the `hdfs namenode` and `hdfs --daemon start namenode` commands verify that the user running the commands are the hdfs user by checking the `USER` environment variable. This also works for non-daemons. Setting `HADOOP_DISTCP_USER=jane` will verify that `USER` is set to `jane` before being allowed to execute the `hadoop distcp` command.

If a \_USER environment variable exists and commands are run with a privilege (e.g., as root; see hadoop\_privilege\_check in the API documentation), execution will switch to the specified user first. For commands that support user account switching for security reasons and therefore have a SECURE\_USER variable (see more below), the base \_USER variable needs to be the user that is expected to be used to switch to the SECURE\_USER account. For example:

```
HDFS_DATANODE_USER=root
HDFS_DATANODE_SECURE_USER=hdfs
```

will force ‘hdfs –daemon start datanode’ to be root, but will eventually switch to the hdfs user after the privileged work has been completed.

Be aware that if the --workers flag is used, the user switch happens *after* ssh is invoked. The multi-daemon start and stop commands in sbin will, however, switch (if appropriate) prior and will therefore use the keys of the specified \_USER.

## Developer and Advanced Administrator Environment

### Shell Profiles

Apache Hadoop allows for third parties to easily add new features through a variety of pluggable interfaces. This includes a shell code subsystem that makes it easy to inject the necessary content into the base installation.

Core to this functionality is the concept of a shell profile. Shell profiles are shell snippets that can do things such as add jars to the classpath, configure Java system properties and more.

Shell profiles may be installed in either `${HADOOP_CONF_DIR}/shellprofile.d` or `${HADOOP_HOME}/libexec/shellprofile.d`. Shell profiles in the `libexec` directory are part of the base installation and cannot be overridden by the user. Shell profiles in the configuration directory may be ignored if the end user changes the configuration directory at runtime.

An example of a shell profile is in the libexec directory.

### Shell API

Apache Hadoop’s shell code has a [function library](./UnixShellAPI.html) that is open for administrators and developers to use to assist in their configuration and advanced feature management. These APIs follow the standard [Apache Hadoop Interface Classification](./InterfaceClassification.html), with one addition: Replaceable.

The shell code allows for core functions to be overridden. However, not all functions can be or are safe to be replaced. If a function is not safe to replace, it will have an attribute of Replaceable: No. If a function is safe to replace, it will have the attribute of Replaceable: Yes.

In order to replace a function, create a file called `hadoop-user-functions.sh` in the `${HADOOP_CONF_DIR}` directory. Simply define the new, replacement function in this file and the system will pick it up automatically. There may be as many replacement functions as needed in this file. Examples of function replacement are in the `hadoop-user-functions.sh.example` file.

Functions that are marked Public and Stable are safe to use in shell profiles as-is. Other functions may change in a minor release.

### User-level API Access

In addition to `.hadoop-env`, which allows individual users to override `hadoop-env.sh`, user’s may also use `.hadooprc`. This is called after the Apache Hadoop shell environment has been configured and allows the full set of shell API function calls.

For example:

```
hadoop_add_classpath /some/path/custom.jar
```

would go into `.hadooprc`

### Dynamic Subcommands

Utilizing the Shell API, it is possible for third parties to add their own subcommands to the primary Hadoop shell scripts (hadoop, hdfs, mapred, yarn).

Prior to executing a subcommand, the primary scripts will check for the existence of a (scriptname)\_subcommand\_(subcommand) function. This function gets executed with the parameters set to all remaining command line arguments. For example, if the following function is defined:

```
function yarn_subcommand_hello
{
  echo "$@"
  exit $?
}
```

then executing `yarn --debug hello world I see you` will activate script debugging and call the `yarn_subcommand_hello` function as:

```
yarn_subcommand_hello world I see you
```

which will result in the output of:

```
world I see you
```

It is also possible to add the new subcommands to the usage output. The `hadoop_add_subcommand` function adds text to the usage output. Utilizing the standard HADOOP\_SHELL\_EXECNAME variable, we can limit which command gets our new function.

```
if [[ "${HADOOP_SHELL_EXECNAME}" = "yarn" ]]; then
  hadoop_add_subcommand "hello" client "Print some text to the screen"
fi
```

We set the subcommand type to be “client” as there are no special restrictions, extra capabilities, etc. This functionality may also be use to override the built-ins. For example, defining:

```
function hdfs_subcommand_fetchdt
{
  ...
}
```

… will replace the existing `hdfs fetchdt` subcommand with a custom one.

Some key environment variables for Dynamic Subcommands:

* HADOOP\_CLASSNAME

This is the name of the Java class to use when program execution continues.

* HADOOP\_PRIV\_CLASSNAME

This is the name of the Java class to use when a daemon is expected to be run in a privileged mode. (See more below.)

* HADOOP\_SHELL\_EXECNAME

This is the name of the script that is being executed. It will be one of hadoop, hdfs, mapred, or yarn.

* HADOOP\_SUBCMD

This is the subcommand that was passed on the command line.

* HADOOP\_SUBCMD\_ARGS

This array contains the argument list after the Apache Hadoop common argument processing has taken place and is the same list that is passed to the subcommand function as arguments. For example, if `hadoop --debug subcmd 1 2 3` has been executed on the command line, then `${HADOOP_SUBCMD_ARGS[0]}` will be 1 and `hadoop_subcommand_subcmd` will also have $1 equal to 1. This array list MAY be modified by subcommand functions to add or delete values from the argument list for further processing.

* HADOOP\_SECURE\_CLASSNAME

If this subcommand runs a service that supports the secure mode, this variable should be set to the classname of the secure version.

* HADOOP\_SUBCMD\_SECURESERVICE

Setting this to true will force the subcommand to run in secure mode regardless of hadoop\_detect\_priv\_subcmd. It is expected that HADOOP\_SECURE\_USER will be set to the user that will be executing the final process. See more about secure mode.

* HADOOP\_SUBCMD\_SUPPORTDAEMONIZATION

If this command can be executed as a daemon, set this to true.

* HADOOP\_USER\_PARAMS

This is the full content of the command line, prior to any parsing done. It will contain flags such as `--debug`. It MAY NOT be manipulated.

The Apache Hadoop runtime facilities require functions exit if no further processing is required. For example, in the hello example above, Java and other facilities were not required so a simple `exit $?` was sufficient. However, if the function were to utilize `HADOOP_CLASSNAME`, then program execution must continue so that Java with the Apache Hadoop-specific parameters will be launched against the given Java class. Another example would be in the case of an unrecoverable error. It is the function’s responsibility to print an appropriate message (preferably using the hadoop\_error API call) and exit appropriately.

### Running with Privilege (Secure Mode)

Some daemons, such as the DataNode and the NFS gateway, may be run in a privileged mode. This means that they are expected to be launched as root and (by default) switched to another userid via jsvc. This allows for these daemons to grab a low, privileged port and then drop superuser privileges during normal execution. Running with privilege is also possible for 3rd parties utilizing Dynamic Subcommands. If the following are true:

* (command)\_(subcommand)\_SECURE\_USER environment variable is defined and points to a valid username
* HADOOP\_SECURE\_CLASSNAME is defined and points to a valid Java class

then the shell scripts will attempt to run the class as a command with privilege as it would the built-ins. In general, users are expected to define the \_SECURE\_USER variable and developers define the \_CLASSNAME in their shell script bootstrap.

---
# The Hadoop FileSystem API Definition

This is a specification of the Hadoop FileSystem APIs, which models the contents of a filesystem as a set of paths that are either directories, symbolic links, or files.

There is surprisingly little prior art in this area. There are multiple specifications of Unix filesystems as a tree of inodes, but nothing public which defines the notion of “Unix filesystem as a conceptual model for data storage access”.

This specification attempts to do that; to define the Hadoop FileSystem model and APIs so that multiple filesystems can implement the APIs and present a consistent model of their data to applications. It does not attempt to formally specify any of the concurrency behaviors of the filesystems, other than to document the behaviours exhibited by HDFS as these are commonly expected by Hadoop client applications.

1. [Introduction](introduction.html)
2. [Notation](notation.html)
3. [Model](model.html)
4. [FileSystem class](filesystem.html)
5. [OutputStream, Syncable and `StreamCapabilities`](outputstream.html)
6. [Abortable](abortable.html)
7. [FSDataInputStream class](fsdatainputstream.html)
8. [PathCapabilities interface](pathcapabilities.html)
9. [FSDataOutputStreamBuilder class](fsdataoutputstreambuilder.html)
10. [Testing with the Filesystem specification](testing.html)
11. [Extending the specification and its tests](extending.html)
12. [Uploading a file using Multiple Parts](multipartuploader.html)
13. [IOStatistics](iostatistics.html)
14. [openFile()](openfile.html)
15. [SafeMode](safemode.html)
16. [LeaseRecoverable](leaserecoverable.html)
17. [BulkDelete](bulkdelete.html)

---
# Authentication for Hadoop HTTP web-consoles

* [Introduction](#Introduction)
* [Configuration](#Configuration)
* [CORS](#CORS)
* [Trusted Proxy](#Trusted_Proxy)

## Introduction

This document describes how to configure Hadoop HTTP web-consoles to require user authentication.

By default Hadoop HTTP web-consoles (ResourceManager, NameNode, NodeManagers and DataNodes) allow access without any form of authentication.

Hadoop HTTP web-consoles can be configured to require Kerberos authentication using HTTP SPNEGO protocol (supported by browsers like Firefox and Internet Explorer).

In addition, Hadoop HTTP web-consoles support the equivalent of Hadoop’s Pseudo/Simple authentication. If this option is enabled, the user name must be specified in the first browser interaction using the user.name query string parameter. e.g. `http://localhost:8088/cluster?user.name=babu`.

If a custom authentication mechanism is required for the HTTP web-consoles, it is possible to implement a plugin to support the alternate authentication mechanism (refer to Hadoop hadoop-auth for details on writing an `AuthenticationHandler`).

The next section describes how to configure Hadoop HTTP web-consoles to require user authentication.

## Configuration

The following properties should be in the `core-site.xml` of all the nodes in the cluster.

| Property Name | Default Value | Description |
| --- | --- | --- |
| `hadoop.http.filter.initializers` |  | Add to this property the `org.apache.hadoop.security.AuthenticationFilterInitializer` initializer class. |
| `hadoop.http.authentication.type` | `simple` | Defines authentication used for the HTTP web-consoles. The supported values are: `simple` | `kerberos` | `#AUTHENTICATION_HANDLER_CLASSNAME#`. |
| `hadoop.http.authentication.token.validity` | `36000` | Indicates how long (in seconds) an authentication token is valid before it has to be renewed. |
| `hadoop.http.authentication.token.max-inactive-interval` | `-1` (disabled) | Specifies the time, in seconds, between client requests the server will invalidate the token. |
| `hadoop.http.authentication.signature.secret.file` | `$user.home/hadoop-http-auth-signature-secret` | The signature secret file for signing the authentication tokens. A different secret should be used for each service in the cluster, ResourceManager, NameNode, DataNode and NodeManager. This file should be readable only by the Unix user running the daemons. |
| `hadoop.http.authentication.cookie.domain` |  | The domain to use for the HTTP cookie that stores the authentication token. For authentication to work correctly across all nodes in the cluster the domain must be correctly set. There is no default value, the HTTP cookie will not have a domain working only with the hostname issuing the HTTP cookie. |
| `hadoop.http.authentication.cookie.persistent` | `false` (session cookie) | Specifies the persistence of the HTTP cookie. If the value is true, the cookie is a persistent one. Otherwise, it is a session cookie. *IMPORTANT*: when using IP addresses, browsers ignore cookies with domain settings. For this setting to work properly all nodes in the cluster must be configured to generate URLs with `hostname.domain` names on it. |
| `hadoop.http.authentication.simple.anonymous.allowed` | `true` | Indicates whether anonymous requests are allowed when using ‘simple’ authentication. |
| `hadoop.http.authentication.kerberos.principal` | `HTTP/_HOST@$LOCALHOST` | Indicates the Kerberos principal to be used for HTTP endpoint when using ‘kerberos’ authentication. The principal short name must be `HTTP` per Kerberos HTTP SPNEGO specification. `_HOST` -if present- is replaced with bind address of the HTTP server. |
| `hadoop.http.authentication.kerberos.keytab` | `$user.home/hadoop.keytab` | Location of the keytab file with the credentials for the Kerberos principal used for the HTTP endpoint. |

## CORS

To enable cross-origin support (CORS), please set the following configuration parameters:

Add org.apache.hadoop.security.HttpCrossOriginFilterInitializer to hadoop.http.filter.initializers in core-site.xml. You will also need to set the following properties in core-site.xml -

| Property | Default Value | Description |
| --- | --- | --- |
| hadoop.http.cross-origin.enabled | `false` | Enables cross origin support for all web-services |
| hadoop.http.cross-origin.allowed-origins | `*` | Comma separated list of origins that are allowed. Values prefixed with `regex:` are interpreted as regular expressions. Values containing wildcards (`*`) are possible as well, here a regular expression is generated, the use is discouraged and support is only available for backward compatibility. |
| hadoop.http.cross-origin.allowed-methods | `GET,POST,HEAD` | Comma separated list of methods that are allowed |
| hadoop.http.cross-origin.allowed-headers | `X-Requested-With,Content-Type,Accept,Origin` | Comma separated list of headers that are allowed |
| hadoop.http.cross-origin.max-age | `1800` | Number of seconds a pre-flighted request can be cached |

## Trusted Proxy

Trusted Proxy adds support to perform operations using end user instead of proxy user. It fetches the end user from doAs query parameter. To enable Trusted Proxy, please set the following configuration parameter:

Add org.apache.hadoop.security.authentication.server.ProxyUserAuthenticationFilterInitializer to hadoop.http.filter.initializers in core-site.xml instead of org.apache.hadoop.security.AuthenticationFilterInitializer.

---
* [JvmMetrics](#JvmMetrics)
* [rpc](#rpc)
* [RetryCache/NameNodeRetryCache](#RetryCache.2FNameNodeRetryCache)
* [FairCallQueue](#FairCallQueue)
* [DecayRpcSchedulerDetailed](#DecayRpcSchedulerDetailed)
* [rpcdetailed](#rpcdetailed)
* [namenode](#namenode)
* [FSNamesystem](#FSNamesystem)
* [BlockManager](#BlockManager)
* [JournalNode](#JournalNode)
* [datanode](#datanode)
* [FsVolume](#FsVolume)
* [RBFMetrics](#RBFMetrics)
* [RouterRPCMetrics](#RouterRPCMetrics)
* [StateStoreMetrics](#StateStoreMetrics)
* [ClusterMetrics](#ClusterMetrics)
* [QueueMetrics](#QueueMetrics)
* [NodeManagerMetrics](#NodeManagerMetrics)
* [ContainerMetrics](#ContainerMetrics)
* [UgiMetrics](#UgiMetrics)
* [MetricsSystem](#MetricsSystem)
* [StartupProgress](#StartupProgress)

# Overview

Metrics are statistical information exposed by Hadoop daemons, used for monitoring, performance tuning and debug. There are many metrics available by default and they are very useful for troubleshooting. This page shows the details of the available metrics.

Each section describes each context into which metrics are grouped.

The documentation of Metrics 2.0 framework is [here](../../api/org/apache/hadoop/metrics2/package-summary.html).

# jvm context

## JvmMetrics

Each metrics record contains tags such as ProcessName, SessionID and Hostname as additional information along with metrics.

| Name | Description |
| --- | --- |
| `MemNonHeapUsedM` | Current non-heap memory used in MB |
| `MemNonHeapCommittedM` | Current non-heap memory committed in MB |
| `MemNonHeapMaxM` | Max non-heap memory size in MB |
| `MemHeapUsedM` | Current heap memory used in MB |
| `MemHeapCommittedM` | Current heap memory committed in MB |
| `MemHeapMaxM` | Max heap memory size in MB |
| `MemMaxM` | Max memory size in MB |
| `ThreadsNew` | Current number of NEW threads |
| `ThreadsRunnable` | Current number of RUNNABLE threads |
| `ThreadsBlocked` | Current number of BLOCKED threads |
| `ThreadsWaiting` | Current number of WAITING threads |
| `ThreadsTimedWaiting` | Current number of TIMED\_WAITING threads |
| `ThreadsTerminated` | Current number of TERMINATED threads |
| `GcInfo` | Total GC count and GC time in msec, grouped by the kind of GC.  ex.) GcCountPS Scavenge=6, GCTimeMillisPS Scavenge=40, GCCountPS MarkSweep=0, GCTimeMillisPS MarkSweep=0 |
| `GcCount` | Total GC count |
| `GcTimeMillis` | Total GC time in msec |
| `LogFatal` | Total number of FATAL logs |
| `LogError` | Total number of ERROR logs |
| `LogWarn` | Total number of WARN logs |
| `LogInfo` | Total number of INFO logs |
| `GcNumWarnThresholdExceeded` | Number of times that the GC warn threshold is exceeded |
| `GcNumInfoThresholdExceeded` | Number of times that the GC info threshold is exceeded |
| `GcTotalExtraSleepTime` | Total GC extra sleep time in msec |
| `GcTimePercentage` | The percentage (0..100) of time that the JVM spent in GC pauses within the observation window if `dfs.namenode.gc.time.monitor.enable` is set to true. Use `dfs.namenode.gc.time.monitor.sleep.interval.ms` to specify the sleep interval in msec. Use `dfs.namenode.gc.time.monitor.observation.window.ms` to specify the observation window in msec. |

# rpc context

## rpc

Each metrics record contains tags such as Hostname and port (number to which server is bound) as additional information along with metrics. `rpc.metrics.timeunit` config can be used to configure timeunit for RPC metrics. The default timeunit used for RPC metrics is milliseconds (as per the below description).

| Name | Description |
| --- | --- |
| `ReceivedBytes` | Total number of received bytes |
| `SentBytes` | Total number of sent bytes |
| `RpcQueueTimeNumOps` | Total number of RPC calls |
| `RpcQueueTimeAvgTime` | Average queue time in milliseconds |
| `RpcLockWaitTimeNumOps` | Total number of RPC calls (same as RpcQueueTimeNumOps) |
| `RpcLockWaitTimeAvgTime` | Average time waiting for lock acquisition in milliseconds |
| `RpcProcessingTimeNumOps` | Total number of RPC calls (same to RpcQueueTimeNumOps) |
| `RpcProcessingAvgTime` | Average Processing time in milliseconds |
| `DeferredRpcProcessingTimeNumOps` | Total number of Deferred RPC calls |
| `DeferredRpcProcessingAvgTime` | Average Deferred Processing time in milliseconds |
| `RpcResponseTimeNumOps` | Total number of RPC calls (same to RpcQueueTimeNumOps) |
| `RpcResponseAvgTime` | Average Response time in milliseconds |
| `RpcAuthenticationFailures` | Total number of authentication failures |
| `RpcAuthenticationSuccesses` | Total number of authentication successes |
| `RpcAuthorizationFailures` | Total number of authorization failures |
| `RpcAuthorizationSuccesses` | Total number of authorization successes |
| `RpcClientBackoff` | Total number of client backoff requests |
| `RpcClientBackoffDisconnected` | Total number of client backoff requests that are disconnected. This is a subset of RpcClientBackoff |
| `RpcSlowCalls` | Total number of slow RPC calls |
| `RpcRequeueCalls` | Total number of requeue RPC calls |
| `RpcCallsSuccesses` | Total number of RPC calls that are successfully processed |
| `NumOpenConnections` | Current number of open connections |
| `NumInProcessHandler` | Current number of handlers on working |
| `CallQueueLength` | Current length of the call queue |
| `numDroppedConnections` | Total number of dropped connections |
| `rpcQueueTime`*num*`sNumOps` | Shows total number of RPC calls (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcQueueTime`*num*`s50thPercentileLatency` | Shows the 50th percentile of RPC queue time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcQueueTime`*num*`s75thPercentileLatency` | Shows the 75th percentile of RPC queue time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcQueueTime`*num*`s90thPercentileLatency` | Shows the 90th percentile of RPC queue time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcQueueTime`*num*`s95thPercentileLatency` | Shows the 95th percentile of RPC queue time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcQueueTime`*num*`s99thPercentileLatency` | Shows the 99th percentile of RPC queue time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcProcessingTime`*num*`sNumOps` | Shows total number of RPC calls (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcProcessingTime`*num*`s50thPercentileLatency` | Shows the 50th percentile of RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcProcessingTime`*num*`s75thPercentileLatency` | Shows the 75th percentile of RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcProcessingTime`*num*`s90thPercentileLatency` | Shows the 90th percentile of RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcProcessingTime`*num*`s95thPercentileLatency` | Shows the 95th percentile of RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcProcessingTime`*num*`s99thPercentileLatency` | Shows the 99th percentile of RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcLockWaitTime`*num*`sNumOps` | Shows total number of RPC calls (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcLockWaitTime`*num*`s50thPercentileLatency` | Shows the 50th percentile of RPC lock wait time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcLockWaitTime`*num*`s75thPercentileLatency` | Shows the 75th percentile of RPC lock wait time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcLockWaitTime`*num*`s90thPercentileLatency` | Shows the 90th percentile of RPC lock wait time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcLockWaitTime`*num*`s95thPercentileLatency` | Shows the 95th percentile of RPC lock wait time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcLockWaitTime`*num*`s99thPercentileLatency` | Shows the 99th percentile of RPC lock wait time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcResponseTime`*num*`sNumOps` | Shows total number of RPC calls (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcResponseTime`*num*`s50thPercentileLatency` | Shows the 50th percentile of RPC response time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcResponseTime`*num*`s75thPercentileLatency` | Shows the 75th percentile of RPC response time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcResponseTime`*num*`s90thPercentileLatency` | Shows the 90th percentile of RPC response time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcResponseTime`*num*`s95thPercentileLatency` | Shows the 95th percentile of RPC response time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `rpcResponseTime`*num*`s99thPercentileLatency` | Shows the 99th percentile of RPC response time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `deferredRpcProcessingTime`*num*`sNumOps` | Shows total number of Deferred RPC calls (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `deferredRpcProcessingTime`*num*`s50thPercentileLatency` | Shows the 50th percentile of Deferred RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `deferredRpcProcessingTime`*num*`s75thPercentileLatency` | Shows the 75th percentile of Deferred RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `deferredRpcProcessingTime`*num*`s90thPercentileLatency` | Shows the 90th percentile of Deferred RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `deferredRpcProcessingTime`*num*`s95thPercentileLatency` | Shows the 95th percentile of Deferred RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `deferredRpcProcessingTime`*num*`s99thPercentileLatency` | Shows the 99th percentile of Deferred RPC processing time in milliseconds (*num* seconds granularity) if `rpc.metrics.quantile.enable` is set to true. *num* is specified by `rpc.metrics.percentiles.intervals`. |
| `TotalRequests` | Total num of requests served by the RPC server. |
| `TotalRequestsPerSeconds` | Total num of requests per second served by the RPC server. |

## RetryCache/NameNodeRetryCache

RetryCache metrics is useful to monitor NameNode fail-over. Each metrics record contains Hostname tag.

| Name | Description |
| --- | --- |
| `CacheHit` | Total number of RetryCache hit |
| `CacheCleared` | Total number of RetryCache cleared |
| `CacheUpdated` | Total number of RetryCache updated |

## FairCallQueue

FairCallQueue metrics will only exist if FairCallQueue is enabled. Each metric exists for each level of priority.

| Name | Description |
| --- | --- |
| `FairCallQueueSize_p`*Priority* | Current number of calls in priority queue |
| `FairCallQueueOverflowedCalls_p`*Priority* | Total number of overflowed calls in priority queue |

## DecayRpcSchedulerDetailed

DecayRpcSchedulerDetailed metrics only exist when DecayRpcScheduler is used (FairCallQueue enabled). It is an addition to FairCallQueue metrics. For each level of priority, rpcqueue and rpcprocessing detailed metrics are exposed.

| Name | Description |
| --- | --- |
| `DecayRPCSchedulerPriority.`*Priority*`.RpcQueueTime` | RpcQueueTime metrics for each priority |
| `DecayRPCSchedulerPriority.`*Priority*`.RpcProcessingTime` | RpcProcessingTime metrics for each priority |

# rpcdetailed context

Metrics of rpcdetailed context are exposed in unified manner by RPC layer. Two metrics are exposed for each RPC based on its name. Metrics named “(RPC method name)NumOps” indicates total number of method calls, and metrics named “(RPC method name)AvgTime” shows average processing time for method calls in milliseconds. Please note that the AvgTime metrics do not include time spent waiting to acquire locks on data structures (see RpcLockWaitTimeAvgTime). Metrics named “Overall(RPC method name)AvgTime” shows the average overall processing time for method calls in milliseconds. It is measured from request arrival to when the response is sent back to the client.

## rpcdetailed

Each metrics record contains tags such as Hostname and port (number to which server is bound) as additional information along with metrics.

The Metrics about RPCs which is not called are not included in metrics record.

| Name | Description |
| --- | --- |
| *methodname*`NumOps` | Total number of the times the method is called |
| *methodname*`AvgTime` | Average turn around time of the method in milliseconds |

# dfs context

## namenode

Each metrics record contains tags such as ProcessName, SessionId, and Hostname as additional information along with metrics.

| Name | Description |
| --- | --- |
| `CreateFileOps` | Total number of files created |
| `FilesCreated` | Total number of files and directories created by create or mkdir operations |
| `FilesAppended` | Total number of files appended |
| `GetBlockLocations` | Total number of getBlockLocations operations |
| `FilesRenamed` | Total number of rename **operations** (NOT number of files/dirs renamed) |
| `GetListingOps` | Total number of directory listing operations |
| `DeleteFileOps` | Total number of delete operations |
| `FilesDeleted` | Total number of files and directories deleted by delete or rename operations |
| `FileInfoOps` | Total number of getFileInfo and getLinkFileInfo operations |
| `AddBlockOps` | Total number of addBlock operations succeeded |
| `GetAdditionalDatanodeOps` | Total number of getAdditionalDatanode operations |
| `CreateSymlinkOps` | Total number of createSymlink operations |
| `GetLinkTargetOps` | Total number of getLinkTarget operations |
| `FilesInGetListingOps` | Total number of files and directories listed by directory listing operations |
| `SuccessfulReReplications` | Total number of successful block re-replications |
| `NumTimesReReplicationNotScheduled` | Total number of times that failed to schedule a block re-replication |
| `TimeoutReReplications` | Total number of timed out block re-replications |
| `AllowSnapshotOps` | Total number of allowSnapshot operations |
| `DisallowSnapshotOps` | Total number of disallowSnapshot operations |
| `CreateSnapshotOps` | Total number of createSnapshot operations |
| `DeleteSnapshotOps` | Total number of deleteSnapshot operations |
| `RenameSnapshotOps` | Total number of renameSnapshot operations |
| `ListSnapshottableDirOps` | Total number of snapshottableDirectoryStatus operations |
| `SnapshotDiffReportOps` | Total number of getSnapshotDiffReport operations |
| `TransactionsNumOps` | Total number of Journal transactions |
| `TransactionsAvgTime` | Average time of Journal transactions in milliseconds |
| `SyncsNumOps` | Total number of Journal syncs |
| `SyncsAvgTime` | Average time of Journal syncs in milliseconds |
| `SyncsTime`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of Journal sync time in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `TransactionsBatchedInSync` | Total number of Journal transactions batched in sync |
| `TransactionsBatchedInSync`*num*`s(50/75/90/95/99)thPercentileCount` | The 50/75/90/95/99th percentile of number of batched Journal transactions (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `StorageBlockReportNumOps` | Total number of processing block reports from individual storages in DataNode |
| `StorageBlockReportAvgTime` | Average time of processing block reports in milliseconds |
| `StorageBlockReport`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of block report processing time in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `CacheReportNumOps` | Total number of processing cache reports from DataNode |
| `CacheReportAvgTime` | Average time of processing cache reports in milliseconds |
| `CacheReport`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of cached report processing time in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `SafeModeTime` | The interval between FSNameSystem starts and the last time safemode leaves in milliseconds.  (sometimes not equal to the time in SafeMode, see [HDFS-5156](https://issues.apache.org/jira/browse/HDFS-5156)) |
| `FsImageLoadTime` | Time loading FS Image at startup in milliseconds |
| `GetEditNumOps` | Total number of edits downloads from SecondaryNameNode |
| `GetEditAvgTime` | Average edits download time in milliseconds |
| `GetImageNumOps` | Total number of fsimage downloads from SecondaryNameNode |
| `GetImageAvgTime` | Average fsimage download time in milliseconds |
| `PutImageNumOps` | Total number of fsimage uploads to SecondaryNameNode |
| `PutImageAvgTime` | Average fsimage upload time in milliseconds |
| `TotalFileOps` | Total number of file operations performed |
| `NNStartedTimeInMillis` | NameNode start time in milliseconds |
| `GenerateEDEKTimeNumOps` | Total number of generating EDEK |
| `GenerateEDEKTimeAvgTime` | Average time of generating EDEK in milliseconds |
| `GenerateEDEKTime`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of time spent in generating EDEK in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `WarmUpEDEKTimeNumOps` | Total number of warming up EDEK |
| `WarmUpEDEKTimeAvgTime` | Average time of warming up EDEK in milliseconds |
| `WarmUpEDEKTime`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of time spent in warming up EDEK in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `ResourceCheckTime`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of NameNode resource check latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `EditLogTailTimeNumOps` | Total number of times the standby NameNode tailed the edit log |
| `EditLogTailTimeAvgTime` | Average time (in milliseconds) spent by standby NameNode in tailing edit log |
| `EditLogTailTime`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of time spent in tailing edit logs by standby NameNode in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `EditLogFetchTimeNumOps` | Total number of times the standby NameNode fetched remote edit streams from journal nodes |
| `EditLogFetchTimeAvgTime` | Average time (in milliseconds) spent by standby NameNode in fetching remote edit streams from journal nodes |
| `EditLogFetchTime`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of time spent in fetching edit streams from journal nodes by standby NameNode in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `NumEditLogLoadedNumOps` | Total number of times edits were loaded by standby NameNode |
| `NumEditLogLoadedAvgCount` | Average number of edits loaded by standby NameNode in each edit log tailing |
| `NumEditLogLoaded`*num*`s(50/75/90/95/99)thPercentileCount` | The 50/75/90/95/99th percentile of number of edits loaded by standby NameNode in each edit log tailing (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `EditLogTailIntervalNumOps` | Total number of intervals between edit log tailings by standby NameNode |
| `EditLogTailIntervalAvgTime` | Average time of intervals between edit log tailings by standby NameNode in milliseconds |
| `EditLogTailInterval`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of time between edit log tailings by standby NameNode in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `PendingEditsCount` | Current number of pending edits |

## FSNamesystem

Each metrics record contains tags such as HAState and Hostname as additional information along with metrics.

| Name | Description |
| --- | --- |
| `MissingBlocks` | Current number of missing blocks |
| `ExpiredHeartbeats` | Total number of expired heartbeats |
| `TransactionsSinceLastCheckpoint` | Total number of transactions since last checkpoint |
| `TransactionsSinceLastLogRoll` | Total number of transactions since last edit log roll |
| `LastWrittenTransactionId` | Last transaction ID written to the edit log |
| `LastCheckpointTime` | Time in milliseconds since epoch of last checkpoint |
| `CapacityTotal` | Current raw capacity of DataNodes in bytes |
| `CapacityTotalGB` | Current raw capacity of DataNodes in GB |
| `CapacityUsed` | Current used capacity across all DataNodes in bytes |
| `CapacityUsedGB` | Current used capacity across all DataNodes in GB |
| `CapacityRemaining` | Current remaining capacity in bytes |
| `CapacityRemainingGB` | Current remaining capacity in GB |
| `CapacityUsedNonDFS` | Current space used by DataNodes for non DFS purposes in bytes |
| `TotalLoad` | Current number of connections |
| `SnapshottableDirectories` | Current number of snapshottable directories |
| `Snapshots` | Current number of snapshots |
| `NumEncryptionZones` | Current number of encryption zones |
| `BlocksTotal` | Current number of allocated blocks in the system |
| `FilesTotal` | Current number of files and directories |
| `PendingReplicationBlocks` | Current number of blocks pending to be replicated |
| `UnderReplicatedBlocks` | Current number of blocks under replicated |
| `CorruptBlocks` | Current number of blocks with corrupt replicas. |
| `ScheduledReplicationBlocks` | Current number of blocks scheduled for replications |
| `PendingDeletionBlocks` | Current number of blocks pending deletion |
| `ExcessBlocks` | Current number of excess blocks |
| `PostponedMisreplicatedBlocks` | (HA-only) Current number of blocks postponed to replicate |
| `PendingDataNodeMessageCount` | (HA-only) Current number of pending block-related messages for later processing in the standby NameNode |
| `MillisSinceLastLoadedEdits` | (HA-only) Time in milliseconds since the last time standby NameNode load edit log. In active NameNode, set to 0 |
| `BlockCapacity` | Current number of block capacity |
| `NumLiveDataNodes` | Number of datanodes which are currently live |
| `NumDeadDataNodes` | Number of datanodes which are currently dead |
| `NumDecomLiveDataNodes` | Number of datanodes which have been decommissioned and are now live |
| `NumDecomDeadDataNodes` | Number of datanodes which have been decommissioned and are now dead |
| `NumDecommissioningDataNodes` | Number of datanodes in decommissioning state |
| `VolumeFailuresTotal` | Total number of volume failures across all Datanodes |
| `EstimatedCapacityLostTotal` | An estimate of the total capacity lost due to volume failures |
| `StaleDataNodes` | Current number of DataNodes marked stale due to delayed heartbeat |
| `NumStaleStorages` | Number of storages marked as content stale (after NameNode restart/failover before first block report is received) |
| `MissingReplOneBlocks` | Current number of missing blocks with replication factor 1 |
| `BadlyDistributedBlocks` | Current number of blocks that are badly distributed across racks. |
| `HighestPriorityLowRedundancyReplicatedBlocks` | Current number of non-corrupt, low redundancy replicated blocks with the highest risk of loss (have 0 or 1 replica). Will be recovered with the highest priority. |
| `HighestPriorityLowRedundancyECBlocks` | Current number of non-corrupt, low redundancy EC blocks with the highest risk of loss. Will be recovered with the highest priority. |
| `NumFilesUnderConstruction` | Current number of files under construction |
| `NumActiveClients` | Current number of active clients holding lease |
| `HAState` | (HA-only) Current state of the NameNode: initializing or active or standby or stopping state |
| `FSState` | Current state of the file system: Safemode or Operational |
| `LockQueueLength` | Number of threads waiting to acquire FSNameSystem lock |
| `ReadLockLongHoldCount` | The number of time the read lock has been held for longer than the threshold |
| `WriteLockLongHoldCount` | The number of time the write lock has been held for longer than the threshold |
| `TotalSyncCount` | Total number of sync operations performed by edit log |
| `TotalSyncTimes` | Total number of milliseconds spent by various edit logs in sync operation |
| `NameDirSize` | NameNode name directories size in bytes |
| `NumTimedOutPendingReconstructions` | The number of timed out reconstructions. Not the number of unique blocks that timed out. |
| `NumInMaintenanceLiveDataNodes` | Number of live Datanodes which are in maintenance state |
| `NumInMaintenanceDeadDataNodes` | Number of dead Datanodes which are in maintenance state |
| `NumEnteringMaintenanceDataNodes` | Number of Datanodes that are entering the maintenance state |
| `FSN(Read/Write)Lock`*OperationName*`NanosNumOps` | Total number of acquiring lock by operations |
| `FSN(Read/Write)Lock`*OperationName*`NanosAvgTime` | Average time of holding the lock by operations in nanoseconds |
| `FSN(Read/Write)LockOverallNanosNumOps` | Total number of acquiring lock by all operations |
| `FSN(Read/Write)LockOverallNanosAvgTime` | Average time of holding the lock by all operations in nanoseconds |
| `PendingSPSPaths` | The number of paths to be processed by storage policy satisfier |

## BlockManager

The metrics present statistics from the BlockManager’s perspective.

| Name | Description |
| --- | --- |
| `StorageTypeStats` | key represents different StorageTypes, and value represents the detailed storage information corresponding to each StorageType. |

## JournalNode

The server-side metrics for a journal from the JournalNode’s perspective. Each metrics record contains Hostname tag as additional information along with metrics.

| Name | Description |
| --- | --- |
| `Syncs60sNumOps` | Number of sync operations (1 minute granularity) |
| `Syncs60s50thPercentileLatencyMicros` | The 50th percentile of sync latency in microseconds (1 minute granularity) |
| `Syncs60s75thPercentileLatencyMicros` | The 75th percentile of sync latency in microseconds (1 minute granularity) |
| `Syncs60s90thPercentileLatencyMicros` | The 90th percentile of sync latency in microseconds (1 minute granularity) |
| `Syncs60s95thPercentileLatencyMicros` | The 95th percentile of sync latency in microseconds (1 minute granularity) |
| `Syncs60s99thPercentileLatencyMicros` | The 99th percentile of sync latency in microseconds (1 minute granularity) |
| `Syncs300sNumOps` | Number of sync operations (5 minutes granularity) |
| `Syncs300s50thPercentileLatencyMicros` | The 50th percentile of sync latency in microseconds (5 minutes granularity) |
| `Syncs300s75thPercentileLatencyMicros` | The 75th percentile of sync latency in microseconds (5 minutes granularity) |
| `Syncs300s90thPercentileLatencyMicros` | The 90th percentile of sync latency in microseconds (5 minutes granularity) |
| `Syncs300s95thPercentileLatencyMicros` | The 95th percentile of sync latency in microseconds (5 minutes granularity) |
| `Syncs300s99thPercentileLatencyMicros` | The 99th percentile of sync latency in microseconds (5 minutes granularity) |
| `Syncs3600sNumOps` | Number of sync operations (1 hour granularity) |
| `Syncs3600s50thPercentileLatencyMicros` | The 50th percentile of sync latency in microseconds (1 hour granularity) |
| `Syncs3600s75thPercentileLatencyMicros` | The 75th percentile of sync latency in microseconds (1 hour granularity) |
| `Syncs3600s90thPercentileLatencyMicros` | The 90th percentile of sync latency in microseconds (1 hour granularity) |
| `Syncs3600s95thPercentileLatencyMicros` | The 95th percentile of sync latency in microseconds (1 hour granularity) |
| `Syncs3600s99thPercentileLatencyMicros` | The 99th percentile of sync latency in microseconds (1 hour granularity) |
| `NumTransactionsBatchedInSync60sNumOps` | Number of times transactions were batched in sync operation (1 minute granularity) |
| `NumTransactionsBatchedInSync60s50thPercentileLatencyMicros` | The 50th percentile of transactions batched in sync count (1 minute granularity) |
| `NumTransactionsBatchedInSync60s75thPercentileLatencyMicros` | The 75th percentile of transactions batched in sync count (1 minute granularity) |
| `NumTransactionsBatchedInSync60s90thPercentileLatencyMicros` | The 90th percentile of transactions batched in sync count (1 minute granularity) |
| `NumTransactionsBatchedInSync60s95thPercentileLatencyMicros` | The 95th percentile of transactions batched in sync count (1 minute granularity) |
| `NumTransactionsBatchedInSync60s99thPercentileLatencyMicros` | The 99th percentile of transactions batched in sync count (1 minute granularity) |
| `NumTransactionsBatchedInSync300sNumOps` | Number of times transactions were batched in sync operation (5 minutes granularity) |
| `NumTransactionsBatchedInSync300s50thPercentileLatencyMicros` | The 50th percentile of transactions batched in sync count (5 minutes granularity) |
| `NumTransactionsBatchedInSync300s75thPercentileLatencyMicros` | The 75th percentile of transactions batched in sync count (5 minutes granularity) |
| `NumTransactionsBatchedInSync300s90thPercentileLatencyMicros` | The 90th percentile of transactions batched in sync count (5 minutes granularity) |
| `NumTransactionsBatchedInSync300s95thPercentileLatencyMicros` | The 95th percentile of transactions batched in sync count (5 minutes granularity) |
| `NumTransactionsBatchedInSync300s99thPercentileLatencyMicros` | The 99th percentile of transactions batched in sync count (5 minutes granularity) |
| `NumTransactionsBatchedInSync3600sNumOps` | Number of times transactions were batched in sync operation (1 hour granularity) |
| `NumTransactionsBatchedInSync3600s50thPercentileLatencyMicros` | The 50th percentile of transactions batched in sync count (1 hour granularity) |
| `NumTransactionsBatchedInSync3600s75thPercentileLatencyMicros` | The 75th percentile of transactions batched in sync count (1 hour granularity) |
| `NumTransactionsBatchedInSync3600s90thPercentileLatencyMicros` | The 90th percentile of transactions batched in sync count (1 hour granularity) |
| `NumTransactionsBatchedInSync3600s95thPercentileLatencyMicros` | The 95th percentile of transactions batched in sync count (1 hour granularity) |
| `NumTransactionsBatchedInSync3600s99thPercentileLatencyMicros` | The 99th percentile of transactions batched in sync count (1 hour granularity) |
| `BatchesWritten` | Total number of batches written since startup |
| `TxnsWritten` | Total number of transactions written since startup |
| `BytesWritten` | Total number of bytes written since startup |
| `BatchesWrittenWhileLagging` | Total number of batches written where this node was lagging |
| `LastWriterEpoch` | Current writer’s epoch number |
| `CurrentLagTxns` | The number of transactions that this JournalNode is lagging |
| `LastWrittenTxId` | The highest transaction id stored on this JournalNode |
| `LastPromisedEpoch` | The last epoch number which this node has promised not to accept any lower epoch, or 0 if no promises have been made |
| `LastJournalTimestamp` | The timestamp of last successfully written transaction |
| `TxnsServedViaRpc` | Number of transactions served via the RPC mechanism |
| `BytesServedViaRpc` | Number of bytes served via the RPC mechanism |
| `RpcRequestCacheMissAmountNumMisses` | Number of RPC requests which could not be served due to lack of data in the cache |
| `RpcRequestCacheMissAmountAvgTxns` | The average number of transactions by which a request missed the cache; for example if transaction ID 10 is requested and the cache’s oldest transaction is ID 15, value 5 will be added to this average |
| `RpcEmptyResponses` | Number of RPC requests with zero edits returned |

## datanode

Each metrics record contains tags such as SessionId and Hostname as additional information along with metrics.

| Name | Description |
| --- | --- |
| `BytesWritten` | Total number of bytes written to DataNode |
| `BytesRead` | Total number of bytes read from DataNode |
| `ReadTransferRateNumOps` | Total number of data read transfers |
| `ReadTransferRateAvgTime` | Average transfer rate of bytes read from DataNode, measured in bytes per second. |
| `ReadTransferRate`*num*`s(50/75/90/95/99)thPercentileRate` | The 50/75/90/95/99th percentile of the transfer rate of bytes read from DataNode, measured in bytes per second. |
| `BlocksWritten` | Total number of blocks written to DataNode |
| `BlocksRead` | Total number of blocks read from DataNode |
| `BlocksReplicated` | Total number of blocks replicated |
| `BlocksRemoved` | Total number of blocks removed |
| `BlocksVerified` | Total number of blocks verified |
| `BlockVerificationFailures` | Total number of verifications failures |
| `BlocksCached` | Total number of blocks cached |
| `BlocksUncached` | Total number of blocks uncached |
| `ReadsFromLocalClient` | Total number of read operations from local client |
| `ReadsFromRemoteClient` | Total number of read operations from remote client |
| `WritesFromLocalClient` | Total number of write operations from local client |
| `WritesFromRemoteClient` | Total number of write operations from remote client |
| `BlocksGetLocalPathInfo` | Total number of operations to get local path names of blocks |
| `RamDiskBlocksWrite` | Total number of blocks written to memory |
| `RamDiskBlocksWriteFallback` | Total number of blocks written to memory but not satisfied (failed-over to disk) |
| `RamDiskBytesWrite` | Total number of bytes written to memory |
| `RamDiskBlocksReadHits` | Total number of times a block in memory was read |
| `RamDiskBlocksEvicted` | Total number of blocks evicted in memory |
| `RamDiskBlocksEvictedWithoutRead` | Total number of blocks evicted in memory without ever being read from memory |
| `RamDiskBlocksEvictionWindowMsNumOps` | Number of blocks evicted in memory |
| `RamDiskBlocksEvictionWindowMsAvgTime` | Average time of blocks in memory before being evicted in milliseconds |
| `RamDiskBlocksEvictionWindows`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of latency between memory write and eviction in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `RamDiskBlocksLazyPersisted` | Total number of blocks written to disk by lazy writer |
| `RamDiskBlocksDeletedBeforeLazyPersisted` | Total number of blocks deleted by application before being persisted to disk |
| `RamDiskBytesLazyPersisted` | Total number of bytes written to disk by lazy writer |
| `RamDiskBlocksLazyPersistWindowMsNumOps` | Number of blocks written to disk by lazy writer |
| `RamDiskBlocksLazyPersistWindowMsAvgTime` | Average time of blocks written to disk by lazy writer in milliseconds |
| `RamDiskBlocksLazyPersistWindows`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of latency between memory write and disk persist in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `FsyncCount` | Total number of fsync |
| `VolumeFailures` | Total number of volume failures occurred |
| `DatanodeNetworkErrors` | Count of network errors on the datanode |
| `DataNodeActiveXceiversCount` | Count of active dataNode xceivers |
| `DataNodeReadActiveXceiversCount` | Count of read active dataNode xceivers |
| `DataNodeWriteActiveXceiversCount` | Count of write active dataNode xceivers |
| `DataNodePacketResponderCount` | Count of active DataNode packetResponder |
| `DataNodeBlockRecoveryWorkerCount` | Count of active DataNode block recovery worker |
| `ReadBlockOpNumOps` | Total number of read operations |
| `ReadBlockOpAvgTime` | Average time of read operations in milliseconds |
| `WriteBlockOpNumOps` | Total number of write operations |
| `WriteBlockOpAvgTime` | Average time of write operations in milliseconds |
| `BlockChecksumOpNumOps` | Total number of blockChecksum operations |
| `BlockChecksumOpAvgTime` | Average time of blockChecksum operations in milliseconds |
| `CopyBlockOpNumOps` | Total number of block copy operations |
| `CopyBlockOpAvgTime` | Average time of block copy operations in milliseconds |
| `ReplaceBlockOpNumOps` | Total number of block replace operations |
| `ReplaceBlockOpAvgTime` | Average time of block replace operations in milliseconds |
| `HeartbeatsNumOps` | Total number of heartbeats |
| `HeartbeatsAvgTime` | Average heartbeat time in milliseconds |
| `HeartbeatsFor`*ServiceId*`-`*NNId*`NumOps` | Total number of heartbeats to specific serviceId and nnId |
| `HeartbeatsFor`*ServiceId*`-`*NNId*`AvgTime` | Average heartbeat time in milliseconds to specific serviceId and nnId |
| `HeartbeatsTotalNumOps` | Total number of heartbeats which is a duplicate of HeartbeatsNumOps |
| `HeartbeatsTotalAvgTime` | Average total heartbeat time in milliseconds |
| `HeartbeatsTotalFor`*ServiceId*`-`*NNId*`NumOps` | Total number of heartbeats to specific serviceId and nnId which is a duplicate of `HeartbeatsFor`*ServiceId*`-`*NNId*`NumOps` |
| `HeartbeatsTotalFor`*ServiceId*`-`*NNId*`AvgTime` | Average total heartbeat time in milliseconds to specific serviceId and nnId |
| `LifelinesNumOps` | Total number of lifeline messages |
| `LifelinesAvgTime` | Average lifeline message processing time in milliseconds |
| `LifelinesFor`*ServiceId*`-`*NNId*`NumOps` | Total number of lifeline messages to specific serviceId and nnId |
| `LifelinesFor`*ServiceId*`-`*NNId*`AvgTime` | Average lifeline message processing time to specific serviceId and nnId in milliseconds |
| `BlockReportsNumOps` | Total number of block report operations |
| `BlockReportsAvgTime` | Average time of block report operations in milliseconds |
| `BlockReports`*ServiceId*`-`*NNId*`NumOps` | Total number of block report operations to specific serviceId and nnId |
| `BlockReports`*ServiceId*`-`*NNId*`AvgTime` | Average time of block report operations to specific serviceId and nnId in milliseconds |
| `BlockReportsCreateCostMillsNumOps` | Total number of block report creating operations |
| `BlockReportsCreateCostMillsAvgTime` | Average time of block report creating operations in milliseconds |
| `IncrementalBlockReportsNumOps` | Total number of incremental block report operations |
| `IncrementalBlockReportsAvgTime` | Average time of incremental block report operations in milliseconds |
| `IncrementalBlockReports`*ServiceId*`-`*NNId*`NumOps` | Total number of incremental block report operations to specific serviceId and nnId |
| `IncrementalBlockReports`*ServiceId*`-`*NNId*`AvgTime` | Average time of incremental block report operations to specific serviceId and nnId in milliseconds |
| `CacheReportsNumOps` | Total number of cache report operations |
| `CacheReportsAvgTime` | Average time of cache report operations in milliseconds |
| `PacketAckRoundTripTimeNanosNumOps` | Total number of ack round trip |
| `PacketAckRoundTripTimeNanosAvgTime` | Average time from ack send to receive minus the downstream ack time in nanoseconds |
| `PacketAckRoundTripTimeNanos`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile latency from ack send to receive minus the downstream ack time in nanoseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `FlushNanosNumOps` | Total number of flushes |
| `FlushNanosAvgTime` | Average flush time in nanoseconds |
| `FlushNanos`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile flush time in nanoseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `FsyncNanosNumOps` | Total number of fsync |
| `FsyncNanosAvgTime` | Average fsync time in nanoseconds |
| `FsyncNanos`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile fsync time in nanoseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `SendDataPacketBlockedOnNetworkNanosNumOps` | Total number of sending packets |
| `SendDataPacketBlockedOnNetworkNanosAvgTime` | Average waiting time of sending packets in nanoseconds |
| `SendDataPacketBlockedOnNetworkNanos`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile waiting time of sending packets in nanoseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `SendDataPacketTransferNanosNumOps` | Total number of sending packets |
| `SendDataPacketTransferNanosAvgTime` | Average transfer time of sending packets in nanoseconds |
| `SendDataPacketTransferNanos`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile transfer time of sending packets in nanoseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `TotalWriteTime` | Total number of milliseconds spent on write operation |
| `TotalReadTime` | Total number of milliseconds spent on read operation |
| `RemoteBytesRead` | Number of bytes read by remote clients |
| `RemoteBytesWritten` | Number of bytes written by remote clients |
| `BPServiceActorInfo` | The information about a block pool service actor |
| `BlocksInPendingIBR` | Number of blocks in pending incremental block report (IBR) |
| `BlocksReceivingInPendingIBR` | Number of blocks at receiving status in pending incremental block report (IBR) |
| `BlocksReceivedInPendingIBR` | Number of blocks at received status in pending incremental block report (IBR) |
| `BlocksDeletedInPendingIBR` | Number of blocks at deleted status in pending incremental block report (IBR) |
| `EcReconstructionTasks` | Total number of erasure coding reconstruction tasks |
| `EcFailedReconstructionTasks` | Total number of erasure coding failed reconstruction tasks |
| `EcInvalidReconstructionTasks` | Total number of erasure coding invalidated reconstruction tasks |
| `EcDecodingTimeNanos` | Total number of nanoseconds spent by decoding tasks |
| `EcReconstructionBytesRead` | Total number of bytes read by erasure coding worker |
| `EcReconstructionBytesWritten` | Total number of bytes written by erasure coding worker |
| `EcReconstructionRemoteBytesRead` | Total number of bytes remote read by erasure coding worker |
| `CreateRbwOpNumOps` | Total number of create rbw operations |
| `CreateRbwOpAvgTime` | Average time of create rbw operations in milliseconds |
| `RecoverRbwOpNumOps` | Total number of recovery rbw operations |
| `RecoverRbwOpAvgTime` | Average time of recovery rbw operations in milliseconds |
| `ConvertTemporaryToRbwOpNumOps` | Total number of convert temporary to rbw operations |
| `ConvertTemporaryToRbwOpAvgTime` | Average time of convert temporary to rbw operations in milliseconds |
| `CreateTemporaryOpNumOps` | Total number of create temporary operations |
| `CreateTemporaryOpAvgTime` | Average time of create temporary operations in milliseconds |
| `FinalizeBlockOpNumOps` | Total number of finalize block operations |
| `FinalizeBlockOpAvgTime` | Average time of finalize block operations in milliseconds |
| `UnfinalizeBlockOpNumOps` | Total number of un-finalize block operations |
| `UnfinalizeBlockOpAvgTime` | Average time of un-finalize block operations in milliseconds |
| `CheckAndUpdateOpNumOps` | Total number of check and update operations |
| `CheckAndUpdateOpAvgTime` | Average time of check and update operations in milliseconds |
| `UpdateReplicaUnderRecoveryOpNumOps` | Total number of update replica under recovery operations |
| `UpdateReplicaUnderRecoveryOpAvgTime` | Average time of update replica under recovery operations in milliseconds |
| `PacketsReceived` | Total number of packets received by Datanode (excluding heartbeat packet from client) |
| `PacketsSlowWriteToMirror` | Total number of packets whose write to other Datanodes in the pipeline takes more than a certain time (300ms by default) |
| `PacketsSlowWriteToDisk` | Total number of packets whose write to disk takes more than a certain time (300ms by default) |
| `PacketsSlowWriteToOsCache` | Total number of packets whose write to os cache takes more than a certain time (300ms by default) |
| `SlowFlushOrSyncCount` | Total number of packets whose sync/flush takes more than a certain time (300ms by default) |
| `SlowAckToUpstreamCount` | Total number of packets whose upstream ack takes more than a certain time (300ms by default) |
| `SumOfActorCommandQueueLength` | Sum of all BPServiceActors command queue length |
| `NumProcessedCommands` | Num of processed commands of all BPServiceActors |
| `ProcessedCommandsOpNumOps` | Total number of processed commands operations |
| `ProcessedCommandsOpAvgTime` | Average time of processed commands operations in milliseconds |
| `NullStorageBlockReports` | Number of blocks in IBRs that failed due to null storage |
| `AcquireDatasetReadLockNumOps` | Total number of acquiring dataset read lock operations |
| `AcquireDatasetReadLockAvgTime` | Average time of acquiring dataset read lock operations in nanoseconds |
| `AcquireDatasetWriteLockNumOps` | Total number of acquiring dataset write lock operations |
| `AcquireDatasetWriteLockAvgTime` | Average time of acquiring dataset write lock operations in nanoseconds |

## FsVolume

Per-volume metrics contain Datanode Volume IO related statistics. Per-volume metrics are off by default. They can be enabled by setting `dfs.datanode .fileio.profiling.percentage.fraction` to an integer value between 1 and 100. Setting this value to 0 would mean profiling is not enabled. But enabling per-volume metrics may have a performance impact. Each metrics record contains tags such as Hostname as additional information along with metrics.

| Name | Description |
| --- | --- |
| `TotalMetadataOperations` | Total number (monotonically increasing) of metadata operations. Metadata operations include stat, list, mkdir, delete, move, open and posix\_fadvise. |
| `MetadataOperationRateNumOps` | The number of metadata operations within an interval time of metric |
| `MetadataOperationRateAvgTime` | Mean time of metadata operations in milliseconds |
| `MetadataOperationLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of metadata operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `TotalDataFileIos` | Total number (monotonically increasing) of data file io operations |
| `DataFileIoRateNumOps` | The number of data file io operations within an interval time of metric |
| `DataFileIoRateAvgTime` | Mean time of data file io operations in milliseconds |
| `DataFileIoLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of data file io operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `FlushIoRateNumOps` | The number of file flush io operations within an interval time of metric |
| `FlushIoRateAvgTime` | Mean time of file flush io operations in milliseconds |
| `FlushIoLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of file flush io operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `SyncIoRateNumOps` | The number of file sync io operations within an interval time of metric |
| `SyncIoRateAvgTime` | Mean time of file sync io operations in milliseconds |
| `SyncIoLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of file sync io operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `ReadIoRateNumOps` | The number of file read io operations within an interval time of metric |
| `ReadIoRateAvgTime` | Mean time of file read io operations in milliseconds |
| `ReadIoLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of file read io operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `WriteIoRateNumOps` | The number of file write io operations within an interval time of metric |
| `WriteIoRateAvgTime` | Mean time of file write io operations in milliseconds |
| `WriteIoLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of file write io operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `TransferIoRateNumOps` | The number of file transfer io operations within an interval time of metric |
| `TransferIoRateAvgTime` | Mean time of file transfer io operations in milliseconds |
| `TransferIoLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of file transfer io operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `NativeCopyIoRateNumOps` | The number of file nativeCopy io operations within an interval time of metric |
| `NativeCopyIoRateAvgTime` | Mean time of file nativeCopy io operations in milliseconds |
| `NativeCopyIoLatency`*num*`s(50/75/90/95/99)thPercentileLatency` | The 50/75/90/95/99th percentile of file nativeCopy io operations latency in milliseconds (*num* seconds granularity). Percentile measurement is off by default, by watching no intervals. The intervals are specified by `dfs.metrics.percentiles.intervals`. |
| `TotalFileIoErrors` | Total number (monotonically increasing) of file io error operations |
| `FileIoErrorRateNumOps` | The number of file io error operations within an interval time of metric |
| `FileIoErrorRateAvgTime` | It measures the mean time in milliseconds from the start of an operation to hitting a failure |

## RBFMetrics

RBFMetrics shows the metrics which are the aggregated values of sub-clusters’ information in the Router-based federation.

| Name | Description |
| --- | --- |
| `NumFiles` | Current number of files and directories |
| `NumBlocks` | Current number of allocated blocks |
| `NumOfBlocksPendingReplication` | Current number of blocks pending to be replicated |
| `NumOfBlocksUnderReplicated` | Current number of blocks under replicated |
| `NumOfBlocksPendingDeletion` | Current number of blocks pending deletion |
| `ProvidedSpace` | The total remote storage capacity mounted in the federated cluster |
| `NumInMaintenanceLiveDataNodes` | Number of live Datanodes which are in maintenance state |
| `NumInMaintenanceDeadDataNodes` | Number of dead Datanodes which are in maintenance state |
| `NumEnteringMaintenanceDataNodes` | Number of Datanodes that are entering the maintenance state |
| `TotalCapacity` | Current raw capacity of DataNodes in bytes (long primitive, may overflow) |
| `UsedCapacity` | Current used capacity across all DataNodes in bytes (long primitive, may overflow) |
| `RemainingCapacity` | Current remaining capacity in bytes (long primitive, may overflow) |
| `TotalCapacityBigInt` | Current raw capacity of DataNodes in bytes (using BigInteger) |
| `UsedCapacityBigInt` | Current used capacity across all DataNodes in bytes (using BigInteger) |
| `RemainingCapacityBigInt` | Current remaining capacity in bytes (using BigInteger) |
| `NumOfMissingBlocks` | Current number of missing blocks |
| `NumLiveNodes` | Number of datanodes which are currently live |
| `NumDeadNodes` | Number of datanodes which are currently dead |
| `NumStaleNodes` | Current number of DataNodes marked stale due to delayed heartbeat |
| `NumDecomLiveNodes` | Number of datanodes which have been decommissioned and are now live |
| `NumDecomDeadNodes` | Number of datanodes which have been decommissioned and are now dead |
| `NumDecommissioningNodes` | Number of datanodes in decommissioning state |
| `Namenodes` | Current information about all the namenodes |
| `Nameservices` | Current information for each registered nameservice |
| `MountTable` | The mount table for the federated filesystem |
| `Routers` | Current information about all routers |
| `NumNameservices` | Number of nameservices |
| `NumNamenodes` | Number of namenodes |
| `NumExpiredNamenodes` | Number of expired namenodes |
| `NodeUsage` | Max, Median, Min and Standard Deviation of DataNodes usage |

## RouterRPCMetrics

RouterRPCMetrics shows the statistics of the Router component in Router-based federation.

| Name | Description |
| --- | --- |
| `ProcessingOp` | Number of operations the Router processed internally |
| `ProxyOp` | Number of operations the Router proxied to a Namenode |
| `ProxyOpFailureStandby` | Number of operations to hit a standby NN |
| `ProxyOpFailureCommunicate` | Number of operations to fail to reach NN |
| `ProxyOpNotImplemented` | Number of operations not implemented |
| `RouterFailureStateStore` | Number of failed requests due to State Store unavailable |
| `RouterFailureReadOnly` | Number of failed requests due to read only mount point |
| `RouterFailureLocked` | Number of failed requests due to locked path |
| `RouterFailureSafemode` | Number of failed requests due to safe mode |
| `ProcessingNumOps` | Number of operations the Router processed internally within an interval time of metric |
| `ProcessingAvgTime` | Average time for the Router to process operations in milliseconds |
| `ProxyNumOps` | Number of times of that the Router to proxy operations to the Namenodes within an interval time of metric |
| `ProxyAvgTime` | Average time for the Router to proxy operations to the Namenodes in milliseconds |

## StateStoreMetrics

StateStoreMetrics shows the statistics of the State Store component in Router-based federation.

| Name | Description |
| --- | --- |
| `ReadsNumOps` | Number of GET transactions for State Store within an interval time of metric |
| `ReadsAvgTime` | Average time of GET transactions for State Store in milliseconds |
| `WritesNumOps` | Number of PUT transactions for State Store within an interval time of metric |
| `WritesAvgTime` | Average time of PUT transactions for State Store in milliseconds |
| `RemovesNumOps` | Number of REMOVE transactions for State Store within an interval time of metric |
| `RemovesAvgTime` | Average time of REMOVE transactions for State Store in milliseconds |
| `FailuresNumOps` | Number of failed transactions for State Store within an interval time of metric |
| `FailuresAvgTime` | Average time of failed transactions for State Store in milliseconds |
| `Cache`*BaseRecord*`Size` | Number of store records to cache in State Store |
| `Cache`*BaseRecord*`LoadNumOps` | Number of times store records are loaded in the State Store Cache from State Store |
| `Cache`*BaseRecord*`LoadAvgTime` | Average time of loading State Store Cache from State Store in milliseconds |

# yarn context

## ClusterMetrics

ClusterMetrics shows the metrics of the YARN cluster from the ResourceManager’s perspective. Each metrics record contains Hostname tag as additional information along with metrics.

| Name | Description |
| --- | --- |
| `NumActiveNMs` | Current number of active NodeManagers |
| `numDecommissioningNMs` | Current number of NodeManagers being decommissioned |
| `NumDecommissionedNMs` | Current number of decommissioned NodeManagers |
| `NumShutdownNMs` | Current number of NodeManagers shut down gracefully. Note that this does not count NodeManagers that are forcefully killed. |
| `NumLostNMs` | Current number of lost NodeManagers for not sending heartbeats. |
| `NumUnhealthyNMs` | Current number of unhealthy NodeManagers |
| `NumRebootedNMs` | Current number of rebooted NodeManagers |
| `AMLaunchDelayNumOps` | Total number of AMs launched |
| `AMLaunchDelayAvgTime` | Average time in milliseconds RM spends to launch AM containers after the AM container is allocated |
| `AMRegisterDelayNumOps` | Total number of AMs registered |
| `AMRegisterDelayAvgTime` | Average time in milliseconds AM spends to register with RM after the AM container gets launched |

## QueueMetrics

QueueMetrics shows an application queue from the ResourceManager’s perspective. Each metrics record shows the statistics of each queue, and contains tags such as queue name and Hostname as additional information along with metrics.

In `running_`*num* metrics such as `running_0`, you can set the property `yarn.resourcemanager.metrics.runtime.buckets` in yarn-site.xml to change the buckets. The default values is `60,300,1440`.

| Name | Description |
| --- | --- |
| `running_0` | Current number of running applications whose elapsed time are less than 60 minutes |
| `running_60` | Current number of running applications whose elapsed time are between 60 and 300 minutes |
| `running_300` | Current number of running applications whose elapsed time are between 300 and 1440 minutes |
| `running_1440` | Current number of running applications elapsed time are more than 1440 minutes |
| `AppsSubmitted` | Total number of submitted applications |
| `AppsRunning` | Current number of running applications |
| `AppsPending` | Current number of applications that have not yet been assigned by any containers |
| `AppsCompleted` | Total number of completed applications |
| `AppsKilled` | Total number of killed applications |
| `AppsFailed` | Total number of failed applications |
| `AllocatedMB` | Current allocated memory in MB |
| `AllocatedVCores` | Current allocated CPU in virtual cores |
| `AllocatedContainers` | Current number of allocated containers |
| `AggregateContainersAllocated` | Total number of allocated containers |
| `aggregateNodeLocalContainersAllocated` | Total number of node local containers allocated |
| `aggregateRackLocalContainersAllocated` | Total number of rack local containers allocated |
| `aggregateOffSwitchContainersAllocated` | Total number of off switch containers allocated |
| `AggregateContainersReleased` | Total number of released containers |
| `AvailableMB` | Current available memory in MB |
| `AvailableVCores` | Current available CPU in virtual cores |
| `PendingMB` | Current memory requests in MB that are pending to be fulfilled by the scheduler |
| `PendingVCores` | Current CPU requests in virtual cores that are pending to be fulfilled by the scheduler |
| `PendingContainers` | Current number of containers that are pending to be fulfilled by the scheduler |
| `ReservedMB` | Current reserved memory in MB |
| `ReservedVCores` | Current reserved CPU in virtual cores |
| `ReservedContainers` | Current number of reserved containers |
| `ActiveUsers` | Current number of active users |
| `ActiveApplications` | Current number of active applications |
| `AppAttemptFirstContainerAllocationDelayNumOps` | Total number of first container allocated for all attempts |
| `AppAttemptFirstContainerAllocationDelayAvgTime` | Average time RM spends to allocate the first container for all attempts. For managed AM, the first container is AM container. So, this indicates the time duration to allocate AM container. For unmanaged AM, this is the time duration to allocate the first container asked by unmanaged AM. |
| `FairShareMB` | (FairScheduler only) Current fair share of memory in MB |
| `FairShareVCores` | (FairScheduler only) Current fair share of CPU in virtual cores |
| `MinShareMB` | (FairScheduler only) Minimum share of memory in MB |
| `MinShareVCores` | (FairScheduler only) Minimum share of CPU in virtual cores |
| `MaxShareMB` | (FairScheduler only) Maximum share of memory in MB |
| `MaxShareVCores` | (FairScheduler only) Maximum share of CPU in virtual cores |

## NodeManagerMetrics

NodeManagerMetrics shows the statistics of the containers in the node. Each metrics record contains Hostname tag as additional information along with metrics.

| Name | Description |
| --- | --- |
| `containersLaunched` | Total number of launched containers |
| `containersCompleted` | Total number of successfully completed containers |
| `containersFailed` | Total number of failed containers |
| `containersKilled` | Total number of killed containers |
| `containersIniting` | Current number of initializing containers |
| `containersRunning` | Current number of running containers |
| `allocatedContainers` | Current number of allocated containers |
| `allocatedGB` | Current allocated memory in GB |
| `availableGB` | Current available memory in GB |
| `allocatedVcores` | Current used vcores |
| `availableVcores` | Current available vcores |
| `containerLaunchDuration` | Average time duration in milliseconds NM takes to launch a container |
| `badLocalDirs` | Current number of bad local directories. Currently, a disk that cannot be read/written/executed by NM process or A disk being full is considered as bad. |
| `badLogDirs` | Current number of bad log directories. Currently, a disk that cannot be read/written/executed by NM process or A disk being full is considered as bad. |
| `goodLocalDirsDiskUtilizationPerc` | Current disk utilization percentage across all good local directories |
| `goodLogDirsDiskUtilizationPerc` | Current disk utilization percentage across all good log directories |

## ContainerMetrics

ContainerMetrics shows the resource utilization statistics of a container. Each metrics record contains tags such as ContainerPid and Hostname as additional information along with metrics.

| Name | Description |
| --- | --- |
| `pMemLimitMBs` | Physical memory limit of the container in MB |
| `vMemLimitMBs` | Virtual memory limit of the container in MB |
| `vCoreLimit` | CPU limit of the container in number of vcores |
| `launchDurationMs` | Container launch duration in msec |
| `localizationDurationMs` | Container localization duration in msec |
| `StartTime` | Time in msec when container starts |
| `FinishTime` | Time in msec when container finishes |
| `ExitCode` | Container’s exit code |
| `PMemUsageMBsNumUsage` | Total number of physical memory used metrics |
| `PMemUsageMBsAvgMBs` | Average physical memory used in MB |
| `PMemUsageMBsStdevMBs` | Standard deviation of the physical memory used in MB |
| `PMemUsageMBsMinMBs` | Minimum physical memory used in MB |
| `PMemUsageMBsMaxMBs` | Maximum physical memory used in MB |
| `PMemUsageMBsIMinMBs` | Minimum physical memory used in MB of current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `PMemUsageMBsIMaxMBs` | Maximum physical memory used in MB of current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `PMemUsageMBsINumUsage` | Total number of physical memory used metrics in current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `PCpuUsagePercentNumUsage` | Total number of physical CPU cores percent used metrics |
| `PCpuUsagePercentAvgPercents` | Average physical CPU cores percent used |
| `PCpuUsagePercentStdevPercents` | Standard deviation of physical CPU cores percent used |
| `PCpuUsagePercentMinPercents` | Minimum physical CPU cores percent used |
| `PCpuUsagePercentMaxPercents` | Maximum physical CPU cores percent used |
| `PCpuUsagePercentIMinPercents` | Minimum physical CPU cores percent used in current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `PCpuUsagePercentIMaxPercents` | Maximum physical CPU cores percent used in current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `PCpuUsagePercentINumUsage` | Total number of physical CPU cores used metrics in current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `MilliVcoreUsageNumUsage` | Total number of vcores used metrics |
| `MilliVcoreUsageAvgMilliVcores` | 1000 times the average vcores used |
| `MilliVcoreUsageStdevMilliVcores` | 1000 times the standard deviation of vcores used |
| `MilliVcoreUsageMinMilliVcores` | 1000 times the minimum vcores used |
| `MilliVcoreUsageMaxMilliVcores` | 1000 times the maximum vcores used |
| `MilliVcoreUsageIMinMilliVcores` | 1000 times the average vcores used in current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `MilliVcoreUsageIMaxMilliVcores` | 1000 times the maximum vcores used in current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `MilliVcoreUsageINumUsage` | Total number of vcores used metrics in current *interval* (the time of *interval* is specified by yarn.nodemanager.container-metrics.period-ms) |
| `PMemUsageMBHistogramNumUsage` | Total number of physical memory used metrics (1 second granularity) |
| `PMemUsageMBHistogram50thPercentileMBs` | The 50th percentile of physical memory used in MB (1 second granularity) |
| `PMemUsageMBHistogram75thPercentileMBs` | The 75th percentile of physical memory used in MB (1 second granularity) |
| `PMemUsageMBHistogram90thPercentileMBs` | The 90th percentile of physical memory used in MB (1 second granularity) |
| `PMemUsageMBHistogram95thPercentileMBs` | The 95th percentile of physical memory used in MB (1 second granularity) |
| `PMemUsageMBHistogram99thPercentileMBs` | The 99th percentile of physical memory used in MB (1 second granularity) |
| `PCpuUsagePercentHistogramNumUsage` | Total number of physical CPU cores used metrics (1 second granularity) |
| `PCpuUsagePercentHistogram50thPercentilePercents` | The 50th percentile of physical CPU cores percent used (1 second granularity) |
| `PCpuUsagePercentHistogram75thPercentilePercents` | The 75th percentile of physical CPU cores percent used (1 second granularity) |
| `PCpuUsagePercentHistogram90thPercentilePercents` | The 90th percentile of physical CPU cores percent used (1 second granularity) |
| `PCpuUsagePercentHistogram95thPercentilePercents` | The 95th percentile of physical CPU cores percent used (1 second granularity) |
| `PCpuUsagePercentHistogram99thPercentilePercents` | The 99th percentile of physical CPU cores percent used (1 second granularity) |

# ugi context

## UgiMetrics

UgiMetrics is related to user and group information. Each metrics record contains Hostname tag as additional information along with metrics.

| Name | Description |
| --- | --- |
| `LoginSuccessNumOps` | Total number of successful kerberos logins |
| `LoginSuccessAvgTime` | Average time for successful kerberos logins in milliseconds |
| `LoginFailureNumOps` | Total number of failed kerberos logins |
| `LoginFailureAvgTime` | Average time for failed kerberos logins in milliseconds |
| `getGroupsNumOps` | Total number of group resolutions |
| `getGroupsAvgTime` | Average time for group resolution in milliseconds |
| `getGroups`*num*`sNumOps` | Total number of group resolutions (*num* seconds granularity). *num* is specified by `hadoop.user.group.metrics.percentiles.intervals`. |
| `getGroups`*num*`s50thPercentileLatency` | Shows the 50th percentile of group resolution time in milliseconds (*num* seconds granularity). *num* is specified by `hadoop.user.group.metrics.percentiles.intervals`. |
| `getGroups`*num*`s75thPercentileLatency` | Shows the 75th percentile of group resolution time in milliseconds (*num* seconds granularity). *num* is specified by `hadoop.user.group.metrics.percentiles.intervals`. |
| `getGroups`*num*`s90thPercentileLatency` | Shows the 90th percentile of group resolution time in milliseconds (*num* seconds granularity). *num* is specified by `hadoop.user.group.metrics.percentiles.intervals`. |
| `getGroups`*num*`s95thPercentileLatency` | Shows the 95th percentile of group resolution time in milliseconds (*num* seconds granularity). *num* is specified by `hadoop.user.group.metrics.percentiles.intervals`. |
| `getGroups`*num*`s99thPercentileLatency` | Shows the 99th percentile of group resolution time in milliseconds (*num* seconds granularity). *num* is specified by `hadoop.user.group.metrics.percentiles.intervals`. |

# metricssystem context

## MetricsSystem

MetricsSystem shows the statistics for metrics snapshots and publishes. Each metrics record contains Hostname tag as additional information along with metrics.

| Name | Description |
| --- | --- |
| `NumActiveSources` | Current number of active metrics sources |
| `NumAllSources` | Total number of metrics sources |
| `NumActiveSinks` | Current number of active sinks |
| `NumAllSinks` | Total number of sinks  (BUT usually less than `NumActiveSinks`, see [HADOOP-9946](https://issues.apache.org/jira/browse/HADOOP-9946)) |
| `SnapshotNumOps` | Total number of operations to snapshot statistics from a metrics source |
| `SnapshotAvgTime` | Average time in milliseconds to snapshot statistics from a metrics source |
| `PublishNumOps` | Total number of operations to publish statistics to a sink |
| `PublishAvgTime` | Average time in milliseconds to publish statistics to a sink |
| `DroppedPubAll` | Total number of dropped publishes |
| `Sink_`*instance*`NumOps` | Total number of sink operations for the *instance* |
| `Sink_`*instance*`AvgTime` | Average time in milliseconds of sink operations for the *instance* |
| `Sink_`*instance*`Dropped` | Total number of dropped sink operations for the *instance* |
| `Sink_`*instance*`Qsize` | Current queue length of sink operations |

# default context

## StartupProgress

StartupProgress metrics shows the statistics of NameNode startup. Four metrics are exposed for each startup phase based on its name. The startup *phase*s are `LoadingFsImage`, `LoadingEdits`, `SavingCheckpoint`, and `SafeMode`. Each metrics record contains Hostname tag as additional information along with metrics.

| Name | Description |
| --- | --- |
| `ElapsedTime` | Total elapsed time in milliseconds |
| `PercentComplete` | Current rate completed in NameNode startup progress  (The max value is not 100 but 1.0) |
| *phase*`Count` | Total number of steps completed in the phase |
| *phase*`ElapsedTime` | Total elapsed time in the phase in milliseconds |
| *phase*`Total` | Total number of steps in the phase |
| *phase*`PercentComplete` | Current rate completed in the phase  (The max value is not 100 but 1.0) |

---
# Hadoop Benchmarking

* [NNThroughputBenchmark](#NNThroughputBenchmark)
  * [Overview](#Overview)
  * [Commands](#Commands)
    * [Generic Options](#Generic_Options)
    * [Command Options](#Command_Options)
  * [Reports](#Reports)

This page is to discuss benchmarking Hadoop using tools it provides.

## NNThroughputBenchmark

### Overview

**NNThroughputBenchmark**, as its name indicates, is a name-node throughput benchmark, which runs a series of client threads on a single node against a name-node. If no name-node is configured, it will firstly start a name-node in the same process (*standalone mode*), in which case each client repetitively performs the same operation by directly calling the respective name-node methods. Otherwise, the benchmark will perform the operations against a remote name-node via client protocol RPCs (*remote mode*). Either way, all clients are running locally in a single process rather than remotely across different nodes. The reason is to avoid communication overhead caused by RPC connections and serialization, and thus reveal the upper bound of pure name-node performance.

The benchmark first generates inputs for each thread so that the input generation overhead does not effect the resulting statistics. The number of operations performed by threads is practically the same. Precisely, the difference between the number of operations performed by any two threads does not exceed 1. Then the benchmark executes the specified number of operations using the specified number of threads and outputs the resulting stats by measuring the number of operations performed by the name-node per second.

### Commands

The general command line syntax is:

`hadoop org.apache.hadoop.hdfs.server.namenode.NNThroughputBenchmark [genericOptions] [commandOptions]`

#### Generic Options

This benchmark honors the [Hadoop command-line Generic Options](CommandsManual.html#Generic_Options) to alter its behavior. The benchmark, as other tools, will rely on the `fs.defaultFS` config, which is overridable by `-fs` command option, to run standalone mode or remote mode. If the `fs.defaultFS` scheme is not specified or is `file` (local), the benchmark will run in *standalone mode*. Specially, the *remote* name-node config `dfs.namenode.fs-limits.min-block-size` should be set as 16 while in *standalone mode* the benchmark turns off minimum block size verification for its internal name-node.

#### Command Options

The following are all supported command options:

| COMMAND\_OPTION | Description |
| --- | --- |
| `-op` | Specify the operation. This option must be provided and should be the first option. |
| `-logLevel` | Specify the logging level when the benchmark runs. The default logging level is ERROR. |
| `-UGCacheRefreshCount` | After every specified number of operations, the benchmark purges the name-node’s user group cache. By default the refresh is never called. |
| `-keepResults` | If specified, do not clean up the name-space after execution. By default the name-space will be removed after test. |
| `-nonSuperUser` | If specified, non super user can use the tool and can be helpful for bringing authorization time into benchmarking calculations. |

##### Operations Supported

Following are all the operations supported along with their respective operation-specific parameters (all optional) and default values.

| OPERATION\_OPTION | Operation-specific parameters |
| --- | --- |
| `all` | *options for other operations* |
| `create` | [`-threads 3`] [`-files 10`] [`-filesPerDir 4`] [`-close`] [`-baseDirName /nnThroughputBenchmark`] |
| `mkdirs` | [`-threads 3`] [`-dirs 10`] [`-dirsPerDir 2`] [`-baseDirName /nnThroughputBenchmark`] |
| `open` | [`-threads 3`] [`-files 10`] [`-filesPerDir 4`] [`-useExisting`] [`-baseDirName /nnThroughputBenchmark`] |
| `delete` | [`-threads 3`] [`-files 10`] [`-filesPerDir 4`] [`-useExisting`] [`-baseDirName /nnThroughputBenchmark`] |
| `append` | [`-threads 3`] [`-files 10`] [`-filesPerDir 4`] [`-useExisting`] [`-appendNewBlk`] [`-baseDirName /nnThroughputBenchmark`] |
| `fileStatus` | [`-threads 3`] [`-files 10`] [`-filesPerDir 4`] [`-useExisting`] [`-baseDirName /nnThroughputBenchmark`] |
| `rename` | [`-threads 3`] [`-files 10`] [`-filesPerDir 4`] [`-useExisting`] [`-baseDirName /nnThroughputBenchmark`] |
| `blockReport` | [`-datanodes 10`] [`-reports 30`] [`-blocksPerReport 100`] [`-blocksPerFile 10`] [`-baseDirName /nnThroughputBenchmark`] |
| `replication` | [`-datanodes 10`] [`-nodesToDecommission 1`] [`-nodeReplicationLimit 100`] [`-totalBlocks 100`] [`-replication 3`] [`-baseDirName /nnThroughputBenchmark`] |
| `clean` | N/A |

##### Operation Options

When running benchmarks with the above operation(s), please provide operation-specific parameters illustrated as following.

| OPERATION\_SPECIFIC\_OPTION | Description |
| --- | --- |
| `-threads` | Number of total threads to run the respective operation. |
| `-files` | Number of total files for the respective operation. |
| `-dirs` | Number of total directories for the respective operation. |
| `-filesPerDir` | Number of files per directory. |
| `-close` | Close the files after creation. |
| `-dirsPerDir` | Number of directories per directory. |
| `-useExisting` | If specified, do not recreate the name-space, use existing data. |
| `-datanodes` | Total number of simulated data-nodes. |
| `-reports` | Total number of block reports to send. |
| `-blocksPerReport` | Number of blocks per report. |
| `-blocksPerFile` | Number of blocks per file. |
| `-nodesToDecommission` | Total number of simulated data-nodes to decommission. |
| `-nodeReplicationLimit` | The maximum number of outgoing replication streams for a data-node. |
| `-totalBlocks` | Number of total blocks to operate. |
| `-replication` | Replication factor. Will be adjusted to number of data-nodes if it is larger than that. |
| `-baseDirName` | The base dir name for benchmarks, to support multiple clients submitting benchmark tests at the same time. |
| `-blockSize` | The block size for new files. |

### Reports

The benchmark measures the number of operations performed by the name-node per second. Specifically, for each operation tested, it reports the total running time in seconds (*Elapsed Time*), operation throughput (*Ops per sec*), and average time for the operations (*Average Time*). The higher, the better.

Following is a sample reports by running following commands that opens 100K files with 1K threads against a remote name-node. See [HDFS scalability: the limits to growth](https://www.usenix.org/legacy/publications/login/2010-04/openpdfs/shvachko.pdf) for real-world benchmark stats.

```
$ hadoop org.apache.hadoop.hdfs.server.namenode.NNThroughputBenchmark -fs hdfs://nameservice:9000 -op open -threads 1000 -files 100000

--- open inputs ---
nrFiles = 100000
nrThreads = 1000
nrFilesPerDir = 4
--- open stats  ---
# operations: 100000
Elapsed Time: 9510
 Ops per sec: 10515.247108307045
Average Time: 90
```

---
# Proxy user - Superusers Acting On Behalf Of Other Users

* [Introduction](#Introduction)
* [Use Case](#Use_Case)
* [Code example](#Code_example)
* [Configurations](#Configurations)
* [Caveats](#Caveats)

## Introduction

This document describes how a superuser can submit jobs or access hdfs on behalf of another user.

## Use Case

The code example described in the next section is applicable for the following use case.

A superuser with username ‘super’ wants to submit job and access hdfs on behalf of a user joe. The superuser has kerberos credentials but user joe doesn’t have any. The tasks are required to run as user joe and any file accesses on namenode are required to be done as user joe. It is required that user joe can connect to the namenode or job tracker on a connection authenticated with super’s kerberos credentials. In other words super is impersonating the user joe.

Some products such as Apache Oozie need this.

## Code example

In this example super’s credentials are used for login and a proxy user ugi object is created for joe. The operations are performed within the doAs method of this proxy user ugi object.

```
    ...
    //Create ugi for joe. The login user is 'super'.
    UserGroupInformation ugi =
            UserGroupInformation.createProxyUser("joe", UserGroupInformation.getLoginUser());
    ugi.doAs(new PrivilegedExceptionAction<Void>() {
      public Void run() throws Exception {
        //Submit a job
        JobClient jc = new JobClient(conf);
        jc.submitJob(conf);
        //OR access hdfs
        FileSystem fs = FileSystem.get(conf);
        fs.mkdir(someFilePath);
      }
    }
```

## Configurations

You can configure proxy user using properties `hadoop.proxyuser.$superuser.hosts` along with either or both of `hadoop.proxyuser.$superuser.groups` and `hadoop.proxyuser.$superuser.users`.

By specifying as below in core-site.xml, the superuser named `super` can connect only from `host1` and `host2` to impersonate a user belonging to `group1` and `group2`.

```
   <property>
     <name>hadoop.proxyuser.super.hosts</name>
     <value>host1,host2</value>
   </property>
   <property>
     <name>hadoop.proxyuser.super.groups</name>
     <value>group1,group2</value>
   </property>
```

If these configurations are not present, impersonation will not be allowed and connection will fail.

If more lax security is preferred, the wildcard value \* may be used to allow impersonation from any host or of any user. For example, by specifying as below in core-site.xml, user named `oozie` accessing from any host can impersonate any user belonging to any group.

```
  <property>
    <name>hadoop.proxyuser.oozie.hosts</name>
    <value>*</value>
  </property>
  <property>
    <name>hadoop.proxyuser.oozie.groups</name>
    <value>*</value>
  </property>
```

The `hadoop.proxyuser.$superuser.hosts` accepts list of ip addresses, ip address ranges in CIDR format and/or host names. For example, by specifying as below, user named `super` accessing from hosts in the range `10.222.0.0-10.222.255.255` and `10.113.221.221` can impersonate `user1` and `user2`.

```
   <property>
     <name>hadoop.proxyuser.super.hosts</name>
     <value>10.222.0.0/16,10.113.221.221</value>
   </property>
   <property>
     <name>hadoop.proxyuser.super.users</name>
     <value>user1,user2</value>
   </property>
```

## Caveats

If the cluster is running in [Secure Mode](./SecureMode.html), the superuser must have kerberos credentials to be able to impersonate another user.

It cannot use delegation tokens for this feature. It would be wrong if superuser adds its own delegation token to the proxy user ugi, as it will allow the proxy user to connect to the service with the privileges of the superuser.

However, if the superuser does want to give a delegation token to joe, it must first impersonate joe and get a delegation token for joe, in the same way as the code example above, and add it to the ugi of joe. In this way the delegation token will have the owner as joe.

---
* [appendToFile](#appendToFile)
* [cat](#cat)
* [checksum](#checksum)
* [chgrp](#chgrp)
* [chmod](#chmod)
* [chown](#chown)
* [copyFromLocal](#copyFromLocal)
* [copyToLocal](#copyToLocal)
* [count](#count)
* [cp](#cp)
* [createSnapshot](#createSnapshot)
* [deleteSnapshot](#deleteSnapshot)
* [df](#df)
* [du](#du)
* [dus](#dus)
* [expunge](#expunge)
* [find](#find)
* [get](#get)
* [getfacl](#getfacl)
* [getfattr](#getfattr)
* [getmerge](#getmerge)
* [head](#head)
* [help](#help)
* [ls](#ls)
* [lsr](#lsr)
* [mkdir](#mkdir)
* [moveFromLocal](#moveFromLocal)
* [moveToLocal](#moveToLocal)
* [mv](#mv)
* [put](#put)
* [renameSnapshot](#renameSnapshot)
* [rm](#rm)
* [rmdir](#rmdir)
* [rmr](#rmr)
* [setfacl](#setfacl)
* [setfattr](#setfattr)
* [setrep](#setrep)
* [stat](#stat)
* [tail](#tail)
* [test](#test)
* [text](#text)
* [touch](#touch)
* [touchz](#touchz)
* [truncate](#truncate)
* [concat](#concat)
* [usage](#usage)
* [Deleting objects](#Deleting_objects)
* [Overwriting Objects](#Overwriting_Objects)
* [Timestamps](#Timestamps)
* [Security model and operations](#Security_model_and_operations)
* [Commands of limited value](#Commands_of_limited_value)

# Overview

The File System (FS) shell includes various shell-like commands that directly interact with the Hadoop Distributed File System (HDFS) as well as other file systems that Hadoop supports, such as Local FS, WebHDFS, S3 FS, and others. The FS shell is invoked by:

```
bin/hadoop fs <args>
```

All FS shell commands take path URIs as arguments. The URI format is `scheme://authority/path`. For HDFS the scheme is `hdfs`, and for the Local FS the scheme is `file`. The scheme and authority are optional. If not specified, the default scheme specified in the configuration is used. An HDFS file or directory such as /parent/child can be specified as `hdfs://namenodehost/parent/child` or simply as `/parent/child` (given that your configuration is set to point to `hdfs://namenodehost`).

Most of the commands in FS shell behave like corresponding Unix commands. Differences are described with each of the commands. Error information is sent to stderr and the output is sent to stdout.

If HDFS is being used, `hdfs dfs` is a synonym.

Relative paths can be used. For HDFS, the current working directory is the HDFS home directory `/user/<username>` that often has to be created manually. The HDFS home directory can also be implicitly accessed, e.g., when using the HDFS trash folder, the `.Trash` directory in the home directory.

See the [Commands Manual](./CommandsManual.html) for generic shell options.

## appendToFile

Usage: `hadoop fs -appendToFile [-n] <localsrc> ... <dst>`

Append single src, or multiple srcs from local file system to the destination file system. Also reads input from stdin and appends to destination file system.

Options

* The `-n` option represents that use NEW\_BLOCK create flag to append file.

Example:

* `hadoop fs -appendToFile localfile /user/hadoop/hadoopfile`
* `hadoop fs -appendToFile localfile1 localfile2 /user/hadoop/hadoopfile`
* `hadoop fs -appendToFile localfile hdfs://nn.example.com/hadoop/hadoopfile`
* `hadoop fs -appendToFile - hdfs://nn.example.com/hadoop/hadoopfile` Reads the input from stdin.

Exit Code:

Returns 0 on success and 1 on error.

## cat

Usage: `hadoop fs -cat [-ignoreCrc] URI [URI ...]`

Copies source paths to stdout.

Options

* The `-ignoreCrc` option disables checksum verification.

Example:

* `hadoop fs -cat hdfs://nn1.example.com/file1 hdfs://nn2.example.com/file2`
* `hadoop fs -cat file:///file3 /user/hadoop/file4`

Exit Code:

Returns 0 on success and -1 on error.

## checksum

Usage: `hadoop fs -checksum [-v] URI [URI ...]`

Returns the checksum information of the file(s).

Options

* The `-v` option displays blocks size for the file(s).

Example:

* `hadoop fs -checksum hdfs://nn1.example.com/file1`
* `hadoop fs -checksum file:///etc/hosts`
* `hadoop fs -checksum file:///etc/hosts hdfs://nn1.example.com/file1`

## chgrp

Usage: `hadoop fs -chgrp [-R] GROUP URI [URI ...]`

Change group association of files. The user must be the owner of files, or else a super-user. Additional information is in the [Permissions Guide](../hadoop-hdfs/HdfsPermissionsGuide.html).

Options

* The -R option will make the change recursively through the directory structure.

## chmod

Usage: `hadoop fs -chmod [-R] <MODE[,MODE]... | OCTALMODE> URI [URI ...]`

Change the permissions of files. With -R, make the change recursively through the directory structure. The user must be the owner of the file, or else a super-user. Additional information is in the [Permissions Guide](../hadoop-hdfs/HdfsPermissionsGuide.html).

Options

* The -R option will make the change recursively through the directory structure.

## chown

Usage: `hadoop fs -chown [-R] [OWNER][:[GROUP]] URI [URI ]`

Change the owner of files. The user must be a super-user. Additional information is in the [Permissions Guide](../hadoop-hdfs/HdfsPermissionsGuide.html).

Options

* The -R option will make the change recursively through the directory structure.

## copyFromLocal

Identical to the -put command.

## copyToLocal

Identical to the -get command.

## count

Usage: `hadoop fs -count [-q] [-h] [-v] [-x] [-t [<storage type>]] [-u] [-e] [-s] <paths>`

Count the number of directories, files and bytes under the paths that match the specified file pattern. Get the quota and the usage. The output columns with -count are: DIR\_COUNT, FILE\_COUNT, CONTENT\_SIZE, PATHNAME

The -u and -q options control what columns the output contains. -q means show quotas and usage, -u limits the output to show quotas only.

The output columns with -count -q are: QUOTA, REMAINING\_QUOTA, SPACE\_QUOTA, REMAINING\_SPACE\_QUOTA, DIR\_COUNT, FILE\_COUNT, CONTENT\_SIZE, PATHNAME

The output columns with -count -u are: QUOTA, REMAINING\_QUOTA, SPACE\_QUOTA, REMAINING\_SPACE\_QUOTA, PATHNAME

The -t option shows the quota and usage for each storage type. The -t option is ignored if -u or -q option is not given. The list of possible parameters that can be used in -t option(case insensitive except the parameter): "", “all”, “ram\_disk”, “ssd”, “disk” or “archive”.

The -h option shows sizes in human readable format.

The -v option displays a header line.

The -x option excludes snapshots from the result calculation. Without the -x option (default), the result is always calculated from all INodes, including all snapshots under the given path. The -x option is ignored if -u or -q option is given.

The -e option shows the erasure coding policy for each file.

The output columns with -count -e are: DIR\_COUNT, FILE\_COUNT, CONTENT\_SIZE, ERASURECODING\_POLICY, PATHNAME

The ERASURECODING\_POLICY is name of the policy for the file. If an erasure coding policy is set on that file, it will return the name of the policy. Otherwise, it will return "Replicated" which means it uses the replication storage strategy.

The -s option shows the snapshot counts for each directory.

Example:

* `hadoop fs -count hdfs://nn1.example.com/file1 hdfs://nn2.example.com/file2`
* `hadoop fs -count -q hdfs://nn1.example.com/file1`
* `hadoop fs -count -q -h hdfs://nn1.example.com/file1`
* `hadoop fs -count -q -h -v hdfs://nn1.example.com/file1`
* `hadoop fs -count -u hdfs://nn1.example.com/file1`
* `hadoop fs -count -u -h hdfs://nn1.example.com/file1`
* `hadoop fs -count -u -h -v hdfs://nn1.example.com/file1`
* `hadoop fs -count -e hdfs://nn1.example.com/file1`
* `hadoop fs -count -s hdfs://nn1.example.com/file1`

Exit Code:

Returns 0 on success and -1 on error.

## cp

Usage: `hadoop fs -cp [-f] [-p | -p[topax]] [-d] [-t <thread count>] [-q <thread pool queue size>] URI [URI ...] <dest>`

Copy files from source to destination. This command allows multiple sources as well in which case the destination must be a directory.

‘raw.\*’ namespace extended attributes are preserved if (1) the source and destination filesystems support them (HDFS only), and (2) all source and destination pathnames are in the /.reserved/raw hierarchy. Determination of whether raw.\* namespace xattrs are preserved is independent of the -p (preserve) flag.

Options:

* `-f` : Overwrite the destination if it already exists.
* `-d` : Skip creation of temporary file with the suffix `._COPYING_`.
* `-p` : Preserve file attributes [topax](timestamps, ownership, permission, ACL, XAttr). If -p is specified with no *arg*, then preserves timestamps, ownership, permission. If -pa is specified, then preserves permission also because ACL is a super-set of permission. Determination of whether raw namespace extended attributes are preserved is independent of the -p flag.
* `-t <thread count>` : Number of threads to be used, default is 1. Useful when copying directories containing more than 1 file.
* `-q <thread pool queue size>` : Thread pool queue size to be used, default is 1024. It takes effect only when thread count greater than 1.

Example:

* `hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2`
* `hadoop fs -cp -f -d /user/hadoop/file1 /user/hadoop/file2`
* `hadoop fs -cp /user/hadoop/file1 /user/hadoop/file2 /user/hadoop/dir`
* `hadoop fs -cp -t 5 /user/hadoop/file1 /user/hadoop/file2 /user/hadoop/dir`
* `hadoop fs -cp -t 10 -q 2048 /user/hadoop/file1 /user/hadoop/file2 /user/hadoop/dir`

Exit Code:

Returns 0 on success and -1 on error.

## createSnapshot

See [HDFS Snapshots Guide](../hadoop-hdfs/HdfsSnapshots.html).

## deleteSnapshot

See [HDFS Snapshots Guide](../hadoop-hdfs/HdfsSnapshots.html).

## df

Usage: `hadoop fs -df [-h] URI [URI ...]`

Displays free space.

Options:

* The -h option will format file sizes in a “human-readable” fashion (e.g 64.0m instead of 67108864)

Example:

* `hadoop dfs -df /user/hadoop/dir1`

## du

Usage: `hadoop fs -du [-s] [-h] [-v] [-x] URI [URI ...]`

Displays sizes of files and directories contained in the given directory or the length of a file in case its just a file.

Options:

* The -s option will result in an aggregate summary of file lengths being displayed, rather than the individual files. Without the -s option, calculation is done by going 1-level deep from the given path.
* The -h option will format file sizes in a “human-readable” fashion (e.g 64.0m instead of 67108864)
* The -v option will display the names of columns as a header line.
* The -x option will exclude snapshots from the result calculation. Without the -x option (default), the result is always calculated from all INodes, including all snapshots under the given path.

The du returns three columns with the following format:

```
size disk_space_consumed_with_all_replicas full_path_name
```

Example:

* `hadoop fs -du /user/hadoop/dir1 /user/hadoop/file1 hdfs://nn.example.com/user/hadoop/dir1`

Exit Code: Returns 0 on success and -1 on error.

## dus

Usage: `hadoop fs -dus <args>`

Displays a summary of file lengths.

**Note:** This command is deprecated. Instead use `hadoop fs -du -s`.

## expunge

Usage: `hadoop fs -expunge [-immediate] [-fs <path>]`

Permanently delete files in checkpoints older than the retention threshold from trash directory, and create new checkpoint.

When checkpoint is created, recently deleted files in trash are moved under the checkpoint. Files in checkpoints older than `fs.trash.interval` will be permanently deleted on the next invocation of `-expunge` command.

If the file system supports the feature, users can configure to create and delete checkpoints periodically by the parameter stored as `fs.trash.checkpoint.interval` (in core-site.xml). This value should be smaller or equal to `fs.trash.interval`.

If the `-immediate` option is passed, all files in the trash for the current user are immediately deleted, ignoring the `fs.trash.interval` setting.

If the `-fs` option is passed, the supplied filesystem will be expunged, rather than the default filesystem and checkpoint is created.

For example

```
hadoop fs -expunge -immediate -fs s3a://landsat-pds/
```

Refer to the [HDFS Architecture guide](../hadoop-hdfs/HdfsDesign.html#File_Deletes_and_Undeletes) for more information about trash feature of HDFS.

## find

Usage: `hadoop fs -find <path> ... <expression> ...`

Finds all files that match the specified expression and applies selected actions to them. If no *path* is specified then defaults to the current working directory. If no expression is specified then defaults to -print.

The following primary expressions are recognised:

* -name pattern  
  -iname pattern

  Evaluates as true if the basename of the file matches the pattern using standard file system globbing. If -iname is used then the match is case insensitive.
* -print  
  -print0

  Always evaluates to true. Causes the current pathname to be written to standard output. If the -print0 expression is used then an ASCII NULL character is appended.

The following operators are recognised:

* expression -a expression  
  expression -and expression  
  expression expression

  Logical AND operator for joining two expressions. Returns true if both child expressions return true. Implied by the juxtaposition of two expressions and so does not need to be explicitly specified. The second expression will not be applied if the first fails.

Example:

`hadoop fs -find / -name test -print`

Exit Code:

Returns 0 on success and -1 on error.

## get

Usage: `hadoop fs -get [-ignoreCrc] [-crc] [-p] [-f] [-t <thread count>] [-q <thread pool queue size>] <src> ... <localdst>`

Copy files to the local file system. Files that fail the CRC check may be copied with the -ignoreCrc option. Files and CRCs may be copied using the -crc option.

Options:

* `-p` : Preserves access and modification times, ownership and the permissions. (assuming the permissions can be propagated across filesystems)
* `-f` : Overwrites the destination if it already exists.
* `-ignoreCrc` : Skip CRC checks on the file(s) downloaded.
* `-crc`: write CRC checksums for the files downloaded.
* `-t <thread count>` : Number of threads to be used, default is 1. Useful when downloading directories containing more than 1 file.
* `-q <thread pool queue size>` : Thread pool queue size to be used, default is 1024. It takes effect only when thread count greater than 1.

Example:

* `hadoop fs -get /user/hadoop/file localfile`
* `hadoop fs -get hdfs://nn.example.com/user/hadoop/file localfile`
* `hadoop fs -get -t 10 hdfs://nn.example.com/user/hadoop/dir1 localdir`
* `hadoop fs -get -t 10 -q 2048 hdfs://nn.example.com/user/hadoop/dir* localdir`

Exit Code:

Returns 0 on success and -1 on error.

## getfacl

Usage: `hadoop fs -getfacl [-R] <path>`

Displays the Access Control Lists (ACLs) of files and directories. If a directory has a default ACL, then getfacl also displays the default ACL.

Options:

* -R: List the ACLs of all files and directories recursively.
* *path*: File or directory to list.

Examples:

* `hadoop fs -getfacl /file`
* `hadoop fs -getfacl -R /dir`

Exit Code:

Returns 0 on success and non-zero on error.

## getfattr

Usage: `hadoop fs -getfattr [-R] -n name | -d [-e en] <path>`

Displays the extended attribute names and values (if any) for a file or directory.

Options:

* -R: Recursively list the attributes for all files and directories.
* -n name: Dump the named extended attribute value.
* -d: Dump all extended attribute values associated with pathname.
* -e *encoding*: Encode values after retrieving them. Valid encodings are “text”, “hex”, and “base64”. Values encoded as text strings are enclosed in double quotes ("), and values encoded as hexadecimal and base64 are prefixed with 0x and 0s, respectively.
* *path*: The file or directory.

Examples:

* `hadoop fs -getfattr -d /file`
* `hadoop fs -getfattr -R -n user.myAttr /dir`

Exit Code:

Returns 0 on success and non-zero on error.

## getmerge

Usage: `hadoop fs -getmerge [-nl] [-skip-empty-file] <src> <localdst>`

Takes a source directory and a destination file as input and concatenates files in src into the destination local file. Optionally -nl can be set to enable adding a newline character (LF) at the end of each file. -skip-empty-file can be used to avoid unwanted newline characters in case of empty files.

Examples:

* `hadoop fs -getmerge -nl /src /opt/output.txt`
* `hadoop fs -getmerge -nl /src/file1.txt /src/file2.txt /output.txt`
* `hadoop fs -getmerge -nl -skip-empty-file /src/file1.txt /src/file2.txt /output.txt`

Exit Code:

Returns 0 on success and non-zero on error.

## head

Usage: `hadoop fs -head URI`

Displays first kilobyte of the file to stdout.

Example:

* `hadoop fs -head pathname`

Exit Code: Returns 0 on success and -1 on error.

## help

Usage: `hadoop fs -help`

Return usage output.

## ls

Usage: `hadoop fs -ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [-e] <args>`

Options:

* -C: Display the paths of files and directories only.
* -d: Directories are listed as plain files.
* -h: Format file sizes in a human-readable fashion (eg 64.0m instead of 67108864).
* -q: Print ? instead of non-printable characters.
* -R: Recursively list subdirectories encountered.
* -t: Sort output by modification time (most recent first).
* -S: Sort output by file size.
* -r: Reverse the sort order.
* -u: Use access time rather than modification time for display and sorting.
* -e: Display the erasure coding policy of files and directories only.

For a file ls returns stat on the file with the following format:

```
permissions number_of_replicas userid groupid filesize modification_date modification_time filename
```

For a directory it returns list of its direct children as in Unix. A directory is listed as:

```
permissions userid groupid modification_date modification_time dirname
```

Files within a directory are order by filename by default.

Example:

* `hadoop fs -ls /user/hadoop/file1`
* `hadoop fs -ls -e /ecdir`

Exit Code:

Returns 0 on success and -1 on error.

## lsr

Usage: `hadoop fs -lsr <args>`

Recursive version of ls.

**Note:** This command is deprecated. Instead use `hadoop fs -ls -R`

## mkdir

Usage: `hadoop fs -mkdir [-p] <paths>`

Takes path uri’s as argument and creates directories.

Options:

* The -p option behavior is much like Unix mkdir -p, creating parent directories along the path.

Example:

* `hadoop fs -mkdir /user/hadoop/dir1 /user/hadoop/dir2`
* `hadoop fs -mkdir hdfs://nn1.example.com/user/hadoop/dir hdfs://nn2.example.com/user/hadoop/dir`

Exit Code:

Returns 0 on success and -1 on error.

## moveFromLocal

Usage: `hadoop fs -moveFromLocal <localsrc> <dst>`

Similar to put command, except that the source localsrc is deleted after it’s copied.

## moveToLocal

Usage: `hadoop fs -moveToLocal [-crc] <src> <dst>`

Displays a “Not implemented yet” message.

## mv

Usage: `hadoop fs -mv URI [URI ...] <dest>`

Moves files from source to destination. This command allows multiple sources as well in which case the destination needs to be a directory. Moving files across file systems is not permitted.

Example:

* `hadoop fs -mv /user/hadoop/file1 /user/hadoop/file2`
* `hadoop fs -mv hdfs://nn.example.com/file1 hdfs://nn.example.com/file2 hdfs://nn.example.com/file3 hdfs://nn.example.com/dir1`

Exit Code:

Returns 0 on success and -1 on error.

## put

Usage: `hadoop fs -put [-f] [-p] [-l] [-d] [-t <thread count>] [-q <thread pool queue size>] [ - | <localsrc> ...] <dst>`

Copy single src, or multiple srcs from local file system to the destination file system. Also reads input from stdin and writes to destination file system if the source is set to “-”

Copying fails if the file already exists, unless the -f flag is given.

Options:

* `-p` : Preserves access and modification times, ownership and the permissions. (assuming the permissions can be propagated across filesystems)
* `-f` : Overwrites the destination if it already exists.
* `-l` : Allow DataNode to lazily persist the file to disk, Forces a replication factor of 1. This flag will result in reduced durability. Use with care.
* `-d` : Skip creation of temporary file with the suffix `._COPYING_`.
* `-t <thread count>` : Number of threads to be used, default is 1. Useful when uploading directories containing more than 1 file.
* `-q <thread pool queue size>` : Thread pool queue size to be used, default is 1024. It takes effect only when thread count greater than 1.

Examples:

* `hadoop fs -put localfile /user/hadoop/hadoopfile`
* `hadoop fs -put -f localfile1 localfile2 /user/hadoop/hadoopdir`
* `hadoop fs -put -d localfile hdfs://nn.example.com/hadoop/hadoopfile`
* `hadoop fs -put - hdfs://nn.example.com/hadoop/hadoopfile` Reads the input from stdin.
* `hadoop fs -put -t 5 localdir hdfs://nn.example.com/hadoop/hadoopdir`
* `hadoop fs -put -t 10 -q 2048 localdir1 localdir2 hdfs://nn.example.com/hadoop/hadoopdir`

Exit Code:

Returns 0 on success and -1 on error.

## renameSnapshot

See [HDFS Snapshots Guide](../hadoop-hdfs/HdfsSnapshots.html).

## rm

Usage: `hadoop fs -rm [-f] [-r |-R] [-skipTrash] [-safely] URI [URI ...]`

Delete files specified as args.

If trash is enabled, file system instead moves the deleted file to a trash directory (given by [FileSystem#getTrashRoot](../../api/org/apache/hadoop/fs/FileSystem.html)).

Currently, the trash feature is disabled by default. User can enable trash by setting a value greater than zero for parameter `fs.trash.interval` (in core-site.xml).

See [expunge](#expunge) about deletion of files in trash.

Options:

* The -f option will not display a diagnostic message or modify the exit status to reflect an error if the file does not exist.
* The -R option deletes the directory and any content under it recursively.
* The -r option is equivalent to -R.
* The -skipTrash option will bypass trash, if enabled, and delete the specified file(s) immediately. This can be useful when it is necessary to delete files from an over-quota directory.
* The -safely option will require safety confirmation before deleting directory with total number of files greater than `hadoop.shell.delete.limit.num.files` (in core-site.xml, default: 100). It can be used with -skipTrash to prevent accidental deletion of large directories. Delay is expected when walking over large directory recursively to count the number of files to be deleted before the confirmation.

Example:

* `hadoop fs -rm hdfs://nn.example.com/file /user/hadoop/emptydir`

Exit Code:

Returns 0 on success and -1 on error.

## rmdir

Usage: `hadoop fs -rmdir [--ignore-fail-on-non-empty] URI [URI ...]`

Delete a directory.

Options:

* `--ignore-fail-on-non-empty`: When using wildcards, do not fail if a directory still contains files.

Example:

* `hadoop fs -rmdir /user/hadoop/emptydir`

## rmr

Usage: `hadoop fs -rmr [-skipTrash] URI [URI ...]`

Recursive version of delete.

**Note:** This command is deprecated. Instead use `hadoop fs -rm -r`

## setfacl

Usage: `hadoop fs -setfacl [-R] [-b |-k -m |-x <acl_spec> <path>] |[--set <acl_spec> <path>]`

Sets Access Control Lists (ACLs) of files and directories.

Options:

* -b: Remove all but the base ACL entries. The entries for user, group and others are retained for compatibility with permission bits.
* -k: Remove the default ACL.
* -R: Apply operations to all files and directories recursively.
* -m: Modify ACL. New entries are added to the ACL, and existing entries are retained.
* -x: Remove specified ACL entries. Other ACL entries are retained.
* `--set`: Fully replace the ACL, discarding all existing entries. The *acl\_spec* must include entries for user, group, and others for compatibility with permission bits. If the ACL spec contains only access entries, then the existing default entries are retained. If the ACL spec contains only default entries, then the existing access entries are retained. If the ACL spec contains both access and default entries, then both are replaced.
* *acl\_spec*: Comma separated list of ACL entries.
* *path*: File or directory to modify.

Examples:

* `hadoop fs -setfacl -m user:hadoop:rw- /file`
* `hadoop fs -setfacl -x user:hadoop /file`
* `hadoop fs -setfacl -b /file`
* `hadoop fs -setfacl -k /dir`
* `hadoop fs -setfacl --set user::rw-,user:hadoop:rw-,group::r--,other::r-- /file`
* `hadoop fs -setfacl -R -m user:hadoop:r-x /dir`
* `hadoop fs -setfacl -m default:user:hadoop:r-x /dir`

Exit Code:

Returns 0 on success and non-zero on error.

## setfattr

Usage: `hadoop fs -setfattr -n name [-v value] | -x name <path>`

Sets an extended attribute name and value for a file or directory.

Options:

* -n name: The extended attribute name.
* -v value: The extended attribute value. There are three different encoding methods for the value. If the argument is enclosed in double quotes, then the value is the string inside the quotes. If the argument is prefixed with 0x or 0X, then it is taken as a hexadecimal number. If the argument begins with 0s or 0S, then it is taken as a base64 encoding.
* -x name: Remove the extended attribute.
* *path*: The file or directory.

Examples:

* `hadoop fs -setfattr -n user.myAttr -v myValue /file`
* `hadoop fs -setfattr -n user.noValue /file`
* `hadoop fs -setfattr -x user.myAttr /file`

Exit Code:

Returns 0 on success and non-zero on error.

## setrep

Usage: `hadoop fs -setrep [-R] [-w] <numReplicas> <path>`

Changes the replication factor of a file. If *path* is a directory then the command recursively changes the replication factor of all files under the directory tree rooted at *path*. The EC files will be ignored when executing this command.

Options:

* The -w flag requests that the command wait for the replication to complete. This can potentially take a very long time.
* The -R flag is accepted for backwards compatibility. It has no effect.

Example:

* `hadoop fs -setrep -w 3 /user/hadoop/dir1`

Exit Code:

Returns 0 on success and -1 on error.

## stat

Usage: `hadoop fs -stat [format] <path> ...`

Print statistics about the file/directory at <path> in the specified format. Format accepts permissions in octal (%a) and symbolic (%A), filesize in bytes (%b), type (%F), group name of owner (%g), name (%n), block size (%o), replication (%r), user name of owner(%u), access date(%x, %X), and modification date (%y, %Y). %x and %y show UTC date as “yyyy-MM-dd HH:mm:ss”, and %X and %Y show milliseconds since January 1, 1970 UTC. If the format is not specified, %y is used by default.

Example:

* `hadoop fs -stat "type:%F perm:%a %u:%g size:%b mtime:%y atime:%x name:%n" /file`

Exit Code: Returns 0 on success and -1 on error.

## tail

Usage: `hadoop fs -tail [-f] URI`

Displays last kilobyte of the file to stdout.

Options:

* The -f option will output appended data as the file grows, as in Unix.

Example:

* `hadoop fs -tail pathname`

Exit Code: Returns 0 on success and -1 on error.

## test

Usage: `hadoop fs -test -[defswrz] URI`

Options:

* -d: if the path is a directory, return 0.
* -e: if the path exists, return 0.
* -f: if the path is a file, return 0.
* -s: if the path is not empty, return 0.
* -w: if the path exists and write permission is granted, return 0.
* -r: if the path exists and read permission is granted, return 0.
* -z: if the file is zero length, return 0.

Example:

* `hadoop fs -test -e filename`

## text

Usage: `hadoop fs -text <src>`

Takes a source file and outputs the file in text format. The allowed formats are zip and TextRecordInputStream.

## touch

Usage: `hadoop fs -touch [-a] [-m] [-t TIMESTAMP] [-c] URI [URI ...]`

Updates the access and modification times of the file specified by the URI to the current time. If the file does not exist, then a zero length file is created at URI with current time as the timestamp of that URI.

* Use -a option to change only the access time
* Use -m option to change only the modification time
* Use -t option to specify timestamp (in format yyyyMMdd:HHmmss) instead of current time
* Use -c option to not create file if it does not exist

The timestamp format is as follows \* yyyy Four digit year (e.g. 2018) \* MM Two digit month of the year (e.g. 08 for month of August) \* dd Two digit day of the month (e.g. 01 for first day of the month) \* HH Two digit hour of the day using 24 hour notation (e.g. 23 stands for 11 pm, 11 stands for 11 am) \* mm Two digit minutes of the hour \* ss Two digit seconds of the minute e.g. 20180809:230000 represents August 9th 2018, 11pm

Example:

* `hadoop fs -touch pathname`
* `hadoop fs -touch -m -t 20180809:230000 pathname`
* `hadoop fs -touch -t 20180809:230000 pathname`
* `hadoop fs -touch -a pathname`

Exit Code: Returns 0 on success and -1 on error.

## touchz

Usage: `hadoop fs -touchz URI [URI ...]`

Create a file of zero length. An error is returned if the file exists with non-zero length.

Example:

* `hadoop fs -touchz pathname`

Exit Code: Returns 0 on success and -1 on error.

## truncate

Usage: `hadoop fs -truncate [-w] <length> <paths>`

Truncate all files that match the specified file pattern to the specified length.

Options:

* The -w flag requests that the command waits for block recovery to complete, if necessary.  
  Without -w flag the file may remain unclosed for some time while the recovery is in progress.  
  During this time file cannot be reopened for append.

Example:

* `hadoop fs -truncate 55 /user/hadoop/file1 /user/hadoop/file2`
* `hadoop fs -truncate -w 127 hdfs://nn1.example.com/user/hadoop/file1`

## concat

Usage: `hadoop fs -concat <target file> <source files>`

Concatenate existing source files into the target file. Target file and source files should be in the same directory.

Example:

* `hadoop fs -concat hdfs://cluster/user/hadoop/target-file hdfs://cluster/user/hadoop/file-0 hdfs://cluster/user/hadoop/file-1`

## usage

Usage: `hadoop fs -usage command`

Return the help for an individual command.

# Working with Object Storage

The Hadoop FileSystem shell works with Object Stores such as Amazon S3, Azure ABFS and Google GCS.

```
# Create a directory
hadoop fs -mkdir s3a://bucket/datasets/

# Upload a file from the cluster filesystem
hadoop fs -put /datasets/example.orc s3a://bucket/datasets/

# touch a file
hadoop fs -touchz wasb://yourcontainer@youraccount.blob.core.windows.net/touched
```

Unlike a normal filesystem, renaming files and directories in an object store usually takes time proportional to the size of the objects being manipulated. As many of the filesystem shell operations use renaming as the final stage in operations, skipping that stage can avoid long delays.

In particular, the `put` and `copyFromLocal` commands should both have the `-d` options set for a direct upload.

```
# Upload a file from the cluster filesystem
hadoop fs -put -d /datasets/example.orc s3a://bucket/datasets/

# Upload a file from under the user's home directory in the local filesystem.
# Note it is the shell expanding the "~", not the hadoop fs command
hadoop fs -copyFromLocal -d -f ~/datasets/devices.orc s3a://bucket/datasets/

# create a file from stdin
# the special "-" source means "use stdin"
echo "hello" | hadoop fs -put -d -f - wasb://yourcontainer@youraccount.blob.core.windows.net/hello.txt
```

Objects can be downloaded and viewed:

```
# copy a directory to the local filesystem
hadoop fs -copyToLocal s3a://bucket/datasets/

# copy a file from the object store to the cluster filesystem.
hadoop fs -get wasb://yourcontainer@youraccount.blob.core.windows.net/hello.txt /examples

# print the object
hadoop fs -cat wasb://yourcontainer@youraccount.blob.core.windows.net/hello.txt

# print the object, unzipping it if necessary
hadoop fs -text wasb://yourcontainer@youraccount.blob.core.windows.net/hello.txt

## download log files into a local file
hadoop fs -getmerge wasb://yourcontainer@youraccount.blob.core.windows.net/logs\* log.txt
```

Commands which list many files tend to be significantly slower than when working with HDFS or other filesystems

```
hadoop fs -count s3a://bucket/
hadoop fs -du s3a://bucket/
```

Other slow commands include `find`, `mv`, `cp` and `rm`.

**Find**

This can be very slow on a large store with many directories under the path supplied.

```
# enumerate all files in the object store's container.
hadoop fs -find s3a://bucket/ -print

# remember to escape the wildcards to stop the shell trying to expand them first
hadoop fs -find s3a://bucket/datasets/ -name \*.txt -print
```

**Rename**

The time to rename a file depends on its size.

The time to rename a directory depends on the number and size of all files beneath that directory.

```
hadoop fs -mv s3a://bucket/datasets s3a://bucket/historical
```

If the operation is interrupted, the object store will be in an undefined state.

**Copy**

```
hadoop fs -cp s3a://bucket/datasets s3a://bucket/historical
```

The copy operation reads each file and then writes it back to the object store; the time to complete depends on the amount of data to copy, and the bandwidth in both directions between the local computer and the object store.

**The further the computer is from the object store, the longer the copy takes**

## Deleting objects

The `rm` command will delete objects and directories full of objects. If the object store is *eventually consistent*, `fs ls` commands and other accessors may briefly return the details of the now-deleted objects; this is an artifact of object stores which cannot be avoided.

If the filesystem client is configured to copy files to a trash directory, this will be in the bucket; the `rm` operation will then take time proportional to the size of the data. Furthermore, the deleted files will continue to incur storage costs.

To avoid this, use the `-skipTrash` option.

```
hadoop fs -rm -skipTrash s3a://bucket/dataset
```

Data moved to the `.Trash` directory can be purged using the `expunge` command. As this command only works with the default filesystem, it must be configured to make the default filesystem the target object store.

```
hadoop fs -expunge -D fs.defaultFS=s3a://bucket/
```

## Overwriting Objects

If an object store is *eventually consistent*, then any operation which overwrites existing objects may not be immediately visible to all clients/queries. That is: later operations which query the same object’s status or contents may get the previous object. This can sometimes surface within the same client, while reading a single object.

Avoid having a sequence of commands which overwrite objects and then immediately work on the updated data; there is a risk that the previous data will be used instead.

## Timestamps

Timestamps of objects and directories in Object Stores may not follow the behavior of files and directories in HDFS.

1. The creation and initial modification times of an object will be the time it was created on the object store; this will be at the end of the write process, not the beginning.
2. The timestamp will be taken from the object store infrastructure’s clock, not that of the client.
3. If an object is overwritten, the modification time will be updated.
4. Directories may or may not have valid timestamps. They are unlikely to have their modification times updated when an object underneath is updated.
5. The `atime` access time feature is not supported by any of the object stores found in the Apache Hadoop codebase.

Consult the `DistCp` documentation for details on how this may affect the `distcp -update` operation.

## Security model and operations

The security and permissions models of object stores are usually very different from those of a Unix-style filesystem; operations which query or manipulate permissions are generally unsupported.

Operations to which this applies include: `chgrp`, `chmod`, `chown`, `getfacl`, and `setfacl`. The related attribute commands `getfattr` and`setfattr` are also usually unavailable.

* Filesystem commands which list permission and user/group details, usually simulate these details.
* Operations which try to preserve permissions (example `fs -put -p`) do not preserve permissions for this reason. (Special case: `wasb://`, which preserves permissions but does not enforce them).

When interacting with read-only object stores, the permissions found in “list” and “stat” commands may indicate that the user has write access, when in fact they do not.

Object stores usually have permissions models of their own, models can be manipulated through store-specific tooling. Be aware that some of the permissions which an object store may provide (such as write-only paths, or different permissions on the root path) may be incompatible with the Hadoop filesystem clients. These tend to require full read and write access to the entire object store bucket/container into which they write data.

As an example of how permissions are mocked, here is a listing of Amazon’s public, read-only bucket of Landsat images:

```
$ hadoop fs -ls s3a://landsat-pds/
Found 10 items
drwxrwxrwx   - mapred          0 2016-09-26 12:16 s3a://landsat-pds/L8
-rw-rw-rw-   1 mapred      23764 2015-01-28 18:13 s3a://landsat-pds/index.html
drwxrwxrwx   - mapred          0 2016-09-26 12:16 s3a://landsat-pds/landsat-pds_stats
-rw-rw-rw-   1 mapred        105 2016-08-19 18:12 s3a://landsat-pds/robots.txt
-rw-rw-rw-   1 mapred         38 2016-09-26 12:16 s3a://landsat-pds/run_info.json
drwxrwxrwx   - mapred          0 2016-09-26 12:16 s3a://landsat-pds/runs
-rw-rw-rw-   1 mapred   27458808 2016-09-26 12:16 s3a://landsat-pds/scene_list.gz
drwxrwxrwx   - mapred          0 2016-09-26 12:16 s3a://landsat-pds/tarq
drwxrwxrwx   - mapred          0 2016-09-26 12:16 s3a://landsat-pds/tarq_corrupt
drwxrwxrwx   - mapred          0 2016-09-26 12:16 s3a://landsat-pds/test
```

1. All files are listed as having full read/write permissions.
2. All directories appear to have full `rwx` permissions.
3. The replication count of all files is “1”.
4. The owner of all files and directories is declared to be the current user (`mapred`).
5. The timestamp of all directories is actually that of the time the `-ls` operation was executed. This is because these directories are not actual objects in the store; they are simulated directories based on the existence of objects under their paths.

When an attempt is made to delete one of the files, the operation fails —despite the permissions shown by the `ls` command:

```
$ hadoop fs -rm s3a://landsat-pds/scene_list.gz
rm: s3a://landsat-pds/scene_list.gz: delete on s3a://landsat-pds/scene_list.gz:
  com.amazonaws.services.s3.model.AmazonS3Exception: Access Denied (Service: Amazon S3;
  Status Code: 403; Error Code: AccessDenied; Request ID: 1EF98D5957BCAB3D),
  S3 Extended Request ID: wi3veOXFuFqWBUCJgV3Z+NQVj9gWgZVdXlPU4KBbYMsw/gA+hyhRXcaQ+PogOsDgHh31HlTCebQ=
```

This demonstrates that the listed permissions cannot be taken as evidence of write access; only object manipulation can determine this.

Note that the Microsoft Azure WASB filesystem does allow permissions to be set and checked, however the permissions are not actually enforced. This feature offers the ability for a HDFS directory tree to be backed up with DistCp, with its permissions preserved, permissions which may be restored when copying the directory back into HDFS. For securing access to the data in the object store, however, Azure’s [own model and tools must be used](https://azure.microsoft.com/en-us/documentation/articles/storage-security-guide/).

## Commands of limited value

Here is the list of shell commands which generally have no effect —and may actually fail.

| command | limitations |
| --- | --- |
| `appendToFile` | generally unsupported |
| `checksum` | the usual checksum is “NONE” |
| `chgrp` | generally unsupported permissions model; no-op |
| `chmod` | generally unsupported permissions model; no-op |
| `chown` | generally unsupported permissions model; no-op |
| `createSnapshot` | generally unsupported |
| `deleteSnapshot` | generally unsupported |
| `df` | default values are normally displayed |
| `getfacl` | may or may not be supported |
| `getfattr` | generally supported |
| `renameSnapshot` | generally unsupported |
| `setfacl` | generally unsupported permissions model |
| `setfattr` | generally unsupported permissions model |
| `setrep` | has no effect |
| `truncate` | generally unsupported |
| `concat` | generally unsupported |

Different object store clients *may* support these commands: do consult the documentation and test against the target store.

---
## The YARN Service Registry

# Introduction and concepts

This document describes a Hadoop service registry built to address two problems:

1. How can clients talk to YARN-deployed services and the components which form such services?
2. Allow Hadoop core services to be registered and discovered thereby reducing configuration parameters and to allow core services to be more easily moved.

Service registration and discovery is a long-standing problem in distributed computing, dating back to Xerox’s Grapevine Service. This proposal is for a registry for locating distributed applications deployed by YARN, and determining the binding information needed to communicate with these applications.

### Definitions

**Service**: a potentially-distributed application deployed in —or reachable from— a Hadoop YARN cluster. Examples: Apache HBase, Apache hcatalog, Apache Storm. Services may be short-lived or long-lived.

**Service Class:** the name of a type of service, used as a path in a registry and matching the DNS-compatible path naming scheme. Examples: `org-apache-hbase`, `org-apache-hcatalog`

**Component**: a distributed element of a service. Examples: HBase master nodes, HBase region servers and HBase REST servers.

**Service Instance:** A single instance of an application. Example, an HBase cluster `demo1`. A service instance is running if the instances the components which for the service are running. This does not imply “live” in the distributed computing sense, merely that the process are running.

**Component Instance**: a single instance of a component within a service instance. Examples: an HBase master node on host `rack1server6` or a region server on host `rack3server40`.

**Endpoint**: one means of binding with a service instance or a component instance. Examples: HBase’s Apache Zookeeper binding, a Java JMX port on a region server, a Web UI on an HBase Master, and the REST API of an HBase REST component instance. Endpoints may be *internal* —for use within the service instance, or *external*: for use by clients of a service instance.

**Service Record**: a record in the registry describing a service instance or a component instance, including listing its endpoints.

**YARN Resource Manager, “RM”:** the YARN component which allows client applications to submit work (including requests to deploy service instances) to a YARN cluster. The RM retains state on all running applications.

**YARN Application**: An application deployed via YARN. Every application instance has a unique application ID.

**YARN Application Master, “AM”:** the application-specific component which is scheduled and deployed by the RM. It has the duty of maintaining the internal state of the application, including requesting and managing all other component instances of this application instance. The YARN RM will detect the failure of the AM, and respond by rescheduling it.

**YARN Container:** An allocation of resources, including CPU and RAM, for a component instance. The AM has the responsibility of requesting the containers its components need, and building the commands to instantiate its component instances onto allocated containers. Every allocated container has a unique container ID.

## The binding problem

Hadoop YARN allows applications to run on the Hadoop cluster. Some of these are batch jobs or queries that can managed via YARN’s existing API using its application ID. In addition YARN can deploy long-lived services instances such a pool of Apache Tomcat web servers or an Apache HBase cluster. YARN will deploy them across the cluster depending on the individual each component requirements and server availability. These service instances need to be discovered by clients; traditionally their IP added is registered in DNS or in some configuration file —but that is not feasible in YARN-deployed applications when neither the hostname nor network ports can be known in advance.

As a result there is no easy way for clients to interact with dynamically deployed applications.

YARN supports a rudimentary registry which allows YARN Application Masters to register a web URL and an IPC address. but is not sufficient for our purposes since it It does not allow any other *endpoints* to be registered —such as REST URLs, or zookeeper path or the endpoints of the tasks that the Application Master executes. Further, information that can be registered is mapped to the YARN application instance —a unique instance ID that changes whenever a YARN application is started. This makes it impossible to resolve binding information via a static reference to a named service, or to even probe for the existence of a service instance which is not currently live.

# Use Cases

## Service Name Examples

Core Hadoop services.

These may be deployed statically, dynamically via an account with the permissions to write to the `/services` path, or even registrations of remote services accessible from within the Hadoop cluster

```
    /services/hdfs
    /services/yarn
    /services/oozie
```

YARN-deployed services belonging to individual users.

```
    /users/joe/org-apache-hbase/demo1
    /users/joe/org-apache-hbase/demo1/components/regionserver1
```

## Registration Use Cases

1. A Hadoop core service that is not running under YARN example: HDFS) can be registered in for discovery. This could be done by the service or by management tools..
2. A long-lived application deployed by YARN registers itself for discovery by clients. The registration data is intended to outlive the application master, and perhaps the lifespan of a single deployment of the service instance.
3. Component instances of a service register themselves, publishing internal binding information, such as JMX ports.
4. A YARN-deployed application can bind to dependent service instances both static and dynamic. Example: a Tomcat web pool binding to the dynamic HBase service instance “/users/joe/services/hbase/demo1”.
5. Component Instances use the registry to bind to an internal endpoint of their application master, to which they heartbeat regularly.

## Unsupported Registration use cases:

1. A short-lived YARN application is registered automatically in the registry, including all its containers. and unregistered when the job terminates. Short-lived applications with many containers will place excessive load on a registry. All YARN applications will be given the option of registering, but it will not be automatic —and application authors must be advised against registering short-lived containers.

## Lookup Use Cases

1. A client application looks up a dynamically deployed service instance whose user, service class and instance name is known, e.g. `/users/joe/services/hbase/demo1`, and retrieves the information needed to connect to the service
2. A client application looks up a statically deployed Hadoop service Example: `/services/hdfs`.
3. An Application Master enumerates all registered component instances, discovers their listed JMX ports, and, initializes own web UI, offers links to these endpoints.
4. A user connects to a private HBase service instance at `/users/joe/services/hbase/demo1`.
5. A user connects to the cluster’s HBase service at `/services/hbase`.
6. A user looks up the binding information to a remote Hadoop cluster’s filesystem at `/net/cluster4/services/hdfs`. The registration information includes the `webhdfs://` URL for the remote filesystem.
7. A user lists their HBase service instances:

   ```
   ls /users/joe/services/hbase
   ```
8. User finds all Hbase services in the cluster:

   ```
   find -endpointField.api=org.apache.hbase
   ```
9. Possibly in future: looking up a service via DNS.

This registry proposal is intended to support these use cases by providing a means for applications to register their service endpoints, and for clients to locate them.

# Key Requirements of a Service Registry

Allow dynamic registration of service instances

* YARN deployed services instances must be able register their bindings and be discovered by clients.
* Core Hadoop service instances must be able to register their service endpoints.
* The binding must be upgradable if the service moves or in case if HA fails over.
* A service instance must be able to publish a variety of endpoints for a service: Web UI, RPC, REST, Zookeeper, others. Furthermore one must also be able register certificates and other public security information may be published as part of a binding.

Registry service properties:

* The registry must be highly available.
* Scale: many services and many clients in a large cluster. This will limit how much data a service can publish.
* Ubiquity: we need this in every YARN cluster, whether physical, virtual or in-cloud.
* Must support hierarchical namespace and names. The name convention must match that of DNS so that we have the option of accessing the namespace via DNS protocol at a later phase of the project.
* Registry API Language/Protocols
* Cross-language: independent of any language; client language != service
* REST API for reading registry data

Access Control:

* Read access for all
* Write is restricted so that squatting and impersonation can be avoided.

Remote accessibility: supports remote access even on clusters which are only reachable via Apache Knox, or hosted in cloud environments.

## Non-Requirements

* The registry is not intended for liveness detection, leader-election or perform other “shared consensual state” actions for an application itself, other than potentially sharing binding information between component instances.
* The registry is not intended to be a store for arbitrary application state, or for publishing configuration data other than binding information to endpoints offered by a service and its components. Such use would overload the registry and rapidly reach limits of what Zookeeper permits.

# Architecture

We propose a base registry service that binds string-names to records describing service and component instances. We plan to use ZK as the base name service since it supports many of the properties, We pick a part of the ZK namespace to be the root of the service registry ( default: `yarnRegistry`).

On top this base implementation we build our registry service API and the naming conventions that YARN will use for its services. The registry will be accessed by the registry API, not directly via ZK - ZK is just an implementation choice (although unlikely to change in the future).

1. Services are registered by binding a ***path*** to a value called a ***Service Record***. Paths are hierarchical and use `/` as the root as well as the separator.
2. Service records are registered as persistent znodes. This ensures that the record remains present during planned and unplanned outages of the service, on the assumption that client code is resilient to transient outages.
3. Each service instance’s service record lists the endpoints for its various protocols exported by that service instance.
4. For each protocol endpoint it must contain

   1. The *protocol* name including: Web, REST, IPC, zookeeper. (type:string)
   2. Its *address*: the specific details used to locate this endpoint
   3. Its *addressType*. This is the format of the binding string. (URL, ZK path, hostname:port pair). For the predefined protocols, we will define what format the binding string MUST be. Example: `protocol==REST` means binding type is `URL`, `protocol==IPC` binding uses the addresstype `host/port`.
   4. The *api*. This is the API offered by the endpoint, and is application specific. examples: `org.apache.hadoop.namenode`, `org.apache.hadoop.webhdfs`
5. Endpoints may be *external* —for use by programs other than the service itself, and *internal* —for connecting components within the service instance. They will be listed in different sections of the Service Record to distinguish them.
6. Core services will be registered using the following convention: `/services/{servicename}` e.g. `/services/hdfs`.
7. YARN services SHOULD be registered using the following convention:

   ```
   /users/{username}/{serviceclass}/{instancename}
   ```
8. Component instances SHOULD be registered under

   ```
   /users/{username}/{serviceclass}/{instancename}/components/{componentname}
   ```
9. Each of the user’s services which follows this convention must have unique service class names,
10. Each component instance must have a name that is unique for that service instance. For a YARN-deployed application, this can be trivially derived from the container ID.

The requirements for unique names ensures that the path to a service instance or component instance is guaranteed to be unique, and that all instances of a specific service class can be enumerated by listing all children of the service class path.

# Registry Model

Service entries MUST be persistent —it is the responsibility of YARN and other tools to determine when a service entry is to be deleted.

## Path Elements

All path elements MUST match that of a lower-case entry in a hostname path as defined in RFC1123; the regular expression is:

```
([a-z0-9]|([a-z0-9][a-z0-9\-]*[a-z0-9]))
```

This policy will ensure that were the registry hierarchy ever to exported by a DNS service, all service classes and names would be valid.

A complication arises with user names, as platforms may allow user names with spaces, high unicode and other characters in them. Such paths must be converted to valid DNS hostname entries using the punycode convention used for internationalized DNS.

## Service Record

A Service Record has some basic information and possibly empty lists of internal and external endpoints.

### Service Record:

A Service Record contains some basic informations and two lists of endpoints: one list for users of a service, one list for internal use within the application.

|  |  |
| --- | --- |
| Name | Description |
| type: String | Always: "JSONServiceRecord" |
| description: String | Human-readable description. |
| external: List[Endpoint] | A list of service endpoints for external callers. |
| internal: List[Endpoint] | A list of service endpoints for internal use within the service instance. |

The type field MUST be `"JSONServiceRecord"`. Mandating this string allows future record types *and* permits rapid rejection of byte arrays that lack this string before attempting to parse the data with a JSON parser.

### YARN Persistence policies

The attributes, `yarn:id` and `yarn:persistence` specify which records *and any child entries* may be deleted as the associated YARN components complete.

The `yarn:id` field defines the application, attempt or container ID to match; the `yarn:persistence` attribute defines the trigger for record cleanup, and implicitly the type of the contents of the `yarn:id` field.

These attributes use the prefix “`yarn:`” to indicate that their reliance on the YARN layer of the Hadoop cluster to implement the policy. If the registry were to run standalone —which is entirely possible— all records would be implicitly persistent.

|  |  |  |
| --- | --- | --- |
| Name | Description | contents of `yarn:id` field |
| permanent | The record persists until removed manually. | (unused) |
| application | Remove when the YARN application defined in the id field terminates. | application ID |
| application-attempt | Remove when the current YARN application attempt finishes. | application attempt ID |
| container | Remove when the YARN container in the ID field finishes | container ID |

The policies which clean up when an application, application attempt or container terminates require the `yarn:id` field to match that of the application, attempt or container. If the wrong ID is set, the cleanup does not take place —and if set to a different application or container, will be cleaned up according the lifecycle of that application.

### Endpoint:

|  |  |
| --- | --- |
| Name | Description |
| api: URI as String | API implemented at the end of the binding || protocol: String | Protocol. Examples: `http`, `https`, `hadoop-rpc`, `zookeeper`, `web`, `REST`, `SOAP`, ... |
| addressType: String | format of the binding |

| addresses: List[Map[String, String]] | a list of address maps |

All string fields have a limit on size, to dissuade services from hiding complex JSON structures in the text description.

#### Field `addressType`: Address Type

The `addressType` field defines the string format of entries.

Having separate types is that tools (such as a web viewer) can process binding strings without having to recognize the protocol.

|  |  |
| --- | --- |
| Format | binding format |
| uri | uri:URI of endpoint |
| hostname | hostname: service host |
| inetaddress | hostname: service host, port: service port |
| path | path: generic unix filesystem path |
| zookeeper | hostname: service host, port: service port, path: ZK path |

In the zookeeper binding, every entry represents a single node in quorum, the `hostname` and `port` fields defining the hostname of the ZK instance and the port on which it is listening. The `path` field lists zookeeper path for applications to use. For example, for HBase this would refer to the znode containing information about the HBase cluster.

The path MUST be identical across all address elements in the `addresses` list. This ensures that any single address contains enough information to connect to the quorum and connect to the relevant znode.

New Address types may be defined; if not standard please prefix with the character sequence `"x-"`.

### Field `api`: API identifier

The API field MUST contain a URI that identifies the specific API of an endpoint. These MUST be unique to an API to avoid confusion.

The following strategies are suggested to provide unique URIs for an API

1. The SOAP/WS-\* convention of using the URL to where the WSDL defining the service
2. A URL to the svn/git hosted document defining a REST API
3. the `classpath` schema followed by a path to a class or package in an application.
4. The `uuid` schema with a generated UUID.

It is hoped that standard API URIs will be defined for common APIs. Two such non-normative APIs are used in this document

* `http://` : A web site for humans
* `classpath:javax.management.jmx`: and endpoint supporting the JMX management protocol (RMI-based)

### Examples of Service Entries

Here is an example of a service entry for a YARN-deployed tomcat application.

After creation and registration of the application, the registry looks as follows:

```
/users
  /devteam
   /org-apache-tomcat
     /test1
       /components
         /container-1408631738011-0001-01-000002
         /container-1408631738011-0001-01-000001
```

The `/users/devteam/org-apache-tomcat/tomcat-test` service record describes the overall application. It exports the URL to a load balancer.

```
{
  "description" : "tomcat-based web application",
  "external" : [ {
    "api" : "http://internal.example.org/restapis/scheduler/20141026v1",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [
     { "uri" : "http://loadbalancer/" },
     { "uri" : "http://loadbalancer2/" }
      ]
  } ],
  "internal" : [ ]
}
```

The service instance is built from two component instances, each described with their container ID converted into a DNS-compatible hostname. The entries are marked as ephemeral. If the entries were set within the container, then when that container is released or if the component fails, the entries will be automatically removed. Accordingly, it’s persistence policy is declared to be “3”, container. The `yarn:id` field identifies the container whose completion will trigger the deletion of this entry

```
/users/devteam/org-apache-tomcat/test1/components/container-1408631738011-0001-01-000001

{
  "yarn:id" : "container_1408631738011_0001_01_000001",
  "yarn:persistence" : "container",
  "description" : "",
  "external" : [ {
    "api" : "http://internal.example.org/restapis/scheduler/20141026v1",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [{ "uri" : "rack4server3:43572" }  ]
  } ],
  "internal" : [ {
    "api" : "classpath:javax.management.jmx",
    "addressType" : "host/port",
    "protocol" : "rmi",
    "addresses" : [ {
      "host" : "rack4server3",
      "port" : "48551"
    } ]
  } ]
}
```

The component instances list their endpoints: the public REST API as an external endpoint, the JMX addresses as internal.

```
/users/devteam/org-apache-tomcat/test1/components/container-1408631738011-0001-01-000002

{
  "registrationTime" : 1408638082445,
  "yarn:id" : "container_1408631738011_0001_01_000002",
  "yarn:persistence" : "container",
  "description" : null,
  "external" : [ {
    "api" : "http://internal.example.org/restapis/scheduler/20141026v1",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ [ "http://rack1server28:35881" ] ]
  } ],
  "internal" : [ {
    "api" : "classpath:javax.management.jmx",
    "addressType" : "host/port",
    "protocol" : "rmi",
    "addresses" : [ {
      "host" : "rack1server28",
      "port" : "48551"
    } ]
  } ]
}
```

This information could be used by the (hypothetical) load balancer to enumerate the components and build a list of component instances to dispatch requests to. Similarly, a management application could enumerate all available component instances and their JMX ports, then connect to each to collect performance metrics.

# Registry API

Here is the registry API as seen from a Java application. The API is a thin layer above the ZK operations, essentially building up paths, reading, writing and updating entries, and enumerating children. The REST API is implemented inside a server and use this same API to implement its REST API.

The exceptions that are listed are only a subset of possible exception —the interface merely lists those that have special meaning.

All write operations must assume that they are communicating with a registry service with the consistency view of a Zookeeper client; read-only clients must assume that their view may be somewhat out of date.

All clients must recognize that the registry is a shared resource and that it may change during a sequence of actions.

### Registry Operations

```
public interface RegistryOperations extends Service {

  /**
   * Create a path.
   *
   * It is not an error if the path exists already, be it empty or not.
   *
   * The createParents flag also requests creating the parents.
   * As entries in the registry can hold data while still having
   * child entries, it is not an error if any of the parent path
   * elements have service records.
   *
   * @param path path to create
   * @param createParents also create the parents.
   * @throws PathNotFoundException parent path is not in the registry.
   * @throws InvalidPathnameException path name is invalid.
   * @throws IOException Any other IO Exception.
   * @return true if the path was created, false if it existed.
   */
  boolean mknode(String path, boolean createParents)
      throws PathNotFoundException,
      InvalidPathnameException,
      IOException;

  /**
   * Set a service record to an entry
   * @param path path to service record
   * @param record service record service record to create/update
   * @param createFlags creation flags
   * @throws PathNotFoundException the parent path does not exist
   * @throws FileAlreadyExistsException path exists but create flags
   * do not include "overwrite"
   * @throws InvalidPathnameException path name is invalid.
   * @throws IOException Any other IO Exception.
   */
  void bind(String path, ServiceRecord record, int createFlags)
      throws PathNotFoundException,
      FileAlreadyExistsException,
      InvalidPathnameException,
      IOException;

  /**
   * Resolve the record at a path
   * @param path path to service record
   * @return the record
   * @throws PathNotFoundException path is not in the registry.
   * @throws InvalidPathnameException the path is invalid.
   * @throws IOException Any other IO Exception
   */

  ServiceRecord resolve(String path) throws PathNotFoundException,
      InvalidPathnameException,
      IOException;

  /**
   * Get the status of a path
   * @param path path to query
   * @return the status of the path
   * @throws PathNotFoundException path is not in the registry.
   * @throws InvalidPathnameException the path is invalid.
   * @throws IOException Any other IO Exception
   */
  RegistryPathStatus stat(String path)
      throws PathNotFoundException,
      InvalidPathnameException,
      IOException;

  /**
   * Probe for a path existing.
   * This is equivalent to {@link #stat(String)} with
   * any failure downgraded to a
   * @param path path to query
   * @return true if the path was found
   * @throws IOException
   */
  boolean exists(String path) throws IOException;

 /**
   * List all entries under a registry path
   * @param path path to query
   * @return a possibly empty list of the full path names of
   * child entries
   * @throws PathNotFoundException
   * @throws InvalidPathnameException
   * @throws IOException
   */
   List<String> list(String path) throws
      PathNotFoundException,
      InvalidPathnameException,
      IOException;

  /**
   * Delete a path.
   *
   * If the operation returns without an error then the entry has been
   * deleted.
   * @param path path delete recursively
   * @param recursive recursive flag
   * @throws PathNotFoundException path is not in the registry.
   * @throws InvalidPathnameException the path is invalid.
   * @throws PathIsNotEmptyDirectoryException path has child entries, but
   * recursive is false.
   * @throws IOException Any other IO Exception
   *
   */
  void delete(String path, boolean recursive)
      throws PathNotFoundException,
      PathIsNotEmptyDirectoryException,
      InvalidPathnameException,
      IOException;

  /**
   * Add a new write access entry to be added to node permissions in all
   * future write operations of a session connected to a secure registry.
   *
   * This does not grant the session any more rights: if it lacked any write
   * access, it will still be unable to manipulate the registry.
   *
   * In an insecure cluster, this operation has no effect.
   * @param id ID to use
   * @param pass password
   * @return true if the accessor was added: that is, the registry connection
   * uses permissions to manage access
   * @throws IOException on any failure to build the digest
   */
  boolean addWriteAccessor(String id, String pass) throws IOException;

  /**
   * Clear all write accessors.
   *
   * At this point all standard permissions/ACLs are retained,
   * including any set on behalf of the user
   * Only  accessors added via {@link #addWriteAccessor(String, String)}
   * are removed.
   */
  public void clearWriteAccessors();
}
```

### `RegistryPathStatus`

The `RegistryPathStatus` class summarizes the contents of a node in the registry.

```
public class RegistryPathStatus {

  /**
   * Short path in the registry to this entry
   */
  public String path;

  /**
   * Timestamp
   */
  public long time;

  /**
   * Entry size in bytes, as returned by the storage infrastructure.
   * In zookeeper, even "empty" nodes have a non-zero size.
   */
  public long size;

  /**
   * Number of child nodes
   */
  public int children;
}
```

## Security

The registry will allow a service instance can only be registered under the path where it has permissions. YARN will create directories with appropriate permissions for users where YARN deployed services can be registered by a user. of the user account of the service instance. The admin will also create directories (such as `/services`) with appropriate permissions (where core Hadoop services can register themselves.

There will no attempt to restrict read access to registry information. The services will protect inappropriate access by clients by requiring authentication and authorization. There is a *scope* field in a service record , but this is just a marker to say “internal API only”, rather than a direct security restriction. (this is why “internal” and “external” are proposed, not “public” and “private”).

Rationale: the endpoints being registered would be discoverable through port scanning anyway. Having everything world-readable allows the REST API to have a simpler access model —and is consistent with DNS.

On a secure cluster, ZK token renewal may become an issue for long-lived services —if their token expires their session may expire. Renewal of such tokens is not part of the API implementation —we may need to add a means to update the tokens of an instance of the registry operations class.

### Security Policy Summary

In an a non-Kerberos Zookeeper Cluster, no security policy is implemented.

The registry is designed to be secured *on a kerberos-managed cluster*.

* The registry root grants full rights to “system accounts”: `mapred`, `hdfs`, `yarn` : `"rwcda"`; all other accounts, and anonymous access is read-only.
* The permissions are similarly restricted for `/users`, and `/services/`
* installations may extend or change these system accounts.
* When an application belonging to a user is scheduled, YARN SHALL create an entry for that user `/users/${username}`.
* This node will have full access to the system; the user the access rights: `"crd"`. That is, they may create or delete child nodes, but not write to their home node, —or alter its permissions.
* Applications wishing to write to the registry must use a SASL connection to authenticate via Zookeeper,
* Applications creating nodes in the user path MUST include the site-specified system accounts in the ACL list, with full access.
* Applications creating nodes in the user path MUST include an ACL Which
* Applications creating nodes in the user path MUST declare their own user identity as a `sasl:user@REALM` entry.
* Applications creating nodes the user path MAY add extra `digest:` ACL tokens so as to give their services the ability to manipulate portions of the registry *without needing kerberos credentials*.

The digest-driven authentication avoid the problem of credential renewal in long-lived applications. An YARN application may be passed the token to connect with the ZK service when launched. It can then create or update an entry, including a secret digest ACL in the permissions of nodes it creates. As a result, even after the credentials expire, it retains *some* access.

Note that for this to be successful, the client will need to fall back session to *not* use SASL, instead using authentication id:pass credentials.

## Out of cluster and cross-cluster access

1. A client should be able to access the registry of another cluster in order to access services of that cluster. Detail of this need to further fleshed out.
2. Firewall services such as Apache Knox can examine the internal set of published services, and publish a subset of their endpoints. They MAY implement a future REST API.

# Limits

**Entry Size**

Zookeeper has a default limit of 1MB/node. If all endpoints of a service or component are stored in JSON attached to that node, then there is a total limit of 1MB of all endpoint registration data.

To prevent this becoming a problem, the client API should implement strict limits on the maximum length of fields, with low limits on the addressType, protocol, and api fields, something longer on the description and addresses elements —along with a limit on the number of elements in the addresses field.

**Name size**

To support DNS in future, there must be a limit of 63 bytes on all path elements. For non-ASCII User names, this restriction implies that a shorter path may be a limit.

**Rate of Update**

A rapid rate of entry change is considered antisocial in a ZK cluster. Implementations may throttle update operations.

**Rate of Polling**

Clients which poll the registry may be throttled.

# Complete service record example

Below is a (non-normative) example of a service record retrieved from a YARN application.

```
{
  "type" : "JSONServiceRecord",
  "description" : "Slider Application Master",
  "yarn:persistence" : "application",
  "yarn:id" : "application_1414052463672_0028",
  "external" : [ {
    "api" : "classpath:org.apache.slider.appmaster",
    "addressType" : "host/port",
    "protocol" : "hadoop/IPC",
    "addresses" : [ {
      "port" : "48551",
      "host" : "nn.example.com"
    } ]
  }, {
    "api" : "http://",
    "addressType" : "uri",
    "protocol" : "web",
    "addresses" : [ {
      "uri" : "http://nn.example.com:40743"
    } ]
  }, {
    "api" : "classpath:org.apache.slider.management",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ {
      "uri" : "http://nn.example.com:40743/ws/v1/slider/mgmt"
    } ]
  }, {
    "api" : "classpath:org.apache.slider.publisher",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ {
      "uri" : "http://nn.example.com:40743/ws/v1/slider/publisher"
    } ]
  }, {
    "api" : "classpath:org.apache.slider.registry",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ {
      "uri" : "http://nn.example.com:40743/ws/v1/slider/registry"
    } ]
  }, {
    "api" : "classpath:org.apache.slider.publisher.configurations",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ {
      "uri" : "http://nn.example.com:40743/ws/v1/slider/publisher/slider"
    } ]
  }, {
    "api" : "classpath:org.apache.slider.publisher.exports",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ {
      "uri" : "http://nn.example.com:40743/ws/v1/slider/publisher/exports"
    } ]
  } ],
  "internal" : [ {
    "api" : "classpath:org.apache.slider.agents.secure",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ {
      "uri" : "https://nn.example.com:52705/ws/v1/slider/agents"
    } ]
  }, {
    "api" : "classpath:org.apache.slider.agents.oneway",
    "addressType" : "uri",
    "protocol" : "REST",
    "addresses" : [ {
      "uri" : "https://nn.example.com:33425/ws/v1/slider/agents"
    } ]
  } ]
}
```

It publishes a number of endpoints, both internal and external.

External:

1. The IPC hostname and port for client-AM communications
2. URL to the AM’s web UI
3. A series of REST URLs under the web UI for specific application services. The details are irrelevant —note that they use an application-specific API value to ensure uniqueness.

Internal:

1. Two URLs to REST APIs offered by the AM for containers deployed by the application itself.

Python agents running in the containers retrieve the internal endpoint URLs to communicate with their AM. The record is resolved on container startup and cached until communications problems occur. At that point the registry is queried for the current record, then an attempt is made to reconnect to the AM.

Here “connectivity” problems means both “low level socket/IO errors” and “failures in HTTPS authentication”. The agents use two-way HTTPS authentication —if the AM fails and another application starts listening on the same ports it will trigger an authentication failure and hence service record reread.

---
# Using the Hadoop Service Registry

The Hadoop service registry can be used in a number of ways :-

1. To register dynamic YARN-deployed applications with entries that match the lifespan of the YARN application. Service Records can be set to be deleted on the completion of the YARN application, the application attempt, or an individual container.
2. To look up static or dynamic applications and the mechanisms to communicate with them. Those mechanisms can include: HTTP(S) URLs, Zookeeper paths, hostnames and ports and even paths in a Hadoop filesystem to configuration data.
3. On a secure cluster, to verify that a service binding has been published by a specific user, or a system account. This can be done simply by looking at the path under which an entry has been placed.
4. To register static applications. These will remain in the registry until deleted. They can be updated as required.

A user of the registry may be both a publisher of entries —Service Records— and a consumer of other services located via their service records. Different parts of a distributed application may also use it for different purposes. As an example, the Application Master of a YARN application can publish bindings for use by its worker containers. The code running in the containers which can then look up the bindings to communicate with that manager even if it was restarted on different nodes in the cluster. Client applications can look up external service endpoints to interact with the AM via a public API.

The registry cannot be used:-

* To subscribe to service records or registry paths and listen for changes.
* To directly share arbitrary data from a server for their clients. Such data must be published by some other means, a means which the registry entry can publish.
* To share secrets between processes. The registry is world readable.

## Registry Application Design Patterns

### Short-lived YARN Application Masters registering their public service endpoints.

1. A YARN application is deployed. In a secure cluster, it is given the kerberos token to write to the registry.
2. When launched, it creates a service record at a known path
3. This record MAY have application attempt persistence policy of and an ID of the application attempt

   ```
   yarn:persistence = "application_attempt"
   yarn:id = ${application_attemptId}
   ```

   This means that the record will be deleted when the application attempt completes, even if a new attempt is created. Every Application attempt will have to re-register the endpoint —which may be needed to locate the service anyway.
4. Alternatively, the record MAY have the persistence policy of “application”:

   ```
   yarn:persistence = "application_attempt"
   yarn:id = application_attemptId
   ```

   This means that the record will persist even between application attempts, albeit with out of date endpoint information.
5. Client applications look up the service by way of the path.

The choice of path is an application specific one. For services with a YARN application name guaranteed to be unique, we recommend a convention of:

```
/users/${username}/applications/${service-class}/${instance-name}
```

Alternatively, the application Id can be used in the path:

```
/users/${username}/applications/${service-class}/${applicationId}
```

The latter makes mapping a YARN application listing entry to a service record trivial.

Client applications may locate the service

* By enumerating all instances of a service class and selecting one by specific critera.
* From a supplied service class and instance name
* If listed by application ID, from the service class and application ID.

After locating a service record, the client can enumerate the `external` bindings and locate the entry with the desired API.

### YARN Containers registering their public service endpoints

Here all containers in a YARN application are publishing service endpoints for public consumption.

1. The deployed containers are passed the base path under which they should register themselves.
2. Long-lived containers must be passed an `id:password` pair which gives them the right to update these entries without the kerberos credentials of the user. This allows the containers to update their entries even after the user tokens granting the AM write access to a registry path expire.
3. The containers instantiate a registry operations instance with the `id:password` pair.
4. They then a register service record on a path consisting of:

   ```
   ${base-path} + "/" + RegistryPathUtils.encodeYarnID(containerId)
   ```

   This record should have the container persistence policy an ID of the container

   ```
   yarn:persistence = "container"
   yarn:id = containerId
   ```

   When the container is terminated, the entry will be automatically deleted.
5. The exported service endpoints of this container-deployed service should be listed in the `external` endpoint list of the service record.
6. Clients can enumerate all containers exported by a YARN application by listing the entries under `${base-path}`.

### Registering Static cluster services.

Services which are generally fixed in a cluster, but which need to publish binding and configuration information may be published in the registry. Example: an Apache Oozie service. Services external to the cluster to which deployed applications may also be published. Example: An Amazon Dynamo instance.

These services can be registered under paths which belong to the users running the service, such as `/users/oozie` or `/users/hbase`. Client applications would use this path. While this can authenticate the validity of the service record, it does rely on the client applications knowing the username a service is deployed on, or being configured with the full path.

The alternative is for the services to be deployed under a static services path, under `/services`. For example, `/services/oozie` could contain the registration of the Oozie service. As the permissions for this path are restricted to pre-configured system accounts, the presence of a service registration on this path on a secure cluster, confirms that it was registered by the cluster administration tools.

1. The service is deployed by some management tool, or directly by the cluster operator.
2. The deployed application can register itself under its own user name if given the binding information for the registry.
3. If the application is to be registered under `/services` and it has been deployed by one of the system user accounts —it may register itself directly.
4. If the application does not have the permissions to do so, the cluster administration tools must register the service instead.
5. Client applications may locate a service by resolving its well known/configured path.
6. If a service is stopped, the administration tools may delete the entry, or retain the entry but delete all it service endpoints. This is a proposed convention to indicate “the service is known but not currently reachable”.
7. When a service is restarted, its binding information may be updated, or its entire registry entry recreated.

### YARN containers locating their Application Master

Here YARN containers register with their AM to receive work, usually by some heartbeat mechanism where they report in regularly. If the AM is configured for containers to outlive the application attempt, when an AM fails the containers keep running. These containers will need to bind to any restarted AM. They may also wish to conclude that if an AM does not restart, that they should eventually time out and terminate themselves. Such a policy helps the application react to network partitions.

1. The YARN AM publishes its service endpoints such as the FQDN and socket port needed for IPC communications, or an HTTP/HTTPS URL needed for a REST channel. These are published in the `internal` endpoint list, with the `api` field set to a URL of the specific API the containers use.
2. The YARN containers are launched with the path to the service record (somehow) passed to them. Environment variables or command line parameters are two viable mechanisms. Shared secrets should also be passed that way: command line parameters are visible in the unix `ps` command. More secure is saving shared secrets to the cluster filesystem, passing down the path to the containers. The URI to such as path MAY be one of the registered internal endpoints of the application.
3. The YARN containers look up the service registry to identify the communications binding.
4. If the registered service entry cannot be found, the container MAY do one of: exit. spin with some (jittered) retry period, polling for the entry, until the entry reappears. This implies that the AM has been found.
5. If the service entry is found, the client should attempt to communicate with the AM on its channel. Shared authentication details may be used to validate the client with the server and vice versa.
6. The client report in to the AM until the connections start failing to connect or authenticate, or when a long lived connection is broken and cannot be restarted.
7. A this point the client may revert to step (3). Again, some backoff policy with some jitter helps stop a newly-restarted AM being overloaded. Containers may also with to have some timeout after which they conclude that the AM is not coming back and exit.
8. We recommend that alongside the functional commands that an AM may issue to a client, a “terminate” command can be issued to a container. This allows the system to handle the specific situation of the YARN Node Manager terminating while spawned containers keep running.

### YARN Applications and containers publishing their management and metrics bindings

Management ports and bindings are simply others endpoint to publish. These should be published as *internal* endpoints, as they are not intended for public consumption.

### Client application enumerating services by endpoint APIs

A client application wishes to locate all services implementing a specific API, such as `"classpath://org.apache.hbase"`

1. The client starts from a path in the registry
2. The client calls `registryOperations.list(path)` to list all nodes directly under that path, getting a relative list of child nodes.
3. the client enumerates the child record statuses by calling `stat()` on each child.
4. For all status entries, if the size of the entry is greater than the value of `ServiceRecordHeader.getLength()`, it MAY contain a service record.
5. The contents can be retrieved using the `resolve()` operation. If successful, it does contain a service record —so the client can enumerate the `external` endpoints and locate the one with the desired API.
6. The `children` field of each `RegistryPathStatus` status entry should be examined. If it is >= 0, the enumeration should be performed recursively on the path of that entry.
7. The operation ultimately completes with a list of all entries.
8. One of the enumerated endpoints may be selected and used as the binding information for a service

This algorithm describes a depth first search of the registry tree. Variations are of course possible, including breadth-first search, or immediately halting the search as soon as a single entry point. There is also the option of parallel searches of different subtrees —this may reduce search time, albeit at the price of a higher client load on the registry infrastructure.

A utility class `RegistryUtils` provides static utility methods for common registry operations,in particular, `RegistryUtils.listServiceRecords(registryOperations, path)` performs the listing and collection of all immediate child record entries of a specified path.

Client applications are left with the problem of “what to do when the endpoint is not valid”, specifically, when a service is not running —what should be done?

Some transports assume that the outage is transient, and that spinning retries against the original binding is the correct strategy. This is the default policy of the Hadoop IPC client.

Other transports fail fast, immediately reporting the failure via an exception or other mechanism. This is directly visible to the client —but does allow the client to rescan the registry and rebind to the application.

Finally, some application have been designed for dynamic failover from the outset: their published binding information is actually a zookeeper path. Apache HBase and Apache Accumulo are examples of this. The registry is used for the initial lookup of the binding, after which the clients are inherently resilient to failure.

---
# Registry Security

This document describes how security is implemented in the service registry

In a non-Kerberos-enabled Hadoop cluster, the Registry does not offer any security at all: the registry is world writeable.

This document is therefore relevant only to secure clusters.

## Security Model

The security model of the registry is designed to meet the following goals a secure registry: 1. Deliver functional security on a secure ZK installation. 1. Allow the RM to create per-user regions of the registration space 1. Allow applications belonging to a user to write registry entries into their part of the space. These may be short-lived or long-lived YARN applications, or they may be static applications. 1. Prevent other users from writing into another user’s part of the registry. 1. Allow system services to register to a `/services` section of the registry. 1. Provide read access to clients of a registry. 1. Permit future support of DNS 1. Permit the future support of registering data private to a user. This allows a service to publish binding credentials (keys &c) for clients to use. 1. Not require a ZK keytab on every user’s home directory in a YARN cluster. This implies that kerberos credentials cannot be used by YARN applications.

ZK security uses an ACL model, documented in [Zookeeper and SASL](https://cwiki.apache.org/confluence/display/ZOOKEEPER/Zookeeper+and+SASL) In which different authentication schemes may be used to restrict access to different znodes. This permits the registry to use a mixed Kerberos + Private password model.

* The YARN-based registry (the `RMRegistryOperationsService`), uses kerberos as the authentication mechanism for YARN itself.
* The registry configures the base of the registry to be writeable only by itself and other hadoop system accounts holding the relevant kerberos credentials.
* The user specific parts of the tree are also configured to allow the same system accounts to write and manipulate that part of the tree.
* User accounts are created with a `(username,password)` keypair granted write access to their part of the tree.
* The secret part of the keypair is stored in the users’ home directory on HDFS, using the Hadoop Credentials API.
* Initially, the entire registry tree will be world readable.

What are the limitations of such a scheme?

1. It is critical that the user-specific registry keypair is kept a secret. This relies on filesystem security to keep the file readable only by the (authenticated) user.
2. As the [ZK Documentation says](http://zookeeper.apache.org/doc/r3.4.6/zookeeperProgrammers.html#sc_ZooKeeperAccessControl), \*" Authentication is done by sending the username:password in clear text"
3. While it is possible to change the password for an account, this involves a recursive walk down the registry tree, and will stop all running services from being able to authenticate for write access until they reload the key.
4. A world-readable registry tree is exposing information about the cluster. There is some mitigation here in that access may be restricted by IP Address.
5. There’s also the need to propagate information from the registry down to the clients for setting up ACLs.

## ACL Configuration propagation

The registry manager cannot rely on clients consistently setting ZK permissions. At the very least, they cannot relay on client applications unintentionally wrong values for the accounts of the system services

*Solution*: Initially, a registry permission is used here.

### Automatic domain extension

In a kerberos domain, it is possible for a kerberized client to determine the realm of a cluster at run time from the local user’s kerberos credentials as used to talk to YARN or HDFS.

This can be used to auto-generate account names with the correct realm for the system accounts hence aid having valid constants.

This allows the registry to support a default configuration value for `hadoop.registry.system.accounts` of:

```
  "sasl:yarn@, sasl:mapred@, sasl:hdfs@, sasl:hadoop@";
```

#### In-registry publishing of core binding data

Another strategy could be to have a `ServiceRecord` at the root of the registry that actually defines the registry —including listing those default binding values in the `data` field..

### Auditing

Something (perhaps the RM) could scan a user’s portion of the registry and detect some ACL problems: IP/world access too lax, admin account settings wrong. It cannot view or fix the ACL permissions unless it has the `ADMIN` permission, though that situation can at least be detected. Given the RM must have `DELETE` permissions further up the stack, it would be in a position to delete the errant part of the tree —though this could be a destructive overreaction.

## Further Reading

* [Zookeeper and SASL](https://cwiki.apache.org/confluence/display/ZOOKEEPER/Zookeeper+and+SASL)
* [Up and Running with Secure Zookeeper](https://github.com/ekoontz/zookeeper/wiki)

---
# Registry DNS Server

* [Introduction](#Introduction)
* [Service Properties](#Service_Properties)
  * [Functional properties](#Functional_properties)
  * [Deployment properties](#Deployment_properties)
* [DNS Record Name Structure](#DNS_Record_Name_Structure)
  * [Notes about DNS Names](#Notes_about_DNS_Names)
* [DNS Server Functionality](#DNS_Server_Functionality)
  * [DNS record creation](#DNS_record_creation)
  * [DNS record removal](#DNS_record_removal)
  * [DNS Service initialization](#DNS_Service_initialization)
* [Start the DNS Server](#Start_the_DNS_Server)
* [Configuration](#Configuration)
  * [Sample configurations](#Sample_configurations)
* [Make your cluster use Registry DNS](#Make_your_cluster_use_Registry_DNS)

The document describes the internals of Registry DNS server. It is based on the [Hadoop service registry](../registry/index.html) which is backed by a zookeeper cluster.

## Introduction

The Registry DNS Server provides a standard DNS interface to the information posted into the Hadoop Registry by deployed applications. The DNS service serves the following functions:

1. **Exposing existing service-discovery information via DNS** - Information provided in the current Hadoop service registry’s records will be converted into DNS entries, thus allowing users to discover information about YARN applications using standard DNS client mechanisms (e.g. a DNS SRV Record specifying the hostname and port number for services).
2. **Enabling Container to IP mappings** - Enables discovery of the IPs of containers via standard DNS lookups. Given the availability of the records via DNS, container name-based communication will be facilitated (e.g. `curl http://solr-0.solr-service.devuser.yarncluster:8983/solr/admin/collections?action=LIST`).

## Service Properties

The existing Hadoop Service Registry is leveraged as the source of information for the DNS Service.

The following core functions are supported by the DNS-Server:

### Functional properties

1. Supports creation of DNS records for end-points of the deployed YARN applications
2. Record names remain unchanged during restart of containers and/or applications
3. Supports reverse lookups (name based on IP). Note, this works only for Docker containers because other containers share the IP of the host
4. Supports security using the standards defined by The Domain Name System Security Extensions (DNSSEC)
5. Highly available
6. Scalable - The service provides the responsiveness (e.g. low-latency) required to respond to DNS queries (timeouts yield attempts to invoke other configured name servers).

### Deployment properties

1. Supports integration with existing DNS assets (e.g. a corporate DNS server) by acting as a DNS server for a Hadoop cluster zone/domain. The server is not intended to act as a primary DNS server and does not forward requests to other servers. Rather, a primary DNS server can be configured to forward a zone to the registry DNS server.
2. The DNS Server exposes a port that can receive both TCP and UDP requests per DNS standards. The default port for DNS protocols is not in the restricted range (5335). However, existing DNS assets may only allow zone forwarding to non-custom ports. To support this, the registry DNS server can be started in privileged mode.

## DNS Record Name Structure

The DNS names of generated records are composed from the following elements (labels). Note that these elements must be compatible with DNS conventions (see “Preferred Name Syntax” in [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt)):

* **domain** - the name of the cluster DNS domain. This name is provided as a configuration property. In addition, it is this name that is configured at a parent DNS server as the zone name for the defined registry DNS zone (the zone for which the parent DNS server will forward requests to registry DNS). E.g. yarncluster.com
* **username** - the name of the application deployer. This name is the simple short-name (for e.g. the primary component of the Kerberos principal) associated with the user launching the application. As the username is one of the elements of DNS names, it is expected that this also conforms to DNS name conventions (RFC 1035 linked above), so it is converted to a valid DNS hostname entries using the punycode convention used for internationalized DNS.
* **application name** - the name of the deployed YARN application. This name is inferred from the YARN registry path to the application’s node. Application name, rather than application id, was chosen as a way of making it easy for users to refer to human-readable DNS names. This obviously mandates certain uniqueness properties on application names.
* **container id** - the YARN assigned ID to a container (e.g. container\_e3741\_1454001598828\_01\_000004)
* **component name** - the name assigned to the deployed component (for e.g. a master component). A component is a distributed element of an application or service that is launched in a YARN container (e.g. an HBase master). One can imagine multiple components within an application. A component name is not yet a first class concept in YARN, but is a very useful one that we are introducing here for the sake of registry DNS entries. Many frameworks like MapReduce, Slider already have component names (though, as mentioned, they are not yet supported in YARN in a first class fashion).
* **api** - the api designation for the exposed endpoint

### Notes about DNS Names

* In most instances, the DNS names can be easily distinguished by the number of elements/labels that compose the name. The cluster’s domain name is always the last element. After that element is parsed out, reading from right to left, the first element maps to the application user and so on. Wherever it is not easily distinguishable, naming conventions are used to disambiguate the name using a prefix such as “container” or suffix such as “api”. For example, an endpoint published as a management endpoint will be referenced with the name *management-api.griduser.yarncluster.com*.
* Unique application name (per user) is not currently supported/guaranteed by YARN, but it is supported by the YARN service framework. The registry DNS service currently leverages the last element of the ZK path entry for the application as an application name. These application names have to be unique for a given user.

## DNS Server Functionality

The primary functions of the DNS service are illustrated in the following diagram:

![DNS Functional Overview](assets/hadoop_hadoop-project-dist_hadoop-common_images_dns_overview.png "DNS Functional Overview")

### DNS record creation

The following figure illustrates at slightly greater detail the DNS record creation and registration sequence (NOTE: service record updates would follow a similar sequence of steps, distinguished only by the different event type):

![DNS Functional Overview](assets/hadoop_hadoop-project-dist_hadoop-common_images_dns_record_creation.jpeg "DNS Functional Overview")

### DNS record removal

Similarly, record removal follows a similar sequence

![DNS Functional Overview](assets/hadoop_hadoop-project-dist_hadoop-common_images_dns_record_removal.jpeg "DNS Functional Overview")

(NOTE: The DNS Zone requires a record as an argument for the deletion method, thus requiring similar parsing logic to identify the specific records that should be removed).

### DNS Service initialization

* The DNS service initializes both UDP and TCP listeners on a configured port. If a port in the restricted range is desired (such as the standard DNS port 53), the DNS service can be launched using jsvc as described in the section on starting the DNS server.
* Subsequently, the DNS service listens for inbound DNS requests. Those requests are standard DNS requests from users or other DNS servers (for example, DNS servers that have the RegistryDNS service configured as a forwarder).

## Start the DNS Server

By default, the DNS server runs on non-privileged port `5335`. Start the server with:

```
hadoop --daemon start registrydns
```

If the DNS server is configured to use the standard privileged port `53`, the environment variables HADOOP\_REGISTRYDNS\_SECURE\_USER and HADOOP\_REGISTRYDNS\_SECURE\_EXTRA\_OPTS must be uncommented in the hadoop-env.sh file. The DNS server should then be launched as root and jsvc will be used to reduce the privileges of the daemon after the port has been bound.

## Configuration

The Registry DNS server reads its configuration properties from the core-site.xml file. The following are the DNS associated configuration properties:

| Name | Description |
| --- | --- |
| hadoop.registry.zk.quorum | A comma separated list of hostname:port pairs defining the zookeeper quorum for the [Hadoop registry](../registry/registry-configuration.html). |
| hadoop.registry.dns.enabled | The DNS functionality is enabled for the cluster. Default is false. |
| hadoop.registry.dns.domain-name | The domain name for Hadoop cluster associated records. |
| hadoop.registry.dns.bind-address | Address associated with the network interface to which the DNS listener should bind. |
| hadoop.registry.dns.bind-port | The port number for the DNS listener. The default port is 5335. |
| hadoop.registry.dns.dnssec.enabled | Indicates whether the DNSSEC support is enabled. Default is false. |
| hadoop.registry.dns.public-key | The base64 representation of the server’s public key. Leveraged for creating the DNSKEY Record provided for DNSSEC client requests. |
| hadoop.registry.dns.private-key-file | The path to the standard DNSSEC private key file. Must only be readable by the DNS launching identity. See [dnssec-keygen](https://ftp.isc.org/isc/bind/cur/9.9/doc/arm/man.dnssec-keygen.html) documentation. |
| hadoop.registry.dns-ttl | The default TTL value to associate with DNS records. The default value is set to 1 (a value of 0 has undefined behavior). A typical value should be approximate to the time it takes YARN to restart a failed container. |
| hadoop.registry.dns.zone-subnet | An indicator of the IP range associated with the cluster containers. The setting is utilized for the generation of the reverse zone name. |
| hadoop.registry.dns.zone-mask | The network mask associated with the zone IP range. If specified, it is utilized to ascertain the IP range possible and come up with an appropriate reverse zone name. |
| hadoop.registry.dns.zones-dir | A directory containing zone configuration files to read during zone initialization. This directory can contain zone master files named *zone-name.zone*. See [here](http://www.zytrax.com/books/dns/ch6/mydomain.html) for zone master file documentation. |

### Sample configurations

```
 <property>
    <description>The domain name for Hadoop cluster associated records.</description>
    <name>hadoop.registry.dns.domain-name</name>
    <value>ycluster</value>
  </property>

  <property>
    <description>The port number for the DNS listener. The default port is 5335.
    If the standard privileged port 53 is used, make sure start the DNS with jsvc support.</description>
    <name>hadoop.registry.dns.bind-port</name>
    <value>5335</value>
  </property>

  <property>
    <description>The DNS functionality is enabled for the cluster. Default is false.</description>
    <name>hadoop.registry.dns.enabled</name>
    <value>true</value>
  </property>

  <property>
    <description>Address associated with the network interface to which the DNS listener should bind.</description>
    <name>hadoop.registry.dns.bind-address</name>
    <value>localhost</value>
  </property>

  <property>
    <description>A comma separated list of hostname:port pairs defining the zookeeper quorum for the Hadoop registry</description>
    <name>hadoop.registry.zk.quorum</name>
    <value>localhost:2181</value>
  </property>
```

To configure Registry DNS to serve reverse lookup for `172.17.0.0/24`

```
  <property>
    <description>The network mask associated with the zone IP range. If specified, it is utilized to ascertain the
    IP range possible and come up with an appropriate reverse zone name.</description>
    <name>hadoop.registry.dns.zone-mask</name>
    <value>255.255.255.0</value>
  </property>

  <property>
    <description>An indicator of the IP range associated with the cluster containers. The setting is utilized for the
     generation of the reverse zone name.</description>
    <name>hadoop.registry.dns.zone-subnet</name>
    <value>172.17.0.0</value>
  </property>
```

## Make your cluster use Registry DNS

You can edit the `/etc/resolv.conf` to make your system use the registry DNS such as below, where `192.168.154.3` is the ip address of your DNS host. It should appear before any nameservers that would return NXDOMAIN for lookups in the domain used by the cluster.

```
nameserver 192.168.154.3
```

Alternatively, if you have a corporate DNS in your organization, you can configure zone forwarding so that the Registry DNS resolves hostnames for the domain used by the cluster.

---
# Registry Configuration

The Hadoop service registry is built on top of Apache Zookeeper. It is configured by way of a Hadoop `Configuration` class: the instance used to create the service controls the behavior of the client.

This document lists the configuration parameters which control the registry client.

The default values of all these settings are defined in `core-default.xml`. The values in this file may not match those listed in this document. If this is the case, the values in `core-default.xml` MUST be considered normative.

## Changing the configuration values

Changes to the configuration values SHOULD be done in `core-site.xml`. This will ensure that client and non-YARN applications will pick up the values, so enabling them to read from and potentially write to the registry.

## Core Settings

### Setting the Zookeeper Quorum: `hadoop.registry.zk.quorum`

This is an essential setting: it identifies the lists of zookeeper hosts and the ports on which the ZK services are listening.

```
  <property>
    <description>
      A comma separated list of hostname:port pairs defining the
      zookeeper quorum binding for the registry
    </description>
    <name>hadoop.registry.zk.quorum</name>
    <value>localhost:2181</value>
  </property>
```

It takes a comma-separated list, such as `zk1:2181 ,zk2:2181, zk3:2181`

### Setting the Zookeeper Registry Base path: `hadoop.registry.zk.root`

This path sets the base zookeeper node for the registry

```
  <property>
    <description>
      The root zookeeper node for the registry
    </description>
    <name>hadoop.registry.zk.root</name>
    <value>/registry</value>
  </property>
```

The default value of `/registry` is normally sufficient. A different value may be needed for security reasons or because the `/registry` path is in use.

The root value is prepended to all registry paths so as to create the absolute path. For example:

* `/` maps to `/registry`
* `/services` maps to `/registry/services`
* `/users/yarn` maps to `/registry/users/yarn`

A different value of `hadoop.registry.zk.root` would result in a different mapping to absolute zookeeper paths.

## Security Options

Registry security is enabled when the property `hadoop.registry.secure` is set to `true`. Once set, nodes are created with permissions, so that only a specific user *and the configured cluster “superuser” accounts* can write under their home path of `${hadoop.registry.zk.root}/users`. Only the superuser accounts will be able to manipulate the root path, including `${hadoop.registry.zk.root}/services` and `${hadoop.registry.zk.root}/users`.

All write operations on the registry (including deleting entries and paths) must be authenticated. Read operations are still permitted by unauthenticated callers.

The key settings for secure registry support are:

* enabling the secure mode: `hadoop.registry.secure`
* listing the superuser zookeeper ACLs: `hadoop.registry.system.acls`
* listing the kerberos realm for the principals: `hadoop.registry.kerberos.realm`
* identifying the JAAS context within the JAAS configuration which defines the user: `hadoop.registry.jaas.context`

### Enabling security

```
  <property>
    <description>
      Key to set if the registry is secure. Turning it on
      changes the permissions policy from "open access"
      to restrictions on kerberos with the option of
      a user adding one or more auth key pairs down their
      own tree.
    </description>
    <name>hadoop.registry.secure</name>
    <value>false</value>
  </property>
```

### Identifying the client JAAS context

The registry clients must identify the JAAS context which they use to authenticate to the registry.

```
  <property>
    <description>
      Key to define the JAAS context. Used in secure mode
    </description>
    <name>hadoop.registry.jaas.context</name>
    <value>Client</value>
  </property>
```

*Note* as the Resource Manager is simply another client of the registry, it too must have this context defined.

### Identifying the system accounts `hadoop.registry.system.acls`

These are the accounts which are given full access to the base of the registry. The Resource Manager needs this option to create the root paths.

Client applications writing to the registry access to the nodes it creates.

1. The property `hadoop.registry.system.acls` takes a comma-separated list of zookeeper `ACLs` which are given full access to created nodes; the permissions `READ | WRITE | CREATE | DELETE | ADMIN`.
2. Any zookeeper ACL scheme may be added to this, such as the `digest:` scheme.
3. The SASL scheme, `sasl:`, is used to identify which callers identified by sasl have full access. These are the superuser accounts.
4. They may be identified by elements such as `sasl:yarn@REALM.COM`.
5. To aid portability of SASL settings, especially the default value, any `sasl:` entry without the realm value —that is, any entry that terminates in the `@` symbol— has the current realm appended to it.
6. This realm is set to that of the current user.
7. It may be overridden by the property `hadoop.registry.kerberos.realm`.

```
  <property>
    <description>
      A comma separated list of Zookeeper ACL identifiers with
      system access to the registry in a secure cluster.
      These are given full access to all entries.
      If there is an "@" at the end of a SASL entry it
      instructs the registry client to append the default kerberos domain.
    </description>
    <name>hadoop.registry.system.acls</name>
    <value>sasl:yarn@, sasl:mapred@, sasl:mapred@, sasl:hdfs@</value>
  </property>

  <property>
    <description>
      The kerberos realm: used to set the realm of
      system principals which do not declare their realm,
      and any other accounts that need the value.
      If empty, the default realm of the running process
      is used.
      If neither are known and the realm is needed, then the registry
      service/client will fail.
    </description>
    <name>hadoop.registry.kerberos.realm</name>
    <value></value>
  </property>
```

Example: an `hadoop.registry.system.acls` entry of `sasl:yarn@, sasl:admin@EXAMPLE.COM, sasl:system@REALM2`, would, in a YARN cluster with the realm `EXAMPLE.COM`, add the following admin accounts to every node

* `sasl:yarn@EXAMPLE.COM`
* `sasl:admin@EXAMPLE.COM`
* `sasl:system@REALM2`

The identity of a client application creating registry entries will be automatically included in the permissions of all entries created. If, for example, the account creating an entry was `hbase`, another entry would be created

* `sasl:hbase@EXAMPLE.COM`

**Important**: when setting the system ACLS, *it is critical to include the identity of the YARN Resource Manager*.

The RM needs to be able to create the root and user paths, and delete service records during application and container cleanup.

## Zookeeper connection management options

Some low level options manage the ZK connection —more specifically, its failure handling.

The Zookeeper registry clients use Apache Curator to connect to Zookeeper, a library which detects timeouts and attempts to reconnect to one of the servers which forms the zookeeper quorum. It is only after a timeout is detected that a retry is triggered.

```
  <property>
    <description>
      Zookeeper session timeout in milliseconds
    </description>
    <name>hadoop.registry.zk.session.timeout.ms</name>
    <value>60000</value>
  </property>

  <property>
    <description>
      Zookeeper connection timeout in milliseconds
    </description>
    <name>hadoop.registry.zk.connection.timeout.ms</name>
    <value>15000</value>
  </property>

  <property>
    <description>
      Zookeeper connection retry count before failing
    </description>
    <name>hadoop.registry.zk.retry.times</name>
    <value>5</value>
  </property>

  <property>
    <description>
    </description>
    <name>hadoop.registry.zk.retry.interval.ms</name>
    <value>1000</value>
  </property>

  <property>
    <description>
      Zookeeper retry limit in milliseconds, during
      exponential backoff.
      This places a limit even
      if the retry times and interval limit, combined
      with the backoff policy, result in a long retry
      period
    </description>
    <name>hadoop.registry.zk.retry.ceiling.ms</name>
    <value>60000</value>
  </property>
```

The retry strategy used in the registry client is [`BoundedExponentialBackoffRetry`](https://curator.apache.org/apidocs/org/apache/curator/retry/BoundedExponentialBackoffRetry.html): This backs off exponentially on connection failures before eventually concluding that the quorum is unreachable and failing.

## Complete Set of Configuration Options

```
  <!-- YARN registry -->

  <property>
    <description>
      A comma separated list of hostname:port pairs defining the
      zookeeper quorum binding for the registry
    </description>
    <name>hadoop.registry.zk.quorum</name>
    <value>localhost:2181</value>
  </property>

  <property>
    <description>
      The root zookeeper node for the registry
    </description>
    <name>hadoop.registry.zk.root</name>
    <value>/registry</value>
  </property>

  <property>
    <description>
      Key to set if the registry is secure. Turning it on
      changes the permissions policy from "open access"
      to restrictions on kerberos with the option of
      a user adding one or more auth key pairs down their
      own tree.
    </description>
    <name>hadoop.registry.secure</name>
    <value>false</value>
  </property>

  <property>
    <description>
      A comma separated list of Zookeeper ACL identifiers with
      system access to the registry in a secure cluster.

      These are given full access to all entries.

      If there is an "@" at the end of a SASL entry it
      instructs the registry client to append the default kerberos domain.
    </description>
    <name>hadoop.registry.system.acls</name>
    <value>sasl:yarn@, sasl:mapred@, sasl:mapred@, sasl:hdfs@</value>
  </property>

  <property>
    <description>
      The kerberos realm: used to set the realm of
      system principals which do not declare their realm,
      and any other accounts that need the value.

      If empty, the default realm of the running process
      is used.

      If neither are known and the realm is needed, then the registry
      service/client will fail.
    </description>
    <name>hadoop.registry.kerberos.realm</name>
    <value></value>
  </property>

  <property>
    <description>
      Key to define the JAAS context. Used in secure
      mode
    </description>
    <name>hadoop.registry.jaas.context</name>
    <value>Client</value>
  </property>


  <property>
    <description>
      Zookeeper session timeout in milliseconds
    </description>
    <name>hadoop.registry.zk.session.timeout.ms</name>
    <value>60000</value>
  </property>

  <property>
    <description>
      Zookeeper session timeout in milliseconds
    </description>
    <name>hadoop.registry.zk.connection.timeout.ms</name>
    <value>15000</value>
  </property>

  <property>
    <description>
      Zookeeper connection retry count before failing
    </description>
    <name>hadoop.registry.zk.retry.times</name>
    <value>5</value>
  </property>

  <property>
    <description>
    </description>
    <name>hadoop.registry.zk.retry.interval.ms</name>
    <value>1000</value>
  </property>

  <property>
    <description>
      Zookeeper retry limit in milliseconds, during
      exponential backoff: {@value}

      This places a limit even
      if the retry times and interval limit, combined
      with the backoff policy, result in a long retry
      period
    </description>
    <name>hadoop.registry.zk.retry.ceiling.ms</name>
    <value>60000</value>
  </property>
```

---
# Hadoop Groups Mapping

* [Overview](#Overview)
* [Static Mapping](#Static_Mapping)
* [Caching/Negative caching](#Caching.2FNegative_caching)
* [LDAP Groups Mapping](#LDAP_Groups_Mapping)
  * [Bind user(s)](#Bind_user.28s.29)
* [Multiple bind users](#Multiple_bind_users)
  * [Active Directory](#Active_Directory)
  * [POSIX Groups](#POSIX_Groups)
  * [SSL](#SSL)
  * [Low latency group mapping resolution](#Low_latency_group_mapping_resolution)
  * [Configuring retries and multiple LDAP servers with failover](#Configuring_retries_and_multiple_LDAP_servers_with_failover)
* [Composite Groups Mapping](#Composite_Groups_Mapping)
  * [Multiple group mapping providers configuration sample](#Multiple_group_mapping_providers_configuration_sample)

## Overview

The groups of a user is determined by a group mapping service provider. Hadoop supports various group mapping mechanisms, configured by the `hadoop.security.group.mapping` property. Some of them, such as `JniBasedUnixGroupsMappingWithFallback`, use operating systems’ group name resolution and requires no configuration. But Hadoop also supports special group mapping mechanisms through LDAP and composition of LDAP and operating system group name resolution, which require additional configurations. `hadoop.security.group.mapping` can be one of the following:

* **org.apache.hadoop.security.JniBasedUnixGroupsMappingWithFallback**

  The default implementation. It will determine if the Java Native Interface (JNI) is available. If JNI is available, the implementation will use the API within hadoop to resolve a list of groups for a user. If JNI is not available then the shell-based implementation, `ShellBasedUnixGroupsMapping`, is used.
* **org.apache.hadoop.security.JniBasedUnixGroupsNetgroupMappingWithFallback**

  Similar to `JniBasedUnixGroupsMappingWithFallback`. If JNI is available, it obtains netgroup membership using the Hadoop native API; otherwise uses `ShellBasedUnixGroupsNetgroupMapping`.
* **org.apache.hadoop.security.ShellBasedUnixGroupsMapping**

  This implementation shells out with the `bash -c groups` command (for a Linux/Unix environment) or the `net group` command (for a Windows environment) to resolve a list of groups for a user.
* **org.apache.hadoop.security.ShellBasedUnixGroupsNetgroupMapping**

  This implementation is similar to `ShellBasedUnixGroupsMapping`, except that it executes `getent netgroup` command to get netgroup membership.
* **org.apache.hadoop.security.LdapGroupsMapping**

  An alternate implementation, which connects directly to an LDAP server to resolve the list of groups. However, this provider should only be used if the required groups reside exclusively in LDAP, and are not materialized on the Unix servers. LdapGroupsMapping supports SSL connection and POSIX group semantics. See section [LDAP Groups Mapping](#LDAP_Groups_Mapping) for details.
* **org.apache.hadoop.security.CompositeGroupsMapping**

  This implementation composites other group mapping providers for determining group membership. This allows to combine existing provider implementations and composite a virtually new provider without customized development to deal with complex situation. See section [Composite Groups Mapping](#Composite_Groups_Mapping) for details.

For HDFS, the mapping of users to groups is performed on the NameNode. Thus, the host system configuration of the NameNode determines the group mappings for the users.

Note that HDFS stores the user and group of a file or directory as strings; there is no conversion from user and group identity numbers as is conventional in Unix.

## Static Mapping

It is possible to statically map users to groups by defining the mapping in `hadoop.user.group.static.mapping.overrides` in the format `user1=group1,group2;user2=;user3=group2`. This property overrides any group mapping service provider. If a user’s groups are defined in it, the groups are returned without more lookups; otherwise, the service provider defined in `hadoop.security.group.mapping` is used to look up the groups. By default, `dr.who=;` is defined, so the fake user dr.who will not have any groups.

## Caching/Negative caching

Since the group mapping resolution relies on external mechanisms, the NameNode performance may be impacted. To reduce the impact due to repeated lookups, Hadoop caches the groups returned by the service provider. The cache invalidate is configurable via `hadoop.security.groups.cache.secs`, and the default is 300 seconds.

With the default caching implementation, after `hadoop.security.groups.cache.secs` when the cache entry expires, the next thread to request group membership will query the group mapping service provider to lookup the current groups for the user. While this lookup is running, the thread that initiated it will block, while any other threads requesting groups for the same user will retrieve the previously cached values. If the refresh fails, the thread performing the refresh will throw an exception and the process will repeat for the next thread that requests a lookup for that value. If the lookup repeatedly fails, and the cache is not updated, after `hadoop.security.groups.cache.secs * 10` seconds the cached entry will be evicted and all threads will block until a successful reload is performed.

To avoid any threads blocking when the cached entry expires, set `hadoop.security.groups.cache.background.reload` to true. This enables a small thread pool of `hadoop.security.groups.cache.background.reload.threads` threads having 3 threads by default. With this setting, when the cache is queried for an expired entry, the expired result is returned immediately and a task is queued to refresh the cache in the background. If the background refresh fails a new refresh operation will be queued by the next request to the cache, until `hadoop.security.groups.cache.secs * 10` when the cached entry will be evicted and all threads will block for that user until a successful reload occurs.

To avoid spamming NameNode with unknown users, Hadoop employs negative caching so that if the result of the lookup is empty, return an empty group directly instead of performing more group mapping queries, The cache invalidation is configurable via `hadoop.security.groups.negative-cache.secs`. The default is 30 seconds, so if group mapping service providers returns no group for a user, no lookup will be performed for the same user within 30 seconds.

## LDAP Groups Mapping

This provider supports LDAP with simple password authentication using JNDI API. `hadoop.security.group.mapping.ldap.url` must be set. This refers to the URL of the LDAP server(s) for resolving user groups. It supports configuring multiple LDAP servers via a comma-separated list.

`hadoop.security.group.mapping.ldap.base` configures the search base for the LDAP connection. This is a distinguished name, and will typically be the root of the LDAP directory. Get groups for a given username first looks up the user and then looks up the groups for the user result. If the directory setup has different user and group search bases, use `hadoop.security.group.mapping.ldap.userbase` and `hadoop.security.group.mapping.ldap.groupbase` configs.

It is possible to set a maximum time limit when searching and awaiting a result. Set `hadoop.security.group.mapping.ldap.directory.search.timeout` to 0 if infinite wait period is desired. Default is 10,000 milliseconds (10 seconds). This is the limit for each ldap query. If `hadoop.security.group.mapping.ldap.search.group.hierarchy.levels` is set to a positive value, then the total latency will be bounded by max(Recur Depth in LDAP, `hadoop.security.group.mapping.ldap.search.group.hierarchy.levels` ) \* `hadoop.security.group.mapping.ldap.directory.search.timeout`.

`hadoop.security.group.mapping.ldap.base` configures how far to walk up the groups hierarchy when resolving groups. By default, with a limit of 0, in order to be considered a member of a group, the user must be an explicit member in LDAP. Otherwise, it will traverse the group hierarchy `hadoop.security.group.mapping.ldap.search.group.hierarchy.levels` levels up.

It is possible to have custom group search filters with different arguments using the configuration `hadoop.security.group.mapping.ldap.group.search.filter.pattern`, we can configure comma separated values here and the values configured will be fetched from the LDAP attributes and will be replaced in the group search filter in the order they appear here, say if the first entry here is uid, so uid will be fetched from the attributes and the value fetched will be used in place of {0} in the group search filter, similarly the second value configured will replace {1} and so on.

Note: If `hadoop.security.group.mapping.ldap.group.search.filter.pattern` is configured, the group search will always be done assuming this group search filter pattern irrespective of any other parameters.

### Bind user(s)

If the LDAP server does not support anonymous binds, set the distinguished name of the user to bind in `hadoop.security.group.mapping.ldap.bind.user`. The path to the file containing the bind user’s password is specified in `hadoop.security.group.mapping.ldap.bind.password.file`. This file should be readable only by the Unix user running the daemons.

## Multiple bind users

If multiple bind users are required, they can be specified through `hadoop.security.group.mapping.ldap.bind.users`. These will represent the aliases of users to be used to bind as when connecting to the LDAP. Each alias will then have to have its distinguished name and password configured. This is useful if the bind user’s password has to be reset. If AuthenticationException is encountered when connecting to LDAP, LDAPGroupsMapping will switch to the next bind user information and cycle back if necessary.

For example, if: `hadoop.security.group.mapping.ldap.bind.users=alias1,alias2` , then the following configuration is valid: `hadoop.security.group.mapping.ldap.bind.users.alias1.bind.user=bindUser1` `hadoop.security.group.mapping.ldap.bind.users.alias1.bind.password.alias=bindPasswordAlias1` `hadoop.security.group.mapping.ldap.bind.users.alias2.bind.user=bindUser2` `hadoop.security.group.mapping.ldap.bind.users.alias2.bind.password.alias=bindPasswordAlias2`

### Active Directory

The default configuration supports LDAP group name resolution with an Active Directory server.

### POSIX Groups

If the LDAP server supports POSIX group semantics (RFC-2307), Hadoop can perform LDAP group resolution queries to the server by setting both `hadoop.security.group.mapping.ldap.search.filter.user` to `(&amp;(objectClass=posixAccount)(uid={0}))` and `hadoop.security.group.mapping.ldap.search.filter.group` to `(objectClass=posixGroup)`.

### SSL

To secure the connection, the implementation supports LDAP over SSL (LDAPS). SSL is enable by setting `hadoop.security.group.mapping.ldap.ssl` to `true`. In addition, specify the path to the keystore file for SSL connection in `hadoop.security.group.mapping.ldap.ssl.keystore` and keystore password in `hadoop.security.group.mapping.ldap.ssl.keystore.password`, at the same time, make sure `hadoop.security.credential.clear-text-fallback` is true. Alternatively, store the keystore password in a file, and point `hadoop.security.group.mapping.ldap.ssl.keystore.password.file` to that file. For security purposes, this file should be readable only by the Unix user running the daemons, and for preventing recursive dependency, this file should be a local file. The first approach aka using `hadoop.security.group.mapping.ldap.ssl.keystore.password` is highly discouraged because it exposes the password in the configuration file.

### Low latency group mapping resolution

Typically, Hadoop resolves a user’s group names by making two LDAP queries: the first query gets the user object, and the second query uses the user’s Distinguished Name to find the groups. For some LDAP servers, such as Active Directory, the user object returned in the first query also contains the DN of the user’s groups in its `memberOf` attribute, and the name of a group is its Relative Distinguished Name. Therefore, it is possible to infer the user’s groups from the first query without sending the second one, and it may reduce group name resolution latency incurred by the second query. If it fails to get group names, it will fall back to the typical two-query scenario and send the second query to get group names. To enable this feature, set `hadoop.security.group.mapping.ldap.search.attr.memberof` to `memberOf`, and Hadoop will resolve group names using this attribute in the user object.

If the LDAP server’s certificate is not signed by a well known certificate authority, specify the path to the truststore in `hadoop.security.group.mapping.ldap.ssl.truststore`. Similar to keystore, specify the truststore password file in `hadoop.security.group.mapping.ldap.ssl.truststore.password.file`.

### Configuring retries and multiple LDAP servers with failover

If there are issues encountered when retrieving information from LDAP servers, the request will be retried. To configure the number of retries, use the following configuration:

```
     <name>hadoop.security.group.mapping.ldap.num.attempts</name>
     <value>3</value>
     <description>
       This property is the number of attempts to be made for LDAP operations.
       If this limit is exceeded, LdapGroupsMapping will return an empty
       group list.
     </description>
    </property>
```

LDAP Groups Mapping also supports configuring multiple LDAP servers and failover if a particular instance is not available or is misbehaving. The following configuration shows configuring 3 LDAP servers. Additionally, 2 attempts will be made for each server before failing over to the next one, with 6 attempts overall before failing.

```
<property>
  <name>hadoop.security.group.mapping.ldap.url</name>
  <value>ldap://server1,ldap://server2,ldap://server3</value>
  <description>
    The URL of the LDAP server(s) to use for resolving user groups when using
    the LdapGroupsMapping user to group mapping. Supports configuring multiple
    LDAP servers via a comma-separated list.
  </description>
</property>

<property>
  <name>hadoop.security.group.mapping.ldap.num.attempts</name>
  <value>6</value>
  <description>
    This property is the number of attempts to be made for LDAP operations.
    If this limit is exceeded, LdapGroupsMapping will return an empty
    group list.
  </description>
</property>

<property>
  <name>hadoop.security.group.mapping.ldap.num.attempts.before.failover</name>
  <value>2</value>
  <description>
    This property is the number of attempts to be made for LDAP operations
    using a single LDAP instance. If multiple LDAP servers are configured
    and this number of failed operations is reached, we will switch to the
    next LDAP server. The configuration for the overall number of attempts
    will still be respected, failover will thus be performed only if this
    property is less than hadoop.security.group.mapping.ldap.num.attempts.
  </description>
</property>
```

## Composite Groups Mapping

`CompositeGroupsMapping` works by enumerating a list of service providers in `hadoop.security.group.mapping.providers`. It get groups from each of the providers in the list one after the other. If `hadoop.security.group.mapping.providers.combined` is `true`, merge the groups returned by all providers; otherwise, return the groups in the first successful provider. See the following section for a sample configuration.

### Multiple group mapping providers configuration sample

This sample illustrates a typical use case for `CompositeGroupsMapping` where Hadoop authentication uses MIT Kerberos which trusts an AD realm. In this case, service principals such as hdfs, mapred, hbase, hive, oozie and etc can be placed in MIT Kerberos, but end users are just from the trusted AD. For the service principals, `ShellBasedUnixGroupsMapping` provider can be used to query their groups for efficiency, and for end users, `LdapGroupsMapping` provider can be used. This avoids to add group entries in AD for service principals when only using `LdapGroupsMapping` provider. In case multiple ADs are involved and trusted by the MIT Kerberos, `LdapGroupsMapping` provider can be used multiple times with different AD specific configurations. This sample also shows how to do that. Here are the necessary configurations.

```
  <name>hadoop.security.group.mapping</name>
  <value>org.apache.hadoop.security.CompositeGroupsMapping</value>
  <description>
    Class for user to group mapping (get groups for a given user) for ACL, which
    makes use of other multiple providers to provide the service.
  </description>
</property>

<property>
  <name>hadoop.security.group.mapping.providers</name>
  <value>shell4services,ad4usersX,ad4usersY</value>
  <description>
    Comma separated of names of other providers to provide user to group mapping.
  </description>
</property>

<property>
  <name>hadoop.security.group.mapping.providers.combined</name>
  <value>true</value>
  <description>
    true or false to indicate whether groups from the providers are combined or not. The default value is true
    If true, then all the providers will be tried to get groups and all the groups are combined to return as
    the final results. Otherwise, providers are tried one by one in the configured list order, and if any
    groups are retrieved from any provider, then the groups will be returned without trying the left ones.
  </description>
</property>

<property>
  <name>hadoop.security.group.mapping.provider.shell4services</name>
  <value>org.apache.hadoop.security.ShellBasedUnixGroupsMapping</value>
  <description>
    Class for group mapping provider named by 'shell4services'. The name can then be referenced
    by hadoop.security.group.mapping.providers property.
  </description>
</property>

<property>
  <name>hadoop.security.group.mapping.provider.ad4usersX</name>
  <value>org.apache.hadoop.security.LdapGroupsMapping</value>
  <description>
    Class for group mapping provider named by 'ad4usersX'. The name can then be referenced
    by hadoop.security.group.mapping.providers property.
  </description>
</property>

<property>
  <name>hadoop.security.group.mapping.provider.ad4usersY</name>
  <value>org.apache.hadoop.security.LdapGroupsMapping</value>
  <description>
    Class for group mapping provider named by 'ad4usersY'. The name can then be referenced
    by hadoop.security.group.mapping.providers property.
  </description>
</property>

<property>
<name>hadoop.security.group.mapping.provider.ad4usersX.ldap.url</name>
<value>ldap://ad-host-for-users-X:389</value>
  <description>
    ldap url for the provider named by 'ad4usersX'. Note this property comes from
    'hadoop.security.group.mapping.ldap.url'.
  </description>
</property>

<property>
<name>hadoop.security.group.mapping.provider.ad4usersY.ldap.url</name>
<value>ldap://ad-host-for-users-Y:389</value>
  <description>
    ldap url for the provider named by 'ad4usersY'. Note this property comes from
    'hadoop.security.group.mapping.ldap.url'.
  </description>
</property>
```

You also need to configure other properties like hadoop.security.group.mapping.ldap.bind.password.file and etc. for ldap providers in the same way as above does.

---
## Hadoop Docker

### Running from existing setups

There are special branches for running hadoop in docker.

The `docker-hadoop-runner*` branches contain scripts that set up base images that can be used for running any Hadoop version.

* [docker-hadoop-runner-latest](https://github.com/apache/hadoop/tree/docker-hadoop-runner-latest)
* [docker-hadoop-runner-jdk11](https://github.com/apache/hadoop/tree/docker-hadoop-runner-jdk11)
* [docker-hadoop-runner-jdk8](https://github.com/apache/hadoop/tree/docker-hadoop-runner-jdk8)
* [docker-hadoop-runner](https://github.com/apache/hadoop/tree/docker-hadoop-runner)

The `docker-hadoop*` branches can be used for running a specific version.

* [docker-hadoop-3](https://github.com/apache/hadoop/tree/docker-hadoop-3)
* `hadoop-3.3.6`
* [docker-hadoop-2](https://github.com/apache/hadoop/tree/docker-hadoop-2)
* `hadoop-2.10.2`

### Running from the source code

There is a setup under `hadoop-dist` that contains Docker Compose definitions for running the current version of Hadoop in a multi-node docker environment.

This is meant for testing code changes locally and debugging.

The base image used by the Docker setup is built as part of the maven lifecycle. The distribution files generated while building the project with the `-Pdist` profile enabled, will be used for running hadoop inside the containers.

In order to start the docker environment you need to do the following \* Build the project, using the `-Pdist` profile

```
> mvn clean install -Dmaven.javadoc.skip=true -DskipTests -DskipShade -Pdist,src
```

* From the project root, navigate under the docker-compose dir under the generated dist directory

```
> cd hadoop-dist/target/hadoop-<current-version>/compose/hadoop
```

* Start the docker environment

```
> docker-compose up -d --scale datanode=3
```

* Connect to a container to execute commands

```
> docker exec -it hadoop_datanode_1 bash
bash-4.2$ hdfs dfs -mkdir /test
```

### Config files

To add or remove properties from the `core-site.xml`, `hdfs-site.xml`, etc. files used in the docker environment, simply edit the `config` file before starting the containers. The changes will be persisted in the docker environment.

---
# Testing the Filesystem Contract

* [Running the tests](#Running_the_tests)
  * [ftp://](#ftp:.2F.2F)
* [Testing a new filesystem](#Testing_a_new_filesystem)
  * [Handling test failures](#Handling_test_failures)
  * [‘Lax vs Strict’ exceptions](#a.E2.80.98Lax_vs_Strict.E2.80.99_exceptions)
  * [Supporting FileSystems with login and authentication parameters](#Supporting_FileSystems_with_login_and_authentication_parameters)
  * [Important: passing the tests does not guarantee compatibility](#Important:_passing_the_tests_does_not_guarantee_compatibility)
* [Adding a new test suite](#Adding_a_new_test_suite)
  * [Root manipulation tests](#Root_manipulation_tests)
  * [Scalability tests](#Scalability_tests)
* [Extending the specification](#Extending_the_specification)

## Running the tests

A normal Hadoop test run will test those FileSystems that can be tested locally via the local filesystem. This typically means `file://` and its underlying `LocalFileSystem`, and `hdfs://` via the HDFS MiniCluster.

Other filesystems are skipped unless there is a specific configuration to the remote server providing the filesystem.

These filesystem bindings must be defined in an XML configuration file, usually `hadoop-common-project/hadoop-common/src/test/resources/contract-test-options.xml`. This file is excluded and should not be checked in.

### <ftp://>

In `contract-test-options.xml`, the filesystem name must be defined in the property `fs.contract.test.fs.ftp`. The specific login options to connect to the FTP Server must then be provided.

A path to a test directory must also be provided in the option `fs.contract.test.ftp.testdir`. This is the directory under which operations take place.

Example:

```
<configuration>
  <property>
    <name>fs.contract.test.fs.ftp</name>
    <value>ftp://server1/</value>
  </property>

  <property>
    <name>fs.ftp.user.server1</name>
    <value>testuser</value>
  </property>

  <property>
    <name>fs.contract.test.ftp.testdir</name>
    <value>/home/testuser/test</value>
  </property>

  <property>
    <name>fs.ftp.password.server1</name>
    <value>secret-login</value>
  </property>
</configuration>
```

## Testing a new filesystem

The core of adding a new FileSystem to the contract tests is adding a new contract class, then creating a new non-abstract test class for every test suite that you wish to test.

1. Do not try and add these tests into Hadoop itself. They won’t be added to the source tree. The tests must live with your own filesystem source.
2. Create a package in your own test source tree (usually) under `contract`, for the files and tests.
3. Subclass `AbstractFSContract` for your own contract implementation.
4. For every test suite you plan to support create a non-abstract subclass, with the name starting with `Test` and the name of the filesystem. Example: `TestHDFSRenameContract`.
5. These non-abstract classes must implement the abstract method `createContract()`.
6. Identify and document any filesystem bindings that must be defined in a `src/test/resources/contract-test-options.xml` file of the specific project.
7. Run the tests until they work.

As an example, here is the implementation of the test of the `create()` tests for the local filesystem.

```
package org.apache.hadoop.fs.contract.localfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.contract.AbstractCreateContractTest;
import org.apache.hadoop.fs.contract.AbstractFSContract;

public class TestLocalCreateContract extends AbstractCreateContractTest {
  @Override
  protected AbstractFSContract createContract(Configuration conf) {
    return new LocalFSContract(conf);
  }
}
```

The standard implementation technique for subclasses of `AbstractFSContract` is to be driven entirely by a Hadoop XML configuration file stored in the test resource tree. The best practise is to store it under `/contract` with the name of the FileSystem, such as `contract/localfs.xml`. Having the XML file define all FileSystem options makes the listing of FileSystem behaviors immediately visible.

The `LocalFSContract` is a special case of this, as it must adjust its case sensitivity policy based on the OS on which it is running: for both Windows and OS/X, the filesystem is case insensitive, so the `ContractOptions.IS_CASE_SENSITIVE` option must be set to false. Furthermore, the Windows filesystem does not support Unix file and directory permissions, so the relevant flag must also be set. This is done *after* loading the XML contract file from the resource tree, simply by updating the now-loaded configuration options:

```
  getConf().setBoolean(getConfKey(ContractOptions.SUPPORTS_UNIX_PERMISSIONS), false);
```

### Handling test failures

If your new `FileSystem` test cases fails one of the contract tests, what you can you do?

It depends on the cause of the problem

1. Case: custom `FileSystem` subclass class doesn’t correctly implement specification. Fix.
2. Case: Underlying filesystem doesn’t behave in a way that matches Hadoop’s expectations. Ideally, fix. Or try to make your `FileSystem` subclass hide the differences, e.g. by translating exceptions.
3. Case: fundamental architectural differences between your filesystem and Hadoop. Example: different concurrency and consistency model. Recommendation: document and make clear that the filesystem is not compatible with HDFS.
4. Case: test does not match the specification. Fix: patch test, submit the patch to Hadoop.
5. Case: specification incorrect. The underlying specification is (with a few exceptions) HDFS. If the specification does not match HDFS, HDFS should normally be assumed to be the real definition of what a FileSystem should do. If there’s a mismatch, please raise it on the `hdfs-dev` mailing list. Note that while FileSystem tests live in the core Hadoop codebase, it is the HDFS team who owns the FileSystem specification and the tests that accompany it.

If a test needs to be skipped because a feature is not supported, look for a existing configuration option in the `ContractOptions` class. If there is no method, the short term fix is to override the method and use the `ContractTestUtils.skip()` message to log the fact that a test is skipped. Using this method prints the message to the logs, then tells the test runner that the test was skipped. This highlights the problem.

A recommended strategy is to call the superclass, catch the exception, and verify that the exception class and part of the error string matches that raised by the current implementation. It should also `fail()` if superclass actually succeeded -that is it failed the way that the implemention does not currently do. This will ensure that the test path is still executed, any other failure of the test -possibly a regression- is picked up. And, if the feature does become implemented, that the change is picked up.

A long-term solution is to enhance the base test to add a new optional feature key. This will require collaboration with the developers on the `hdfs-dev` mailing list.

### ‘Lax vs Strict’ exceptions

The contract tests include the notion of strict vs lax exceptions. *Strict* exception reporting means: reports failures using specific subclasses of `IOException`, such as `FileNotFoundException`, `EOFException` and so on. *Lax* reporting means throws `IOException`.

While FileSystems SHOULD raise stricter exceptions, there may be reasons why they cannot. Raising lax exceptions is still allowed, it merely hampers diagnostics of failures in user applications. To declare that a FileSystem does not support the stricter exceptions, set the option `fs.contract.supports-strict-exceptions` to false.

### Supporting FileSystems with login and authentication parameters

Tests against remote FileSystems will require the URL to the FileSystem to be specified; tests against remote FileSystems that require login details require usernames/IDs and passwords.

All these details MUST be required to be placed in the file `src/test/resources/contract-test-options.xml`, and your SCM tools configured to never commit this file to subversion, git or equivalent. Furthermore, the build MUST be configured to never bundle this file in any `-test` artifacts generated. The Hadoop build does this, excluding `src/test/**/*.xml` from the JAR files. In addition, `src/test/resources/auth-keys.xml` will need to be created. It can be a copy of `contract-test-options.xml`. The `AbstractFSContract` class automatically loads this resource file if present; specific keys for specific test cases can be added.

As an example, here are what S3A test keys look like:

```
<configuration>
  <property>
    <name>fs.contract.test.fs.s3a</name>
    <value>s3a://tests3contract</value>
  </property>

  <property>
    <name>fs.s3a.access.key</name>
    <value>DONOTPCOMMITTHISKEYTOSCM</value>
  </property>

  <property>
    <name>fs.s3a.secret.key</name>
    <value>DONOTEVERSHARETHISSECRETKEY!</value>
  </property>
</configuration>
```

The `AbstractBondedFSContract` automatically skips a test suite if the FileSystem URL is not defined in the property `fs.contract.test.fs.%s`, where `%s` matches the schema name of the FileSystem.

When running the tests `maven.test.skip` will need to be turned off since it is true by default on these tests. This can be done with a command like `mvn test -Ptests-on`.

### Important: passing the tests does not guarantee compatibility

Passing all the FileSystem contract tests does not mean that a filesystem can be described as “compatible with HDFS”. The tests try to look at the isolated functionality of each operation, and focus on the preconditions and postconditions of each action. Core areas not covered are concurrency and aspects of failure across a distributed system.

* Consistency: are all changes immediately visible?
* Atomicity: are operations which HDFS guarantees to be atomic equally so on the new filesystem.
* Idempotency: if the filesystem implements any retry policy, is idempotent even while other clients manipulate the filesystem?
* Scalability: does it support files as large as HDFS, or as many in a single directory?
* Durability: do files actually last -and how long for?

There are also some specific aspects of the use of the FileSystem API:

* Compatibility with the `hadoop -fs` CLI.
* Whether the blocksize policy produces file splits that are suitable for analytics workss. (as an example, a blocksize of 1 matches the specification, but as it tells MapReduce jobs to work a byte at a time, unusable).

Tests that verify these behaviors are of course welcome.

## Adding a new test suite

1. New tests should be split up with a test class per operation, as is done for `seek()`, `rename()`, `create()`, and so on. This is to match up the way that the FileSystem contract specification is split up by operation. It also makes it easier for FileSystem implementors to work on one test suite at a time.
2. Subclass `AbstractFSContractTestBase` with a new abstract test suite class. Again, use `Abstract` in the title.
3. Look at `org.apache.hadoop.fs.contract.ContractTestUtils` for utility classes to aid testing, with lots of filesystem-centric assertions. Use these to make assertions about the filesystem state, and to incude diagnostics information such as directory listings and dumps of mismatched files when an assertion actually fails.
4. Write tests for the local, raw local and HDFS filesystems -if one of these fails the tests then there is a sign of a problem -though be aware that they do have differnces
5. Test on the object stores once the core filesystems are passing the tests.
6. Try and log failures with as much detail as you can -the people debugging the failures will appreciate it.

### Root manipulation tests

Some tests work directly against the root filesystem, attempting to do things like rename “/” and similar actions. The root directory is “special”, and it’s important to test this, especially on non-POSIX filesystems such as object stores. These tests are potentially very destructive to native filesystems, so use care.

1. Add the tests under `AbstractRootDirectoryContractTest` or create a new test with (a) `Root` in the title and (b) a check in the setup method to skip the test if root tests are disabled:

   ```
     skipIfUnsupported(TEST_ROOT_TESTS_ENABLED);
   ```
2. Don’t provide an implementation of this test suite to run against the local FS.

### Scalability tests

Tests designed to generate scalable load -and that includes a large number of small files, as well as fewer larger files, should be designed to be configurable, so that users of the test suite can configure the number and size of files.

Be aware that on object stores, the directory rename operation is usually `O(files)*O(data)` while the delete operation is `O(files)`. The latter means even any directory cleanup operations may take time and can potentially timeout. It is important to design tests that work against remote filesystems with possible delays in all operations.

## Extending the specification

The specification is incomplete. It doesn’t have complete coverage of the FileSystem classes, and there may be bits of the existing specified classes that are not covered.

1. Look at the implementations of a class/interface/method to see what they do, especially HDFS and local. These are the documentation of what is done today.
2. Look at the POSIX API specification.
3. Search through the HDFS JIRAs for discussions on FileSystem topics, and try to understand what was meant to happen, as well as what does happen.
4. Use an IDE to find out how methods are used in Hadoop, HBase and other parts of the stack. Although this assumes that these are representative Hadoop applications, it will at least show how applications *expect* a FileSystem to behave.
5. Look in the java.io source to see how the bunded FileSystem classes are expected to behave -and read their javadocs carefully.
6. If something is unclear -as on the hdfs-dev list.
7. Don’t be afraid to write tests to act as experiments and clarify what actually happens. Use the HDFS behaviours as the normative guide.

---
# Notation

* * [Mathematics Symbols in this document](#Mathematics_Symbols_in_this_document)
    * [Sets, Lists, Maps, and Strings](#Sets.2C__Lists.2C_Maps.2C_and_Strings)
    * [State Immutability](#State_Immutability)
    * [Function Specifications](#Function_Specifications)
  * [Exceptions](#Exceptions)
  * [Conditions](#Conditions)
    * [supported(instance, method)](#supported.28instance.2C_method.29)

A formal notation such as [The Z Notation](http://www.open-std.org/jtc1/sc22/open/n3187.pdf) would be the strictest way to define Hadoop FileSystem behavior, and could even be used to prove some axioms.

However, it has a number of practical flaws:

1. Such notations are not as widely used as they should be, so the broader software development community is not going to have practical experience of it.
2. It’s very hard to work with without dropping into tools such as LaTeX *and* add-on libraries.
3. Such notations are difficult to understand, even for experts.

Given that the target audience of this specification is FileSystem developers, formal notations are not appropriate. Instead, broad comprehensibility, ease of maintenance, and ease of deriving tests take priority over mathematically-pure formal notation.

### Mathematics Symbols in this document

This document does use a subset of [the notation in the Z syntax](http://staff.washington.edu/jon/z/glossary.html), but in an ASCII form and the use of Python list notation for manipulating lists and sets.

* `iff` : `iff` If and only if
* `⇒` : `implies`
* `→` : `-->` total function
* `↛` : `->` partial function
* `∩` : `^`: Set Intersection
* `∪` : `+`: Set Union
* `\` : `-`: Set Difference
* `∃` : `exists` Exists predicate
* `∀` : `forall`: For all predicate
* `=` : `==` Equals operator
* `≠` : `!=` operator. In Java `z ≠ y` is written as `!( z.equals(y))` for all non-simple datatypes
* `≡` : `equivalent-to` equivalence operator. This is stricter than equals.
* `∅` : `{}` Empty Set. `∅ ≡ {}`
* `≈` : `approximately-equal-to` operator
* `¬` : `not` Not operator. In Java, `!`
* `∄` : `does-not-exist`: Does not exist predicate. Equivalent to `not exists`
* `∧` : `and` : local and operator. In Java , `&&`
* `∨` : `or` : local and operator. In Java, `||`
* `∈` : `in` : element of
* `∉` : `not in` : not an element of
* `⊆` : `subset-or-equal-to` the subset or equality condition
* `⊂` : `subset-of` the proper subset condition
* `| p |` : `len(p)` the size of a variable
* `:=` : `=` :
* `` : `#` : Python-style comments
* `happens-before` : `happens-before` : Lamport’s ordering relationship as defined in [Time, Clocks and the Ordering of Events in a Distributed System](http://research.microsoft.com/en-us/um/people/lamport/pubs/time-clocks.pdf)

#### Sets, Lists, Maps, and Strings

The [python data structures](http://docs.python.org/2/tutorial/datastructures.html) are used as the basis for this syntax as it is both plain ASCII and well-known.

##### Lists

* A list *L* is an ordered sequence of elements `[e1, e2, ... e(n)]`
* The size of a list `len(L)` is the number of elements in a list.
* Items can be addressed by a 0-based index `e1 == L[0]`
* Python slicing operators can address subsets of a list `L[0:3] == [e1,e2,e3]`, `L[:-1] == [e1, ... e(n-1)]`
* Lists can be concatenated `L' = L + [ e3 ]`
* Lists can have entries removed `L' = L - [ e2, e1 ]`. This is different from Python’s `del` operation, which operates on the list in place.
* The membership predicate `in` returns true iff an element is a member of a List: `e2 in L`
* List comprehensions can create new lists: `L' = [ x for x in L where x < 5]`
* for a list `L`, `len(L)` returns the number of elements.

##### Sets

Sets are an extension of the List notation, adding the restrictions that there can be no duplicate entries in the set, and there is no defined order.

* A set is an unordered collection of items surrounded by `{` and `}` braces.
* When declaring one, the python constructor `{}` is used. This is different from Python, which uses the function `set([list])`. Here the assumption is that the difference between a set and a dictionary can be determined from the contents.
* The empty set `{}` has no elements.
* All the usual set concepts apply.
* The membership predicate is `in`.
* Set comprehension uses the Python list comprehension. `S' = {s for s in S where len(s)==2}`
* for a set *s*, `len(s)` returns the number of elements.
* The `-` operator returns a new set excluding all items listed in the righthand set of the operator.

##### Maps

Maps resemble Python dictionaries; {“key”:value, “key2”,value2}

* `keys(Map)` represents the set of keys in a map.
* `k in Map` holds iff `k in keys(Map)`
* The empty map is written `{:}`
* The `-` operator returns a new map which excludes the entry with the key specified.
* `len(Map)` returns the number of entries in the map.

##### Strings

Strings are lists of characters represented in double quotes. e.g. `"abc"`

```
"abc" == ['a','b','c']
```

#### State Immutability

All system state declarations are immutable.

The suffix “’” (single quote) is used as the convention to indicate the state of the system after a mutating operation:

```
L' = L + ['d','e']
```

#### Function Specifications

A function is defined as a set of preconditions and a set of postconditions, where the postconditions define the new state of the system and the return value from the function.

### Exceptions

In classic specification languages, the preconditions define the predicates that MUST be satisfied else some failure condition is raised.

For Hadoop, we need to be able to specify what failure condition results if a specification is not met (usually what exception is to be raised).

The notation `raise <exception-name>` is used to indicate that an exception is to be raised.

It can be used in the if-then-else sequence to define an action if a precondition is not met.

Example:

```
if not exists(FS, Path) : raise IOException
```

If implementations may raise any one of a set of exceptions, this is denoted by providing a set of exceptions:

```
if not exists(FS, Path) : raise {FileNotFoundException, IOException}
```

If a set of exceptions is provided, the earlier elements of the set are preferred to the later entries, on the basis that they aid diagnosis of problems.

We also need to distinguish predicates that MUST be satisfied, along with those that SHOULD be met. For this reason a function specification MAY include a section in the preconditions marked ‘Should:’ All predicates declared in this section SHOULD be met, and if there is an entry in that section which specifies a stricter outcome, it SHOULD BE preferred. Here is an example of a should-precondition:

Should:

```
if not exists(FS, Path) : raise FileNotFoundException
```

### Conditions

There are further conditions used in precondition and postcondition declarations.

#### `supported(instance, method)`

This condition declares that a subclass implements the named method -some subclasses of the verious FileSystem classes do not, and instead raise `UnsupportedOperation`

As an example, one precondition of `FSDataInputStream.seek` is that the implementation must support `Seekable.seek` :

```
supported(FDIS, Seekable.seek) else raise UnsupportedOperation
```

---
# interface `BulkDelete`

* [Key Features](#Key_Features)
  * [Interface org.apache.hadoop.fs.BulkDeleteSource](#Interface_org.apache.hadoop.fs.BulkDeleteSource)
  * [Interface org.apache.hadoop.fs.BulkDelete](#Interface_org.apache.hadoop.fs.BulkDelete)
  * [bulkDelete(paths)](#bulkDelete.28paths.29)
  * [Availability](#Availability)
  * [Invocation through Reflection.](#Invocation_through_Reflection.)
  * [Implementations](#Implementations)

The `BulkDelete` interface provides an API to perform bulk delete of files/objects in an object store or filesystem.

## Key Features

* An API for submitting a list of paths to delete.
* This list must be no larger than the “page size” supported by the client; This size is also exposed as a method.
* This list must not have any path outside the base path.
* Triggers a request to delete files at the specific paths.
* Returns a list of which paths were reported as delete failures by the store.
* Does not consider a nonexistent file to be a failure.
* Does not offer any atomicity guarantees.
* Idempotency guarantees are weak: retries may delete files newly created by other clients.
* Provides no guarantees as to the outcome if a path references a directory.
* Provides no guarantees that parent directories will exist after the call.

The API is designed to match the semantics of the AWS S3 [Bulk Delete](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) REST API call, but it is not exclusively restricted to this store. This is why the “provides no guarantees” restrictions do not state what the outcome will be when executed on other stores.

### Interface `org.apache.hadoop.fs.BulkDeleteSource`

The interface `BulkDeleteSource` is offered by a FileSystem/FileContext class if it supports the API. The default implementation is implemented in base FileSystem class that returns an instance of `org.apache.hadoop.fs.impl.DefaultBulkDeleteOperation`. The default implementation details are provided in below sections.

```
@InterfaceAudience.Public
@InterfaceStability.Unstable
public interface BulkDeleteSource {
  BulkDelete createBulkDelete(Path path)
      throws UnsupportedOperationException, IllegalArgumentException, IOException;

}
```

### Interface `org.apache.hadoop.fs.BulkDelete`

This is the bulk delete implementation returned by the `createBulkDelete()` call.

```
@InterfaceAudience.Public
@InterfaceStability.Unstable
public interface BulkDelete extends IOStatisticsSource, Closeable {
  int pageSize();
  Path basePath();
  List<Map.Entry<Path, String>> bulkDelete(List<Path> paths)
      throws IOException, IllegalArgumentException;

}
```

### `bulkDelete(paths)`

#### Preconditions

```
if length(paths) > pageSize: throw IllegalArgumentException
```

#### Postconditions

All paths which refer to files are removed from the set of files.

```
FS'Files = FS.Files - [paths]
```

No other restrictions are placed upon the outcome.

### Availability

The `BulkDeleteSource` interface is exported by `FileSystem` and `FileContext` storage clients which is available for all FS via `org.apache.hadoop.fs.impl.DefaultBulkDeleteSource`. For integration in applications like Apache Iceberg to work seamlessly, all implementations of this interface MUST NOT reject the request but instead return a BulkDelete instance of size >= 1.

Use the `PathCapabilities` probe `fs.capability.bulk.delete`.

```
store.hasPathCapability(path, "fs.capability.bulk.delete")
```

### Invocation through Reflection.

The need for many libraries to compile against very old versions of Hadoop means that most of the cloud-first Filesystem API calls cannot be used except through reflection -And the more complicated The API and its data types are, The harder that reflection is to implement.

To assist this, the class `org.apache.hadoop.io.wrappedio.WrappedIO` has few methods which are intended to provide simple access to the API, especially through reflection.

```
  public static int bulkDeletePageSize(FileSystem fs, Path path) throws IOException;

  public static int bulkDeletePageSize(FileSystem fs, Path path) throws IOException;

  public static List<Map.Entry<Path, String>> bulkDelete(FileSystem fs, Path base, Collection<Path> paths);
```

### Implementations

#### Default Implementation

The default implementation which will be used by all implementation of `FileSystem` of the `BulkDelete` interface is `org.apache.hadoop.fs.impl.DefaultBulkDeleteOperation` which fixes the page size to be 1 and calls `FileSystem.delete(path, false)` on the single path in the list.

#### S3A Implementation

The S3A implementation is `org.apache.hadoop.fs.s3a.impl.BulkDeleteOperation` which implements the multi object delete semantics of the AWS S3 API [Bulk Delete](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) For more details please refer to the S3A Performance documentation.

---
# interface `org.apache.hadoop.fs.Abortable`

* [Method abort()](#Method_abort.28.29)
* [Method abort() on an output stream](#Method_abort.28.29_on_an_output_stream)
* [Preconditions](#Preconditions)
* [Postconditions](#Postconditions)
  * [Cleanup](#Cleanup)
  * [Thread safety and atomicity](#Thread_safety_and_atomicity)
* [Path/Stream capability “fs.capability.outputstream.abortable”](#Path.2FStream_capability_.E2.80.9Cfs.capability.outputstream.abortable.E2.80.9D)

Abort the active operation such that the output does not become manifest.

Specifically, if supported on an [output stream](outputstream.html), a successful `abort()` MUST guarantee that the stream will not be made visible in the `close()` operation.

```
@InterfaceAudience.Public
@InterfaceStability.Unstable
public interface Abortable {

  /**
   * Abort the active operation without the output becoming visible.
   *
   * This is to provide ability to cancel the write on stream; once
   * a stream is aborted, the write MUST NOT become visible.
   *
   * @throws UnsupportedOperationException if the operation is not supported.
   * @return the result.
   */
  AbortableResult abort();

  /**
   * Interface for the result of aborts; allows subclasses to extend
   * (IOStatistics etc) or for future enhancements if ever needed.
   */
  interface AbortableResult {

    /**
     * Was the stream already closed/aborted?
     * @return true if a close/abort operation had already
     * taken place.
     */
    boolean alreadyClosed();

    /**
     * Any exception caught during cleanup operations,
     * exceptions whose raising/catching does not change
     * the semantics of the abort.
     * @return an exception or null.
     */
    IOException anyCleanupException();
  }
}
```

## Method `abort()`

Aborts the ongoing operation such that no output SHALL become visible when the operation is completed.

Unless and until other File System classes implement `Abortable`, the interface is specified purely for output streams.

## Method `abort()` on an output stream

`Abortable.abort()` MUST only be supported on output streams whose output is only made visible when `close()` is called, for example. output streams returned by the S3A FileSystem.

## Preconditions

The stream MUST implement `Abortable` and `StreamCapabilities`.

```
if unsupported:
  throw UnsupportedException

if not isOpen(stream):
  no-op

StreamCapabilities.hasCapability("fs.capability.outputstream.abortable") == True
```

## Postconditions

After `abort()` returns, the filesystem MUST be unchanged:

```
FS' = FS
```

A successful `abort()` operation MUST guarantee that when the stream`close()` is invoked no output shall be manifest.

* The stream MUST retry any remote calls needed to force the abort outcome.
* If any file was present at the destination path, it MUST remain unchanged.

Strictly then:

> if `Abortable.abort()` does not raise `UnsupportedOperationException` then returns, then it guarantees that the write SHALL NOT become visible and that any existing data in the filesystem at the destination path SHALL continue to be available.

1. Calls to `write()` methods MUST fail.
2. Calls to `flush()` MUST be no-ops (applications sometimes call this on closed streams)
3. Subsequent calls to `abort()` MUST be no-ops.
4. `close()` MUST NOT manifest the file, and MUST NOT raise an exception

That is, the postconditions of `close()` becomes:

```
FS' = FS
```

### Cleanup

* If temporary data is stored in the local filesystem or in the store’s upload infrastructure then this MAY be cleaned up; best-effort is expected here.
* The stream SHOULD NOT retry cleanup operations; any failure there MUST be caught and added to `AbortResult`

#### Returned `AbortResult`

The `AbortResult` value returned is primarily for testing and logging.

`alreadyClosed()`: MUST return `true` if the write had already been aborted or closed;

`anyCleanupException();`: SHOULD return any IOException raised during any optional cleanup operations.

### Thread safety and atomicity

Output streams themselves aren’t formally required to be thread safe, but as applications do sometimes assume they are, this call MUST be thread safe.

## Path/Stream capability “fs.capability.outputstream.abortable”

An application MUST be able to verify that a stream supports the `Abortable.abort()` operation without actually calling it. This is done through the `StreamCapabilities` interface.

1. If a stream instance supports `Abortable` then it MUST return `true` in the probe `hasCapability("fs.capability.outputstream.abortable")`
2. If a stream instance does not support `Abortable` then it MUST return `false` in the probe `hasCapability("fs.capability.outputstream.abortable")`

That is: if a stream declares its support for the feature, a call to `abort()` SHALL meet the defined semantics of the operation.

FileSystem/FileContext implementations SHOULD declare support similarly, to allow for applications to probe for the feature in the destination directory/path.

If a filesystem supports `Abortable` under a path `P` then it SHOULD return `true` to `PathCababilities.hasPathCapability(path, "fs.capability.outputstream.abortable")` This is to allow applications to verify that the store supports the feature.

If a filesystem does not support `Abortable` under a path `P` then it MUST return `false` to `PathCababilities.hasPathCapability(path, "fs.capability.outputstream.abortable")`

---
# interface `org.apache.hadoop.fs.MultipartUploader`

* [Invariants](#Invariants)
* [Concurrency](#Concurrency)
* [Model](#Model)
* [Asynchronous API](#Asynchronous_API)
  * [close()](#close.28.29)
* [State Changing Operations](#State_Changing_Operations)
  * [CompletableFuture<UploadHandle> startUpload(Path)](#CompletableFuture.3CUploadHandle.3E_startUpload.28Path.29)
  * [CompletableFuture<PartHandle> putPart(UploadHandle uploadHandle, int partNumber, Path filePath, InputStream inputStream, long lengthInBytes)](#CompletableFuture.3CPartHandle.3E_putPart.28UploadHandle_uploadHandle.2C_int_partNumber.2C_Path_filePath.2C_InputStream_inputStream.2C_long_lengthInBytes.29)
  * [CompletableFuture<PathHandle> complete(UploadHandle uploadId, Path filePath, Map<Integer, PartHandle> handles)](#CompletableFuture.3CPathHandle.3E_complete.28UploadHandle_uploadId.2C_Path_filePath.2C_Map.3CInteger.2C_PartHandle.3E_handles.29)
  * [CompletableFuture<Void> abort(UploadHandle uploadId, Path filePath)](#CompletableFuture.3CVoid.3E_abort.28UploadHandle_uploadId.2C_Path_filePath.29)
  * [CompletableFuture<Integer> abortUploadsUnderPath(Path path)](#CompletableFuture.3CInteger.3E_abortUploadsUnderPath.28Path_path.29)

The `MultipartUploader` can upload a file using multiple parts to Hadoop-supported filesystems. The benefits of a multipart upload is that the file can be uploaded from multiple clients or processes in parallel and the results will not be visible to other clients until the `complete` function is called.

When implemented by an object store, uploaded data may incur storage charges, even before it is visible in the filesystems. Users of this API must be diligent and always perform best-effort attempts to complete or abort the upload. The `abortUploadsUnderPath(path)` operation can help here.

## Invariants

All the requirements of a valid `MultipartUploader` are considered implicit econditions and postconditions:

The operations of a single multipart upload may take place across different instance of a multipart uploader, across different processes and hosts. It is therefore a requirement that:

1. All state needed to upload a part, complete an upload or abort an upload must be contained within or retrievable from an upload handle.
2. That handle MUST be serializable; it MUST be deserializable to different processes executing the exact same version of Hadoop.
3. different hosts/processes MAY upload different parts, sequentially or simultaneously. The order in which they are uploaded to the filesystem MUST NOT constrain the order in which the data is stored in the final file.
4. An upload MAY be completed on a different instance than any which uploaded parts.
5. The output of an upload MUST NOT be visible at the final destination until the upload may complete.
6. It is not an error if a single multipart uploader instance initiates or completes multiple uploads files to the same destination sequentially, irrespective of whether or not the store supports concurrent uploads.

## Concurrency

Multiple processes may upload parts of a multipart upload simultaneously.

If a call is made to `startUpload(path)` to a destination where an active upload is in progress, implementations MUST perform one of the two operations.

* Reject the call as a duplicate.
* Permit both to proceed, with the final output of the file being that of *exactly one of the two uploads*.

Which upload succeeds is undefined. Users must not expect consistent behavior across filesystems, across filesystem instances \*or even across different requests.

If a multipart upload is completed or aborted while a part upload is in progress, the in-progress upload, if it has not completed, must not be included in the final file, in whole or in part. Implementations SHOULD raise an error in the `putPart()` operation.

# Serialization Compatibility

Users MUST NOT expect that serialized PathHandle versions are compatible across \* different multipart uploader implementations. \* different versions of the same implementation.

That is: all clients MUST use the exact same version of Hadoop.

## Model

A FileSystem/FileContext which supports Multipart Uploads extends the existing model `(Directories, Files, Symlinks)` to one of `(Directories, Files, Symlinks, Uploads)` `Uploads` of type `Map[UploadHandle -> Map[PartHandle -> UploadPart]`.

The `Uploads` element of the state tuple is a map of all active uploads.

```
Uploads: Map[UploadHandle -> Map[PartHandle -> UploadPart]`
```

An UploadHandle is a non-empty list of bytes.

```
UploadHandle: List[byte]
len(UploadHandle) > 0
```

Clients *MUST* treat this as opaque. What is core to this features design is that the handle is valid from across clients: the handle may be serialized on host `hostA`, deserialized on `hostB` and still used to extend or complete the upload.

```
UploadPart = (Path: path, parts: Map[PartHandle -> byte[]])
```

Similarly, the `PartHandle` type is also a non-empty list of opaque bytes, again, marshallable between hosts.

```
PartHandle: List[byte]
```

It is implicit that each `UploadHandle` in `FS.Uploads` is unique. Similarly, each `PartHandle` in the map of `[PartHandle -> UploadPart]` must also be unique.

1. There is no requirement that Part Handles are unique across uploads.
2. There is no requirement that Upload Handles are unique over time. However, if Part Handles are rapidly recycled, there is a risk that the nominally idempotent operation `abort(FS, uploadHandle)` could unintentionally cancel a successor operation which used the same Upload Handle.

## Asynchronous API

All operations return `CompletableFuture<>` types which must be subsequently evaluated to get their return values.

1. The execution of the operation MAY be a blocking operation in on the call thread.
2. If not, it SHALL be executed in a separate thread and MUST complete by the time the future evaluation returns.
3. Some/All preconditions MAY be evaluated at the time of initial invocation,
4. All those which are not evaluated at that time, MUST Be evaluated during the execution of the future.

What this means is that when an implementation interacts with a fast file system/store all preconditions including the existence of files MAY be evaluated early, whereas and implementation interacting with a remote object store whose probes are slow MAY verify preconditions in the asynchronous phase -especially those which interact with the remote store.

Java CompletableFutures do not work well with checked exceptions. The Hadoop codease is still evolving the details of the exception handling here, as more use is made of the asynchronous APIs. Assume that any precondition failure which declares that an `IOException` MUST be raised may have that operation wrapped in a `RuntimeException` of some form if evaluated in the future; this also holds for any other `IOException` raised during the operations.

### `close()`

Applications MUST call `close()` after using an uploader; this is so it may release other objects, update statistics, etc.

## State Changing Operations

### `CompletableFuture<UploadHandle> startUpload(Path)`

Starts a Multipart Upload, ultimately returning an `UploadHandle` for use in subsequent operations.

#### Preconditions

```
if path == "/" : raise IOException

if exists(FS, path) and not isFile(FS, path) raise PathIsDirectoryException, IOException
```

If a filesystem does not support concurrent uploads to a destination, then the following precondition is added:

```
if path in values(FS.Uploads) raise PathExistsException, IOException
```

#### Postconditions

Once the initialization operation completes, the filesystem state is updated with a new active upload, with a new handle, this handle being returned to the caller.

```
handle' = UploadHandle where not handle' in keys(FS.Uploads)
FS' = FS where FS'.Uploads(handle') == {}
result = handle'
```

### `CompletableFuture<PartHandle> putPart(UploadHandle uploadHandle, int partNumber, Path filePath, InputStream inputStream, long lengthInBytes)`

Upload a part for the specific multipart upload, eventually being returned an opaque part handle represting this part of the specified upload.

#### Preconditions

```
uploadHandle in keys(FS.Uploads)
partNumber >= 1
lengthInBytes >= 0
len(inputStream) >= lengthInBytes
```

#### Postconditions

```
data' = inputStream(0..lengthInBytes)
partHandle' = byte[] where not partHandle' in keys(FS.uploads(uploadHandle).parts)
FS' = FS where FS'.uploads(uploadHandle).parts(partHandle') == data'
result = partHandle'
```

The data is stored in the filesystem, pending completion. It MUST NOT be visible at the destination path. It MAY be visible in a temporary path somewhere in the file system; This is implementation-specific and MUST NOT be relied upon.

### `CompletableFuture<PathHandle> complete(UploadHandle uploadId, Path filePath, Map<Integer, PartHandle> handles)`

Complete the multipart upload.

A Filesystem may enforce a minimum size of each part, excluding the last part uploaded.

If a part is out of this range, an `IOException` MUST be raised.

#### Preconditions

```
uploadHandle in keys(FS.Uploads) else raise FileNotFoundException
FS.Uploads(uploadHandle).path == path
if exists(FS, path) and not isFile(FS, path) raise PathIsDirectoryException, IOException
parts.size() > 0
forall k in keys(parts): k > 0
forall k in keys(parts):
  not exists(k2 in keys(parts)) where (parts[k] == parts[k2])
```

All keys MUST be greater than zero, and there MUST not be any duplicate references to the same parthandle. These validations MAY be performed at any point during the operation. After a failure, there is no guarantee that a `complete()` call for this upload with a valid map of paths will complete. Callers SHOULD invoke `abort()` after any such failure to ensure cleanup.

if `putPart()` operations For this `uploadHandle` were performed But whose `PathHandle` Handles were not included in this request -the omitted parts SHALL NOT be a part of the resulting file.

The MultipartUploader MUST clean up any such outstanding entries.

In the case of backing stores that support directories (local filesystem, HDFS, etc), if, at the point of completion, there is now a directory at the destination then a `PathIsDirectoryException` or other `IOException` must be thrown.

#### Postconditions

```
UploadData' == ordered concatention of all data in the map of parts, ordered by key
exists(FS', path') and result = PathHandle(path')
FS' = FS where FS.Files(path) == UploadData' and not uploadHandle in keys(FS'.uploads)
```

The `PathHandle` is returned by the complete operation so subsequent operations will be able to identify that the data has not changed in the meantime.

The order of parts in the uploaded by file is that of the natural order of parts in the map: part 1 is ahead of part 2, etc.

### `CompletableFuture<Void> abort(UploadHandle uploadId, Path filePath)`

Abort a multipart upload. The handle becomes invalid and not subject to reuse.

#### Preconditions

```
uploadHandle in keys(FS.Uploads) else raise FileNotFoundException
```

#### Postconditions

The upload handle is no longer known.

```
FS' = FS where not uploadHandle in keys(FS'.uploads)
```

A subsequent call to `abort()` with the same handle will fail, unless the handle has been recycled.

### `CompletableFuture<Integer> abortUploadsUnderPath(Path path)`

Perform a best-effort cleanup of all uploads under a path.

returns a future which resolves to.

```
-1 if unsuppported
>= 0 if supported
```

Because it is best effort a strict postcondition isn’t possible. The ideal postcondition is all uploads under the path are aborted, and the count is the number of uploads aborted:

```
FS'.uploads forall upload in FS.uploads:
    not isDescendant(FS, path, upload.path)
return len(forall upload in FS.uploads:
               isDescendant(FS, path, upload.path))
```

---
# Statistic collection with the IOStatistics API

```
@InterfaceAudience.Public
@InterfaceStability.Unstable
```

The `IOStatistics` API is intended to provide statistics on individual IO classes -such as input and output streams, *in a standard way which applications can query*

Many filesystem-related classes have implemented statistics gathering and provided private/unstable ways to query this, but as they were not common across implementations it was unsafe for applications to reference these values. Example: `S3AInputStream` and its statistics API. This is used in internal tests, but cannot be used downstream in applications such as Apache Hive or Apache HBase.

The IOStatistics API is intended to

1. Be instance specific:, rather than shared across multiple instances of a class, or thread local.
2. Be public and stable enough to be used by applications.
3. Be easy to use in applications written in Java, Scala, and, via libhdfs, C/C++
4. Have foundational interfaces and classes in the `hadoop-common` JAR.

## Core Model

Any class *may* implement `IOStatisticsSource` in order to provide statistics.

Wrapper I/O Classes such as `FSDataInputStream` anc `FSDataOutputStream` *should* implement the interface and forward it to the wrapped class, if they also implement it -and return `null` if they do not.

`IOStatisticsSource` implementations `getIOStatistics()` return an instance of `IOStatistics` enumerating the statistics of that specific instance.

The `IOStatistics` Interface exports five kinds of statistic:

| Category | Type | Description |
| --- | --- | --- |
| `counter` | `long` | a counter which may increase in value; SHOULD BE >= 0 |
| `gauge` | `long` | an arbitrary value which can down as well as up; SHOULD BE >= 0 |
| `minimum` | `long` | an minimum value; MAY BE negative |
| `maximum` | `long` | a maximum value; MAY BE negative |
| `meanStatistic` | `MeanStatistic` | an arithmetic mean and sample size; mean MAY BE negative |

Four are simple `long` values, with the variations how they are likely to change and how they are aggregated.

#### Aggregation of Statistic Values

For the different statistic category, the result of `aggregate(x, y)` is

| Category | Aggregation |
| --- | --- |
| `counter` | `max(0, x) + max(0, y)` |
| `gauge` | `max(0, x) + max(0, y)` |
| `minimum` | `min(x, y)` |
| `maximum` | `max(x, y)` |
| `meanStatistic` | calculation of the mean of `x` and `y` ) |

#### Class `MeanStatistic`

## package `org.apache.hadoop.fs.statistics`

This package contains the public statistics APIs intended for use by applications.




`MeanStatistic` is a tuple of `(mean, samples)` to support aggregation.

A `MeanStatistic` with a sample of `0` is considered an empty statistic.

All `MeanStatistic` instances where `sample = 0` are considered equal, irrespective of the `mean` value.

Algorithm to calculate the mean :

```
if x.samples = 0:
    y
else if y.samples = 0 :
    x
else:
    samples' = x.samples + y.samples
    mean' = (x.mean * x.samples) + (y.mean * y.samples) / samples'
    (samples', mean')
```

Implicitly, this means that if both samples are empty, then the aggregate value is also empty.

```
public final class MeanStatistic implements Serializable, Cloneable {
  /**
   * Arithmetic mean.
   */
  private double mean;

  /**
   * Number of samples used to calculate
   * the mean.
   */
  private long samples;

  /**
   * Get the mean value.
   * @return the mean
   */
  public double getMean() {
    return mean;
  }

  /**
   * Get the sample count.
   * @return the sample count; 0 means empty
   */
  public long getSamples() {
    return samples;
  }

  /**
   * Is a statistic empty?
   * @return true if the sample count is 0
   */
  public boolean isEmpty() {
    return samples == 0;
  }
   /**
   * Add another mean statistic to create a new statistic.
   * When adding two statistics, if either is empty then
   * a copy of the non-empty statistic is returned.
   * If both are empty then a new empty statistic is returned.
   *
   * @param other other value
   * @return the aggregate mean
   */
  public MeanStatistic add(final MeanStatistic other) {
    /* Implementation elided. */
  }
  @Override
  public int hashCode() {
    return Objects.hash(mean, samples);
  }

  @Override
  public boolean equals(final Object o) {
    if (this == o) { return true; }
    if (o == null || getClass() != o.getClass()) { return false; }
    MeanStatistic that = (MeanStatistic) o;
    if (this.isEmpty()) {
      return that.isEmpty();
    }
    return Double.compare(that.mean, mean) == 0 &&
        samples == that.samples;
  }

  @Override
  public MeanStatistic clone() {
    return new MeanStatistic(this);
  }

  public MeanStatistic copy() {
    return new MeanStatistic(this);
  }

}
```




### class `org.apache.hadoop.fs.statistics.IOStatisticsSource`

```
/**
 * A source of IO statistics.
 * These statistics MUST be instance specific, not thread local.
 */
@InterfaceStability.Unstable
public interface IOStatisticsSource {

  /**
   * Return a statistics instance.
   * It is not a requirement that the same instance is returned every time.
   * {@link IOStatisticsSource}.
   * If the object implementing this is Closeable, this method
   * may return null if invoked on a closed object, even if
   * it returns a valid instance when called earlier.
   * @return an IOStatistics instance or null
   */
  IOStatistics getIOStatistics();
}
```

This is the interface which an object instance MUST implement if they are a source of IOStatistics information.

#### Invariants

The result of `getIOStatistics()` must be one of

* `null`
* an immutable `IOStatistics` for which each map of entries is an empty map.
* an instance of an `IOStatistics` whose statistics MUST BE unique to that instance of the class implementing `IOStatisticsSource`.

Less formally: if the statistics maps returned are non-empty, all the statistics must be collected from the current instance, and not from any other instances, the way some of the `FileSystem` statistics are collected.

The result of `getIOStatistics()`, if non-null, MAY be a different instance on every invocation.

### class `org.apache.hadoop.fs.statistics.IOStatistics`

These are per-instance statistics provided by an object which implements `IOStatisticsSource`.

```
@InterfaceAudience.Public
@InterfaceStability.Unstable
public interface IOStatistics {

  /**
   * Map of counters.
   * @return the current map of counters.
   */
  Map<String, Long> counters();

  /**
   * Map of gauges.
   * @return the current map of gauges.
   */
  Map<String, Long> gauges();

  /**
   * Map of minumums.
   * @return the current map of minumums.
   */
  Map<String, Long> minumums();

  /**
   * Map of maximums.
   * @return the current map of maximums.
   */
  Map<String, Long> maximums();

  /**
   * Map of meanStatistics.
   * @return the current map of MeanStatistic statistics.
   */
  Map<String, MeanStatistic> meanStatistics();

}
```

### Statistic Naming

The naming policy of statistics is designed to be readable, shareable and ideally consistent across `IOStatisticSource` implementations.

* Characters in key names MUST match the regular expression `[a-z|0-9|_]` with the exception of the first character, which MUST be in the range `[a-z]`. Thus the full regular expression for a valid statistic name is:

  ```
  [a-z][a-z|0-9|_]+
  ```
* Where possible, the names of statistics SHOULD be those defined with common names.

  ```
  org.apache.hadoop.fs.statistics.StreamStatisticNames
  org.apache.hadoop.fs.statistics.StoreStatisticNames
  ```

Note 1.: these are evolving; for clients to safely reference their statistics by name they SHOULD be copied to the application. (i.e. for an application compiled hadoop 3.4.2 to link against hadoop 3.4.1, copy the strings).

Note 2: keys defined in these classes SHALL NOT be removed from subsequent Hadoop releases.

* A common statistic name MUST NOT be used to report any other statistic and MUST use the pre-defined unit of measurement.
* A statistic name in one of the maps SHOULD NOT be re-used in another map. This aids diagnostics of logged statistics.

### Statistic Maps

For each map of statistics returned:

* The operations to add/remove entries are unsupported: the map returned MAY be mutable by the source of statistics.
* The map MAY be empty.
* The map keys each represent a measured statistic.
* The set of keys in a map SHOULD remain unchanged, and MUST NOT remove keys.
* The statistics SHOULD be dynamic: every lookup of an entry SHOULD return the latest value.
* The values MAY change across invocations of `Map.values()` and `Map.entries()`
* The update MAY be in the `iterable()` calls of the iterators returned, or MAY be in the actual `iterable.next()` operation. That is: there is no guarantee as to when the evaluation takes place.
* The returned `Map.Entry` instances MUST return the same value on repeated `getValue()` calls. (i.e once you have the entry, it is immutable).
* Queries of statistics SHOULD be fast and non-blocking to the extent that if invoked during a long operation, they will prioritize returning fast over most timely values.
* The statistics MAY lag; especially for statistics collected in separate operations (e.g stream IO statistics as provided by a filesystem instance).
* Statistics which represent time SHOULD use milliseconds as their unit.
* Statistics which represent time and use a different unit MUST document the unit used.

### Thread Model

1. An instance of `IOStatistics` can be shared across threads;
2. Read access to the supplied statistics maps MUST be thread safe.
3. Iterators returned from the maps MUST NOT be shared across threads.
4. The statistics collected MUST include all operations which took place across all threads performing work for the monitored object.
5. The statistics reported MUST NOT be local to the active thread.

This is different from the `FileSystem.Statistics` behavior where per-thread statistics are collected and reported.

That mechanism supports collecting limited read/write statistics for different worker threads sharing the same FS instance, but as the collection is thread local, it invariably under-reports IO performed in other threads on behalf of a worker thread.

## Statisic Snapshot

A snapshot of the current statistic values MAY be obtained by calling `IOStatisticsSupport.snapshotIOStatistics()`

```
  public static <X extends IOStatistics & Serializable> X
      snapshotIOStatistics(IOStatistics statistics)
```

This snapshot is serializable through Java serialization and through Jackson to/from JSON.

## Helper Classes

### class `org.apache.hadoop.fs.statistics.IOStatisticsSupport`

This provides helper methods to work with IOStatistics sources and instances.

Consult the javadocs for its operations.

### class `org.apache.hadoop.fs.statistics.IOStatisticsLogging`

Support for efficiently logging `IOStatistics`/`IOStatisticsSource` instances.

These are intended for assisting logging, including only enumerating the state of an `IOStatistics` instance when the log level needs it.

```
LOG.info("IOStatistics after upload: {}", demandStringify(iostats));

// or even better, as it results in only a single object creations
Object latest = demandStringify(iostats);
LOG.info("IOStatistics : {}", latest);
/* do some work. */
LOG.info("IOStatistics : {}", latest);
```

## Package `org.apache.hadoop.fs.statistics.impl`

This contains implementation classes to support providing statistics to applications.

These MUST NOT BE used by applications. If a feature is needed from this package then the provisioning of a public implementation MAY BE raised via the Hadoop development channels.

These MAY be used by those implementations of the Hadoop `FileSystem`, `AbstractFileSystem` and related classes which are not in the hadoop source tree. Implementors MUST BE aware that the implementation this code is unstable and may change across minor point releases of Hadoop.

---
# interface `PathCapabilities`

The `PathCapabilities` interface provides a way to programmatically query the operations offered under a given path by an instance of `FileSystem`, `FileContext` or other implementing class.

```
public interface PathCapabilities {
  boolean hasPathCapability(Path path, String capability)
      throws IOException;
}
```

There are a number of goals here:

1. Allow callers to probe for optional filesystem operations without actually having to invoke them.
2. Allow filesystems with their own optional per-instance features to declare whether or not they are active for the specific instance.
3. Allow for filesystem connectors which work with object stores to expose the fundamental difference in semantics of these stores (e.g: files not visible until closed, file rename being `O(data)`), directory rename being non-atomic, etc.

### Available Capabilities

Capabilities are defined as strings and split into “Common Capabilites” and non-standard ones for a specific store.

The common capabilities are all defined under the prefix `fs.capability.`

Consult the javadocs for `org.apache.hadoop.fs.CommonPathCapabilities` for these.

Individual filesystems MAY offer their own set of capabilities which can be probed for. These MUST begin with `fs.` + the filesystem scheme + `.capability`. For example `fs.s3a.capability.select.sql`;

### `boolean hasPathCapability(path, capability)`

Probe for the instance offering a specific capability under the given path.

#### Postconditions

```
if fs_supports_the_feature(path, capability):
  return True
else:
  return False
```

Return: `True`, iff the specific capability is available.

A filesystem instance *MUST NOT* return `True` for any capability unless it is known to be supported by that specific instance. As a result, if a caller probes for a capability then it can assume that the specific feature/semantics are available.

If the probe returns `False` then it can mean one of:

1. The capability is unknown.
2. The capability is known, and known to be unavailable on this instance.
3. The capability is known but this local class does not know if it is supported under the supplied path.

This predicate is intended to be low cost. If it requires remote calls other than path/link resolution, it SHOULD conclude that the availability of the feature is unknown and return `False`.

The predicate MUST also be side-effect free.

*Validity of paths* There is no requirement that the existence of the path must be checked; the parameter exists so that any filesystem which relays operations to other filesystems (e.g `viewfs`) can resolve and relay it to the nested filesystem. Consider the call to be *relatively* lightweight.

Because of this, it may be that while the filesystem declares that it supports a capability under a path, the actual invocation of the operation may fail for other reasons.

As an example, while a filesystem may support `append()` under a path, if invoked on a directory, the call may fail.

That is for a path `root = new Path("/")`: the capabilities call may succeed

```
fs.hasCapabilities(root, "fs.capability.append") == true
```

But a subsequent call to the operation on that specific path may fail, because the root path is a directory:

```
fs.append(root)
```

Similarly, there is no checking that the caller has the permission to perform a specific operation: just because a feature is available on that path does not mean that the caller can execute the operation.

The `hasCapabilities(path, capability)` probe is therefore declaring that the operation will not be rejected as unsupported, not that a specific invocation will be permitted on that path by the caller.

*Duration of availability*

As the state of a remote store changes,so may path capabilities. This may be due to changes in the local state of the filesystem (e.g. symbolic links or mount points changing), or changes in its functionality (e.g. a feature becoming availaible/unavailable due to operational changes, system upgrades, etc.)

*Capabilities which must be invoked to determine availablity*

Some operations may be known by the client connector, and believed to be available, but may actually fail when invoked due to the state and permissons of the remote store —state which is cannot be determined except by attempting side-effecting operations.

A key example of this is symbolic links and the local filesystem. The filesystem declares that it supports this unless symbolic links are explicitly disabled —when invoked they may actually fail.

### Implementors Notes

Implementors *MUST NOT* return `true` for any capability which is not guaranteed to be supported. To return `true` indicates that the implementation/deployment of the filesystem does, to the best of the knowledge of the filesystem client, offer the desired operations *and semantics* queried for.

For performance reasons, implementations *SHOULD NOT* check the path for existence, unless it needs to resolve symbolic links in parts of the path to determine whether a feature is present. This is required of `FileContext` and `viewfs`.

Individual filesystems *MUST NOT* unilaterally define new `fs.capability`-prefixed capabilities. Instead they *MUST* do one of the following:

* Define and stabilize new cross-filesystem capability flags (preferred), and so formally add a new `fs.capability` value.
* Use the scheme of the filesystem to as a prefix for their own options, e.g `fs.hdfs.`

---
# interface `LeaseRecoverable`

The `LeaseRecoverable` interface tells whether a given path of current filesystem can perform lease recovery for open file that a lease is not explicitly renewed or the client holding it goes away.

This interface should be implemented accordingly when necessary to any Filesystem that supports lease recovery, e.g. `DistributedFileSystem` (HDFS) and `ViewDistributedFileSystem`.

```
public interface LeaseRecoverable {
  boolean recoverLease(Path file) throws IOException;
  boolean isFileClosed(Path file) throws IOException;
}
```

There are two main functions of this interface, one performs lease recovery and another one verifies if a file has been closed.

### boolean recoverLease(Path file)

This function performs the lease recovery for the given file path, and it does not support directory path recovery. 1. Return `true`, if the file has already closed, or does not require lease recovery. 1. Return `false`, if the lease recovery is yet completed. 1. Throw `IOException` if a directory path is given as input.

### boolean isFileClosed(Path file)

This function only checks if the give file path has been closed, and it does not support directory verification. 1. Return `true`, if the file has been closed. 1. Return `false`, if the file is still open. 1. Throw `IOException` if a directory path is given as input.

### Path Capabilities SHOULD BE declared

If a filesystem supports `LeaseRecoverable`, it should return `true` to `PathCapabilities.hasPathCapability(path, "fs.capability.lease.recoverable")` for a given path.

---
# Extending the File System specification and its tests

* [How to update this specification](#How_to_update_this_specification)

The FileSystem specification is incomplete. It doesn’t cover all operations or even interfaces and classes in the FileSystem APIs. There may be some minor issues with those that it does cover, such as corner cases, failure modes, and other unexpected outcomes. It may also be that a standard FileSystem significantly diverges from the specification, and it is felt that this needs to be documented and coped with in tests.

Finally, the FileSystem classes and methods are not fixed forever. They may be extended with new operations on existing classes, as well as potentially entirely new classes and interfaces.

Accordingly, do not view this specification as a complete static document, any more than the rest of the Hadoop code.

1. View it as a live document to accompany the reference implementation (HDFS), and the tests used to validate filesystems.
2. Don’t be afraid to extend or correct it.
3. If you are proposing enhancements to the FileSystem APIs, you should extend the specification to match.

## How to update this specification

1. Although found in the `hadoop-common` codebase, the HDFS team has ownership of the FileSystem and FileContext APIs. Work with them on the hdfs-dev mailing list.
2. Create JIRA issues in the `HADOOP` project, component `fs`, to cover changes in the APIs and/or specification.
3. Code changes will of course require tests. Ideally, changes to the specification itself are accompanied by new tests.
4. If the change involves operations that already have an `Abstract*ContractTest`, add new test methods to the class and verify that they work on filesystem-specific tests that subclass it. That includes the object stores as well as the local and HDFS filesystems.
5. If the changes add a new operation, add a new abstract test class with the same contract-driven architecture as the existing one, and an implementation subclass for all filesystems that support the operation.
6. Add test methods to verify that invalid preconditions result in the expected failures.
7. Add test methods to verify that valid preconditions result in the expected final state of the filesystem. Testing as little as possible per test aids in tracking down problems.
8. If possible, add tests to show concurrency expectations.

If a FileSystem fails a newly added test, then it may be because:

* The specification is wrong.
* The test is wrong.
* The test is looking for the wrong exception (i.e. it is too strict).
* The specification and tests are correct -and it is the filesystem is not consistent with expectations.

HDFS has to be treated as correct in its behavior. If the test and specification do not match this behavior, then the specification needs to be updated. Even so, there may be cases where the FS could be changed:

1. The exception raised is a generic `IOException`, when a more informative subclass, such as `EOFException` can be raised.
2. The FileSystem does not fail correctly when passed an invalid set of arguments. This MAY be correctable, though must be done cautiously.

If the mismatch is in LocalFileSystem, then it probably can’t be corrected, as this is the native filesystem as accessed via the Java IO APIs.

For other FileSystems, their behaviour MAY be updated to more accurately reflect the behavior of HDFS and/or LocalFileSystem. For most operations this is straightforward, though the semantics of `rename()` are complicated enough that it is not clear that HDFS is the correct reference.

If a test fails and it is felt that it is a unfixable FileSystem-specific issue, then a new contract option to allow for different interpretations of the results should be added to the `ContractOptions` interface, the test modified to react to the presence/absence of the option, and the XML contract files for the standard FileSystems updated to indicate when a feature/failure mode is present.

---
# class `org.apache.hadoop.fs.FileSystem`

* [Invariants](#Invariants)
* [Feasible features](#Feasible_features)
  * [Protected directories](#Protected_directories)
* [Predicates and other state access operations](#Predicates_and_other_state_access_operations)
  * [boolean exists(Path p)](#boolean_exists.28Path_p.29)
  * [boolean isDirectory(Path p)](#boolean_isDirectory.28Path_p.29)
  * [boolean isFile(Path p)](#boolean_isFile.28Path_p.29)
  * [FileStatus getFileStatus(Path p)](#FileStatus_getFileStatus.28Path_p.29)
  * [msync()](#msync.28.29)
  * [Path getHomeDirectory()](#Path_getHomeDirectory.28.29)
  * [FileStatus[] listStatus(Path path, PathFilter filter)](#FileStatus.5B.5D_listStatus.28Path_path.2C_PathFilter_filter.29)
  * [FileStatus[] listStatus(Path path)](#FileStatus.5B.5D_listStatus.28Path_path.29)
  * [FileStatus[] listStatus(Path[] paths, PathFilter filter)](#FileStatus.5B.5D_listStatus.28Path.5B.5D_paths.2C_PathFilter_filter.29)
  * [RemoteIterator<FileStatus> listStatusIterator(Path p)](#RemoteIterator.3CFileStatus.3E_listStatusIterator.28Path_p.29)
  * [FileStatus[] listStatus(Path[] paths)](#FileStatus.5B.5D_listStatus.28Path.5B.5D_paths.29)
  * [RemoteIterator[LocatedFileStatus] listLocatedStatus(Path path, PathFilter filter)](#RemoteIterator.5BLocatedFileStatus.5D_listLocatedStatus.28Path_path.2C_PathFilter_filter.29)
  * [RemoteIterator[LocatedFileStatus] listLocatedStatus(Path path)](#RemoteIterator.5BLocatedFileStatus.5D_listLocatedStatus.28Path_path.29)
  * [RemoteIterator[LocatedFileStatus] listFiles(Path path, boolean recursive)](#RemoteIterator.5BLocatedFileStatus.5D_listFiles.28Path_path.2C_boolean_recursive.29)
  * [Postconditions](#Postconditions)
  * [ContentSummary getContentSummary(Path path)](#ContentSummary_getContentSummary.28Path_path.29)
  * [BlockLocation[] getFileBlockLocations(FileStatus f, int s, int l)](#BlockLocation.5B.5D_getFileBlockLocations.28FileStatus_f.2C_int_s.2C_int_l.29)
  * [BlockLocation[] getFileBlockLocations(Path P, int S, int L)](#BlockLocation.5B.5D_getFileBlockLocations.28Path_P.2C_int_S.2C_int_L.29)
  * [long getDefaultBlockSize()](#long_getDefaultBlockSize.28.29)
  * [long getDefaultBlockSize(Path p)](#long_getDefaultBlockSize.28Path_p.29)
  * [long getBlockSize(Path p)](#long_getBlockSize.28Path_p.29)
  * [Path getEnclosingRoot(Path p)](#Path_getEnclosingRoot.28Path_p.29)
* [State Changing Operations](#State_Changing_Operations)
  * [boolean mkdirs(Path p, FsPermission permission)](#boolean_mkdirs.28Path_p.2C_FsPermission_permission.29)
  * [FSDataOutputStream create(Path, ...)](#FSDataOutputStream_create.28Path.2C_....29)
  * [FSDataOutputStreamBuilder createFile(Path p)](#FSDataOutputStreamBuilder_createFile.28Path_p.29)
  * [FSDataOutputStream append(Path p, int bufferSize, Progressable progress)](#FSDataOutputStream_append.28Path_p.2C_int_bufferSize.2C_Progressable_progress.29)
  * [FSDataOutputStreamBuilder appendFile(Path p)](#FSDataOutputStreamBuilder_appendFile.28Path_p.29)
  * [FSDataInputStream open(Path f, int bufferSize)](#FSDataInputStream_open.28Path_f.2C_int_bufferSize.29)
  * [FSDataInputStreamBuilder openFile(Path path)](#FSDataInputStreamBuilder_openFile.28Path_path.29)
  * [FSDataInputStreamBuilder openFile(PathHandle)](#FSDataInputStreamBuilder_openFile.28PathHandle.29)
  * [PathHandle getPathHandle(FileStatus stat, HandleOpt... options)](#PathHandle_getPathHandle.28FileStatus_stat.2C_HandleOpt..._options.29)
  * [FSDataInputStream open(PathHandle handle, int bufferSize)](#FSDataInputStream_open.28PathHandle_handle.2C_int_bufferSize.29)
  * [boolean delete(Path p, boolean recursive)](#boolean_delete.28Path_p.2C_boolean_recursive.29)
  * [Object Stores: root directory deletion](#Object_Stores:_root_directory_deletion)
  * [boolean rename(Path src, Path d)](#boolean_rename.28Path_src.2C_Path_d.29)
  * [void concat(Path p, Path sources[])](#void_concat.28Path_p.2C_Path_sources.5B.5D.29)
  * [boolean truncate(Path p, long newLength)](#boolean_truncate.28Path_p.2C_long_newLength.29)
  * [boolean copyFromLocalFile(boolean delSrc, boolean overwrite, Path src, Path dst)](#boolean_copyFromLocalFile.28boolean_delSrc.2C_boolean_overwrite.2C_Path_src.2C_Path_dst.29)
* [interface RemoteIterator](#interface_RemoteIterator)
  * [boolean hasNext()](#boolean_hasNext.28.29)
  * [E next()](#E_next.28.29)
  * [Concurrency and the Remote Iterator](#Concurrency_and_the_Remote_Iterator)
* [interface StreamCapabilities](#interface_StreamCapabilities)
  * [boolean hasCapability(capability)](#boolean_hasCapability.28capability.29)
* [Etag probes through the interface EtagSource](#Etag_probes_through_the_interface_EtagSource)
  * [Etag support MUST BE across all list/getFileStatus() calls.](#Etag_support_MUST_BE_across_all_list.2FgetFileStatus.28.29_calls.)
  * [FileStatus instances MUST have etags whenever the remote store provides them.](#FileStatus_instances_MUST_have_etags_whenever_the_remote_store_provides_them.)
  * [Etags of files MUST BE Consistent across all list/getFileStatus operations.](#Etags_of_files_MUST_BE_Consistent_across_all_list.2FgetFileStatus_operations.)
  * [Etags MUST BE different for different file contents.](#Etags_MUST_BE_different_for_different_file_contents.)
  * [Etags of files SHOULD BE preserved across rename operations](#Etags_of_files_SHOULD_BE_preserved_across_rename_operations)
  * [Directories MAY have etags](#Directories_MAY_have_etags)
  * [All etag-aware FileStatus subclass MUST BE Serializable; MAY BE Writable](#All_etag-aware_FileStatus_subclass_MUST_BE_Serializable.3B_MAY_BE_Writable)
  * [Appropriate etag Path Capabilities SHOULD BE declared](#Appropriate_etag_Path_Capabilities_SHOULD_BE_declared)
  * [Non-requirements of etag support](#Non-requirements_of_etag_support)

The abstract `FileSystem` class is the original class to access Hadoop filesystems; non-abstract subclasses exist for all Hadoop-supported filesystems.

All operations that take a Path to this interface MUST support relative paths. In such a case, they must be resolved relative to the working directory defined by `setWorkingDirectory()`.

For all clients, therefore, we also add the notion of a state component PWD: this represents the present working directory of the client. Changes to this state are not reflected in the filesystem itself: they are unique to the instance of the client.

**Implementation Note**: the static `FileSystem get(URI uri, Configuration conf)` method MAY return a pre-existing instance of a filesystem client class—a class that may also be in use in other threads. The implementations of `FileSystem` shipped with Apache Hadoop *do not make any attempt to synchronize access to the working directory field*.

## Invariants

All the requirements of a valid FileSystem are considered implicit preconditions and postconditions: all operations on a valid FileSystem MUST result in a new FileSystem that is also valid.

## Feasible features

### Protected directories

HDFS has the notion of *Protected Directories*, which are declared in the option `fs.protected.directories`. Any attempt to delete or rename such a directory or a parent thereof raises an `AccessControlException`. Accordingly, any attempt to delete the root directory SHALL, if there is a protected directory, result in such an exception being raised.

## Predicates and other state access operations

### `boolean exists(Path p)`

```
def exists(FS, p) = p in paths(FS)
```

### `boolean isDirectory(Path p)`

```
def isDir(FS, p) = p in directories(FS)
```

### `boolean isFile(Path p)`

```
def isFile(FS, p) = p in filenames(FS)
```

### `FileStatus getFileStatus(Path p)`

Get the status of a path

#### Preconditions

```
if not exists(FS, p) : raise FileNotFoundException
```

#### Postconditions

```
result = stat: FileStatus where:
    if isFile(FS, p) :
        stat.length = len(FS.Files[p])
        stat.isdir = False
        stat.blockSize > 0
    elif isDir(FS, p) :
        stat.length = 0
        stat.isdir = True
    elif isSymlink(FS, p) :
        stat.length = 0
        stat.isdir = False
        stat.symlink = FS.Symlinks[p]
    stat.hasAcl = hasACL(FS, p)
    stat.isEncrypted = inEncryptionZone(FS, p)
    stat.isErasureCoded = isErasureCoded(FS, p)
```

The returned `FileStatus` status of the path additionally carries details on ACL, encryption and erasure coding information. `getFileStatus(Path p).hasAcl()` can be queried to find if the path has an ACL. `getFileStatus(Path p).isEncrypted()` can be queried to find if the path is encrypted. `getFileStatus(Path p).isErasureCoded()` will tell if the path is erasure coded or not.

YARN’s distributed cache lets applications add paths to be cached across containers and applications via `Job.addCacheFile()` and `Job.addCacheArchive()`. The cache treats world-readable resources paths added as shareable across applications, and downloads them differently, unless they are declared as encrypted.

To avoid failures during container launching, especially when delegation tokens are used, filesystems and object stores which not implement POSIX access permissions for both files and directories, MUST always return `true` to the `isEncrypted()` predicate. This can be done by setting the `encrypted` flag to true when creating the `FileStatus` instance.

### `msync()`

Synchronize metadata state of the client with the latest state of the metadata service of the FileSystem.

In highly available FileSystems standby service can be used as a read-only metadata replica. This call is essential to guarantee consistency of reads from the standby replica and to avoid stale reads.

It is currently only implemented for HDFS and others will just throw `UnsupportedOperationException`.

#### Preconditions

#### Postconditions

This call internally records the state of the metadata service at the time of the call. This guarantees consistency of subsequent reads from any metadata replica. It assures the client will never access the state of the metadata that preceded the recorded state.

#### HDFS implementation notes

HDFS supports `msync()` in HA mode by calling the Active NameNode and requesting its latest journal transaction ID. For more details see HDFS documentation [Consistent Reads from HDFS Observer NameNode](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/ObserverNameNode.html)

### `Path getHomeDirectory()`

The function `getHomeDirectory` returns the home directory for the FileSystem and the current user account.

For some FileSystems, the path is `["/", "users", System.getProperty("user-name")]`.

However, for HDFS, the username is derived from the credentials used to authenticate the client with HDFS. This may differ from the local user account name.

**It is the responsibility of the FileSystem to determine the actual home directory of the caller.**

#### Preconditions

#### Postconditions

```
result = p where valid-path(FS, p)
```

There is no requirement that the path exists at the time the method was called, or, if it exists, that it points to a directory. However, code tends to assume that `not isFile(FS, getHomeDirectory())` holds to the extent that follow-on code may fail.

#### Implementation Notes

* The `FTPFileSystem` queries this value from the remote filesystem and may fail with a `RuntimeException` or subclass thereof if there is a connectivity problem. The time to execute the operation is not bounded.

### `FileStatus[] listStatus(Path path, PathFilter filter)`

Lists entries under a path, `path`.

If `path` refers to a file and the filter accepts it, then that file’s `FileStatus` entry is returned in a single-element array.

If the path refers to a directory, the call returns a list of all its immediate child paths which are accepted by the filter —and does not include the directory itself.

A `PathFilter` `filter` is a class whose `accept(path)` returns true iff the path `path` meets the filter’s conditions.

#### Preconditions

Path `path` must exist:

```
if not exists(FS, path) : raise FileNotFoundException
```

#### Postconditions

```
if isFile(FS, path) and filter.accept(path) :
  result = [ getFileStatus(path) ]

elif isFile(FS, path) and not filter.accept(P) :
  result = []

elif isDir(FS, path):
  result = [
    getFileStatus(c) for c in children(FS, path) if filter.accepts(c)
  ]
```

**Implicit invariant**: the contents of a `FileStatus` of a child retrieved via `listStatus()` are equal to those from a call of `getFileStatus()` to the same path:

```
forall fs in listStatus(path) :
  fs == getFileStatus(fs.path)
```

**Ordering of results**: there is no guarantee of ordering of the listed entries. While HDFS currently returns an alphanumerically sorted list, neither the Posix `readdir()` nor Java’s `File.listFiles()` API calls define any ordering of returned values. Applications which require a uniform sort order on the results must perform the sorting themselves.

**Null return**: Local filesystems prior to 3.0.0 returned null upon access error. It is considered erroneous. Expect IOException upon access error.

#### Atomicity and Consistency

By the time the `listStatus()` operation returns to the caller, there is no guarantee that the information contained in the response is current. The details MAY be out of date, including the contents of any directory, the attributes of any files, and the existence of the path supplied.

The state of a directory MAY change during the evaluation process.

* After an entry at path `P` is created, and before any other changes are made to the filesystem, `listStatus(P)` MUST find the file and return its status.
* After an entry at path `P` is deleted, and before any other changes are made to the filesystem, `listStatus(P)` MUST raise a `FileNotFoundException`.
* After an entry at path `P` is created, and before any other changes are made to the filesystem, the result of `listStatus(parent(P))` SHOULD include the value of `getFileStatus(P)`.
* After an entry at path `P` is deleted, and before any other changes are made to the filesystem, the result of `listStatus(parent(P))` SHOULD NOT include the value of `getFileStatus(P)`.

This is not a theoretical possibility, it is observable in HDFS when a directory contains many thousands of files.

Consider a directory `"/d"` with the contents:

```
a
part-0000001
part-0000002
...
part-9999999
```

If the number of files is such that HDFS returns a partial listing in each response, then, if a listing `listStatus("/d")` takes place concurrently with the operation `rename("/d/a","/d/z"))`, the result may be one of:

```
[a, part-0000001, ... , part-9999999]
[part-0000001, ... , part-9999999, z]
[a, part-0000001, ... , part-9999999, z]
[part-0000001, ... , part-9999999]
```

While this situation is likely to be a rare occurrence, it MAY happen. In HDFS these inconsistent views are only likely when listing a directory with many children.

Other filesystems may have stronger consistency guarantees, or return inconsistent data more readily.

### `FileStatus[] listStatus(Path path)`

This is exactly equivalent to `listStatus(Path, DEFAULT_FILTER)` where `DEFAULT_FILTER.accept(path) = True` for all paths.

The atomicity and consistency constraints are as for `listStatus(Path, DEFAULT_FILTER)`.

### `FileStatus[] listStatus(Path[] paths, PathFilter filter)`

Enumerate all files found in the list of directories passed in, calling `listStatus(path, filter)` on each one.

As with `listStatus(path, filter)`, the results may be inconsistent. That is: the state of the filesystem changed during the operation.

There are no guarantees as to whether paths are listed in a specific order, only that they must all be listed, and, at the time of listing, exist.

#### Preconditions

All paths must exist. There is no requirement for uniqueness.

```
forall p in paths :
  exists(FS, p) else raise FileNotFoundException
```

#### Postconditions

The result is an array whose entries contain every status element found in the path listings, and no others.

```
result = [listStatus(p, filter) for p in paths]
```

Implementations MAY merge duplicate entries; and/or optimize the operation by recoginizing duplicate paths and only listing the entries once.

The default implementation iterates through the list; it does not perform any optimizations.

The atomicity and consistency constraints are as for `listStatus(Path, PathFilter)`.

### `RemoteIterator<FileStatus> listStatusIterator(Path p)`

Return an iterator enumerating the `FileStatus` entries under a path. This is similar to `listStatus(Path)` except the fact that rather than returning an entire list, an iterator is returned. The result is exactly the same as `listStatus(Path)`, provided no other caller updates the directory during the listing. Having said that, this does not guarantee atomicity if other callers are adding/deleting the files inside the directory while listing is being performed. Different filesystems may provide a more efficient implementation, for example S3A does the listing in pages and fetches the next pages asynchronously while a page is getting processed.

Note that now since the initial listing is async, bucket/path existence exception may show up later during next() call.

Callers should prefer using listStatusIterator over listStatus as it is incremental in nature.

### `FileStatus[] listStatus(Path[] paths)`

Enumerate all files found in the list of directories passed in, calling `listStatus(path, DEFAULT_FILTER)` on each one, where the `DEFAULT_FILTER` accepts all path names.

### `RemoteIterator[LocatedFileStatus] listLocatedStatus(Path path, PathFilter filter)`

Return an iterator enumerating the `LocatedFileStatus` entries under a path. This is similar to `listStatus(Path)` except that the return value is an instance of the `LocatedFileStatus` subclass of a `FileStatus`, and that rather than return an entire list, an iterator is returned.

This is actually a `protected` method, directly invoked by `listLocatedStatus(Path path)`. Calls to it may be delegated through layered filesystems, such as `FilterFileSystem`, so its implementation MUST be considered mandatory, even if `listLocatedStatus(Path path)` has been implemented in a different manner. There are open JIRAs proposing making this method public; it may happen in future.

There is no requirement for the iterator to provide a consistent view of the child entries of a path. The default implementation does use `listStatus(Path)` to list its children, with its consistency constraints already documented. Other implementations may perform the enumeration even more dynamically. For example fetching a windowed subset of child entries, so avoiding building up large data structures and the transmission of large messages. In such situations, changes to the filesystem are more likely to become visible.

Callers MUST assume that the iteration operation MAY fail if changes to the filesystem take place between this call returning and the iteration being completely performed.

#### Preconditions

Path `path` must exist:

```
if not exists(FS, path) : raise FileNotFoundException
```

#### Postconditions

The operation generates a set of results, `resultset`, equal to the result of `listStatus(path, filter)`:

```
if isFile(FS, path) and filter.accept(path) :
  resultset =  [ getLocatedFileStatus(FS, path) ]

elif isFile(FS, path) and not filter.accept(path) :
  resultset = []

elif isDir(FS, path) :
  resultset = [
    getLocatedFileStatus(FS, c)
     for c in children(FS, path) where filter.accept(c)
  ]
```

The operation `getLocatedFileStatus(FS, path: Path): LocatedFileStatus` is defined as a generator of a `LocatedFileStatus` instance `ls` where:

```
fileStatus = getFileStatus(FS, path)

bl = getFileBlockLocations(FS, path, 0, fileStatus.len)

locatedFileStatus = new LocatedFileStatus(fileStatus, bl)
```

The ordering in which the elements of `resultset` are returned in the iterator is undefined.

The atomicity and consistency constraints are as for `listStatus(Path, PathFilter)`.

### `RemoteIterator[LocatedFileStatus] listLocatedStatus(Path path)`

The equivalent to `listLocatedStatus(path, DEFAULT_FILTER)`, where `DEFAULT_FILTER` accepts all path names.

### `RemoteIterator[LocatedFileStatus] listFiles(Path path, boolean recursive)`

Create an iterator over all files in/under a directory, potentially recursing into child directories.

The goal of this operation is to permit large recursive directory scans to be handled more efficiently by filesystems, by reducing the amount of data which must be collected in a single RPC call.

#### Preconditions

```
if not exists(FS, path) : raise FileNotFoundException
```

### Postconditions

The outcome is an iterator, whose output from the sequence of `iterator.next()` calls can be defined as the set `iteratorset`:

```
if not recursive:
  iteratorset == listStatus(path)
else:
  iteratorset = [
    getLocatedFileStatus(FS, d)
      for d in descendants(FS, path)
  ]
```

The function `getLocatedFileStatus(FS, d)` is as defined in `listLocatedStatus(Path, PathFilter)`.

The atomicity and consistency constraints are as for `listStatus(Path, PathFilter)`.

### `ContentSummary getContentSummary(Path path)`

Given a path return its content summary.

`getContentSummary()` first checks if the given path is a file and if yes, it returns 0 for directory count and 1 for file count.

#### Preconditions

```
if not exists(FS, path) : raise FileNotFoundException
```

#### Postconditions

Returns a `ContentSummary` object with information such as directory count and file count for a given path.

The atomicity and consistency constraints are as for `listStatus(Path, PathFilter)`.

### `BlockLocation[] getFileBlockLocations(FileStatus f, int s, int l)`

#### Preconditions

```
if s < 0 or l < 0 : raise {HadoopIllegalArgumentException, InvalidArgumentException}
```

* HDFS throws `HadoopIllegalArgumentException` for an invalid offset or length; this extends `IllegalArgumentException`.

#### Postconditions

If the filesystem is location aware, it must return the list of block locations where the data in the range `[s:s+l]` can be found.

```
if f == null :
    result = null
elif f.getLen() <= s:
    result = []
else result = [ locations(FS, b) for b in blocks(FS, p, s, s+l)]
```

Where

```
  def locations(FS, b) = a list of all locations of a block in the filesystem

  def blocks(FS, p, s, s +  l)  = a list of the blocks containing data(FS, path)[s:s+l]
```

Note that as `length(FS, f)` is defined as `0` if `isDir(FS, f)`, the result of `getFileBlockLocations()` on a directory is `[]`

If the filesystem is not location aware, it SHOULD return

```
  [
    BlockLocation(["localhost:9866"] ,
              ["localhost"],
              ["/default/localhost"]
               0, f.getLen())
   ] ;
```

\*A bug in Hadoop 1.0.3 means that a topology path of the same number of elements as the cluster topology MUST be provided, hence Filesystems SHOULD return that `"/default/localhost"` path. While this is no longer an issue, the convention is generally retained.

### `BlockLocation[] getFileBlockLocations(Path P, int S, int L)`

#### Preconditions

```
if p == null : raise NullPointerException
if not exists(FS, p) : raise FileNotFoundException
```

#### Postconditions

```
result = getFileBlockLocations(getFileStatus(FS, P), S, L)
```

### `long getDefaultBlockSize()`

Get the “default” block size for a filesystem. This is often used during split calculations to divide work optimally across a set of worker processes.

#### Preconditions

#### Postconditions

```
result = integer > 0
```

Although there is no defined minimum value for this result, as it is used to partition work during job submission, a block size that is too small will result in badly partitioned workload, or even the `JobSubmissionClient` and equivalent running out of memory as it calculates the partitions.

Any FileSystem that does not actually break files into blocks SHOULD return a number for this that results in efficient processing. A FileSystem MAY make this user-configurable (the object store connectors usually do this).

### `long getDefaultBlockSize(Path p)`

Get the “default” block size for a path –that is, the block size to be used when writing objects to a path in the filesystem.

#### Preconditions

#### Postconditions

```
result = integer >= 0
```

The outcome of this operation is usually identical to `getDefaultBlockSize()`, with no checks for the existence of the given path.

Filesystems that support mount points may have different default values for different paths, in which case the specific default value for the destination path SHOULD be returned.

It is not an error if the path does not exist: the default/recommended value for that part of the filesystem MUST be returned.

### `long getBlockSize(Path p)`

This method is exactly equivalent to querying the block size of the `FileStatus` structure returned in `getFileStatus(p)`. It is deprecated in order to encourage users to make a single call to `getFileStatus(p)` and then use the result to examine multiple attributes of the file (e.g. length, type, block size). If more than one attribute is queried, This can become a significant performance optimization —and reduce load on the filesystem.

#### Preconditions

```
if not exists(FS, p) : raise FileNotFoundException
```

#### Postconditions

```
if len(FS, P) > 0 :  getFileStatus(P).getBlockSize() > 0
result == getFileStatus(P).getBlockSize()
```

1. The outcome of this operation MUST be identical to the value of `getFileStatus(P).getBlockSize()`.
2. By inference, it MUST be > 0 for any file of length > 0.

### `Path getEnclosingRoot(Path p)`

This method is used to find a root directory for a path given. This is useful for creating staging and temp directories in the same enclosing root directory. There are constraints around how renames are allowed to atomically occur (ex. across hdfs volumes or across encryption zones).

For any two paths p1 and p2 that do not have the same enclosing root, `rename(p1, p2)` is expected to fail or will not be atomic.

For object stores, even with the same enclosing root, there is no guarantee file or directory rename is atomic

The following statement is always true: `getEnclosingRoot(p) == getEnclosingRoot(getEnclosingRoot(p))`

```
path in ancestors(FS, p) or path == p:
isDir(FS, p)
```

#### Preconditions

The path does not have to exist, but the path does need to be valid and reconcilable by the filesystem \* if a linkfallback is used all paths are reconcilable \* if a linkfallback is not used there must be a mount point covering the path

#### Postconditions

* The path returned will not be null, if there is no deeper enclosing root, the root path (“/”) will be returned.
* The path returned is a directory

## State Changing Operations

### `boolean mkdirs(Path p, FsPermission permission)`

Create a directory and all its parents.

#### Preconditions

The path must either be a directory or not exist

```
 if exists(FS, p) and not isDir(FS, p) :
     raise [ParentNotDirectoryException, FileAlreadyExistsException, IOException]
```

No ancestor may be a file

```
forall d = ancestors(FS, p) : 
    if exists(FS, d) and not isDir(FS, d) :
        raise {ParentNotDirectoryException, FileAlreadyExistsException, IOException}
```

#### Postconditions

```
FS' where FS'.Directories = FS.Directories + [p] + ancestors(FS, p)
result = True
```

The condition exclusivity requirement of a FileSystem’s directories, files and symbolic links must hold.

The probe for the existence and type of a path and directory creation MUST be atomic. The combined operation, including `mkdirs(parent(F))` MAY be atomic.

The return value is always true—even if a new directory is not created (this is defined in HDFS).

### `FSDataOutputStream create(Path, ...)`

```
FSDataOutputStream create(Path p,
      FsPermission permission,
      boolean overwrite,
      int bufferSize,
      short replication,
      long blockSize,
      Progressable progress) throws IOException;
```

#### Preconditions

The file must not exist for a no-overwrite create:

```
if not overwrite and isFile(FS, p) : raise FileAlreadyExistsException
```

Writing to or overwriting a directory must fail.

```
if isDir(FS, p) : raise {FileAlreadyExistsException, FileNotFoundException, IOException}
```

No ancestor may be a file

```
forall d = ancestors(FS, p) : 
    if exists(FS, d) and not isDir(FS, d) :
        raise {ParentNotDirectoryException, FileAlreadyExistsException, IOException}
```

FileSystems may reject the request for other reasons, such as the FS being read-only (HDFS), the block size being below the minimum permitted (HDFS), the replication count being out of range (HDFS), quotas on namespace or filesystem being exceeded, reserved names, etc. All rejections SHOULD be `IOException` or a subclass thereof and MAY be a `RuntimeException` or subclass. For instance, HDFS may raise an `InvalidPathException`.

#### Postconditions

```
FS' where :
   FS'.Files[p] == []
   ancestors(p) subset-of FS'.Directories

result = FSDataOutputStream
```

A zero byte file MUST exist at the end of the specified path, visible to all.

The updated (valid) FileSystem MUST contain all the parent directories of the path, as created by `mkdirs(parent(p))`.

The result is `FSDataOutputStream`, which through its operations may generate new filesystem states with updated values of `FS.Files[p]`

The behavior of the returned stream is covered in [Output](outputstream.html).

#### Implementation Notes

* Some implementations split the create into a check for the file existing from the actual creation. This means the operation is NOT atomic: it is possible for clients creating files with `overwrite==true` to fail if the file is created by another client between the two tests.
* The S3A and potentially other Object Stores connectors currently don’t change the `FS` state until the output stream `close()` operation is completed. This is a significant difference between the behavior of object stores and that of filesystems, as it allows >1 client to create a file with `overwrite=false`, and potentially confuse file/directory logic. In particular, using `create()` to acquire an exclusive lock on a file (whoever creates the file without an error is considered the holder of the lock) may not be a safe algorithm to use when working with object stores.
* Object stores may create an empty file as a marker when a file is created. However, object stores with `overwrite=true` semantics may not implement this atomically, so creating files with `overwrite=false` cannot be used as an implicit exclusion mechanism between processes.
* The Local FileSystem raises a `FileNotFoundException` when trying to create a file over a directory, hence it is listed as an exception that MAY be raised when this precondition fails.
* Not covered: symlinks. The resolved path of the symlink is used as the final path argument to the `create()` operation

### `FSDataOutputStreamBuilder createFile(Path p)`

Make a `FSDataOutputStreamBuilder` to specify the parameters to create a file.

The behavior of the returned stream is covered in [Output](outputstream.html).

#### Implementation Notes

`createFile(p)` returns a `FSDataOutputStreamBuilder` only and does not make changes on the filesystem immediately. When `build()` is invoked on the `FSDataOutputStreamBuilder`, the builder parameters are verified and [`create(Path p)`](#FileSystem.create) is invoked on the underlying filesystem. `build()` has the same preconditions and postconditions as [`create(Path p)`](#FileSystem.create).

* Similar to [`create(Path p)`](#FileSystem.create), files are overwritten by default, unless specified by `builder.overwrite(false)`.
* Unlike [`create(Path p)`](#FileSystem.create), missing parent directories are not created by default, unless specified by `builder.recursive()`.

### `FSDataOutputStream append(Path p, int bufferSize, Progressable progress)`

Implementations without a compliant call SHOULD throw `UnsupportedOperationException`.

#### Preconditions

```
if not exists(FS, p) : raise FileNotFoundException

if not isFile(FS, p) : raise {FileAlreadyExistsException, FileNotFoundException, IOException}
```

#### Postconditions

```
FS' = FS
result = FSDataOutputStream
```

Return: `FSDataOutputStream`, which can update the entry `FS'.Files[p]` by appending data to the existing list.

The behavior of the returned stream is covered in [Output](outputstream.html).

### `FSDataOutputStreamBuilder appendFile(Path p)`

Make a `FSDataOutputStreamBuilder` to specify the parameters to append to an existing file.

The behavior of the returned stream is covered in [Output](outputstream.html).

#### Implementation Notes

`appendFile(p)` returns a `FSDataOutputStreamBuilder` only and does not make change on filesystem immediately. When `build()` is invoked on the `FSDataOutputStreamBuilder`, the builder parameters are verified and [`append()`](#FileSystem.append) is invoked on the underlying filesystem. `build()` has the same preconditions and postconditions as [`append()`](#FileSystem.append).

### `FSDataInputStream open(Path f, int bufferSize)`

Implementations without a compliant call SHOULD throw `UnsupportedOperationException`.

#### Preconditions

```
if not isFile(FS, p)) : raise {FileNotFoundException, IOException}
```

This is a critical precondition. Implementations of some FileSystems (e.g. Object stores) could shortcut one round trip by postponing their HTTP GET operation until the first `read()` on the returned `FSDataInputStream`. However, much client code does depend on the existence check being performed at the time of the `open()` operation. Implementations MUST check for the presence of the file at the time of creation. This does not imply that the file and its data is still at the time of the following `read()` or any successors.

#### Postconditions

```
result = FSDataInputStream(0, FS.Files[p])
```

The result provides access to the byte array defined by `FS.Files[p]`; whether that access is to the contents at the time the `open()` operation was invoked, or whether and how it may pick up changes to that data in later states of FS is an implementation detail.

The result MUST be the same for local and remote callers of the operation.

#### HDFS implementation notes

1. HDFS MAY throw `UnresolvedPathException` when attempting to traverse symbolic links
2. HDFS throws `IOException("Cannot open filename " + src)` if the path exists in the metadata, but no copies of its blocks can be located; -`FileNotFoundException` would seem more accurate and useful.

### `FSDataInputStreamBuilder openFile(Path path)`

See [openFile()](openfile.html).

### `FSDataInputStreamBuilder openFile(PathHandle)`

See [openFile()](openfile.html).

### `PathHandle getPathHandle(FileStatus stat, HandleOpt... options)`

Implementations without a compliant call MUST throw `UnsupportedOperationException`

#### Preconditions

```
let stat = getFileStatus(Path p)
let FS' where:
  (FS'.Directories, FS.Files', FS'.Symlinks)
  p' in paths(FS') where:
    exists(FS, stat.path) implies exists(FS', p')
```

The referent of a `FileStatus` instance, at the time it was resolved, is the same referent as the result of `getPathHandle(FileStatus)`. The `PathHandle` may be used in subsequent operations to ensure invariants hold between calls.

The `options` parameter specifies whether a subsequent call e.g., `open(PathHandle)` will succeed if the referent data or location changed. By default, any modification results in an error. The caller MAY specify relaxations that allow operations to succeed even if the referent exists at a different path and/or its data are changed.

An implementation MUST throw `UnsupportedOperationException` if it cannot support the semantics specified by the caller. The default set of options are as follows.

|  | Unmoved | Moved |
| --- | --- | --- |
| Unchanged | EXACT | CONTENT |
| Changed | PATH | REFERENCE |

Changes to ownership, extended attributes, and other metadata are not required to match the `PathHandle`. Implementations can extend the set of `HandleOpt` parameters with custom constraints.

##### Examples

A client specifies that the `PathHandle` should track the entity across renames using `REFERENCE`. The implementation MUST throw an `UnsupportedOperationException` when creating the `PathHandle` unless failure to resolve the reference implies the entity no longer exists.

A client specifies that the `PathHandle` should resolve only if the entity is unchanged using `PATH`. The implementation MUST throw an `UnsupportedOperationException` when creating the `PathHandle` unless it can distinguish between an identical entity located subsequently at the same path.

#### Postconditions

```
result = PathHandle(p')
```

#### Implementation notes

The referent of a `PathHandle` is the namespace when the `FileStatus` instance was created, *not* its state when the `PathHandle` is created. An implementation MAY reject attempts to create or resolve `PathHandle` instances that are valid, but expensive to service.

Object stores that implement rename by copying objects MUST NOT claim to support `CONTENT` and `REFERENCE` unless the lineage of the object is resolved.

It MUST be possible to serialize a `PathHandle` instance and reinstantiate it in one or more processes, on another machine, and arbitrarily far into the future without changing its semantics. The implementation MUST refuse to resolve instances if it can no longer guarantee its invariants.

#### HDFS implementation notes

HDFS does not support `PathHandle` references to directories or symlinks. Support for `CONTENT` and `REFERENCE` looks up files by INode. INodes are not unique across NameNodes, so federated clusters SHOULD include enough metadata in the `PathHandle` to detect references from other namespaces.

### `FSDataInputStream open(PathHandle handle, int bufferSize)`

Implementations without a compliant call MUST throw `UnsupportedOperationException`

#### Preconditions

```
let fd = getPathHandle(FileStatus stat)
if stat.isdir : raise IOException
let FS' where:
  (FS'.Directories, FS.Files', FS'.Symlinks)
  p' in FS'.Files where:
    FS'.Files[p'] = fd
if not exists(FS', p') : raise InvalidPathHandleException
```

The implementation MUST resolve the referent of the `PathHandle` following the constraints specified at its creation by `getPathHandle(FileStatus)`.

Metadata necessary for the `FileSystem` to satisfy this contract MAY be encoded in the `PathHandle`.

#### Postconditions

```
result = FSDataInputStream(0, FS'.Files[p'])
```

The stream returned is subject to the constraints of a stream returned by `open(Path)`. Constraints checked on open MAY hold to hold for the stream, but this is not guaranteed.

For example, a `PathHandle` created with `CONTENT` constraints MAY return a stream that ignores updates to the file after it is opened, if it was unmodified when `open(PathHandle)` was resolved.

#### Implementation notes

An implementation MAY check invariants either at the server or before returning the stream to the client. For example, an implementation may open the file, then verify the invariants in the `PathHandle` using `getFileStatus(Path)` to implement `CONTENT`. This could yield false positives and it requires additional RPC traffic.

### `boolean delete(Path p, boolean recursive)`

Delete a path, be it a file, symbolic link or directory. The `recursive` flag indicates whether a recursive delete should take place —if unset then a non-empty directory cannot be deleted.

Except in the special case of the root directory, if this API call completed successfully then there is nothing at the end of the path. That is: the outcome is desired. The return flag simply tells the caller whether or not any change was made to the state of the filesystem.

*Note*: many uses of this method surround it with checks for the return value being false, raising exception if so. For example

```
if (!fs.delete(path, true)) throw new IOException("Could not delete " + path);
```

This pattern is not needed. Code SHOULD just call `delete(path, recursive)` and assume the destination is no longer present —except in the special case of root directories, which will always remain (see below for special coverage of root directories).

#### Preconditions

A directory with children and `recursive == False` cannot be deleted

```
if isDir(FS, p) and not recursive and (children(FS, p) != {}) : raise IOException
```

(HDFS raises `PathIsNotEmptyDirectoryException` here.)

#### Postconditions

##### Nonexistent path

If the file does not exist the filesystem state does not change

```
if not exists(FS, p) :
    FS' = FS
    result = False
```

The result SHOULD be `False`, indicating that no file was deleted.

##### Simple File

A path referring to a file is removed, return value: `True`

```
if isFile(FS, p) :
    FS' = (FS.Directories, FS.Files - [p], FS.Symlinks)
    result = True
```

##### Empty root directory, `recursive == False`

Deleting an empty root does not change the filesystem state and may return true or false.

```
if isRoot(p) and children(FS, p) == {} :
    FS ' = FS
    result = (undetermined)
```

There is no consistent return code from an attempt to delete the root directory.

Implementations SHOULD return true; this avoids code which checks for a false return value from overreacting.

*Object Stores*: see [Object Stores: root directory deletion](#object-stores-rm-root).

##### Empty (non-root) directory `recursive == False`

Deleting an empty directory that is not root will remove the path from the FS and return true.

```
if isDir(FS, p) and not isRoot(p) and children(FS, p) == {} :
    FS' = (FS.Directories - [p], FS.Files, FS.Symlinks)
    result = True
```

##### Recursive delete of non-empty root directory

Deleting a root path with children and `recursive==True` can generally have three outcomes:

1. The POSIX model assumes that if the user has the correct permissions to delete everything, they are free to do so (resulting in an empty filesystem).

   ```
   if isDir(FS, p) and isRoot(p) and recursive :
       FS' = ({["/"]}, {}, {}, {})
       result = True
   ```
2. HDFS never permits the deletion of the root of a filesystem; the filesystem must be taken offline and reformatted if an empty filesystem is desired.

   ```
   if isDir(FS, p) and isRoot(p) and recursive :
       FS' = FS
       result = False
   ```
3. Object Stores: see [Object Stores: root directory deletion](#object-stores-rm-root).

This specification does not recommend any specific action. Do note, however, that the POSIX model assumes that there is a permissions model such that normal users do not have the permission to delete that root directory; it is an action which only system administrators should be able to perform.

Any filesystem client which interacts with a remote filesystem which lacks such a security model, MAY reject calls to `delete("/", true)` on the basis that it makes it too easy to lose data.

### Object Stores: root directory deletion

Some of the object store based filesystem implementations always return false when deleting the root, leaving the state of the store unchanged.

```
if isRoot(p) :
    FS' = FS
    result = False
```

This is irrespective of the recursive flag status or the state of the directory.

This is a simplification which avoids the inevitably non-atomic scan and delete of the contents of the store. It also avoids any confusion about whether the operation actually deletes that specific store/container itself, and adverse consequences of the simpler permissions models of stores.

##### Recursive delete of non-root directory

Deleting a non-root path with children `recursive==true` removes the path and all descendants

```
if isDir(FS, p) and not isRoot(p) and recursive :
    FS' where:
        not isDir(FS', p)
        and forall d in descendants(FS, p):
            not isDir(FS', d)
            not isFile(FS', d)
            not isSymlink(FS', d)
    result = True
```

#### Atomicity

* Deleting a file MUST be an atomic action.
* Deleting an empty directory MUST be an atomic action.
* A recursive delete of a directory tree MUST be atomic.

#### Implementation Notes

* Object Stores and other non-traditional filesystems onto which a directory tree is emulated, tend to implement `delete()` as recursive listing and entry-by-entry delete operation. This can break the expectations of client applications for O(1) atomic directory deletion, preventing the stores’ use as drop-in replacements for HDFS.

### `boolean rename(Path src, Path d)`

In terms of its specification, `rename()` is one of the most complex operations within a filesystem.

In terms of its implementation, it is the one with the most ambiguity regarding when to return false versus raising an exception.

Rename includes the calculation of the destination path. If the destination exists and is a directory, the final destination of the rename becomes the destination + the filename of the source path.

```
let dest = if (isDir(FS, d) and d != src) :
        d + [filename(src)]
    else :
        d
```

#### Preconditions

All checks on the destination path MUST take place after the final `dest` path has been calculated.

Source `src` must exist:

```
if not exists(FS, src) : raise FileNotFoundException
```

`dest` cannot be a descendant of `src`:

```
if isDescendant(FS, src, dest) : raise IOException
```

This implicitly covers the special case of `isRoot(FS, src)`.

`dest` must be root, or have a parent that exists:

```
if not (isRoot(FS, dest) or exists(FS, parent(dest))) : raise IOException
```

The parent path of a destination must not be a file:

```
if isFile(FS, parent(dest)) : raise IOException
```

This implicitly covers all the ancestors of the parent.

There must not be an existing file at the end of the destination path:

```
if isFile(FS, dest) : raise FileAlreadyExistsException, IOException
```

#### Postconditions

##### Renaming a directory onto itself

Renaming a directory onto itself is no-op; return value is not specified.

In POSIX the result is `False`; in HDFS the result is `True`.

```
if isDir(FS, src) and src == dest :
    FS' = FS
    result = (undefined)
```

##### Renaming a file to self

Renaming a file to itself is a no-op; the result is `True`.

```
 if isFile(FS, src) and src == dest :
     FS' = FS
     result = True
```

##### Renaming a file onto a nonexistent path

Renaming a file where the destination is a directory moves the file as a child of the destination directory, retaining the filename element of the source path.

```
if isFile(FS, src) and src != dest:
    FS' where:
        not exists(FS', src)
        and exists(FS', dest)
        and data(FS', dest) == data (FS, source)
    result = True
```

##### Renaming a directory onto a directory

If `src` is a directory then all its children will then exist under `dest`, while the path `src` and its descendants will no longer exist. The names of the paths under `dest` will match those under `src`, as will the contents:

```
if isDir(FS, src) and isDir(FS, dest) and src != dest :
    FS' where:
        not exists(FS', src)
        and dest in FS'.Directories
        and forall c in descendants(FS, src) :
            not exists(FS', c))
        and forall c in descendants(FS, src) where isDir(FS, c):
            isDir(FS', dest + childElements(src, c)
        and forall c in descendants(FS, src) where not isDir(FS, c):
                data(FS', dest + childElements(s, c)) == data(FS, c)
    result = True
```

##### Renaming into a path where the parent path does not exist

```
  not exists(FS, parent(dest))
```

There is no consistent behavior here.

*HDFS*

The outcome is no change to FileSystem state, with a return value of false.

```
FS' = FS
result = False
```

*Local Filesystem*

The outcome is as a normal rename, with the additional (implicit) feature that the parent directories of the destination also exist.

```
exists(FS', parent(dest))
```

*S3A FileSystem*

The outcome is as a normal rename, with the additional (implicit) feature that the parent directories of the destination then exist: `exists(FS', parent(dest))`

There is a check for and rejection if the `parent(dest)` is a file, but no checks for any other ancestors.

*Other Filesystems*

Other filesystems strictly reject the operation, raising a `FileNotFoundException`

##### Concurrency requirements

* The core operation of `rename()`—moving one entry in the filesystem to another—MUST be atomic. Some applications rely on this as a way to coordinate access to data.
* Some FileSystem implementations perform checks on the destination FileSystem before and after the rename. One example of this is `ChecksumFileSystem`, which provides checksummed access to local data. The entire sequence MAY NOT be atomic.

##### Implementation Notes

**Files open for reading, writing or appending**

The behavior of `rename()` on an open file is unspecified: whether it is allowed, what happens to later attempts to read from or write to the open stream

**Renaming a directory onto itself**

The return code of renaming a directory onto itself is unspecified.

**Destination exists and is a file**

Renaming a file atop an existing file is specified as failing, raising an exception.

* Local FileSystem : the rename succeeds; the destination file is replaced by the source file.
* HDFS : The rename fails, no exception is raised. Instead the method call simply returns false.

**Missing source file**

If the source file `src` does not exist, `FileNotFoundException` should be raised.

HDFS fails without raising an exception; `rename()` merely returns false.

```
FS' = FS
result = false
```

The behavior of HDFS here should not be considered a feature to replicate. `FileContext` explicitly changed the behavior to raise an exception, and the retrofitting of that action to the `DFSFileSystem` implementation is an ongoing matter for debate.

### `void concat(Path p, Path sources[])`

Joins multiple blocks together to create a single file. This is a little-used operation currently implemented only by HDFS.

Implementations without a compliant call SHOULD throw `UnsupportedOperationException`.

#### Preconditions

```
if not exists(FS, p) : raise FileNotFoundException

if sources==[] : raise IllegalArgumentException
```

All sources MUST be in the same directory:

```
for s in sources:
    if parent(s) != parent(p) : raise IllegalArgumentException
```

All block sizes must match that of the target:

```
for s in sources:
    getBlockSize(FS, s) == getBlockSize(FS, p)
```

No duplicate paths:

```
let input = sources + [p]
not (exists i, j: i != j and input[i] == input[j])
```

HDFS: All source files except the final one MUST be a complete block:

```
for s in (sources[0:length(sources)-1] + [p]):
    (length(FS, s) mod getBlockSize(FS, p)) == 0
```

#### Postconditions

```
FS' where:
    (data(FS', p) = data(FS, p) + data(FS, sources[0]) + ... + data(FS, sources[length(sources)-1]))
    for s in sources: not exists(FS', s)
```

HDFS’s restrictions may be an implementation detail of how it implements `concat` by changing the inode references to join them together in a sequence. As no other filesystem in the Hadoop core codebase implements this method, there is no way to distinguish implementation detail from specification.

### `boolean truncate(Path p, long newLength)`

Truncate file `p` to the specified `newLength`.

Implementations without a compliant call SHOULD throw `UnsupportedOperationException`.

#### Preconditions

```
if not exists(FS, p) : raise FileNotFoundException

if isDir(FS, p) : raise {FileNotFoundException, IOException}

if newLength < 0 || newLength > len(FS.Files[p]) : raise HadoopIllegalArgumentException
```

HDFS: The source file MUST be closed. Truncate cannot be performed on a file, which is open for writing or appending.

#### Postconditions

```
len(FS'.Files[p]) = newLength
```

Return: `true`, if truncation is finished and the file can be immediately opened for appending, or `false` otherwise.

HDFS: HDFS returns `false` to indicate that a background process of adjusting the length of the last block has been started, and clients should wait for it to complete before they can proceed with further file updates.

#### Concurrency

If an input stream is open when truncate() occurs, the outcome of read operations related to the part of the file being truncated is undefined.

### `boolean copyFromLocalFile(boolean delSrc, boolean overwrite, Path src, Path dst)`

The source file or directory at `src` is on the local disk and is copied into the file system at destination `dst`. If the source must be deleted after the move then `delSrc` flag must be set to TRUE. If destination already exists, and the destination contents must be overwritten then `overwrite` flag must be set to TRUE.

#### Preconditions

Source and destination must be different

```
if src = dest : raise FileExistsException
```

Destination and source must not be descendants of one another

```
if isDescendant(src, dest) or isDescendant(dest, src) : raise IOException
```

The source file or directory must exist locally:

```
if not exists(LocalFS, src) : raise FileNotFoundException
```

Directories cannot be copied into files regardless to what the overwrite flag is set to:

```
if isDir(LocalFS, src) and isFile(FS, dst) : raise PathExistsException
```

For all cases, except the one for which the above precondition throws, the overwrite flag must be set to TRUE for the operation to succeed if destination exists. This will also overwrite any files / directories at the destination:

```
if exists(FS, dst) and not overwrite : raise PathExistsException
```

#### Determining the final name of the copy

Given a base path on the source `base` and a child path `child` where `base` is in `ancestors(child) + child`:

```
def final_name(base, child, dest):
    if base == child:
        return dest
    else:
        return dest + childElements(base, child)
```

#### Outcome where source is a file `isFile(LocalFS, src)`

For a file, data at destination becomes that of the source. All ancestors are directories.

```
if isFile(LocalFS, src) and (not exists(FS, dest) or (exists(FS, dest) and overwrite)):
    FS' = FS where:
        FS'.Files[dest] = LocalFS.Files[src]
        FS'.Directories = FS.Directories + ancestors(FS, dest)
    LocalFS' = LocalFS where
        not delSrc or (delSrc = true and delete(LocalFS, src, false))
else if isFile(LocalFS, src) and isDir(FS, dest):
    FS' = FS where:
        let d = final_name(src, dest)
        FS'.Files[d] = LocalFS.Files[src]
    LocalFS' = LocalFS where:
        not delSrc or (delSrc = true and delete(LocalFS, src, false))
```

There are no expectations that the file changes are atomic for both local `LocalFS` and remote `FS`.

#### Outcome where source is a directory `isDir(LocalFS, src)`

```
if isDir(LocalFS, src) and (isFile(FS, dest) or isFile(FS, dest + childElements(src))):
    raise FileAlreadyExistsException
else if isDir(LocalFS, src):
    if exists(FS, dest):
        dest' = dest + childElements(src)
        if exists(FS, dest') and not overwrite:
            raise PathExistsException
    else:
        dest' = dest

    FS' = FS where:
        forall c in descendants(LocalFS, src):
            not exists(FS', final_name(c)) or overwrite
        and forall c in descendants(LocalFS, src) where isDir(LocalFS, c):
            FS'.Directories = FS'.Directories + (dest' + childElements(src, c))
        and forall c in descendants(LocalFS, src) where isFile(LocalFS, c):
            FS'.Files[final_name(c, dest')] = LocalFS.Files[c]
    LocalFS' = LocalFS where
        not delSrc or (delSrc = true and delete(LocalFS, src, true))
```

There are no expectations of operation isolation / atomicity. This means files can change in source or destination while the operation is executing. No guarantees are made for the final state of the file or directory after a copy other than it is best effort. E.g.: when copying a directory, one file can be moved from source to destination but there’s nothing stopping the new file at destination being updated while the copy operation is still in place.

#### Implementation

The default HDFS implementation, is to recurse through each file and folder, found at `src`, and copy them sequentially to their final destination (relative to `dst`).

Object store based file systems should be mindful of what limitations arise from the above implementation and could take advantage of parallel uploads and possible re-ordering of files copied into the store to maximize throughput.

## interface `RemoteIterator`

The `RemoteIterator` interface is used as a remote-access equivalent to `java.util.Iterator`, allowing the caller to iterate through a finite sequence of remote data elements.

The core differences are

1. `Iterator`’s optional `void remove()` method is not supported.
2. For those methods which are supported, `IOException` exceptions may be raised.

```
public interface RemoteIterator<E> {
  boolean hasNext() throws IOException;
  E next() throws IOException;
}
```

The basic view of the interface is that `hasNext()` being true implies that `next()` will successfully return the next entry in the list:

```
while hasNext(): next()
```

Equally, a successful call to `next()` implies that had `hasNext()` been invoked prior to the call to `next()`, it would have been true.

```
boolean elementAvailable = hasNext();
try {
  next();
  assert elementAvailable;
} catch (NoSuchElementException e) {
  assert !elementAvailable
}
```

The `next()` operator MUST iterate through the list of available results, *even if no calls to `hasNext()` are made*.

That is, it is possible to enumerate the results through a loop which only terminates when a `NoSuchElementException` exception is raised.

```
try {
  while (true) {
    process(iterator.next());
  }
} catch (NoSuchElementException ignored) {
  // the end of the list has been reached
}
```

The output of the iteration is equivalent to the loop

```
while (iterator.hasNext()) {
  process(iterator.next());
}
```

As raising exceptions is an expensive operation in JVMs, the `while(hasNext())` loop option is more efficient. (see also [Concurrency and the Remote Iterator](#RemoteIteratorConcurrency) for a discussion on this topic).

Implementors of the interface MUST support both forms of iterations; authors of tests SHOULD verify that both iteration mechanisms work.

The iteration is required to return a finite sequence; both forms of loop MUST ultimately terminate. All implementations of the interface in the Hadoop codebase meet this requirement; all consumers assume that it holds.

### `boolean hasNext()`

Returns true if-and-only-if a subsequent single call to `next()` would return an element rather than raise an exception.

#### Preconditions

#### Postconditions

```
result = True ==> next() will succeed.
result = False ==> next() will raise an exception
```

Multiple calls to `hasNext()`, without any intervening `next()` calls, MUST return the same value.

```
boolean has1 = iterator.hasNext();
boolean has2 = iterator.hasNext();
assert has1 == has2;
```

### `E next()`

Return the next element in the iteration.

#### Preconditions

```
hasNext() else raise java.util.NoSuchElementException
```

#### Postconditions

```
result = the next element in the iteration
```

Repeated calls to `next()` return subsequent elements in the sequence, until the entire sequence has been returned.

### Concurrency and the Remote Iterator

The primary use of `RemoteIterator` in the filesystem APIs is to list files on (possibly remote) filesystems. These filesystems are invariably accessed concurrently; the state of the filesystem MAY change between a `hasNext()` probe and the invocation of the `next()` call.

During iteration through a `RemoteIterator`, if the directory is deleted on remote filesystem, then `hasNext()` or `next()` call may throw `FileNotFoundException`.

Accordingly, a robust iteration through a `RemoteIterator` would catch and discard `NoSuchElementException` exceptions raised during the process, which could be done through the `while(true)` iteration example above, or through a `hasNext()/next()` sequence with an outer `try/catch` clause to catch a `NoSuchElementException` alongside other exceptions which may be raised during a failure (for example, a `FileNotFoundException`)

```
try {
  while (iterator.hasNext()) {
    process(iterator.next());
  }
} catch (NoSuchElementException ignored) {
  // the end of the list has been reached
}
```

It is notable that this is *not* done in the Hadoop codebase. This does not imply that robust loops are not recommended —more that the concurrency problems were not considered during the implementation of these loops.

## interface `StreamCapabilities`

The `StreamCapabilities` provides a way to programmatically query the capabilities that `OutputStream`, `InputStream`, or other FileSystem class supports.

```
public interface StreamCapabilities {
  boolean hasCapability(String capability);
}
```

### `boolean hasCapability(capability)`

Return true iff the `OutputStream`, `InputStream`, or other FileSystem class has the desired capability.

The caller can query the capabilities of a stream using a string value. Here is a table of possible string values:

| String | Constant | Implements | Description |
| --- | --- | --- | --- |
| hflush | HFLUSH | Syncable | Flush out the data in client’s user buffer. After the return of this call, new readers will see the data. |
| hsync | HSYNC | Syncable | Flush out the data in client’s user buffer all the way to the disk device (but the disk may have it in its cache). Similar to POSIX fsync. |
| in:readahead | READAHEAD | CanSetReadahead | Set the readahead on the input stream. |
| dropbehind | DROPBEHIND | CanSetDropBehind | Drop the cache. |
| in:unbuffer | UNBUFFER | CanUnbuffer | Reduce the buffering on the input stream. |

## Etag probes through the interface `EtagSource`

FileSystem implementations MAY support querying HTTP etags from `FileStatus` entries. If so, the requirements are as follows

### Etag support MUST BE across all list/`getFileStatus()` calls.

That is: when adding etag support, all operations which return `FileStatus` or `ListLocatedStatus` entries MUST return subclasses which are instances of `EtagSource`.

### FileStatus instances MUST have etags whenever the remote store provides them.

To support etags, they MUST BE to be provided in both `getFileStatus()` and list calls.

Implementors note: the core APIs which MUST BE overridden to achieve this are as follows:

```
FileStatus getFileStatus(Path)
FileStatus[] listStatus(Path)
RemoteIterator<FileStatus> listStatusIterator(Path)
RemoteIterator<LocatedFileStatus> listFiles([Path, boolean)
```

### Etags of files MUST BE Consistent across all list/getFileStatus operations.

The value of `EtagSource.getEtag()` MUST be the same for list\* queries which return etags for calls of `getFileStatus()` for the specific object.

```
((EtagSource)getFileStatus(path)).getEtag() == ((EtagSource)listStatus(path)[0]).getEtag()
```

Similarly, the same value MUST BE returned for `listFiles()`, `listStatusIncremental()` of the path and when listing the parent path, of all files in the listing.

### Etags MUST BE different for different file contents.

Two different arrays of data written to the same path MUST have different etag values when probed. This is a requirement of the HTTP specification.

### Etags of files SHOULD BE preserved across rename operations

After a file is renamed, the value of `((EtagSource)getFileStatus(dest)).getEtag()` SHOULD be the same as the value of `((EtagSource)getFileStatus(source)).getEtag()` was before the rename took place.

This is an implementation detail of the store; it does not hold for AWS S3.

If and only if the store consistently meets this requirement, the filesystem SHOULD declare in `hasPathCapability()` that it supports `fs.capability.etags.preserved.in.rename`

### Directories MAY have etags

Directory entries MAY return etags in listing/probe operations; these entries MAY be preserved across renames.

Equally, directory entries MAY NOT provide such entries, MAY NOT preserve them acrosss renames, and MAY NOT guarantee consistency over time.

Note: special mention of the root path “/”. As that isn’t a real “directory”, nobody should expect it to have an etag.

### All etag-aware `FileStatus` subclass MUST BE `Serializable`; MAY BE `Writable`

The base `FileStatus` class implements `Serializable` and `Writable` and marshalls its fields appropriately.

Subclasses MUST support java serialization (Some Apache Spark applications use it), preserving the etag. This is a matter of making the etag field non-static and adding a `serialVersionUID`.

The `Writable` support was used for marshalling status data over Hadoop IPC calls; in Hadoop 3 that is implemented through `org/apache/hadoop/fs/protocolPB/PBHelper.java`and the methods deprecated. Subclasses MAY override the deprecated methods to add etag marshalling. However -but there is no expectation of this and such marshalling is unlikely to ever take place.

### Appropriate etag Path Capabilities SHOULD BE declared

1. `hasPathCapability(path, "fs.capability.etags.available")` MUST return true iff the filesystem returns valid (non-empty etags) on file status/listing operations.
2. `hasPathCapability(path, "fs.capability.etags.consistent.across.rename")` MUST return true if and only if etags are preserved across renames.

### Non-requirements of etag support

* There is no requirement/expectation that `FileSystem.getFileChecksum(Path)` returns a checksum value related to the etag of an object, if any value is returned.
* If the same data is uploaded to the twice to the same or a different path, the etag of the second upload MAY NOT match that of the first upload.

---
* [Introduction](#Introduction)
* [How data is written to a filesystem](#How_data_is_written_to_a_filesystem)
* [Output Stream Model](#Output_Stream_Model)
  * * [Visibility of Flushed Data](#Visibility_of_Flushed_Data)
  * [State of Stream and File System after Filesystem.create()](#State_of_Stream_and_File_System_after_Filesystem.create.28.29)
  * [State of Stream and File System after Filesystem.append()](#State_of_Stream_and_File_System_after_Filesystem.append.28.29)
    * [Persisting data](#Persisting_data)
* [Class FSDataOutputStream](#Class_FSDataOutputStream)
* [Class java.io.OutputStream](#Class_java.io.OutputStream)
  * [write(Stream, data)](#write.28Stream.2C_data.29)
    * [Preconditions](#Preconditions)
    * [Postconditions](#Postconditions)
  * [write(Stream, byte[] data, int offset, int len)](#write.28Stream.2C_byte.5B.5D_data.2C_int_offset.2C_int_len.29)
    * [Preconditions](#Preconditions)
    * [Postconditions](#Postconditions)
  * [write(byte[] data)](#write.28byte.5B.5D_data.29)
  * [flush()](#flush.28.29)
    * [Preconditions](#Preconditions)
    * [Postconditions](#Postconditions)
  * [close()](#close.28.29)
  * [HDFS and OutputStream.close()](#HDFS_and_OutputStream.close.28.29)
* [org.apache.hadoop.fs.Syncable](#org.apache.hadoop.fs.Syncable)
  * [Syncable.hflush()](#Syncable.hflush.28.29)
    * [Preconditions](#Preconditions)
    * [Postconditions](#Postconditions)
    * [hflush() Performance](#hflush.28.29_Performance)
  * [Syncable.hsync()](#Syncable.hsync.28.29)
    * [Preconditions](#Preconditions)
    * [Postconditions](#Postconditions)
* [Interface StreamCapabilities](#Interface_StreamCapabilities)
* [interface CanSetDropBehind](#interface_CanSetDropBehind)
* [Durability, Concurrency, Consistency and Visibility of stream output.](#Durability.2C_Concurrency.2C_Consistency_and_Visibility_of_stream_output.)
  * [Durability](#Durability)
  * [Concurrency](#Concurrency)
  * [Consistency and Visibility](#Consistency_and_Visibility)
* [Issues with the Hadoop Output Stream model.](#Issues_with_the_Hadoop_Output_Stream_model.)
  * [HDFS](#HDFS)
    * [HDFS: hsync() only syncs the latest block](#HDFS:_hsync.28.29_only_syncs_the_latest_block)
    * [HDFS: delayed visibility of metadata updates.](#HDFS:_delayed_visibility_of_metadata_updates.)
  * [Local Filesystem, file:](#Local_Filesystem.2C_file:)
  * [Checksummed output streams](#Checksummed_output_streams)
  * [Object Stores](#Object_Stores)
    * [Visibility of newly created objects](#Visibility_of_newly_created_objects)
    * [Visibility of the output of a stream after close()](#Visibility_of_the_output_of_a_stream_after_close.28.29)
* [Implementors notes.](#Implementors_notes.)
  * [Always implement Syncable -even if just to throw UnsupportedOperationException](#Always_implement_Syncable_-even_if_just_to_throw_UnsupportedOperationException)
  * [StreamCapabilities](#StreamCapabilities)
  * [Metadata updates](#Metadata_updates)
  * [Does close() synchronize and persist data?](#Does_close.28.29_synchronize_and_persist_data.3F)

# Output: `OutputStream`, `Syncable` and `StreamCapabilities`

## Introduction

This document covers the Output Streams within the context of the [Hadoop File System Specification](index.html).

It uses the filesystem model defined in [A Model of a Hadoop Filesystem](model.html) with the notation defined in [notation](Notation.html).

The target audiences are: 1. Users of the APIs. While `java.io.OutputStream` is a standard interfaces, this document clarifies how it is implemented in HDFS and elsewhere. The Hadoop-specific interfaces `Syncable` and `StreamCapabilities` are new; `Syncable` is notable in offering durability and visibility guarantees which exceed that of `OutputStream`. 1. Implementors of File Systems and clients.

## How data is written to a filesystem

The core mechanism to write data to files through the Hadoop FileSystem APIs is through `OutputStream` subclasses obtained through calls to `FileSystem.create()`, `FileSystem.append()`, or `FSDataOutputStreamBuilder.build()`.

These all return instances of `FSDataOutputStream`, through which data can be written through various `write()` methods. After a stream’s `close()` method is called, all data written to the stream MUST BE persisted to the filesystem and visible to oll other clients attempting to read data from that path via `FileSystem.open()`.

As well as operations to write the data, Hadoop’s `OutputStream` implementations provide methods to flush buffered data back to the filesystem, so as to ensure that the data is reliably persisted and/or visible to other callers. This is done via the `Syncable` interface. It was originally intended that the presence of this interface could be interpreted as a guarantee that the stream supported its methods. However, this has proven impossible to guarantee as the static nature of the interface is incompatible with filesystems whose syncability semantics may vary on a store/path basis. As an example, erasure coded files in HDFS do not support the Sync operations, even though they are implemented as subclass of an output stream which is `Syncable`.

A new interface: `StreamCapabilities`. This allows callers to probe the exact capabilities of a stream, even transitively through a chain of streams.

## Output Stream Model

For this specification, an output stream can be viewed as a list of bytes stored in the client; `hsync()` and `hflush()` are operations the actions which propagate the data to be visible to other readers of the file and/or made durable.

```
buffer: List[byte]
```

A flag, `open` tracks whether the stream is open: after the stream is closed no more data may be written to it:

```
open: bool
buffer: List[byte]
```

The destination path of the stream, `path`, can be tracked to form a triple `path, open, buffer`

```
Stream = (path: Path, open: Boolean, buffer: byte[])
```

#### Visibility of Flushed Data

(Immediately) after `Syncable` operations which flush data to the filesystem, the data at the stream’s destination path MUST match that of `buffer`. That is, the following condition MUST hold:

```
FS'.Files(path) == buffer
```

Any client reading the data at the path MUST see the new data. The `Syncable` operations differ in their durability guarantees, not visibility of data.

### State of Stream and File System after `Filesystem.create()`

The output stream returned by a `FileSystem.create(path)` or `FileSystem.createFile(path).build()` within a filesystem `FS`, can be modeled as a triple containing an empty array of no data:

```
Stream' = (path, true, [])
```

The filesystem `FS'` MUST contain a 0-byte file at the path:

```
FS' = FS where data(FS', path) == []
```

Thus, the initial state of `Stream'.buffer` is implicitly consistent with the data at the filesystem.

*Object Stores*: see caveats in the “Object Stores” section below.

### State of Stream and File System after `Filesystem.append()`

The output stream returned from a call of `FileSystem.append(path, buffersize, progress)` within a filesystem `FS`, can be modelled as a stream whose `buffer` is initialized to that of the original file:

```
Stream' = (path, true, data(FS, path))
```

#### Persisting data

When the stream writes data back to its store, be it in any supported flush operation, in the `close()` operation, or at any other time the stream chooses to do so, the contents of the file are replaced with the current buffer

```
Stream' = (path, true, buffer)
FS' = FS where data(FS', path) == buffer
```

After a call to `close()`, the stream is closed for all operations other than `close()`; they MAY fail with `IOException` or `RuntimeException`.

```
Stream' = (path, false, [])
```

The `close()` operation MUST be idempotent with the sole attempt to write the data made in the first invocation.

1. If `close()` succeeds, subsequent calls are no-ops.
2. If `close()` fails, again, subsequent calls are no-ops. They MAY rethrow the previous exception, but they MUST NOT retry the write.

## Class `FSDataOutputStream`

```
public class FSDataOutputStream
  extends DataOutputStream
  implements Syncable, CanSetDropBehind, StreamCapabilities {
 // ...
}
```

The `FileSystem.create()`, `FileSystem.append()` and `FSDataOutputStreamBuilder.build()` calls return an instance of a class `FSDataOutputStream`, a subclass of `java.io.OutputStream`.

The base class wraps an `OutputStream` instance, one which may implement `Syncable`, `CanSetDropBehind` and `StreamCapabilities`.

This document covers the requirements of such implementations.

HDFS’s `FileSystem` implementation, `DistributedFileSystem`, returns an instance of `HdfsDataOutputStream`. This implementation has at least two behaviors which are not explicitly declared by the base Java implementation

1. Writes are synchronized: more than one thread can write to the same output stream. This is a use pattern which HBase relies on.
2. `OutputStream.flush()` is a no-op when the file is closed. Apache Druid has made such a call on this in the past [HADOOP-14346](https://issues.apache.org/jira/browse/HADOOP-14346).

As the HDFS implementation is considered the de-facto specification of the FileSystem APIs, the fact that `write()` is thread-safe is significant.

For compatibility, not only SHOULD other FS clients be thread-safe, but new HDFS features, such as encryption and Erasure Coding SHOULD also implement consistent behavior with the core HDFS output stream.

Put differently:

*It isn’t enough for Output Streams to implement the core semantics of `java.io.OutputStream`: they need to implement the extra semantics of `HdfsDataOutputStream`, especially for HBase to work correctly.*

The concurrent `write()` call is the most significant tightening of the Java specification.

## Class `java.io.OutputStream`

A Java `OutputStream` allows applications to write a sequence of bytes to a destination. In a Hadoop filesystem, that destination is the data under a path in the filesystem.

```
public abstract class OutputStream implements Closeable, Flushable {
  public abstract void write(int b) throws IOException;
  public void write(byte b[]) throws IOException;
  public void write(byte b[], int off, int len) throws IOException;
  public void flush() throws IOException;
  public void close() throws IOException;
}
```

### `write(Stream, data)`

Writes a byte of data to the stream.

#### Preconditions

```
Stream.open else raise ClosedChannelException, PathIOException, IOException
```

The exception `java.nio.channels.ClosedChannelExceptionn` is raised in the HDFS output streams when trying to write to a closed file. This exception does not include the destination path; and `Exception.getMessage()` is `null`. It is therefore of limited value in stack traces. Implementors may wish to raise exceptions with more detail, such as a `PathIOException`.

#### Postconditions

The buffer has the lower 8 bits of the data argument appended to it.

```
Stream'.buffer = Stream.buffer + [data & 0xff]
```

There may be an explicit limit on the size of cached data, or an implicit limit based by the available capacity of the destination filesystem. When a limit is reached, `write()` SHOULD fail with an `IOException`.

### `write(Stream, byte[] data, int offset, int len)`

#### Preconditions

The preconditions are all defined in `OutputStream.write()`

```
Stream.open else raise ClosedChannelException, PathIOException, IOException
data != null else raise NullPointerException
offset >= 0 else raise IndexOutOfBoundsException
len >= 0 else raise IndexOutOfBoundsException
offset < data.length else raise IndexOutOfBoundsException
offset + len < data.length else raise IndexOutOfBoundsException
```

After the operation has returned, the buffer may be re-used. The outcome of updates to the buffer while the `write()` operation is in progress is undefined.

#### Postconditions

```
Stream'.buffer = Stream.buffer + data[offset...(offset + len)]
```

### `write(byte[] data)`

This is defined as the equivalent of:

```
write(data, 0, data.length)
```

### `flush()`

Requests that the data is flushed. The specification of `ObjectStream.flush()` declares that this SHOULD write data to the “intended destination”.

It explicitly precludes any guarantees about durability.

For that reason, this document doesn’t provide any normative specifications of behaviour.

#### Preconditions

None.

#### Postconditions

None.

If the implementation chooses to implement a stream-flushing operation, the data may be saved to the file system such that it becomes visible to others"

```
FS' = FS where data(FS', path) == buffer
```

When a stream is closed, `flush()` SHOULD downgrade to being a no-op, if it was not one already. This is to work with applications and libraries which can invoke it in exactly this way.

*Issue*: Should `flush()` forward to `hflush()`?

No. Or at least, make it optional.

There’s a lot of application code which assumes that `flush()` is low cost and should be invoked after writing every single line of output, after writing small 4KB blocks or similar.

Forwarding this to a full flush across a distributed filesystem, or worse, a distant object store, is very inefficient. Filesystem clients which convert a `flush()` to an `hflush()` will eventually have to roll back that feature: [HADOOP-16548](https://issues.apache.org/jira/browse/HADOOP-16548).

### `close()`

The `close()` operation saves all data to the filesystem and releases any resources used for writing data.

The `close()` call is expected to block until the write has completed (as with `Syncable.hflush()`), possibly until it has been written to durable storage.

After `close()` completes, the data in a file MUST be visible and consistent with the data most recently written. The metadata of the file MUST be consistent with the data and the write history itself (i.e. any modification time fields updated).

After `close()` is invoked, all subsequent `write()` calls on the stream MUST fail with an `IOException`.

Any locking/leaseholding mechanism MUST release its lock/lease.

```
Stream'.open = false
FS' = FS where data(FS', path) == buffer
```

The `close()` call MAY fail during its operation.

1. Callers of the API MUST expect for some calls to `close()` to fail and SHOULD code appropriately. Catching and swallowing exceptions, while common, is not always the ideal solution.
2. Even after a failure, `close()` MUST place the stream into a closed state. Follow-on calls to `close()` are ignored, and calls to other methods rejected. That is: caller’s cannot be expected to call `close()` repeatedly until it succeeds.
3. The duration of the `close()` operation is undefined. Operations which rely on acknowledgements from remote systems to meet the persistence guarantees implicitly have to await these acknowledgements. Some Object Store output streams upload the entire data file in the `close()` operation. This can take a large amount of time. The fact that many user applications assume that `close()` is both fast and does not fail means that this behavior is dangerous.

Recommendations for safe use by callers

* Do plan for exceptions being raised, either in catching and logging or by throwing the exception further up. Catching and silently swallowing exceptions may hide serious problems.
* Heartbeat operations SHOULD take place on a separate thread, so that a long delay in `close()` does not block the thread so long that the heartbeat times out.

Implementors:

* Have a look at [HADOOP-16785](https://issues.apache.org/jira/browse/HADOOP-16785) to see examples of complications in close.
* Incrementally writing blocks before a close operation results in a behavior which matches client expectations better: write failures to surface earlier and close to be more housekeeping than the actual upload.
* If block uploads are executed in separate threads, the output stream `close()` call MUST block until all the asynchronous uploads have completed; any error raised MUST be reported. If multiple errors were raised, the stream can choose which to propagate. What is important is: when `close()` returns without an error, applications expect the data to have been successfully written.

### HDFS and `OutputStream.close()`

HDFS does not immediately `sync()` the output of a written file to disk on `OutputStream.close()` unless configured with `dfs.datanode.synconclose` is true. This has caused [problems in some applications](https://issues.apache.org/jira/browse/ACCUMULO-1364).

Applications which absolutely require the guarantee that a file has been persisted MUST call `Syncable.hsync()` *before* the file is closed.

## `org.apache.hadoop.fs.Syncable`

```
@InterfaceAudience.Public
@InterfaceStability.Stable
public interface Syncable {


  /** Flush out the data in client's user buffer. After the return of
   * this call, new readers will see the data.
   * @throws IOException if any error occurs
   */
  void hflush() throws IOException;

  /** Similar to posix fsync, flush out the data in client's user buffer
   * all the way to the disk device (but the disk may have it in its cache).
   * @throws IOException if error occurs
   */
  void hsync() throws IOException;
}
```

The purpose of `Syncable` interface is to provide guarantees that data is written to a filesystem for both visibility and durability.

*SYNC-1*: An `OutputStream` which implements `Syncable` and does not raise `UnsupportedOperationException` on invocations is making an explicit declaration that it can meet those guarantees.

*SYNC-2*: If a stream, declares the interface as implemented, but does not provide durability, the interface’s methods MUST raise `UnsupportedOperationException`.

The `Syncable` interface has been implemented by other classes than subclasses of `OutputStream`, such as `org.apache.hadoop.io.SequenceFile.Writer`.

*SYNC-3* The fact that a class implements `Syncable` does not guarantee that `extends OutputStream` holds.

That is, for any class `C`: `(C instanceof Syncable)` does not imply `(C instanceof OutputStream)`

This specification only covers the required behavior of `OutputStream` subclasses which implement `Syncable`.

*SYNC-4:* The return value of `FileSystem.create(Path)` is an instance of `FSDataOutputStream`.

*SYNC-5:* `FSDataOutputStream implements Syncable`

SYNC-5 and SYNC-1 imply that all output streams which can be created with `FileSystem.create(Path)` must support the semantics of `Syncable`. This is demonstrably not true: `FSDataOutputStream` simply downgrades to a `flush()` if its wrapped stream is not `Syncable`. Therefore the declarations SYNC-1 and SYNC-2 do not hold: you cannot trust `Syncable`.

Put differently: *callers MUST NOT rely on the presence of the interface as evidence that the semantics of `Syncable` are supported*. Instead they MUST be dynamically probed for using the `StreamCapabilities` interface, where available.

### `Syncable.hflush()`

Flush out the data in client’s user buffer. After the return of this call, new readers will see the data. The `hflush()` operation does not contain any guarantees as to the durability of the data. only its visibility.

Thus implementations may cache the written data in memory —visible to all, but not yet persisted.

#### Preconditions

```
hasCapability(Stream, "hflush")
Stream.open else raise IOException
```

#### Postconditions

```
FS' = FS where data(path) == cache
```

After the call returns, the data MUST be visible to all new callers of `FileSystem.open(path)` and `FileSystem.openFile(path).build()`.

There is no requirement or guarantee that clients with an existing `DataInputStream` created by a call to `(FS, path)` will see the updated data, nor is there a guarantee that they *will not* in a current or subsequent read.

Implementation note: as a correct `hsync()` implementation MUST also offer all the semantics of an `hflush()` call, implementations of `hflush()` may just invoke `hsync()`:

```
public void hflush() throws IOException {
  hsync();
}
```

#### `hflush()` Performance

The `hflush()` call MUST block until the store has acknowledge that the data has been received and is now visible to others. This can be slow, as it will include the time to upload any outstanding data from the client, and for the filesystem itself to process it.

Often Filesystems only offer the `Syncable.hsync()` guarantees: persistence as well as visibility. This means the time to return can be even greater.

Application code MUST NOT call `hflush()` or `hsync()` at the end of every line or, unless they are writing a WAL, at the end of every record. Use with care.

### `Syncable.hsync()`

Similar to POSIX `fsync()`, this call saves the data in client’s user buffer all the way to the disk device (but the disk may have it in its cache).

That is: it is a requirement for the underlying FS To save all the data to the disk hardware itself, where it is expected to be durable.

#### Preconditions

```
hasCapability(Stream, "hsync")
Stream.open else raise IOException
```

#### Postconditions

```
FS' = FS where data(path) == buffer
```

*Implementations are required to block until that write has been acknowledged by the store.*

This is so the caller can be confident that once the call has returned successfully, the data has been written.

## Interface `StreamCapabilities`

```
@InterfaceAudience.Public
@InterfaceStability.Evolving
```

The `org.apache.hadoop.fs.StreamCapabilities` interface exists to allow callers to dynamically determine the behavior of a stream.

```
  public boolean hasCapability(String capability) {
    switch (capability.toLowerCase(Locale.ENGLISH)) {
      case StreamCapabilities.HSYNC:
      case StreamCapabilities.HFLUSH:
        return supportFlush;
      default:
        return false;
    }
  }
```

Once a stream has been closed, a `hasCapability()` call MUST do one of

* return the capabilities of the open stream.
* return false.

That is: it MUST NOT raise an exception about the file being closed;

See [pathcapabilities](pathcapabilities.html) for specifics on the `PathCapabilities` API; the requirements are similar: a stream MUST NOT return true for a capability for which it lacks support, be it because

* The capability is unknown.
* The capability is known and known to be unsupported.

Standard stream capabilities are defined in `StreamCapabilities`; consult the javadocs for the complete set of options.

| Name | Probes for support of |
| --- | --- |
| `dropbehind` | `CanSetDropBehind.setDropBehind()` |
| `hsync` | `Syncable.hsync()` |
| `hflush` | `Syncable.hflush()`. Deprecated: probe for `HSYNC` only. |
| `in:readahead` | `CanSetReadahead.setReadahead()` |
| `in:unbuffer"` | `CanUnbuffer.unbuffer()` |
| `in:readbytebuffer` | `ByteBufferReadable#read(ByteBuffer)` |
| `in:preadbytebuffer` | `ByteBufferPositionedReadable#read(long, ByteBuffer)` |

Stream implementations MAY add their own custom options. These MUST be prefixed with `fs.SCHEMA.`, where `SCHEMA` is the schema of the filesystem.

## interface `CanSetDropBehind`

```
@InterfaceAudience.Public
@InterfaceStability.Evolving
public interface CanSetDropBehind {
  /**
   * Configure whether the stream should drop the cache.
   *
   * @param dropCache     Whether to drop the cache.  null means to use the
   *                      default value.
   * @throws IOException  If there was an error changing the dropBehind
   *                      setting.
   *         UnsupportedOperationException  If this stream doesn't support
   *                                        setting the drop-behind.
   */
  void setDropBehind(Boolean dropCache)
      throws IOException, UnsupportedOperationException;
}
```

This interface allows callers to change policies used inside HDFS.

Implementations MUST return `true` for the call

```
StreamCapabilities.hasCapability("dropbehind");
```

## Durability, Concurrency, Consistency and Visibility of stream output.

These are the aspects of the system behaviour which are not directly covered in this (very simplistic) filesystem model, but which are visible in production.

### Durability

1. `OutputStream.write()` MAY persist the data, synchronously or asynchronously
2. `OutputStream.flush()` flushes data to the destination. There are no strict persistence requirements.
3. `Syncable.hflush()` synchronously sends all outstanding data to the destination filesystem. After returning to the caller, the data MUST be visible to other readers, it MAY be durable. That is: it does not have to be persisted, merely guaranteed to be consistently visible to all clients attempting to open a new stream reading data at the path.
4. `Syncable.hsync()` MUST transmit the data as per `hflush` and persist that data to the underlying durable storage.
5. `close()` The first call to `close()` MUST flush out all remaining data in the buffers, and persist it, as a call to `hsync()`.

Many applications call `flush()` far too often -such as at the end of every line written. If this triggered an update of the data in persistent storage and any accompanying metadata, distributed stores would overload fast. Thus: `flush()` is often treated at most as a cue to flush data to the network buffers -but not commit to writing any data.

It is only the `Syncable` interface which offers guarantees.

The two `Syncable` operations `hsync()` and `hflush()` differ purely by the extra guarantee of `hsync()`: the data must be persisted. If `hsync()` is implemented, then `hflush()` can be implemented simply by invoking `hsync()`

```
public void hflush() throws IOException {
  hsync();
}
```

This is perfectly acceptable as an implementation: the semantics of `hflush()` are satisfied. What is not acceptable is downgrading `hsync()` to `hflush()`, as the durability guarantee is no longer met.

### Concurrency

1. The outcome of more than one process writing to the same file is undefined.
2. An input stream opened to read a file *before the file was opened for writing* MAY fetch data updated by writes to an OutputStream. Because of buffering and caching, this is not a requirement —and if an input stream does pick up updated data, the point at which the updated data is read is undefined. This surfaces in object stores where a `seek()` call which closes and re-opens the connection may pick up updated data, while forward stream reads do not. Similarly, in block-oriented filesystems, the data may be cached a block at a time —and changes only picked up when a different block is read.
3. A filesystem MAY allow the destination path to be manipulated while a stream is writing to it —for example, `rename()` of the path or a parent; `delete()` of a path or parent. In such a case, the outcome of future write operations on the output stream is undefined. Some filesystems MAY implement locking to prevent conflict. However, this tends to be rare on distributed filesystems, for reasons well known in the literature.
4. The Java API specification of `java.io.OutputStream` does not require an instance of the class to be thread safe. However, `org.apache.hadoop.hdfs.DFSOutputStream` has a stronger thread safety model (possibly unintentionally). This fact is relied upon in Apache HBase, as discovered in HADOOP-11708. Implementations SHOULD be thread safe. *Note*: even the `DFSOutputStream` synchronization model permits the output stream to have `close()` invoked while awaiting an acknowledgement from datanode or namenode writes in an `hsync()` operation.

### Consistency and Visibility

There is no requirement for the data to be immediately visible to other applications —not until a specific call to flush buffers or persist it to the underlying storage medium are made.

If an output stream is created with `FileSystem.create(path, overwrite==true)` and there is an existing file at the path, that is `exists(FS, path)` holds, then, the existing data is immediately unavailable; the data at the end of the path MUST consist of an empty byte sequence `[]`, with consistent metadata.

```
exists(FS, path)
(Stream', FS') = create(FS, path)
exists(FS', path)
getFileStatus(FS', path).getLen() = 0
```

The metadata of a file (`length(FS, path)` in particular) SHOULD be consistent with the contents of the file after `flush()` and `sync()`.

```
(Stream', FS') = create(FS, path)
(Stream'', FS'') = write(Stream', data)
(Stream''', FS''') hsync(Stream'')
exists(FS''', path)
getFileStatus(FS''', path).getLen() = len(data)
```

*HDFS does not do this except when the write crosses a block boundary*; to do otherwise would overload the Namenode. Other stores MAY copy this behavior.

As a result, while a file is being written `length(Filesystem, Path)` MAY be less than the length of `data(Filesystem, Path)`.

The metadata MUST be consistent with the contents of a file after the `close()` operation.

After the contents of an output stream have been persisted (`hflush()/hsync()`) all new `open(FS, Path)` operations MUST return the updated data.

After `close()` has been invoked on an output stream, a call to `getFileStatus(path)` MUST return the final metadata of the written file, including length and modification time. The metadata of the file returned in any of the FileSystem `list` operations MUST be consistent with this metadata.

The value of `getFileStatus(path).getModificationTime()` is not defined while a stream is being written to. The timestamp MAY be updated while a file is being written, especially after a `Syncable.hsync()` call. The timestamps MUST be updated after the file is closed to that of a clock value observed by the server during the `close()` call. It is *likely* to be in the time and time zone of the filesystem, rather than that of the client.

Formally, if a `close()` operation triggers an interaction with a server which starts at server-side time `t1` and completes at time `t2` with a successfully written file, then the last modification time SHOULD be a time `t` where `t1 <= t <= t2`

## Issues with the Hadoop Output Stream model.

There are some known issues with the output stream model as offered by Hadoop, specifically about the guarantees about when data is written and persisted —and when the metadata is synchronized. These are where implementation aspects of HDFS and the “Local” filesystem do not follow the simple model of the filesystem used in this specification.

### HDFS

#### HDFS: `hsync()` only syncs the latest block

The reference implementation, `DFSOutputStream` will block until an acknowledgement is received from the datanodes: that is, all hosts in the replica write chain have successfully written the file.

That means that the expectation callers may have is that the return of the method call contains visibility and durability guarantees which other implementations must maintain.

Note, however, that the reference `DFSOutputStream.hsync()` call only actually persists *the current block*. If there have been a series of writes since the last sync, such that a block boundary has been crossed. The `hsync()` call claims only to write the most recent.

From the javadocs of `DFSOutputStream.hsync(EnumSet<SyncFlag> syncFlags)`

> Note that only the current block is flushed to the disk device. To guarantee durable sync across block boundaries the stream should be created with {@link CreateFlag#SYNC\_BLOCK}.

This is an important HDFS implementation detail which must not be ignored by anyone relying on HDFS to provide a Write-Ahead-Log or other database structure where the requirement of the application is that “all preceeding bytes MUST have been persisted before the commit flag in the WAL is flushed”

See [Stonebraker81], Michael Stonebraker, *Operating System Support for Database Management*, 1981, for a discussion on this topic.

If you do need `hsync()` to have synced every block in a very large write, call it regularly.

#### HDFS: delayed visibility of metadata updates.

That HDFS file metadata often lags the content of a file being written to is not something everyone expects, nor convenient for any program trying to pick up updated data in a file being written. Most visible is the length of a file returned in the various `list` commands and `getFileStatus` —this is often out of date.

As HDFS only supports file growth in its output operations, this means that the size of the file as listed in the metadata may be less than or equal to the number of available bytes —but never larger. This is a guarantee which is also held

One algorithm to determine whether a file in HDFS is updated is:

1. Remember the last read position `pos` in the file, using `0` if this is the initial read.
2. Use `getFileStatus(FS, Path)` to query the updated length of the file as recorded in the metadata.
3. If `Status.length &gt; pos`, the file has grown.
4. If the number has not changed, then
   1. Reopen the file.
   2. `seek(pos)` to that location
   3. If `read() != -1`, there is new data.

This algorithm works for filesystems which are consistent with metadata and data, as well as HDFS. What is important to know is that, for an open file `getFileStatus(FS, path).getLen() == 0` does not imply that `data(FS, path)` is empty.

When an output stream in HDFS is closed; the newly written data is not immediately written to disk unless HDFS is deployed with `dfs.datanode.synconclose` set to true. Otherwise it is cached and written to disk later.

### Local Filesystem, `file:`

`LocalFileSystem`, `file:`, (or any other `FileSystem` implementation based on `ChecksumFileSystem`) has a different issue. If an output stream is obtained from `create()` and `FileSystem.setWriteChecksum(false)` has *not* been called on the filesystem, then the stream only flushes as much local data as can be written to full checksummed blocks of data.

That is, the hsync/hflush operations are not guaranteed to write all the pending data until the file is finally closed.

For this reason, the local filesystem accessed via `file://` URLs does not support `Syncable` unless `setWriteChecksum(false)` was called on that FileSystem instance so as to disable checksum creation. After which, obviously, checksums are not generated for any file. Is

### Checksummed output streams

Because `org.apache.hadoop.fs.FSOutputSummer` and `org.apache.hadoop.fs.ChecksumFileSystem.ChecksumFSOutputSummer` implement the underlying checksummed output stream used by HDFS and other filesystems, it provides some of the core semantics of the output stream behavior.

1. The `close()` call is unsynchronized, re-entrant and may attempt to close the stream more than once.
2. It is possible to call `write(int)` on a closed stream (but not `write(byte[], int, int)`).
3. It is possible to call `flush()` on a closed stream.

Behaviors 1 and 2 really have to be considered bugs to fix, albeit with care.

Behavior 3 has to be considered a defacto standard, for other implementations to copy.

### Object Stores

Object store streams MAY buffer the entire stream’s output until the final `close()` operation triggers a single `PUT` of the data and materialization of the final output.

This significantly changes their behaviour compared to that of POSIX filesystems and that specified in this document.

#### Visibility of newly created objects

There is no guarantee that any file will be visible at the path of an output stream after the output stream is created .

That is: while `create(FS, path, boolean)` returns a new stream

```
Stream' = (path, true, [])
```

The other postcondition of the operation, `data(FS', path) == []` MAY NOT hold, in which case:

1. `exists(FS, p)` MAY return false.
2. If a file was created with `overwrite = True`, the existing data MAY still be visible: `data(FS', path) = data(FS, path)`.
3. The check for existing data in a `create()` call with `overwrite=False`, may take place in the `create()` call itself, in the `close()` call prior to/during the write, or at some point in between. In the special case that the object store supports an atomic `PUT` operation, the check for existence of existing data and the subsequent creation of data at the path contains a race condition: other clients may create data at the path between the existence check and the subsequent write.
4. Calls to `create(FS, Path, overwrite=false)` MAY succeed, returning a new `OutputStream`, even while another stream is open and writing to the destination path.

This allows for the following sequence of operations, which would raise an exception in the second `open()` call if invoked against HDFS:

```
Stream1 = open(FS, path, false)
sleep(200)
Stream2 = open(FS, path, false)
Stream.write('a')
Stream1.close()
Stream2.close()
```

For anyone wondering why the clients don’t create a 0-byte file in the `create()` call, it would cause problems after `close()` —the marker file could get returned in `open()` calls instead of the final data.

#### Visibility of the output of a stream after `close()`

One guarantee which Object Stores SHOULD make is the same as those of POSIX filesystems: After a stream `close()` call returns, the data MUST be persisted durably and visible to all callers. Unfortunately, even that guarantee is not always met:

1. Existing data on a path MAY be visible for an indeterminate period of time.
2. If the store has any form of create inconsistency or buffering of negative existence probes, then even after the stream’s `close()` operation has returned, `getFileStatus(FS, path)` and `open(FS, path)` may fail with a `FileNotFoundException`.

In their favour, the atomicity of the store’s PUT operations do offer their own guarantee: a newly created object is either absent or all of its data is present: the act of instantiating the object, while potentially exhibiting create inconsistency, is atomic. Applications may be able to use that fact to their advantage.

The [Abortable](abortable.html) interface exposes this ability to abort an output stream before its data is made visible, so can be used for checkpointing and similar operations.

## Implementors notes.

### Always implement `Syncable` -even if just to throw `UnsupportedOperationException`

Because `FSDataOutputStream` silently downgrades `Syncable.hflush()` and `Syncable.hsync()` to `wrappedStream.flush()`, callers of the API MAY be misled into believing that their data has been flushed/synced after syncing to a stream which does not support the APIs.

Implementations SHOULD implement the API but throw `UnsupportedOperationException`.

### `StreamCapabilities`

Implementors of filesystem clients SHOULD implement the `StreamCapabilities` interface and its `hasCapabilities()` method to declare whether or not an output streams offer the visibility and durability guarantees of `Syncable`.

Implementors of `StreamCapabilities.hasCapabilities()` MUST NOT declare that they support the `hflush` and `hsync` capabilities on streams where this is not true.

Sometimes streams pass their data to store, but the far end may not sync it all the way to disk. That is not something the client can determine. Here: if the client code is making the hflush/hsync passes these requests on to the distributed FS, it SHOULD declare that it supports them.

### Metadata updates

Implementors MAY NOT update a file’s metadata (length, date, …) after every `hsync()` call. HDFS doesn’t, except when the written data crosses a block boundary.

### Does `close()` synchronize and persist data?

By default, HDFS does not immediately data to disk when a stream is closed; it will be asynchronously saved to disk.

This does not mean that users do not expect it.

The behavior as implemented is similar to the write-back aspect’s of NFS’s [caching](https://docstore.mik.ua/orelly/networking_2ndEd/nfs/ch07_04.htm). `DFSClient.close()` is performing an `hflush()` to the client to upload all data to the datanodes.

1. `close()` SHALL return once the guarantees of `hflush()` are met: the data is visible to others.
2. For durability guarantees, `hsync()` MUST be called first.

---
# interface `SafeMode`

The `SafeMode` interface provides a way to perform safe mode actions and obtain the status after such actions performed to the `FileSystem`.

This is admin only interface, should be implemented accordingly when necessary to Filesystem that support safe mode, e.g. `DistributedFileSystem` (HDFS) and `ViewDistributedFileSystem`.

```
public interface SafeMode {
  default boolean setSafeMode(SafeModeAction action) throws IOException {
    return setSafeMode(action, false);
  }
  boolean setSafeMode(SafeModeAction action, boolean isChecked) throws IOException;
}
```

The goals of this interface is allow any file system implementation to share the same concept of safe mode with the following actions and states

### Safe mode actions

1. `GET`, get the safe mode status of the file system.
2. `ENTER`, enter the safe mode for the file system.
3. `LEAVE`, exit safe mode for the file system gracefully.
4. `FORCE_EXIT`, exit safe mode for the file system even if there is any ongoing data process.

### Safe mode states

1. return true, when safe mode is on.
2. return false, when safe mode is off, usually it’s the result of safe mode actions with `GET`, `LEAVE`, `FORCE_EXIT`.

---
# Introduction

* [Naming](#Naming)
* [Implicit assumptions of the Hadoop FileSystem APIs](#Implicit_assumptions_of_the_Hadoop_FileSystem_APIs)
  * [Path Names](#Path_Names)
  * [Security Assumptions](#Security_Assumptions)
  * [Networking Assumptions](#Networking_Assumptions)
* [Core Expectations of a Hadoop Compatible FileSystem](#Core_Expectations_of_a_Hadoop_Compatible_FileSystem)
  * [Atomicity](#Atomicity)
  * [Consistency](#Consistency)
  * [Concurrency](#Concurrency)
  * [Operations and failures](#Operations_and_failures)
  * [Undefined capacity limits](#Undefined_capacity_limits)
  * [Undefined timeouts](#Undefined_timeouts)
  * [Object Stores vs. Filesystems](#Object_Stores_vs._Filesystems)

This document defines the required behaviors of a Hadoop-compatible filesystem for implementors and maintainers of the Hadoop filesystem, and for users of the Hadoop FileSystem APIs

Most of the Hadoop operations are tested against HDFS in the Hadoop test suites, initially through `MiniDFSCluster`, before release by vendor-specific ‘production’ tests, and implicitly by the Hadoop stack above it.

HDFS’s actions have been modeled on POSIX filesystem behavior, using the actions and return codes of Unix filesystem actions as a reference. Even so, there are places where HDFS diverges from the expected behaviour of a POSIX filesystem.

The bundled S3A FileSystem clients make Amazon’s S3 Object Store (“blobstore”) accessible through the FileSystem API. The Azure ABFS, WASB and ADL object storage FileSystems talks to Microsoft’s Azure storage. All of these bind to object stores, which do have different behaviors, especially regarding consistency guarantees, and atomicity of operations.

The “Local” FileSystem provides access to the underlying filesystem of the platform. Its behavior is defined by the operating system and can behave differently from HDFS. Examples of local filesystem quirks include case-sensitivity, action when attempting to rename a file atop another file, and whether it is possible to `seek()` past the end of the file.

There are also filesystems implemented by third parties that assert compatibility with Apache Hadoop. There is no formal compatibility suite, and hence no way for anyone to declare compatibility except in the form of their own compatibility tests.

These documents *do not* attempt to provide a normative definition of compatibility. Passing the associated test suites *does not* guarantee correct behavior of applications.

What the test suites do define is the expected set of actions—failing these tests will highlight potential issues.

By making each aspect of the contract tests configurable, it is possible to declare how a filesystem diverges from parts of the standard contract. This is information which can be conveyed to users of the filesystem.

## Naming

This document follows RFC 2119 rules regarding the use of MUST, MUST NOT, MAY, and SHALL. MUST NOT is treated as normative.

## Implicit assumptions of the Hadoop FileSystem APIs

The original `FileSystem` class and its usages are based on an implicit set of assumptions. Chiefly, that HDFS is the underlying FileSystem, and that it offers a subset of the behavior of a POSIX filesystem (or at least the implementation of the POSIX filesystem APIs and model provided by Linux filesystems).

Irrespective of the API, it’s expected that all Hadoop-compatible filesystems present the model of a filesystem implemented in Unix:

* It’s a hierarchical directory structure with files and directories.
* Files contain zero or more bytes of data.
* You cannot put files or directories under a file.
* Directories contain zero or more files.
* A directory entry has no data itself.
* You can write arbitrary binary data to a file. When the file’s contents are read, from anywhere inside or outside of the cluster, the data is returned.
* You can store many gigabytes of data in a single file.
* The root directory, `"/"`, always exists, and cannot be renamed.
* The root directory, `"/"`, is always a directory, and cannot be overwritten by a file write operation.
* Any attempt to recursively delete the root directory will delete its contents (barring lack of permissions), but will not delete the root path itself.
* You cannot rename/move a directory under itself.
* You cannot rename/move a directory atop any existing file other than the source file itself.
* Directory listings return all the data files in the directory (i.e. there may be hidden checksum files, but all the data files are listed).
* The attributes of a file in a directory listing (e.g. owner, length) match the actual attributes of a file, and are consistent with the view from an opened file reference.
* Security: if the caller lacks the permissions for an operation, it will fail and raise an error.

### Path Names

* A Path is comprised of Path elements separated by `"/"`.
* A path element is a unicode string of 1 or more characters.
* Path element MUST NOT include the characters `":"` or `"/"`.
* Path element SHOULD NOT include characters of ASCII/UTF-8 value 0-31 .
* Path element MUST NOT be `"."` or `".."`
* Note also that the Azure blob store documents say that paths SHOULD NOT use a trailing `"."` (as their .NET URI class strips it).
* Paths are compared based on unicode code-points.
* Case-insensitive and locale-specific comparisons MUST NOT not be used.

### Security Assumptions

Except in the special section on security, this document assumes the client has full access to the FileSystem. Accordingly, the majority of items in the list do not add the qualification “assuming the user has the rights to perform the operation with the supplied parameters and paths”.

The failure modes when a user lacks security permissions are not specified.

### Networking Assumptions

This document assumes that all network operations succeed. All statements can be assumed to be qualified as *“assuming the operation does not fail due to a network availability problem”*

* The final state of a FileSystem after a network failure is undefined.
* The immediate consistency state of a FileSystem after a network failure is undefined.
* If a network failure can be reported to the client, the failure MUST be an instance of `IOException` or subclass thereof.
* The exception details SHOULD include diagnostics suitable for an experienced Java developer *or* operations team to begin diagnostics. For example, source and destination hostnames and ports on a ConnectionRefused exception.
* The exception details MAY include diagnostics suitable for inexperienced developers to begin diagnostics. For example Hadoop tries to include a reference to [ConnectionRefused](http://wiki.apache.org/hadoop/ConnectionRefused) when a TCP connection request is refused.

## Core Expectations of a Hadoop Compatible FileSystem

Here are the core expectations of a Hadoop-compatible FileSystem. Some FileSystems do not meet all these expectations; as a result, some programs may not work as expected.

### Atomicity

There are some operations that MUST be atomic. This is because they are often used to implement locking/exclusive access between processes in a cluster.

1. Creating a file. If the `overwrite` parameter is false, the check and creation MUST be atomic.
2. Deleting a file.
3. Renaming a file.
4. Renaming a directory.
5. Creating a single directory with `mkdir()`.

* Recursive directory deletion MAY be atomic. Although HDFS offers atomic recursive directory deletion, none of the other Hadoop FileSystems offer such a guarantee (including local FileSystems).

Most other operations come with no requirements or guarantees of atomicity.

### Consistency

The consistency model of a Hadoop FileSystem is *one-copy-update-semantics*; that of a traditional local POSIX filesystem. Note that even NFS relaxes some constraints about how fast changes propagate.

* *Create.* Once the `close()` operation on an output stream writing a newly created file has completed, in-cluster operations querying the file metadata and contents MUST immediately see the file and its data.
* *Update.* Once the `close()` operation on an output stream writing a newly created file has completed, in-cluster operations querying the file metadata and contents MUST immediately see the new data.
* *Delete.* once a `delete()` operation on a path other than “/” has completed successfully, it MUST NOT be visible or accessible. Specifically, `listStatus()`, `open()` ,`rename()` and `append()` operations MUST fail.
* *Delete then create.* When a file is deleted then a new file of the same name created, the new file MUST be immediately visible and its contents accessible via the FileSystem APIs.
* *Rename.* After a `rename()` has completed, operations against the new path MUST succeed; attempts to access the data against the old path MUST fail.
* The consistency semantics inside of the cluster MUST be the same as outside of the cluster. All clients querying a file that is not being actively manipulated MUST see the same metadata and data irrespective of their location.

### Concurrency

There are no guarantees of isolated access to data: if one client is interacting with a remote file and another client changes that file, the changes may or may not be visible.

### Operations and failures

* All operations MUST eventually complete, successfully or unsuccessfully.
* The time to complete an operation is undefined and may depend on the implementation and on the state of the system.
* Operations MAY throw a `RuntimeException` or subclass thereof.
* Operations SHOULD raise all network, remote, and high-level problems as an `IOException` or subclass thereof, and SHOULD NOT raise a `RuntimeException` for such problems.
* Operations SHOULD report failures by way of raised exceptions, rather than specific return codes of an operation.
* In the text, when an exception class is named, such as `IOException`, the raised exception MAY be an instance or subclass of the named exception. It MUST NOT be a superclass.
* If an operation is not implemented in a class, the implementation must throw an `UnsupportedOperationException`.
* Implementations MAY retry failed operations until they succeed. If they do this, they SHOULD do so in such a way that the *happens-before* relationship between any sequence of operations meets the consistency and atomicity requirements stated. See [HDFS-4849](https://issues.apache.org/jira/browse/HDFS-4849) for an example of this: HDFS does not implement any retry feature that could be observable by other callers.

### Undefined capacity limits

Here are some limits to FileSystem capacity that have never been explicitly defined.

1. The maximum number of files in a directory.
2. Max number of directories in a directory
3. Maximum total number of entries (files and directories) in a filesystem.
4. The maximum length of a filename under a directory (HDFS: 8000).
5. `MAX_PATH` - the total length of the entire directory tree referencing a file. Blobstores tend to stop at ~1024 characters.
6. The maximum depth of a path (HDFS: 1000 directories).
7. The maximum size of a single file.

### Undefined timeouts

Timeouts for operations are not defined at all, including:

* The maximum completion time of blocking FS operations. MAPREDUCE-972 documents how `distcp` broke on slow s3 renames.
* The timeout for idle read streams before they are closed.
* The timeout for idle write streams before they are closed.

The blocking-operation timeout is in fact variable in HDFS, as sites and clients may tune the retry parameters so as to convert filesystem failures and failovers into pauses in operation. Instead there is a general assumption that FS operations are “fast but not as fast as local FS operations”, and that the latency of data reads and writes scale with the volume of data. This assumption by client applications reveals a more fundamental one: that the filesystem is “close” as far as network latency and bandwidth is concerned.

There are also some implicit assumptions about the overhead of some operations.

1. `seek()` operations are fast and incur little or no network delays. [This does not hold on blob stores]
2. Directory list operations are fast for directories with few entries.
3. Directory list operations are fast for directories with few entries, but may incur a cost that is `O(entries)`. Hadoop 2 added iterative listing to handle the challenge of listing directories with millions of entries without buffering at the cost of consistency.
4. A `close()` of an `OutputStream` is fast, irrespective of whether or not the file operation has succeeded or not.
5. The time to delete a directory is independent of the size of the number of child entries

### Object Stores vs. Filesystems

This specification refers to *Object Stores* in places, often using the term *Blobstore*. Hadoop does provide FileSystem client classes for some of these even though they violate many of the requirements.

Consult the documentation for a specific store to determine its compatibility with specific applications and services.

*What is an Object Store?*

An object store is a data storage service, usually accessed over HTTP/HTTPS. A `PUT` request uploads an object/“Blob”; a `GET` request retrieves it; ranged `GET` operations permit portions of a blob to retrieved. To delete the object, the HTTP `DELETE` operation is invoked.

Objects are stored by name: a string, possibly with “/” symbols in them. There is no notion of a directory; arbitrary names can be assigned to objects — within the limitations of the naming scheme imposed by the service’s provider.

The object stores invariably provide an operation to retrieve objects with a given prefix; a `GET` operation on the root of the service with the appropriate query parameters.

Object stores usually prioritize availability —there is no single point of failure equivalent to the HDFS NameNode(s). They also strive for simple non-POSIX APIs: the HTTP verbs are the operations allowed.

Hadoop FileSystem clients for object stores attempt to make the stores pretend that they are a FileSystem, a FileSystem with the same features and operations as HDFS. This is —ultimately—a pretence: they have different characteristics and occasionally the illusion fails.

1. **Consistency**. Object may be *Eventually Consistent*: it can take time for changes to objects —creation, deletion and updates— to become visible to all callers. Indeed, there is no guarantee a change is immediately visible to the client which just made the change. As an example, an object `test/data1.csv` may be overwritten with a new set of data, but when a `GET test/data1.csv` call is made shortly after the update, the original data returned. Hadoop assumes that filesystems are consistent; that creation, updates and deletions are immediately visible, and that the results of listing a directory are current with respect to the files within that directory.
2. **Atomicity**. Hadoop assumes that directory `rename()` operations are atomic, as are `delete()` operations. Object store FileSystem clients implement these as operations on the individual objects whose names match the directory prefix. As a result, the changes take place a file at a time, and are not atomic. If an operation fails part way through the process, then the state of the object store reflects the partially completed operation. Note also that client code assumes that these operations are `O(1)` —in an object store they are more likely to be `O(child-entries)`.
3. **Durability**. Hadoop assumes that `OutputStream` implementations write data to their (persistent) storage on a `flush()` operation. Object store implementations save all their written data to a local file, a file that is then only `PUT` to the object store in the final `close()` operation. As a result, there is never any partial data from incomplete or failed operations. Furthermore, as the write process only starts in `close()` operation, that operation may take a time proportional to the quantity of data to upload, and inversely proportional to the network bandwidth. It may also fail —a failure that is better escalated than ignored.
4. **Authorization**. Hadoop uses the `FileStatus` class to represent core metadata of files and directories, including the owner, group and permissions. Object stores might not have a viable way to persist this metadata, so they might need to populate `FileStatus` with stub values. Even if the object store persists this metadata, it still might not be feasible for the object store to enforce file authorization in the same way as a traditional file system. If the object store cannot persist this metadata, then the recommended convention is:

   * File owner is reported as the current user.
   * File group also is reported as the current user.
   * Directory permissions are reported as 777.
   * File permissions are reported as 666.
   * File system APIs that set ownership and permissions execute successfully without error, but they are no-ops.

Object stores with these characteristics, can not be used as a direct replacement for HDFS. In terms of this specification, their implementations of the specified operations do not match those required. They are considered supported by the Hadoop development community, but not to the same extent as HDFS.

#### Timestamps

`FileStatus` entries have a modification time and an access time.

1. The exact behavior as to when these timestamps are set and whether or not they are valid varies between filesystems, and potentially between individual installations of a filesystem.
2. The granularity of the timestamps is again, specific to both a filesystem and potentially individual installations.

The HDFS filesystem does not update the modification time while it is being written to.

Specifically

* `FileSystem.create()` creation: a zero-byte file is listed; the modification time is set to the current time as seen on the NameNode.
* Writes to a file via the output stream returned in the `create()` call: the modification time *does not change*.
* When `OutputStream.close()` is called, all remaining data is written, the file closed and the NameNode updated with the final size of the file. The modification time is set to the time the file was closed.
* Opening a file for appends via an `append()` operation does not change the modification time of the file until the `close()` call is made on the output stream.
* `FileSystem.setTimes()` can be used to explicitly set the time on a file.
* When a file is renamed, its modification time is not changed, but the source and destination directories have their modification times updated.
* The rarely used operations: `FileSystem.concat()`, `createSnapshot()`, `createSymlink()` and `truncate()` all update the modification time.
* The access time granularity is set in milliseconds `dfs.namenode.access.time.precision`; the default granularity is 1 hour. If the precision is set to zero, access times are not recorded.
* If a modification or access time is not set, the value of that `FileStatus` field is 0.

Other filesystems may have different behaviors. In particular,

* Access times may or may not be supported; even if the underlying FS may support access times, the option it is often disabled for performance reasons.
* The granularity of the timestamps is an implementation-specific detail.

Object stores have an even vaguer view of time, which can be summarized as “it varies”.

* The timestamp granularity is likely to be 1 second, that being the granularity of timestamps returned in HTTP HEAD and GET requests.
* Access times are likely to be unset. That is, `FileStatus.getAccessTime() == 0`.
* The modification timestamp for a newly created file MAY be that of the `create()` call, or the actual time which the PUT request was initiated. This may be in the `FileSystem.create()` call, the final `OutputStream.close()` operation, some period in between.
* The modification time may not be updated in the `close()` call.
* The timestamp is likely to be in UTC or the TZ of the object store. If the client is in a different timezone, the timestamp of objects may be ahead or behind that of the client.
* A file’s modification time is often the same as its creation time.
* The `FileSystem.setTimes()` operation to set file timestamps *may* be ignored.
* `FileSystem.chmod()` may update modification times (example: Azure `wasb://`).
* If `FileSystem.append()` is supported, the changes and modification time are likely to only become visible after the output stream is closed.
* Out-of-band operations to data in object stores (that is: direct requests to object stores which bypass the Hadoop FileSystem APIs), may result in different timestamps being stored and/or returned.
* As the notion of a directory structure is often simulated, the timestamps of directories *may* be artificially generated —perhaps using the current system time.
* As `rename()` operations are often implemented as a COPY + DELETE, the timestamps of renamed objects may become that of the time the rename of an object was started, rather than the timestamp of the source object.
* The exact timestamp behavior may vary between different object store installations, even with the same timestore client.

Finally, note that the Apache Hadoop project cannot make any guarantees about whether the timestamp behavior of a remote object store will remain consistent over time: they are third-party services, usually accessed via third-party libraries.

The best strategy here is “experiment with the exact endpoint you intend to work with”. Furthermore, if you intend to use any caching/consistency layer, test with that feature enabled. Retest after updates to Hadoop releases, and endpoint object store updates.

---
# class `org.apache.hadoop.fs.FSDataOutputStreamBuilder`

* [Invariants](#Invariants)
* [Implementation-agnostic parameters.](#Implementation-agnostic_parameters.)
  * [FSDataOutputStreamBuilder create()](#FSDataOutputStreamBuilder_create.28.29)
  * [FSDataOutputStreamBuilder append()](#FSDataOutputStreamBuilder_append.28.29)
  * [FSDataOutputStreamBuilder overwrite(boolean overwrite)](#FSDataOutputStreamBuilder_overwrite.28boolean_overwrite.29)
  * [FSDataOutputStreamBuilder permission(FsPermission permission)](#FSDataOutputStreamBuilder_permission.28FsPermission_permission.29)
  * [FSDataOutputStreamBuilder bufferSize(int bufSize)](#FSDataOutputStreamBuilder_bufferSize.28int_bufSize.29)
  * [FSDataOutputStreamBuilder replication(short replica)](#FSDataOutputStreamBuilder_replication.28short_replica.29)
  * [FSDataOutputStreamBuilder blockSize(long size)](#FSDataOutputStreamBuilder_blockSize.28long_size.29)
  * [FSDataOutputStreamBuilder recursive()](#FSDataOutputStreamBuilder_recursive.28.29)
  * [FSDataOutputStreamBuilder progress(Progresable prog)](#FSDataOutputStreamBuilder_progress.28Progresable_prog.29)
  * [FSDataOutputStreamBuilder checksumOpt(ChecksumOpt chksumOpt)](#FSDataOutputStreamBuilder_checksumOpt.28ChecksumOpt_chksumOpt.29)
  * [Set optional or mandatory parameters](#Set_optional_or_mandatory_parameters)
* [HDFS-specific parameters.](#HDFS-specific_parameters.)
  * [FSDataOutpuStreamBuilder favoredNodes(InetSocketAddress[] nodes)](#FSDataOutpuStreamBuilder_favoredNodes.28InetSocketAddress.5B.5D_nodes.29)
  * [FSDataOutputStreamBuilder syncBlock()](#FSDataOutputStreamBuilder_syncBlock.28.29)
  * [FSDataOutputStreamBuilder lazyPersist()](#FSDataOutputStreamBuilder_lazyPersist.28.29)
  * [FSDataOutputStreamBuilder newBlock()](#FSDataOutputStreamBuilder_newBlock.28.29)
  * [FSDataOutputStreamBuilder noLocalWrite()](#FSDataOutputStreamBuilder_noLocalWrite.28.29)
  * [FSDataOutputStreamBuilder ecPolicyName()](#FSDataOutputStreamBuilder_ecPolicyName.28.29)
  * [FSDataOutputStreamBuilder replicate()](#FSDataOutputStreamBuilder_replicate.28.29)
* [Builder interface](#Builder_interface)
  * [FSDataOutputStream build()](#FSDataOutputStream_build.28.29)
* [S3A-specific options](#S3A-specific_options)
  * [fs.s3a.create.performance](#fs.s3a.create.performance)
  * [fs.s3a.create.header User-supplied header support](#fs.s3a.create.header_User-supplied_header_support)
  * [fs.s3a.create.multipart Create a multipart file](#fs.s3a.create.multipart_Create_a_multipart_file)

Builder pattern for `FSDataOutputStream` and its subclasses. It is used to create a new file or open an existing file on `FileSystem` for write.

## Invariants

The `FSDataOutputStreamBuilder` interface does not validate parameters and modify the state of `FileSystem` until `build()` is invoked.

## Implementation-agnostic parameters.

### `FSDataOutputStreamBuilder create()`

Specify `FSDataOutputStreamBuilder` to create a file on `FileSystem`, equivalent to `CreateFlag#CREATE`.

### `FSDataOutputStreamBuilder append()`

Specify `FSDataOutputStreamBuilder` to append to an existing file on `FileSystem`, equivalent to `CreateFlag#APPEND`.

### `FSDataOutputStreamBuilder overwrite(boolean overwrite)`

Specify `FSDataOutputStreamBuilder` to overwrite an existing file or not. If giving `overwrite==true`, it truncates an existing file, equivalent to `CreateFlag#OVERWITE`.

### `FSDataOutputStreamBuilder permission(FsPermission permission)`

Set permission for the file.

### `FSDataOutputStreamBuilder bufferSize(int bufSize)`

Set the size of the buffer to be used.

### `FSDataOutputStreamBuilder replication(short replica)`

Set the replication factor.

### `FSDataOutputStreamBuilder blockSize(long size)`

Set block size in bytes.

### `FSDataOutputStreamBuilder recursive()`

Create parent directories if they do not exist.

### `FSDataOutputStreamBuilder progress(Progresable prog)`

Set the facility of reporting progress.

### `FSDataOutputStreamBuilder checksumOpt(ChecksumOpt chksumOpt)`

Set checksum opt.

### Set optional or mandatory parameters

```
FSDataOutputStreamBuilder opt(String key, ...)
FSDataOutputStreamBuilder must(String key, ...)
```

Set optional or mandatory parameters to the builder. Using `opt()` or `must()`, client can specify FS-specific parameters without inspecting the concrete type of `FileSystem`.

```
// Don't
if (fs instanceof FooFileSystem) {
    FooFileSystem fs = (FooFileSystem) fs;
    out = dfs.createFile(path)
        .optionA()
        .optionB("value")
        .cache()
        .build()
} else if (fs instanceof BarFileSystem) {
    ...
}

// Do
out = fs.createFile(path)
    .permission(perm)
    .bufferSize(bufSize)
    .opt("foofs:option.a", true)
    .opt("foofs:option.b", "value")
    .opt("barfs:cache", true)
    .must("foofs:cache", true)
    .must("barfs:cache-size", 256 * 1024 * 1024)
    .build();
```

#### Implementation Notes

The concrete `FileSystem` and/or `FSDataOutputStreamBuilder` implementation MUST verify that implementation-agnostic parameters (i.e., "syncable`) or implementation-specific parameters (i.e., "foofs:cache") are supported.`FileSystem`will satisfy optional parameters (via`opt(key, …)`) on best effort. If the mandatory parameters (via`must(key, …)`) can not be satisfied in the`FileSystem`,`IllegalArgumentException`must be thrown in`build()`.

The behavior of resolving the conflicts between the parameters set by builder methods (i.e., `bufferSize()`) and `opt()`/`must()` is as follows:

> The last option specified defines the value and its optional/mandatory state.

## HDFS-specific parameters.

`HdfsDataOutputStreamBuilder extends FSDataOutputStreamBuilder` provides additional HDFS-specific parameters, for further customize file creation / append behavior.

### `FSDataOutpuStreamBuilder favoredNodes(InetSocketAddress[] nodes)`

Set favored DataNodes for new blocks.

### `FSDataOutputStreamBuilder syncBlock()`

Force closed blocks to the disk device. See `CreateFlag#SYNC_BLOCK`

### `FSDataOutputStreamBuilder lazyPersist()`

Create the block on transient storage if possible.

### `FSDataOutputStreamBuilder newBlock()`

Append data to a new block instead of the end of the last partial block.

### `FSDataOutputStreamBuilder noLocalWrite()`

Advise that a block replica NOT be written to the local DataNode.

### `FSDataOutputStreamBuilder ecPolicyName()`

Enforce the file to be a striped file with erasure coding policy ‘policyName’, no matter what its parent directory’s replication or erasure coding policy is.

### `FSDataOutputStreamBuilder replicate()`

Enforce the file to be a replicated file, no matter what its parent directory’s replication or erasure coding policy is.

## Builder interface

### `FSDataOutputStream build()`

Create a new file or append an existing file on the underlying `FileSystem`, and return `FSDataOutputStream` for write.

#### Preconditions

The following combinations of parameters are not supported:

```
if APPEND|OVERWRITE: raise HadoopIllegalArgumentException
if CREATE|APPEND|OVERWRITE: raise HadoopIllegalArgumentExdeption
```

`FileSystem` may reject the request for other reasons and throw `IOException`, see `FileSystem#create(path, ...)` and `FileSystem#append()`.

#### Postconditions

```
FS' where :
   FS'.Files'[p] == []
   ancestors(p) is-subset-of FS'.Directories'

result = FSDataOutputStream
```

The result is `FSDataOutputStream` to be used to write data to filesystem.

## S3A-specific options

Here are the custom options which the S3A Connector supports.

| Name | Type | Meaning |
| --- | --- | --- |
| `fs.s3a.create.performance` | `boolean` | create a file with maximum performance |
| `fs.s3a.create.header` | `string` | prefix for user supplied headers |
| `fs.s3a.create.multipart` | `boolean` | create a multipart file |

### `fs.s3a.create.performance`

Prioritize file creation performance over safety checks for filesystem consistency.

This: 1. Skips the `LIST` call which makes sure a file is being created over a directory. Risk: a file is created over a directory. 2. If the overwrite flag is false and filesystem flag`fs.s3a.create.conditional.enabled` is true, uses conditional creation to prevent the overwrite of any object at the destination. 3. Never issues a `DELETE` call to delete parent directory markers.

It is possible to probe an S3A Filesystem instance for this capability through the `hasPathCapability(path, "fs.s3a.create.performance")` check.

Creating files with this option over existing directories is likely to make S3A filesystem clients behave inconsistently.

Operations optimized for directories (e.g. listing calls) are likely to see the directory tree not the file; operations optimized for files (`getFileStatus()`, `isFile()`) more likely to see the file. The exact form of the inconsistencies, and which operations/parameters trigger this are undefined and may change between even minor releases.

Using this option is the equivalent of pressing and holding down the “Electronic Stability Control” button on a rear-wheel drive car for five seconds: the safety checks are off. Things wil be faster if the driver knew what they were doing. If they didn’t, the fact they had held the button down will be used as evidence at the inquest as proof that they made a conscious decision to choose speed over safety and that the outcome was their own fault.

Note: the option can be set for an entire filesystem. Again, the safety checks are there to more closely match the semantics of a classic filesystem, and to reduce the likelihood that the object store ends up in a state which diverges so much from the classic directory + tree structur that applications get confused.

Accordingly: *Use if and only if you are confident that the conditions are met.*

### `fs.s3a.create.header` User-supplied header support

Options with the prefix `fs.s3a.create.header.` will be added to the S3 object metadata as “user defined metadata”. This metadata is visible to all applications. It can also be retrieved through the FileSystem/FileContext `listXAttrs()` and `getXAttrs()` API calls with the prefix `header.`

When an object is renamed, the metadata is propagated the copy created.

It is possible to probe an S3A Filesystem instance for this capability through the `hasPathCapability(path, "fs.s3a.create.header")` check.

### `fs.s3a.create.multipart` Create a multipart file

Initiate a multipart upload when a file is created, rather than only when the amount of data buffered reaches the threshold set in `fs.s3a.multipart.size`.

This is only relevant during testing, as it allows for multipart operation to be initiated without writing any data, so reducing test time.

It is not recommended for production use, because as well as adding more network IO, it is not compatible with third-party stores which do not supprt multipart uploads.

---
# `FileSystem.openFile()`/`FileContext.openFile()`

This is a method provided by both FileSystem and FileContext for advanced file opening options and, where implemented, an asynchrounous/lazy opening of a file.

Creates a builder to open a file, supporting options both standard and filesystem specific. The return value of the `build()` call is a `Future<FSDataInputStream>`, which must be waited on. The file opening may be asynchronous, and it may actually be postponed (including permission/existence checks) until reads are actually performed.

This API call was added to `FileSystem` and `FileContext` in Hadoop 3.3.0; it was tuned in Hadoop 3.3.1 as follows.

* Added `opt(key, long)` and `must(key, long)`.
* Declared that `withFileStatus(null)` is allowed.
* Declared that `withFileStatus(status)` only checks the filename of the path, not the full path. This is needed to support passthrough/mounted filesystems.
* Added standard option keys.

### `FutureDataInputStreamBuilder openFile(Path path)`

Creates a [`FutureDataInputStreamBuilder`](fsdatainputstreambuilder.html) to construct a operation to open the file at `path` for reading.

When `build()` is invoked on the returned `FutureDataInputStreamBuilder` instance, the builder parameters are verified and `FileSystem.openFileWithOptions(Path, OpenFileParameters)` or `AbstractFileSystem.openFileWithOptions(Path, OpenFileParameters)` invoked.

These protected methods returns a `CompletableFuture<FSDataInputStream>` which, when its `get()` method is called, either returns an input stream of the contents of opened file, or raises an exception.

The base implementation of the `FileSystem.openFileWithOptions(PathHandle, OpenFileParameters)` ultimately invokes `FileSystem.open(Path, int)`.

Thus the chain `FileSystem.openFile(path).build().get()` has the same preconditions and postconditions as `FileSystem.open(Path p, int bufferSize)`

However, there is one difference which implementations are free to take advantage of:

The returned stream MAY implement a lazy open where file non-existence or access permission failures may not surface until the first `read()` of the actual data.

This saves network IO on object stores.

The `openFile()` operation MAY check the state of the filesystem during its invocation, but as the state of the filesystem may change between this call and the actual `build()` and `get()` operations, this file-specific preconditions (file exists, file is readable, etc) MUST NOT be checked here.

FileSystem implementations which do not implement `open(Path, int)` MAY postpone raising an `UnsupportedOperationException` until either the `FutureDataInputStreamBuilder.build()` or the subsequent `get()` call, else they MAY fail fast in the `openFile()` call.

Consult [`FutureDataInputStreamBuilder`](fsdatainputstreambuilder.html) for details on how to use the builder, and for standard options which may be passed in.

### `FutureDataInputStreamBuilder openFile(PathHandle)`

Creates a [`FutureDataInputStreamBuilder`](fsdatainputstreambuilder.html) to construct a operation to open the file identified by the given `PathHandle` for reading.

If implemented by a filesystem, the semantics of [`openFile(Path)`](#openfile_path_) Thus the chain `openFile(pathhandle).build().get()` has the same preconditions and postconditions as `open(Pathhandle, int)`

FileSystem implementations which do not implement `open(PathHandle handle, int bufferSize)` MAY postpone raising an `UnsupportedOperationException` until either the `FutureDataInputStreamBuilder.build()` or the subsequent `get()` call, else they MAY fail fast in the `openFile(PathHandle)` call.

The base implementation raises this exception in the `build()` operation; other implementations SHOULD copy this.

### Implementors notes

The base implementation of `openFileWithOptions()` actually executes the `open(path)` operation synchronously, yet still returns the result or any failures in the `CompletableFuture<>`, so as to provide a consistent lifecycle across all filesystems.

Any filesystem client where the time to open a file may be significant SHOULD execute it asynchronously by submitting the operation in some executor/thread pool. This is particularly recommended for object stores and other filesystems likely to be accessed over long-haul connections.

Arbitrary filesystem-specific options MAY be supported; these MUST be prefixed with either the filesystem schema, e.g. `hdfs.` or in the `fs.SCHEMA` format as normal configuration settings `fs.hdfs`. The latter style allows the same configuration option to be used for both filesystem configuration and file-specific configuration.

It SHOULD be possible to always open a file without specifying any options, so as to present a consistent model to users. However, an implementation MAY opt to require one or more mandatory options to be set.

The returned stream may perform “lazy” evaluation of file access. This is relevant for object stores where the probes for existence are expensive, and, even with an asynchronous open, may be considered needless.

---
# class `org.apache.hadoop.fs.FSDataInputStream`

* [Class FSDataInputStream extends DataInputStream](#Class_FSDataInputStream_extends_DataInputStream)
  * [Closeable.close()](#Closeable.close.28.29)
  * [Seekable.getPos()](#Seekable.getPos.28.29)
  * [InputStream.read()](#InputStream.read.28.29)
  * [InputStream.read(buffer[], offset, length)](#InputStream.read.28buffer.5B.5D.2C_offset.2C_length.29)
  * [Seekable.seek(s)](#Seekable.seek.28s.29)
  * [Seekable.seekToNewSource(offset)](#Seekable.seekToNewSource.28offset.29)
  * [CanUnbuffer.unbuffer()](#CanUnbuffer.unbuffer.28.29)
* [interface PositionedReadable](#interface_PositionedReadable)
  * [Implementation preconditions](#Implementation_preconditions)
  * [Failure states](#Failure_states)
  * [int PositionedReadable.read(position, buffer, offset, length)](#int_PositionedReadable.read.28position.2C_buffer.2C_offset.2C_length.29)
  * [void PositionedReadable.readFully(position, buffer, offset, length)](#void_PositionedReadable.readFully.28position.2C_buffer.2C_offset.2C_length.29)
  * [PositionedReadable.readFully(position, buffer)](#PositionedReadable.readFully.28position.2C_buffer.29)
  * [void readVectored(List<? extends FileRange> ranges, IntFunction<ByteBuffer> allocate)](#void_readVectored.28List.3C.3F_extends_FileRange.3E_ranges.2C_IntFunction.3CByteBuffer.3E_allocate.29)
* [void readVectored(List<? extends FileRange> ranges, IntFunction<ByteBuffer> allocate, Consumer<ByteBuffer> release)](#void_readVectored.28List.3C.3F_extends_FileRange.3E_ranges.2C_IntFunction.3CByteBuffer.3E_allocate.2C_Consumer.3CByteBuffer.3E_release.29)

## Class `FSDataInputStream extends DataInputStream`

The core behavior of `FSDataInputStream` is defined by `java.io.DataInputStream`, with extensions that add key assumptions to the system.

1. The source is a local or remote filesystem.
2. The stream being read references a finite array of bytes.
3. The length of the data does not change during the read process.
4. The contents of the data does not change during the process.
5. The source file remains present during the read process.
6. Callers may use `Seekable.seek()` to offsets within the array of bytes, with future reads starting at this offset.
7. The cost of forward and backward seeks is low.
8. There is no requirement for the stream implementation to be thread-safe.
9. BUT, if a stream implements [PositionedReadable](#PositionedReadable), “positioned reads” MUST be thread-safe.

Files are opened via `FileSystem.open(p)`, which, if successful, returns:

```
result = FSDataInputStream(0, FS.Files[p])
```

The stream can be modeled as:

```
FSDIS = (pos, data[], isOpen)
```

with access functions:

```
pos(FSDIS)
data(FSDIS)
isOpen(FSDIS)
```

**Implicit invariant**: the size of the data stream equals the size of the file as returned by `FileSystem.getFileStatus(Path p)`

```
forall p in dom(FS.Files[p]) :
    len(data(FSDIS)) == FS.getFileStatus(p).length
```

### `Closeable.close()`

The semantics of `java.io.Closeable` are defined in the interface definition within the JRE.

The operation MUST be idempotent; the following sequence is not an error:

```
FSDIS.close();
FSDIS.close();
```

#### Implementation Notes

* Implementations SHOULD be robust against failure. If an inner stream is closed, it should be checked for being `null` first.
* Implementations SHOULD NOT raise `IOException` exceptions (or any other exception) during this operation. Client applications often ignore these, or may fail unexpectedly.

#### Postconditions

```
FSDIS' = ((undefined), (undefined), False)
```

### `Seekable.getPos()`

Return the current position. The outcome when a stream is closed is undefined.

#### Preconditions

```
isOpen(FSDIS)
```

#### Postconditions

```
result = pos(FSDIS)
```

### `InputStream.read()`

Return the data at the current position.

1. Implementations should fail when a stream is closed.
2. There is no limit on how long `read()` may take to complete.

#### Preconditions

```
isOpen(FSDIS)
```

#### Postconditions

```
if ( pos < len(data) ):
   FSDIS' = (pos + 1, data, True)
   result = data[pos]
else
    result = -1
```

### `InputStream.read(buffer[], offset, length)`

Read `length` bytes of data into the destination buffer, starting at offset `offset`. The source of the data is the current position of the stream, as implicitly set in `pos`.

#### Preconditions

```
isOpen(FSDIS)
buffer != null else raise NullPointerException, IllegalArgumentException
offset >= 0 else raise IndexOutOfBoundsException
length >= 0 else raise IndexOutOfBoundsException, IllegalArgumentException
offset < len(buffer) else raise IndexOutOfBoundsException
length <= len(buffer) - offset else raise IndexOutOfBoundsException
pos >= 0 else raise EOFException, IOException
```

Exceptions that may be raised on precondition failure are

```
InvalidArgumentException
ArrayIndexOutOfBoundsException
RuntimeException
```

Not all filesystems check the `isOpen` state.

#### Postconditions

```
if length == 0 :
  result = 0

else if pos > len(data):
  result = -1

else
  let l = min(length, len(data)-length) :
    buffer' = buffer where forall i in [0..l-1]:
       buffer'[o+i] = data[pos+i]
    FSDIS' = (pos+l, data, true)
    result = l
```

The `java.io` API states that if the amount of data to be read (i.e. `length`) then the call must block until the amount of data available is greater than zero —that is, until there is some data. The call is not required to return when the buffer is full, or indeed block until there is no data left in the stream.

That is, rather than `l` being simply defined as `min(length, len(data)-length)`, it strictly is an integer in the range `1..min(length, len(data)-length)`. While the caller may expect as much of the buffer as possible to be filled in, it is within the specification for an implementation to always return a smaller number, perhaps only ever 1 byte.

What is critical is that unless the destination buffer size is 0, the call must block until at least one byte is returned. Thus, for any data source of length greater than zero, repeated invocations of this `read()` operation will eventually read all the data.

#### Implementation Notes

1. If the caller passes a `null` buffer, then an unchecked exception MUST be thrown. The base JDK `InputStream` implementation throws `NullPointerException`. HDFS historically used `IllegalArgumentException`. Implementations MAY use either of these.
2. If the caller passes a negative value for `length`, then an unchecked exception MUST be thrown. The base JDK `InputStream` implementation throws `IndexOutOfBoundsException`. HDFS historically used `IllegalArgumentException`. Implementations MAY use either of these.
3. Reads through any method MUST return the same data.
4. Callers MAY interleave calls to different read methods (single-byte and multi-byte) on the same stream. The stream MUST return the same underlying data, regardless of the specific read calls or their ordering.

### `Seekable.seek(s)`

#### Preconditions

Not all subclasses implement the Seek operation:

```
supported(FSDIS, Seekable.seek) else raise [UnsupportedOperationException, IOException]
```

If the operation is supported, the file SHOULD be open:

```
isOpen(FSDIS)
```

Some filesystems do not perform this check, relying on the `read()` contract to reject reads on a closed stream (e.g. `RawLocalFileSystem`).

A `seek(0)` MUST always succeed, as the seek position must be positive and less than the length of the Stream:

```
s > 0 and ((s==0) or ((s < len(data)))) else raise [EOFException, IOException]
```

Some FileSystems do not raise an exception if this condition is not met. They instead return -1 on any `read()` operation where, at the time of the read, `len(data(FSDIS)) < pos(FSDIS)`.

After a failed seek, the value of `pos(FSDIS)` may change. As an example, seeking past the EOF may move the read position to the end of the file, *as well as raising an `EOFException`.*

#### Postconditions

```
FSDIS' = (s, data, True)
```

There is an implicit invariant: a seek to the current position is a no-op

```
seek(getPos())
```

Implementations may recognise this operation and bypass all other precondition checks, leaving the input stream unchanged.

The most recent connectors to object stores all implement some form of “lazy-seek”: the `seek()` call may appear to update the stream, and the value of `getPos()` is updated, but the file is not opened/reopenend until data is actually read. Implementations of lazy seek MUST still validate the new seek position against the known length of the file. However the state of the file (i.e. does it exist, what its current length is) does not need to be refreshed at this point. The fact that a file has been deleted or truncated may not surface until that `read()` call.

### `Seekable.seekToNewSource(offset)`

This operation instructs the source to retrieve `data[]` from a different source from the current source. This is only relevant if the filesystem supports multiple replicas of a file and there is more than 1 replica of the data at offset `offset`.

#### Preconditions

Not all subclasses implement this operation, and instead either raise an exception or return `False`.

```
supported(FSDIS, Seekable.seekToNewSource) else raise [UnsupportedOperationException, IOException]
```

Examples: `CompressionInputStream` , `HttpFSFileSystem`

If supported, the file must be open:

```
isOpen(FSDIS)
```

#### Postconditions

The majority of subclasses that do not implement this operation simply fail.

```
if not supported(FSDIS, Seekable.seekToNewSource(s)):
    result = False
```

Examples: `RawLocalFileSystem` , `HttpFSFileSystem`

If the operation is supported and there is a new location for the data:

```
FSDIS' = (pos, data', true)
result = True
```

The new data is the original data (or an updated version of it, as covered in the Consistency section below), but the block containing the data at `offset` is sourced from a different replica.

If there is no other copy, `FSDIS` is not updated; the response indicates this:

```
result = False
```

Outside of test methods, the primary use of this method is in the {{FSInputChecker}} class, which can react to a checksum error in a read by attempting to source the data elsewhere. If a new source can be found it attempts to reread and recheck that portion of the file.

### `CanUnbuffer.unbuffer()`

This operation instructs the source to release any system resources they are currently holding on to, such as buffers, sockets, file descriptors, etc. Any subsequent IO operation will likely have to reacquire these resources. Unbuffering is useful in situation where streams need to remain open, but no IO operation is expected from the stream in the immediate future (examples include file handle cacheing).

#### Preconditions

Not all subclasses implement this operation. In addition to implementing `CanUnbuffer`. Subclasses must implement the `StreamCapabilities` interface and `StreamCapabilities.hasCapability(UNBUFFER)` must return true. If a subclass implements `CanUnbuffer` but does not report the functionality via `StreamCapabilities` then the call to `unbuffer` does nothing. If a subclass reports that it does implement `UNBUFFER`, but does not implement the `CanUnbuffer` interface, an `UnsupportedOperationException` is thrown.

```
supported(FSDIS, StreamCapabilities.hasCapability && FSDIS.hasCapability(UNBUFFER) && CanUnbuffer.unbuffer)
```

This method is not thread-safe. If `unbuffer` is called while a `read` is in progress, the outcome is undefined.

`unbuffer` can be called on a closed file, in which case `unbuffer` will do nothing.

#### Postconditions

The majority of subclasses that do not implement this operation simply do nothing.

If the operation is supported, `unbuffer` releases any and all system resources associated with the stream. The exact list of what these resources are is generally implementation dependent, however, in general, it may include buffers, sockets, file descriptors, etc.

## interface `PositionedReadable`

The `PositionedReadable` operations supply “positioned reads” (“pread”). They provide the ability to read data into a buffer from a specific position in the data stream. Positioned reads equate to a [`Seekable.seek`](#Seekable.seek) at a particular offset followed by a [`InputStream.read(buffer[], offset, length)`](#InputStream.read.buffer), only there is a single method invocation, rather than `seek` then `read`, and two positioned reads can *optionally* run concurrently over a single instance of a `FSDataInputStream` stream.

The interface declares positioned reads thread-safe (some of the implementations do not follow this guarantee).

Any positional read run concurrent with a stream operation — e.g. [`Seekable.seek`](#Seekable.seek), [`Seekable.getPos()`](#Seekable.getPos), and [`InputStream.read()`](#InputStream.read) — MUST run in isolation; there must not be mutual interference.

Concurrent positional reads and stream operations MUST be serializable; one may block the other so they run in series but, for better throughput and ‘liveness’, they SHOULD run concurrently.

Given two parallel positional reads, one at `pos1` for `len1` into buffer `dest1`, and another at `pos2` for `len2` into buffer `dest2`, AND given a concurrent, stream read run after a seek to `pos3`, the resultant buffers MUST be filled as follows, even if the reads happen to overlap on the underlying stream:

```
// Positioned read #1
read(pos1, dest1, ... len1) -> dest1[0..len1 - 1] =
  [data(FS, path, pos1), data(FS, path, pos1 + 1) ... data(FS, path, pos1 + len1 - 1]

// Positioned read #2
read(pos2, dest2, ... len2) -> dest2[0..len2 - 1] =
  [data(FS, path, pos2), data(FS, path, pos2 + 1) ... data(FS, path, pos2 + len2 - 1]

// Stream read
seek(pos3);
read(dest3, ... len3) -> dest3[0..len3 - 1] =
  [data(FS, path, pos3), data(FS, path, pos3 + 1) ... data(FS, path, pos3 + len3 - 1]
```

Note that implementations are not required to be atomic; the intermediate state of the operation (the change in the value of `getPos()`) may be visible.

### Implementation preconditions

Not all `FSDataInputStream` implementations support these operations. Those that do not implement `Seekable.seek()` do not implement the `PositionedReadable` interface.

```
supported(FSDIS, Seekable.seek) else raise [UnsupportedOperationException, IOException]
```

This could be considered obvious: if a stream is not `Seekable`, a client cannot seek to a location. It is also a side effect of the base class implementation, which uses `Seekable.seek()`.

**Implicit invariant**: for all `PositionedReadable` operations, the value of `pos` is unchanged at the end of the operation

```
pos(FSDIS') == pos(FSDIS)
```

### Failure states

For any operations that fail, the contents of the destination `buffer` are undefined. Implementations may overwrite part or all of the buffer before reporting a failure.

### `int PositionedReadable.read(position, buffer, offset, length)`

Read as much data as possible into the buffer space allocated for it.

#### Preconditions

```
position >= 0 else raise [EOFException, IOException, IllegalArgumentException, RuntimeException]
len(buffer) - offset >= length else raise [IndexOutOfBoundException, RuntimeException]
length >= 0
offset >= 0
```

#### Postconditions

The amount of data read is the less of the length or the amount of data available from the specified position:

```
let available = min(length, len(data)-position)
buffer'[offset..(offset+available-1)] = data[position..position+available -1]
result = available
```

1. A return value of -1 means that the stream had no more available data.
2. An invocation with `length==0` implicitly does not read any data; implementations may short-cut the operation and omit any IO. In such instances, checks for the stream being at the end of the file may be omitted.
3. If an IO exception occurs during the read operation(s), the final state of `buffer` is undefined.

### `void PositionedReadable.readFully(position, buffer, offset, length)`

Read exactly `length` bytes of data into the buffer, failing if there is not enough data available.

#### Preconditions

```
position >= 0 else raise [EOFException, IOException, IllegalArgumentException, RuntimeException]
length >= 0
offset >= 0
len(buffer) - offset >= length else raise [IndexOutOfBoundException, RuntimeException]
(position + length) <= len(data) else raise [EOFException, IOException]
```

If an IO exception occurs during the read operation(s), the final state of `buffer` is undefined.

If there is not enough data in the input stream to satisfy the requests, the final state of `buffer` is undefined.

#### Postconditions

The buffer from offset `offset` is filled with the data starting at `position`

```
buffer'[offset..(offset+length-1)] = data[position..(position + length -1)]
```

### `PositionedReadable.readFully(position, buffer)`

The semantics of this are exactly equivalent to

```
readFully(position, buffer, 0, len(buffer))
```

That is, the buffer is filled entirely with the contents of the input source from position `position`.

### `void readVectored(List<? extends FileRange> ranges, IntFunction<ByteBuffer> allocate)`

Read fully data for a list of ranges asynchronously. The default implementation iterates through the ranges, tries to coalesce the ranges based on values of `minSeekForVectorReads` and `maxReadSizeForVectorReads` and then read each merged ranges synchronously, but the intent is sub classes can implement efficient implementation. Reading in both direct and heap byte buffers are supported. Also, clients are encouraged to use `WeakReferencedElasticByteBufferPool` for allocating buffers such that even direct buffers are garbage collected when they are no longer referenced.

The position returned by `getPos()` after `readVectored()` is undefined.

If a file is changed while the `readVectored()` operation is in progress, the output is undefined. Some ranges may have old data, some may have new, and some may have both.

While a `readVectored()` operation is in progress, normal read API calls MAY block; the value of `getPos(`) is also undefined. Applications SHOULD NOT make such requests while waiting for the results of a vectored read.

Note: Don’t use direct buffers for reading from `ChecksumFileSystem` as that may lead to memory fragmentation explained in [HADOOP-18296](https://issues.apache.org/jira/browse/HADOOP-18296) *Memory fragmentation in ChecksumFileSystem Vectored IO implementation*

#### Preconditions

No empty lists.

```
if ranges = null raise NullPointerException
if allocate = null raise NullPointerException
```

For each requested range `range[i]` in the list of ranges `range[0..n]` sorted on `getOffset()` ascending such that

for all `i where i > 0`:

```
range[i].getOffset() > range[i-1].getOffset()
```

For all ranges `0..i` the preconditions are:

```
ranges[i] != null else raise IllegalArgumentException
ranges[i].getOffset() >= 0 else raise EOFException
ranges[i].getLength() >= 0 else raise IllegalArgumentException
if i > 0 and ranges[i].getOffset() < (ranges[i-1].getOffset() + ranges[i-1].getLength) :
   raise IllegalArgumentException
```

If the length of the file is known during the validation phase:

```
if range[i].getOffset + range[i].getLength >= data.length() raise EOFException
```

#### Postconditions

For each requested range `range[i]` in the list of ranges `range[0..n]`

```
ranges[i]'.getData() = CompletableFuture<buffer: ByteBuffer>
```

and when `getData().get()` completes:

```
let buffer = `getData().get()
let len = ranges[i].getLength()
let data = new byte[len]
(buffer.position() - buffer.limit) = len
buffer.get(data, 0, len) = readFully(ranges[i].getOffset(), data, 0, len)
```

That is: the result of every ranged read is the result of the (possibly asynchronous) call to `PositionedReadable.readFully()` for the same offset and length

#### `minSeekForVectorReads()`

The smallest reasonable seek. Two ranges won’t be merged together if the difference between end of first and start of next range is more than this value.

#### `maxReadSizeForVectorReads()`

Maximum number of bytes which can be read in one go after merging the ranges. Two ranges won’t be merged if the combined data to be read. Essentially setting this to 0 will disable the merging of ranges.

#### Concurrency

* When calling `readVectored()` while a separate thread is trying to read data through `read()`/`readFully()`, all operations MUST complete successfully.
* Invoking a vector read while an existing set of pending vector reads are in progress MUST be supported. The order of which ranges across the multiple requests complete is undefined.
* Invoking `read()`/`readFully()` while a vector API call is in progress MUST be supported. The order of which calls return data is undefined.

The S3A connector closes any open stream when its `synchronized readVectored()` method is invoked; It will then switch the read policy from normal to random so that any future invocations will be for limited ranges. This is because the expectation is that vector IO and large sequential reads are not mixed and that holding on to any open HTTP connection is wasteful.

#### Handling of zero-length ranges

Implementations MAY short-circuit reads for any range where `range.getLength() = 0` and return an empty buffer.

In such circumstances, other validation checks MAY be omitted.

There are no guarantees that such optimizations take place; callers SHOULD NOT include empty ranges for this reason.

#### Consistency

* All readers, local and remote, of a data stream `FSDIS` provided from a `FileSystem.open(p)` are expected to receive access to the data of `FS.Files[p]` at the time of opening.
* If the underlying data is changed during the read process, these changes MAY or MAY NOT be visible.
* Such changes that are visible MAY be partially visible.

At time `t0`

```
FSDIS0 = FS'read(p) = (0, data0[])
```

At time `t1`

```
FS' = FS' where FS'.Files[p] = data1
```

From time `t >= t1`, the value of `FSDIS0` is undefined.

It may be unchanged

```
FSDIS0.data == data0

forall l in len(FSDIS0.data):
  FSDIS0.read() == data0[l]
```

It may pick up the new data

```
FSDIS0.data == data1

forall l in len(FSDIS0.data):
  FSDIS0.read() == data1[l]
```

It may be inconsistent, such that a read of an offset returns data from either of the datasets

```
forall l in len(FSDIS0.data):
  (FSDIS0.read(l) == data0[l]) or (FSDIS0.read(l) == data1[l]))
```

That is, every value read may be from the original or updated file.

It may also be inconsistent on repeated reads of same offset, that is at time `t2 > t1`:

```
r2 = FSDIS0.read(l)
```

While at time `t3 > t2`:

```
r3 = FSDIS0.read(l)
```

It may be that `r3 != r2`. (That is, some of the data my be cached or replicated, and on a subsequent read, a different version of the file’s contents are returned).

Similarly, if the data at the path `p`, is deleted, this change MAY or MAY not be visible during read operations performed on `FSDIS0`.

#### API Stabilization Notes

The `readVectored()` API was shipped in Hadoop 3.3.5, with explicit local, raw local and S3A support -and fallback everywhere else.

*Overlapping ranges*

The restriction “no overlapping ranges” was only initially enforced in the S3A connector, which would raise `UnsupportedOperationException`. Adding the range check as a precondition for all implementations (Raw Local being an exception) guarantees consistent behavior everywhere. The reason Raw Local doesn’t have this precondition is ChecksumFileSystem creates the chunked ranges based on the checksum chunk size and then calls readVectored on Raw Local which may lead to overlapping ranges in some cases. For details see [HADOOP-19291](https://issues.apache.org/jira/browse/HADOOP-19291)

For reliable use with older hadoop releases with the API: sort the list of ranges and check for overlaps before calling `readVectored()`.

#### Direct Buffer Reads

Releases without [HADOOP-19101](https://issues.apache.org/jira/browse/HADOOP-19101) *Vectored Read into off-heap buffer broken in fallback implementation* can read data from the wrong offset with the default “fallback” implementation if the buffer allocator function returns off heap “direct” buffers.

The custom implementations in local filesystem and S3A’s non-prefetching stream are safe.

Anyone implementing support for the API, unless confident they only run against releases with the fixed implementation, SHOULD NOT use the API if the allocator is direct and the input stream does not explicitly declare support through an explicit `hasCapability()` probe:

```
Stream.hasCapability("in:readvectored")
```

#### Buffer Slicing

[HADOOP-18296](https://issues.apache.org/jira/browse/HADOOP-18296), *Memory fragmentation in ChecksumFileSystem Vectored IO implementation* highlights that `ChecksumFileSystem` (which the default implementation of `file://` subclasses), may return buffers which are sliced subsets of buffers allocated through the `allocate()` function passed in.

This will happen during reads with and without range coalescing.

Checksum verification may be disabled by setting the option `fs.file.checksum.verify` to false (Hadoop 3.4.2 and later).

```
<property>
  <name>fs.file.checksum.verify</name>
  <value>false</value>
</property>
```

(As you would expect, disabling checksum verification means that errors reading data may not be detected during the read operation. Use with care in production.)

Filesystem instances which split buffers during vector read operations MUST declare this by returning `true` to the path capabilities probe `fs.capability.vectoredio.sliced`, and for the open stream in its `hasCapability()` method.

The local filesystem will not slice buffers if the checksum file of `filename + ".crc"` is not found. This is not declared in the filesystem `hasPathCapability(filename, "fs.capability.vectoredio.sliced")` call, as no checks for the checksum file are made then. This cannot be relied on in production, but it may be useful when testing for buffer recycling with Hadoop releases 3.4.1 and earlier.

*Implementors Notes*

* Don’t slice buffers. `ChecksumFileSystem` has to be considered an outlier which needs to be addressed in future.
* Always free buffers in error handling code paths.
* When handling errors in coalesced ranges, don’t release buffers for any sub-ranges which have already completed.

Handling failures in coalesced ranges is complicated. Recent implementations, such as `org.apache.hadoop.fs.s3a.impl.streams.AnalyticsStream` omit range coalescing, relying solely on parallel HTTP for performance.

## `void readVectored(List<? extends FileRange> ranges, IntFunction<ByteBuffer> allocate, Consumer<ByteBuffer> release)`

This is the extension of `readVectored/2` with an additional `release` consumer operation to release buffers.

The specification and rules of this method are exactly those of the other operation, with the addition of:

Preconditions

```
if release = null raise NullPointerException
```

* If a read operation fails due to an `IOException` or similar, the implementation of `readVectored()`, SHOULD call `release(buffer)` with the buffer created by invoking the `allocate()` function into which the data was being read.
* Implementations MUST NOT call `release(buffer)` with any non-null buffer *not* obtained through `allocate()`.
* Implementations MUST only call `release(buffer)` when a failure has occurred and the future is about to have `Future.completedExceptionally()` invoked.

It is an extension to the original Vector Read API -not all versions of Hadoop with the original `readVectored()` call define it. If used directly in application code, that application is restricting itself to later versions of the API.

If used via reflection, if this method is not found, fall back to the original method.

---
# A Model of a Hadoop Filesystem

* [Paths and Path Elements](#Paths_and_Path_Elements)
  * [Predicates and Functions](#Predicates_and_Functions)
    * [valid-path-element(List[String]): bool](#valid-path-element.28List.5BString.5D.29:_bool)
    * [valid-path(List[PathElement]): bool](#valid-path.28List.5BPathElement.5D.29:_bool)
    * [parent(path:Path): Path](#parent.28path:Path.29:_Path)
    * [filename(Path): PathElement](#filename.28Path.29:_PathElement)
    * [childElements(Path p, Path q): Path](#childElements.28Path_p.2C_Path_q.29:_Path)
    * [ancestors(Path): List[Path]](#ancestors.28Path.29:_List.5BPath.5D)
  * [Notes for relative paths](#Notes_for_relative_paths)
* [Defining the Filesystem](#Defining_the_Filesystem)
  * [Directory references](#Directory_references)
  * [File references](#File_references)
  * [Symbolic references](#Symbolic_references)
  * [File Length](#File_Length)
  * [User home](#User_home)
  * [Exclusivity](#Exclusivity)
  * [Encryption Zone](#Encryption_Zone)
* [Notes](#Notes)

## Paths and Path Elements

A Path is a list of Path elements which represents a path to a file, directory or symbolic link

Path elements are non-empty strings. The exact set of valid strings MAY be specific to a particular FileSystem implementation.

Path elements MUST NOT be in `{"", ".", "..", "/"}`.

Path elements MUST NOT contain the characters `{'/', ':'}`.

Filesystems MAY have other strings that are not permitted in a path element.

When validating path elements, the exception `InvalidPathException` SHOULD be raised when a path is invalid [HDFS]

### Predicates and Functions

#### `valid-path-element(List[String]): bool`

A path element `pe` is invalid if any character in it is in the set of forbidden characters, or the element as a whole is invalid

```
forall e in pe: not (e in {'/', ':'})
not pe in {"", ".",  "..", "/"}
```

#### `valid-path(List[PathElement]): bool`

A Path `p` is *valid* if all path elements in it are valid

```
def valid-path(path): forall pe in path: valid-path-element(pe)
```

The set of all possible paths is *Paths*; this is the infinite set of all lists of valid path elements.

The path represented by empty list, `[]` is the *root path*, and is denoted by the string `"/"`.

#### `parent(path:Path): Path`

The partial function `parent(path:Path):Path` provides the parent path can be defined using list slicing.

```
def parent(pe) : pe[0:-1]
```

Preconditions:

```
path != []
```

#### `filename(Path): PathElement`

The last Path Element in a Path is called the filename.

```
def filename(p) : p[-1]
```

Preconditions:

```
p != []
```

#### `childElements(Path p, Path q): Path`

The partial function `childElements:(Path p, Path q):Path` is the list of path elements in `p` that follow the path `q`.

```
def childElements(p, q): p[len(q):]
```

Preconditions:

```
# The path 'q' must be at the head of the path 'p'
q == p[:len(q)]
```

#### `ancestors(Path): List[Path]`

The list of all paths that are either the direct parent of a path p, or a parent of ancestor of p.

### Notes for relative paths

This definition handles absolute paths but not relative ones; it needs to be reworked so the root element is explicit, presumably by declaring that the root (and only the root) path element may be [‘/’].

Relative paths can then be distinguished from absolute paths as the input to any function and resolved when the second entry in a two-argument function such as `rename`.

## Defining the Filesystem

A filesystem `FS` contains directories (a set of paths), files (a mapping of a path to a list of bytes) and symlinks (a set of paths mapping to paths)

```
(Directories:Set[Path], Files:Map[Path:List[byte]], Symlinks:Map[Path:Path])
```

Accessor functions return the specific element of a filesystem

```
def directories(FS)  = FS.Directories
def files(FS) = FS.Files
def symlinks(FS) = keys(FS.Symlinks)
def filenames(FS) = keys(FS.Files)
```

The entire set of a paths finite subset of all possible Paths, and functions to resolve a path to data, a directory predicate or a symbolic link:

```
def paths(FS) = FS.Directories + filenames(FS) + symlinks(FS)
```

A path is deemed to exist if it is in this aggregate set:

```
def exists(FS, p) = p in paths(FS)
```

The root path, “/”, is a directory represented by the path [“/”], which must always exist in a filesystem.

```
def isRoot(p) = p == ["/"].

forall FS in FileSystems : ["/"] in FS.Directories
```

### Directory references

A path MAY refer to a directory in a FileSystem:

```
isDir(FS, p): p in FS.Directories
```

Directories may have children, that is, there may exist other paths in the FileSystem whose path begins with a directory. Only directories may have children. This can be expressed by saying that every path’s parent must be a directory.

It can then be declared that a path has no parent in which case it is the root directory, or it MUST have a parent that is a directory:

```
forall p in paths(FS) : isRoot(p) or isDir(FS, parent(p))
```

Because the parent directories of all directories must themselves satisfy this criterion, it is implicit that only leaf nodes may be files or symbolic links:

Furthermore, because every filesystem contains the root path, every filesystem must contain at least one directory.

A directory may have children:

```
def children(FS, p) = {q for q in paths(FS) where parent(q) == p}
```

There are no duplicate names in the child paths, because all paths are taken from the set of lists of path elements. There can be no duplicate entries in a set, hence no children with duplicate names.

A path *D* is a descendant of a path *P* if it is the direct child of the path *P* or an ancestor is a direct child of path *P*:

```
def isDescendant(P, D) = parent(D) == P or isDescendant(P, parent(D))
```

The descendants of a directory P are all paths in the filesystem whose path begins with the path P, i.e. their parent is P or an ancestor is P

```
def descendants(FS, D) = {p for p in paths(FS) where isDescendant(D, p)}
```

### File references

A path MAY refer to a file that has data in the filesystem; its path is a key in the data dictionary

```
def isFile(FS, p) =  p in keys(FS.Files)
```

### Symbolic references

A path MAY refer to a symbolic link:

```
def isSymlink(FS, p) = p in symlinks(FS)
```

### File Length

Files store data:

```
def data(FS, p) = files(FS)[p]
```

The length of a path p in a filesystem FS is the length of the data stored, or 0 if it is a directory:

```
def length(FS, p) = if isFile(p) : return length(data(FS, p)) else return 0
```

### User home

The home directory of a user is an implicit part of a filesystem, and is derived from the userid of the process working with the filesystem:

```
def getHomeDirectory(FS) : Path
```

The function `getHomeDirectory` returns the home directory for the Filesystem and the current user account. For some FileSystems, the path is `["/","users", System.getProperty("user-name")]`. However, for HDFS, the username is derived from the credentials used to authenticate the client with HDFS. This may differ from the local user account name.

### Exclusivity

A path cannot refer to more than one of a file, a directory or a symbolic link

```
directories(FS) ^ filenames(FS) == {}
directories(FS) ^ symlinks(FS) == {}
filenames(FS) ^ symlinks(FS) == {}
```

This implies that only files may have data.

This condition is invariant and is an implicit postcondition of all operations that manipulate the state of a FileSystem `FS`.

### Encryption Zone

The data is encrypted if the file is in encryption zone.

```
def inEncryptionZone(FS, path): bool
```

The nature of the encryption and the mechanism for creating an encryption zone are implementation details not covered in this specification. No guarantees are made about the quality of the encryption. The metadata is not encrypted.

All files and directories under a directory in an encryption zone are also in an encryption zone.

```
forall d in directories(FS): inEncyptionZone(FS, d) implies
  forall c in children(FS, d) where (isFile(FS, c) or isDir(FS, c)) :
    inEncyptionZone(FS, c)
```

For all files in an encrypted zone, the data is encrypted, but the encryption type and specification are not defined.

```
forall f in files(FS) where inEncyptionZone(FS, f):
  isEncrypted(data(FS, f))
```

## Notes

Not covered: hard links in a FileSystem. If a FileSystem supports multiple references in *paths(FS)* to point to the same data, the outcome of operations are undefined.

This model of a FileSystem is sufficient to describe all the FileSystem queries and manipulations excluding metadata and permission operations. The Hadoop `FileSystem` and `FileContext` interfaces can be specified in terms of operations that query or change the state of a FileSystem.

---
# class `org.apache.hadoop.fs.FutureDataInputStreamBuilder`

* [History](#History)
  * [Hadoop 3.3.0: API introduced](#Hadoop_3.3.0:_API_introduced)
  * [Hadoop 3.3.5: standardization and expansion](#Hadoop_3.3.5:_standardization_and_expansion)
  * [Hadoop 3.3.6: API change to address operator overload bugs.](#Hadoop_3.3.6:_API_change_to_address_operator_overload_bugs.)
* [Invariants](#Invariants)
* [`Implementation-agnostic parameters.](#a.60Implementation-agnostic_parameters.)
  * [FutureDataInputStreamBuilder bufferSize(int bufSize)](#FutureDataInputStreamBuilder_bufferSize.28int_bufSize.29)
  * [FutureDataInputStreamBuilder withFileStatus(FileStatus status)](#FutureDataInputStreamBuilder_withFileStatus.28FileStatus_status.29)
  * [Set optional or mandatory parameters](#Set_optional_or_mandatory_parameters)
  * [When to use opt versus must](#When_to_use_opt_versus_must)
* [Implementation Notes](#Implementation_Notes)
* [Builder interface](#Builder_interface)
  * [CompletableFuture<FSDataInputStream> build()](#CompletableFuture.3CFSDataInputStream.3E_build.28.29)
* [Standard openFile() options since hadoop branch-3.3](#Standard_openFile.28.29_options_since_hadoop_branch-3.3)
  * [Option: fs.option.openfile.buffer.size](#Option:_fs.option.openfile.buffer.size)
  * [Option: fs.option.openfile.read.policy](#Option:_fs.option.openfile.read.policy)
  * [Option: fs.option.openfile.length: Long](#Option:_fs.option.openfile.length:_Long)
  * [Options: fs.option.openfile.split.start and fs.option.openfile.split.end: Long](#Options:_fs.option.openfile.split.start_and_fs.option.openfile.split.end:_Long)
  * [Option: fs.option.openfile.footer.cache: Boolean](#Option:_fs.option.openfile.footer.cache:_Boolean)
* [S3A-specific options](#S3A-specific_options)
* [ABFS-specific options](#ABFS-specific_options)
* [Examples](#Examples)

  * [Opening a file with both standard and non-standard options](#Opening_a_file_with_both_standard_and_non-standard_options)
  * [Opening a file with older releases](#Opening_a_file_with_older_releases)
  * [Passing options in to MapReduce](#Passing_options_in_to_MapReduce)
  * [MapReduce input format propagating options](#MapReduce_input_format_propagating_options)
  * [FileContext.openFile](#FileContext.openFile)
  * [Example: reading a whole file](#Example:_reading_a_whole_file)

An interface offering of the Builder pattern for creating Java `Future` references to `FSDataInputStream` and its subclasses. It is used to initate a (potentially asynchronous) operation to open an existing file for reading.

## History

### Hadoop 3.3.0: API introduced

[HADOOP-15229](https://issues.apache.org/jira/browse/HADOOP-15229) *Add FileSystem builder-based openFile() API to match createFile()*

* No `opt(String key, long value)` method was available.
* the `withFileStatus(status)` call required a non-null parameter.
* Sole Filesystem to process options and file status was S3A;
* Only the s3a specific options were the S3 select and `fs.s3a.experimental.input.fadvise`
* S3A Filesystem raised `IllegalArgumentException` if a file status was passed in and the path of the filestatus did not match the path of the `openFile(path)` call.

This is the baseline implementation. To write code guaranteed to compile against this version, use the `opt(String, String)` and `must(String, String)` methods, converting numbers to string explicitly.

```
fs.open("s3a://bucket/file")
  .opt("fs.option.openfile.length", Long.toString(length))
  .build().get()
```

### Hadoop 3.3.5: standardization and expansion

[HADOOP-16202](https://issues.apache.org/jira/browse/HADOOP-16202) *Enhance openFile() for better read performance against object stores*

* `withFileStatus(null)` required to be accepted (and ignored)
* only the filename part of any supplied FileStatus path must match the filename passed in on `openFile(path)`.
* An `opt(String key, long value)` option was added. \*This is now deprecated as it caused regression
* Standard `fs.option.openfile` options defined.
* S3A FS to use openfile length option, seek start/end options not *yet* used.
* Azure ABFS connector takes a supplied `VersionedFileStatus` and omits any HEAD probe for the object.

### Hadoop 3.3.6: API change to address operator overload bugs.

new `optLong()`, `optDouble()`, `mustLong()` and `mustDouble()` builder methods.

* See [HADOOP-18724](https://issues.apache.org/jira/browse/HADOOP-18724) *Open file fails with NumberFormatException for S3AFileSystem*, which was somehow caused by the overloaded `opt(long)`.
* Specification updated to declare that unparseable numbers MUST be treated as “unset” and the default value used instead.

## Invariants

The `FutureDataInputStreamBuilder` interface does not require parameters or or the state of `FileSystem` until `build()` is invoked and/or during the asynchronous open operation itself.

Some aspects of the state of the filesystem, MAY be checked in the initial `openFile()` call, provided they are known to be invariants which will not change between `openFile()` and the `build().get()` sequence. For example, path validation.

## `Implementation-agnostic parameters.

### `FutureDataInputStreamBuilder bufferSize(int bufSize)`

Set the size of the buffer to be used.

### `FutureDataInputStreamBuilder withFileStatus(FileStatus status)`

A `FileStatus` instance which refers to the file being opened.

This MAY be used by implementations to short-circuit checks for the file, So potentially saving on remote calls especially to object stores.

Requirements:

* `status != null`
* `status.getPath().getName()` == the name of the file being opened.

The path validation MUST take place if the store uses the `FileStatus` when it opens files, and MAY be performed otherwise. The validation SHOULD be postponed until the `build()` operation.

This operation should be considered a hint to the filesystem.

If a filesystem implementation extends the `FileStatus` returned in its implementation MAY use this information when opening the file.

This is relevant with those stores which return version/etag information, -they MAY use this to guarantee that the file they opened is exactly the one returned in the listing.

The final `status.getPath().getName()` element of the supplied status MUST equal the name value of the path supplied to the `openFile(path)` call.

Filesystems MUST NOT validate the rest of the path. This is needed to support viewfs and other mount-point wrapper filesystems where schemas and paths are different. These often create their own FileStatus results

Preconditions

```
status == null or status.getPath().getName() == path.getName()
```

Filesystems MUST NOT require the class of `status` to equal that of any specific subclass their implementation returns in filestatus/list operations. This is to support wrapper filesystems and serialization/deserialization of the status.

### Set optional or mandatory parameters

```
FutureDataInputStreamBuilder opt(String key, String value)
FutureDataInputStreamBuilder opt(String key, int value)
FutureDataInputStreamBuilder opt(String key, boolean value)
FutureDataInputStreamBuilder optLong(String key, long value)
FutureDataInputStreamBuilder optDouble(String key, double value)
FutureDataInputStreamBuilder must(String key, String value)
FutureDataInputStreamBuilder must(String key, int value)
FutureDataInputStreamBuilder must(String key, boolean value)
FutureDataInputStreamBuilder mustLong(String key, long value)
FutureDataInputStreamBuilder mustDouble(String key, double value)
```

Set optional or mandatory parameters to the builder. Using `opt()` or `must()`, client can specify FS-specific parameters without inspecting the concrete type of `FileSystem`.

Example:

```
out = fs.openFile(path)
    .must("fs.option.openfile.read.policy", "random")
    .optLong("fs.http.connection.timeout", 30_000L)
    .withFileStatus(statusFromListing)
    .build()
    .get();
```

Here the read policy of `random` has been specified, with the requirement that the filesystem implementation must understand the option. An http-specific option has been supplied which may be interpreted by any store; If the filesystem opening the file does not recognize the option, it can safely be ignored.

### When to use `opt` versus `must`

The difference between `opt` versus `must` is how the FileSystem opening the file must react to an option which it does not recognize.

```
def must(name, value):
  if not name in known_keys:
    raise IllegalArgumentException
  if not name in supported_keys:
    raise UnsupportedException


def opt(name, value):
  if not name in known_keys:
     # ignore option
```

For any known key, the validation of the `value` argument MUST be the same irrespective of how the (key, value) pair was declared.

1. For a filesystem-specific option, it is the choice of the implementation how to validate the entry.
2. For standard options, the specification of what is a valid `value` is defined in this filesystem specification, validated through contract tests.

## Implementation Notes

Checking for supported options must be performed in the `build()` operation.

1. If a mandatory parameter declared via `must(key, value)`) is not recognized, `IllegalArgumentException` MUST be thrown.
2. If a mandatory parameter declared via `must(key, value)` relies on a feature which is recognized but not supported in the specific `FileSystem`/`FileContext` instance `UnsupportedException` MUST be thrown.

Parsing of numeric values SHOULD trim any string and if the value cannot be parsed as a number, downgrade to any default value supplied. This is to address [HADOOP-18724](https://issues.apache.org/jira/browse/HADOOP-18724) *Open file fails with NumberFormatException for S3AFileSystem*, which was cause by the overloaded `opt()` builder parameter binding to `opt(String, double)` rather than `opt(String, long)` when a long value was passed in.

The behavior of resolving the conflicts between the parameters set by builder methods (i.e., `bufferSize()`) and `opt()`/`must()` is as follows:

> The last option specified defines the value and its optional/mandatory state.

If the `FileStatus` option passed in `withFileStatus()` is used, implementations MUST accept all subclasses of `FileStatus`, including `LocatedFileStatus`, rather than just any FS-specific subclass implemented by the implementation (e.g `S3AFileStatus`). They MAY simply ignore those which are not the custom subclasses.

This is critical to ensure safe use of the feature: directory listing/ status serialization/deserialization can result in the `withFileStatus()` argument not being the custom subclass returned by the Filesystem instance’s own `getFileStatus()`, `listFiles()`, `listLocatedStatus()` calls, etc.

In such a situation the implementations must:

1. Verify that `status.getPath().getName()` matches the current `path.getName()` value. The rest of the path MUST NOT be validated.
2. Use any status fields as desired -for example the file length.

Even if not values of the status are used, the presence of the argument can be interpreted as the caller declaring that they believe the file to be present and of the given size.

## Builder interface

### `CompletableFuture<FSDataInputStream> build()`

Return an `CompletableFuture<FSDataInputStream>` which, when successfully completed, returns an input stream which can read data from the filesystem.

The `build()` operation MAY perform the validation of the file’s existence, its kind, so rejecting attempts to read from a directory or non-existent file. Alternatively \* file existence/status checks MAY be performed asynchronously within the returned `CompletableFuture<>`. \* file existence/status checks MAY be postponed until the first byte is read in any of the read such as `read()` or `PositionedRead`.

That is, the precondition `exists(FS, path)` and `isFile(FS, path)` are only guaranteed to have been met after the `get()` called on returned future and an attempt has been made to read the stream.

Thus, if even when file does not exist, or is a directory rather than a file, the following call MUST succeed, returning a `CompletableFuture` to be evaluated.

```
Path p = new Path("file://tmp/file-which-does-not-exist");

CompletableFuture<FSDataInputStream> future = p.getFileSystem(conf)
      .openFile(p)
      .build();
```

The inability to access/read a file MUST raise an `IOException`or subclass in either the future’s `get()` call, or, for late binding operations, when an operation to read data is invoked.

Therefore the following sequence SHALL fail when invoked on the `future` returned by the previous example.

```
  future.get().read();
```

Access permission checks have the same visibility requirements: permission failures MUST be delayed until the `get()` call and MAY be delayed into subsequent operations.

Note: some operations on the input stream, such as `seek()` may not attempt any IO at all. Such operations MAY NOT raise exceotions when interacting with nonexistent/unreadable files.

## Standard `openFile()` options since hadoop branch-3.3

These are options which `FileSystem` and `FileContext` implementation MUST recognise and MAY support by changing the behavior of their input streams as appropriate.

Hadoop 3.3.0 added the `openFile()` API; these standard options were defined in a later release. Therefore, although they are “well known”, unless confident that the application will only be executed against releases of Hadoop which knows of the options -applications SHOULD set the options via `opt()` calls rather than `must()`.

When opening a file through the `openFile()` builder API, callers MAY use both `.opt(key, value)` and `.must(key, value)` calls to set standard and filesystem-specific options.

If set as an `opt()` parameter, unsupported “standard” options MUST be ignored, as MUST unrecognized standard options.

If set as a `must()` parameter, unsupported “standard” options MUST be ignored. unrecognized standard options MUST be rejected.

The standard `openFile()` options are defined in `org.apache.hadoop.fs.OpenFileOptions`; they all SHALL start with `fs.option.openfile.`.

Note that while all `FileSystem`/`FileContext` instances SHALL support these options to the extent that `must()` declarations SHALL NOT fail, the implementations MAY support them to the extent of interpreting the values. This means that it is not a requirement for the stores to actually read the read policy or file length values and use them when opening files.

Unless otherwise stated, they SHOULD be viewed as hints.

Note: if a standard option is added such that if set but not supported would be an error, then implementations SHALL reject it. For example, the S3A filesystem client supports the ability to push down SQL commands. If something like that were ever standardized, then the use of the option, either in `opt()` or `must()` argument MUST be rejected for filesystems which don’t support the feature.

### Option: `fs.option.openfile.buffer.size`

Read buffer size in bytes.

This overrides the default value set in the configuration with the option `io.file.buffer.size`.

It is supported by all filesystem clients which allow for stream-specific buffer sizes to be set via `FileSystem.open(path, buffersize)`.

### Option: `fs.option.openfile.read.policy`

Declare the read policy of the input stream. This is a hint as to what the expected read pattern of an input stream will be. This MAY control readahead, buffering and other optimizations.

Sequential reads may be optimized with prefetching data and/or reading data in larger blocks. Some applications (e.g. distCp) perform sequential IO even over columnar data.

In contrast, random IO reads data in different parts of the file using a sequence of `seek()/read()` or via the `PositionedReadable` or `ByteBufferPositionedReadable` APIs.

Random IO performance may be best if little/no prefetching takes place, along with other possible optimizations

Queries over columnar formats such as Apache ORC and Apache Parquet perform such random IO; other data formats may be best read with sequential or whole-file policies.

What is key is that optimizing reads for seqential reads may impair random performance -and vice versa.

1. The seek policy is a hint; even if declared as a `must()` option, the filesystem MAY ignore it.
2. The interpretation/implementation of a policy is a filesystem specific behavior -and it may change with Hadoop releases and/or specific storage subsystems.
3. If a policy is not recognized, the filesystem client MUST ignore it.

| Policy | Meaning |
| --- | --- |
| `adaptive` | Any adaptive policy implemented by the store. |
| `avro` | This is an avro format which will be read sequentially |
| `csv` | This is CSV data which will be read sequentially |
| `default` | The default policy for this store. Generally “adaptive”. |
| `columnar` | This is any columnar format other than ORC/parquet. |
| `hbase` | This is an HBase Table |
| `json` | This is a UTF-8 JSON/JSON lines format which will be read sequentially |
| `orc` | This is an ORC file. Optimize for it. |
| `parquet` | This is a Parquet file. Optimize for it. |
| `random` | Optimize for random access. |
| `sequential` | Optimize for sequential access. |
| `vector` | The Vectored IO API is intended to be used. |
| `whole-file` | The whole file will be read. |

Choosing the wrong read policy for an input source may be inefficient but never fatal.

A list of read policies MAY be supplied; the first one recognized/supported by the filesystem SHALL be the one used. This allows for configurations which are compatible across versions. A policy `parquet, columnar, vector, random, adaptive` will use the parquet policy for any filesystem aware of it, falling back to `columnar`, `vector`, `random` and finally `adaptive`. The S3A connector will recognize the `random` since Hadoop 3.3.5 (i.e. since the `openFile()` API was added), and `vector` from Hadoop 3.4.0.

The S3A and ABFS input streams both implement the [IOStatisticsSource](iostatistics.html) API, and can be queried for their IO Performance.

*Tip:* log the `toString()` value of input streams at `DEBUG`. The S3A and ABFS Input Streams log read statistics, which can provide insight about whether reads are being performed efficiently or not.

*Futher reading*

* [Linux fadvise()](https://linux.die.net/man/2/fadvise).
* [Windows `CreateFile()`](https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea#caching-behavior)

#### Read Policy `adaptive`

Try to adapt the seek policy to the read pattern of the application.

The `normal` policy of the S3A client and the sole policy supported by the `wasb:` client are both adaptive -they assume sequential IO, but once a backwards seek/positioned read call is made the stream switches to random IO.

Other filesystem implementations may wish to adopt similar strategies, and/or extend the algorithms to detect forward seeks and/or switch from random to sequential IO if that is considered more efficient.

Adaptive read policies are the absence of the ability to declare the seek policy in the `open()` API, so requiring it to be declared, if configurable, in the cluster/application configuration. However, the switch from sequential to random seek policies may be exensive.

When applications explicitly set the `fs.option.openfile.read.policy` option, if they know their read plan, they SHOULD declare which policy is most appropriate.

#### Read Policy `default`

The default policy for the filesystem instance. Implementation/installation-specific.

#### Read Policy `sequential`

Expect sequential reads from the first byte read to the end of the file/until the stream is closed.

#### Read Policy `random`

Expect `seek()/read()` sequences, or use of `PositionedReadable` or `ByteBufferPositionedReadable` APIs.

#### Read Policy `vector`

This declares that the caller intends to use the Vectored read API of [HADOOP-11867](https://issues.apache.org/jira/browse/HADOOP-11867) *Add a high-performance vectored read API*.

This is a hint: it is not a requirement when using the API. It does inform the implemenations that the stream should be configured for optimal vectored IO performance, if such a feature has been implemented.

It is *not* exclusive: the same stream may still be used for classic `InputStream` and `PositionedRead` API calls. Implementations SHOULD use the `random` read policy with these operations.

#### Read Policy `whole-file`

This declares that the whole file is to be read end-to-end; the file system client is free to enable whatever strategies maximise performance for this. In particular, larger ranged reads/GETs can deliver high bandwidth by reducing socket/TLS setup costs and providing a connection long-lived enough for TCP flow control to determine the optimal download rate.

Strategies can include:

* Initiate an HTTP GET of the entire file in `openFile()` operation.
* Prefech data in large blocks, possibly in parallel read operations.

Applications which know that the entire file is to be read from an opened stream SHOULD declare this read policy.

#### Read Policy `columnar`

Declare that the data is some (unspecific) columnar format and that read sequencies should be expected to be random IO of whole column stripes/rowgroups, possibly fetching associated column statistics first, to determine whether a scan of a stripe/rowgroup can be skipped entirely.

#### File Format Read Policies `parquet`, and `orc`

These are read policies which declare that the file is of a specific columnar format and that the input stream MAY be optimized for reading from these.

In particular \* File footers may be fetched and cached. \* Vector IO and random IO SHOULD be expected.

These read policies are a Hadoop 3.4.x addition, so applications and libraries targeting multiple versions, SHOULD list their fallback policies if these are not recognized, e.g. request a policy such as `parquet, vector, random`.

#### File format Read Policies `avro`, `json` and `csv`

These are read policies which declare that the file is of a specific sequential format and that the input stream MAY be optimized for reading from these.

These read policies are a Hadoop 3.4.x addition, so applications and libraries targeting multiple versions, SHOULD list their fallback policies if these are not recognized, e.g. request a policy such as `avro, sequential`.

#### File Format Read Policy `hbase`

The file is an HBase table. Use whatever policy is appropriate for these files, where `random` is what should be used unless there are specific optimizations related to HBase.

### Option: `fs.option.openfile.length`: `Long`

Declare the length of a file.

This can be used by clients to skip querying a remote store for the size of/existence of a file when opening it, similar to declaring a file status through the `withFileStatus()` option.

If supported by a filesystem connector, this option MUST be interpreted as declaring the minimum length of the file:

1. If the value is negative, the option SHALL be considered unset.
2. It SHALL NOT be an error if the actual length of the file is greater than this value.
3. `read()`, `seek()` and positioned read calls MAY use a position across/beyond this length but below the actual length of the file. Implementations MAY raise `EOFExceptions` in such cases, or they MAY return data.

If this option is used by the FileSystem implementation

*Implementor’s Notes*

* A value of `fs.option.openfile.length` < 0 MUST be ignored.
* If a file status is supplied along with a value in `fs.opt.openfile.length`; the file status values take precedence.

### Options: `fs.option.openfile.split.start` and `fs.option.openfile.split.end`: `Long`

Declare the start and end of the split when a file has been split for processing in pieces.

1. If a value is negative, the option SHALL be considered unset.
2. Filesystems MAY assume that the length of the file is greater than or equal to the value of `fs.option.openfile.split.end`.
3. And that they MAY raise an exception if the client application reads past the value set in `fs.option.openfile.split.end`.
4. The pair of options MAY be used to optimise the read plan, such as setting the content range for GET requests, or using the split end as an implicit declaration of the guaranteed minimum length of the file.
5. If both options are set, and the split start is declared as greater than the split end, then the split start SHOULD just be reset to zero, rather than rejecting the operation.

The split end value can provide a hint as to the end of the input stream. The split start can be used to optimize any initial read offset for filesystem clients.

\*Note for implementors: applications will read past the end of a split when they need to read to the end of a record/line which begins before the end of the split.

Therefore clients MUST be allowed to `seek()`/`read()` past the length set in `fs.option.openfile.split.end` if the file is actually longer than that value.

### Option: `fs.option.openfile.footer.cache`: `Boolean`

Should a footer be cached?

* This is a hint for clients which cache footers.
* If a format with known footers are is declared in the read policy, the default footer cache policy of that file type SHALL be used.

This option allows for that default policy to be overridden. This is recommended if an application wishes to explicitly declare that Parquet/ORC files are being read -but does not want or need the filesystem stream to cache any footer because the application itself does such caching. Duplicating footer caching is inefficient and if there is memory/memory cache conflict, potentially counter-efficient.

## S3A-specific options

The S3A Connector supports custom options for readahead and seek policy.

| Name | Type | Meaning |
| --- | --- | --- |
| `fs.s3a.readahead.range` | `long` | readahead range in bytes |
| `fs.s3a.experimental.input.fadvise` | `String` | seek policy. Superceded by `fs.option.openfile.read.policy` |
| `fs.s3a.input.async.drain.threshold` | `long` | threshold to switch to asynchronous draining of the stream. (Since 3.3.5) |

If the option set contains a SQL statement in the `fs.s3a.select.sql` statement, then the file is opened as an S3 Select query. Consult the S3A documentation for more details.

## ABFS-specific options

The ABFS Connector supports custom input stream options.

| Name | Type | Meaning |
| --- | --- | --- |
| `fs.azure.buffered.pread.disable` | `boolean` | disable caching on the positioned read operations. |

Disables caching on data read through the [PositionedReadable](fsdatainputstream.html#PositionedReadable) APIs.

Consult the ABFS Documentation for more details.

## Examples

#### Declaring seek policy and split limits when opening a file.

Here is an example from a proof of concept `org.apache.parquet.hadoop.util.HadoopInputFile` reader which uses a (nullable) file status and a split start/end.

The `FileStatus` value is always passed in -but if it is null, then the split end is used to declare the length of the file.

```
protected SeekableInputStream newStream(Path path, FileStatus stat,
     long splitStart, long splitEnd)
     throws IOException {

   FutureDataInputStreamBuilder builder = fs.openFile(path)
   .opt("fs.option.openfile.read.policy", "vector, random")
   .withFileStatus(stat);

   builder.optLong("fs.option.openfile.split.start", splitStart);
   builder.optLong("fs.option.openfile.split.end", splitEnd);
   CompletableFuture<FSDataInputStream> streamF = builder.build();
   return HadoopStreams.wrap(FutureIO.awaitFuture(streamF));
}
```

As a result, whether driven directly by a file listing, or when opening a file from a query plan of `(path, splitStart, splitEnd)`, there is no need to probe the remote store for the length of the file. When working with remote object stores, this can save tens to hundreds of milliseconds, even if such a probe is done asynchronously.

If both the file length and the split end is set, then the file length MUST be considered “more” authoritative, that is it really SHOULD be defining the file length. If the split end is set, the caller MAY ot read past it.

The `CompressedSplitLineReader` can read past the end of a split if it is partway through processing a compressed record. That is: it assumes an incomplete record read means that the file length is greater than the split length, and that it MUST read the entirety of the partially read record. Other readers may behave similarly.

Therefore

1. File length as supplied in a `FileStatus` or in `fs.option.openfile.length` SHALL set the strict upper limit on the length of a file
2. The split end as set in `fs.option.openfile.split.end` MUST be viewed as a hint, rather than the strict end of the file.

### Opening a file with both standard and non-standard options

Standard and non-standard options MAY be combined in the same `openFile()` operation.

```
Future<FSDataInputStream> f = openFile(path)
  .must("fs.option.openfile.read.policy", "random, adaptive")
  .opt("fs.s3a.readahead.range", 1024 * 1024)
  .build();

FSDataInputStream is = f.get();
```

The option set in `must()` MUST be understood, or at least recognized and ignored by all filesystems. In this example, S3A-specific option MAY be ignored by all other filesystem clients.

### Opening a file with older releases

Not all hadoop releases recognize the `fs.option.openfile.read.policy` option.

The option can be safely used in application code if it is added via the `opt()` builder argument, as it will be treated as an unknown optional key which can then be discarded.

```
Future<FSDataInputStream> f = openFile(path)
  .opt("fs.option.openfile.read.policy", "vector, random, adaptive")
  .build();

FSDataInputStream is = f.get();
```

*Note 1* if the option name is set by a reference to a constant in `org.apache.hadoop.fs.Options.OpenFileOptions`, then the program will not link against versions of Hadoop without the specific option. Therefore for resilient linking against older releases -use a copy of the value.

*Note 2* as option validation is performed in the FileSystem connector, a third-party connector designed to work with multiple hadoop versions MAY NOT support the option.

### Passing options in to MapReduce

Hadoop MapReduce will automatically read MR Job Options with the prefixes `mapreduce.job.input.file.option.` and `mapreduce.job.input.file.must.` prefixes, and apply these values as `.opt()` and `must()` respectively, after remove the mapreduce-specific prefixes.

This makes passing options in to MR jobs straightforward. For example, to declare that a job should read its data using random IO:

```
JobConf jobConf = (JobConf) job.getConfiguration()
jobConf.set(
    "mapreduce.job.input.file.option.fs.option.openfile.read.policy",
    "random");
```

### MapReduce input format propagating options

An example of a record reader passing in options to the file it opens.

```
  public void initialize(InputSplit genericSplit,
                     TaskAttemptContext context) throws IOException {
    FileSplit split = (FileSplit)genericSplit;
    Configuration job = context.getConfiguration();
    start = split.getStart();
    end = start + split.getLength();
    Path file = split.getPath();

    // open the file and seek to the start of the split
    FutureDataInputStreamBuilder builder =
      file.getFileSystem(job).openFile(file);
    // the start and end of the split may be used to build
    // an input strategy.
    builder.optLong("fs.option.openfile.split.start", start);
    builder.optLong("fs.option.openfile.split.end", end);
    FutureIO.propagateOptions(builder, job,
        "mapreduce.job.input.file.option",
        "mapreduce.job.input.file.must");

    fileIn = FutureIO.awaitFuture(builder.build());
    fileIn.seek(start)
    /* Rest of the operation on the opened stream */
  }
```

### `FileContext.openFile`

From `org.apache.hadoop.fs.AvroFSInput`; a file is opened with sequential input. Because the file length has already been probed for, the length is passed down

```
  public AvroFSInput(FileContext fc, Path p) throws IOException {
    FileStatus status = fc.getFileStatus(p);
    this.len = status.getLen();
    this.stream = awaitFuture(fc.openFile(p)
        .opt("fs.option.openfile.read.policy",
            "sequential")
        .optLong("fs.option.openfile.length",
            Long.toString(status.getLen()))
        .build());
    fc.open(p);
  }
```

In this example, the length is passed down as a string (via `Long.toString()`) rather than directly as a long. This is to ensure that the input format will link against versions of $Hadoop which do not have the `opt(String, long)` and `must(String, long)` builder parameters. Similarly, the values are passed as optional, so that if unrecognized the application will still succeed.

### Example: reading a whole file

This is from `org.apache.hadoop.util.JsonSerialization`.

Its `load(FileSystem, Path, FileStatus)` method \* declares the whole file is to be read end to end. \* passes down the file status

```
public T load(FileSystem fs,
        Path path,
        status)
        throws IOException {

 try (FSDataInputStream dataInputStream =
          awaitFuture(fs.openFile(path)
              .opt("fs.option.openfile.read.policy", "whole-file")
              .withFileStatus(status)
              .build())) {
   return fromJsonStream(dataInputStream);
 } catch (JsonProcessingException e) {
   throw new PathIOException(path.toString(),
       "Failed to read JSON file " + e, e);
 }
}
```

---
