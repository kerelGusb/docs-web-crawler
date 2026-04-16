# Introduction[#](#introduction "Link to this heading")

DataFusion is a very fast, extensible query engine for building
high-quality data-centric systems in [Rust](http://rustlang.org),
using the [Apache Arrow](https://arrow.apache.org) in-memory format.
DataFusion originated as part of the [Apache Arrow](https://arrow.apache.org/)
project.

DataFusion offers SQL and Dataframe APIs, excellent [performance](https://benchmark.clickhouse.com/), built-in support for CSV, Parquet, JSON, and Avro, [python bindings](https://github.com/apache/datafusion-python), extensive customization, a great community, and more.

## Project Goals[#](#project-goals "Link to this heading")

DataFusion aims to be the query engine of choice for new, fast
data centric systems such as databases, dataframe libraries, machine
learning and streaming applications by leveraging the unique features
of [Rust](https://www.rust-lang.org/) and [Apache
Arrow](https://arrow.apache.org/).

## Features[#](#features "Link to this heading")

* Feature-rich [SQL support](https://datafusion.apache.org/user-guide/sql/index.html) and [DataFrame API](https://datafusion.apache.org/user-guide/dataframe.html)
* Blazingly fast, vectorized, multithreaded, streaming execution engine.
* Native support for Parquet, CSV, JSON, and Avro file formats. Support
  for custom file formats and non-file datasources via the `TableProvider` trait.
* Many extension points: user defined scalar/aggregate/window functions, DataSources, SQL,
  other query languages, custom plan and execution nodes, optimizer passes, and more.
* Streaming, asynchronous IO directly from popular object stores, including AWS S3,
  Azure Blob Storage, and Google Cloud Storage (Other storage systems are supported via the
  `ObjectStore` trait).
* [Excellent Documentation](https://docs.rs/datafusion/latest) and a
  [welcoming community](https://datafusion.apache.org/contributor-guide/communication.html).
* A state of the art query optimizer with expression coercion and
  simplification, projection and filter pushdown, sort and distribution
  aware optimizations, automatic join reordering, and more.
* Permissive Apache 2.0 License, predictable and well understood
  [Apache Software Foundation](https://www.apache.org/) governance.
* Implementation in [Rust](https://www.rust-lang.org/), a modern
  system language with development productivity similar to Java or
  Golang, the performance of C++, and [loved by programmers
  everywhere](https://insights.stackoverflow.com/survey/2021#technology-most-loved-dreaded-and-wanted).
* Support for [Substrait](https://substrait.io/) query plans, to
  easily pass plans across language and system boundaries.

## Use Cases[#](#use-cases "Link to this heading")

DataFusion can be used without modification as an embedded SQL
engine or can be customized and used as a foundation for
building new systems.

While most current use cases are “analytic” or (throughput) some
components of DataFusion such as the plan representations, are
suitable for “streaming” and “transaction” style systems (low
latency).

Here are some example systems built using DataFusion:

* Specialized Analytical Database systems such as [HoraeDB](https://github.com/apache/incubator-horaedb) and more general Apache Spark like system such as [Ballista](https://github.com/apache/datafusion-ballista)
* New query language engines such as [prql-query](https://github.com/prql/prql-query) and accelerators such as [VegaFusion](https://vegafusion.io/)
* Research platform for new Database Systems, such as [Flock](https://github.com/flock-lab/flock)
* SQL support to another library, such as [Vortex](https://vortex.dev/)
* Streaming data platforms such as [Synnada](https://synnada.ai/)
* Tools for reading / sorting / transcoding Parquet, CSV, AVRO, and JSON files such as [qv](https://github.com/timvw/qv)
* Native Spark runtime replacement such as [Auron](https://github.com/apache/auron)
* Distributed data cache to boost GPU utilization of AI workloads with [Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/user-guides/data-cache/)

By using DataFusion, projects are freed to focus on their specific
features, and avoid reimplementing general (but still necessary)
features such as an expression representation, standard optimizations,
parallelized streaming execution plans, file format support, etc.

## Known Users[#](#known-users "Link to this heading")

Here are some active projects using DataFusion:

* [Arroyo](https://github.com/ArroyoSystems/arroyo) Distributed stream processing engine in Rust
* [ArkFlow](https://github.com/arkflow-rs/arkflow) High-performance Rust stream processing engine
* [Auron](https://github.com/apache/auron) The Auron accelerator for big data engine (e.g., Spark, Flink) leverages native vectorized execution to accelerate query processing
* [Ballista](https://github.com/apache/datafusion-ballista) Distributed SQL Query Engine
* [CnosDB](https://github.com/cnosdb/cnosdb) Open Source Distributed Time Series Database
* [Comet](https://github.com/apache/datafusion-comet) Apache Spark native query execution plugin
* [Cube Store](https://github.com/cube-js/cube.js/tree/master/rust) Cube’s universal semantic layer platform is the next evolution of OLAP technology for AI, BI, spreadsheets, and embedded analytics
* [datafusion-dft](https://github.com/datafusion-contrib/datafusion-dft) Batteries included CLI, TUI, and server implementations for DataFusion.
* [dbt Fusion engine](https://github.com/dbt-labs/dbt-fusion) The dbt Fusion engine, written in Rust, designed for speed and correctness with a native SQL understanding across DWH SQL dialects.
* [delta-rs](https://github.com/delta-io/delta-rs) Native Rust implementation of Delta Lake
* [EDB Postgres Lakehouse](https://www.enterprisedb.com/products/analytics) built with [Seafowl](https://github.com/splitgraph/seafowl)
* [Feldera](https://github.com/feldera/feldera) Fast query engine for incremental computation
* [Funnel](https://funnel.io/) Data Platform powering Marketing Intelligence applications.
* [GlareDB](https://github.com/GlareDB/glaredb) Fast SQL database for querying and analyzing distributed data.
* [GreptimeDB](https://github.com/GreptimeTeam/greptimedb) Open Source & Cloud Native Distributed Time Series Database
* [hiop](https://hiop.io) Serverless Data Logistic Platform
* [HoraeDB](https://github.com/apache/incubator-horaedb) Distributed Time-Series Database
* [Iceberg-rust](https://github.com/apache/iceberg-rust) Rust implementation of Apache Iceberg
* [InfluxDB](https://github.com/influxdata/influxdb) Time Series Database
* [Kamu](https://github.com/kamu-data/kamu-cli) Planet-scale streaming data pipeline
* [Kubeflow Trainer](https://github.com/kubeflow/trainer) Kubernetes-native project designed for
  scalable LLMs fine-tuning and distributed AI model training.
* [LakeSoul](https://github.com/lakesoul-io/LakeSoul) Open source LakeHouse framework with native IO in Rust.
* [Lance](https://github.com/lancedb/lance) Modern columnar data format for ML
* [OpenObserve](https://github.com/openobserve/openobserve) Distributed cloud native observability platform
* [ParadeDB](https://github.com/paradedb/paradedb) PostgreSQL for Search & Analytics
* [Parseable](https://github.com/parseablehq/parseable) Log storage and observability platform
* [Polygon.io](https://polygon.io/) Stock Market API
* [qv](https://github.com/timvw/qv) Quickly view your data
* [R2 Query Engine](https://blog.cloudflare.com/r2-sql-deep-dive/) Cloudflare’s distributed engine for querying data in Iceberg Catalogs
* [rerun.io](https://rerun.io/) Visualize and query robotics logs and transform them into training data.
* [Restate](https://github.com/restatedev) Easily build resilient applications using distributed durable async/await
* [ROAPI](https://github.com/roapi/roapi) Create full-fledged APIs for slowly moving datasets without writing a single line of code
* [Sail](https://github.com/lakehq/sail) Unifying stream, batch and AI workloads with Apache Spark compatibility
* [SedonaDB](https://github.com/apache/sedona-db) A single-node analytical database engine with geospatial as a first-class citizen
* [Sleeper](https://github.com/gchq/sleeper) Serverless, cloud-native, log-structured merge tree based, scalable key-value store
* [Spice.ai](https://github.com/spiceai/spiceai) Building blocks for data-driven AI applications
* [Synnada](https://synnada.ai/) Streaming-first framework for data products
* [VegaFusion](https://vegafusion.io/) Server-side acceleration for the [Vega](https://vega.github.io/) visualization grammar
* [Vortex](https://vortex.dev/) An extensible, state of the art columnar file format
* [Telemetry](https://telemetry.sh/) Structured logging made easy
* [Xorq](https://github.com/xorq-labs/xorq/) Xorq is a multi-engine batch transformation framework built on Ibis, DataFusion and Arrow
* [KalamDB](https://github.com/jamals86/KalamDB) SQL-first realtime state database for AI agents, chat products, and multi-tenant SaaS.

Here are some less active projects that used DataFusion:

* [bdt](https://github.com/datafusion-contrib/bdt) Boring Data Tool
* [Cloudfuse Buzz](https://github.com/cloudfuse-io/buzz-rust)
* [Dask SQL](https://github.com/dask-contrib/dask-sql) Distributed SQL query engine in Python
* [Exon](https://github.com/wheretrue/exon) Analysis toolkit for life-science applications
* [Flock](https://github.com/flock-lab/flock)
* [Tensorbase](https://github.com/tensorbase/tensorbase)

If you know of another project, please submit a PR to add a link!

## Integrations and Extensions[#](#integrations-and-extensions "Link to this heading")

There are a number of community projects that extend DataFusion or
provide integrations with other systems, some of which are described below:

### Language Bindings[#](#language-bindings "Link to this heading")

* [datafusion-c](https://github.com/datafusion-contrib/datafusion-c)
* [datafusion-python](https://github.com/apache/datafusion-python)
* [datafusion-ruby](https://github.com/datafusion-contrib/datafusion-ruby)
* [datafusion-java](https://github.com/datafusion-contrib/datafusion-java)

### Integrations[#](#integrations "Link to this heading")

* [datafusion-bigtable](https://github.com/datafusion-contrib/datafusion-bigtable)
* [datafusion-catalogprovider-glue](https://github.com/datafusion-contrib/datafusion-catalogprovider-glue)
* [datafusion-federation](https://github.com/datafusion-contrib/datafusion-federation)

## Why DataFusion?[#](#why-datafusion "Link to this heading")

* *High Performance*: Leveraging Rust and Arrow’s memory model, DataFusion is very fast.
* *Easy to Connect*: Being part of the Apache Arrow ecosystem (Arrow, Parquet, and Flight), DataFusion works well with the rest of the big data ecosystem
* *Easy to Embed*: Allowing extension at almost any point in its design, and published regularly as a crate on [crates.io](http://crates.io), DataFusion can be integrated and tailored for your specific usecase.
* *High Quality*: Extensively tested, both by itself and with the rest of the Arrow ecosystem, DataFusion can and is used as the foundation for production systems.

## Rust Version Compatibility Policy[#](#rust-version-compatibility-policy "Link to this heading")

The Rust toolchain releases are tracked at [Rust Versions](https://releases.rs) and follow
[semantic versioning](https://semver.org/). A Rust toolchain release can be identified
by a version string like `1.80.0`, or more generally `major.minor.patch`.

DataFusion supports the last 4 stable Rust minor versions released and any such versions released within the last 4 months.

For example, given the releases `1.78.0`, `1.79.0`, `1.80.0`, `1.80.1` and `1.81.0` DataFusion will support 1.78.0, which is 3 minor versions prior to the most minor recent `1.81`.

Note: If a Rust hotfix is released for the current MSRV, the MSRV will be updated to the specific minor version that includes all applicable hotfixes preceding other policies.

DataFusion enforces MSRV policy using a [MSRV CI Check](https://github.com/search?q=repo%3Aapache%2Fdatafusion+rust-version+language%3ATOML+path%3A%2F%5ECargo.toml%2F&amp;type=code)

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/introduction.md)

[Show Source](../_sources/user-guide/introduction.md.txt)

---
# Overview[#](#overview "Link to this heading")

DataFusion CLI (`datafusion-cli`) is an interactive command-line utility for executing
SQL queries against any supported data files.

While intended as an example of how to use DataFusion, `datafusion-cli` offers a
full range of SQL and support reading and writing CSV, Parquet, JSON, Arrow and
Avro, from local files, directories, or remote locations such as S3.

Here is an example of how to run a SQL query against a local file, `hits.parquet`:

```
$ datafusion-cli
DataFusion CLI v37.0.0
> select count(distinct "URL") from 'hits.parquet';
+----------------------------------+
| COUNT(DISTINCT hits.parquet.URL) |
+----------------------------------+
| 18342019                         |
+----------------------------------+
1 row(s) fetched.
Elapsed 1.969 seconds.
```

For more information, see the [Installation](installation.html), [Usage Guide](usage.html)
and [Data Sources](datasources.html) sections.

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/cli/overview.md)

[Show Source](../../_sources/user-guide/cli/overview.md.txt)

---
# Format Options[#](#format-options "Link to this heading")

DataFusion supports customizing how data is read from or written to disk as a result of a `COPY`, `INSERT INTO`, or `CREATE EXTERNAL TABLE` statements. There are a few special options, file format (e.g., CSV or Parquet) specific options, and Parquet column-specific options. In some cases, Options can be specified in multiple ways with a set order of precedence.

## Specifying Options and Order of Precedence[#](#specifying-options-and-order-of-precedence "Link to this heading")

Format-related options can be specified in three ways, in decreasing order of precedence:

* `CREATE EXTERNAL TABLE` syntax
* `COPY` option tuples
* Session-level config defaults

For a list of supported session-level config defaults, see [Configuration Settings](../configs.html). These defaults apply to all operations but have the lowest level of precedence.

If creating an external table, table-specific format options can be specified when the table is created using the `OPTIONS` clause:

```
CREATE EXTERNAL TABLE
  my_table(a bigint, b bigint)
  STORED AS csv
  LOCATION '/tmp/my_csv_table/'
  OPTIONS(
    NULL_VALUE 'NAN',
    'has_header' 'true',
    'format.delimiter' ';'
  );
```

When running `INSERT INTO my_table ...`, the options from the `CREATE TABLE` will be respected (e.g., gzip compression, special delimiter, and header row included). Note that compression, header, and delimiter settings can also be specified within the `OPTIONS` tuple list. Dedicated syntax within the SQL statement always takes precedence over arbitrary option tuples, so if both are specified, the `OPTIONS` setting will be ignored.

For example, with the table defined above, running the following command:

```
INSERT INTO my_table VALUES(1,2);
```

Results in a new CSV file with the specified options:

```
$ cat /tmp/my_csv_table/bmC8zWFvLMtWX68R_0.csv
a;b
1;2
```

Finally, options can be passed when running a `COPY` command.

```
COPY source_table
  TO 'test/table_with_options'
  PARTITIONED BY (column3, column4)
  OPTIONS (
    format parquet,
    compression snappy,
    'compression::column1' 'zstd(5)',
  )
```

In this example, we write the entire `source_table` out to a folder of Parquet files. One Parquet file will be written in parallel to the folder for each partition in the query. The next option `compression` set to `snappy` indicates that unless otherwise specified, all columns should use the snappy compression codec. The option `compression::col1` sets an override, so that the column `col1` in the Parquet file will use the ZSTD compression codec with compression level `5`. In general, Parquet options that support column-specific settings can be specified with the syntax `OPTION::COLUMN.NESTED.PATH`.

# Available Options[#](#available-options "Link to this heading")

## JSON Format Options[#](#json-format-options "Link to this heading")

The following options are available when reading or writing JSON files. Note: If any unsupported option is specified, an error will be raised and the query will fail.

| Option | Description | Default Value |
| --- | --- | --- |
| COMPRESSION | Sets the compression that should be applied to the entire JSON file. Supported values are GZIP, BZIP2, XZ, ZSTD, and UNCOMPRESSED. | UNCOMPRESSED |

**Example:**

```
CREATE EXTERNAL TABLE t(a int)
STORED AS JSON
LOCATION '/tmp/foo/'
OPTIONS('COMPRESSION' 'gzip');
```

## CSV Format Options[#](#csv-format-options "Link to this heading")

The following options are available when reading or writing CSV files. Note: If any unsupported option is specified, an error will be raised and the query will fail.

| Option | Description | Default Value |
| --- | --- | --- |
| COMPRESSION | Sets the compression that should be applied to the entire CSV file. Supported values are GZIP, BZIP2, XZ, ZSTD, and UNCOMPRESSED. | UNCOMPRESSED |
| HAS\_HEADER | Sets if the CSV file should include column headers. If not set, uses session or system default. | None |
| DELIMITER | Sets the character which should be used as the column delimiter within the CSV file. | `,` (comma) |
| QUOTE | Sets the character which should be used for quoting values within the CSV file. | `"` (double quote) |
| TERMINATOR | Sets the character which should be used as the line terminator within the CSV file. | None |
| ESCAPE | Sets the character which should be used for escaping special characters within the CSV file. | None |
| DOUBLE\_QUOTE | Sets if quotes within quoted fields should be escaped by doubling them (e.g., `"aaa""bbb"`). | None |
| NEWLINES\_IN\_VALUES | Sets if newlines in quoted values are supported. If not set, uses session or system default. | None |
| DATE\_FORMAT | Sets the format that dates should be encoded in within the CSV file. | None |
| DATETIME\_FORMAT | Sets the format that datetimes should be encoded in within the CSV file. | None |
| TIMESTAMP\_FORMAT | Sets the format that timestamps should be encoded in within the CSV file. | None |
| TIMESTAMP\_TZ\_FORMAT | Sets the format that timestamps with timezone should be encoded in within the CSV file. | None |
| TIME\_FORMAT | Sets the format that times should be encoded in within the CSV file. | None |
| NULL\_VALUE | Sets the string which should be used to indicate null values within the CSV file. | None |
| NULL\_REGEX | Sets the regex pattern to match null values when loading CSVs. | None |
| SCHEMA\_INFER\_MAX\_REC | Sets the maximum number of records to scan to infer the schema. If set to 0, schema inference is disabled and all fields will be inferred as Utf8 (string) type. | None |
| COMMENT | Sets the character which should be used to indicate comment lines in the CSV file. | None |

**Example:**

```
CREATE EXTERNAL TABLE t (col1 varchar, col2 int, col3 boolean)
STORED AS CSV
LOCATION '/tmp/foo/'
OPTIONS('DELIMITER' '|', 'HAS_HEADER' 'true', 'NEWLINES_IN_VALUES' 'true');
```

## Parquet Format Options[#](#parquet-format-options "Link to this heading")

The following options are available when reading or writing Parquet files. If any unsupported option is specified, an error will be raised and the query will fail. If a column-specific option is specified for a column that does not exist, the option will be ignored without error.

| Option | Can be Column Specific? | Description | OPTIONS Key | Default Value |
| --- | --- | --- | --- | --- |
| COMPRESSION | Yes | Sets the internal Parquet **compression codec** for data pages, optionally including the compression level. Applies globally if set without `::col`, or specifically to a column if set using `'compression::column_name'`. Valid values: `uncompressed`, `snappy`, `gzip(level)`, `brotli(level)`, `lz4`, `zstd(level)`, `lz4_raw`. | `'compression'` or `'compression::col'` | zstd(3) |
| ENCODING | Yes | Sets the **encoding** scheme for data pages. Valid values: `plain`, `plain_dictionary`, `rle`, `bit_packed`, `delta_binary_packed`, `delta_length_byte_array`, `delta_byte_array`, `rle_dictionary`, `byte_stream_split`. Use key `'encoding'` or `'encoding::col'` in OPTIONS. | `'encoding'` or `'encoding::col'` | None |
| DICTIONARY\_ENABLED | Yes | Sets whether dictionary encoding should be enabled globally or for a specific column. | `'dictionary_enabled'` or `'dictionary_enabled::col'` | true |
| STATISTICS\_ENABLED | Yes | Sets the level of statistics to write (`none`, `chunk`, `page`). | `'statistics_enabled'` or `'statistics_enabled::col'` | page |
| BLOOM\_FILTER\_ENABLED | Yes | Sets whether a bloom filter should be written for a specific column. | `'bloom_filter_enabled::column_name'` | None |
| BLOOM\_FILTER\_FPP | Yes | Sets bloom filter false positive probability (global or per column). | `'bloom_filter_fpp'` or `'bloom_filter_fpp::col'` | None |
| BLOOM\_FILTER\_NDV | Yes | Sets bloom filter number of distinct values (global or per column). | `'bloom_filter_ndv'` or `'bloom_filter_ndv::col'` | None |
| MAX\_ROW\_GROUP\_SIZE | No | Sets the maximum number of rows per row group. Larger groups require more memory but can improve compression and scan efficiency. | `'max_row_group_size'` | 1048576 |
| ENABLE\_PAGE\_INDEX | No | If true, reads the Parquet data page level metadata (the Page Index), if present, to reduce I/O and decoding. | `'enable_page_index'` | true |
| PRUNING | No | If true, enables row group pruning based on min/max statistics. | `'pruning'` | true |
| SKIP\_METADATA | No | If true, skips optional embedded metadata in the file schema. | `'skip_metadata'` | true |
| METADATA\_SIZE\_HINT | No | Sets the size hint (in bytes) for fetching Parquet file metadata. | `'metadata_size_hint'` | None |
| PUSHDOWN\_FILTERS | No | If true, enables filter pushdown during Parquet decoding. | `'pushdown_filters'` | false |
| REORDER\_FILTERS | No | If true, enables heuristic reordering of filters during Parquet decoding. | `'reorder_filters'` | false |
| SCHEMA\_FORCE\_VIEW\_TYPES | No | If true, reads Utf8/Binary columns as view types. | `'schema_force_view_types'` | true |
| BINARY\_AS\_STRING | No | If true, reads Binary columns as strings. | `'binary_as_string'` | false |
| DATA\_PAGESIZE\_LIMIT | No | Sets best effort maximum size of data page in bytes. | `'data_pagesize_limit'` | 1048576 |
| DATA\_PAGE\_ROW\_COUNT\_LIMIT | No | Sets best effort maximum number of rows in data page. | `'data_page_row_count_limit'` | 20000 |
| DICTIONARY\_PAGE\_SIZE\_LIMIT | No | Sets best effort maximum dictionary page size, in bytes. | `'dictionary_page_size_limit'` | 1048576 |
| WRITE\_BATCH\_SIZE | No | Sets write\_batch\_size in rows. | `'write_batch_size'` | 1024 |
| WRITER\_VERSION | No | Sets the Parquet writer version (`1.0` or `2.0`). | `'writer_version'` | 1.0 |
| SKIP\_ARROW\_METADATA | No | If true, skips writing Arrow schema information into the Parquet file metadata. | `'skip_arrow_metadata'` | false |
| CREATED\_BY | No | Sets the “created by” string in the Parquet file metadata. | `'created_by'` | datafusion version X.Y.Z |
| COLUMN\_INDEX\_TRUNCATE\_LENGTH | No | Sets the length (in bytes) to truncate min/max values in column indexes. | `'column_index_truncate_length'` | 64 |
| STATISTICS\_TRUNCATE\_LENGTH | No | Sets statistics truncate length. | `'statistics_truncate_length'` | None |
| BLOOM\_FILTER\_ON\_WRITE | No | Sets whether bloom filters should be written for all columns by default (can be overridden per column). | `'bloom_filter_on_write'` | false |
| ALLOW\_SINGLE\_FILE\_PARALLELISM | No | Enables parallel serialization of columns in a single file. | `'allow_single_file_parallelism'` | true |
| MAXIMUM\_PARALLEL\_ROW\_GROUP\_WRITERS | No | Maximum number of parallel row group writers. | `'maximum_parallel_row_group_writers'` | 1 |
| MAXIMUM\_BUFFERED\_RECORD\_BATCHES\_PER\_STREAM | No | Maximum number of buffered record batches per stream. | `'maximum_buffered_record_batches_per_stream'` | 2 |
| KEY\_VALUE\_METADATA | No (Key is specific) | Adds custom key-value pairs to the file metadata. Use the format `'metadata::your_key_name' 'your_value'`. Multiple entries allowed. | `'metadata::key_name'` | None |

**Example:**

```
CREATE EXTERNAL TABLE t (id bigint, value double, category varchar)
STORED AS PARQUET
LOCATION '/tmp/parquet_data/'
OPTIONS(
  'COMPRESSION::user_id' 'snappy',
  'ENCODING::col_a' 'delta_binary_packed',
  'MAX_ROW_GROUP_SIZE' '1000000',
  'BLOOM_FILTER_ENABLED::id' 'true'
);
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/format_options.md)

[Show Source](../../_sources/user-guide/sql/format_options.md.txt)

---
# Scalar Functions[#](#scalar-functions "Link to this heading")

## Math Functions[#](#math-functions "Link to this heading")

* [abs](#abs)
* [acos](#acos)
* [acosh](#acosh)
* [asin](#asin)
* [asinh](#asinh)
* [atan](#atan)
* [atan2](#atan2)
* [atanh](#atanh)
* [cbrt](#cbrt)
* [ceil](#ceil)
* [cos](#cos)
* [cosh](#cosh)
* [cot](#cot)
* [degrees](#degrees)
* [exp](#exp)
* [factorial](#factorial)
* [floor](#floor)
* [gcd](#gcd)
* [isnan](#isnan)
* [iszero](#iszero)
* [lcm](#lcm)
* [ln](#ln)
* [log](#log)
* [log10](#log10)
* [log2](#log2)
* [nanvl](#nanvl)
* [pi](#pi)
* [pow](#pow)
* [power](#power)
* [radians](#radians)
* [random](#random)
* [round](#round)
* [signum](#signum)
* [sin](#sin)
* [sinh](#sinh)
* [sqrt](#sqrt)
* [tan](#tan)
* [tanh](#tanh)
* [trunc](#trunc)

### `abs`[#](#abs "Link to this heading")

Returns the absolute value of a number.

```
abs(numeric_expression)
```

#### Arguments[#](#arguments "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#example "Link to this heading")

```
> SELECT abs(-5);
+----------+
| abs(-5)  |
+----------+
| 5        |
+----------+
```

### `acos`[#](#acos "Link to this heading")

Returns the arc cosine or inverse cosine of a number.

```
acos(numeric_expression)
```

#### Arguments[#](#id1 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id2 "Link to this heading")

```
> SELECT acos(1);
+----------+
| acos(1)  |
+----------+
| 0.0      |
+----------+
```

### `acosh`[#](#acosh "Link to this heading")

Returns the area hyperbolic cosine or inverse hyperbolic cosine of a number.

```
acosh(numeric_expression)
```

#### Arguments[#](#id3 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id4 "Link to this heading")

```
> SELECT acosh(2);
+------------+
| acosh(2)   |
+------------+
| 1.31696    |
+------------+
```

### `asin`[#](#asin "Link to this heading")

Returns the arc sine or inverse sine of a number.

```
asin(numeric_expression)
```

#### Arguments[#](#id5 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id6 "Link to this heading")

```
> SELECT asin(0.5);
+------------+
| asin(0.5)  |
+------------+
| 0.5235988  |
+------------+
```

### `asinh`[#](#asinh "Link to this heading")

Returns the area hyperbolic sine or inverse hyperbolic sine of a number.

```
asinh(numeric_expression)
```

#### Arguments[#](#id7 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id8 "Link to this heading")

```
> SELECT asinh(1);
+------------+
| asinh(1)   |
+------------+
| 0.8813736  |
+------------+
```

### `atan`[#](#atan "Link to this heading")

Returns the arc tangent or inverse tangent of a number.

```
atan(numeric_expression)
```

#### Arguments[#](#id9 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id10 "Link to this heading")

```
    > SELECT atan(1);
+-----------+
| atan(1)   |
+-----------+
| 0.7853982 |
+-----------+
```

### `atan2`[#](#atan2 "Link to this heading")

Returns the arc tangent or inverse tangent of `expression_y / expression_x`.

```
atan2(expression_y, expression_x)
```

#### Arguments[#](#id11 "Link to this heading")

* **expression\_y**: First numeric expression to operate on.
  Can be a constant, column, or function, and any combination of arithmetic operators.
* **expression\_x**: Second numeric expression to operate on.
  Can be a constant, column, or function, and any combination of arithmetic operators.

#### Example[#](#id12 "Link to this heading")

```
> SELECT atan2(1, 1);
+------------+
| atan2(1,1) |
+------------+
| 0.7853982  |
+------------+
```

### `atanh`[#](#atanh "Link to this heading")

Returns the area hyperbolic tangent or inverse hyperbolic tangent of a number.

```
atanh(numeric_expression)
```

#### Arguments[#](#id13 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id14 "Link to this heading")

```
    > SELECT atanh(0.5);
+-------------+
| atanh(0.5)  |
+-------------+
| 0.5493061   |
+-------------+
```

### `cbrt`[#](#cbrt "Link to this heading")

Returns the cube root of a number.

```
cbrt(numeric_expression)
```

#### Arguments[#](#id15 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id16 "Link to this heading")

```
> SELECT cbrt(27);
+-----------+
| cbrt(27)  |
+-----------+
| 3.0       |
+-----------+
```

### `ceil`[#](#ceil "Link to this heading")

Returns the nearest integer greater than or equal to a number.

```
ceil(numeric_expression)
```

#### Arguments[#](#id17 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id18 "Link to this heading")

```
> SELECT ceil(3.14);
+------------+
| ceil(3.14) |
+------------+
| 4.0        |
+------------+
```

### `cos`[#](#cos "Link to this heading")

Returns the cosine of a number.

```
cos(numeric_expression)
```

#### Arguments[#](#id19 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id20 "Link to this heading")

```
> SELECT cos(0);
+--------+
| cos(0) |
+--------+
| 1.0    |
+--------+
```

### `cosh`[#](#cosh "Link to this heading")

Returns the hyperbolic cosine of a number.

```
cosh(numeric_expression)
```

#### Arguments[#](#id21 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id22 "Link to this heading")

```
> SELECT cosh(1);
+-----------+
| cosh(1)   |
+-----------+
| 1.5430806 |
+-----------+
```

### `cot`[#](#cot "Link to this heading")

Returns the cotangent of a number.

```
cot(numeric_expression)
```

#### Arguments[#](#id23 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id24 "Link to this heading")

```
> SELECT cot(1);
+---------+
| cot(1)  |
+---------+
| 0.64209 |
+---------+
```

### `degrees`[#](#degrees "Link to this heading")

Converts radians to degrees.

```
degrees(numeric_expression)
```

#### Arguments[#](#id25 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id26 "Link to this heading")

```
    > SELECT degrees(pi());
+------------+
| degrees(0) |
+------------+
| 180.0      |
+------------+
```

### `exp`[#](#exp "Link to this heading")

Returns the base-e exponential of a number.

```
exp(numeric_expression)
```

#### Arguments[#](#id27 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id28 "Link to this heading")

```
> SELECT exp(1);
+---------+
| exp(1)  |
+---------+
| 2.71828 |
+---------+
```

### `factorial`[#](#factorial "Link to this heading")

Factorial. Returns 1 if value is less than 2.

```
factorial(numeric_expression)
```

#### Arguments[#](#id29 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id30 "Link to this heading")

```
> SELECT factorial(5);
+---------------+
| factorial(5)  |
+---------------+
| 120           |
+---------------+
```

### `floor`[#](#floor "Link to this heading")

Returns the nearest integer less than or equal to a number.

```
floor(numeric_expression)
```

#### Arguments[#](#id31 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id32 "Link to this heading")

```
> SELECT floor(3.14);
+-------------+
| floor(3.14) |
+-------------+
| 3.0         |
+-------------+
```

### `gcd`[#](#gcd "Link to this heading")

Returns the greatest common divisor of `expression_x` and `expression_y`. Returns 0 if both inputs are zero.

```
gcd(expression_x, expression_y)
```

#### Arguments[#](#id33 "Link to this heading")

* **expression\_x**: First numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_y**: Second numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id34 "Link to this heading")

```
> SELECT gcd(48, 18);
+------------+
| gcd(48,18) |
+------------+
| 6          |
+------------+
```

### `isnan`[#](#isnan "Link to this heading")

Returns true if a given number is +NaN or -NaN otherwise returns false.

```
isnan(numeric_expression)
```

#### Arguments[#](#id35 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id36 "Link to this heading")

```
> SELECT isnan(1);
+----------+
| isnan(1) |
+----------+
| false    |
+----------+
```

### `iszero`[#](#iszero "Link to this heading")

Returns true if a given number is +0.0 or -0.0 otherwise returns false.

```
iszero(numeric_expression)
```

#### Arguments[#](#id37 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id38 "Link to this heading")

```
> SELECT iszero(0);
+------------+
| iszero(0)  |
+------------+
| true       |
+------------+
```

### `lcm`[#](#lcm "Link to this heading")

Returns the least common multiple of `expression_x` and `expression_y`. Returns 0 if either input is zero.

```
lcm(expression_x, expression_y)
```

#### Arguments[#](#id39 "Link to this heading")

* **expression\_x**: First numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_y**: Second numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id40 "Link to this heading")

```
> SELECT lcm(4, 5);
+----------+
| lcm(4,5) |
+----------+
| 20       |
+----------+
```

### `ln`[#](#ln "Link to this heading")

Returns the natural logarithm of a number.

```
ln(numeric_expression)
```

#### Arguments[#](#id41 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id42 "Link to this heading")

```
> SELECT ln(2.71828);
+-------------+
| ln(2.71828) |
+-------------+
| 1.0         |
+-------------+
```

### `log`[#](#log "Link to this heading")

Returns the base-x logarithm of a number. Can either provide a specified base, or if omitted then takes the base-10 of a number.

```
log(base, numeric_expression)
log(numeric_expression)
```

#### Arguments[#](#id43 "Link to this heading")

* **base**: Base numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id44 "Link to this heading")

```
> SELECT log(10);
+---------+
| log(10) |
+---------+
| 1.0     |
+---------+
```

### `log10`[#](#log10 "Link to this heading")

Returns the base-10 logarithm of a number.

```
log10(numeric_expression)
```

#### Arguments[#](#id45 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id46 "Link to this heading")

```
> SELECT log10(100);
+-------------+
| log10(100)  |
+-------------+
| 2.0         |
+-------------+
```

### `log2`[#](#log2 "Link to this heading")

Returns the base-2 logarithm of a number.

```
log2(numeric_expression)
```

#### Arguments[#](#id47 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id48 "Link to this heading")

```
> SELECT log2(8);
+-----------+
| log2(8)   |
+-----------+
| 3.0       |
+-----------+
```

### `nanvl`[#](#nanvl "Link to this heading")

Returns the first argument if it’s not *NaN*.
Returns the second argument otherwise.

```
nanvl(expression_x, expression_y)
```

#### Arguments[#](#id49 "Link to this heading")

* **expression\_x**: Numeric expression to return if it’s not *NaN*. Can be a constant, column, or function, and any combination of arithmetic operators.
* **expression\_y**: Numeric expression to return if the first expression is *NaN*. Can be a constant, column, or function, and any combination of arithmetic operators.

#### Example[#](#id50 "Link to this heading")

```
> SELECT nanvl(0, 5);
+------------+
| nanvl(0,5) |
+------------+
| 0          |
+------------+
```

### `pi`[#](#pi "Link to this heading")

Returns an approximate value of π.

```
pi()
```

### `pow`[#](#pow "Link to this heading")

*Alias of [power](#power).*

### `power`[#](#power "Link to this heading")

Returns a base expression raised to the power of an exponent.

```
power(base, exponent)
```

#### Arguments[#](#id51 "Link to this heading")

* **base**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **exponent**: Exponent numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id52 "Link to this heading")

```
> SELECT power(2, 3);
+-------------+
| power(2,3)  |
+-------------+
| 8           |
+-------------+
```

#### Aliases[#](#aliases "Link to this heading")

* pow

### `radians`[#](#radians "Link to this heading")

Converts degrees to radians.

```
radians(numeric_expression)
```

#### Arguments[#](#id53 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id54 "Link to this heading")

```
> SELECT radians(180);
+----------------+
| radians(180)   |
+----------------+
| 3.14159265359  |
+----------------+
```

### `random`[#](#random "Link to this heading")

Returns a random float value in the range [0, 1).
The random seed is unique to each row.

```
random()
```

#### Example[#](#id55 "Link to this heading")

```
> SELECT random();
+------------------+
| random()         |
+------------------+
| 0.7389238902938  |
+------------------+
```

### `round`[#](#round "Link to this heading")

Rounds a number to the nearest integer.

```
round(numeric_expression[, decimal_places])
```

#### Arguments[#](#id56 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **decimal\_places**: Optional. The number of decimal places to round to. Defaults to 0.

#### Example[#](#id57 "Link to this heading")

```
> SELECT round(3.14159);
+--------------+
| round(3.14159)|
+--------------+
| 3.0          |
+--------------+
```

### `signum`[#](#signum "Link to this heading")

Returns the sign of a number.
Negative numbers return `-1`.
Zero and positive numbers return `1`.

```
signum(numeric_expression)
```

#### Arguments[#](#id58 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id59 "Link to this heading")

```
> SELECT signum(-42);
+-------------+
| signum(-42) |
+-------------+
| -1          |
+-------------+
```

### `sin`[#](#sin "Link to this heading")

Returns the sine of a number.

```
sin(numeric_expression)
```

#### Arguments[#](#id60 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id61 "Link to this heading")

```
> SELECT sin(0);
+----------+
| sin(0)   |
+----------+
| 0.0      |
+----------+
```

### `sinh`[#](#sinh "Link to this heading")

Returns the hyperbolic sine of a number.

```
sinh(numeric_expression)
```

#### Arguments[#](#id62 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id63 "Link to this heading")

```
> SELECT sinh(1);
+-----------+
| sinh(1)   |
+-----------+
| 1.1752012 |
+-----------+
```

### `sqrt`[#](#sqrt "Link to this heading")

Returns the square root of a number.

```
sqrt(numeric_expression)
```

#### Arguments[#](#id64 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

### `tan`[#](#tan "Link to this heading")

Returns the tangent of a number.

```
tan(numeric_expression)
```

#### Arguments[#](#id65 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id66 "Link to this heading")

```
> SELECT tan(pi()/4);
+--------------+
| tan(PI()/4)  |
+--------------+
| 1.0          |
+--------------+
```

### `tanh`[#](#tanh "Link to this heading")

Returns the hyperbolic tangent of a number.

```
tanh(numeric_expression)
```

#### Arguments[#](#id67 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id68 "Link to this heading")

```
  > SELECT tanh(20);
  +----------+
  | tanh(20) |
  +----------+
  | 1.0      |
  +----------+
```

### `trunc`[#](#trunc "Link to this heading")

Truncates a number to a whole number or truncated to the specified decimal places.

```
trunc(numeric_expression[, decimal_places])
```

#### Arguments[#](#id69 "Link to this heading")

* **numeric\_expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **decimal\_places**: Optional. The number of decimal places to
  truncate to. Defaults to 0 (truncate to a whole number). If
  `decimal_places` is a positive integer, truncates digits to the
  right of the decimal point. If `decimal_places` is a negative
  integer, replaces digits to the left of the decimal point with `0`.

#### Example[#](#id70 "Link to this heading")

```
> SELECT trunc(42.738);
+----------------+
| trunc(42.738)  |
+----------------+
| 42             |
+----------------+
```

## Conditional Functions[#](#conditional-functions "Link to this heading")

* [coalesce](#coalesce)
* [greatest](#greatest)
* [ifnull](#ifnull)
* [least](#least)
* [nullif](#nullif)
* [nvl](#nvl)
* [nvl2](#nvl2)

### `coalesce`[#](#coalesce "Link to this heading")

Returns the first of its arguments that is not *null*. Returns *null* if all arguments are *null*. This function is often used to substitute a default value for *null* values.

```
coalesce(expression1[, ..., expression_n])
```

#### Arguments[#](#id71 "Link to this heading")

* **expression1, expression\_n**: Expression to use if previous expressions are *null*. Can be a constant, column, or function, and any combination of arithmetic operators. Pass as many expression arguments as necessary.

#### Example[#](#id72 "Link to this heading")

```
> select coalesce(null, null, 'datafusion');
+----------------------------------------+
| coalesce(NULL,NULL,Utf8("datafusion")) |
+----------------------------------------+
| datafusion                             |
+----------------------------------------+
```

### `greatest`[#](#greatest "Link to this heading")

Returns the greatest value in a list of expressions. Returns *null* if all expressions are *null*.

```
greatest(expression1[, ..., expression_n])
```

#### Arguments[#](#id73 "Link to this heading")

* **expression1, expression\_n**: Expressions to compare and return the greatest value.. Can be a constant, column, or function, and any combination of arithmetic operators. Pass as many expression arguments as necessary.

#### Example[#](#id74 "Link to this heading")

```
> select greatest(4, 7, 5);
+---------------------------+
| greatest(4,7,5)           |
+---------------------------+
| 7                         |
+---------------------------+
```

### `ifnull`[#](#ifnull "Link to this heading")

*Alias of [nvl](#nvl).*

### `least`[#](#least "Link to this heading")

Returns the smallest value in a list of expressions. Returns *null* if all expressions are *null*.

```
least(expression1[, ..., expression_n])
```

#### Arguments[#](#id75 "Link to this heading")

* **expression1, expression\_n**: Expressions to compare and return the smallest value. Can be a constant, column, or function, and any combination of arithmetic operators. Pass as many expression arguments as necessary.

#### Example[#](#id76 "Link to this heading")

```
> select least(4, 7, 5);
+---------------------------+
| least(4,7,5)              |
+---------------------------+
| 4                         |
+---------------------------+
```

### `nullif`[#](#nullif "Link to this heading")

Returns *null* if *expression1* equals *expression2*; otherwise it returns *expression1*.
This can be used to perform the inverse operation of [`coalesce`](#coalesce).

```
nullif(expression1, expression2)
```

#### Arguments[#](#id77 "Link to this heading")

* **expression1**: Expression to compare and return if equal to expression2. Can be a constant, column, or function, and any combination of operators.
* **expression2**: Expression to compare to expression1. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id78 "Link to this heading")

```
> select nullif('datafusion', 'data');
+-----------------------------------------+
| nullif(Utf8("datafusion"),Utf8("data")) |
+-----------------------------------------+
| datafusion                              |
+-----------------------------------------+
> select nullif('datafusion', 'datafusion');
+-----------------------------------------------+
| nullif(Utf8("datafusion"),Utf8("datafusion")) |
+-----------------------------------------------+
|                                               |
+-----------------------------------------------+
```

### `nvl`[#](#nvl "Link to this heading")

Returns *expression2* if *expression1* is NULL otherwise it returns *expression1* and *expression2* is not evaluated. This function can be used to substitute a default value for NULL values.

```
nvl(expression1, expression2)
```

#### Arguments[#](#id79 "Link to this heading")

* **expression1**: Expression to return if not null. Can be a constant, column, or function, and any combination of operators.
* **expression2**: Expression to return if expr1 is null. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id80 "Link to this heading")

```
> select nvl(null, 'a');
+---------------------+
| nvl(NULL,Utf8("a")) |
+---------------------+
| a                   |
+---------------------+\
> select nvl('b', 'a');
+--------------------------+
| nvl(Utf8("b"),Utf8("a")) |
+--------------------------+
| b                        |
+--------------------------+
```

#### Aliases[#](#id81 "Link to this heading")

* ifnull

### `nvl2`[#](#nvl2 "Link to this heading")

Returns *expression2* if *expression1* is not NULL; otherwise it returns *expression3*.

```
nvl2(expression1, expression2, expression3)
```

#### Arguments[#](#id82 "Link to this heading")

* **expression1**: Expression to test for null. Can be a constant, column, or function, and any combination of operators.
* **expression2**: Expression to return if expr1 is not null. Can be a constant, column, or function, and any combination of operators.
* **expression3**: Expression to return if expr1 is null. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id83 "Link to this heading")

```
> select nvl2(null, 'a', 'b');
+--------------------------------+
| nvl2(NULL,Utf8("a"),Utf8("b")) |
+--------------------------------+
| b                              |
+--------------------------------+
> select nvl2('data', 'a', 'b');
+----------------------------------------+
| nvl2(Utf8("data"),Utf8("a"),Utf8("b")) |
+----------------------------------------+
| a                                      |
+----------------------------------------+
```

## String Functions[#](#string-functions "Link to this heading")

* [ascii](#ascii)
* [bit\_length](#bit-length)
* [btrim](#btrim)
* [char\_length](#char-length)
* [character\_length](#character-length)
* [chr](#chr)
* [concat](#concat)
* [concat\_ws](#concat-ws)
* [contains](#contains)
* [ends\_with](#ends-with)
* [find\_in\_set](#find-in-set)
* [initcap](#initcap)
* [instr](#instr)
* [left](#left)
* [length](#length)
* [levenshtein](#levenshtein)
* [lower](#lower)
* [lpad](#lpad)
* [ltrim](#ltrim)
* [octet\_length](#octet-length)
* [overlay](#overlay)
* [position](#position)
* [repeat](#repeat)
* [replace](#replace)
* [reverse](#reverse)
* [right](#right)
* [rpad](#rpad)
* [rtrim](#rtrim)
* [split\_part](#split-part)
* [starts\_with](#starts-with)
* [strpos](#strpos)
* [substr](#substr)
* [substr\_index](#substr-index)
* [substring](#substring)
* [substring\_index](#substring-index)
* [to\_hex](#to-hex)
* [translate](#translate)
* [trim](#trim)
* [upper](#upper)
* [uuid](#uuid)

### `ascii`[#](#ascii "Link to this heading")

Returns the first Unicode scalar value of a string.

```
ascii(str)
```

#### Arguments[#](#id84 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id85 "Link to this heading")

```
> select ascii('abc');
+--------------------+
| ascii(Utf8("abc")) |
+--------------------+
| 97                 |
+--------------------+
> select ascii('🚀');
+-------------------+
| ascii(Utf8("🚀")) |
+-------------------+
| 128640            |
+-------------------+
```

**Related functions**:

* [chr](#chr)

### `bit_length`[#](#bit-length "Link to this heading")

Returns the bit length of a string.

```
bit_length(str)
```

#### Arguments[#](#id86 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id87 "Link to this heading")

```
> select bit_length('datafusion');
+--------------------------------+
| bit_length(Utf8("datafusion")) |
+--------------------------------+
| 80                             |
+--------------------------------+
```

**Related functions**:

* [length](#length)
* [octet\_length](#octet-length)

### `btrim`[#](#btrim "Link to this heading")

Trims the specified trim string from the start and end of a string. If no trim string is provided, all spaces are removed from the start and end of the input string.

```
btrim(str[, trim_str])
```

#### Arguments[#](#id88 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **trim\_str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators. *Default is a space.*

#### Example[#](#id89 "Link to this heading")

```
> select btrim('__datafusion____', '_');
+-------------------------------------------+
| btrim(Utf8("__datafusion____"),Utf8("_")) |
+-------------------------------------------+
| datafusion                                |
+-------------------------------------------+
```

#### Alternative Syntax[#](#alternative-syntax "Link to this heading")

```
trim(BOTH trim_str FROM str)
```

```
trim(trim_str FROM str)
```

#### Aliases[#](#id90 "Link to this heading")

* trim

**Related functions**:

* [ltrim](#ltrim)
* [rtrim](#rtrim)

### `char_length`[#](#char-length "Link to this heading")

*Alias of [character\_length](#character-length).*

### `character_length`[#](#character-length "Link to this heading")

Returns the number of characters in a string.

```
character_length(str)
```

#### Arguments[#](#id91 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id92 "Link to this heading")

```
> select character_length('Ångström');
+------------------------------------+
| character_length(Utf8("Ångström")) |
+------------------------------------+
| 8                                  |
+------------------------------------+
```

#### Aliases[#](#id93 "Link to this heading")

* length
* char\_length

**Related functions**:

* [bit\_length](#bit-length)
* [octet\_length](#octet-length)

### `chr`[#](#chr "Link to this heading")

Returns a string containing the character with the specified Unicode scalar value.

```
chr(expression)
```

#### Arguments[#](#id94 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id95 "Link to this heading")

```
> select chr(128640);
+--------------------+
| chr(Int64(128640)) |
+--------------------+
| 🚀                 |
+--------------------+
```

**Related functions**:

* [ascii](#ascii)

### `concat`[#](#concat "Link to this heading")

Concatenates multiple strings together.

```
concat(str[, ..., str_n])
```

#### Arguments[#](#id96 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **str\_n**: Subsequent string expressions to concatenate.

#### Example[#](#id97 "Link to this heading")

```
> select concat('data', 'f', 'us', 'ion');
+-------------------------------------------------------+
| concat(Utf8("data"),Utf8("f"),Utf8("us"),Utf8("ion")) |
+-------------------------------------------------------+
| datafusion                                            |
+-------------------------------------------------------+
```

**Related functions**:

* [concat\_ws](#concat-ws)

### `concat_ws`[#](#concat-ws "Link to this heading")

Concatenates multiple strings together with a specified separator.

```
concat_ws(separator, str[, ..., str_n])
```

#### Arguments[#](#id98 "Link to this heading")

* **separator**: Separator to insert between concatenated strings.
* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **str\_n**: Subsequent string expressions to concatenate.

#### Example[#](#id99 "Link to this heading")

```
> select concat_ws('_', 'data', 'fusion');
+--------------------------------------------------+
| concat_ws(Utf8("_"),Utf8("data"),Utf8("fusion")) |
+--------------------------------------------------+
| data_fusion                                      |
+--------------------------------------------------+
```

**Related functions**:

* [concat](#concat)

### `contains`[#](#contains "Link to this heading")

Return true if search\_str is found within string (case-sensitive).

```
contains(str, search_str)
```

#### Arguments[#](#id100 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **search\_str**: The string to search for in str.

#### Example[#](#id101 "Link to this heading")

```
> select contains('the quick brown fox', 'row');
+---------------------------------------------------+
| contains(Utf8("the quick brown fox"),Utf8("row")) |
+---------------------------------------------------+
| true                                              |
+---------------------------------------------------+
```

### `ends_with`[#](#ends-with "Link to this heading")

Tests if a string ends with a substring.

```
ends_with(str, substr)
```

#### Arguments[#](#id102 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **substr**: Substring to test for.

#### Example[#](#id103 "Link to this heading")

```
>  select ends_with('datafusion', 'soin');
+--------------------------------------------+
| ends_with(Utf8("datafusion"),Utf8("soin")) |
+--------------------------------------------+
| false                                      |
+--------------------------------------------+
> select ends_with('datafusion', 'sion');
+--------------------------------------------+
| ends_with(Utf8("datafusion"),Utf8("sion")) |
+--------------------------------------------+
| true                                       |
+--------------------------------------------+
```

### `find_in_set`[#](#find-in-set "Link to this heading")

Returns a value in the range of 1 to N if the string str is in the string list strlist consisting of N substrings.

```
find_in_set(str, strlist)
```

#### Arguments[#](#id104 "Link to this heading")

* **str**: String expression to find in strlist.
* **strlist**: A string list is a string composed of substrings separated by , characters.

#### Example[#](#id105 "Link to this heading")

```
> select find_in_set('b', 'a,b,c,d');
+----------------------------------------+
| find_in_set(Utf8("b"),Utf8("a,b,c,d")) |
+----------------------------------------+
| 2                                      |
+----------------------------------------+
```

### `initcap`[#](#initcap "Link to this heading")

Capitalizes the first character in each word in the input string. Words are delimited by non-alphanumeric characters.

```
initcap(str)
```

#### Arguments[#](#id106 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id107 "Link to this heading")

```
> select initcap('apache datafusion');
+------------------------------------+
| initcap(Utf8("apache datafusion")) |
+------------------------------------+
| Apache Datafusion                  |
+------------------------------------+
```

**Related functions**:

* [lower](#lower)
* [upper](#upper)

### `instr`[#](#instr "Link to this heading")

*Alias of [strpos](#strpos).*

### `left`[#](#left "Link to this heading")

Returns a specified number of characters from the left side of a string.

```
left(str, n)
```

#### Arguments[#](#id108 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **n**: Number of characters to return.

#### Example[#](#id109 "Link to this heading")

```
> select left('datafusion', 4);
+-----------------------------------+
| left(Utf8("datafusion"),Int64(4)) |
+-----------------------------------+
| data                              |
+-----------------------------------+
```

**Related functions**:

* [right](#right)

### `length`[#](#length "Link to this heading")

*Alias of [character\_length](#character-length).*

### `levenshtein`[#](#levenshtein "Link to this heading")

Returns the [`Levenshtein distance`](https://en.wikipedia.org/wiki/Levenshtein_distance) between the two given strings.

```
levenshtein(str1, str2)
```

#### Arguments[#](#id110 "Link to this heading")

* **str1**: String expression to compute Levenshtein distance with str2.
* **str2**: String expression to compute Levenshtein distance with str1.

#### Example[#](#id111 "Link to this heading")

```
> select levenshtein('kitten', 'sitting');
+---------------------------------------------+
| levenshtein(Utf8("kitten"),Utf8("sitting")) |
+---------------------------------------------+
| 3                                           |
+---------------------------------------------+
```

### `lower`[#](#lower "Link to this heading")

Converts a string to lower-case.

```
lower(str)
```

#### Arguments[#](#id112 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id113 "Link to this heading")

```
> select lower('Ångström');
+-------------------------+
| lower(Utf8("Ångström")) |
+-------------------------+
| ångström                |
+-------------------------+
```

**Related functions**:

* [initcap](#initcap)
* [upper](#upper)

### `lpad`[#](#lpad "Link to this heading")

Pads the left side of a string with another string to a specified string length.

```
lpad(str, n[, padding_str])
```

#### Arguments[#](#id114 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **n**: String length to pad to. If the input string is longer than this length, it is truncated (on the right).
* **padding\_str**: Optional string expression to pad with. Can be a constant, column, or function, and any combination of string operators. *Default is a space.*

#### Example[#](#id115 "Link to this heading")

```
> select lpad('Dolly', 10, 'hello');
+---------------------------------------------+
| lpad(Utf8("Dolly"),Int64(10),Utf8("hello")) |
+---------------------------------------------+
| helloDolly                                  |
+---------------------------------------------+
```

**Related functions**:

* [rpad](#rpad)

### `ltrim`[#](#ltrim "Link to this heading")

Trims the specified trim string from the beginning of a string. If no trim string is provided, spaces are removed from the start of the input string.

```
ltrim(str[, trim_str])
```

#### Arguments[#](#id116 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **trim\_str**: String expression to trim from the beginning of the input string. Can be a constant, column, or function, and any combination of arithmetic operators. *Default is a space.*

#### Example[#](#id117 "Link to this heading")

```
> select ltrim('  datafusion  ');
+-------------------------------+
| ltrim(Utf8("  datafusion  ")) |
+-------------------------------+
| datafusion                    |
+-------------------------------+
> select ltrim('___datafusion___', '_');
+-------------------------------------------+
| ltrim(Utf8("___datafusion___"),Utf8("_")) |
+-------------------------------------------+
| datafusion___                             |
+-------------------------------------------+
```

#### Alternative Syntax[#](#id118 "Link to this heading")

```
trim(LEADING trim_str FROM str)
```

**Related functions**:

* [btrim](#btrim)
* [rtrim](#rtrim)

### `octet_length`[#](#octet-length "Link to this heading")

Returns the length of a string in bytes.

```
octet_length(str)
```

#### Arguments[#](#id119 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id120 "Link to this heading")

```
> select octet_length('Ångström');
+--------------------------------+
| octet_length(Utf8("Ångström")) |
+--------------------------------+
| 10                             |
+--------------------------------+
```

**Related functions**:

* [bit\_length](#bit-length)
* [length](#length)

### `overlay`[#](#overlay "Link to this heading")

Returns the string which is replaced by another string from the specified position and specified count length.

```
overlay(str PLACING substr FROM pos [FOR count])
```

#### Arguments[#](#id121 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **substr**: Substring to replace in str.
* **pos**: The start position to start the replace in str.
* **count**: The count of characters to be replaced from start position of str. If not specified, will use substr length instead.

#### Example[#](#id122 "Link to this heading")

```
> select overlay('Txxxxas' placing 'hom' from 2 for 4);
+--------------------------------------------------------+
| overlay(Utf8("Txxxxas"),Utf8("hom"),Int64(2),Int64(4)) |
+--------------------------------------------------------+
| Thomas                                                 |
+--------------------------------------------------------+
```

### `position`[#](#position "Link to this heading")

*Alias of [strpos](#strpos).*

### `repeat`[#](#repeat "Link to this heading")

Returns a string with an input string repeated a specified number.

```
repeat(str, n)
```

#### Arguments[#](#id123 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **n**: Number of times to repeat the input string.

#### Example[#](#id124 "Link to this heading")

```
> select repeat('data', 3);
+-------------------------------+
| repeat(Utf8("data"),Int64(3)) |
+-------------------------------+
| datadatadata                  |
+-------------------------------+
```

### `replace`[#](#replace "Link to this heading")

Replaces all occurrences of a specified substring in a string with a new substring.

```
replace(str, substr, replacement)
```

#### Arguments[#](#id125 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **substr**: Substring expression to replace in the input string. Substring expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **replacement**: Replacement substring expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id126 "Link to this heading")

```
> select replace('ABabbaBA', 'ab', 'cd');
+-------------------------------------------------+
| replace(Utf8("ABabbaBA"),Utf8("ab"),Utf8("cd")) |
+-------------------------------------------------+
| ABcdbaBA                                        |
+-------------------------------------------------+
```

### `reverse`[#](#reverse "Link to this heading")

Reverses the character order of a string.

```
reverse(str)
```

#### Arguments[#](#id127 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id128 "Link to this heading")

```
> select reverse('datafusion');
+-----------------------------+
| reverse(Utf8("datafusion")) |
+-----------------------------+
| noisufatad                  |
+-----------------------------+
```

### `right`[#](#right "Link to this heading")

Returns a specified number of characters from the right side of a string.

```
right(str, n)
```

#### Arguments[#](#id129 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **n**: Number of characters to return.

#### Example[#](#id130 "Link to this heading")

```
> select right('datafusion', 6);
+------------------------------------+
| right(Utf8("datafusion"),Int64(6)) |
+------------------------------------+
| fusion                             |
+------------------------------------+
```

**Related functions**:

* [left](#left)

### `rpad`[#](#rpad "Link to this heading")

Pads the right side of a string with another string to a specified string length.

```
rpad(str, n[, padding_str])
```

#### Arguments[#](#id131 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **n**: String length to pad to. If the input string is longer than this length, it is truncated.
* **padding\_str**: String expression to pad with. Can be a constant, column, or function, and any combination of string operators. *Default is a space.*

#### Example[#](#id132 "Link to this heading")

```
>  select rpad('datafusion', 20, '_-');
+-----------------------------------------------+
| rpad(Utf8("datafusion"),Int64(20),Utf8("_-")) |
+-----------------------------------------------+
| datafusion_-_-_-_-_-                          |
+-----------------------------------------------+
```

**Related functions**:

* [lpad](#lpad)

### `rtrim`[#](#rtrim "Link to this heading")

Trims the specified trim string from the end of a string. If no trim string is provided, all spaces are removed from the end of the input string.

```
rtrim(str[, trim_str])
```

#### Arguments[#](#id133 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **trim\_str**: String expression to trim from the end of the input string. Can be a constant, column, or function, and any combination of arithmetic operators. *Default is a space.*

#### Example[#](#id134 "Link to this heading")

```
> select rtrim('  datafusion  ');
+-------------------------------+
| rtrim(Utf8("  datafusion  ")) |
+-------------------------------+
|   datafusion                  |
+-------------------------------+
> select rtrim('___datafusion___', '_');
+-------------------------------------------+
| rtrim(Utf8("___datafusion___"),Utf8("_")) |
+-------------------------------------------+
| ___datafusion                             |
+-------------------------------------------+
```

#### Alternative Syntax[#](#id135 "Link to this heading")

```
trim(TRAILING trim_str FROM str)
```

**Related functions**:

* [btrim](#btrim)
* [ltrim](#ltrim)

### `split_part`[#](#split-part "Link to this heading")

Splits a string based on a specified delimiter and returns the substring in the specified position.

```
split_part(str, delimiter, pos)
```

#### Arguments[#](#id136 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **delimiter**: String or character to split on.
* **pos**: Position of the part to return (counting from 1). Negative values count backward from the end of the string.

#### Example[#](#id137 "Link to this heading")

```
> select split_part('1.2.3.4.5', '.', 3);
+--------------------------------------------------+
| split_part(Utf8("1.2.3.4.5"),Utf8("."),Int64(3)) |
+--------------------------------------------------+
| 3                                                |
+--------------------------------------------------+
```

### `starts_with`[#](#starts-with "Link to this heading")

Tests if a string starts with a substring.

```
starts_with(str, substr)
```

#### Arguments[#](#id138 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **substr**: Substring to test for.

#### Example[#](#id139 "Link to this heading")

```
> select starts_with('datafusion','data');
+----------------------------------------------+
| starts_with(Utf8("datafusion"),Utf8("data")) |
+----------------------------------------------+
| true                                         |
+----------------------------------------------+
```

### `strpos`[#](#strpos "Link to this heading")

Returns the starting position of a specified substring in a string. Positions begin at 1. If the substring does not exist in the string, the function returns 0.

```
strpos(str, substr)
```

#### Arguments[#](#id140 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **substr**: Substring expression to search for.

#### Example[#](#id141 "Link to this heading")

```
> select strpos('datafusion', 'fus');
+----------------------------------------+
| strpos(Utf8("datafusion"),Utf8("fus")) |
+----------------------------------------+
| 5                                      |
+----------------------------------------+
```

#### Alternative Syntax[#](#id142 "Link to this heading")

```
position(substr in origstr)
```

#### Aliases[#](#id143 "Link to this heading")

* instr
* position

### `substr`[#](#substr "Link to this heading")

Extracts a substring of a specified number of characters from a specific starting position in a string.

```
substr(str, start_pos[, length])
```

#### Arguments[#](#id144 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **start\_pos**: Character position to start the substring at. The first character in the string has a position of 1. If the start position is less than 1, it is treated as if it is before the start of the string and the (absolute) number of characters before position 1 is subtracted from `length` (if given). For example, `substr('abc', -3, 6)` returns `'ab'`.
* **length**: Number of characters to extract. If not specified, returns the rest of the string after the start position.

#### Example[#](#id145 "Link to this heading")

```
> select substr('datafusion', 5, 3);
+----------------------------------------------+
| substr(Utf8("datafusion"),Int64(5),Int64(3)) |
+----------------------------------------------+
| fus                                          |
+----------------------------------------------+
```

#### Alternative Syntax[#](#id146 "Link to this heading")

```
substring(str from start_pos for length)
```

#### Aliases[#](#id147 "Link to this heading")

* substring

### `substr_index`[#](#substr-index "Link to this heading")

Returns the substring from str before count occurrences of the delimiter delim.
If count is positive, everything to the left of the final delimiter (counting from the left) is returned.
If count is negative, everything to the right of the final delimiter (counting from the right) is returned.

```
substr_index(str, delim, count)
```

#### Arguments[#](#id148 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **delim**: The string to find in str to split str.
* **count**: The number of times to search for the delimiter. Can be either a positive or negative number.

#### Example[#](#id149 "Link to this heading")

```
> select substr_index('www.apache.org', '.', 1);
+---------------------------------------------------------+
| substr_index(Utf8("www.apache.org"),Utf8("."),Int64(1)) |
+---------------------------------------------------------+
| www                                                     |
+---------------------------------------------------------+
> select substr_index('www.apache.org', '.', -1);
+----------------------------------------------------------+
| substr_index(Utf8("www.apache.org"),Utf8("."),Int64(-1)) |
+----------------------------------------------------------+
| org                                                      |
+----------------------------------------------------------+
```

#### Aliases[#](#id150 "Link to this heading")

* substring\_index

### `substring`[#](#substring "Link to this heading")

*Alias of [substr](#substr).*

### `substring_index`[#](#substring-index "Link to this heading")

*Alias of [substr\_index](#substr-index).*

### `to_hex`[#](#to-hex "Link to this heading")

Converts an integer to a hexadecimal string.

```
to_hex(int)
```

#### Arguments[#](#id151 "Link to this heading")

* **int**: Integer expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id152 "Link to this heading")

```
> select to_hex(12345689);
+-------------------------+
| to_hex(Int64(12345689)) |
+-------------------------+
| bc6159                  |
+-------------------------+
```

### `translate`[#](#translate "Link to this heading")

Performs character-wise substitution based on a mapping.

```
translate(str, from, to)
```

#### Arguments[#](#id153 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **from**: The characters to be replaced.
* **to**: The characters to replace them with. Each character in **from** that is found in **str** is replaced by the character at the same index in **to**. Any characters in **from** that don’t have a corresponding character in **to** are removed. If a character appears more than once in **from**, the first occurrence determines the mapping.

#### Example[#](#id154 "Link to this heading")

```
> select translate('twice', 'wic', 'her');
+--------------------------------------------------+
| translate(Utf8("twice"),Utf8("wic"),Utf8("her")) |
+--------------------------------------------------+
| there                                            |
+--------------------------------------------------+
```

### `trim`[#](#trim "Link to this heading")

*Alias of [btrim](#btrim).*

### `upper`[#](#upper "Link to this heading")

Converts a string to upper-case.

```
upper(str)
```

#### Arguments[#](#id155 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id156 "Link to this heading")

```
> select upper('dataFusion');
+---------------------------+
| upper(Utf8("dataFusion")) |
+---------------------------+
| DATAFUSION                |
+---------------------------+
```

**Related functions**:

* [initcap](#initcap)
* [lower](#lower)

### `uuid`[#](#uuid "Link to this heading")

Returns [`UUID v4`](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_%28random%29) string value which is unique per row.

```
uuid()
```

#### Example[#](#id157 "Link to this heading")

```
> select uuid();
+--------------------------------------+
| uuid()                               |
+--------------------------------------+
| 6ec17ef8-1934-41cc-8d59-d0c8f9eea1f0 |
+--------------------------------------+
```

## Binary String Functions[#](#binary-string-functions "Link to this heading")

* [decode](#decode)
* [encode](#encode)

### `decode`[#](#decode "Link to this heading")

Decode binary data from textual representation in string.

```
decode(expression, format)
```

#### Arguments[#](#id158 "Link to this heading")

* **expression**: Expression containing encoded string data
* **format**: Same arguments as [encode](#encode)

**Related functions**:

* [encode](#encode)

### `encode`[#](#encode "Link to this heading")

Encode binary data into a textual representation.

```
encode(expression, format)
```

#### Arguments[#](#id159 "Link to this heading")

* **expression**: Expression containing string or binary data
* **format**: Supported formats are: `base64`, `base64pad`, `hex`

**Related functions**:

* [decode](#decode)

## Regular Expression Functions[#](#regular-expression-functions "Link to this heading")

Apache DataFusion uses a [PCRE-like](https://en.wikibooks.org/wiki/Regular_Expressions/Perl-Compatible_Regular_Expressions)
regular expression [syntax](https://docs.rs/regex/latest/regex/#syntax)
(minus support for several features including look-around and backreferences).
The following regular expression functions are supported:

* [regexp\_count](#regexp-count)
* [regexp\_instr](#regexp-instr)
* [regexp\_like](#regexp-like)
* [regexp\_match](#regexp-match)
* [regexp\_replace](#regexp-replace)

### `regexp_count`[#](#regexp-count "Link to this heading")

Returns the number of matches that a [regular expression](https://docs.rs/regex/latest/regex/#syntax) has in a string.

```
regexp_count(str, regexp[, start, flags])
```

#### Arguments[#](#id160 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **regexp**: Regular expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **start**: - **start**: Optional start position (the first position is 1) to search for the regular expression. Can be a constant, column, or function.
* **flags**: Optional regular expression flags that control the behavior of the regular expression. The following flags are supported:

  * **i**: case-insensitive: letters match both upper and lower case
  * **m**: multi-line mode: ^ and $ match begin/end of line
  * **s**: allow . to match \n
  * **R**: enables CRLF mode: when multi-line mode is enabled, \r\n is used
  * **U**: swap the meaning of x\* and x\*?

#### Example[#](#id161 "Link to this heading")

```
> select regexp_count('abcAbAbc', 'abc', 2, 'i');
+---------------------------------------------------------------+
| regexp_count(Utf8("abcAbAbc"),Utf8("abc"),Int64(2),Utf8("i")) |
+---------------------------------------------------------------+
| 1                                                             |
+---------------------------------------------------------------+
```

### `regexp_instr`[#](#regexp-instr "Link to this heading")

Returns the position in a string where the specified occurrence of a POSIX regular expression is located.

```
regexp_instr(str, regexp[, start[, N[, flags[, subexpr]]]])
```

#### Arguments[#](#id162 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **regexp**: Regular expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **start**: - **start**: Optional start position (the first position is 1) to search for the regular expression. Can be a constant, column, or function. Defaults to 1
* **N**: - **N**: Optional The N-th occurrence of pattern to find. Defaults to 1 (first match). Can be a constant, column, or function.
* **flags**: Optional regular expression flags that control the behavior of the regular expression. The following flags are supported:

  * **i**: case-insensitive: letters match both upper and lower case
  * **m**: multi-line mode: ^ and $ match begin/end of line
  * **s**: allow . to match \n
  * **R**: enables CRLF mode: when multi-line mode is enabled, \r\n is used
  * **U**: swap the meaning of x\* and x\*?
* **subexpr**: Optional Specifies which capture group (subexpression) to return the position for. Defaults to 0, which returns the position of the entire match.

#### Example[#](#id163 "Link to this heading")

```
> SELECT regexp_instr('ABCDEF', 'C(.)(..)');
+---------------------------------------------------------------+
| regexp_instr(Utf8("ABCDEF"),Utf8("C(.)(..)"))                 |
+---------------------------------------------------------------+
| 3                                                             |
+---------------------------------------------------------------+
```

### `regexp_like`[#](#regexp-like "Link to this heading")

Returns true if a [regular expression](https://docs.rs/regex/latest/regex/#syntax) has at least one match in a string, false otherwise.

```
regexp_like(str, regexp[, flags])
```

#### Arguments[#](#id164 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **regexp**: Regular expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **flags**: Optional regular expression flags that control the behavior of the regular expression. The following flags are supported:

  * **i**: case-insensitive: letters match both upper and lower case
  * **m**: multi-line mode: ^ and $ match begin/end of line
  * **s**: allow . to match \n
  * **R**: enables CRLF mode: when multi-line mode is enabled, \r\n is used
  * **U**: swap the meaning of x\* and x\*?

#### Example[#](#id165 "Link to this heading")

```
select regexp_like('Köln', '[a-zA-Z]ö[a-zA-Z]{2}');
+--------------------------------------------------------+
| regexp_like(Utf8("Köln"),Utf8("[a-zA-Z]ö[a-zA-Z]{2}")) |
+--------------------------------------------------------+
| true                                                   |
+--------------------------------------------------------+
SELECT regexp_like('aBc', '(b|d)', 'i');
+--------------------------------------------------+
| regexp_like(Utf8("aBc"),Utf8("(b|d)"),Utf8("i")) |
+--------------------------------------------------+
| true                                             |
+--------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/regexp.rs)

### `regexp_match`[#](#regexp-match "Link to this heading")

Returns the first [regular expression](https://docs.rs/regex/latest/regex/#syntax) matches in a string.

```
regexp_match(str, regexp[, flags])
```

#### Arguments[#](#id166 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **regexp**: Regular expression to match against.
  Can be a constant, column, or function.
* **flags**: Optional regular expression flags that control the behavior of the regular expression. The following flags are supported:

  * **i**: case-insensitive: letters match both upper and lower case
  * **m**: multi-line mode: ^ and $ match begin/end of line
  * **s**: allow . to match \n
  * **R**: enables CRLF mode: when multi-line mode is enabled, \r\n is used
  * **U**: swap the meaning of x\* and x\*?

#### Example[#](#id167 "Link to this heading")

```
            > select regexp_match('Köln', '[a-zA-Z]ö[a-zA-Z]{2}');
            +---------------------------------------------------------+
            | regexp_match(Utf8("Köln"),Utf8("[a-zA-Z]ö[a-zA-Z]{2}")) |
            +---------------------------------------------------------+
            | [Köln]                                                  |
            +---------------------------------------------------------+
            SELECT regexp_match('aBc', '(b|d)', 'i');
            +---------------------------------------------------+
            | regexp_match(Utf8("aBc"),Utf8("(b|d)"),Utf8("i")) |
            +---------------------------------------------------+
            | [B]                                               |
            +---------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/regexp.rs)

### `regexp_replace`[#](#regexp-replace "Link to this heading")

Replaces substrings in a string that match a [regular expression](https://docs.rs/regex/latest/regex/#syntax).

```
regexp_replace(str, regexp, replacement[, flags])
```

#### Arguments[#](#id168 "Link to this heading")

* **str**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **regexp**: Regular expression to match against.
  Can be a constant, column, or function.
* **replacement**: Replacement string expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **flags**: Optional regular expression flags that control the behavior of the regular expression. The following flags are supported:
* **g**: (global) Search globally and don’t return after the first match
* **i**: case-insensitive: letters match both upper and lower case
* **m**: multi-line mode: ^ and $ match begin/end of line
* **s**: allow . to match \n
* **R**: enables CRLF mode: when multi-line mode is enabled, \r\n is used
* **U**: swap the meaning of x\* and x\*?

#### Example[#](#id169 "Link to this heading")

```
> select regexp_replace('foobarbaz', 'b(..)', 'X\\1Y', 'g');
+------------------------------------------------------------------------+
| regexp_replace(Utf8("foobarbaz"),Utf8("b(..)"),Utf8("X\1Y"),Utf8("g")) |
+------------------------------------------------------------------------+
| fooXarYXazY                                                            |
+------------------------------------------------------------------------+
SELECT regexp_replace('aBc', '(b|d)', 'Ab\\1a', 'i');
+-------------------------------------------------------------------+
| regexp_replace(Utf8("aBc"),Utf8("(b|d)"),Utf8("Ab\1a"),Utf8("i")) |
+-------------------------------------------------------------------+
| aAbBac                                                            |
+-------------------------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/regexp.rs)

## Time and Date Functions[#](#time-and-date-functions "Link to this heading")

* [current\_date](#current-date)
* [current\_time](#current-time)
* [current\_timestamp](#current-timestamp)
* [date\_bin](#date-bin)
* [date\_format](#date-format)
* [date\_part](#date-part)
* [date\_trunc](#date-trunc)
* [datepart](#datepart)
* [datetrunc](#datetrunc)
* [from\_unixtime](#from-unixtime)
* [make\_date](#make-date)
* [make\_time](#make-time)
* [now](#now)
* [to\_char](#to-char)
* [to\_date](#to-date)
* [to\_local\_time](#to-local-time)
* [to\_time](#to-time)
* [to\_timestamp](#to-timestamp)
* [to\_timestamp\_micros](#to-timestamp-micros)
* [to\_timestamp\_millis](#to-timestamp-millis)
* [to\_timestamp\_nanos](#to-timestamp-nanos)
* [to\_timestamp\_seconds](#to-timestamp-seconds)
* [to\_unixtime](#to-unixtime)
* [today](#today)

### `current_date`[#](#current-date "Link to this heading")

Returns the current date in the session time zone.

The `current_date()` return value is determined at query time and will return the same date, no matter when in the query plan the function executes.

```
current_date()
    (optional) SET datafusion.execution.time_zone = '+00:00';
    SELECT current_date();
```

#### Example[#](#id170 "Link to this heading")

```
> SELECT current_date();
+----------------+
| current_date() |
+----------------+
| 2024-12-23     |
+----------------+

-- The current date is based on the session time zone (UTC by default)
> SET datafusion.execution.time_zone = 'Asia/Tokyo';
> SELECT current_date();
+----------------+
| current_date() |
+----------------+
| 2024-12-24     |
+----------------+
```

#### Aliases[#](#id171 "Link to this heading")

* today

### `current_time`[#](#current-time "Link to this heading")

Returns the current time in the session time zone.

The `current_time()` return value is determined at query time and will return the same time, no matter when in the query plan the function executes.

The session time zone can be set using the statement ‘SET datafusion.execution.time\_zone = desired time zone’. The time zone can be a value like +00:00, ‘Europe/London’ etc.

```
current_time()
    (optional) SET datafusion.execution.time_zone = '+00:00';
    SELECT current_time();
```

#### Example[#](#id172 "Link to this heading")

```
> SELECT current_time();
+--------------------+
| current_time()     |
+--------------------+
| 06:30:00.123456789 |
+--------------------+

-- The current time is based on the session time zone (UTC by default)
> SET datafusion.execution.time_zone = 'Asia/Tokyo';
> SELECT current_time();
+--------------------+
| current_time()     |
+--------------------+
| 15:30:00.123456789 |
+--------------------+
```

### `current_timestamp`[#](#current-timestamp "Link to this heading")

*Alias of [now](#now).*

### `date_bin`[#](#date-bin "Link to this heading")

Calculates time intervals and returns the start of the interval nearest to the specified timestamp. Use `date_bin` to downsample time series data by grouping rows into time-based “bins” or “windows” and applying an aggregate or selector function to each window.

For example, if you “bin” or “window” data into 15 minute intervals, an input timestamp of `2023-01-01T18:18:18Z` will be updated to the start time of the 15 minute bin it is in: `2023-01-01T18:15:00Z`.

```
date_bin(interval, expression, origin-timestamp)
```

#### Arguments[#](#id173 "Link to this heading")

* **interval**: Bin interval.
* **expression**: Time expression to operate on. Can be a constant, column, or function.
* **origin-timestamp**: Optional. Starting point used to determine bin boundaries. If not specified defaults 1970-01-01T00:00:00Z (the UNIX epoch in UTC). The following intervals are supported:

  * nanoseconds
  * microseconds
  * milliseconds
  * seconds
  * minutes
  * hours
  * days
  * weeks
  * months
  * years
  * century

#### Example[#](#id174 "Link to this heading")

```
-- Bin the timestamp into 1 day intervals
> SELECT date_bin(interval '1 day', time) as bin
FROM VALUES ('2023-01-01T18:18:18Z'), ('2023-01-03T19:00:03Z')  t(time);
+---------------------+
| bin                 |
+---------------------+
| 2023-01-01T00:00:00 |
| 2023-01-03T00:00:00 |
+---------------------+
2 row(s) fetched.

-- Bin the timestamp into 1 day intervals starting at 3AM on  2023-01-01
> SELECT date_bin(interval '1 day', time,  '2023-01-01T03:00:00') as bin
FROM VALUES ('2023-01-01T18:18:18Z'), ('2023-01-03T19:00:03Z')  t(time);
+---------------------+
| bin                 |
+---------------------+
| 2023-01-01T03:00:00 |
| 2023-01-03T03:00:00 |
+---------------------+
2 row(s) fetched.

-- Bin the time into 15 minute intervals starting at 1 min
>  SELECT date_bin(interval '15 minutes', time, TIME '00:01:00') as bin
FROM VALUES (TIME '02:18:18'), (TIME '19:00:03')  t(time);
+----------+
| bin      |
+----------+
| 02:16:00 |
| 18:46:00 |
+----------+
2 row(s) fetched.
```

### `date_format`[#](#date-format "Link to this heading")

*Alias of [to\_char](#to-char).*

### `date_part`[#](#date-part "Link to this heading")

Returns the specified part of the date as an integer.

```
date_part(part, expression)
```

#### Arguments[#](#id175 "Link to this heading")

* **part**: Part of the date to return. The following date parts are supported:

  * year
  * isoyear (ISO 8601 week-numbering year)
  * quarter (emits value in inclusive range [1, 4] based on which quartile of the year the date is in)
  * month
  * week (week of the year)
  * day (day of the month)
  * hour
  * minute
  * second
  * millisecond
  * microsecond
  * nanosecond
  * dow (day of the week where Sunday is 0)
  * doy (day of the year)
  * epoch (seconds since Unix epoch for timestamps/dates, total seconds for intervals)
  * isodow (day of the week where Monday is 0)
* **expression**: Time expression to operate on. Can be a constant, column, or function.

#### Example[#](#id176 "Link to this heading")

```
> SELECT date_part('year', '2024-05-01T00:00:00');
+-----------------------------------------------------+
| date_part(Utf8("year"),Utf8("2024-05-01T00:00:00")) |
+-----------------------------------------------------+
| 2024                                                |
+-----------------------------------------------------+
> SELECT extract(day FROM timestamp '2024-05-01T00:00:00');
+----------------------------------------------------+
| date_part(Utf8("DAY"),Utf8("2024-05-01T00:00:00")) |
+----------------------------------------------------+
| 1                                                  |
+----------------------------------------------------+
```

#### Alternative Syntax[#](#id177 "Link to this heading")

```
extract(field FROM source)
```

#### Aliases[#](#id178 "Link to this heading")

* datepart

### `date_trunc`[#](#date-trunc "Link to this heading")

Truncates a timestamp or time value to a specified precision.

```
date_trunc(precision, expression)
```

#### Arguments[#](#id179 "Link to this heading")

* **precision**: Time precision to truncate to. The following precisions are supported:

  For Timestamp types:

  * year / YEAR
  * quarter / QUARTER
  * month / MONTH
  * week / WEEK
  * day / DAY
  * hour / HOUR
  * minute / MINUTE
  * second / SECOND
  * millisecond / MILLISECOND
  * microsecond / MICROSECOND

  For Time types (hour, minute, second, millisecond, microsecond only):

  * hour / HOUR
  * minute / MINUTE
  * second / SECOND
  * millisecond / MILLISECOND
  * microsecond / MICROSECOND
* **expression**: Timestamp or time expression to operate on. Can be a constant, column, or function.

#### Example[#](#id180 "Link to this heading")

```
> SELECT date_trunc('month', '2024-05-15T10:30:00');
+-----------------------------------------------+
| date_trunc(Utf8("month"),Utf8("2024-05-15T10:30:00")) |
+-----------------------------------------------+
| 2024-05-01T00:00:00                           |
+-----------------------------------------------+
> SELECT date_trunc('hour', '2024-05-15T10:30:00');
+----------------------------------------------+
| date_trunc(Utf8("hour"),Utf8("2024-05-15T10:30:00")) |
+----------------------------------------------+
| 2024-05-15T10:00:00                          |
+----------------------------------------------+
```

#### Aliases[#](#id181 "Link to this heading")

* datetrunc

### `datepart`[#](#datepart "Link to this heading")

*Alias of [date\_part](#date-part).*

### `datetrunc`[#](#datetrunc "Link to this heading")

*Alias of [date\_trunc](#date-trunc).*

### `from_unixtime`[#](#from-unixtime "Link to this heading")

Converts an integer to RFC3339 timestamp format (`YYYY-MM-DDT00:00:00.000000000Z`). Integers and unsigned integers are interpreted as seconds since the unix epoch (`1970-01-01T00:00:00Z`) return the corresponding timestamp.

```
from_unixtime(expression[, timezone])
```

#### Arguments[#](#id182 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **timezone**: Optional timezone to use when converting the integer to a timestamp. If not provided, the default timezone is UTC.

#### Example[#](#id183 "Link to this heading")

```
> select from_unixtime(1599572549, 'America/New_York');
+-----------------------------------------------------------+
| from_unixtime(Int64(1599572549),Utf8("America/New_York")) |
+-----------------------------------------------------------+
| 2020-09-08T09:42:29-04:00                                 |
+-----------------------------------------------------------+
```

### `make_date`[#](#make-date "Link to this heading")

Make a date from year/month/day component parts.

```
make_date(year, month, day)
```

#### Arguments[#](#id184 "Link to this heading")

* **year**: Year to use when making the date. Can be a constant, column or function, and any combination of arithmetic operators.
* **month**: Month to use when making the date. Can be a constant, column or function, and any combination of arithmetic operators.
* **day**: Day to use when making the date. Can be a constant, column or function, and any combination of arithmetic operators.

#### Example[#](#id185 "Link to this heading")

```
> select make_date(2023, 1, 31);
+-------------------------------------------+
| make_date(Int64(2023),Int64(1),Int64(31)) |
+-------------------------------------------+
| 2023-01-31                                |
+-------------------------------------------+
> select make_date('2023', '01', '31');
+-----------------------------------------------+
| make_date(Utf8("2023"),Utf8("01"),Utf8("31")) |
+-----------------------------------------------+
| 2023-01-31                                    |
+-----------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `make_time`[#](#make-time "Link to this heading")

Make a time from hour/minute/second component parts.

```
make_time(hour, minute, second)
```

#### Arguments[#](#id186 "Link to this heading")

* **hour**: Hour to use when making the time. Can be a constant, column or function, and any combination of arithmetic operators.
* **minute**: Minute to use when making the time. Can be a constant, column or function, and any combination of arithmetic operators.
* **second**: Second to use when making the time. Can be a constant, column or function, and any combination of arithmetic operators.

#### Example[#](#id187 "Link to this heading")

```
> select make_time(13, 23, 1);
+-------------------------------------------+
| make_time(Int64(13),Int64(23),Int64(1))   |
+-------------------------------------------+
| 13:23:01                                  |
+-------------------------------------------+
> select make_time('23', '01', '31');
+-----------------------------------------------+
| make_time(Utf8("23"),Utf8("01"),Utf8("31"))   |
+-----------------------------------------------+
| 23:01:31                                      |
+-----------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `now`[#](#now "Link to this heading")

Returns the current timestamp in the system configured timezone (None by default).

The `now()` return value is determined at query time and will return the same timestamp, no matter when in the query plan the function executes.

```
now()
```

#### Example[#](#id188 "Link to this heading")

```
> SELECT now();
+----------------------------------+
| now()                            |
+----------------------------------+
| 2024-12-23T06:30:00.123456789    |
+----------------------------------+

-- The timezone of the returned timestamp depends on the session time zone
> SET datafusion.execution.time_zone = 'America/New_York';
> SELECT now();
+--------------------------------------+
| now()                                |
+--------------------------------------+
| 2024-12-23T01:30:00.123456789-05:00  |
+--------------------------------------+
```

#### Aliases[#](#id189 "Link to this heading")

* current\_timestamp

### `to_char`[#](#to-char "Link to this heading")

Returns a string representation of a date, time, timestamp or duration based on a [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html). Unlike the PostgreSQL equivalent of this function numerical formatting is not supported.

```
to_char(expression, format)
```

#### Arguments[#](#id190 "Link to this heading")

* **expression**: Expression to operate on. Can be a constant, column, or function that results in a date, time, timestamp or duration.
* **format**: A [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) string to use to convert the expression.
* **day**: Day to use when making the date. Can be a constant, column or function, and any combination of arithmetic operators.

#### Example[#](#id191 "Link to this heading")

```
> select to_char('2023-03-01'::date, '%d-%m-%Y');
+----------------------------------------------+
| to_char(Utf8("2023-03-01"),Utf8("%d-%m-%Y")) |
+----------------------------------------------+
| 01-03-2023                                   |
+----------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

#### Aliases[#](#id192 "Link to this heading")

* date\_format

### `to_date`[#](#to-date "Link to this heading")

Converts a value to a date (`YYYY-MM-DD`).
Supports strings, numeric and timestamp types as input.
Strings are parsed as YYYY-MM-DD (e.g. ‘2023-07-20’) if no [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html)s are provided.
Integers and doubles are interpreted as days since the unix epoch (`1970-01-01T00:00:00Z`).
Returns the corresponding date.

Note: `to_date` returns Date32, which represents its values as the number of days since unix epoch(`1970-01-01`) stored as signed 32 bit value. The largest supported date value is `9999-12-31`.

```
to_date('2017-05-31', '%Y-%m-%d')
```

#### Arguments[#](#id193 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **format\_n**: Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression. Formats will be tried in the order
  they appear with the first successful one being returned. If none of the formats successfully parse the expression
  an error will be returned.

#### Example[#](#id194 "Link to this heading")

```
> select to_date('2023-01-31');
+-------------------------------+
| to_date(Utf8("2023-01-31")) |
+-------------------------------+
| 2023-01-31                    |
+-------------------------------+
> select to_date('2023/01/31', '%Y-%m-%d', '%Y/%m/%d');
+---------------------------------------------------------------------+
| to_date(Utf8("2023/01/31"),Utf8("%Y-%m-%d"),Utf8("%Y/%m/%d")) |
+---------------------------------------------------------------------+
| 2023-01-31                                                          |
+---------------------------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `to_local_time`[#](#to-local-time "Link to this heading")

Converts a timestamp with a timezone to a timestamp without a timezone (with no offset or timezone information). This function handles daylight saving time changes.

```
to_local_time(expression)
```

#### Arguments[#](#id195 "Link to this heading")

* **expression**: Time expression to operate on. Can be a constant, column, or function.

#### Example[#](#id196 "Link to this heading")

```
> SELECT to_local_time('2024-04-01T00:00:20Z'::timestamp);
+---------------------------------------------+
| to_local_time(Utf8("2024-04-01T00:00:20Z")) |
+---------------------------------------------+
| 2024-04-01T00:00:20                         |
+---------------------------------------------+

> SELECT to_local_time('2024-04-01T00:00:20Z'::timestamp AT TIME ZONE 'Europe/Brussels');
+---------------------------------------------+
| to_local_time(Utf8("2024-04-01T00:00:20Z")) |
+---------------------------------------------+
| 2024-04-01T00:00:20                         |
+---------------------------------------------+

> SELECT
  time,
  arrow_typeof(time) as type,
  to_local_time(time) as to_local_time,
  arrow_typeof(to_local_time(time)) as to_local_time_type
FROM (
  SELECT '2024-04-01T00:00:20Z'::timestamp AT TIME ZONE 'Europe/Brussels' AS time
);
+---------------------------+----------------------------------+---------------------+--------------------+
| time                      | type                             | to_local_time       | to_local_time_type |
+---------------------------+----------------------------------+---------------------+--------------------+
| 2024-04-01T00:00:20+02:00 | Timestamp(ns, "Europe/Brussels") | 2024-04-01T00:00:20 | Timestamp(ns)      |
+---------------------------+----------------------------------+---------------------+--------------------+

# combine `to_local_time()` with `date_bin()` to bin on boundaries in the timezone rather
# than UTC boundaries

> SELECT date_bin(interval '1 day', to_local_time('2024-04-01T00:00:20Z'::timestamp AT TIME ZONE 'Europe/Brussels')) AS date_bin;
+---------------------+
| date_bin            |
+---------------------+
| 2024-04-01T00:00:00 |
+---------------------+

> SELECT date_bin(interval '1 day', to_local_time('2024-04-01T00:00:20Z'::timestamp AT TIME ZONE 'Europe/Brussels')) AT TIME ZONE 'Europe/Brussels' AS date_bin_with_timezone;
+---------------------------+
| date_bin_with_timezone    |
+---------------------------+
| 2024-04-01T00:00:00+02:00 |
+---------------------------+
```

### `to_time`[#](#to-time "Link to this heading")

Converts a value to a time (`HH:MM:SS.nnnnnnnnn`).
Supports strings and timestamps as input.
Strings are parsed as `HH:MM:SS`, `HH:MM:SS.nnnnnnnnn`, or `HH:MM` if no [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html)s are provided.
Timestamps will have the time portion extracted.
Returns the corresponding time.

Note: `to_time` returns Time64(Nanosecond), which represents the time of day in nanoseconds since midnight.

```
to_time('12:30:45', '%H:%M:%S')
```

#### Arguments[#](#id197 "Link to this heading")

* **expression**: String or Timestamp expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **format\_n**: Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression. Formats will be tried in the order
  they appear with the first successful one being returned. If none of the formats successfully parse the expression
  an error will be returned.

#### Example[#](#id198 "Link to this heading")

```
> select to_time('12:30:45');
+---------------------------+
| to_time(Utf8("12:30:45")) |
+---------------------------+
| 12:30:45                  |
+---------------------------+
> select to_time('12-30-45', '%H-%M-%S');
+--------------------------------------------+
| to_time(Utf8("12-30-45"),Utf8("%H-%M-%S")) |
+--------------------------------------------+
| 12:30:45                                   |
+--------------------------------------------+
> select to_time('2024-01-15 14:30:45'::timestamp);
+--------------------------------------------------+
| to_time(Utf8("2024-01-15 14:30:45"))             |
+--------------------------------------------------+
| 14:30:45                                         |
+--------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `to_timestamp`[#](#to-timestamp "Link to this heading")

Converts a value to a timestamp (`YYYY-MM-DDT00:00:00.000000<TZ>`) in the session time zone. Supports strings,
integer, unsigned integer, and double types as input. Strings are parsed as RFC3339 (e.g. ‘2023-07-20T05:44:00’)
if no [Chrono formats](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) are provided.
Strings that parse without a time zone are treated as if they are in the
session time zone, or UTC if no session time zone is set.
Integers, unsigned integers, and doubles are interpreted as seconds since the unix epoch (`1970-01-01T00:00:00Z`).

Note: `to_timestamp` returns `Timestamp(ns, TimeZone)` where the time zone is the session time zone. The supported range
for integer input is between`-9223372037` and `9223372036`. Supported range for string input is between
`1677-09-21T00:12:44.0` and `2262-04-11T23:47:16.0`. Please use `to_timestamp_seconds`
for the input outside of supported bounds.

The session time zone can be set using the statement `SET TIMEZONE = 'desired time zone'`.
The time zone can be a value like +00:00, ‘Europe/London’ etc.

```
to_timestamp(expression[, ..., format_n])
```

#### Arguments[#](#id199 "Link to this heading")

* **expression**: Expression to operate on. Can be a constant, column, or function, and any combination of arithmetic operators.
* **format\_n**:
  Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression.
  Formats will be tried in the order they appear with the first successful one being returned. If none of the formats successfully
  parse the expression an error will be returned. Note: parsing of named timezones (e.g. ‘America/New\_York’) using %Z is
  only supported at the end of the string preceded by a space.

#### Example[#](#id200 "Link to this heading")

```
> select to_timestamp('2023-01-31T09:26:56.123456789-05:00');
+-----------------------------------------------------------+
| to_timestamp(Utf8("2023-01-31T09:26:56.123456789-05:00")) |
+-----------------------------------------------------------+
| 2023-01-31T14:26:56.123456789                             |
+-----------------------------------------------------------+
> select to_timestamp('03:59:00.123456789 05-17-2023', '%c', '%+', '%H:%M:%S%.f %m-%d-%Y');
+--------------------------------------------------------------------------------------------------------+
| to_timestamp(Utf8("03:59:00.123456789 05-17-2023"),Utf8("%c"),Utf8("%+"),Utf8("%H:%M:%S%.f %m-%d-%Y")) |
+--------------------------------------------------------------------------------------------------------+
| 2023-05-17T03:59:00.123456789                                                                          |
+--------------------------------------------------------------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `to_timestamp_micros`[#](#to-timestamp-micros "Link to this heading")

Converts a value to a timestamp (`YYYY-MM-DDT00:00:00.000000<TZ>`) in the session time zone. Supports strings,
integer, unsigned integer, and double types as input. Strings are parsed as RFC3339 (e.g. ‘2023-07-20T05:44:00’)
if no [Chrono formats](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) are provided.
Strings that parse without a time zone are treated as if they are in the
session time zone, or UTC if no session time zone is set.
Integers, unsigned integers, and doubles are interpreted as microseconds since the unix epoch (`1970-01-01T00:00:00Z`).

The session time zone can be set using the statement `SET TIMEZONE = 'desired time zone'`.
The time zone can be a value like +00:00, ‘Europe/London’ etc.

```
to_timestamp_micros(expression[, ..., format_n])
```

#### Arguments[#](#id201 "Link to this heading")

* **expression**: Expression to operate on. Can be a constant, column, or function, and any combination of arithmetic operators.
* **format\_n**:
  Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression.
  Formats will be tried in the order they appear with the first successful one being returned. If none of the formats successfully
  parse the expression an error will be returned. Note: parsing of named timezones (e.g. ‘America/New\_York’) using %Z is
  only supported at the end of the string preceded by a space.

#### Example[#](#id202 "Link to this heading")

```
> select to_timestamp_micros('2023-01-31T09:26:56.123456789-05:00');
+------------------------------------------------------------------+
| to_timestamp_micros(Utf8("2023-01-31T09:26:56.123456789-05:00")) |
+------------------------------------------------------------------+
| 2023-01-31T14:26:56.123456                                       |
+------------------------------------------------------------------+
> select to_timestamp_micros('03:59:00.123456789 05-17-2023', '%c', '%+', '%H:%M:%S%.f %m-%d-%Y');
+---------------------------------------------------------------------------------------------------------------+
| to_timestamp_micros(Utf8("03:59:00.123456789 05-17-2023"),Utf8("%c"),Utf8("%+"),Utf8("%H:%M:%S%.f %m-%d-%Y")) |
+---------------------------------------------------------------------------------------------------------------+
| 2023-05-17T03:59:00.123456                                                                                    |
+---------------------------------------------------------------------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `to_timestamp_millis`[#](#to-timestamp-millis "Link to this heading")

Converts a value to a timestamp (`YYYY-MM-DDT00:00:00.000<TZ>`) in the session time zone. Supports strings,
integer, unsigned integer, and double types as input. Strings are parsed as RFC3339 (e.g. ‘2023-07-20T05:44:00’)
if no [Chrono formats](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) are provided.
Strings that parse without a time zone are treated as if they are in the
session time zone, or UTC if no session time zone is set.
Integers, unsigned integers, and doubles are interpreted as milliseconds since the unix epoch (`1970-01-01T00:00:00Z`).

The session time zone can be set using the statement `SET TIMEZONE = 'desired time zone'`.
The time zone can be a value like +00:00, ‘Europe/London’ etc.

```
to_timestamp_millis(expression[, ..., format_n])
```

#### Arguments[#](#id203 "Link to this heading")

* **expression**: Expression to operate on. Can be a constant, column, or function, and any combination of arithmetic operators.
* **format\_n**:
  Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression.
  Formats will be tried in the order they appear with the first successful one being returned. If none of the formats successfully
  parse the expression an error will be returned. Note: parsing of named timezones (e.g. ‘America/New\_York’) using %Z is
  only supported at the end of the string preceded by a space.

#### Example[#](#id204 "Link to this heading")

```
> select to_timestamp_millis('2023-01-31T09:26:56.123456789-05:00');
+------------------------------------------------------------------+
| to_timestamp_millis(Utf8("2023-01-31T09:26:56.123456789-05:00")) |
+------------------------------------------------------------------+
| 2023-01-31T14:26:56.123                                          |
+------------------------------------------------------------------+
> select to_timestamp_millis('03:59:00.123456789 05-17-2023', '%c', '%+', '%H:%M:%S%.f %m-%d-%Y');
+---------------------------------------------------------------------------------------------------------------+
| to_timestamp_millis(Utf8("03:59:00.123456789 05-17-2023"),Utf8("%c"),Utf8("%+"),Utf8("%H:%M:%S%.f %m-%d-%Y")) |
+---------------------------------------------------------------------------------------------------------------+
| 2023-05-17T03:59:00.123                                                                                       |
+---------------------------------------------------------------------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `to_timestamp_nanos`[#](#to-timestamp-nanos "Link to this heading")

Converts a value to a timestamp (`YYYY-MM-DDT00:00:00.000000000<TZ>`) in the session time zone. Supports strings,
integer, unsigned integer, and double types as input. Strings are parsed as RFC3339 (e.g. ‘2023-07-20T05:44:00’)
if no [Chrono formats](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) are provided.
Strings that parse without a time zone are treated as if they are in the
session time zone. Integers, unsigned integers, and doubles are interpreted as nanoseconds since the unix epoch (`1970-01-01T00:00:00Z`).

The session time zone can be set using the statement `SET TIMEZONE = 'desired time zone'`.
The time zone can be a value like +00:00, ‘Europe/London’ etc.

```
to_timestamp_nanos(expression[, ..., format_n])
```

#### Arguments[#](#id205 "Link to this heading")

* **expression**: Expression to operate on. Can be a constant, column, or function, and any combination of arithmetic operators.
* **format\_n**:
  Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression.
  Formats will be tried in the order they appear with the first successful one being returned. If none of the formats successfully
  parse the expression an error will be returned. Note: parsing of named timezones (e.g. ‘America/New\_York’) using %Z is
  only supported at the end of the string preceded by a space.

#### Example[#](#id206 "Link to this heading")

```
> select to_timestamp_nanos('2023-01-31T09:26:56.123456789-05:00');
+-----------------------------------------------------------------+
| to_timestamp_nanos(Utf8("2023-01-31T09:26:56.123456789-05:00")) |
+-----------------------------------------------------------------+
| 2023-01-31T14:26:56.123456789                                   |
+-----------------------------------------------------------------+
> select to_timestamp_nanos('03:59:00.123456789 05-17-2023', '%c', '%+', '%H:%M:%S%.f %m-%d-%Y');
+--------------------------------------------------------------------------------------------------------------+
| to_timestamp_nanos(Utf8("03:59:00.123456789 05-17-2023"),Utf8("%c"),Utf8("%+"),Utf8("%H:%M:%S%.f %m-%d-%Y")) |
+--------------------------------------------------------------------------------------------------------------+
| 2023-05-17T03:59:00.123456789                                                                                |
+---------------------------------------------------------------------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `to_timestamp_seconds`[#](#to-timestamp-seconds "Link to this heading")

Converts a value to a timestamp (`YYYY-MM-DDT00:00:00<TZ>`) in the session time zone. Supports strings,
integer, unsigned integer, and double types as input. Strings are parsed as RFC3339 (e.g. ‘2023-07-20T05:44:00’)
if no [Chrono formats](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) are provided.
Strings that parse without a time zone are treated as if they are in the
session time zone, or UTC if no session time zone is set.
Integers, unsigned integers, and doubles are interpreted as seconds since the unix epoch (`1970-01-01T00:00:00Z`).

The session time zone can be set using the statement `SET TIMEZONE = 'desired time zone'`.
The time zone can be a value like +00:00, ‘Europe/London’ etc.

```
to_timestamp_seconds(expression[, ..., format_n])
```

#### Arguments[#](#id207 "Link to this heading")

* **expression**: Expression to operate on. Can be a constant, column, or function, and any combination of arithmetic operators.
* **format\_n**:
  Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression.
  Formats will be tried in the order they appear with the first successful one being returned. If none of the formats successfully
  parse the expression an error will be returned. Note: parsing of named timezones (e.g. ‘America/New\_York’) using %Z is
  only supported at the end of the string preceded by a space.

#### Example[#](#id208 "Link to this heading")

```
> select to_timestamp_seconds('2023-01-31T09:26:56.123456789-05:00');
+-------------------------------------------------------------------+
| to_timestamp_seconds(Utf8("2023-01-31T09:26:56.123456789-05:00")) |
+-------------------------------------------------------------------+
| 2023-01-31T14:26:56                                               |
+-------------------------------------------------------------------+
> select to_timestamp_seconds('03:59:00.123456789 05-17-2023', '%c', '%+', '%H:%M:%S%.f %m-%d-%Y');
+----------------------------------------------------------------------------------------------------------------+
| to_timestamp_seconds(Utf8("03:59:00.123456789 05-17-2023"),Utf8("%c"),Utf8("%+"),Utf8("%H:%M:%S%.f %m-%d-%Y")) |
+----------------------------------------------------------------------------------------------------------------+
| 2023-05-17T03:59:00                                                                                            |
+----------------------------------------------------------------------------------------------------------------+
```

Additional examples can be found [here](https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/builtin_functions/date_time.rs)

### `to_unixtime`[#](#to-unixtime "Link to this heading")

Converts a value to seconds since the unix epoch (`1970-01-01T00:00:00`).
Supports strings, dates, timestamps, integer, unsigned integer, and float types as input.
Strings are parsed as RFC3339 (e.g. ‘2023-07-20T05:44:00’)
if no [Chrono formats](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) are provided.
Integers, unsigned integers, and floats are interpreted as seconds since the unix epoch (`1970-01-01T00:00:00`).

```
to_unixtime(expression[, ..., format_n])
```

#### Arguments[#](#id209 "Link to this heading")

* **expression**: Expression to operate on. Can be a constant, column, or function, and any combination of arithmetic operators.
* **format\_n**: Optional [Chrono format](https://docs.rs/chrono/latest/chrono/format/strftime/index.html) strings to use to parse the expression. Formats will be tried in the order they appear with the first successful one being returned. If none of the formats successfully parse the expression an error will be returned.

#### Example[#](#id210 "Link to this heading")

```
> select to_unixtime('2020-09-08T12:00:00+00:00');
+------------------------------------------------+
| to_unixtime(Utf8("2020-09-08T12:00:00+00:00")) |
+------------------------------------------------+
| 1599566400                                     |
+------------------------------------------------+
> select to_unixtime('01-14-2023 01:01:30+05:30', '%q', '%d-%m-%Y %H/%M/%S', '%+', '%m-%d-%Y %H:%M:%S%#z');
+-----------------------------------------------------------------------------------------------------------------------------+
| to_unixtime(Utf8("01-14-2023 01:01:30+05:30"),Utf8("%q"),Utf8("%d-%m-%Y %H/%M/%S"),Utf8("%+"),Utf8("%m-%d-%Y %H:%M:%S%#z")) |
+-----------------------------------------------------------------------------------------------------------------------------+
| 1673638290                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------+
```

### `today`[#](#today "Link to this heading")

*Alias of [current\_date](#current-date).*

## Array Functions[#](#array-functions "Link to this heading")

* [array\_any\_value](#array-any-value)
* [array\_append](#array-append)
* [array\_cat](#array-cat)
* [array\_compact](#array-compact)
* [array\_concat](#array-concat)
* [array\_contains](#array-contains)
* [array\_dims](#array-dims)
* [array\_distance](#array-distance)
* [array\_distinct](#array-distinct)
* [array\_element](#array-element)
* [array\_empty](#array-empty)
* [array\_except](#array-except)
* [array\_extract](#array-extract)
* [array\_has](#array-has)
* [array\_has\_all](#array-has-all)
* [array\_has\_any](#array-has-any)
* [array\_indexof](#array-indexof)
* [array\_intersect](#array-intersect)
* [array\_join](#array-join)
* [array\_length](#array-length)
* [array\_max](#array-max)
* [array\_min](#array-min)
* [array\_ndims](#array-ndims)
* [array\_pop\_back](#array-pop-back)
* [array\_pop\_front](#array-pop-front)
* [array\_position](#array-position)
* [array\_positions](#array-positions)
* [array\_prepend](#array-prepend)
* [array\_push\_back](#array-push-back)
* [array\_push\_front](#array-push-front)
* [array\_remove](#array-remove)
* [array\_remove\_all](#array-remove-all)
* [array\_remove\_n](#array-remove-n)
* [array\_repeat](#array-repeat)
* [array\_replace](#array-replace)
* [array\_replace\_all](#array-replace-all)
* [array\_replace\_n](#array-replace-n)
* [array\_resize](#array-resize)
* [array\_reverse](#array-reverse)
* [array\_slice](#array-slice)
* [array\_sort](#array-sort)
* [array\_to\_string](#array-to-string)
* [array\_union](#array-union)
* [arrays\_overlap](#arrays-overlap)
* [arrays\_zip](#arrays-zip)
* [cardinality](#cardinality)
* [empty](#empty)
* [flatten](#flatten)
* [generate\_series](#generate-series)
* [list\_any\_value](#list-any-value)
* [list\_append](#list-append)
* [list\_cat](#list-cat)
* [list\_compact](#list-compact)
* [list\_concat](#list-concat)
* [list\_contains](#list-contains)
* [list\_dims](#list-dims)
* [list\_distance](#list-distance)
* [list\_distinct](#list-distinct)
* [list\_element](#list-element)
* [list\_empty](#list-empty)
* [list\_except](#list-except)
* [list\_extract](#list-extract)
* [list\_has](#list-has)
* [list\_has\_all](#list-has-all)
* [list\_has\_any](#list-has-any)
* [list\_indexof](#list-indexof)
* [list\_intersect](#list-intersect)
* [list\_join](#list-join)
* [list\_length](#list-length)
* [list\_max](#list-max)
* [list\_ndims](#list-ndims)
* [list\_pop\_back](#list-pop-back)
* [list\_pop\_front](#list-pop-front)
* [list\_position](#list-position)
* [list\_positions](#list-positions)
* [list\_prepend](#list-prepend)
* [list\_push\_back](#list-push-back)
* [list\_push\_front](#list-push-front)
* [list\_remove](#list-remove)
* [list\_remove\_all](#list-remove-all)
* [list\_remove\_n](#list-remove-n)
* [list\_repeat](#list-repeat)
* [list\_replace](#list-replace)
* [list\_replace\_all](#list-replace-all)
* [list\_replace\_n](#list-replace-n)
* [list\_resize](#list-resize)
* [list\_reverse](#list-reverse)
* [list\_slice](#list-slice)
* [list\_sort](#list-sort)
* [list\_to\_string](#list-to-string)
* [list\_union](#list-union)
* [list\_zip](#list-zip)
* [make\_array](#make-array)
* [make\_list](#make-list)
* [range](#range)
* [string\_to\_array](#string-to-array)
* [string\_to\_list](#string-to-list)

### `array_any_value`[#](#array-any-value "Link to this heading")

Returns the first non-null element in the array.

```
array_any_value(array)
```

#### Arguments[#](#id211 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id212 "Link to this heading")

```
> select array_any_value([NULL, 1, 2, 3]);
+-------------------------------+
| array_any_value(List([NULL,1,2,3])) |
+-------------------------------------+
| 1                                   |
+-------------------------------------+
```

#### Aliases[#](#id213 "Link to this heading")

* list\_any\_value

### `array_append`[#](#array-append "Link to this heading")

Appends an element to the end of an array.

```
array_append(array, element)
```

#### Arguments[#](#id214 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Element to append to the array.

#### Example[#](#id215 "Link to this heading")

```
> select array_append([1, 2, 3], 4);
+--------------------------------------+
| array_append(List([1,2,3]),Int64(4)) |
+--------------------------------------+
| [1, 2, 3, 4]                         |
+--------------------------------------+
```

#### Aliases[#](#id216 "Link to this heading")

* list\_append
* array\_push\_back
* list\_push\_back

### `array_cat`[#](#array-cat "Link to this heading")

*Alias of [array\_concat](#array-concat).*

### `array_compact`[#](#array-compact "Link to this heading")

Removes null values from the array.

```
array_compact(array)
```

#### Arguments[#](#id217 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id218 "Link to this heading")

```
> select array_compact([1, NULL, 2, NULL, 3]) arr;
+-----------+
| arr       |
+-----------+
| [1, 2, 3] |
+-----------+
```

#### Aliases[#](#id219 "Link to this heading")

* list\_compact

### `array_concat`[#](#array-concat "Link to this heading")

Concatenates arrays.

```
array_concat(array[, ..., array_n])
```

#### Arguments[#](#id220 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **array\_n**: Subsequent array column or literal array to concatenate.

#### Example[#](#id221 "Link to this heading")

```
> select array_concat([1, 2], [3, 4], [5, 6]);
+---------------------------------------------------+
| array_concat(List([1,2]),List([3,4]),List([5,6])) |
+---------------------------------------------------+
| [1, 2, 3, 4, 5, 6]                                |
+---------------------------------------------------+
```

#### Aliases[#](#id222 "Link to this heading")

* array\_cat
* list\_concat
* list\_cat

### `array_contains`[#](#array-contains "Link to this heading")

*Alias of [array\_has](#array-has).*

### `array_dims`[#](#array-dims "Link to this heading")

Returns an array of the array’s dimensions.

```
array_dims(array)
```

#### Arguments[#](#id223 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id224 "Link to this heading")

```
> select array_dims([[1, 2, 3], [4, 5, 6]]);
+---------------------------------+
| array_dims(List([1,2,3,4,5,6])) |
+---------------------------------+
| [2, 3]                          |
+---------------------------------+
```

#### Aliases[#](#id225 "Link to this heading")

* list\_dims

### `array_distance`[#](#array-distance "Link to this heading")

Returns the Euclidean distance between two input arrays of equal length.

```
array_distance(array1, array2)
```

#### Arguments[#](#id226 "Link to this heading")

* **array1**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **array2**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id227 "Link to this heading")

```
> select array_distance([1, 2], [1, 4]);
+------------------------------------+
| array_distance(List([1,2], [1,4])) |
+------------------------------------+
| 2.0                                |
+------------------------------------+
```

#### Aliases[#](#id228 "Link to this heading")

* list\_distance

### `array_distinct`[#](#array-distinct "Link to this heading")

Returns distinct values from the array after removing duplicates.

```
array_distinct(array)
```

#### Arguments[#](#id229 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id230 "Link to this heading")

```
> select array_distinct([1, 3, 2, 3, 1, 2, 4]);
+---------------------------------+
| array_distinct(List([1,2,3,4])) |
+---------------------------------+
| [1, 2, 3, 4]                    |
+---------------------------------+
```

#### Aliases[#](#id231 "Link to this heading")

* list\_distinct

### `array_element`[#](#array-element "Link to this heading")

Extracts the element with the index n from the array.

```
array_element(array, index)
```

#### Arguments[#](#id232 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **index**: Index to extract the element from the array.

#### Example[#](#id233 "Link to this heading")

```
> select array_element([1, 2, 3, 4], 3);
+-----------------------------------------+
| array_element(List([1,2,3,4]),Int64(3)) |
+-----------------------------------------+
| 3                                       |
+-----------------------------------------+
```

#### Aliases[#](#id234 "Link to this heading")

* array\_extract
* list\_element
* list\_extract

### `array_empty`[#](#array-empty "Link to this heading")

*Alias of [empty](#empty).*

### `array_except`[#](#array-except "Link to this heading")

Returns an array of the elements that appear in the first array but not in the second.

```
array_except(array1, array2)
```

#### Arguments[#](#id235 "Link to this heading")

* **array1**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **array2**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id236 "Link to this heading")

```
> select array_except([1, 2, 3, 4], [5, 6, 3, 4]);
+----------------------------------------------------+
| array_except([1, 2, 3, 4], [5, 6, 3, 4]);           |
+----------------------------------------------------+
| [1, 2]                                              |
+----------------------------------------------------+
> select array_except([1, 2, 3, 4], [3, 4, 5, 6]);
+----------------------------------------------------+
| array_except([1, 2, 3, 4], [3, 4, 5, 6]);           |
+----------------------------------------------------+
| [1, 2]                                              |
+----------------------------------------------------+
```

#### Aliases[#](#id237 "Link to this heading")

* list\_except

### `array_extract`[#](#array-extract "Link to this heading")

*Alias of [array\_element](#array-element).*

### `array_has`[#](#array-has "Link to this heading")

Returns true if the array contains the element.

```
array_has(array, element)
```

#### Arguments[#](#id238 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Scalar or Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id239 "Link to this heading")

```
> select array_has([1, 2, 3], 2);
+-----------------------------+
| array_has(List([1,2,3]), 2) |
+-----------------------------+
| true                        |
+-----------------------------+
```

#### Aliases[#](#id240 "Link to this heading")

* list\_has
* array\_contains
* list\_contains

### `array_has_all`[#](#array-has-all "Link to this heading")

Returns true if all elements of sub-array exist in array.

```
array_has_all(array, sub-array)
```

#### Arguments[#](#id241 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **sub-array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id242 "Link to this heading")

```
> select array_has_all([1, 2, 3, 4], [2, 3]);
+--------------------------------------------+
| array_has_all(List([1,2,3,4]), List([2,3])) |
+--------------------------------------------+
| true                                       |
+--------------------------------------------+
```

#### Aliases[#](#id243 "Link to this heading")

* list\_has\_all

### `array_has_any`[#](#array-has-any "Link to this heading")

Returns true if the arrays have any elements in common.

```
array_has_any(array1, array2)
```

#### Arguments[#](#id244 "Link to this heading")

* **array1**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **array2**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id245 "Link to this heading")

```
> select array_has_any([1, 2, 3], [3, 4]);
+------------------------------------------+
| array_has_any(List([1,2,3]), List([3,4])) |
+------------------------------------------+
| true                                     |
+------------------------------------------+
```

#### Aliases[#](#id246 "Link to this heading")

* list\_has\_any
* arrays\_overlap

### `array_indexof`[#](#array-indexof "Link to this heading")

*Alias of [array\_position](#array-position).*

### `array_intersect`[#](#array-intersect "Link to this heading")

Returns an array of elements in the intersection of array1 and array2.

```
array_intersect(array1, array2)
```

#### Arguments[#](#id247 "Link to this heading")

* **array1**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **array2**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id248 "Link to this heading")

```
> select array_intersect([1, 2, 3, 4], [5, 6, 3, 4]);
+----------------------------------------------------+
| array_intersect([1, 2, 3, 4], [5, 6, 3, 4]);       |
+----------------------------------------------------+
| [3, 4]                                             |
+----------------------------------------------------+
> select array_intersect([1, 2, 3, 4], [5, 6, 7, 8]);
+----------------------------------------------------+
| array_intersect([1, 2, 3, 4], [5, 6, 7, 8]);       |
+----------------------------------------------------+
| []                                                 |
+----------------------------------------------------+
```

#### Aliases[#](#id249 "Link to this heading")

* list\_intersect

### `array_join`[#](#array-join "Link to this heading")

*Alias of [array\_to\_string](#array-to-string).*

### `array_length`[#](#array-length "Link to this heading")

Returns the length of the array dimension.

```
array_length(array, dimension)
```

#### Arguments[#](#id250 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **dimension**: Array dimension.

#### Example[#](#id251 "Link to this heading")

```
> select array_length([1, 2, 3, 4, 5], 1);
+-------------------------------------------+
| array_length(List([1,2,3,4,5]), 1)        |
+-------------------------------------------+
| 5                                         |
+-------------------------------------------+
```

#### Aliases[#](#id252 "Link to this heading")

* list\_length

### `array_max`[#](#array-max "Link to this heading")

Returns the maximum value in the array.

```
array_max(array)
```

#### Arguments[#](#id253 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id254 "Link to this heading")

```
> select array_max([3,1,4,2]);
+-----------------------------------------+
| array_max(List([3,1,4,2]))              |
+-----------------------------------------+
| 4                                       |
+-----------------------------------------+
```

#### Aliases[#](#id255 "Link to this heading")

* list\_max

### `array_min`[#](#array-min "Link to this heading")

Returns the minimum value in the array.

```
array_min(array)
```

#### Arguments[#](#id256 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id257 "Link to this heading")

```
> select array_min([3,1,4,2]);
+-----------------------------------------+
| array_min(List([3,1,4,2]))              |
+-----------------------------------------+
| 1                                       |
+-----------------------------------------+
```

### `array_ndims`[#](#array-ndims "Link to this heading")

Returns the number of dimensions of the array.

```
array_ndims(array, element)
```

#### Arguments[#](#id258 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Array element.

#### Example[#](#id259 "Link to this heading")

```
> select array_ndims([[1, 2, 3], [4, 5, 6]]);
+----------------------------------+
| array_ndims(List([1,2,3,4,5,6])) |
+----------------------------------+
| 2                                |
+----------------------------------+
```

#### Aliases[#](#id260 "Link to this heading")

* list\_ndims

### `array_pop_back`[#](#array-pop-back "Link to this heading")

Returns the array without the last element.

```
array_pop_back(array)
```

#### Arguments[#](#id261 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id262 "Link to this heading")

```
> select array_pop_back([1, 2, 3]);
+-------------------------------+
| array_pop_back(List([1,2,3])) |
+-------------------------------+
| [1, 2]                        |
+-------------------------------+
```

#### Aliases[#](#id263 "Link to this heading")

* list\_pop\_back

### `array_pop_front`[#](#array-pop-front "Link to this heading")

Returns the array without the first element.

```
array_pop_front(array)
```

#### Arguments[#](#id264 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id265 "Link to this heading")

```
> select array_pop_front([1, 2, 3]);
+-------------------------------+
| array_pop_front(List([1,2,3])) |
+-------------------------------+
| [2, 3]                        |
+-------------------------------+
```

#### Aliases[#](#id266 "Link to this heading")

* list\_pop\_front

### `array_position`[#](#array-position "Link to this heading")

Returns the position of the first occurrence of the specified element in the array, or NULL if not found. Comparisons are done using `IS DISTINCT FROM` semantics, so NULL is considered to match NULL.

```
array_position(array, element)
array_position(array, element, index)
```

#### Arguments[#](#id267 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Element to search for in the array.
* **index**: Index at which to start searching (1-indexed).

#### Example[#](#id268 "Link to this heading")

```
> select array_position([1, 2, 2, 3, 1, 4], 2);
+----------------------------------------------+
| array_position(List([1,2,2,3,1,4]),Int64(2)) |
+----------------------------------------------+
| 2                                            |
+----------------------------------------------+
> select array_position([1, 2, 2, 3, 1, 4], 2, 3);
+----------------------------------------------------+
| array_position(List([1,2,2,3,1,4]),Int64(2), Int64(3)) |
+----------------------------------------------------+
| 3                                                  |
+----------------------------------------------------+
```

#### Aliases[#](#id269 "Link to this heading")

* list\_position
* array\_indexof
* list\_indexof

### `array_positions`[#](#array-positions "Link to this heading")

Searches for an element in the array, returns all occurrences.

```
array_positions(array, element)
```

#### Arguments[#](#id270 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Element to search for in the array.

#### Example[#](#id271 "Link to this heading")

```
> select array_positions([1, 2, 2, 3, 1, 4], 2);
+-----------------------------------------------+
| array_positions(List([1,2,2,3,1,4]),Int64(2)) |
+-----------------------------------------------+
| [2, 3]                                        |
+-----------------------------------------------+
```

#### Aliases[#](#id272 "Link to this heading")

* list\_positions

### `array_prepend`[#](#array-prepend "Link to this heading")

Prepends an element to the beginning of an array.

```
array_prepend(element, array)
```

#### Arguments[#](#id273 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Element to prepend to the array.

#### Example[#](#id274 "Link to this heading")

```
> select array_prepend(1, [2, 3, 4]);
+---------------------------------------+
| array_prepend(Int64(1),List([2,3,4])) |
+---------------------------------------+
| [1, 2, 3, 4]                          |
+---------------------------------------+
```

#### Aliases[#](#id275 "Link to this heading")

* list\_prepend
* array\_push\_front
* list\_push\_front

### `array_push_back`[#](#array-push-back "Link to this heading")

*Alias of [array\_append](#array-append).*

### `array_push_front`[#](#array-push-front "Link to this heading")

*Alias of [array\_prepend](#array-prepend).*

### `array_remove`[#](#array-remove "Link to this heading")

Removes the first element from the array equal to the given value. NULL elements already in the array are preserved when removing a non-NULL value. If `element` evaluates to NULL, the result is NULL rather than removing NULL entries.

```
array_remove(array, element)
```

#### Arguments[#](#id276 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Element to be removed from the array.

#### Example[#](#id277 "Link to this heading")

```
> select array_remove([1, 2, 2, 3, 2, 1, 4], 2);
+----------------------------------------------+
| array_remove(List([1,2,2,3,2,1,4]),Int64(2)) |
+----------------------------------------------+
| [1, 2, 3, 2, 1, 4]                           |
+----------------------------------------------+

> select array_remove([1, 2, NULL, 2, 4], 2);
+---------------------------------------------------+
| array_remove(List([1,2,NULL,2,4]),Int64(2)) |
+---------------------------------------------------+
| [1, NULL, 2, 4]                              |
+---------------------------------------------------+
```

#### Aliases[#](#id278 "Link to this heading")

* list\_remove

### `array_remove_all`[#](#array-remove-all "Link to this heading")

Removes all elements from the array equal to the given value. NULL elements already in the array are preserved when removing a non-NULL value. If `element` evaluates to NULL, the result is NULL rather than removing NULL entries.

```
array_remove_all(array, element)
```

#### Arguments[#](#id279 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Element to be removed from the array.

#### Example[#](#id280 "Link to this heading")

```
> select array_remove_all([1, 2, 2, 3, 2, 1, 4], 2);
+--------------------------------------------------+
| array_remove_all(List([1,2,2,3,2,1,4]),Int64(2)) |
+--------------------------------------------------+
| [1, 3, 1, 4]                                     |
+--------------------------------------------------+

> select array_remove_all([1, 2, NULL, 2, 4], 2);
+-----------------------------------------------------+
| array_remove_all(List([1,2,NULL,2,4]),Int64(2)) |
+-----------------------------------------------------+
| [1, NULL, 4]                                     |
+-----------------------------------------------------+
```

#### Aliases[#](#id281 "Link to this heading")

* list\_remove\_all

### `array_remove_n`[#](#array-remove-n "Link to this heading")

Removes the first `max` elements from the array equal to the given value. NULL elements already in the array are preserved when removing a non-NULL value. If `element` evaluates to NULL, the result is NULL rather than removing NULL entries.

```
array_remove_n(array, element, max)
```

#### Arguments[#](#id282 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **element**: Element to be removed from the array.
* **max**: Number of first occurrences to remove.

#### Example[#](#id283 "Link to this heading")

```
> select array_remove_n([1, 2, 2, 3, 2, 1, 4], 2, 2);
+---------------------------------------------------------+
| array_remove_n(List([1,2,2,3,2,1,4]),Int64(2),Int64(2)) |
+---------------------------------------------------------+
| [1, 3, 2, 1, 4]                                         |
+---------------------------------------------------------+

> select array_remove_n([1, 2, NULL, 2, 4], 2, 2);
+----------------------------------------------------------+
| array_remove_n(List([1,2,NULL,2,4]),Int64(2),Int64(2)) |
+----------------------------------------------------------+
| [1, NULL, 4]                                            |
+----------------------------------------------------------+
```

#### Aliases[#](#id284 "Link to this heading")

* list\_remove\_n

### `array_repeat`[#](#array-repeat "Link to this heading")

Returns an array containing element `count` times.

```
array_repeat(element, count)
```

#### Arguments[#](#id285 "Link to this heading")

* **element**: Element expression. Can be a constant, column, or function, and any combination of array operators.
* **count**: Value of how many times to repeat the element.

#### Example[#](#id286 "Link to this heading")

```
> select array_repeat(1, 3);
+---------------------------------+
| array_repeat(Int64(1),Int64(3)) |
+---------------------------------+
| [1, 1, 1]                       |
+---------------------------------+
> select array_repeat([1, 2], 2);
+------------------------------------+
| array_repeat(List([1,2]),Int64(2)) |
+------------------------------------+
| [[1, 2], [1, 2]]                   |
+------------------------------------+
```

#### Aliases[#](#id287 "Link to this heading")

* list\_repeat

### `array_replace`[#](#array-replace "Link to this heading")

Replaces the first occurrence of the specified element with another specified element.

```
array_replace(array, from, to)
```

#### Arguments[#](#id288 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **from**: Initial element.
* **to**: Final element.

#### Example[#](#id289 "Link to this heading")

```
> select array_replace([1, 2, 2, 3, 2, 1, 4], 2, 5);
+--------------------------------------------------------+
| array_replace(List([1,2,2,3,2,1,4]),Int64(2),Int64(5)) |
+--------------------------------------------------------+
| [1, 5, 2, 3, 2, 1, 4]                                  |
+--------------------------------------------------------+
```

#### Aliases[#](#id290 "Link to this heading")

* list\_replace

### `array_replace_all`[#](#array-replace-all "Link to this heading")

Replaces all occurrences of the specified element with another specified element.

```
array_replace_all(array, from, to)
```

#### Arguments[#](#id291 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **from**: Initial element.
* **to**: Final element.

#### Example[#](#id292 "Link to this heading")

```
> select array_replace_all([1, 2, 2, 3, 2, 1, 4], 2, 5);
+------------------------------------------------------------+
| array_replace_all(List([1,2,2,3,2,1,4]),Int64(2),Int64(5)) |
+------------------------------------------------------------+
| [1, 5, 5, 3, 5, 1, 4]                                      |
+------------------------------------------------------------+
```

#### Aliases[#](#id293 "Link to this heading")

* list\_replace\_all

### `array_replace_n`[#](#array-replace-n "Link to this heading")

Replaces the first `max` occurrences of the specified element with another specified element.

```
array_replace_n(array, from, to, max)
```

#### Arguments[#](#id294 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **from**: Initial element.
* **to**: Final element.
* **max**: Number of first occurrences to replace.

#### Example[#](#id295 "Link to this heading")

```
> select array_replace_n([1, 2, 2, 3, 2, 1, 4], 2, 5, 2);
+-------------------------------------------------------------------+
| array_replace_n(List([1,2,2,3,2,1,4]),Int64(2),Int64(5),Int64(2)) |
+-------------------------------------------------------------------+
| [1, 5, 5, 3, 2, 1, 4]                                             |
+-------------------------------------------------------------------+
```

#### Aliases[#](#id296 "Link to this heading")

* list\_replace\_n

### `array_resize`[#](#array-resize "Link to this heading")

Resizes the list to contain size elements. Initializes new elements with value or empty if value is not set.

```
array_resize(array, size, value)
```

#### Arguments[#](#id297 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **size**: New size of given array.
* **value**: Defines new elements’ value or empty if value is not set.

#### Example[#](#id298 "Link to this heading")

```
> select array_resize([1, 2, 3], 5, 0);
+-------------------------------------+
| array_resize(List([1,2,3],5,0))     |
+-------------------------------------+
| [1, 2, 3, 0, 0]                     |
+-------------------------------------+
```

#### Aliases[#](#id299 "Link to this heading")

* list\_resize

### `array_reverse`[#](#array-reverse "Link to this heading")

Returns the array with the order of the elements reversed.

```
array_reverse(array)
```

#### Arguments[#](#id300 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id301 "Link to this heading")

```
> select array_reverse([1, 2, 3, 4]);
+------------------------------------------------------------+
| array_reverse(List([1, 2, 3, 4]))                          |
+------------------------------------------------------------+
| [4, 3, 2, 1]                                               |
+------------------------------------------------------------+
```

#### Aliases[#](#id302 "Link to this heading")

* list\_reverse

### `array_slice`[#](#array-slice "Link to this heading")

Returns a slice of the array based on 1-indexed start and end positions.

```
array_slice(array, begin, end)
```

#### Arguments[#](#id303 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **begin**: Index of the first element. If negative, it counts backward from the end of the array.
* **end**: Index of the last element. If negative, it counts backward from the end of the array.
* **stride**: Stride of the array slice. The default is 1.

#### Example[#](#id304 "Link to this heading")

```
> select array_slice([1, 2, 3, 4, 5, 6, 7, 8], 3, 6);
+--------------------------------------------------------+
| array_slice(List([1,2,3,4,5,6,7,8]),Int64(3),Int64(6)) |
+--------------------------------------------------------+
| [3, 4, 5, 6]                                           |
+--------------------------------------------------------+
```

#### Aliases[#](#id305 "Link to this heading")

* list\_slice

### `array_sort`[#](#array-sort "Link to this heading")

Sort array.

```
array_sort(array, desc, nulls_first)
```

#### Arguments[#](#id306 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **desc**: Whether to sort in ascending (`ASC`) or descending (`DESC`) order. The default is `ASC`.
* **nulls\_first**: Whether to sort nulls first (`NULLS FIRST`) or last (`NULLS LAST`). The default is `NULLS FIRST`.

#### Example[#](#id307 "Link to this heading")

```
> select array_sort([3, 1, 2]);
+-----------------------------+
| array_sort(List([3,1,2]))   |
+-----------------------------+
| [1, 2, 3]                   |
+-----------------------------+
```

#### Aliases[#](#id308 "Link to this heading")

* list\_sort

### `array_to_string`[#](#array-to-string "Link to this heading")

Converts each element to its text representation.

```
array_to_string(array, delimiter[, null_string])
```

#### Arguments[#](#id309 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **delimiter**: Array element separator.
* **null\_string**: Optional. String to use for null values in the output. If not provided, nulls will be omitted.

#### Example[#](#id310 "Link to this heading")

```
> select array_to_string([[1, 2, 3, 4], [5, 6, 7, 8]], ',');
+----------------------------------------------------+
| array_to_string(List([1,2,3,4,5,6,7,8]),Utf8(",")) |
+----------------------------------------------------+
| 1,2,3,4,5,6,7,8                                    |
+----------------------------------------------------+
```

#### Aliases[#](#id311 "Link to this heading")

* list\_to\_string
* array\_join
* list\_join

### `array_union`[#](#array-union "Link to this heading")

Returns an array of elements that are present in both arrays (all elements from both arrays) without duplicates.

```
array_union(array1, array2)
```

#### Arguments[#](#id312 "Link to this heading")

* **array1**: Array expression. Can be a constant, column, or function, and any combination of array operators.
* **array2**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id313 "Link to this heading")

```
> select array_union([1, 2, 3, 4], [5, 6, 3, 4]);
+----------------------------------------------------+
| array_union([1, 2, 3, 4], [5, 6, 3, 4]);           |
+----------------------------------------------------+
| [1, 2, 3, 4, 5, 6]                                 |
+----------------------------------------------------+
> select array_union([1, 2, 3, 4], [5, 6, 7, 8]);
+----------------------------------------------------+
| array_union([1, 2, 3, 4], [5, 6, 7, 8]);           |
+----------------------------------------------------+
| [1, 2, 3, 4, 5, 6, 7, 8]                           |
+----------------------------------------------------+
```

#### Aliases[#](#id314 "Link to this heading")

* list\_union

### `arrays_overlap`[#](#arrays-overlap "Link to this heading")

*Alias of [array\_has\_any](#array-has-any).*

### `arrays_zip`[#](#arrays-zip "Link to this heading")

Returns an array of structs created by combining the elements of each input array at the same index. If the arrays have different lengths, shorter arrays are padded with NULLs.

```
arrays_zip(array1[, ..., array_n])
```

#### Arguments[#](#id315 "Link to this heading")

* **array1**: First array expression.
* **array\_n**: Optional additional array expressions.

#### Example[#](#id316 "Link to this heading")

```
> select arrays_zip([1, 2, 3]);
+---------------------------------------------------+
| arrays_zip([1, 2, 3])                             |
+---------------------------------------------------+
| [{1: 1}, {1: 2}, {1: 3}]                          |
+---------------------------------------------------+
> select arrays_zip([1, 2], [3, 4, 5]);
+---------------------------------------------------+
| arrays_zip([1, 2], [3, 4, 5])                     |
+---------------------------------------------------+
| [{1: 1, 2: 3}, {1: 2, 2: 4}, {1: NULL, 2: 5}]     |
+---------------------------------------------------+
```

#### Aliases[#](#id317 "Link to this heading")

* list\_zip

### `cardinality`[#](#cardinality "Link to this heading")

Returns the total number of elements in the array.

```
cardinality(array)
```

#### Arguments[#](#id318 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id319 "Link to this heading")

```
> select cardinality([[1, 2, 3, 4], [5, 6, 7, 8]]);
+--------------------------------------+
| cardinality(List([1,2,3,4,5,6,7,8])) |
+--------------------------------------+
| 8                                    |
+--------------------------------------+
```

### `empty`[#](#empty "Link to this heading")

Returns 1 for an empty array or 0 for a non-empty array.

```
empty(array)
```

#### Arguments[#](#id320 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id321 "Link to this heading")

```
> select empty([1]);
+------------------+
| empty(List([1])) |
+------------------+
| 0                |
+------------------+
```

#### Aliases[#](#id322 "Link to this heading")

* array\_empty
* list\_empty

### `flatten`[#](#flatten "Link to this heading")

Converts an array of arrays to a flat array.

* Applies to any depth of nested arrays
* Does not change arrays that are already flat

The flattened array contains all the elements from all source arrays.

```
flatten(array)
```

#### Arguments[#](#id323 "Link to this heading")

* **array**: Array expression. Can be a constant, column, or function, and any combination of array operators.

#### Example[#](#id324 "Link to this heading")

```
> select flatten([[1, 2], [3, 4]]);
+------------------------------+
| flatten(List([1,2], [3,4]))  |
+------------------------------+
| [1, 2, 3, 4]                 |
+------------------------------+
```

### `generate_series`[#](#generate-series "Link to this heading")

Similar to the range function, but it includes the upper bound.

```
generate_series(stop)
generate_series(start, stop[, step])
```

#### Arguments[#](#id325 "Link to this heading")

* **start**: Start of the series. Ints, timestamps, dates or string types that can be coerced to Date32 are supported.
* **end**: End of the series (included). Type must be the same as start.
* **step**: Increase by step (can not be 0). Steps less than a day are supported only for timestamp ranges.

#### Example[#](#id326 "Link to this heading")

```
> select generate_series(1,3);
+------------------------------------+
| generate_series(Int64(1),Int64(3)) |
+------------------------------------+
| [1, 2, 3]                          |
+------------------------------------+
```

### `list_any_value`[#](#list-any-value "Link to this heading")

*Alias of [array\_any\_value](#array-any-value).*

### `list_append`[#](#list-append "Link to this heading")

*Alias of [array\_append](#array-append).*

### `list_cat`[#](#list-cat "Link to this heading")

*Alias of [array\_concat](#array-concat).*

### `list_compact`[#](#list-compact "Link to this heading")

*Alias of [array\_compact](#array-compact).*

### `list_concat`[#](#list-concat "Link to this heading")

*Alias of [array\_concat](#array-concat).*

### `list_contains`[#](#list-contains "Link to this heading")

*Alias of [array\_has](#array-has).*

### `list_dims`[#](#list-dims "Link to this heading")

*Alias of [array\_dims](#array-dims).*

### `list_distance`[#](#list-distance "Link to this heading")

*Alias of [array\_distance](#array-distance).*

### `list_distinct`[#](#list-distinct "Link to this heading")

*Alias of [array\_distinct](#array-distinct).*

### `list_element`[#](#list-element "Link to this heading")

*Alias of [array\_element](#array-element).*

### `list_empty`[#](#list-empty "Link to this heading")

*Alias of [empty](#empty).*

### `list_except`[#](#list-except "Link to this heading")

*Alias of [array\_except](#array-except).*

### `list_extract`[#](#list-extract "Link to this heading")

*Alias of [array\_element](#array-element).*

### `list_has`[#](#list-has "Link to this heading")

*Alias of [array\_has](#array-has).*

### `list_has_all`[#](#list-has-all "Link to this heading")

*Alias of [array\_has\_all](#array-has-all).*

### `list_has_any`[#](#list-has-any "Link to this heading")

*Alias of [array\_has\_any](#array-has-any).*

### `list_indexof`[#](#list-indexof "Link to this heading")

*Alias of [array\_position](#array-position).*

### `list_intersect`[#](#list-intersect "Link to this heading")

*Alias of [array\_intersect](#array-intersect).*

### `list_join`[#](#list-join "Link to this heading")

*Alias of [array\_to\_string](#array-to-string).*

### `list_length`[#](#list-length "Link to this heading")

*Alias of [array\_length](#array-length).*

### `list_max`[#](#list-max "Link to this heading")

*Alias of [array\_max](#array-max).*

### `list_ndims`[#](#list-ndims "Link to this heading")

*Alias of [array\_ndims](#array-ndims).*

### `list_pop_back`[#](#list-pop-back "Link to this heading")

*Alias of [array\_pop\_back](#array-pop-back).*

### `list_pop_front`[#](#list-pop-front "Link to this heading")

*Alias of [array\_pop\_front](#array-pop-front).*

### `list_position`[#](#list-position "Link to this heading")

*Alias of [array\_position](#array-position).*

### `list_positions`[#](#list-positions "Link to this heading")

*Alias of [array\_positions](#array-positions).*

### `list_prepend`[#](#list-prepend "Link to this heading")

*Alias of [array\_prepend](#array-prepend).*

### `list_push_back`[#](#list-push-back "Link to this heading")

*Alias of [array\_append](#array-append).*

### `list_push_front`[#](#list-push-front "Link to this heading")

*Alias of [array\_prepend](#array-prepend).*

### `list_remove`[#](#list-remove "Link to this heading")

*Alias of [array\_remove](#array-remove).*

### `list_remove_all`[#](#list-remove-all "Link to this heading")

*Alias of [array\_remove\_all](#array-remove-all).*

### `list_remove_n`[#](#list-remove-n "Link to this heading")

*Alias of [array\_remove\_n](#array-remove-n).*

### `list_repeat`[#](#list-repeat "Link to this heading")

*Alias of [array\_repeat](#array-repeat).*

### `list_replace`[#](#list-replace "Link to this heading")

*Alias of [array\_replace](#array-replace).*

### `list_replace_all`[#](#list-replace-all "Link to this heading")

*Alias of [array\_replace\_all](#array-replace-all).*

### `list_replace_n`[#](#list-replace-n "Link to this heading")

*Alias of [array\_replace\_n](#array-replace-n).*

### `list_resize`[#](#list-resize "Link to this heading")

*Alias of [array\_resize](#array-resize).*

### `list_reverse`[#](#list-reverse "Link to this heading")

*Alias of [array\_reverse](#array-reverse).*

### `list_slice`[#](#list-slice "Link to this heading")

*Alias of [array\_slice](#array-slice).*

### `list_sort`[#](#list-sort "Link to this heading")

*Alias of [array\_sort](#array-sort).*

### `list_to_string`[#](#list-to-string "Link to this heading")

*Alias of [array\_to\_string](#array-to-string).*

### `list_union`[#](#list-union "Link to this heading")

*Alias of [array\_union](#array-union).*

### `list_zip`[#](#list-zip "Link to this heading")

*Alias of [arrays\_zip](#arrays-zip).*

### `make_array`[#](#make-array "Link to this heading")

Returns an array using the specified input expressions.

```
make_array(expression1[, ..., expression_n])
```

#### Arguments[#](#id327 "Link to this heading")

* **expression\_n**: Expression to include in the output array. Can be a constant, column, or function, and any combination of arithmetic or string operators.

#### Example[#](#id328 "Link to this heading")

```
> select make_array(1, 2, 3, 4, 5);
+----------------------------------------------------------+
| make_array(Int64(1),Int64(2),Int64(3),Int64(4),Int64(5)) |
+----------------------------------------------------------+
| [1, 2, 3, 4, 5]                                          |
+----------------------------------------------------------+
```

#### Aliases[#](#id329 "Link to this heading")

* make\_list

### `make_list`[#](#make-list "Link to this heading")

*Alias of [make\_array](#make-array).*

### `range`[#](#range "Link to this heading")

Returns an Arrow array between start and stop with step. The range start..end contains all values with start <= x < end. It is empty if start >= end. Step cannot be 0.

```
range(stop)
range(start, stop[, step])
```

#### Arguments[#](#id330 "Link to this heading")

* **start**: Start of the range. Ints, timestamps, dates or string types that can be coerced to Date32 are supported.
* **end**: End of the range (not included). Type must be the same as start.
* **step**: Increase by step (cannot be 0). Steps less than a day are supported only for timestamp ranges.

#### Example[#](#id331 "Link to this heading")

```
> select range(2, 10, 3);
+-----------------------------------+
| range(Int64(2),Int64(10),Int64(3))|
+-----------------------------------+
| [2, 5, 8]                         |
+-----------------------------------+

> select range(DATE '1992-09-01', DATE '1993-03-01', INTERVAL '1' MONTH);
+--------------------------------------------------------------------------+
| range(DATE '1992-09-01', DATE '1993-03-01', INTERVAL '1' MONTH)          |
+--------------------------------------------------------------------------+
| [1992-09-01, 1992-10-01, 1992-11-01, 1992-12-01, 1993-01-01, 1993-02-01] |
+--------------------------------------------------------------------------+
```

### `string_to_array`[#](#string-to-array "Link to this heading")

Splits a string into an array of substrings based on a delimiter. Any substrings matching the optional `null_str` argument are replaced with NULL.

```
string_to_array(str, delimiter[, null_str])
```

#### Arguments[#](#id332 "Link to this heading")

* **str**: String expression to split.
* **delimiter**: Delimiter string to split on.
* **null\_str**: Substring values to be replaced with `NULL`.

#### Example[#](#id333 "Link to this heading")

```
> select string_to_array('abc##def', '##');
+-----------------------------------+
| string_to_array(Utf8('abc##def'))  |
+-----------------------------------+
| ['abc', 'def']                    |
+-----------------------------------+
> select string_to_array('abc def', ' ', 'def');
+---------------------------------------------+
| string_to_array(Utf8('abc def'), Utf8(' '), Utf8('def')) |
+---------------------------------------------+
| ['abc', NULL]                               |
+---------------------------------------------+
```

#### Aliases[#](#id334 "Link to this heading")

* string\_to\_list

### `string_to_list`[#](#string-to-list "Link to this heading")

*Alias of [string\_to\_array](#string-to-array).*

## Struct Functions[#](#struct-functions "Link to this heading")

* [named\_struct](#named-struct)
* [row](#row)
* [struct](#struct)

### `named_struct`[#](#named-struct "Link to this heading")

Returns an Arrow struct using the specified name and input expressions pairs.
For information on comparing and ordering struct values (including `NULL` handling),
see [Comparison and Ordering](struct_coercion.html#comparison-and-ordering).

```
named_struct(expression1_name, expression1_input[, ..., expression_n_name, expression_n_input])
```

#### Arguments[#](#id335 "Link to this heading")

* **expression\_n\_name**: Name of the column field. Must be a constant string.
* **expression\_n\_input**: Expression to include in the output struct. Can be a constant, column, or function, and any combination of arithmetic or string operators.

#### Example[#](#id336 "Link to this heading")

For example, this query converts two columns `a` and `b` to a single column with
a struct type of fields `field_a` and `field_b`:

```
> select * from t;
+---+---+
| a | b |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+
> select named_struct('field_a', a, 'field_b', b) from t;
+-------------------------------------------------------+
| named_struct(Utf8("field_a"),t.a,Utf8("field_b"),t.b) |
+-------------------------------------------------------+
| {field_a: 1, field_b: 2}                              |
| {field_a: 3, field_b: 4}                              |
+-------------------------------------------------------+
```

### `row`[#](#row "Link to this heading")

*Alias of [struct](#struct).*

### `struct`[#](#struct "Link to this heading")

Returns an Arrow struct using the specified input expressions optionally named.
Fields in the returned struct use the optional name or the `cN` naming convention.
For example: `c0`, `c1`, `c2`, etc.
For information on comparing and ordering struct values (including `NULL` handling),
see [Comparison and Ordering](struct_coercion.html#comparison-and-ordering).

```
struct(expression1[, ..., expression_n])
```

#### Arguments[#](#id337 "Link to this heading")

* **expression1, expression\_n**: Expression to include in the output struct. Can be a constant, column, or function, any combination of arithmetic or string operators.

#### Example[#](#id338 "Link to this heading")

For example, this query converts two columns `a` and `b` to a single column with
a struct type of fields `field_a` and `c1`:

```
> select * from t;
+---+---+
| a | b |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+

-- use default names `c0`, `c1`
> select struct(a, b) from t;
+-----------------+
| struct(t.a,t.b) |
+-----------------+
| {c0: 1, c1: 2}  |
| {c0: 3, c1: 4}  |
+-----------------+

-- name the first field `field_a`
select struct(a as field_a, b) from t;
+--------------------------------------------------+
| named_struct(Utf8("field_a"),t.a,Utf8("c1"),t.b) |
+--------------------------------------------------+
| {field_a: 1, c1: 2}                              |
| {field_a: 3, c1: 4}                              |
+--------------------------------------------------+
```

#### Aliases[#](#id339 "Link to this heading")

* row

## Map Functions[#](#map-functions "Link to this heading")

* [element\_at](#element-at)
* [map](#map)
* [map\_entries](#map-entries)
* [map\_extract](#map-extract)
* [map\_keys](#map-keys)
* [map\_values](#map-values)

### `element_at`[#](#element-at "Link to this heading")

*Alias of [map\_extract](#map-extract).*

### `map`[#](#map "Link to this heading")

Returns an Arrow map with the specified key-value pairs.

The `make_map` function creates a map from two lists: one for keys and one for values. Each key must be unique and non-null.

```
map(key, value)
map(key: value)
make_map(['key1', 'key2'], ['value1', 'value2'])
```

#### Arguments[#](#id340 "Link to this heading")

* **key**: For `map`: Expression to be used for key. Can be a constant, column, function, or any combination of arithmetic or string operators.
  For `make_map`: The list of keys to be used in the map. Each key must be unique and non-null.
* **value**: For `map`: Expression to be used for value. Can be a constant, column, function, or any combination of arithmetic or string operators.
  For `make_map`: The list of values to be mapped to the corresponding keys.

#### Example[#](#id341 "Link to this heading")

```
-- Using map function
SELECT MAP('type', 'test');
----
{type: test}

SELECT MAP(['POST', 'HEAD', 'PATCH'], [41, 33, null]);
----
{POST: 41, HEAD: 33, PATCH: NULL}

SELECT MAP([[1,2], [3,4]], ['a', 'b']);
----
{[1, 2]: a, [3, 4]: b}

SELECT MAP { 'a': 1, 'b': 2 };
----
{a: 1, b: 2}

-- Using make_map function
SELECT MAKE_MAP(['POST', 'HEAD'], [41, 33]);
----
{POST: 41, HEAD: 33}

SELECT MAKE_MAP(['key1', 'key2'], ['value1', null]);
----
{key1: value1, key2: }
```

### `map_entries`[#](#map-entries "Link to this heading")

Returns a list of all entries in the map.

```
map_entries(map)
```

#### Arguments[#](#id342 "Link to this heading")

* **map**: Map expression. Can be a constant, column, or function, and any combination of map operators.

#### Example[#](#id343 "Link to this heading")

```
SELECT map_entries(MAP {'a': 1, 'b': NULL, 'c': 3});
----
[{'key': a, 'value': 1}, {'key': b, 'value': NULL}, {'key': c, 'value': 3}]

SELECT map_entries(map([100, 5], [42, 43]));
----
[{'key': 100, 'value': 42}, {'key': 5, 'value': 43}]
```

### `map_extract`[#](#map-extract "Link to this heading")

Returns a list containing the value for the given key or an empty list if the key is not present in the map.

```
map_extract(map, key)
```

#### Arguments[#](#id344 "Link to this heading")

* **map**: Map expression. Can be a constant, column, or function, and any combination of map operators.
* **key**: Key to extract from the map. Can be a constant, column, or function, any combination of arithmetic or string operators, or a named expression of the previously listed.

#### Example[#](#id345 "Link to this heading")

```
SELECT map_extract(MAP {'a': 1, 'b': NULL, 'c': 3}, 'a');
----
[1]

SELECT map_extract(MAP {1: 'one', 2: 'two'}, 2);
----
['two']

SELECT map_extract(MAP {'x': 10, 'y': NULL, 'z': 30}, 'y');
----
[NULL]

-- non-existing key
SELECT map_extract(MAP {'x': 10, 'y': NULL, 'z': 30}, 'a');
----
[]
```

#### Aliases[#](#id346 "Link to this heading")

* element\_at

### `map_keys`[#](#map-keys "Link to this heading")

Returns a list of all keys in the map.

```
map_keys(map)
```

#### Arguments[#](#id347 "Link to this heading")

* **map**: Map expression. Can be a constant, column, or function, and any combination of map operators.

#### Example[#](#id348 "Link to this heading")

```
SELECT map_keys(MAP {'a': 1, 'b': NULL, 'c': 3});
----
[a, b, c]

SELECT map_keys(map([100, 5], [42, 43]));
----
[100, 5]
```

### `map_values`[#](#map-values "Link to this heading")

Returns a list of all values in the map.

```
map_values(map)
```

#### Arguments[#](#id349 "Link to this heading")

* **map**: Map expression. Can be a constant, column, or function, and any combination of map operators.

#### Example[#](#id350 "Link to this heading")

```
SELECT map_values(MAP {'a': 1, 'b': NULL, 'c': 3});
----
[1, , 3]

SELECT map_values(map([100, 5], [42, 43]));
----
[42, 43]
```

## Hashing Functions[#](#hashing-functions "Link to this heading")

* [digest](#digest)
* [md5](#md5)
* [sha224](#sha224)
* [sha256](#sha256)
* [sha384](#sha384)
* [sha512](#sha512)

### `digest`[#](#digest "Link to this heading")

Computes the binary hash of an expression using the specified algorithm.

```
digest(expression, algorithm)
```

#### Arguments[#](#id351 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **algorithm**: String expression specifying algorithm to use. Must be one of:

  * md5
  * sha224
  * sha256
  * sha384
  * sha512
  * blake2s
  * blake2b
  * blake3

#### Example[#](#id352 "Link to this heading")

```
> select digest('foo', 'sha256');
+------------------------------------------------------------------+
| digest(Utf8("foo"),Utf8("sha256"))                               |
+------------------------------------------------------------------+
| 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae |
+------------------------------------------------------------------+
```

### `md5`[#](#md5 "Link to this heading")

Computes an MD5 128-bit checksum for a string expression.

```
md5(expression)
```

#### Arguments[#](#id353 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id354 "Link to this heading")

```
> select md5('foo');
+----------------------------------+
| md5(Utf8("foo"))                 |
+----------------------------------+
| acbd18db4cc2f85cedef654fccc4a4d8 |
+----------------------------------+
```

### `sha224`[#](#sha224 "Link to this heading")

Computes the SHA-224 hash of a binary string.

```
sha224(expression)
```

#### Arguments[#](#id355 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id356 "Link to this heading")

```
> select sha224('foo');
+----------------------------------------------------------+
| sha224(Utf8("foo"))                                      |
+----------------------------------------------------------+
| 0808f64e60d58979fcb676c96ec938270dea42445aeefcd3a4e6f8db |
+----------------------------------------------------------+
```

### `sha256`[#](#sha256 "Link to this heading")

Computes the SHA-256 hash of a binary string.

```
sha256(expression)
```

#### Arguments[#](#id357 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id358 "Link to this heading")

```
> select sha256('foo');
+------------------------------------------------------------------+
| sha256(Utf8("foo"))                                              |
+------------------------------------------------------------------+
| 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae |
+------------------------------------------------------------------+
```

### `sha384`[#](#sha384 "Link to this heading")

Computes the SHA-384 hash of a binary string.

```
sha384(expression)
```

#### Arguments[#](#id359 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id360 "Link to this heading")

```
> select sha384('foo');
+--------------------------------------------------------------------------------------------------+
| sha384(Utf8("foo"))                                                                              |
+--------------------------------------------------------------------------------------------------+
| 98c11ffdfdd540676b1a137cb1a22b2a70350c9a44171d6b1180c6be5cbb2ee3f79d532c8a1dd9ef2e8e08e752a3babb |
+--------------------------------------------------------------------------------------------------+
```

### `sha512`[#](#sha512 "Link to this heading")

Computes the SHA-512 hash of a binary string.

```
sha512(expression)
```

#### Arguments[#](#id361 "Link to this heading")

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id362 "Link to this heading")

```
> select sha512('foo');
+----------------------------------------------------------------------------------------------------------------------------------+
| sha512(Utf8("foo"))                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------+
| f7fbba6e0636f890e56fbbf3283e524c6fa3204ae298382d624741d0dc6638326e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7 |
+----------------------------------------------------------------------------------------------------------------------------------+
```

## Union Functions[#](#union-functions "Link to this heading")

Functions to work with the union data type, also know as tagged unions, variant types, enums or sum types. Note: Not related to the SQL UNION operator

* [union\_extract](#union-extract)
* [union\_tag](#union-tag)

### `union_extract`[#](#union-extract "Link to this heading")

Returns the value of the given field in the union when selected, or NULL otherwise.

```
union_extract(union, field_name)
```

#### Arguments[#](#id363 "Link to this heading")

* **union**: Union expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **field\_name**: String expression to operate on. Must be a constant.

#### Example[#](#id364 "Link to this heading")

```
❯ select union_column, union_extract(union_column, 'a'), union_extract(union_column, 'b') from table_with_union;
+--------------+----------------------------------+----------------------------------+
| union_column | union_extract(union_column, 'a') | union_extract(union_column, 'b') |
+--------------+----------------------------------+----------------------------------+
| {a=1}        | 1                                |                                  |
| {b=3.0}      |                                  | 3.0                              |
| {a=4}        | 4                                |                                  |
| {b=}         |                                  |                                  |
| {a=}         |                                  |                                  |
+--------------+----------------------------------+----------------------------------+
```

### `union_tag`[#](#union-tag "Link to this heading")

Returns the name of the currently selected field in the union

```
union_tag(union_expression)
```

#### Arguments[#](#id365 "Link to this heading")

* **union**: Union expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id366 "Link to this heading")

```
❯ select union_column, union_tag(union_column) from table_with_union;
+--------------+-------------------------+
| union_column | union_tag(union_column) |
+--------------+-------------------------+
| {a=1}        | a                       |
| {b=3.0}      | b                       |
| {a=4}        | a                       |
| {b=}         | b                       |
| {a=}         | a                       |
+--------------+-------------------------+
```

## Other Functions[#](#other-functions "Link to this heading")

* [arrow\_cast](#arrow-cast)
* [arrow\_field](#arrow-field)
* [arrow\_metadata](#arrow-metadata)
* [arrow\_try\_cast](#arrow-try-cast)
* [arrow\_typeof](#arrow-typeof)
* [cast\_to\_type](#cast-to-type)
* [get\_field](#get-field)
* [try\_cast\_to\_type](#try-cast-to-type)
* [version](#version)
* [with\_metadata](#with-metadata)

### `arrow_cast`[#](#arrow-cast "Link to this heading")

Casts a value to a specific Arrow data type.

```
arrow_cast(expression, datatype)
```

#### Arguments[#](#id367 "Link to this heading")

* **expression**: Expression to cast. The expression can be a constant, column, or function, and any combination of operators.
* **datatype**: [Arrow data type](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) name to cast to, as a string. The format is the same as that returned by [`arrow_typeof`]

#### Example[#](#id368 "Link to this heading")

```
> select
  arrow_cast(-5,    'Int8') as a,
  arrow_cast('foo', 'Dictionary(Int32, Utf8)') as b,
  arrow_cast('bar', 'LargeUtf8') as c;

+----+-----+-----+
| a  | b   | c   |
+----+-----+-----+
| -5 | foo | bar |
+----+-----+-----+

> select
  arrow_cast('2023-01-02T12:53:02', 'Timestamp(µs, "+08:00")') as d,
  arrow_cast('2023-01-02T12:53:02', 'Timestamp(µs)') as e;

+---------------------------+---------------------+
| d                         | e                   |
+---------------------------+---------------------+
| 2023-01-02T12:53:02+08:00 | 2023-01-02T12:53:02 |
+---------------------------+---------------------+
```

### `arrow_field`[#](#arrow-field "Link to this heading")

Returns a struct containing the Arrow field information of the expression, including name, data type, nullability, and metadata.

```
arrow_field(expression)
```

#### Arguments[#](#id369 "Link to this heading")

* **expression**: Expression to evaluate. The expression can be a constant, column, or function, and any combination of operators.

#### Example[#](#id370 "Link to this heading")

```
> select arrow_field(1);
+-------------------------------------------------------------+
| arrow_field(Int64(1))                                       |
+-------------------------------------------------------------+
| {name: lit, data_type: Int64, nullable: false, metadata: {}} |
+-------------------------------------------------------------+

> select arrow_field(1)['data_type'];
+-----------------------------------+
| arrow_field(Int64(1))[data_type]  |
+-----------------------------------+
| Int64                             |
+-----------------------------------+
```

### `arrow_metadata`[#](#arrow-metadata "Link to this heading")

Returns the metadata of the input expression. If a key is provided, returns the value for that key. If no key is provided, returns a Map of all metadata.

```
arrow_metadata(expression[, key])
```

#### Arguments[#](#id371 "Link to this heading")

* **expression**: The expression to retrieve metadata from. Can be a column or other expression.
* **key**: Optional. The specific metadata key to retrieve.

#### Example[#](#id372 "Link to this heading")

```
> select arrow_metadata(col) from table;
+----------------------------+
| arrow_metadata(table.col)  |
+----------------------------+
| {k: v}                     |
+----------------------------+
> select arrow_metadata(col, 'k') from table;
+-------------------------------+
| arrow_metadata(table.col, 'k')|
+-------------------------------+
| v                             |
+-------------------------------+
```

### `arrow_try_cast`[#](#arrow-try-cast "Link to this heading")

Casts a value to a specific Arrow data type, returning NULL if the cast fails.

```
arrow_try_cast(expression, datatype)
```

#### Arguments[#](#id373 "Link to this heading")

* **expression**: Expression to cast. The expression can be a constant, column, or function, and any combination of operators.
* **datatype**: [Arrow data type](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) name to cast to, as a string. The format is the same as that returned by [`arrow_typeof`]

#### Example[#](#id374 "Link to this heading")

```
> select arrow_try_cast('123', 'Int64') as a,
         arrow_try_cast('not_a_number', 'Int64') as b;

+-----+------+
| a   | b    |
+-----+------+
| 123 | NULL |
+-----+------+
```

### `arrow_typeof`[#](#arrow-typeof "Link to this heading")

Returns the name of the underlying [Arrow data type](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) of the expression.

```
arrow_typeof(expression)
```

#### Arguments[#](#id375 "Link to this heading")

* **expression**: Expression to evaluate. The expression can be a constant, column, or function, and any combination of operators.

#### Example[#](#id376 "Link to this heading")

```
> select arrow_typeof('foo'), arrow_typeof(1);
+---------------------------+------------------------+
| arrow_typeof(Utf8("foo")) | arrow_typeof(Int64(1)) |
+---------------------------+------------------------+
| Utf8                      | Int64                  |
+---------------------------+------------------------+
```

### `cast_to_type`[#](#cast-to-type "Link to this heading")

Casts the first argument to the data type of the second argument. Only the type of the second argument is used; its value is ignored.

```
cast_to_type(expression, reference)
```

#### Arguments[#](#id377 "Link to this heading")

* **expression**: The expression to cast. It can be a constant, column, or function, and any combination of operators.
* **reference**: Reference expression whose data type determines the target cast type. The value is ignored.

#### Example[#](#id378 "Link to this heading")

```
> select cast_to_type('42', NULL::INTEGER) as a;
+----+
| a  |
+----+
| 42 |
+----+

> select cast_to_type(1 + 2, NULL::DOUBLE) as b;
+-----+
| b   |
+-----+
| 3.0 |
+-----+
```

### `get_field`[#](#get-field "Link to this heading")

Returns a field within a map or a struct with the given key.
Supports nested field access by providing multiple field names.
Note: most users invoke `get_field` indirectly via field access
syntax such as `my_struct_col['field_name']` which results in a call to
`get_field(my_struct_col, 'field_name')`.
Nested access like `my_struct['a']['b']` is optimized to a single call:
`get_field(my_struct, 'a', 'b')`.

```
get_field(expression, field_name[, field_name2, ...])
```

#### Arguments[#](#id379 "Link to this heading")

* **expression**: The map or struct to retrieve a field from.
* **field\_name**: The field name(s) to access, in order for nested access. Must evaluate to strings.

#### Example[#](#id380 "Link to this heading")

```
> -- Access a field from a struct column
> create table test( struct_col) as values
    ({name: 'Alice', age: 30}),
    ({name: 'Bob', age: 25});
> select struct_col from test;
+-----------------------------+
| struct_col                  |
+-----------------------------+
| {name: Alice, age: 30}      |
| {name: Bob, age: 25}        |
+-----------------------------+
> select struct_col['name'] as name from test;
+-------+
| name  |
+-------+
| Alice |
| Bob   |
+-------+

> -- Nested field access with multiple arguments
> create table test(struct_col) as values
    ({outer: {inner_val: 42}});
> select struct_col['outer']['inner_val'] as result from test;
+--------+
| result |
+--------+
| 42     |
+--------+
```

### `try_cast_to_type`[#](#try-cast-to-type "Link to this heading")

Casts the first argument to the data type of the second argument, returning NULL if the cast fails. Only the type of the second argument is used; its value is ignored.

```
try_cast_to_type(expression, reference)
```

#### Arguments[#](#id381 "Link to this heading")

* **expression**: The expression to cast. It can be a constant, column, or function, and any combination of operators.
* **reference**: Reference expression whose data type determines the target cast type. The value is ignored.

#### Example[#](#id382 "Link to this heading")

```
> select try_cast_to_type('123', NULL::INTEGER) as a,
         try_cast_to_type('not_a_number', NULL::INTEGER) as b;

+-----+------+
| a   | b    |
+-----+------+
| 123 | NULL |
+-----+------+
```

### `version`[#](#version "Link to this heading")

Returns the version of DataFusion.

```
version()
```

#### Example[#](#id383 "Link to this heading")

```
> select version();
+--------------------------------------------+
| version()                                  |
+--------------------------------------------+
| Apache DataFusion 42.0.0, aarch64 on macos |
+--------------------------------------------+
```

### `with_metadata`[#](#with-metadata "Link to this heading")

Attaches Arrow field metadata (key/value pairs) to the input expression. Keys must be non-empty constant strings and values must be constant strings (empty values are allowed). Existing metadata on the input field is preserved; new keys overwrite on collision. This is the inverse of `arrow_metadata`.

```
with_metadata(expression, key1, value1[, key2, value2, ...])
```

#### Arguments[#](#id384 "Link to this heading")

* **expression**: The expression whose output Arrow field should be annotated. Values flow through unchanged.
* **key**: Metadata key. Must be a non-empty constant string literal.
* **value**: Metadata value. Must be a constant string literal (may be empty).

#### Example[#](#id385 "Link to this heading")

```
> select arrow_metadata(with_metadata(column1, 'unit', 'ms'), 'unit') from (values (1));
+---------------------------------------------------------------+
| arrow_metadata(with_metadata(column1,Utf8("unit"),Utf8("ms")),Utf8("unit")) |
+---------------------------------------------------------------+
| ms                                                            |
+---------------------------------------------------------------+
> select arrow_metadata(with_metadata(column1, 'unit', 'ms', 'source', 'sensor')) from (values (1));
+--------------------------+
| {source: sensor, unit: ms} |
+--------------------------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/scalar_functions.md)

[Show Source](../../_sources/user-guide/sql/scalar_functions.md.txt)

---
# Usage[#](#usage "Link to this heading")

See the current usage using `datafusion-cli --help`:

```
Apache Arrow <dev@arrow.apache.org>
Command Line Client for DataFusion query engine.

USAGE:
    datafusion-cli [OPTIONS]

OPTIONS:
    -b, --batch-size <BATCH_SIZE>
            The batch size of each query, or use DataFusion default

    -c, --command <COMMAND>...
            Execute the given command string(s), then exit

        --color
            Enables console syntax highlighting

    -f, --file <FILE>...
            Execute commands from file(s), then exit

        --format <FORMAT>
            [default: table] [possible values: csv, tsv, table, json, nd-json]

    -h, --help
            Print help information

    -m, --memory-limit <MEMORY_LIMIT>
            The memory pool limitation (e.g. '10g'), default to None (no limit)

        --maxrows <MAXROWS>
            The max number of rows to display for 'Table' format
            [possible values: numbers(0/10/...), inf(no limit)] [default: 40]

        --mem-pool-type <MEM_POOL_TYPE>
            Specify the memory pool type 'greedy' or 'fair', default to 'greedy'

        --top-memory-consumers <TOP_MEMORY_CONSUMERS>
            The number of top memory consumers to display when query fails due to memory exhaustion.
            To disable memory consumer tracking, set this value to 0 [default: 3].
            Please set one of the runtime configs: '--memory-limit' or '--mem-pool-type' to see 'top-memory-consumers' result when memory is exhausted.

    -d, --disk-limit <DISK_LIMIT>
            Available disk space for spilling queries (e.g. '10g'), default to None (uses DataFusion's default value of '100g')

      --object-store-profiling <OBJECT_STORE_PROFILING>
          Specify the default object_store_profiling mode, defaults to 'disabled'.
          [possible values: disabled, summary, trace] [default: Disabled]

    -p, --data-path <DATA_PATH>
            Path to your data, default to current directory

    -q, --quiet
            Reduce printing other than the results and work quietly

    -r, --rc <RC>...
            Run the provided files on startup instead of ~/.datafusionrc

    -V, --version
            Print version information
```

## Commands[#](#commands "Link to this heading")

Available commands inside DataFusion CLI are:

* Quit

```
> \q
```

* Help

```
> \?
```

* ListTables

```
> \d
```

* DescribeTable

```
> \d table_name
```

* QuietMode

```
> \quiet [true|false]
```

* list function

```
> \h
```

* Search and describe function

```
> \h function
```

* Object Store Profiling Mode

```
> \object_store_profiling [disabled|summary|trace]
```

When enabled, prints detailed information about object store (I/O) operations
performed during query execution to STDOUT.

```
> \object_store_profiling trace
ObjectStore Profile mode set to Trace
> select count(*) from 'https://datasets.clickhouse.com/hits_compatible/athena_partitioned/hits_1.parquet';
+----------+
| count(*) |
+----------+
| 1000000  |
+----------+
1 row(s) fetched.
Elapsed 0.552 seconds.

Object Store Profiling
Instrumented Object Store: instrument_mode: Trace, inner: HttpStore
2025-10-17T18:08:48.457992+00:00 operation=Get duration=0.043592s size=8 range: bytes=174965036-174965043 path=hits_compatible/athena_partitioned/hits_1.parquet
2025-10-17T18:08:48.501878+00:00 operation=Get duration=0.031542s size=34322 range: bytes=174930714-174965035 path=hits_compatible/athena_partitioned/hits_1.parquet

Summaries:
+-----------+----------+-----------+-----------+-----------+-----------+-------+
| Operation | Metric   | min       | max       | avg       | sum       | count |
+-----------+----------+-----------+-----------+-----------+-----------+-------+
| Get       | duration | 0.031542s | 0.043592s | 0.037567s | 0.075133s | 2     |
| Get       | size     | 8 B       | 34322 B   | 17165 B   | 34330 B   | 2     |
+-----------+----------+-----------+-----------+-----------+-----------+-------+
```

## Supported SQL[#](#supported-sql "Link to this heading")

In addition to the normal [SQL supported in DataFusion](../sql/index.html), `datafusion-cli` also
supports additional statements and commands:

### `SHOW ALL [VERBOSE]`[#](#show-all-verbose "Link to this heading")

Show configuration options

```
> show all;

+-------------------------------------------------+---------+
| name                                            | value   |
+-------------------------------------------------+---------+
| datafusion.execution.batch_size                 | 8192    |
| datafusion.execution.coalesce_batches           | true    |
| datafusion.execution.time_zone                  | UTC     |
| datafusion.explain.logical_plan_only            | false   |
| datafusion.explain.physical_plan_only           | false   |
| datafusion.optimizer.filter_null_join_keys      | false   |
| datafusion.optimizer.skip_failed_rules          | true    |
+-------------------------------------------------+---------+
```

### `SHOW <OPTION>>`[#](#show-option "Link to this heading")

Show specific configuration option

```
> show datafusion.execution.batch_size;

+-------------------------------------------------+---------+
| name                                            | value   |
+-------------------------------------------------+---------+
| datafusion.execution.batch_size                 | 8192    |
+-------------------------------------------------+---------+
```

### `SET <OPTION> TO <VALUE>`[#](#set-option-to-value "Link to this heading")

* Set configuration options

```
> SET datafusion.execution.batch_size to 1024;
```

## Configuration Options[#](#configuration-options "Link to this heading")

All available configuration options can be seen using `SHOW ALL` as described above.

You can change the configuration options using environment
variables. `datafusion-cli` looks in the corresponding environment
variable with an upper case name and all `.` converted to `_`.

For example, to set `datafusion.execution.batch_size` to `1024` you
would set the `DATAFUSION_EXECUTION_BATCH_SIZE` environment variable
appropriately:

```
$ DATAFUSION_EXECUTION_BATCH_SIZE=1024 datafusion-cli
DataFusion CLI v12.0.0
> show all;
+-------------------------------------------------+---------+
| name                                            | value   |
+-------------------------------------------------+---------+
| datafusion.execution.batch_size                 | 1024    |
| datafusion.execution.coalesce_batches           | true    |
| datafusion.execution.time_zone                  | UTC     |
| datafusion.explain.logical_plan_only            | false   |
| datafusion.explain.physical_plan_only           | false   |
| datafusion.optimizer.filter_null_join_keys      | false   |
| datafusion.optimizer.skip_failed_rules          | true    |
+-------------------------------------------------+---------+
8 rows in set. Query took 0.002 seconds.
```

You can change the configuration options using `SET` statement as well

```
$ datafusion-cli
DataFusion CLI v13.0.0
> show datafusion.execution.batch_size;
+---------------------------------+---------+
| name                            | value   |
+---------------------------------+---------+
| datafusion.execution.batch_size | 8192    |
+---------------------------------+---------+
1 row in set. Query took 0.011 seconds.

> set datafusion.execution.batch_size to 1024;
0 rows in set. Query took 0.000 seconds.

> show datafusion.execution.batch_size;
+---------------------------------+---------+
| name                            | value   |
+---------------------------------+---------+
| datafusion.execution.batch_size | 1024    |
+---------------------------------+---------+
1 row in set. Query took 0.005 seconds.
```

## Functions[#](#functions "Link to this heading")

`datafusion-cli` comes with build-in functions that are not included in the
DataFusion SQL engine, see [DataFusion CLI specific functions](functions.html) section
for details.

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/cli/usage.md)

[Show Source](../../_sources/user-guide/cli/usage.md.txt)

---
# Window Functions[#](#window-functions "Link to this heading")

A *window function* performs a calculation across a set of table rows that are somehow related to the current row.
This is comparable to the type of calculation that can be done with an aggregate function.
However, window functions do not cause rows to become grouped into a single output row like non-window aggregate calls would.
Instead, the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result

Here is an example that shows how to compare each employee’s salary with the average salary in his or her department:

```
SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;

+-----------+-------+--------+-------------------+
| depname   | empno | salary | avg               |
+-----------+-------+--------+-------------------+
| personnel | 2     | 3900   | 3700.0            |
| personnel | 5     | 3500   | 3700.0            |
| develop   | 8     | 6000   | 5020.0            |
| develop   | 10    | 5200   | 5020.0            |
| develop   | 11    | 5200   | 5020.0            |
| develop   | 9     | 4500   | 5020.0            |
| develop   | 7     | 4200   | 5020.0            |
| sales     | 1     | 5000   | 4866.666666666667 |
| sales     | 4     | 4800   | 4866.666666666667 |
| sales     | 3     | 4800   | 4866.666666666667 |
+-----------+-------+--------+-------------------+
```

A window function call always contains an OVER clause directly following the window function’s name and argument(s). This is what syntactically distinguishes it from a normal function or non-window aggregate. The OVER clause determines exactly how the rows of the query are split up for processing by the window function. The PARTITION BY clause within OVER divides the rows into groups, or partitions, that share the same values of the PARTITION BY expression(s). For each row, the window function is computed across the rows that fall into the same partition as the current row. The previous example showed how to count the average of a column per partition.

You can also control the order in which rows are processed by window functions using ORDER BY within OVER. (The window ORDER BY does not even have to match the order in which the rows are output.) Here is an example:

```
SELECT depname, empno, salary,
       rank() OVER (PARTITION BY depname ORDER BY salary DESC)
FROM empsalary;

+-----------+-------+--------+--------+
| depname   | empno | salary | rank   |
+-----------+-------+--------+--------+
| personnel | 2     | 3900   | 1      |
| develop   | 8     | 6000   | 1      |
| develop   | 10    | 5200   | 2      |
| develop   | 11    | 5200   | 2      |
| develop   | 9     | 4500   | 4      |
| develop   | 7     | 4200   | 5      |
| sales     | 1     | 5000   | 1      |
| sales     | 4     | 4800   | 2      |
| personnel | 5     | 3500   | 2      |
| sales     | 3     | 4800   | 2      |
+-----------+-------+--------+--------+
```

There is another important concept associated with window functions: for each row, there is a set of rows within its partition called its window frame. Some window functions act only on the rows of the window frame, rather than of the whole partition. Here is an example of using window frames in queries:

```
SELECT depname, empno, salary,
    avg(salary) OVER(ORDER BY salary ASC ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS avg,
    min(salary) OVER(ORDER BY empno ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_min
FROM empsalary
ORDER BY empno ASC;

+-----------+-------+--------+--------------------+---------+
| depname   | empno | salary | avg                | cum_min |
+-----------+-------+--------+--------------------+---------+
| sales     | 1     | 5000   | 5000.0             | 5000    |
| personnel | 2     | 3900   | 3866.6666666666665 | 3900    |
| sales     | 3     | 4800   | 4700.0             | 3900    |
| sales     | 4     | 4800   | 4866.666666666667  | 3900    |
| personnel | 5     | 3500   | 3700.0             | 3500    |
| develop   | 7     | 4200   | 4200.0             | 3500    |
| develop   | 8     | 6000   | 5600.0             | 3500    |
| develop   | 9     | 4500   | 4500.0             | 3500    |
| develop   | 10    | 5200   | 5133.333333333333  | 3500    |
| develop   | 11    | 5200   | 5466.666666666667  | 3500    |
+-----------+-------+--------+--------------------+---------+
```

When a query involves multiple window functions, it is possible to write out each one with a separate OVER clause, but this is duplicative and error-prone if the same windowing behavior is wanted for several functions. Instead, each windowing behavior can be named in a WINDOW clause and then referenced in OVER. For example:

```
SELECT sum(salary) OVER w, avg(salary) OVER w
FROM empsalary
WINDOW w AS (PARTITION BY depname ORDER BY salary DESC);
```

## Syntax[#](#syntax "Link to this heading")

The syntax for the OVER-clause is

```
function([expr])
  OVER(
    [PARTITION BY expr[, …]]
    [ORDER BY expr [ ASC | DESC ][, …]]
    [ frame_clause ]
    )
```

where **frame\_clause** is one of:

```
  { RANGE | ROWS | GROUPS } frame_start
  { RANGE | ROWS | GROUPS } BETWEEN frame_start AND frame_end
```

and **frame\_start** and **frame\_end** can be one of

```
UNBOUNDED PRECEDING
offset PRECEDING
CURRENT ROW
offset FOLLOWING
UNBOUNDED FOLLOWING
```

where **offset** is an non-negative integer.

RANGE and GROUPS modes require an ORDER BY clause (with RANGE the ORDER BY must specify exactly one column).

## Filter clause for aggregate window functions[#](#filter-clause-for-aggregate-window-functions "Link to this heading")

Aggregate window functions support the SQL `FILTER (WHERE ...)` clause to include only rows that satisfy the predicate from the window frame in the aggregation.

```
sum(salary) FILTER (WHERE salary > 0)
  OVER (PARTITION BY depname ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```

If no rows in the frame satisfy the filter for a given output row, `COUNT` yields `0` while `SUM`/`AVG`/`MIN`/`MAX` yield `NULL`.

## Aggregate functions[#](#aggregate-functions "Link to this heading")

All [aggregate functions](aggregate_functions.html) can be used as window functions.

## Ranking Functions[#](#ranking-functions "Link to this heading")

* [cume\_dist](#cume-dist)
* [dense\_rank](#dense-rank)
* [ntile](#ntile)
* [percent\_rank](#percent-rank)
* [rank](#rank)
* [row\_number](#row-number)

### `cume_dist`[#](#cume-dist "Link to this heading")

Relative rank of the current row: (number of rows preceding or peer with the current row) / (total rows).

```
cume_dist()
```

#### Example[#](#example "Link to this heading")

```
-- Example usage of the cume_dist window function:
SELECT salary,
    cume_dist() OVER (ORDER BY salary) AS cume_dist
FROM employees;

+--------+-----------+
| salary | cume_dist |
+--------+-----------+
| 30000  | 0.33      |
| 50000  | 0.67      |
| 70000  | 1.00      |
+--------+-----------+
```

### `dense_rank`[#](#dense-rank "Link to this heading")

Returns the rank of the current row without gaps. This function ranks rows in a dense manner, meaning consecutive ranks are assigned even for identical values.

```
dense_rank()
```

#### Example[#](#id1 "Link to this heading")

```
-- Example usage of the dense_rank window function:
SELECT department,
    salary,
    dense_rank() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank
FROM employees;

+-------------+--------+------------+
| department  | salary | dense_rank |
+-------------+--------+------------+
| Sales       | 70000  | 1          |
| Sales       | 50000  | 2          |
| Sales       | 50000  | 2          |
| Sales       | 30000  | 3          |
| Engineering | 90000  | 1          |
| Engineering | 80000  | 2          |
+-------------+--------+------------+
```

### `ntile`[#](#ntile "Link to this heading")

Integer ranging from 1 to the argument value, dividing the partition as equally as possible

```
ntile(expression)
```

#### Arguments[#](#arguments "Link to this heading")

* **expression**: An integer describing the number groups the partition should be split into

#### Example[#](#id2 "Link to this heading")

```
-- Example usage of the ntile window function:
SELECT employee_id,
    salary,
    ntile(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;

+-------------+--------+----------+
| employee_id | salary | quartile |
+-------------+--------+----------+
| 1           | 90000  | 1        |
| 2           | 85000  | 1        |
| 3           | 80000  | 2        |
| 4           | 70000  | 2        |
| 5           | 60000  | 3        |
| 6           | 50000  | 3        |
| 7           | 40000  | 4        |
| 8           | 30000  | 4        |
+-------------+--------+----------+
```

### `percent_rank`[#](#percent-rank "Link to this heading")

Returns the percentage rank of the current row within its partition. The value ranges from 0 to 1 and is computed as `(rank - 1) / (total_rows - 1)`.

```
percent_rank()
```

#### Example[#](#id3 "Link to this heading")

```
    -- Example usage of the percent_rank window function:
SELECT employee_id,
    salary,
    percent_rank() OVER (ORDER BY salary) AS percent_rank
FROM employees;

+-------------+--------+---------------+
| employee_id | salary | percent_rank  |
+-------------+--------+---------------+
| 1           | 30000  | 0.00          |
| 2           | 50000  | 0.50          |
| 3           | 70000  | 1.00          |
+-------------+--------+---------------+
```

### `rank`[#](#rank "Link to this heading")

Returns the rank of the current row within its partition, allowing gaps between ranks. This function provides a ranking similar to `row_number`, but skips ranks for identical values.

```
rank()
```

#### Example[#](#id4 "Link to this heading")

```
-- Example usage of the rank window function:
SELECT department,
    salary,
    rank() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;

+-------------+--------+------+
| department  | salary | rank |
+-------------+--------+------+
| Sales       | 70000  | 1    |
| Sales       | 50000  | 2    |
| Sales       | 50000  | 2    |
| Sales       | 30000  | 4    |
| Engineering | 90000  | 1    |
| Engineering | 80000  | 2    |
+-------------+--------+------+
```

### `row_number`[#](#row-number "Link to this heading")

Number of the current row within its partition, counting from 1.

```
row_number()
```

#### Example[#](#id5 "Link to this heading")

```
-- Example usage of the row_number window function:
SELECT department,
  salary,
  row_number() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM employees;

+-------------+--------+---------+
| department  | salary | row_num |
+-------------+--------+---------+
| Sales       | 70000  | 1       |
| Sales       | 50000  | 2       |
| Sales       | 50000  | 3       |
| Sales       | 30000  | 4       |
| Engineering | 90000  | 1       |
| Engineering | 80000  | 2       |
+-------------+--------+---------+
```

## Analytical Functions[#](#analytical-functions "Link to this heading")

* [first\_value](#first-value)
* [lag](#lag)
* [last\_value](#last-value)
* [lead](#lead)
* [nth\_value](#nth-value)

### `first_value`[#](#first-value "Link to this heading")

Returns value evaluated at the row that is the first row of the window frame.

```
first_value(expression)
```

#### Arguments[#](#id6 "Link to this heading")

* **expression**: Expression to operate on

#### Example[#](#id7 "Link to this heading")

```
-- Example usage of the first_value window function:
SELECT department,
  employee_id,
  salary,
  first_value(salary) OVER (PARTITION BY department ORDER BY salary DESC) AS top_salary
FROM employees;

+-------------+-------------+--------+------------+
| department  | employee_id | salary | top_salary |
+-------------+-------------+--------+------------+
| Sales       | 1           | 70000  | 70000      |
| Sales       | 2           | 50000  | 70000      |
| Sales       | 3           | 30000  | 70000      |
| Engineering | 4           | 90000  | 90000      |
| Engineering | 5           | 80000  | 90000      |
+-------------+-------------+--------+------------+
```

### `lag`[#](#lag "Link to this heading")

Returns value evaluated at the row that is offset rows before the current row within the partition; if there is no such row, instead return default (which must be of the same type as value).

```
lag(expression, offset, default)
```

#### Arguments[#](#id8 "Link to this heading")

* **expression**: Expression to operate on
* **offset**: Integer. Specifies how many rows back the value of expression should be retrieved. Defaults to 1.
* **default**: The default value if the offset is not within the partition. Must be of the same type as expression.

#### Example[#](#id9 "Link to this heading")

```
-- Example usage of the lag window function:
SELECT employee_id,
    salary,
    lag(salary, 1, 0) OVER (ORDER BY employee_id) AS prev_salary
FROM employees;

+-------------+--------+-------------+
| employee_id | salary | prev_salary |
+-------------+--------+-------------+
| 1           | 30000  | 0           |
| 2           | 50000  | 30000       |
| 3           | 70000  | 50000       |
| 4           | 60000  | 70000       |
+-------------+--------+-------------+
```

### `last_value`[#](#last-value "Link to this heading")

Returns value evaluated at the row that is the last row of the window frame.

```
last_value(expression)
```

#### Arguments[#](#id10 "Link to this heading")

* **expression**: Expression to operate on

#### Example[#](#id11 "Link to this heading")

```
-- SQL example of last_value:
SELECT department,
       employee_id,
       salary,
       last_value(salary) OVER (PARTITION BY department ORDER BY salary) AS running_last_salary
FROM employees;

+-------------+-------------+--------+---------------------+
| department  | employee_id | salary | running_last_salary |
+-------------+-------------+--------+---------------------+
| Sales       | 1           | 30000  | 30000               |
| Sales       | 2           | 50000  | 50000               |
| Sales       | 3           | 70000  | 70000               |
| Engineering | 4           | 40000  | 40000               |
| Engineering | 5           | 60000  | 60000               |
+-------------+-------------+--------+---------------------+
```

### `lead`[#](#lead "Link to this heading")

Returns value evaluated at the row that is offset rows after the current row within the partition; if there is no such row, instead return default (which must be of the same type as value).

```
lead(expression, offset, default)
```

#### Arguments[#](#id12 "Link to this heading")

* **expression**: Expression to operate on
* **offset**: Integer. Specifies how many rows forward the value of expression should be retrieved. Defaults to 1.
* **default**: The default value if the offset is not within the partition. Must be of the same type as expression.

#### Example[#](#id13 "Link to this heading")

```
-- Example usage of lead window function:
SELECT
    employee_id,
    department,
    salary,
    lead(salary, 1, 0) OVER (PARTITION BY department ORDER BY salary) AS next_salary
FROM employees;

+-------------+-------------+--------+--------------+
| employee_id | department  | salary | next_salary  |
+-------------+-------------+--------+--------------+
| 1           | Sales       | 30000  | 50000        |
| 2           | Sales       | 50000  | 70000        |
| 3           | Sales       | 70000  | 0            |
| 4           | Engineering | 40000  | 60000        |
| 5           | Engineering | 60000  | 0            |
+-------------+-------------+--------+--------------+
```

### `nth_value`[#](#nth-value "Link to this heading")

Returns the value evaluated at the nth row of the window frame (counting from 1). Returns NULL if no such row exists.

```
nth_value(expression, n)
```

#### Arguments[#](#id14 "Link to this heading")

* **expression**: The column from which to retrieve the nth value.
* **n**: Integer. Specifies the row number (starting from 1) in the window frame.

#### Example[#](#id15 "Link to this heading")

```
-- Sample employees table:
CREATE TABLE employees (id INT, salary INT);
INSERT INTO employees (id, salary) VALUES
(1, 30000),
(2, 40000),
(3, 50000),
(4, 60000),
(5, 70000);

-- Example usage of nth_value:
SELECT nth_value(salary, 2) OVER (
  ORDER BY salary
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS nth_value
FROM employees;

+-----------+
| nth_value |
+-----------+
| 40000     |
| 40000     |
| 40000     |
| 40000     |
| 40000     |
+-----------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/window_functions.md)

[Show Source](../../_sources/user-guide/sql/window_functions.md.txt)

---
# Reading Explain Plans[#](#reading-explain-plans "Link to this heading")

## Introduction[#](#introduction "Link to this heading")

This section describes of how to read a DataFusion query plan. While fully
comprehending all details of these plans requires significant expertise in the
DataFusion engine, this guide will help you get started with the basics.

Datafusion executes queries using a `query plan`. To see the plan without
running the query, add the keyword `EXPLAIN` to your SQL query or call the
[DataFrame::explain](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html#method.explain) method

## Example: Select and filter[#](#example-select-and-filter "Link to this heading")

In this section, we run example queries against the `hits.parquet` file. See
[below](#data-in-this-example)) for information on how to get this file.

Let’s see how DataFusion runs a query that selects the top 5 watch lists for the
site `http://domcheloveplanet.ru/`:

```
EXPLAIN FORMAT INDENT SELECT "WatchID" AS wid, "hits.parquet"."ClientIP" AS ip
FROM 'hits.parquet'
WHERE starts_with("URL", 'http://domcheloveplanet.ru/')
ORDER BY wid ASC, ip DESC
LIMIT 5;
```

The output will look like

```
+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| plan_type     | plan                                                                                                                                                                                                      |
+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| logical_plan  | Sort: wid ASC NULLS LAST, ip DESC NULLS FIRST, fetch=5                                                                                                                                                    |
|               |   Projection: hits.parquet.WatchID AS wid, hits.parquet.ClientIP AS ip                                                                                                                                    |
|               |     Filter: starts_with(hits.parquet.URL, Utf8("http://domcheloveplanet.ru/"))                                                                                                                            |
|               |       TableScan: hits.parquet projection=[WatchID, ClientIP, URL], partial_filters=[starts_with(hits.parquet.URL, Utf8("http://domcheloveplanet.ru/"))]                                                   |
| physical_plan | SortPreservingMergeExec: [wid@0 ASC NULLS LAST,ip@1 DESC], fetch=5                                                                                                                                        |
|               |   SortExec: TopK(fetch=5), expr=[wid@0 ASC NULLS LAST,ip@1 DESC], preserve_partitioning=[true]                                                                                                            |
|               |     ProjectionExec: expr=[WatchID@0 as wid, ClientIP@1 as ip]                                                                                                                                             |
|               |       CoalesceBatchesExec: target_batch_size=8192                                                                                                                                                         |
|               |         FilterExec: starts_with(URL@2, http://domcheloveplanet.ru/)                                                                                                                                       |
|               |           DataSourceExec: file_groups={16 groups: [[hits.parquet:0..923748528], ...]}, projection=[WatchID, ClientIP, URL], predicate=starts_with(URL@13, http://domcheloveplanet.ru/), file_type=parquet |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
2 row(s) fetched.
Elapsed 0.060 seconds.
```

There are two sections: logical plan and physical plan

* **Logical Plan:** is a plan generated for a specific SQL query, DataFrame, or other language without the
  knowledge of the underlying data organization.
* **Physical Plan:** is a plan generated from a logical plan along with consideration of the hardware
  configuration (e.g number of CPUs) and the underlying data organization (e.g number of files).
  This physical plan is specific to your hardware configuration and your data. If you load the same
  data to different hardware with different configurations, the same query may generate different query plans.

Understanding a query plan can help to you understand its performance. For example, when the plan shows your query reads
many files, it signals you to either add more filter in the query to read less data or to modify your file
design to make fewer but larger files. This document focuses on how to read a query plan. How to make a
query run faster depends on the reason it is slow and beyond the scope of this document.

## Query plans are trees[#](#query-plans-are-trees "Link to this heading")

A query plan is an upside down tree, and we always read from bottom up. The
physical plan in Figure 1 in tree format will look like

```
                         ▲
                         │
                         │
┌─────────────────────────────────────────────────┐
│             SortPreservingMergeExec             │
│        [wid@0 ASC NULLS LAST,ip@1 DESC]         │
│                     fetch=5                     │
└─────────────────────────────────────────────────┘
                         ▲
                         │
┌─────────────────────────────────────────────────┐
│             SortExec TopK(fetch=5),             │
│     expr=[wid@0 ASC NULLS LAST,ip@1 DESC],      │
│           preserve_partitioning=[true]          │
└─────────────────────────────────────────────────┘
                         ▲
                         │
┌─────────────────────────────────────────────────┐
│                 ProjectionExec                  │
│    expr=[WatchID@0 as wid, ClientIP@1 as ip]    │
└─────────────────────────────────────────────────┘
                         ▲
                         │
┌─────────────────────────────────────────────────┐
│               CoalesceBatchesExec               │
└─────────────────────────────────────────────────┘
                         ▲
                         │
┌─────────────────────────────────────────────────┐
│                   FilterExec                    │
│ starts_with(URL@2, http://domcheloveplanet.ru/) │
└─────────────────────────────────────────────────┘
                         ▲
                         │
┌────────────────────────────────────────────────┐
│                  DataSourceExec                │
│          hits.parquet (filter = ...)           │
└────────────────────────────────────────────────┘
```

Each node in the tree/plan ends with `Exec` and is sometimes also called an `operator` or `ExecutionPlan` where data is
processed, transformed and sent up.

1. First, data in parquet the `hits.parquet` file us read in parallel using 16 cores in 16 “partitions” (more on this later) from `DataSourceExec`, which applies a first pass at filtering during the scan.
2. Next, the output is filtered using `FilterExec` to ensure only rows where `starts_with(URL, 'http://domcheloveplanet.ru/')` evaluates to true are passed on
3. The `CoalesceBatchesExec` then ensures that the data is grouped into larger batches for processing
4. The `ProjectionExec` then projects the data to rename the `WatchID` and `ClientIP` columns to `wid` and `ip` respectively.
5. The `SortExec` then sorts the data by `wid ASC, ip DESC`. The `Topk(fetch=5)` indicates that a special implementation is used that only tracks and emits the top 5 values in each partition.
6. Finally the `SortPreservingMergeExec` merges the sorted data from all partitions and returns the top 5 rows overall.

## Understanding large query plans[#](#understanding-large-query-plans "Link to this heading")

A large query plan may look intimidating, but you can quickly understand what it does by following these steps

1. As always, read from bottom up, one operator at a time.
2. Understand the job of this operator by reading
   the [Physical Plan documentation](https://docs.rs/datafusion/latest/datafusion/physical_plan/index.html).
3. Understand the input data of the operator and how large/small it may be.
4. Understand how much data that operator produces and what it would look like.

If you can answer those questions, you will be able to estimate how much work
that plan has to do and thus how long it will take. However, the `EXPLAIN` just
shows you the plan without executing it.

If you want to know more about how much work each operator in query plan does,
you can use the `EXPLAIN ANALYZE` to get the explain with runtime added (see
next section)

## More Debugging Information: `EXPLAIN VERBOSE`[#](#more-debugging-information-explain-verbose "Link to this heading")

If the plan has to read too many files, not all of them will be shown in the
`EXPLAIN`. To see them, use `EXPLAIN VEBOSE`. Like `EXPLAIN`, `EXPLAIN VERBOSE`
does not run the query. Instead it shows the full explain plan, with information
that is omitted from the default explain, as well as all intermediate physical
plans DataFusion generates before returning. This mode can be very helpful for
debugging to see why and when DataFusion added and removed operators from a plan.

## Execution Counters: `EXPLAIN ANALYZE`[#](#execution-counters-explain-analyze "Link to this heading")

During execution, DataFusion operators collect detailed metrics. You can access
them programmatically via [`ExecutionPlan::metrics`](https://docs.rs/datafusion/latest/datafusion/physical_plan/trait.ExecutionPlan.html#method.metrics) as well as with the
`EXPLAIN ANALYZE` command. For example here is the same query query as
above but with `EXPLAIN ANALYZE` (note the output is edited for clarity)

```
> EXPLAIN ANALYZE SELECT "WatchID" AS wid, "hits.parquet"."ClientIP" AS ip
FROM 'hits.parquet'
WHERE starts_with("URL", 'http://domcheloveplanet.ru/')
ORDER BY wid ASC, ip DESC
LIMIT 5;
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| plan_type         | plan                                                                                                                                                                                                                                                                                                                                                           |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Plan with Metrics | SortPreservingMergeExec: [wid@0 ASC NULLS LAST,ip@1 DESC], fetch=5, metrics=[output_rows=5, elapsed_compute=2.375µs]                                                                                                                                                                                                                                           |
|                   |   SortExec: TopK(fetch=5), expr=[wid@0 ASC NULLS LAST,ip@1 DESC], preserve_partitioning=[true], metrics=[output_rows=75, elapsed_compute=7.243038ms, row_replacements=482]                                                                                                                                                                                     |
|                   |     ProjectionExec: expr=[WatchID@0 as wid, ClientIP@1 as ip], metrics=[output_rows=811821, elapsed_compute=66.25µs]                                                                                                                                                                                                                                           |
|                   |         FilterExec: starts_with(URL@2, http://domcheloveplanet.ru/), metrics=[output_rows=811821, elapsed_compute=1.36923816s]                                                                                                                                                                                                                                 |
|                   |           DataSourceExec: file_groups={16 groups: [[hits.parquet:0..923748528], ...]}, projection=[WatchID, ClientIP, URL], predicate=starts_with(URL@13, http://domcheloveplanet.ru/), metrics=[output_rows=99997497, elapsed_compute=16ns, ... bytes_scanned=3703192723, ...  time_elapsed_opening=308.203002ms, time_elapsed_scanning_total=8.350342183s, ...] |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row(s) fetched.
Elapsed 0.720 seconds.
```

In this case, DataFusion actually ran the query, but discarded any results, and
instead returned an annotated plan with a new field, `metrics=[...]`

Most operators have the common metrics `output_rows` and `elapsed_compute` and
some have operator specific metrics such as `DataSourceExec` with `ParquetSource` which has
`bytes_scanned=3703192723`. Note that times and counters are reported across all
cores, so if you have 16 cores, the time reported is the sum of the time taken
by all 16 cores.

Again, reading from bottom up:

* `DataSourceExec`

  * `output_rows=99997497`: A total 99.9M rows were produced
  * `bytes_scanned=3703192723`: Of the 14GB file, 3.7GB were actually read (due to projection pushdown)
  * `time_elapsed_opening=308.203002ms`: It took 300ms to open the file and prepare to read it
  * `time_elapsed_scanning_total=8.350342183s`: It took 8.3 seconds of CPU time (across 16 cores) to actually decode the parquet data
* `FilterExec`

  * `output_rows=811821`: Of the 99.9M rows at its input, only 811K rows passed the filter and were produced at the output
  * `elapsed_compute=1.36923816s`: In total, 1.36s of CPU time (across 16 cores) was spend evaluating the filter
* `CoalesceBatchesExec`

  * `output_rows=811821`, `elapsed_compute=12.873379ms`: Produced 811K rows in 13ms
* `ProjectionExec`

  * `output_rows=811821, elapsed_compute=66.25µs`: Produced 811K rows in 66µs (microseconds). This projection is almost instantaneous as it does not manipulate any data
* `SortExec`

  * `output_rows=75`: Produced 75 rows in total. Each of 16 cores could produce up to 5 rows, but in this case not all cores did.
  * `elapsed_compute=7.243038ms`: 7ms was used to determine the top 5 rows
  * `row_replacements=482`: Internally, the TopK operator updated its top list 482 times
* `SortPreservingMergeExec`

  * `output_rows=5`, `elapsed_compute=2.375µs`: Produced the final 5 rows in 2.375µs (microseconds)

When predicate pushdown is enabled, `DataSourceExec` with `ParquetSource` gains the following metrics:

* `output_rows_skew`: output skew score derived from per-partition `output_rows`. `0%` is perfectly balanced, `100%` is maximally skewed, and `N/A` means no output rows were produced.
* `page_index_rows_pruned`: number of rows evaluated by page index filters. The metric reports both how many rows were considered in total and how many matched (were not pruned).
* `page_index_pages_pruned`: number of pages evaluated by page index filters. The metric reports both how many pages were considered in total and how many matched (were not pruned).
* `row_groups_pruned_bloom_filter`: number of row groups evaluated by Bloom Filters, reporting both total checked groups and groups that matched.
* `row_groups_pruned_statistics`: number of row groups evaluated by row-group statistics (min/max), reporting both total checked groups and groups that matched.
* `limit_pruned_row_groups`: number of row groups pruned by the limit.
* `pushdown_rows_matched`: rows that were tested by any of the above filters, and passed all of them.
* `pushdown_rows_pruned`: rows that were tested by any of the above filters, and did not pass at least one of them.
* `predicate_evaluation_errors`: number of times evaluating the filter expression failed (expected to be zero in normal operation)
* `num_predicate_creation_errors`: number of errors creating predicates (expected to be zero in normal operation)
* `bloom_filter_eval_time`: time spent parsing and evaluating Bloom Filters
* `statistics_eval_time`: time spent parsing and evaluating row group-level statistics
* `row_pushdown_eval_time`: time spent evaluating row-level filters
* `page_index_eval_time`: time required to evaluate the page index filters

## Partitions and Execution[#](#partitions-and-execution "Link to this heading")

DataFusion determines the optimal number of cores to use as part of query
planning. Roughly speaking, each “partition” in the plan is run independently using
a separate core. Data crosses between cores only within certain operators such as
`RepartitionExec`, `CoalescePartitions` and `SortPreservingMergeExec`

You can read more about this in the [Partitioning Docs](https://docs.rs/datafusion/latest/datafusion/physical_expr/enum.Partitioning.html).

## Example of an Aggregate Query[#](#example-of-an-aggregate-query "Link to this heading")

Let us delve into an example query that aggregates data from the `hits.parquet`
file. For example, this query from ClickBench finds the top 10 users by their
number of hits:

```
SELECT "UserID", COUNT(*)
FROM 'hits.parquet'
GROUP BY "UserID"
ORDER BY COUNT(*) DESC
LIMIT 10;
```

We can again see the query plan by using `EXPLAIN`:

```
> EXPLAIN FORMAT INDENT SELECT "UserID", COUNT(*) FROM 'hits.parquet' GROUP BY "UserID" ORDER BY COUNT(*) DESC LIMIT 10;
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| plan_type     | plan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| logical_plan  | Limit: skip=0, fetch=10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|               |   Sort: count(*) DESC NULLS FIRST, fetch=10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|               |     Aggregate: groupBy=[[hits.parquet.UserID]], aggr=[[count(Int64(1)) AS count(*)]]                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|               |       TableScan: hits.parquet projection=[UserID]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| physical_plan | GlobalLimitExec: skip=0, fetch=10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|               |   SortPreservingMergeExec: [count(*)@1 DESC], fetch=10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|               |     SortExec: TopK(fetch=10), expr=[count(*)@1 DESC], preserve_partitioning=[true]                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|               |       AggregateExec: mode=FinalPartitioned, gby=[UserID@0 as UserID], aggr=[count(*)]                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|               |         CoalesceBatchesExec: target_batch_size=8192                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|               |           RepartitionExec: partitioning=Hash([UserID@0], 10), input_partitions=10                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|               |             AggregateExec: mode=Partial, gby=[UserID@0 as UserID], aggr=[count(*)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|               |               DataSourceExec: file_groups={10 groups: [[hits.parquet:0..1477997645], [hits.parquet:1477997645..2955995290], [hits.parquet:2955995290..4433992935], [hits.parquet:4433992935..5911990580], [hits.parquet:5911990580..7389988225], ...]}, projection=[UserID], file_type=parquet                                                                                                                                                                                                                                                    |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

For this query, let’s again read the plan from the bottom to the top:

**Logical plan operators**

* `TableScan`

  * `hits.parquet`: Scans data from the file `hits.parquet`.
  * `projection=[UserID]`: Reads only the `UserID` column
* `Aggregate`

  * `groupBy=[[hits.parquet.UserID]]`: Groups by `UserID` column.
  * `aggr=[[count(Int64(1)) AS count(*)]]`: Applies the `COUNT` aggregate on each distinct group.
* `Sort`

  * `count(*) DESC NULLS FIRST`: Sorts the data in descending count order.
  * `fetch=10`: Returns only the first 10 rows.
* `Limit`

  * `skip=0`: Does not skip any data for the results.
  * `fetch=10`: Limits the results to 10 values.

**Physical plan operators**

* `DataSourceExec`

  * `file_groups={10 groups: [...]}`: Reads 10 groups in parallel from `hits.parquet`file. (The example above was run on a machine with 10 cores.)
  * `projection=[UserID]`: Pushes down projection of the `UserID` column. The parquet format is columnar and the DataFusion reader only decodes the columns required.
* `AggregateExec`

  * `mode=Partial` Runs a [partial aggregation](https://docs.rs/datafusion/latest/datafusion/physical_plan/aggregates/enum.AggregateMode.html#variant.Partial) in parallel across each of the 10 partitions from the `DataSourceExec` immediately after reading.
  * `gby=[UserID@0 as UserID]`: Represents `GROUP BY` in the [physical plan](https://docs.rs/datafusion/latest/datafusion/physical_plan/aggregates/struct.PhysicalGroupBy.html) and groups together the same values of `UserID`.
  * `aggr=[count(*)]`: Applies the `COUNT` aggregate on all rows for each group.
* `RepartitionExec`

  * `partitioning=Hash([UserID@0], 10)`: Divides the input into into 10 (new) output partitions based on the value of `hash(UserID)`. You can read more about this in the [partitioning](https://docs.rs/datafusion/latest/datafusion/physical_plan/repartition/struct.RepartitionExec.html) documentation.
  * `input_partitions=10`: Number of input partitions.
* `CoalesceBatchesExec`

  * `target_batch_size=8192`: Combines smaller batches in to larger batches. In this case approximately 8192 rows in each batch.
* `AggregateExec`

  * `mode=FinalPartitioned`: Performs the final aggregation on each group. See the [documentation on multi phase grouping](https://docs.rs/datafusion/latest/datafusion/physical_plan/trait.Accumulator.html#tymethod.state) for more information.
  * `gby=[UserID@0 as UserID]`: Groups by `UserID`.
  * `aggr=[count(*)]`: Applies the `COUNT` aggregate on all rows for each group.
* `SortExec`

  * `TopK(fetch=10)`: Use a special “TopK” sort that keeps only the largest 10 values in memory at a time. You can read more about this in the [TopK](https://docs.rs/datafusion/latest/datafusion/physical_plan/struct.TopK.html) documentation.
  * `expr=[count(*)@1 DESC]`: Sorts all rows in descending order. Note this represents the `ORDER BY` in the physical plan.
  * `preserve_partitioning=[true]`: The sort is done in parallel on each partition. In this case the top 10 values are found for each of the 10 partitions, in parallel.
* `SortPreservingMergeExec`

  * `[count(*)@1 DESC]`: This operator merges the 10 distinct streams into a single stream using this expression.
  * `fetch=10`: Returns only the first 10 rows
* `GlobalLimitExec`

  * `skip=0`: Does not skip any rows
  * `fetch=10`: Returns only the first 10 rows, denoted by `LIMIT 10` in the query.

### Data in this Example[#](#data-in-this-example "Link to this heading")

The examples in this section use data from [ClickBench](https://benchmark.clickhouse.com/), a benchmark for data
analytics. The examples are in terms of the 14GB [`hits.parquet`](https://datasets.clickhouse.com/hits_compatible/hits.parquet) file and can be
downloaded from the website or using the following commands:

```
cd benchmarks
./bench.sh data clickbench_1
***************************
DataFusion Benchmark Runner and Data Generator
COMMAND: data
BENCHMARK: clickbench_1
DATA_DIR: /Users/andrewlamb/Software/datafusion2/benchmarks/data
CARGO_COMMAND: cargo run --release
PREFER_HASH_JOIN: true
***************************
Checking hits.parquet...... found 14779976446 bytes ... Done
```

Then you can run `datafusion-cli` to get plans:

```
cd datafusion/benchmarks/data
datafusion-cli

DataFusion CLI v41.0.0
> select count(*) from 'hits.parquet';
+----------+
| count(*) |
+----------+
| 99997497 |
+----------+
1 row(s) fetched.
Elapsed 0.062 seconds.
>
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/explain-usage.md)

[Show Source](../_sources/user-guide/explain-usage.md.txt)

---
# Frequently Asked Questions[#](#frequently-asked-questions "Link to this heading")

## What is the relationship between Apache Arrow, DataFusion, and Ballista?[#](#what-is-the-relationship-between-apache-arrow-datafusion-and-ballista "Link to this heading")

Apache Arrow is a library which provides a standardized memory representation for columnar data. It also provides
“kernels” for performing common operations on this data.

DataFusion is a library for executing queries in-process using the Apache Arrow memory
model and computational kernels. It is designed to run within a single process, using threads
for parallel query execution.

[Ballista](https://github.com/apache/datafusion-ballista) is a distributed compute platform built on DataFusion.

# How does DataFusion Compare with `XYZ`?[#](#how-does-datafusion-compare-with-xyz "Link to this heading")

When compared to similar systems, DataFusion typically is:

1. Targeted at developers, rather than end users / data scientists.
2. Designed to be embedded, rather than a complete file based SQL system.
3. Governed by the [Apache Software Foundation](https://www.apache.org/) process, rather than a single company or individual.
4. Implemented in `Rust`, rather than `C/C++`

Here is a comparison with similar projects that may help understand
when DataFusion might be suitable or unsuitable for your needs:

* [DuckDB](https://www.duckdb.org) is an open source, in process analytic database.
  Like DataFusion, it supports very fast execution, both from its custom file format
  and directly from parquet files. Unlike DataFusion, it is written in C/C++ and it
  is primarily used directly by users as a serverless database and query system rather
  than as a library for building such database systems.
* [Polars](http://pola.rs): Polars is one of the fastest DataFrame
  libraries at the time of writing. Like DataFusion, it is also
  written in Rust and uses the Apache Arrow memory model, but unlike
  DataFusion it is not designed with as many extension points.
* [Facebook Velox](https://github.com/facebookincubator/velox)
  is an execution engine. Like DataFusion, Velox aims to
  provide a reusable foundation for building database-like systems. Unlike DataFusion,
  it is written in C/C++ and does not include a SQL frontend or planning / optimization
  framework.
* [Databend](https://github.com/datafuselabs/databend) is a complete
  database system. Like DataFusion it is also written in Rust and
  utilizes the Apache Arrow memory model, but unlike DataFusion it
  targets end-users rather than developers of other database systems.

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/faq.md)

[Show Source](../_sources/user-guide/faq.md.txt)

---
# SELECT syntax[#](#select-syntax "Link to this heading")

The queries in DataFusion scan data from tables and return 0 or more rows.
Please be aware that column names in queries are made lower-case, but not on the inferred schema. Accordingly, if you
want to query against a capitalized field, make sure to use double quotes. Please see this
[example](https://datafusion.apache.org/user-guide/example-usage.html) for clarification.
In this documentation we describe the SQL syntax in DataFusion.

DataFusion supports the following syntax for queries:

[ [WITH](#with-clause) with\_query [, …] ]   
[SELECT](#select-clause) [ ALL | DISTINCT ] select\_expr [, …]   
[ [FROM](#from-clause) from\_item [, …] ]   
[ [JOIN](#join-clause) join\_item [, …] ]   
[ [WHERE](#where-clause) condition ]   
[ [GROUP BY](#group-by-clause) grouping\_element [, …] ]   
[ [HAVING](#having-clause) condition]   
[ [QUALIFY](#qualify-clause) condition]   
[ [UNION](#union-clause) [ ALL | select ]   
[ [ORDER BY](#order-by-clause) expression [ ASC | DESC ][, …] ]   
[ [LIMIT](#limit-clause) count ]   
[ [EXCLUDE | EXCEPT](#exclude-and-except-clause) ]   
[Pipe operators](#pipe-operators)

## WITH clause[#](#with-clause "Link to this heading")

A with clause allows to give names for queries and reference them by name.

```
WITH x AS (SELECT a, MAX(b) AS b FROM t GROUP BY a)
SELECT a, b FROM x;
```

## SELECT clause[#](#select-clause "Link to this heading")

Example:

```
SELECT a, b, a + b FROM table
```

The `DISTINCT` quantifier can be added to make the query return all distinct rows.
By default `ALL` will be used, which returns all the rows.

```
SELECT DISTINCT person, age FROM employees
```

## FROM clause[#](#from-clause "Link to this heading")

Example:

```
SELECT t.a FROM table AS t
```

## WHERE clause[#](#where-clause "Link to this heading")

Example:

```
SELECT a FROM table WHERE a > 10
```

## JOIN clause[#](#join-clause "Link to this heading")

DataFusion supports `INNER JOIN`, `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`, `FULL OUTER JOIN`, `NATURAL JOIN`, `CROSS JOIN`, `LEFT SEMI JOIN`, `RIGHT SEMI JOIN`, `LEFT ANTI JOIN`, `RIGHT ANTI JOIN`, and `LATERAL JOIN`.

The following examples are based on this table:

```
select * from x;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
```

### INNER JOIN[#](#inner-join "Link to this heading")

The keywords `JOIN` or `INNER JOIN` define a join that only shows rows where there is a match in both tables.

```
SELECT * FROM x INNER JOIN x y ON x.column_1 = y.column_1;
+----------+----------+----------+----------+
| column_1 | column_2 | column_1 | column_2 |
+----------+----------+----------+----------+
| 1        | 2        | 1        | 2        |
+----------+----------+----------+----------+
```

### LEFT OUTER JOIN[#](#left-outer-join "Link to this heading")

The keywords `LEFT JOIN` or `LEFT OUTER JOIN` define a join that includes all rows from the left table even if there
is not a match in the right table. When there is no match, null values are produced for the right side of the join.

```
SELECT * FROM x LEFT JOIN x y ON x.column_1 = y.column_2;
+----------+----------+----------+----------+
| column_1 | column_2 | column_1 | column_2 |
+----------+----------+----------+----------+
| 1        | 2        |          |          |
+----------+----------+----------+----------+
```

### RIGHT OUTER JOIN[#](#right-outer-join "Link to this heading")

The keywords `RIGHT JOIN` or `RIGHT OUTER JOIN` define a join that includes all rows from the right table even if there
is not a match in the left table. When there is no match, null values are produced for the left side of the join.

```
SELECT * FROM x RIGHT JOIN x y ON x.column_1 = y.column_2;
+----------+----------+----------+----------+
| column_1 | column_2 | column_1 | column_2 |
+----------+----------+----------+----------+
|          |          | 1        | 2        |
+----------+----------+----------+----------+
```

### FULL OUTER JOIN[#](#full-outer-join "Link to this heading")

The keywords `FULL JOIN` or `FULL OUTER JOIN` define a join that is effectively a union of a `LEFT OUTER JOIN` and
`RIGHT OUTER JOIN`. It will show all rows from the left and right side of the join and will produce null values on
either side of the join where there is not a match.

```
SELECT * FROM x FULL OUTER JOIN x y ON x.column_1 = y.column_2;
+----------+----------+----------+----------+
| column_1 | column_2 | column_1 | column_2 |
+----------+----------+----------+----------+
| 1        | 2        |          |          |
|          |          | 1        | 2        |
+----------+----------+----------+----------+
```

### NATURAL JOIN[#](#natural-join "Link to this heading")

A `NATURAL JOIN` defines an inner join based on common column names found between the input tables. When no common
column names are found, it behaves like a `CROSS JOIN`.

```
SELECT * FROM x NATURAL JOIN x y;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
```

### CROSS JOIN[#](#cross-join "Link to this heading")

A `CROSS JOIN` produces a cartesian product that matches every row in the left side of the join with every row in the
right side of the join.

```
SELECT * FROM x CROSS JOIN x y;
+----------+----------+----------+----------+
| column_1 | column_2 | column_1 | column_2 |
+----------+----------+----------+----------+
| 1        | 2        | 1        | 2        |
+----------+----------+----------+----------+
```

### LEFT SEMI JOIN[#](#left-semi-join "Link to this heading")

The `LEFT SEMI JOIN` returns all rows from the left table that have at least one matching row in the right table, and
projects only the columns from the left table.

```
SELECT * FROM x LEFT SEMI JOIN x y ON x.column_1 = y.column_1;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
```

### RIGHT SEMI JOIN[#](#right-semi-join "Link to this heading")

The `RIGHT SEMI JOIN` returns all rows from the right table that have at least one matching row in the left table, and
only projects the columns from the right table.

```
SELECT * FROM x RIGHT SEMI JOIN x y ON x.column_1 = y.column_1;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
```

### LEFT ANTI JOIN[#](#left-anti-join "Link to this heading")

The `LEFT ANTI JOIN` returns all rows from the left table that do not have any matching row in the right table, projecting
only the left table’s columns.

```
SELECT * FROM x LEFT ANTI JOIN x y ON x.column_1 = y.column_1;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
+----------+----------+
```

### RIGHT ANTI JOIN[#](#right-anti-join "Link to this heading")

The `RIGHT ANTI JOIN` returns all rows from the right table that do not have any matching row in the left table, projecting
only the right table’s columns.

```
SELECT * FROM x RIGHT ANTI JOIN x y ON x.column_1 = y.column_1;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
+----------+----------+
```

### LATERAL JOIN[#](#lateral-join "Link to this heading")

A `LATERAL JOIN` allows the right-hand side of a join to reference columns from
the left-hand side. Conceptually, the subquery on the right is evaluated once
for each row of the left-hand table, which makes it possible to “parameterize” a
subquery with values from preceding tables.

The `LATERAL` keyword is required; DataFusion does not implicitly detect
correlation in `FROM` clause subqueries.

The following examples use these tables:

```
CREATE TABLE departments(id INT, name TEXT) AS VALUES (1, 'HR'), (2, 'Eng'), (3, 'Sales');
CREATE TABLE employees(id INT, dept_id INT, name TEXT) AS VALUES
  (10, 1, 'Alice'), (20, 1, 'Bob'), (30, 2, 'Carol');
```

#### Comma syntax[#](#comma-syntax "Link to this heading")

The most concise form places `LATERAL` after a comma in the `FROM` clause.
Rows from the left table that have no matching rows in the subquery are excluded
(inner join semantics).

```
SELECT d.name AS dept, e.name AS emp
FROM departments d, LATERAL (
    SELECT employees.name FROM employees WHERE employees.dept_id = d.id
) AS e
ORDER BY dept, emp;
+------+-------+
| dept | emp   |
+------+-------+
| Eng  | Carol |
| HR   | Alice |
| HR   | Bob   |
+------+-------+
```

#### CROSS JOIN LATERAL[#](#cross-join-lateral "Link to this heading")

Equivalent to the comma syntax above.

```
SELECT d.name AS dept, e.name AS emp
FROM departments d
CROSS JOIN LATERAL (
    SELECT employees.name FROM employees WHERE employees.dept_id = d.id
) AS e
ORDER BY dept, emp;
+------+-------+
| dept | emp   |
+------+-------+
| Eng  | Carol |
| HR   | Alice |
| HR   | Bob   |
+------+-------+
```

#### JOIN LATERAL … ON[#](#join-lateral-on "Link to this heading")

`JOIN LATERAL` with an `ON` clause applies the `ON` condition as an additional
filter after the lateral subquery is evaluated.

```
SELECT d.name AS dept, sub.emp, sub.cnt
FROM departments d
JOIN LATERAL (
    SELECT count(*) AS cnt, min(employees.name) AS emp
    FROM employees WHERE employees.dept_id = d.id
) AS sub ON sub.cnt > 0
ORDER BY dept;
+------+-------+-----+
| dept | emp   | cnt |
+------+-------+-----+
| Eng  | Carol | 1   |
| HR   | Alice | 2   |
+------+-------+-----+
```

#### Limitations[#](#limitations "Link to this heading")

The following patterns are not yet supported:

* `LEFT JOIN LATERAL` (lateral join with outer join semantics).
* Outer references in the `SELECT` list of the lateral subquery (e.g., `LATERAL (SELECT outer.col + 1)`).
* `HAVING` in lateral subqueries.

## GROUP BY clause[#](#group-by-clause "Link to this heading")

Example:

```
SELECT a, b, MAX(c) FROM table GROUP BY a, b
```

Some aggregation functions accept optional ordering requirement, such as `ARRAY_AGG`. If a requirement is given,
aggregation is calculated in the order of the requirement.

Example:

```
SELECT a, b, ARRAY_AGG(c, ORDER BY d) FROM table GROUP BY a, b
```

## HAVING clause[#](#having-clause "Link to this heading")

Example:

```
SELECT a, b, MAX(c) FROM table GROUP BY a, b HAVING MAX(c) > 10
```

## QUALIFY clause[#](#qualify-clause "Link to this heading")

Example:

```
SELECT ROW_NUMBER() OVER (PARTITION BY region) AS rk FROM table QUALIFY rk > 1;
```

## UNION clause[#](#union-clause "Link to this heading")

Example:

```
SELECT
    a,
    b,
    c
FROM table1
UNION ALL
SELECT
    a,
    b,
    c
FROM table2
```

## ORDER BY clause[#](#order-by-clause "Link to this heading")

Orders the results by the referenced expression. By default it uses ascending order (`ASC`).
This order can be changed to descending by adding `DESC` after the order-by expressions.

Examples:

```
SELECT age, person FROM table ORDER BY age;
SELECT age, person FROM table ORDER BY age DESC;
SELECT age, person FROM table ORDER BY age, person DESC;
```

## LIMIT clause[#](#limit-clause "Link to this heading")

Limits the number of rows to be a maximum of `count` rows. `count` should be a non-negative integer.

Example:

```
SELECT age, person FROM table
LIMIT 10
```

## EXCLUDE and EXCEPT clause[#](#exclude-and-except-clause "Link to this heading")

Excluded named columns from query results.

Example selecting all columns except for `age` and `person`:

```
SELECT * EXCEPT(age, person)
FROM table;
```

```
SELECT * EXCLUDE(age, person)
FROM table;
```

## Pipe operators[#](#pipe-operators "Link to this heading")

Some SQL dialects (e.g. BigQuery) support the pipe operator `|>`.
The SQL dialect can be set like this:

```
set datafusion.sql_parser.dialect = 'BigQuery';
```

DataFusion currently supports the following pipe operators:

* [WHERE](#pipe-where)
* [ORDER BY](#pipe-order-by)
* [LIMIT](#pipe-limit)
* [SELECT](#pipe-select)
* [EXTEND](#pipe-extend)
* [AS](#pipe-as)
* [UNION](#pipe-union)
* [INTERSECT](#pipe-intersect)
* [EXCEPT](#pipe-except)
* [AGGREGATE](#pipe-aggregate)
* [JOIN](#pipe-join)

### WHERE[#](#where "Link to this heading")

```
select * from range(0,10)
|> where value < 2;
+-------+
| value |
+-------+
| 0     |
| 1     |
+-------+
```

### ORDER BY[#](#order-by "Link to this heading")

```
select * from range(0,3)
|> order by value desc;
+-------+
| value |
+-------+
| 2     |
| 1     |
| 0     |
+-------+
```

### LIMIT[#](#limit "Link to this heading")

```
select * from range(0,3)
|> order by value desc
|> limit 1;
+-------+
| value |
+-------+
| 2     |
+-------+
```

### SELECT[#](#select "Link to this heading")

```
select * from range(0,3)
|> select value + 10;
+---------------------------+
| range().value + Int64(10) |
+---------------------------+
| 10                        |
| 11                        |
| 12                        |
+---------------------------+
```

### EXTEND[#](#extend "Link to this heading")

```
select * from range(0,3)
|> extend -value AS minus_value;
+-------+-------------+
| value | minus_value |
+-------+-------------+
| 0     | 0           |
| 1     | -1          |
| 2     | -2          |
+-------+-------------+
```

### AS[#](#as "Link to this heading")

```
select * from range(0,3)
|> as my_range
|> SELECT my_range.value;
+-------+
| value |
+-------+
| 0     |
| 1     |
| 2     |
+-------+
```

### UNION[#](#union "Link to this heading")

```
select * from range(0,3)
|> union all (
  select * from range(3,6)
);
+-------+
| value |
+-------+
| 0     |
| 1     |
| 2     |
| 3     |
| 4     |
| 5     |
+-------+
```

### INTERSECT[#](#intersect "Link to this heading")

```
select * from range(0,100)
|> INTERSECT DISTINCT (
  select 3
);
+-------+
| value |
+-------+
| 3     |
+-------+
```

### EXCEPT[#](#except "Link to this heading")

```
select * from range(0,10)
|> EXCEPT DISTINCT (select * from range(5,10));
+-------+
| value |
+-------+
| 0     |
| 1     |
| 2     |
| 3     |
| 4     |
+-------+
```

### AGGREGATE[#](#aggregate "Link to this heading")

```
select * from range(0,3)
|> aggregate sum(value) AS total;
+-------+
| total |
+-------+
| 3     |
+-------+
```

### JOIN[#](#join "Link to this heading")

```
(
  SELECT 'apples' AS item, 2 AS sales
  UNION ALL
  SELECT 'bananas' AS item, 5 AS sales
)
|> AS produce_sales
|> LEFT JOIN
     (
       SELECT 'apples' AS item, 123 AS id
     ) AS produce_data
   ON produce_sales.item = produce_data.item
|> SELECT produce_sales.item, sales, id;
+--------+-------+------+
| item   | sales | id   |
+--------+-------+------+
| apples | 2     | 123  |
| bananas| 5     | NULL |
+--------+-------+------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/select.md)

[Show Source](../../_sources/user-guide/sql/select.md.txt)

---
# DML[#](#dml "Link to this heading")

DML stands for “Data Manipulation Language” and relates to inserting
and modifying data in tables.

## COPY[#](#copy "Link to this heading")

Copies the contents of a table or query to file(s). Supported file
formats are `parquet`, `csv`, `json`, and `arrow`.

```
COPY { table_name | query }
TO 'file_name'
[ STORED AS format ]
[ PARTITIONED BY column_name [, ...] ]
[ OPTIONS( option [, ... ] ) ]
```

`STORED AS` specifies the file format the `COPY` command will write. If this
clause is not specified, it will be inferred from the file extension if possible.

`PARTITIONED BY` specifies the columns to use for partitioning the output files into
separate hive-style directories. By default, columns used in `PARTITIONED BY` will be removed
from the output format. If you want to keep the columns, you should provide the option
`execution.keep_partition_by_columns true`. `execution.keep_partition_by_columns` flag can also
be enabled through `ExecutionOptions` within `SessionConfig`.

The output format is determined by the first match of the following rules:

1. Value of `STORED AS`
2. Filename extension (e.g. `foo.parquet` implies `PARQUET` format)

For a detailed list of valid OPTIONS, see [Format Options](format_options.html).

### Examples[#](#examples "Link to this heading")

Copy the contents of `source_table` to `file_name.json` in JSON format:

```
> COPY source_table TO 'file_name.json';
+-------+
| count |
+-------+
| 2     |
+-------+
```

Copy the contents of `source_table` to one or more Parquet formatted
files in the `dir_name` directory:

```
> COPY source_table TO 'dir_name' STORED AS PARQUET;
+-------+
| count |
+-------+
| 2     |
+-------+
```

Copy the contents of `source_table` to multiple directories
of hive-style partitioned parquet files:

```
> COPY source_table TO 'dir_name' STORED AS parquet, PARTITIONED BY (column1, column2);
+-------+
| count |
+-------+
| 2     |
+-------+
```

If the data contains values of `x` and `y` in column1 and only `a` in
column2, output files will appear in the following directory structure:

```
dir_name/
  column1=x/
    column2=a/
      <file>.parquet
      <file>.parquet
      ...
  column1=y/
    column2=a/
      <file>.parquet
      <file>.parquet
      ...
```

Run the query `SELECT * from source ORDER BY time` and write the
results (maintaining the order) to a parquet file named
`output.parquet` with a maximum parquet row group size of 10MB:

```
> COPY (SELECT * from source ORDER BY time) TO 'output.parquet' OPTIONS (MAX_ROW_GROUP_SIZE 10000000);
+-------+
| count |
+-------+
| 2     |
+-------+
```

## INSERT[#](#insert "Link to this heading")

### Examples[#](#id1 "Link to this heading")

Insert values into a table.

```
INSERT INTO table_name { VALUES ( expression [, ...] ) [, ...] | query }
```

```
> INSERT INTO target_table VALUES (1, 'Foo'), (2, 'Bar');
+-------+
| count |
+-------+
| 2     |
+-------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/dml.md)

[Show Source](../../_sources/user-guide/sql/dml.md.txt)

---
# Expression API[#](#expression-api "Link to this heading")

DataFrame methods such as `select` and `filter` accept one or more logical expressions and there are many functions
available for creating logical expressions. These are documented below.

Tip

Most functions and methods may receive and return an `Expr`, which can be chained together using a fluent-style API:

```
use datafusion::prelude::*;
// create the expression `(a > 6) AND (b < 7)`
col("a").gt(lit(6)).and(col("b").lt(lit(7)));
```

## Identifiers[#](#identifiers "Link to this heading")

| Syntax | Description |
| --- | --- |
| col(ident) | Reference a column in a dataframe `col("a")` |

Note

ident
:   A type which implement `Into<Column>` trait

## Literal Values[#](#literal-values "Link to this heading")

| Syntax | Description |
| --- | --- |
| lit(value) | Literal value such as `lit(123)` or `lit("hello")` |

Note

value
:   A type which implement `Literal`

## Boolean Expressions[#](#boolean-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| and(x, y), x.and(y) | Logical AND |
| or(x, y), x.or(y) | Logical OR |
| !x, not(x), x.not() | Logical NOT |

Note

`!` is a bitwise or logical complement operator in Rust, but it only works as a logical NOT in expression API.

Note

Since `&&` and `||` are logical operators in Rust and cannot be overloaded these are not available in the expression API.

## Bitwise Expressions[#](#bitwise-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| x & y, bitwise\_and(x, y), x.bitand(y) | AND |
| x | y, bitwise\_or(x, y), x.bitor(y) | OR |
| x ^ y, bitwise\_xor(x, y), x.bitxor(y) | XOR |
| x << y, bitwise\_shift\_left(x, y), x.shl(y) | Left shift |
| x >> y, bitwise\_shift\_right(x, y), x.shr(y) | Right shift |

## Comparison Expressions[#](#comparison-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| x.eq(y) | Equal |
| x.not\_eq(y) | Not Equal |
| x.gt(y) | Greater Than |
| x.gt\_eq(y) | Greater Than or Equal |
| x.lt(y) | Less Than |
| x.lt\_eq(y) | Less Than or Equal |

Note

Comparison operators (`<`, `<=`, `==`, `>=`, `>`) could be overloaded by the `PartialOrd` and `PartialEq` trait in Rust,
but these operators always return a `bool` which makes them not work with the expression API.

## Arithmetic Expressions[#](#arithmetic-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| x + y, x.add(y) | Addition |
| x - y, x.sub(y) | Subtraction |
| x \* y, x.mul(y) | Multiplication |
| x / y, x.div(y) | Division |
| x % y, x.rem(y) | Remainder |
| -x, x.neg() | Negation |

## Math Functions[#](#math-functions "Link to this heading")

| Syntax | Description |
| --- | --- |
| abs(x) | absolute value |
| acos(x) | inverse cosine |
| acosh(x) | inverse hyperbolic cosine |
| asin(x) | inverse sine |
| asinh(x) | inverse hyperbolic sine |
| atan(x) | inverse tangent |
| atanh(x) | inverse hyperbolic tangent |
| atan2(y, x) | inverse tangent of y / x |
| cbrt(x) | cube root |
| ceil(x) | nearest integer greater than or equal to argument |
| cos(x) | cosine |
| cosh(x) | hyperbolic cosine |
| degrees(x) | converts radians to degrees |
| exp(x) | exponential |
| factorial(x) | factorial |
| floor(x) | nearest integer less than or equal to argument |
| gcd(x, y) | greatest common divisor |
| isnan(x) | predicate determining whether NaN/-NaN or not |
| iszero(x) | predicate determining whether 0.0/-0.0 or not |
| lcm(x, y) | least common multiple |
| ln(x) | natural logarithm |
| log(base, x) | logarithm of x for a particular base |
| log10(x) | base 10 logarithm |
| log2(x) | base 2 logarithm |
| nanvl(x, y) | returns x if x is not NaN otherwise returns y |
| pi() | approximate value of π |
| power(base, exponent) | base raised to the power of exponent |
| radians(x) | converts degrees to radians |
| round(x) | round to nearest integer |
| signum(x) | sign of the argument (-1, 0, +1) |
| sin(x) | sine |
| sinh(x) | hyperbolic sine |
| sqrt(x) | square root |
| tan(x) | tangent |
| tanh(x) | hyperbolic tangent |
| trunc(x) | truncate toward zero |

Note

Unlike to some databases the math functions in Datafusion works the same way as Rust math functions, avoiding failing on corner cases e.g.

```
select log(-1), log(0), sqrt(-1);
+----------------+---------------+-----------------+
| log(Int64(-1)) | log(Int64(0)) | sqrt(Int64(-1)) |
+----------------+---------------+-----------------+
| NaN            | -inf          | NaN             |
+----------------+---------------+-----------------+
```

## Conditional Expressions[#](#conditional-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| coalesce([value, …]) | Returns the first of its arguments that is not null. Null is returned only if all arguments are null. It is often used to substitute a default value for null values when data is retrieved for display. |
| case(expr)    .when(expr)    .end(),case(expr)    .when(expr)    .otherwise(expr) | CASE expression. The expression may chain multiple `when` expressions and end with an `end` or `otherwise` expression. Example:  ``` case(col(“a”) % lit(3))    .when(lit(0), lit(“A”))    .when(lit(1), lit(“B”))    .when(lit(2), lit(“C”))    .end() ```  or, end with `otherwise` to match any other conditions:  ``` case(col(“b”).gt(lit(100)))    .when(lit(true), lit(“value > 100”))    .otherwise(lit(“value <= 100”)) ``` |
| nullif(value1, value2) | Returns a null value if `value1` equals `value2`; otherwise it returns `value1`. This can be used to perform the inverse operation of the `coalesce` expression. |

## String Expressions[#](#string-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| ascii(character) | Returns a numeric representation of the character (`character`). Example: `ascii('a') -> 97` |
| bit\_length(text) | Returns the length of the string (`text`) in bits. Example: `bit_length('spider') -> 48` |
| btrim(text, characters) | Removes all specified characters (`characters`) from both the beginning and the end of the string (`text`). Example: `btrim('aabchelloccb', 'abc') -> hello` |
| char\_length(text) | Returns number of characters in the string (`text`). The same as `character_length` and `length`. Example: `char_length('lion') -> 4` |
| character\_length(text) | Returns number of characters in the string (`text`). The same as `char_length` and `length`. Example: `character_length('lion') -> 4` |
| concat(value1, [value2 [, …]]) | Concatenates the text representations (`value1, [value2 [, ...]]`) of all the arguments. NULL arguments are ignored. Example: `concat('aaa', 'bbc', NULL, 321) -> aaabbc321` |
| concat\_ws(separator, value1, [value2 [, …]]) | Concatenates the text representations (`value1, [value2 [, ...]]`) of all the arguments with the separator (`separator`). NULL arguments are ignored. `concat_ws('/', 'path', 'to', NULL, 'my', 'folder', 123) -> path/to/my/folder/123` |
| chr(integer) | Returns a character by its numeric representation (`integer`). Example: `chr(90) -> 8` |
| initcap | Converts the first letter of each word to upper case and the rest to lower case. Example: `initcap('hi TOM') -> Hi Tom` |
| left(text, number) | Returns a certain number (`number`) of first characters (`text`). Example: `left('like', 2) -> li` |
| length(text) | Returns number of characters in the string (`text`). The same as `character_length` and `char_length`. Example: `length('lion') -> 4` |
| lower(text) | Converts all characters in the string (`text`) into lower case. Example: `lower('HELLO') -> hello` |
| lpad(text, length, [, fill]) | Extends the string to length (`length`) by prepending the characters (`fill`) (a space by default). Example: `lpad('bb', 5, 'a') → aaabb` |
| ltrim(text, text) | Removes all specified characters (`characters`) from the beginning of the string (`text`). Example: `ltrim('aabchelloccb', 'abc') -> helloccb` |
| md5(text) | Computes the MD5 hash of the argument (`text`). |
| octet\_length(text) | Returns number of bytes in the string (`text`). |
| repeat(text, number) | Repeats the string the specified number of times. Example: `repeat('1', 4) -> 1111` |
| replace(string, from, to) | Replaces a specified string (`from`) with another specified string (`to`) in the string (`string`). Example: `replace('Hello', 'replace', 'el') -> Hola` |
| reverse(text) | Reverses the order of the characters in the string (`text`). Example: `reverse('hello') -> olleh` |
| right(text, number) | Returns a certain number (`number`) of last characters (`text`). Example: `right('like', 2) -> ke` |
| rpad(text, length, [, fill]) | Extends the string to length (`length`) by prepending the characters (`fill`) (a space by default). Example: `rpad('bb', 5, 'a') → bbaaa` |
| rtrim | Removes all specified characters (`characters`) from the end of the string (`text`). Example: `rtrim('aabchelloccb', 'abc') -> aabchello` |
| digest(input, algorithm) | Computes the binary hash of `input`, using the `algorithm`. |
| split\_part(string, delimiter, index) | Splits the string (`string`) based on a delimiter (`delimiter`) and picks out the desired field based on the index (`index`). |
| starts\_with(string, prefix) | Returns `true` if the string (`string`) starts with the specified prefix (`prefix`). If not, it returns `false`. Example: `starts_with('Hi Tom', 'Hi') -> true` |
| strpos | Finds the position from where the `substring` matches the `string` |
| substr(string, position, [, length]) | Returns substring from the position (`position`) with length (`length`) characters in the string (`string`). |
| translate(string, from, to) | Replaces the characters in `from` with the counterpart in `to`. Example: `translate('abcde', 'acd', '15') -> 1b5e` |
| trim(string) | Removes all characters, space by default from the string (`string`) |
| upper | Converts all characters in the string into upper case. Example: `upper('hello') -> HELLO` |

## Array Expressions[#](#array-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| array\_any\_value(array) | Returns the first non-null element in the array. `array_any_value([NULL, 1, 2, 3]) -> 1` |
| array\_append(array, element) | Appends an element to the end of an array. `array_append([1, 2, 3], 4) -> [1, 2, 3, 4]` |
| array\_concat(array[, …, array\_n]) | Concatenates arrays. `array_concat([1, 2, 3], [4, 5, 6]) -> [1, 2, 3, 4, 5, 6]` |
| array\_has(array, element) | Returns true if the array contains the element `array_has([1,2,3], 1) -> true` |
| array\_has\_all(array, sub-array) | Returns true if all elements of sub-array exist in array `array_has_all([1,2,3], [1,3]) -> true` |
| array\_has\_any(array, sub-array) | Returns true if any elements exist in both arrays `array_has_any([1,2,3], [1,4]) -> true` |
| array\_dims(array) | Returns an array of the array’s dimensions. `array_dims([[1, 2, 3], [4, 5, 6]]) -> [2, 3]` |
| array\_distinct(array) | Returns distinct values from the array after removing duplicates. `array_distinct([1, 3, 2, 3, 1, 2, 4]) -> [1, 2, 3, 4]` |
| array\_element(array, index) | Extracts the element with the index n from the array `array_element([1, 2, 3, 4], 3) -> 3` |
| empty(array) | Returns true for an empty array or false for a non-empty array. `empty([1]) -> false` |
| flatten(array) | Converts an array of arrays to a flat array `flatten([[1], [2, 3], [4, 5, 6]]) -> [1, 2, 3, 4, 5, 6]` |
| array\_length(array, dimension) | Returns the length of the array dimension. `array_length([1, 2, 3, 4, 5]) -> 5` |
| array\_ndims(array) | Returns the number of dimensions of the array. `array_ndims([[1, 2, 3], [4, 5, 6]]) -> 2` |
| array\_pop\_front(array) | Returns the array without the first element. `array_pop_front([1, 2, 3]) -> [2, 3]` |
| array\_pop\_back(array) | Returns the array without the last element. `array_pop_back([1, 2, 3]) -> [1, 2]` |
| array\_position(array, element) | Searches for an element in the array, returns first occurrence. `array_position([1, 2, 2, 3, 4], 2) -> 2` |
| array\_positions(array, element) | Searches for an element in the array, returns all occurrences. `array_positions([1, 2, 2, 3, 4], 2) -> [2, 3]` |
| array\_prepend(element, array) | Prepends an element to the beginning of an array. `array_prepend(1, [2, 3, 4]) -> [1, 2, 3, 4]` |
| array\_repeat(element, count) | Returns an array containing element `count` times. `array_repeat(1, 3) -> [1, 1, 1]` |
| array\_remove(array, element) | Removes the first element from the array equal to the given value. `NULL` elements already in the array are preserved when removing a non-`NULL` value, and `array_remove(array, NULL)` returns `NULL`. `array_remove([1, 2, NULL, 2, 4], 2) -> [1, NULL, 2, 4]` |
| array\_remove\_n(array, element, max) | Removes the first `max` elements from the array equal to the given value. `NULL` elements already in the array are preserved when removing a non-`NULL` value, and `array_remove_n(array, NULL, max)` returns `NULL`. `array_remove_n([1, 2, NULL, 2, 4], 2, 2) -> [1, NULL, 4]` |
| array\_remove\_all(array, element) | Removes all elements from the array equal to the given value. `NULL` elements already in the array are preserved when removing a non-`NULL` value, and `array_remove_all(array, NULL)` returns `NULL`. `array_remove_all([1, 2, NULL, 2, 4], 2) -> [1, NULL, 4]` |
| array\_replace(array, from, to) | Replaces the first occurrence of the specified element with another specified element. `array_replace([1, 2, 2, 3, 2, 1, 4], 2, 5) -> [1, 5, 2, 3, 2, 1, 4]` |
| array\_replace\_n(array, from, to, max) | Replaces the first `max` occurrences of the specified element with another specified element. `array_replace_n([1, 2, 2, 3, 2, 1, 4], 2, 5, 2) -> [1, 5, 5, 3, 2, 1, 4]` |
| array\_replace\_all(array, from, to) | Replaces all occurrences of the specified element with another specified element. `array_replace_all([1, 2, 2, 3, 2, 1, 4], 2, 5) -> [1, 5, 5, 3, 5, 1, 4]` |
| array\_slice(array, begin,end) | Returns a slice of the array. `array_slice([1, 2, 3, 4, 5, 6, 7, 8], 3, 6) -> [3, 4, 5, 6]` |
| array\_slice(array, begin, end, stride) | Returns a slice of the array with added stride feature. `array_slice([1, 2, 3, 4, 5, 6, 7, 8], 3, 6, 2) -> [3, 5, 6]` |
| array\_to\_string(array, delimiter) | Converts each element to its text representation. `array_to_string([1, 2, 3, 4], ',') -> 1,2,3,4` |
| array\_intersect(array1, array2) | Returns an array of the elements in the intersection of array1 and array2. `array_intersect([1, 2, 3, 4], [5, 6, 3, 4]) -> [3, 4]` |
| array\_union(array1, array2) | Returns an array of the elements in the union of array1 and array2 without duplicates. `array_union([1, 2, 3, 4], [5, 6, 3, 4]) -> [1, 2, 3, 4, 5, 6]` |
| array\_except(array1, array2) | Returns an array of the elements that appear in the first array but not in the second. `array_except([1, 2, 3, 4], [5, 6, 3, 4]) -> [1, 2]` |
| array\_resize(array, size, value) | Resizes the list to contain size elements. Initializes new elements with value or empty if value is not set. `array_resize([1, 2, 3], 5, 0) -> [1, 2, 3, 0, 0]` |
| array\_sort(array, desc, null\_first) | Returns sorted array. `array_sort([3, 1, 2, 5, 4]) -> [1, 2, 3, 4, 5]` |
| cardinality(array/map) | Returns the total number of elements in the array or map. `cardinality([[1, 2, 3], [4, 5, 6]]) -> 6` |
| make\_array(value1, [value2 [, …]]) | Returns an Arrow array using the specified input expressions. `make_array(1, 2, 3) -> [1, 2, 3]` |
| range(start [, stop, step]) | Returns an Arrow array between start and stop with step. `SELECT range(2, 10, 3) -> [2, 5, 8]` |
| string\_to\_array(array, delimiter, null\_string) | Splits a `string` based on a `delimiter` and returns an array of parts. Any parts matching the optional `null_string` will be replaced with `NULL`. `string_to_array('abc#def#ghi', '#', ' ') -> ['abc', 'def', 'ghi']` |
| trim\_array(array, n) | Deprecated |

## Regular Expressions[#](#regular-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| regexp\_match | Matches a regular expression against a string and returns matched substrings. |
| regexp\_replace | Replaces strings that match a regular expression |

## Temporal Expressions[#](#temporal-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| date\_part | Extracts a subfield from the date. |
| date\_trunc | Truncates the date to a specified level of precision. |
| from\_unixtime | Returns the unix time in format. |
| to\_timestamp | Converts a string to a `Timestamp(_, _)` |
| to\_timestamp\_millis | Converts a string to a `Timestamp(Milliseconds, None)` |
| to\_timestamp\_micros | Converts a string to a `Timestamp(Microseconds, None)` |
| to\_timestamp\_seconds | Converts a string to a `Timestamp(Seconds, None)` |
| now() | Returns current time. |

## Other Expressions[#](#other-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| array([value1, …]) | Returns an array of fixed size with each argument (`[value1, ...]`) on it. |
| in\_list(expr, list, negated) | Returns `true` if (`expr`) belongs or not belongs (`negated`) to a list (`list`), otherwise returns false. |
| random() | Returns a random value from 0 (inclusive) to 1 (exclusive). |
| sha224(text) | Computes the SHA224 hash of the argument (`text`). |
| sha256(text) | Computes the SHA256 hash of the argument (`text`). |
| sha384(text) | Computes the SHA384 hash of the argument (`text`). |
| sha512(text) | Computes the SHA512 hash of the argument (`text`). |
| to\_hex(integer) | Converts the integer (`integer`) to the corresponding hexadecimal string. |

## Aggregate Functions[#](#aggregate-functions "Link to this heading")

| Syntax | Description |
| --- | --- |
| avg(expr) | Сalculates the average value for `expr`. |
| avg\_distinct(expr) | Creates an expression to represent the avg(distinct) aggregate function |
| approx\_distinct(expr) | Calculates an approximate count of the number of distinct values for `expr`. |
| approx\_median(expr) | Calculates an approximation of the median for `expr`. |
| approx\_percentile\_cont(expr, percentile [, centroids]) | Calculates an approximation of the specified `percentile` for `expr`. Optional `centroids` parameter controls accuracy (default: 100). |
| approx\_percentile\_cont\_with\_weight(expr, weight\_expr, percentile [, centroids]) | Calculates an approximation of the specified `percentile` for `expr` and `weight_expr`. Optional `centroids` parameter controls accuracy (default: 100). |
| bit\_and(expr) | Computes the bitwise AND of all non-null input values for `expr`. |
| bit\_or(expr) | Computes the bitwise OR of all non-null input values for `expr`. |
| bit\_xor(expr) | Computes the bitwise exclusive OR of all non-null input values for `expr`. |
| bool\_and(expr) | Returns true if all non-null input values (`expr`) are true, otherwise false. |
| bool\_or(expr) | Returns true if any non-null input value (`expr`) is true, otherwise false. |
| count(expr) | Returns the number of rows for `expr`. |
| count\_distinct(expr) | Creates an expression to represent the count(distinct) aggregate function |
| cube(exprs) | Creates a grouping set for all combination of `exprs` |
| grouping\_set(exprs) | Create a grouping set. |
| max(expr) | Finds the maximum value of `expr`. |
| median(expr) | Сalculates the median of `expr`. |
| min(expr) | Finds the minimum value of `expr`. |
| rollup(exprs) | Creates a grouping set for rollup sets. |
| sum(expr) | Сalculates the sum of `expr`. |
| sum\_distinct(expr) | Creates an expression to represent the sum(distinct) aggregate function |

## Aggregate Function Builder[#](#aggregate-function-builder "Link to this heading")

You can also use the `ExprFunctionExt` trait to more easily build Aggregate arguments `Expr`.

See `datafusion-examples/examples/query_planning/expr_api.rs` for example usage.

| Syntax | Equivalent to |
| --- | --- |
| first\_value\_udaf.call(vec![expr]).order\_by(vec![expr]).build().unwrap() | first\_value(expr, Some(vec![expr])) |

## Subquery Expressions[#](#subquery-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| exists | Creates an `EXISTS` subquery expression |
| in\_subquery | `df1.filter(in_subquery(col("foo"), df2))?` is the equivalent of the SQL `WHERE foo IN <df2>` |
| not\_exists | Creates a `NOT EXISTS` subquery expression |
| not\_in\_subquery | Creates a `NOT IN` subquery expression |
| scalar\_subquery | Creates a scalar subquery expression |

## User-Defined Function Expressions[#](#user-defined-function-expressions "Link to this heading")

| Syntax | Description |
| --- | --- |
| create\_udf | Creates a new UDF with a specific signature and specific return type. |
| create\_udaf | Creates a new UDAF with a specific signature, state type and return type. |

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/expressions.md)

[Show Source](../_sources/user-guide/expressions.md.txt)

---
# Gentle Arrow Introduction[#](#gentle-arrow-introduction "Link to this heading")

## [Overview](#id1)[#](#overview "Link to this heading")

DataFusion uses [Apache Arrow](https://arrow.apache.org/docs/index.html) as its native in-memory format, so anyone using DataFusion will likely interact with Arrow at some point. This guide introduces the key Arrow concepts you need to know to effectively use DataFusion.

Apache Arrow defines a standardized columnar representation for in-memory data. This enables different systems and languages (e.g., Rust and Python) to share data with zero-copy interchange, avoiding serialization overhead. In addition to zero copy interchange, Arrow also standardizes best practice columnar data representation enabling high performance analytical processing through vectorized execution.

## [Columnar Layout](#id2)[#](#columnar-layout "Link to this heading")

Quick visual: row-major (left) vs Arrow’s columnar layout (right). For a deeper primer, see the [arrow2 guide](https://jorgecarleitao.github.io/arrow2/main/guide/arrow.html#what-is-apache-arrow).

```
Traditional Row Storage:          Arrow Columnar Storage:
┌──────────────────┐              ┌─────────┬─────────┬──────────┐
│ id │ name │ age  │              │   id    │  name   │   age    │
├────┼──────┼──────┤              ├─────────┼─────────┼──────────┤
│ 1  │  A   │  30  │              │ [1,2,3] │ [A,B,C] │[30,25,35]│
│ 2  │  B   │  25  │              └─────────┴─────────┴──────────┘
│ 3  │  C   │  35  │                   ↑          ↑         ↑
└──────────────────┘              Int32Array StringArray Int32Array
(read entire rows)                (process entire columns at once)
```

## [`RecordBatch`](#id3)[#](#recordbatch "Link to this heading")

Arrow’s standard unit for packaging data is the **[`RecordBatch`](https://docs.rs/arrow-array/latest/arrow_array/struct.RecordBatch.html)**.

A **[`RecordBatch`](https://docs.rs/arrow-array/latest/arrow_array/struct.RecordBatch.html)** represents a horizontal slice of a table—a collection of equal-length columnar arrays that conform to a defined schema. Each column within the slice is a contiguous Arrow array, and all columns have the same number of rows (length). This chunked, immutable unit enables efficient streaming and parallel execution.

Think of it as having two perspectives:

* **Columnar inside**: Each column (`id`, `name`, `age`) is a contiguous array optimized for vectorized operations
* **Row-chunked externally**: The batch represents a chunk of rows (e.g., rows 1-1000), making it a manageable unit for streaming

RecordBatches are **immutable snapshots**—once created, they cannot be modified. Any transformation produces a *new* RecordBatch, enabling safe parallel processing without locks or coordination overhead.

This design allows DataFusion to process streams of row-based chunks while gaining maximum performance from the columnar layout.

## [Streaming Through the Engine](#id4)[#](#streaming-through-the-engine "Link to this heading")

DataFusion processes queries as pull-based pipelines where operators request batches from their inputs. This streaming approach enables early result production, bounds memory usage (spilling to disk only when necessary), and naturally supports parallel execution across multiple CPU cores.

For example, given the following query:

```
SELECT name FROM 'data.parquet' WHERE id > 10
```

The DataFusion Pipeline looks like this:

```
┌─────────────┐    ┌──────────────┐    ┌────────────────┐    ┌──────────────────┐    ┌──────────┐
│ Parquet     │───▶│ Scan         │───▶│ Filter         │───▶│ Projection       │───▶│ Results  │
│ File        │    │ Operator     │    │ Operator       │    │ Operator         │    │          │
└─────────────┘    └──────────────┘    └────────────────┘    └──────────────────┘    └──────────┘
                   (reads data)        (id > 10)             (keeps "name" col)
                   RecordBatch ───▶    RecordBatch ────▶     RecordBatch ────▶        RecordBatch
```

In this pipeline, [`RecordBatch`](https://docs.rs/arrow-array/latest/arrow_array/struct.RecordBatch.html)es are the “packages” of columnar data that flow between the different stages of query execution. Each operator processes batches incrementally, enabling the system to produce results before reading the entire input.

## [Creating `ArrayRef` and `RecordBatch`es](#id5)[#](#creating-arrayref-and-recordbatches "Link to this heading")

Sometimes you need to create Arrow data programmatically rather than reading from files.

The first thing needed is creating an Arrow Array, for each column. [arrow-rs](https://github.com/apache/arrow-rs) provides array builders and `From` impls to create arrays from Rust vectors.

```
use arrow::array::{StringArray, Int32Array};
// Create an Int32Array from a vector of i32 values
let ids = Int32Array::from(vec![1, 2, 3]);
// There are similar constructors for other array types, e.g., StringArray, Float64Array, etc.
let names = StringArray::from(vec![Some("alice"), None, Some("carol")]);
```

Every element in an Arrow array can be “null” (aka missing). Often, arrays are
created from `Option<T>` values to indicate nullability (e.g., `Some("alice")`
vs `None` above).

Note: You’ll see [`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html) used frequently in the code—Arrow arrays are wrapped in
[`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html) (atomically reference-counted pointers) to enable cheap, thread-safe
sharing across operators and tasks. [`ArrayRef`](https://docs.rs/arrow-array/latest/arrow_array/array/type.ArrayRef.html) is simply a type alias for
`Arc<dyn Array>`. To create an `ArrayRef`, wrap your array in `Arc::new(...)` as shown below.

```
use std::sync::Arc;
// To get an ArrayRef, wrap the Int32Array in an Arc.
// (note you will often have to explicitly type annotate to ArrayRef)
let arr: ArrayRef = Arc::new(Int32Array::from(vec![1, 2, 3]));

// you can also store Strings and other types in ArrayRefs
let arr: ArrayRef = Arc::new(
  StringArray::from(vec![Some("alice"), None, Some("carol")])
);
```

To create a [`RecordBatch`](https://docs.rs/arrow-array/latest/arrow_array/struct.RecordBatch.html), you need to define its [`Schema`](https://docs.rs/arrow-schema/latest/arrow_schema/struct.Schema.html) (the column names and types) and provide the corresponding columns as [`ArrayRef`](https://docs.rs/arrow-array/latest/arrow_array/array/type.ArrayRef.html)s as shown below:

```
use arrow_schema::{DataType, Field, Schema};

// Create the columns as Arrow arrays
let ids = Int32Array::from(vec![1, 2, 3]);
let names = StringArray::from(vec![Some("alice"), None, Some("carol")]);
// Create the schema
let schema = Arc::new(Schema::new(vec![
    Field::new("id", DataType::Int32, false), // false means non-nullable
    Field::new("name", DataType::Utf8, true), // true means nullable
]));
// Assemble the columns
let cols: Vec<ArrayRef> = vec![
      Arc::new(ids),
      Arc::new(names)
];
// Finally, create the RecordBatch
RecordBatch::try_new(schema, cols).expect("Failed to create RecordBatch");
```

## [Working with `ArrayRef` and `RecordBatch`](#id6)[#](#working-with-arrayref-and-recordbatch "Link to this heading")

Most DataFusion APIs are in terms of [`ArrayRef`](https://docs.rs/arrow-array/latest/arrow_array/array/type.ArrayRef.html) and [`RecordBatch`](https://docs.rs/arrow-array/latest/arrow_array/struct.RecordBatch.html). To work with the
underlying data, you typically downcast the [`ArrayRef`](https://docs.rs/arrow-array/latest/arrow_array/array/type.ArrayRef.html) to its concrete type
(e.g., [`Int32Array`](https://docs.rs/arrow/latest/arrow/array/type.Int32Array.html)).

To do so either use the `as_any().downcast_ref::<T>()` method or the
`as_::<T>()` helper method from the [AsArray](https://docs.rs/arrow-array/latest/arrow_array/cast/trait.AsArray.html) trait.

```
// First check the data type of the array
match arr.data_type() {
   &DataType::Int32 => {
         // Downcast to Int32Array
         let int_array = arr.as_primitive::<Int32Type>();
         // Now you can access Int32Array methods
         for i in 0..int_array.len() {
              println!("Value at index {}: {}", i, int_array.value(i));
         }
   }
    _ => {
        println ! ("Array is not of type Int32");
    }
}
```

The following two downcasting methods are equivalent:

```
// Downcast to Int32Array using as_any
let int_array1 = arr.as_any().downcast_ref::<Int32Array>().unwrap();
// This is the same as using the as_::<T>() helper
let int_array2 = arr.as_primitive::<Int32Type>();
assert_eq!(int_array1, int_array2);
```

## [Common Pitfalls](#id7)[#](#common-pitfalls "Link to this heading")

When working with Arrow and RecordBatches, watch out for these common issues:

* **Schema consistency**: All batches in a stream must share the exact same [`Schema`](https://docs.rs/arrow-schema/latest/arrow_schema/struct.Schema.html). For example, you can’t have one batch where a column is [`Int32`](https://docs.rs/arrow-schema/latest/arrow_schema/enum.DataType.html#variant.Int32) and the next where it’s [`Int64`](https://docs.rs/arrow-schema/latest/arrow_schema/enum.DataType.html#variant.Int64), even if the values would fit
* **Immutability**: Arrays are immutable—to “modify” data, you must build new arrays or new RecordBatches. For instance, to change a value in an array, you’d create a new array with the updated value
* **Row by Row Processing**: Avoid iterating over Arrays element by element when possible, and use Arrow’s built-in [compute kernels](https://docs.rs/arrow/latest/arrow/compute/index.html) instead
* **Type mismatches**: Mixed input types across files may require explicit casts. For example, a string column `"123"` from a CSV file won’t automatically join with an integer column `123` from a Parquet file—you’ll need to cast one to match the other. Use Arrow’s [`cast`](https://docs.rs/arrow/latest/arrow/compute/fn.cast.html) kernel where appropriate
* **Batch size assumptions**: Don’t assume a particular batch size; always iterate until the stream ends. One file might produce 8192-row batches while another produces 1024-row batches

## [Further reading](#id8)[#](#further-reading "Link to this heading")

**Arrow Documentation:**

* [Arrow Format Introduction](https://arrow.apache.org/docs/format/Intro.html) - Understand the Arrow specification and why it enables zero-copy data sharing
* [Arrow Columnar Format](https://arrow.apache.org/docs/format/Columnar.html) - Deep dive into memory layout for performance optimization
* [Arrow Rust Documentation](https://docs.rs/arrow/latest/arrow/) - Complete API reference for the Rust implementation

**Key API References:**

* [RecordBatch](https://docs.rs/arrow-array/latest/arrow_array/struct.RecordBatch.html) - The fundamental data structure for columnar data (a table slice)
* [ArrayRef](https://docs.rs/arrow-array/latest/arrow_array/array/type.ArrayRef.html) - Represents a reference-counted Arrow array (single column)
* [DataType](https://docs.rs/arrow-schema/latest/arrow_schema/enum.DataType.html) - Enum of all supported Arrow data types (e.g., Int32, Utf8)
* [Schema](https://docs.rs/arrow-schema/latest/arrow_schema/struct.Schema.html) - Describes the structure of a RecordBatch (column names and types)

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/arrow-introduction.md)

[Show Source](../_sources/user-guide/arrow-introduction.md.txt)

---
# Struct Type Coercion and Field Mapping[#](#struct-type-coercion-and-field-mapping "Link to this heading")

DataFusion uses **name-based field mapping** when coercing struct types across different operations. This document explains how struct coercion works, when it applies, and how to handle NULL fields.

## Overview: Name-Based vs Positional Mapping[#](#overview-name-based-vs-positional-mapping "Link to this heading")

When combining structs from different sources (e.g., in UNION, array construction, or JOINs), DataFusion matches struct fields by **name** rather than by **position**. This provides more robust and predictable behavior compared to positional matching.

### Example: Field Reordering is Handled Transparently[#](#example-field-reordering-is-handled-transparently "Link to this heading")

```
-- These two structs have the same fields in different order
SELECT [{a: 1, b: 2}, {b: 3, a: 4}];

-- Result: Field names matched, values unified
-- [{"a": 1, "b": 2}, {"a": 4, "b": 3}]
```

## Coercion Paths Using Name-Based Matching[#](#coercion-paths-using-name-based-matching "Link to this heading")

The following query operations use name-based field mapping for struct coercion:

### 1. Array Literal Construction[#](#array-literal-construction "Link to this heading")

When creating array literals with struct elements that have different field orders:

```
-- Structs with reordered fields in array literal
SELECT [{x: 1, y: 2}, {y: 3, x: 4}];

-- Unified type: List(Struct("x": Int32, "y": Int32))
-- Values: [{"x": 1, "y": 2}, {"x": 4, "y": 3}]
```

**When it applies:**

* Array literals with struct elements: `[{...}, {...}]`
* Nested arrays with structs: `[[{x: 1}, {x: 2}]]`

### 2. Array Construction from Columns[#](#array-construction-from-columns "Link to this heading")

When constructing arrays from table columns with different struct schemas:

```
CREATE TABLE t_left (s struct(x int, y int)) AS VALUES ({x: 1, y: 2});
CREATE TABLE t_right (s struct(y int, x int)) AS VALUES ({y: 3, x: 4});

-- Dynamically constructs unified array schema
SELECT [t_left.s, t_right.s] FROM t_left JOIN t_right;

-- Result: [{"x": 1, "y": 2}, {"x": 4, "y": 3}]
```

**When it applies:**

* Array construction with column references: `[col1, col2]`
* Array construction in joins with matching field names

### 3. UNION Operations[#](#union-operations "Link to this heading")

When combining query results with different struct field orders:

```
SELECT {a: 1, b: 2} as s
UNION ALL
SELECT {b: 3, a: 4} as s;

-- Result: {"a": 1, "b": 2} and {"a": 4, "b": 3}
```

**When it applies:**

* UNION ALL with structs: field names matched across branches
* UNION (deduplicated) with structs

### 4. Common Table Expressions (CTEs)[#](#common-table-expressions-ctes "Link to this heading")

When multiple CTEs produce structs with different field orders that are combined:

```
WITH
  t1 AS (SELECT {a: 1, b: 2} as s),
  t2 AS (SELECT {b: 3, a: 4} as s)
SELECT s FROM t1
UNION ALL
SELECT s FROM t2;

-- Result: Field names matched across CTEs
```

### 5. VALUES Clauses[#](#values-clauses "Link to this heading")

When creating tables or temporary results with struct values in different field orders:

```
CREATE TABLE t AS VALUES ({a: 1, b: 2}), ({b: 3, a: 4});

-- Table schema unified: struct(a: int, b: int)
-- Values: {a: 1, b: 2} and {a: 4, b: 3}
```

### 6. JOIN Operations[#](#join-operations "Link to this heading")

When joining tables where the JOIN condition involves structs with different field orders:

```
CREATE TABLE orders (customer struct(name varchar, id int));
CREATE TABLE customers (info struct(id int, name varchar));

-- Join matches struct fields by name
SELECT * FROM orders
JOIN customers ON orders.customer = customers.info;
```

### 7. Aggregate Functions[#](#aggregate-functions "Link to this heading")

When collecting structs with different field orders using aggregate functions like `array_agg`:

```
SELECT array_agg(s) FROM (
  SELECT {x: 1, y: 2} as s
  UNION ALL
  SELECT {y: 3, x: 4} as s
) t
GROUP BY category;

-- Result: Array of structs with unified field order
```

### 8. Window Functions[#](#window-functions "Link to this heading")

When using window functions with struct expressions having different field orders:

```
SELECT
  id,
  row_number() over (partition by s order by id) as rn
FROM (
  SELECT {category: 1, value: 10} as s, 1 as id
  UNION ALL
  SELECT {value: 20, category: 1} as s, 2 as id
);

-- Fields matched by name in PARTITION BY clause
```

## NULL Handling for Missing Fields[#](#null-handling-for-missing-fields "Link to this heading")

When structs have different field sets, missing fields are filled with **NULL** values during coercion.

### Example: Partial Field Overlap[#](#example-partial-field-overlap "Link to this heading")

```
-- Struct in first position has fields: a, b
-- Struct in second position has fields: b, c
-- Unified schema includes all fields: a, b, c

SELECT [
  CAST({a: 1, b: 2} AS STRUCT(a INT, b INT, c INT)),
  CAST({b: 3, c: 4} AS STRUCT(a INT, b INT, c INT))
];

-- Result:
-- [
--   {"a": 1, "b": 2, "c": NULL},
--   {"a": NULL, "b": 3, "c": 4}
-- ]
```

### Limitations[#](#limitations "Link to this heading")

**Field count must match exactly.** If structs have different numbers of fields and their field names don’t completely overlap, the query will fail:

```
-- This fails because field sets don't match:
-- t_left has {x, y} but t_right has {x, y, z}
SELECT [t_left.s, t_right.s] FROM t_left JOIN t_right;
-- Error: Cannot coerce struct with mismatched field counts
```

**Workaround: Use explicit CAST**

To handle partial field overlap, explicitly cast structs to a unified schema:

```
SELECT [
  CAST(t_left.s AS STRUCT(x INT, y INT, z INT)),
  CAST(t_right.s AS STRUCT(x INT, y INT, z INT))
] FROM t_left JOIN t_right;
```

## Comparison and Ordering[#](#comparison-and-ordering "Link to this heading")

DataFusion supports comparing `STRUCT` values with standard comparison operators
(`=`, `!=`, `<`, `<=`, `>`, `>=`). Ordering comparisons are lexicographical and
follow DataFusion’s default ascending comparison behavior, where `NULL` sorts
before non-`NULL` values.

### Examples[#](#examples "Link to this heading")

```
SELECT {x: 1, y: 2} < {x: 1, y: 3};
-- true

SELECT {x: 1, y: NULL} < {x: 1, y: 2};
-- true

SELECT {x: 1, y: NULL} = {x: 1, y: NULL};
--true
```

## Migration Guide: From Positional to Name-Based Matching[#](#migration-guide-from-positional-to-name-based-matching "Link to this heading")

If you have existing code that relied on **positional** struct field matching, you may need to update it.

### Example: Query That Changes Behavior[#](#example-query-that-changes-behavior "Link to this heading")

**Old behavior (positional):**

```
-- These would have been positionally mapped (left-to-right)
SELECT [{x: 1, y: 2}, {y: 3, x: 4}];
-- Old result (positional): [{"x": 1, "y": 2}, {"y": 3, "x": 4}]
```

**New behavior (name-based):**

```
-- Now uses name-based matching
SELECT [{x: 1, y: 2}, {y: 3, x: 4}];
-- New result (by name): [{"x": 1, "y": 2}, {"x": 4, "y": 3}]
```

### Migration Steps[#](#migration-steps "Link to this heading")

1. **Review struct operations** - Look for queries that combine structs from different sources
2. **Check field names** - Verify that field names match as expected (not positions)
3. **Test with new coercion** - Run queries and verify the results match your expectations
4. **Handle field reordering** - If you need specific field orders, use explicit CAST operations

### Using Explicit CAST for Compatibility[#](#using-explicit-cast-for-compatibility "Link to this heading")

If you need precise control over struct field order and types, use explicit `CAST`:

```
-- Guarantee specific field order and types
SELECT CAST({b: 3, a: 4} AS STRUCT(a INT, b INT));
-- Result: {"a": 4, "b": 3}
```

## Best Practices[#](#best-practices "Link to this heading")

### 1. Be Explicit with Schema Definitions[#](#be-explicit-with-schema-definitions "Link to this heading")

When joining or combining structs, define target schemas explicitly:

```
-- Good: explicit schema definition
SELECT CAST(data AS STRUCT(id INT, name VARCHAR, active BOOLEAN))
FROM external_source;
```

### 2. Use Named Struct Constructors[#](#use-named-struct-constructors "Link to this heading")

Prefer named struct constructors for clarity:

```
-- Good: field names are explicit
SELECT named_struct('id', 1, 'name', 'Alice', 'active', true);

-- Or using struct literal syntax
SELECT {id: 1, name: 'Alice', active: true};
```

### 3. Test Field Mappings[#](#test-field-mappings "Link to this heading")

Always verify that field mappings work as expected:

```
-- Use arrow_typeof to verify unified schema
SELECT arrow_typeof([{x: 1, y: 2}, {y: 3, x: 4}]);
-- Result: List(Struct("x": Int32, "y": Int32))
```

### 4. Handle Partial Field Overlap Explicitly[#](#handle-partial-field-overlap-explicitly "Link to this heading")

When combining structs with partial field overlap, use explicit CAST:

```
-- Instead of relying on implicit coercion
SELECT [
  CAST(left_struct AS STRUCT(x INT, y INT, z INT)),
  CAST(right_struct AS STRUCT(x INT, y INT, z INT))
];
```

### 5. Document Struct Schemas[#](#document-struct-schemas "Link to this heading")

In complex queries, document the expected struct schemas:

```
-- Expected schema: {customer_id: INT, name: VARCHAR, age: INT}
SELECT {
  customer_id: c.id,
  name: c.name,
  age: c.age
} as customer_info
FROM customers c;
```

## Error Messages and Troubleshooting[#](#error-messages-and-troubleshooting "Link to this heading")

### “Cannot coerce struct with different field counts”[#](#cannot-coerce-struct-with-different-field-counts "Link to this heading")

**Cause:** Trying to combine structs with different numbers of fields.

**Solution:**

```
-- Use explicit CAST to handle missing fields
SELECT [
  CAST(struct1 AS STRUCT(a INT, b INT, c INT)),
  CAST(struct2 AS STRUCT(a INT, b INT, c INT))
];
```

### “Field X not found in struct”[#](#field-x-not-found-in-struct "Link to this heading")

**Cause:** Referencing a field name that doesn’t exist in the struct.

**Solution:**

```
-- Verify field names match exactly (case-sensitive)
SELECT s['field_name'] FROM my_table;  -- Use bracket notation for access
-- Or use get_field function
SELECT get_field(s, 'field_name') FROM my_table;
```

### Unexpected NULL values after coercion[#](#unexpected-null-values-after-coercion "Link to this heading")

**Cause:** Struct coercion added NULL for missing fields.

**Solution:** Check that all structs have the required fields, or explicitly handle NULLs:

```
SELECT COALESCE(s['field'], default_value) FROM my_table;
```

## Related Functions[#](#related-functions "Link to this heading")

* `arrow_typeof()` - Returns the Arrow type of an expression
* `struct()` / `named_struct()` - Creates struct values
* `get_field()` - Extracts field values from structs
* `CAST()` - Explicitly casts structs to specific schemas

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/struct_coercion.md)

[Show Source](../../_sources/user-guide/sql/struct_coercion.md.txt)

---
# EXPLAIN[#](#explain "Link to this heading")

The `EXPLAIN` command shows the logical and physical execution plan for the specified SQL statement.

## Syntax[#](#syntax "Link to this heading")

```
EXPLAIN [ANALYZE] [VERBOSE] [FORMAT format] statement
```

## `EXPLAIN`[#](#id1 "Link to this heading")

Shows the execution plan of a statement.
If you need more detailed output, use `EXPLAIN VERBOSE`.
Note that `EXPLAIN VERBOSE` only supports the `indent` format.

The optional `[FORMAT format]` clause controls how the plan is displayed as
explained below. If this clause is not specified, the plan is displayed using
the format from the [configuration value](../configs.html) `datafusion.explain.format`.

### `tree` format (default)[#](#tree-format-default "Link to this heading")

The `tree` format is modeled after [DuckDB plans](https://duckdb.org/docs/stable/guides/meta/explain.html) and is designed to be easier
to see the high level structure of the plan

```
> EXPLAIN FORMAT TREE SELECT SUM(x) FROM t GROUP BY b;
+---------------+-------------------------------+
| plan_type     | plan                          |
+---------------+-------------------------------+
| physical_plan | ┌───────────────────────────┐ |
|               | │       ProjectionExec      │ |
|               | │    --------------------   │ |
|               | │    sum(t.x): sum(t.x)@1   │ |
|               | └─────────────┬─────────────┘ |
|               | ┌─────────────┴─────────────┐ |
|               | │       AggregateExec       │ |
|               | │    --------------------   │ |
|               | │       aggr: sum(t.x)      │ |
|               | │     group_by: b@0 as b    │ |
|               | │                           │ |
|               | │           mode:           │ |
|               | │      FinalPartitioned     │ |
|               | └─────────────┬─────────────┘ |
|               | ┌─────────────┴─────────────┐ |
|               | │    CoalesceBatchesExec    │ |
|               | └─────────────┬─────────────┘ |
|               | ┌─────────────┴─────────────┐ |
|               | │      RepartitionExec      │ |
|               | │    --------------------   │ |
|               | │   input_partition_count:  │ |
|               | │             1             │ |
|               | │                           │ |
|               | │    partitioning_scheme:   │ |
|               | │      Hash([b@0], 16)      │ |
|               | └─────────────┬─────────────┘ |
|               | ┌─────────────┴─────────────┐ |
|               | │       AggregateExec       │ |
|               | │    --------------------   │ |
|               | │       aggr: sum(t.x)      │ |
|               | │     group_by: b@1 as b    │ |
|               | │       mode: Partial       │ |
|               | └─────────────┬─────────────┘ |
|               | ┌─────────────┴─────────────┐ |
|               | │       DataSourceExec      │ |
|               | │    --------------------   │ |
|               | │         bytes: 224        │ |
|               | │       format: memory      │ |
|               | │          rows: 1          │ |
|               | └───────────────────────────┘ |
|               |                               |
+---------------+-------------------------------+
1 row(s) fetched.
Elapsed 0.016 seconds.
```

### `indent` format[#](#indent-format "Link to this heading")

The `indent` format shows both the logical and physical plan, with one line for
each operator in the plan. Child plans are indented to show the hierarchy.

See [Reading Explain Plans](../explain-usage.html) for more information on how to interpret these plans.

```
> CREATE TABLE t(x int, b int) AS VALUES (1, 2), (2, 3);
0 row(s) fetched.
Elapsed 0.004 seconds.

> EXPLAIN FORMAT INDENT SELECT SUM(x) FROM t GROUP BY b;
+---------------+-------------------------------------------------------------------------------+
| plan_type     | plan                                                                          |
+---------------+-------------------------------------------------------------------------------+
| logical_plan  | Projection: sum(t.x)                                                          |
|               |   Aggregate: groupBy=[[t.b]], aggr=[[sum(CAST(t.x AS Int64))]]                |
|               |     TableScan: t projection=[x, b]                                            |
| physical_plan | ProjectionExec: expr=[sum(t.x)@1 as sum(t.x)]                                 |
|               |   AggregateExec: mode=FinalPartitioned, gby=[b@0 as b], aggr=[sum(t.x)]       |
|               |     CoalesceBatchesExec: target_batch_size=8192                               |
|               |       RepartitionExec: partitioning=Hash([b@0], 16), input_partitions=1       |
|               |         AggregateExec: mode=Partial, gby=[b@1 as b], aggr=[sum(t.x)]          |
|               |           DataSourceExec: partitions=1, partition_sizes=[1]                   |
|               |                                                                               |
+---------------+-------------------------------------------------------------------------------+
2 row(s) fetched.
Elapsed 0.004 seconds.
```

### `pgjson` format[#](#pgjson-format "Link to this heading")

The `pgjson` format is modeled after [Postgres JSON](https://www.postgresql.org/docs/current/sql-explain.html) format.

You can use this format to visualize the plan in existing plan visualization
tools, such as [dalibo](https://explain.dalibo.com/)

```
> EXPLAIN FORMAT PGJSON SELECT SUM(x) FROM t GROUP BY b;
+--------------+----------------------------------------------------+
| plan_type    | plan                                               |
+--------------+----------------------------------------------------+
| logical_plan | [                                                  |
|              |   {                                                |
|              |     "Plan": {                                      |
|              |       "Expressions": [                             |
|              |         "sum(t.x)"                                 |
|              |       ],                                           |
|              |       "Node Type": "Projection",                   |
|              |       "Output": [                                  |
|              |         "sum(t.x)"                                 |
|              |       ],                                           |
|              |       "Plans": [                                   |
|              |         {                                          |
|              |           "Aggregates": "sum(CAST(t.x AS Int64))", |
|              |           "Group By": "t.b",                       |
|              |           "Node Type": "Aggregate",                |
|              |           "Output": [                              |
|              |             "b",                                   |
|              |             "sum(t.x)"                             |
|              |           ],                                       |
|              |           "Plans": [                               |
|              |             {                                      |
|              |               "Node Type": "TableScan",            |
|              |               "Output": [                          |
|              |                 "x",                               |
|              |                 "b"                                |
|              |               ],                                   |
|              |               "Plans": [],                         |
|              |               "Relation Name": "t"                 |
|              |             }                                      |
|              |           ]                                        |
|              |         }                                          |
|              |       ]                                            |
|              |     }                                              |
|              |   }                                                |
|              | ]                                                  |
+--------------+----------------------------------------------------+
1 row(s) fetched.
Elapsed 0.008 seconds.
```

### `graphviz` format[#](#graphviz-format "Link to this heading")

The `graphviz` format uses the [DOT language](https://graphviz.org/doc/info/lang.html) that can be used with [Graphviz](https://graphviz.org/) to
generate a visual representation of the plan.

```
> EXPLAIN FORMAT GRAPHVIZ SELECT SUM(x) FROM t GROUP BY b;
+--------------+------------------------------------------------------------------------------------------------------------------------------+
| plan_type    | plan                                                                                                                         |
+--------------+------------------------------------------------------------------------------------------------------------------------------+
| logical_plan |                                                                                                                              |
|              | // Begin DataFusion GraphViz Plan,                                                                                           |
|              | // display it online here: https://dreampuf.github.io/GraphvizOnline                                                         |
|              |                                                                                                                              |
|              | digraph {                                                                                                                    |
|              |   subgraph cluster_1                                                                                                         |
|              |   {                                                                                                                          |
|              |     graph[label="LogicalPlan"]                                                                                               |
|              |     2[shape=box label="Projection: sum(t.x)"]                                                                                |
|              |     3[shape=box label="Aggregate: groupBy=[[t.b]], aggr=[[sum(CAST(t.x AS Int64))]]"]                                        |
|              |     2 -> 3 [arrowhead=none, arrowtail=normal, dir=back]                                                                      |
|              |     4[shape=box label="TableScan: t projection=[x, b]"]                                                                      |
|              |     3 -> 4 [arrowhead=none, arrowtail=normal, dir=back]                                                                      |
|              |   }                                                                                                                          |
|              |   subgraph cluster_5                                                                                                         |
|              |   {                                                                                                                          |
|              |     graph[label="Detailed LogicalPlan"]                                                                                      |
|              |     6[shape=box label="Projection: sum(t.x)\nSchema: [sum(t.x):Int64;N]"]                                                    |
|              |     7[shape=box label="Aggregate: groupBy=[[t.b]], aggr=[[sum(CAST(t.x AS Int64))]]\nSchema: [b:Int32;N, sum(t.x):Int64;N]"] |
|              |     6 -> 7 [arrowhead=none, arrowtail=normal, dir=back]                                                                      |
|              |     8[shape=box label="TableScan: t projection=[x, b]\nSchema: [x:Int32;N, b:Int32;N]"]                                      |
|              |     7 -> 8 [arrowhead=none, arrowtail=normal, dir=back]                                                                      |
|              |   }                                                                                                                          |
|              | }                                                                                                                            |
|              | // End DataFusion GraphViz Plan                                                                                              |
|              |                                                                                                                              |
+--------------+------------------------------------------------------------------------------------------------------------------------------+
1 row(s) fetched.
Elapsed 0.010 seconds.
```

## `EXPLAIN ANALYZE`[#](#explain-analyze "Link to this heading")

Shows the execution plan and metrics of a statement. Note that `EXPLAIN ANALYZE`
only supports the `indent` format.

```
EXPLAIN ANALYZE SELECT SUM(x) FROM table GROUP BY b;

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| plan_type         | plan                                                                                                                                                      |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Plan with Metrics | CoalescePartitionsExec, metrics=[]                                                                                                                        |
|                   |   ProjectionExec: expr=[SUM(table.x)@1 as SUM(x)], metrics=[]                                                                                             |
|                   |     HashAggregateExec: mode=FinalPartitioned, gby=[b@0 as b], aggr=[SUM(x)], metrics=[outputRows=2]                                                       |
|                   |       CoalesceBatchesExec: target_batch_size=4096, metrics=[]                                                                                             |
|                   |         RepartitionExec: partitioning=Hash([Column { name: "b", index: 0 }], 16), metrics=[sendTime=839560, fetchTime=122528525, repartitionTime=5327877] |
|                   |           HashAggregateExec: mode=Partial, gby=[b@1 as b], aggr=[SUM(x)], metrics=[outputRows=2]                                                          |
|                   |             RepartitionExec: partitioning=RoundRobinBatch(16), metrics=[fetchTime=5660489, repartitionTime=0, sendTime=8012]                              |
|                   |               DataSourceExec: file_groups={1 group: [[/tmp/table.csv]]}, has_header=false, metrics=[]                                                        |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
```

By default `EXPLAIN ANALYZE` shows the aggregated metrics from all partitions for each operator. If you need to display per-partition metrics, use `EXPLAIN ANALYZE VERBOSE`.

You can also set `datafusion.explain.analyze_level` from the [configuration value](../configs.html) to control the detail level for the metrics displayed.

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/explain.md)

[Show Source](../../_sources/user-guide/sql/explain.md.txt)

---
# Subqueries[#](#subqueries "Link to this heading")

Subqueries (also known as inner queries or nested queries) are queries within
a query.
Subqueries can be used in `SELECT`, `FROM`, `WHERE`, and `HAVING` clauses.

The examples below are based on the following tables.

```
SELECT * FROM x;

+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
| 2        | 4        |
+----------+----------+
```

```
SELECT * FROM y;

+--------+--------+
| number | string |
+--------+--------+
| 1      | one    |
+--------+--------+
| 2      | two    |
+--------+--------+
| 3      | three  |
+--------+--------+
| 4      | four   |
+--------+--------+
```

## Subquery operators[#](#subquery-operators "Link to this heading")

* [[ NOT ] EXISTS](#not-exists)
* [[ NOT ] IN](#not-in)

### [ NOT ] EXISTS[#](#not-exists "Link to this heading")

The `EXISTS` operator returns all rows where a
*[correlated subquery](#correlated-subqueries)* produces one or more matches for
that row. `NOT EXISTS` returns all rows where a *correlated subquery* produces
zero matches for that row. Only *correlated subqueries* are supported.

```
[NOT] EXISTS (subquery)
```

### [ NOT ] IN[#](#not-in "Link to this heading")

The `IN` operator returns all rows where a given expression’s value can be found
in the results of a *[correlated subquery](#correlated-subqueries)*.
`NOT IN` returns all rows where a given expression’s value cannot be found in
the results of a subquery or list of values.

```
expression [NOT] IN (subquery|list-literal)
```

#### Examples[#](#examples "Link to this heading")

```
SELECT * FROM x WHERE column_1 IN (1,3);

+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
```

```
SELECT * FROM x WHERE column_1 NOT IN (1,3);

+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 2        | 4        |
+----------+----------+
```

#### `IN` with tuple-like values and `NULL`[#](#in-with-tuple-like-values-and-null "Link to this heading")

For tuple-like values, `IN` uses DataFusion’s struct equality semantics:

```
SELECT (1, 1) IN ((1, NULL));
-- false

SELECT (1, NULL) IN ((1, NULL));
-- true
```

## SELECT clause subqueries[#](#select-clause-subqueries "Link to this heading")

`SELECT` clause subqueries use values returned from the inner query as part
of the outer query’s `SELECT` list.
The `SELECT` clause only supports [scalar subqueries](#scalar-subqueries) that
return a single value per execution of the inner query.
The returned value can be unique per row.

```
SELECT [expression1[, expression2, ..., expressionN],] (<subquery>)
```

**Note**: `SELECT` clause subqueries can be used as an alternative to `JOIN`
operations.

### Example[#](#example "Link to this heading")

```
SELECT
  column_1,
  (
    SELECT
      first_value(string)
    FROM
      y
    WHERE
      number = x.column_1
  ) AS "numeric string"
FROM
  x;

+----------+----------------+
| column_1 | numeric string |
+----------+----------------+
|        1 | one            |
|        2 | two            |
+----------+----------------+
```

## FROM clause subqueries[#](#from-clause-subqueries "Link to this heading")

`FROM` clause subqueries return a set of results that is then queried and
operated on by the outer query.

```
SELECT expression1[, expression2, ..., expressionN] FROM (<subquery>)
```

To reference columns from other tables in the same `FROM` clause, use [`LATERAL JOIN`](select.html#lateral-join).

### Example[#](#id1 "Link to this heading")

The following query returns the average of maximum values per room.
The inner query returns the maximum value for each field from each room.
The outer query uses the results of the inner query and returns the average
maximum value for each field.

```
SELECT
  column_2
FROM
  (
    SELECT
      *
    FROM
      x
    WHERE
      column_1 > 1
  );

+----------+
| column_2 |
+----------+
|        4 |
+----------+
```

## WHERE clause subqueries[#](#where-clause-subqueries "Link to this heading")

`WHERE` clause subqueries compare an expression to the result of the subquery
and return *true* or *false*.
Rows that evaluate to *false* or NULL are filtered from results.
The `WHERE` clause supports correlated and non-correlated subqueries
as well as scalar and non-scalar subqueries (depending on the operator used
in the predicate expression).

```
SELECT
  expression1[, expression2, ..., expressionN]
FROM
  <measurement>
WHERE
  expression operator (<subquery>)
```

**Note:** `WHERE` clause subqueries can be used as an alternative to `JOIN`
operations.

### Examples[#](#id2 "Link to this heading")

#### `WHERE` clause with scalar subquery[#](#where-clause-with-scalar-subquery "Link to this heading")

The following query returns all rows with `column_2` values above the average
of all `number` values in `y`.

```
SELECT
  *
FROM
  x
WHERE
  column_2 > (
    SELECT
      AVG(number)
    FROM
      y
  );

+----------+----------+
| column_1 | column_2 |
+----------+----------+
|        2 |        4 |
+----------+----------+
```

#### `WHERE` clause with non-scalar subquery[#](#where-clause-with-non-scalar-subquery "Link to this heading")

Non-scalar subqueries must use the `[NOT] IN` or `[NOT] EXISTS` operators and
can only return a single column.
The values in the returned column are evaluated as a list.

The following query returns all rows with `column_2` values in table `x` that
are in the list of numbers with string lengths greater than three from table
`y`.

```
SELECT
  *
FROM
  x
WHERE
  column_2 IN (
    SELECT
      number
    FROM
      y
    WHERE
      length(string) > 3
  );

+----------+----------+
| column_1 | column_2 |
+----------+----------+
|        2 |        4 |
+----------+----------+
```

### `WHERE` clause with correlated subquery[#](#where-clause-with-correlated-subquery "Link to this heading")

The following query returns rows with `column_2` values from table `x` greater
than the average `string` value length from table `y`.
The subquery in the `WHERE` clause uses the `column_1` value from the outer
query to return the average `string` value length for that specific value.

```
SELECT
  *
FROM
  x
WHERE
  column_2 > (
    SELECT
      AVG(length(string))
    FROM
      y
    WHERE
      number = x.column_1
  );

+----------+----------+
| column_1 | column_2 |
+----------+----------+
|        2 |        4 |
+----------+----------+
```

## HAVING clause subqueries[#](#having-clause-subqueries "Link to this heading")

`HAVING` clause subqueries compare an expression that uses aggregate values
returned by aggregate functions in the `SELECT` clause to the result of the
subquery and return *true* or *false*.
Rows that evaluate to *false* are filtered from results.
The `HAVING` clause supports correlated and non-correlated subqueries
as well as scalar and non-scalar subqueries (depending on the operator used
in the predicate expression).

```
SELECT
  aggregate_expression1[, aggregate_expression2, ..., aggregate_expressionN]
FROM
  <measurement>
WHERE
  <conditional_expression>
GROUP BY
  column_expression1[, column_expression2, ..., column_expressionN]
HAVING
  expression operator (<subquery>)
```

### Examples[#](#id3 "Link to this heading")

The following query calculates the averages of even and odd numbers in table `y`
and returns the averages that are equal to the maximum value of `column_1`
in table `x`.

#### `HAVING` clause with a scalar subquery[#](#having-clause-with-a-scalar-subquery "Link to this heading")

```
SELECT
  AVG(number) AS avg,
  (number % 2 = 0) AS even
FROM
  y
GROUP BY
  even
HAVING
  avg = (
    SELECT
      MAX(column_1)
    FROM
      x
  );

+-------+--------+
|   avg | even   |
+-------+--------+
|     2 | false  |
+-------+--------+
```

#### `HAVING` clause with a non-scalar subquery[#](#having-clause-with-a-non-scalar-subquery "Link to this heading")

Non-scalar subqueries must use the `[NOT] IN` or `[NOT] EXISTS` operators and
can only return a single column.
The values in the returned column are evaluated as a list.

The following query calculates the averages of even and odd numbers in table `y`
and returns the averages that are in `column_1` of table `x`.

```
SELECT
  AVG(number) AS avg,
  (number % 2 = 0) AS even
FROM
  y
GROUP BY
  even
HAVING
  avg IN (
    SELECT
      column_1
    FROM
      x
  );

+-------+--------+
|   avg | even   |
+-------+--------+
|     2 | false  |
+-------+--------+
```

## Subquery categories[#](#subquery-categories "Link to this heading")

Subqueries can be categorized as one or more of the following based on the
behavior of the subquery:

* [correlated](#correlated-subqueries) or
  [non-correlated](#non-correlated-subqueries)
* [scalar](#scalar-subqueries) or [non-scalar](#non-scalar-subqueries)

### Correlated subqueries[#](#correlated-subqueries "Link to this heading")

In a **correlated** subquery, the inner query depends on the values of the
current row being processed.

**Note:** DataFusion internally rewrites correlated subqueries into JOINs to
improve performance. In general correlated subqueries are **less performant**
than non-correlated subqueries.

### Non-correlated subqueries[#](#non-correlated-subqueries "Link to this heading")

In a **non-correlated** subquery, the inner query *doesn’t* depend on the outer
query and executes independently.
The inner query executes first, and then passes the results to the outer query.

### Scalar subqueries[#](#scalar-subqueries "Link to this heading")

A **scalar** subquery returns a single value (one column of one row).
If no rows are returned, the subquery returns NULL.

### Non-scalar subqueries[#](#non-scalar-subqueries "Link to this heading")

A **non-scalar** subquery returns 0, 1, or multiple rows, each of which may
contain 1 or multiple columns. For each column, if there is no value to return,
the subquery returns NULL. If no rows qualify to be returned, the subquery
returns 0 rows.

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/subqueries.md)

[Show Source](../../_sources/user-guide/sql/subqueries.md.txt)

---
# Installation[#](#installation "Link to this heading")

## Install and run using Cargo[#](#install-and-run-using-cargo "Link to this heading")

To build and install the latest release of `datafusion-cli` from source, do:

```
cargo install datafusion-cli
#    Updating crates.io index
#  Installing datafusion-cli v37.0.0
#    Updating crates.io index
# ...
```

## Install and run using Homebrew (on MacOS)[#](#install-and-run-using-homebrew-on-macos "Link to this heading")

`datafusion-cli` can also be installed via [Homebrew](https://docs.brew.sh/Installation) (on MacOS) like this:

```
brew install datafusion
# ...
# ==> Pouring datafusion--37.0.0.arm64_sonoma.bottle.tar.gz
# 🍺  /opt/homebrew/Cellar/datafusion/37.0.0: 9 files, 63.0MB
# ==> Running `brew cleanup datafusion`...
```

## Run using Docker[#](#run-using-docker "Link to this heading")

There is no officially published Docker image for the DataFusion CLI, so it is necessary to build from source
instead.

Use the following commands to clone this repository and build a Docker image containing the CLI tool. Note
that there is `.dockerignore` file in the root of the repository that may need to be deleted in order for
this to work.

```
git clone https://github.com/apache/datafusion
cd datafusion
# Note: the build can take a while
docker build -f datafusion-cli/Dockerfile . --tag datafusion-cli
# You can also bind persistent storage with `-v /path/to/data:/data`
docker run --rm -it datafusion-cli
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/cli/installation.md)

[Show Source](../../_sources/user-guide/cli/installation.md.txt)

---
# Features[#](#features "Link to this heading")

## General[#](#general "Link to this heading")

* SQL Parser
* SQL Query Planner
* DataFrame API
* Parallel query execution
* Streaming Execution

## Optimizations[#](#optimizations "Link to this heading")

* Query Optimizer
* Constant folding
* Join Reordering
* Limit Pushdown
* Projection push down
* Predicate push down

## SQL Support[#](#sql-support "Link to this heading")

* Type coercion
* Projection (`SELECT`)
* Filter (`WHERE`)
* Filter post-aggregate (`HAVING`)
* Sorting (`ORDER BY`)
* Limit (`LIMIT`)
* Aggregate (`GROUP BY`)
* cast /try\_cast
* [`VALUES` lists](https://www.postgresql.org/docs/current/queries-values.html)
* [String Functions](sql/scalar_functions.html#string-functions)
* [Conditional Functions](sql/scalar_functions.html#conditional-functions)
* [Time and Date Functions](sql/scalar_functions.html#time-and-date-functions)
* [Math Functions](sql/scalar_functions.html#math-functions)
* [Aggregate Functions](sql/aggregate_functions.html) (`SUM`, `MEDIAN`, and many more)
* Schema Queries

  * `SHOW TABLES`
  * `SHOW COLUMNS FROM <table/view>`
  * `SHOW CREATE TABLE <view>`
  * Basic SQL [Information Schema](sql/information_schema.html) (`TABLES`, `VIEWS`, `COLUMNS`)
  * Full SQL [Information Schema](sql/information_schema.html) support
* Support for nested types (`ARRAY`/`LIST` and `STRUCT`.

  * Read support
  * Write support
  * Field access (`col['field']` and [`col[1]`])
  * [Array Functions](sql/scalar_functions.html#array-functions)
  * [Struct Functions](sql/scalar_functions.html#struct-functions)

    * `struct`
    * [Postgres JSON operators](https://github.com/apache/datafusion/issues/6631) (`->`, `->>`, etc.)
* Subqueries
* Common Table Expressions (CTE)
* Set Operations (`UNION [ALL]`, `INTERSECT [ALL]`, `EXCEPT[ALL]`)
* Joins (`INNER`, `LEFT`, `RIGHT`, `FULL`, `CROSS`)
* Window Functions

  * Empty (`OVER()`)
  * Partitioning and ordering: (`OVER(PARTITION BY <..> ORDER BY <..>)`)
  * Custom Window (`ORDER BY time ROWS BETWEEN 2 PRECEDING AND 0 FOLLOWING)`)
  * User Defined Window and Aggregate Functions
* Catalogs

  * Schemas (`CREATE / DROP SCHEMA`)
  * Tables (`CREATE / DROP TABLE`, `CREATE TABLE AS SELECT`)
* Data Insert

  * `INSERT INTO`
  * `COPY .. INTO ..`
  * CSV
  * JSON
  * Parquet
  * Avro

## Runtime[#](#runtime "Link to this heading")

* Streaming Grouping
* Streaming Window Evaluation
* Memory limits enforced
* Spilling (to disk) Sort
* Spilling (to disk) Grouping
* Spilling (to disk) Sort Merge Join
* Spilling (to disk) Hash Join

## Data Sources[#](#data-sources "Link to this heading")

In addition to allowing arbitrary datasources via the [`TableProvider`](https://docs.rs/datafusion/latest/datafusion/catalog/trait.TableProvider.html)
trait, DataFusion includes built in support for the following formats:

* CSV
* Parquet

  * Primitive and Nested Types
  * Row Group and Data Page pruning on min/max statistics
  * Row Group pruning on Bloom Filters
  * Predicate push down (late materialization) [not by default](https://github.com/apache/datafusion/issues/3463)
* JSON
* Avro
* Arrow

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/features.md)

[Show Source](../_sources/user-guide/features.md.txt)

---
# DDL[#](#ddl "Link to this heading")

DDL stands for “Data Definition Language” and relates to creating and
modifying catalog objects such as Tables.

## CREATE DATABASE[#](#create-database "Link to this heading")

Create catalog with specified name.

```
CREATE DATABASE [ IF NOT EXISTS ] catalog
```

```
-- create catalog cat
CREATE DATABASE cat;
```

## CREATE SCHEMA[#](#create-schema "Link to this heading")

Create schema under specified catalog, or the default DataFusion catalog if not specified.

```
CREATE SCHEMA [ IF NOT EXISTS ] [ catalog. ] schema_name
```

```
-- create schema emu under catalog cat
CREATE SCHEMA cat.emu;
```

## CREATE EXTERNAL TABLE[#](#create-external-table "Link to this heading")

`CREATE EXTERNAL TABLE` SQL statement registers a location on a local
file system or remote object store as a named table which can be queried.

The supported syntax is:

```
CREATE [UNBOUNDED] EXTERNAL TABLE
[ IF NOT EXISTS ]
<TABLE_NAME>[ (<column_definition>) ]
STORED AS <file_type>
[ PARTITIONED BY (<column list>) ]
[ WITH ORDER (<ordered column list>) ]
[ OPTIONS (<key_value_list>) ]
LOCATION <literal>

<column_definition> := (<column_name> <data_type>, ...)

<column_list> := (<column_name>, ...)

<ordered_column_list> := (<column_name> <sort_clause>, ...)

<key_value_list> := (<literal> <literal>, <literal> <literal>, ...)
```

For a comprehensive list of format-specific options that can be specified in the `OPTIONS` clause, see [Format Options](format_options.html).

`file_type` is one of `CSV`, `ARROW`, `PARQUET`, `AVRO` or `JSON`

`LOCATION <literal>` specifies the location to find the data. It can be
a path to a file or directory of partitioned files locally or on an
object store.

### Example: Parquet[#](#example-parquet "Link to this heading")

Parquet data sources can be registered by executing a `CREATE EXTERNAL TABLE` SQL statement such as the following. It is not necessary to
provide schema information for Parquet files.

```
CREATE EXTERNAL TABLE taxi
STORED AS PARQUET
LOCATION '/mnt/nyctaxi/tripdata.parquet';
```

Note

Statistics
:   By default, when a table is created, DataFusion will read the files
    to gather statistics, which can be expensive but can accelerate subsequent
    queries substantially. If you don’t want to gather statistics
    when creating a table, set the `datafusion.execution.collect_statistics`
    configuration option to `false` before creating the table. For example:

```
SET datafusion.execution.collect_statistics = false;
```

See the [config settings docs](../configs.html) for more details.

### Example: Comma Separated Value (CSV)[#](#example-comma-separated-value-csv "Link to this heading")

CSV data sources can also be registered by executing a `CREATE EXTERNAL TABLE` SQL statement. The schema will be inferred based on
scanning a subset of the file.

```
CREATE EXTERNAL TABLE test
STORED AS CSV
LOCATION '/path/to/aggregate_simple.csv'
OPTIONS ('has_header' 'true');
```

### Example: Compression[#](#example-compression "Link to this heading")

It is also possible to use compressed files, such as `.csv.gz`:

```
CREATE EXTERNAL TABLE test
STORED AS CSV
COMPRESSION TYPE GZIP
LOCATION '/path/to/aggregate_simple.csv.gz'
OPTIONS ('has_header' 'true');
```

### Example: Specifying Schema[#](#example-specifying-schema "Link to this heading")

It is also possible to specify the schema manually.

```
CREATE EXTERNAL TABLE test (
    c1  VARCHAR NOT NULL,
    c2  INT NOT NULL,
    c3  SMALLINT NOT NULL,
    c4  SMALLINT NOT NULL,
    c5  INT NOT NULL,
    c6  BIGINT NOT NULL,
    c7  SMALLINT NOT NULL,
    c8  INT NOT NULL,
    c9  BIGINT NOT NULL,
    c10 VARCHAR NOT NULL,
    c11 FLOAT NOT NULL,
    c12 DOUBLE NOT NULL,
    c13 VARCHAR NOT NULL
)
STORED AS CSV
LOCATION '/path/to/aggregate_test_100.csv'
OPTIONS ('has_header' 'true');
```

### Example: Partitioned Tables[#](#example-partitioned-tables "Link to this heading")

It is also possible to specify a directory that contains a partitioned
table (multiple files with the same schema)

```
CREATE EXTERNAL TABLE test
STORED AS CSV
LOCATION '/path/to/directory/of/files'
OPTIONS ('has_header' 'true');
```

Tables that are partitioned using a Hive compliant partitioning scheme will have their columns and values automatically
detected and incorporated into the table’s schema and data. Given the following example directory structure:

```
hive_partitioned/
├── a=1
│   └── b=200
│       └── file1.parquet
└── a=2
    └── b=100
        └── file2.parquet
```

Users can specify the top level `hive_partitioned` directory as an `EXTERNAL TABLE` and leverage the Hive partitions to query
and filter data.

```
CREATE EXTERNAL TABLE hive_partitioned
STORED AS PARQUET
LOCATION '/path/to/hive_partitioned/';

SELECT count(*) FROM hive_partitioned WHERE b=100;
+------------------+
| count(*)         |
+------------------+
| 1                |
+------------------+
```

### Example: Unbounded Data Sources[#](#example-unbounded-data-sources "Link to this heading")

We can create unbounded data sources using the `CREATE UNBOUNDED EXTERNAL TABLE` SQL statement.

```
CREATE UNBOUNDED EXTERNAL TABLE taxi
STORED AS PARQUET
LOCATION '/mnt/nyctaxi/tripdata.parquet';
```

Note that this statement actually reads data from a fixed-size file, so a better example would involve reading from a FIFO file. Nevertheless, once Datafusion sees the `UNBOUNDED` keyword in a data source, it tries to execute queries that refer to this unbounded source in streaming fashion. If this is not possible according to query specifications, plan generation fails stating it is not possible to execute given query in streaming fashion. Note that queries that can run with unbounded sources (i.e. in streaming mode) are a subset of those that can with bounded sources. A query that fails with unbounded source(s) may work with bounded source(s).

### Example: `WITH ORDER` Clause[#](#example-with-order-clause "Link to this heading")

When creating an output from a data source that is already ordered by
an expression, you can pre-specify the order of the data using the
`WITH ORDER` clause. This applies even if the expression used for
sorting is complex, allowing for greater flexibility.

Here’s an example of how to use `WITH ORDER` clause.

```
CREATE EXTERNAL TABLE test (
    c1  VARCHAR NOT NULL,
    c2  INT NOT NULL,
    c3  SMALLINT NOT NULL,
    c4  SMALLINT NOT NULL,
    c5  INT NOT NULL,
    c6  BIGINT NOT NULL,
    c7  SMALLINT NOT NULL,
    c8  INT NOT NULL,
    c9  BIGINT NOT NULL,
    c10 VARCHAR NOT NULL,
    c11 FLOAT NOT NULL,
    c12 DOUBLE NOT NULL,
    c13 VARCHAR NOT NULL
)
STORED AS CSV
WITH ORDER (c2 ASC, c5 + c8 DESC NULLS FIRST)
LOCATION '/path/to/aggregate_test_100.csv'
OPTIONS ('has_header' 'true');
```

Where `WITH ORDER` clause specifies the sort order:

```
WITH ORDER (sort_expression1 [ASC | DESC] [NULLS { FIRST | LAST }]
         [, sort_expression2 [ASC | DESC] [NULLS { FIRST | LAST }] ...])
```

#### Cautions when using the WITH ORDER Clause[#](#cautions-when-using-the-with-order-clause "Link to this heading")

* It’s important to understand that using the `WITH ORDER` clause in the `CREATE EXTERNAL TABLE` statement only specifies the order in which the data should be read from the external file. If the data in the file is not already sorted according to the specified order, then the results may not be correct.
* It’s also important to note that the `WITH ORDER` clause does not affect the ordering of the data in the original external file.

If data sources are already partitioned in Hive style, `PARTITIONED BY` can be used for partition pruning.

```
/mnt/nyctaxi/year=2022/month=01/tripdata.parquet
/mnt/nyctaxi/year=2021/month=12/tripdata.parquet
/mnt/nyctaxi/year=2021/month=11/tripdata.parquet
```

```
CREATE EXTERNAL TABLE taxi
STORED AS PARQUET
PARTITIONED BY (year, month)
LOCATION '/mnt/nyctaxi';
```

## CREATE TABLE[#](#create-table "Link to this heading")

An in-memory table can be created with a query or values list.

```
CREATE [OR REPLACE] TABLE [IF NOT EXISTS] table_name AS [SELECT | VALUES LIST];
```

```
CREATE TABLE IF NOT EXISTS valuetable AS VALUES(1,'HELLO'),(12,'DATAFUSION');

CREATE TABLE IF NOT EXISTS valuetable(c1 INT, c2 VARCHAR) AS VALUES(1,'HELLO'),(12,'DATAFUSION');

CREATE TABLE memtable as select * from valuetable;
```

## DROP TABLE[#](#drop-table "Link to this heading")

Removes the table from DataFusion’s catalog.

```
DROP TABLE [ IF EXISTS ] table_name;
```

```
CREATE TABLE users AS VALUES(1,2),(2,3);
DROP TABLE users;
-- or use 'if exists' to silently ignore if the table doesn't exist
DROP TABLE IF EXISTS nonexistent_table;
```

## CREATE VIEW[#](#create-view "Link to this heading")

View is a virtual table based on the result of a SQL query. It can be created from an existing table or values list.

```
CREATE [ OR REPLACE ] VIEW view_name AS statement;
```

```
CREATE TABLE users AS VALUES(1,2),(2,3),(3,4),(4,5);
CREATE VIEW test AS SELECT column1 FROM users;
SELECT * FROM test;
+---------+
| column1 |
+---------+
| 1       |
| 2       |
| 3       |
| 4       |
+---------+
```

```
CREATE VIEW test AS VALUES(1,2),(5,6);
SELECT * FROM test;
+---------+---------+
| column1 | column2 |
+---------+---------+
| 1       | 2       |
| 5       | 6       |
+---------+---------+
```

## DROP VIEW[#](#drop-view "Link to this heading")

Removes the view from DataFusion’s catalog.

```
DROP VIEW [ IF EXISTS ] view_name;
```

```
-- drop users_v view from the customer_a schema
DROP VIEW IF EXISTS customer_a.users_v;
```

## DESCRIBE[#](#describe "Link to this heading")

Displays the schema of a table, showing column names, data types, and nullable status. Both `DESCRIBE` and `DESC` are supported as aliases.

```
{ DESCRIBE | DESC } table_name
```

The output contains three columns:

* `column_name`: The name of the column
* `data_type`: The data type of the column (e.g., Int32, Utf8, Boolean)
* `is_nullable`: Whether the column can contain null values (YES/NO)

### Example: Basic table description[#](#example-basic-table-description "Link to this heading")

```
-- Create a table
CREATE TABLE users AS VALUES (1, 'Alice', true), (2, 'Bob', false);

-- Describe the table structure
DESCRIBE users;
```

Output:

```
+--------------+-----------+-------------+
| column_name  | data_type | is_nullable |
+--------------+-----------+-------------+
| column1      | Int64     | YES         |
| column2      | Utf8      | YES         |
| column3      | Boolean   | YES         |
+--------------+-----------+-------------+
```

### Example: Using DESC alias[#](#example-using-desc-alias "Link to this heading")

```
-- DESC is an alias for DESCRIBE
DESC users;
```

### Example: Describing external tables[#](#example-describing-external-tables "Link to this heading")

```
-- Create an external table
CREATE EXTERNAL TABLE taxi
STORED AS PARQUET
LOCATION '/mnt/nyctaxi/tripdata.parquet';

-- Describe its schema
DESCRIBE taxi;
```

Output might show:

```
+--------------------+-----------------------------+-------------+
| column_name        | data_type                   | is_nullable |
+--------------------+-----------------------------+-------------+
| vendor_id          | Int32                       | YES         |
| pickup_datetime    | Timestamp(Nanosecond, None) | NO          |
| passenger_count    | Int32                       | YES         |
| trip_distance      | Float64                     | YES         |
+--------------------+-----------------------------+-------------+
```

The `DESCRIBE` command works with all table types in DataFusion, including:

* Regular tables created with `CREATE TABLE`
* External tables created with `CREATE EXTERNAL TABLE`
* Views created with `CREATE VIEW`
* Tables in different schemas using qualified names (e.g., `DESCRIBE schema_name.table_name`)

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/ddl.md)

[Show Source](../../_sources/user-guide/sql/ddl.md.txt)

---
# Concepts, Readings, Events[#](#concepts-readings-events "Link to this heading")

## 🧭 Background Concepts[#](#background-concepts "Link to this heading")

* **2024-06-13**: [2024 ACM SIGMOD International Conference on Management of Data: Apache Arrow DataFusion: A Fast, Embeddable, Modular Analytic Query Engine](https://dl.acm.org/doi/10.1145/3626246.3653368) - [Download](https://andrew.nerdnetworks.org/pdf/SIGMOD-2024-lamb.pdf), [Talk](https://youtu.be/-DpKcPfnNms), [Slides](https://docs.google.com/presentation/d/1gqcxSNLGVwaqN0_yJtCbNm19-w5pqPuktII5_EDA6_k/edit#slide=id.p), [Recording](https://youtu.be/-DpKcPfnNms)
* **2024-06-07**: [Video: SIGMOD 2024 Practice: Apache Arrow DataFusion A Fast, Embeddable, Modular Analytic Query Engine](https://www.youtube.com/watch?v=-DpKcPfnNms&amp;t=5s) - [Slides](https://docs.google.com/presentation/d/1gqcxSNLGVwaqN0_yJtCbNm19-w5pqPuktII5_EDA6_k/edit#slide=id.p)
* **2023-04-05**: [Video: DataFusion Architecture Part 3: Physical Plan and Execution](https://youtu.be/2jkWU3_w6z0) - [Slides](https://docs.google.com/presentation/d/1cA2WQJ2qg6tx6y4Wf8FH2WVSm9JQ5UgmBWATHdik0hg)
* **2023-04-04**: [Video: DataFusion Architecture Part 2: Logical Plans and Expressions](https://youtu.be/EzZTLiSJnhY) - [Slides](https://docs.google.com/presentation/d/1ypylM3-w60kVDW7Q6S99AHzvlBgciTdjsAfqNP85K30)
* **2023-03-31**: [Video: DataFusion Architecture Part 1: Query Engines](https://youtu.be/NVKujPxwSBA) - [Slides](https://docs.google.com/presentation/d/1D3GDVas-8y0sA4c8EOgdCvEjVND4s2E7I6zfs67Y4j8)
* **2020-02-27**: [Online Book: How Query Engines Work](https://andygrove.io/2020/02/how-query-engines-work/)

## ✨ Good Reads[#](#good-reads "Link to this heading")

This is a list of DataFusion related blog posts, articles, and other resources. Please open a PR to add any new resources you create or find

* **2026-04-10** [Blog: DataFusion and the Rise of Deconstructed Data Systems](https://thedataquarry.com/blog/datafusion-and-the-rise-of-deconstructed-data-systems/)
* **2026-04-04** [Video: Generalized Consensus & Native Top-K Joins in ParadeDB](https://www.youtube.com/watch?v=TeFsBVIYBis)
* **2026-03-31** [Blog: Writing Custom Table Providers in Apache DataFusion](https://datafusion.apache.org/blog/2026/03/31/custom-table-providers/)
* **2026-03-24** [Podcast: The Data Fusion Secret & Why Custom Query Engines Fail with Nikita Lapkov](https://www.youtube.com/watch?v=HkYF2So6nHQ)
* **2026-03-20** [Blog: Turning LIMIT into an I/O Optimization: Inside DataFusion’s Multi-Layer Pruning Stack](https://datafusion.apache.org/blog/2026/03/20/multi-layer-pruning/)
* **2026-02-09** [Blog: Vector search using only Parquet and DataFusion](https://blog.xiangpeng.systems/posts/vector-search-with-parquet-datafusion/)
* **2026-02-02** [Blog: Optimizing SQL CASE Expression Evaluation](https://datafusion.apache.org/blog/2026/02/02/case-expression/)
* **2026-01-12** [Blog: Extending SQL in DataFusion: from ->> to TABLESAMPLE](https://datafusion.apache.org/blog/2026/01/12/extending-sql)
* **2025-12-15** [Blog: Optimizing Repartitions in DataFusion: How I Went From Database Noob to Core Contribution](https://datafusion.apache.org/blog/2025/12/15/avoid-consecutive-repartitions)
* **2025-09-21** [Blog: Implementing User Defined Types and Custom Metadata in DataFusion](https://datafusion.apache.org/blog/2025/09/21/custom-types-using-metadata)
* **2025-09-10** [Blog: Dynamic Filters: Passing Information Between Operators During Execution for 25x Faster Queries](https://datafusion.apache.org/blog/2025/09/10/dynamic-filters)
* **2025-08-15** [Blog: Using External Indexes, Metadata Stores, Catalogs and Caches to Accelerate Queries on Apache Parquet](https://datafusion.apache.org/blog/2025/08/15/external-parquet-indexes)
* **2025-07-14** [Blog: Embedding User-Defined Indexes in Apache Parquet Files](https://datafusion.apache.org/blog/2025/07/14/user-defined-parquet-indexes)
* **2025-06-30** [Blog: Using Rust async for Query Execution and Cancelling Long-Running Queries](https://datafusion.apache.org/blog/2025/06/30/cancellation)
* **2025-06-15** [Blog: Optimizing SQL (and DataFrames) in DataFusion, Part 1: Query Optimization Overview](https://datafusion.apache.org/blog/2025/06/15/optimizing-sql-dataframes-part-one)
* **2025-06-15** [Blog: Optimizing SQL (and DataFrames) in DataFusion, Part 2: Optimizers in Apache DataFusion](https://datafusion.apache.org/blog/2025/06/15/optimizing-sql-dataframes-part-two)
* **2025-04-19** [Blog: User defined Window Functions in DataFusion](https://datafusion.apache.org/blog/2025/04/19/user-defined-window-functions)
* **2025-04-10** [Blog: tpchgen-rs World’s fastest open source TPC-H data generator, written in Rust](https://datafusion.apache.org/blog/2025/04/10/fastest-tpch-generator)
* **2025-03-11** [Blog: Using Ordering for Better Plans in Apache DataFusion](https://datafusion.apache.org/blog/2025/03/11/ordering-analysis)
* **2024-05-07** [Blog: Announcing Apache Arrow DataFusion is now Apache DataFusion](https://datafusion.apache.org/blog/2024/05/07/datafusion-tlp)
* **2024-03-06** [Blog: Announcing Apache Arrow DataFusion Comet](https://datafusion.apache.org/blog/2024/03/06/comet-donation)
* **2025-03-21** [Blog: Efficient Filter Pushdown in Parquet](https://datafusion.apache.org/blog/2025/03/21/parquet-pushdown/)
* **2025-03-20** [Blog: Parquet Pruning in DataFusion: Read Only What Matters](https://datafusion.apache.org/blog/2025/03/20/parquet-pruning/)
* **2025-02-12** [Video: Alex Kesling on Apache Arrow DataFusion - Papers We Love NYC](https://www.youtube.com/watch?v=6A4vFRpSq3k)
* **2025-01-30** [Video: Data & Drinks: Building Next-Gen Data Systems with Apache DataFusion](https://www.youtube.com/watch?v=GruBeVDoWq4)
* **2024-11-22** [Blog: Apache Datafusion Comet and the story of my first contribution to it](https://semyonsinchenko.github.io/ssinchenko/post/comet-first-contribution/)
* **2024-11-21** [Blog: DataFusion is featured as one of the coolest 10 open source software tools by CRN](https://www.crn.com/news/software/2024/the-10-coolest-open-source-software-tools-of-2024?page=3)
* **2024-11-20** [Blog: Apache DataFusion Comet 0.4.0 Release](https://datafusion.apache.org/blog/2024/11/20/datafusion-comet-0.4.0/)
* **2024-11-19** [Blog: Comparing approaches to User Defined Functions in Apache DataFusion using Python](https://datafusion.apache.org/blog/2024/11/19/datafusion-python-udf-comparisons/)
* **2024-11-18** [Blog: Apache DataFusion is now the fastest single node engine for querying Apache Parquet files](https://datafusion.apache.org/blog/2024/11/18/datafusion-fastest-single-node-parquet-clickbench/)
* **2024-11-18** [Blog: Building Databases over a Weekend](https://www.denormalized.io/blog/building-databases)
* **2024-10-29** [Video: MiDAS Seminar Fall 2024 on “Apache DataFusion” by Andrew Lamb](https://www.youtube.com/watch?v=CpnxuBwHbUc)
* **2024-10-27** [Blog: Caching in DataFusion: Don’t read twice](https://blog.xiangpeng.systems/posts/caching-datafusion/)
* **2024-10-24** [Blog: Parquet pruning in DataFusion: Read no more than you need](https://blog.xiangpeng.systems/posts/parquet-to-arrow/)
* **2024-09-13** [Blog: Using StringView / German Style Strings to make Queries Faster: Part 2 - String Operations](https://www.influxdata.com/blog/faster-queries-with-stringview-part-two-influxdb/) | [Reposted on DataFusion Blog](https://datafusion.apache.org/blog/2024/09/13/string-view-german-style-strings-part-2/)
* **2024-09-13** [Blog: Using StringView / German Style Strings to Make Queries Faster: Part 1- Reading Parquet](https://www.influxdata.com/blog/faster-queries-with-stringview-part-one-influxdb/) | [Reposted on Datafusion Blog](https://datafusion.apache.org/blog/2024/09/13/string-view-german-style-strings-part-1/)
* **2024-09-23 → 2024-12-02** [Talks: Carnegie Mellon University: Database Building Blocks Seminar Series - Fall 2024](https://db.cs.cmu.edu/seminar2024/)

  * **2024-11-12** [Video: Building InfluxDB 3.0 with the FDAP Stack: Apache Flight, DataFusion, Arrow and Parquet (Paul Dix)](https://www.youtube.com/watch?v=AGS4GNGDK_4)
  * **2024-11-04** [Video: Synnada: Towards “Unified” Compute Engines: Opportunities and Challenges (Mehmet Ozan Kabak)](https://www.youtube.com/watch?v=z38WY9uZtt4)
  * **2024-10-28** [Video: Exon: A Built for Purpose Bioinformatics Database (Trent Hauck)](https://www.youtube.com/watch?v=fltZMO8EGl0&amp;list=PLSE8ODhjZXjZc2AdXq_Lc1JS62R48UX2L&amp;index=6)
  * **2024-10-21** [Video: Accelerating Data and AI with Spice.ai Open-Source Software (Luke Kim)](https://www.youtube.com/watch?v=tyM-ec1lKfU&amp;list=PLSE8ODhjZXjZc2AdXq_Lc1JS62R48UX2L&amp;index=5)
  * **2024-10-07** [Video: ParadeDB – Postgres for Search and Analytics (Philippe Noël)](https://www.youtube.com/watch?v=Vxb8TELNM98&amp;list=PLSE8ODhjZXjZc2AdXq_Lc1JS62R48UX2L&amp;index=4)
  * **2024-09-30** [Video: Accelerating Apache Spark Workloads with Apache DataFusion Comet (Andy Grove)](https://www.youtube.com/watch?v=o59s0d3HE1k&amp;list=PLSE8ODhjZXjZc2AdXq_Lc1JS62R48UX2L&amp;index=3)
  * **2024-09-23** [Video: Apache Arrow DataFusion: A Fast, Embeddable, Modular Analytic Query Engine (Andrew Lamb)](https://www.youtube.com/watch?v=iJhRbDFJjbg&amp;list=PLSE8ODhjZXjZc2AdXq_Lc1JS62R48UX2L&amp;index=2)
* **2024-09-17** [Video: Profiling Apache DataFusion using flamegraph](https://www.youtube.com/watch?v=2z11xtYw_xs)
* **2024-08-25** [Blog: Pydantic/logfire: We’re changing database](https://github.com/pydantic/logfire/issues/408)
* **2024-08-15** [Video: Faster DataFusion with StringView - Xiangpeng Hao (Aug 15, 2024)](https://www.youtube.com/watch?v=RVLshX6fbds)
* **2024-08-14** [Blog: DataFusion @ UWheel](https://uwheel.rs/post/datafusion_uwheel/)
* **2024-06-17** [Blog: Columnar File Readers In-Depth: APIs and Fusion](https://blog.lancedb.com/columnar-file-readers-in-depth-apis-and-fusion/)
* **2024-06-14** [Talk: 2024 Simplicity in Management of Data (SiMOD): DataFusion: The Case for Building Open Data Systems (Keynote)](https://sfu-dis.github.io/simod/) - [Slides](https://docs.google.com/presentation/d/1K3EdknzkqU2LhWi_eNKXdcvNk0OEvk9AqTLqhZkPxuI/edit)
* **2024-05-29** [Blog: Query Push Down in Cube’s Semantic Layer](https://cube.dev/blog/query-push-down-in-cubes-semantic-layer)
* **2024-06-26** [Talk: Microsoft Gray Systems Lab: Building InfluxDB 3.0 (and other systems)](https://www.microsoft.com/en-us/research/group/gray-systems-lab) - [Slides](https://docs.google.com/presentation/d/1a4wHZij_69drdmD32TPombQ9zSaE6l26LZ87DAz2New/edit#slide=id.p)
* **2024-04-06** [Video: 1 billion row challenge in Rust using Apache Arrow](https://www.youtube.com/watch?v=Bc55FBwuJLA)
* **2024-03-26** [Talk: DataCouncil 2024: Building InfluxDB 3.0 with Apache Arrow, DataFusion, Flight, and Parquet](https://www.datacouncil.ai/talks24/building-influxdb-30-with-apache-arrow-datafusion-flight-and-parquet?hsLang=en) - [Slides](https://docs.google.com/presentation/d/12kdYHLyH79B5__9xs3de_hZyG9geW4jC3vUpiy39VA0), [Recording](https://www.youtube.com/watch?v=I-Z7kFGsYRI)
* **2024-03-20** [Video: Profiling DataFusion with Instruments (part of XCode on Mac OSx)](https://www.youtube.com/watch?v=P3dXH61Kr5U)
* **2024-03-18** [Blog: Making Recent Value Queries Hundreds of Times Faster](https://www.influxdata.com/blog/making-recent-value-queries-hundreds-times-faster/)
* **2023-10-25** [Blog: Flight, DataFusion, Arrow, and Parquet: Using the FDAP Architecture to build InfluxDB 3.0](https://www.influxdata.com/blog/flight-datafusion-arrow-parquet-fdap-architecture-influxdb/)
* **2023-09-26** [Blog: 100x Faster Ingest with DataFusion + Better Connectivity with FlightSQL](https://www.kamu.dev/blog/2023-09-datafusion-flightsql/)
* **2023-08-15** [Blog: Running Window Query in Stream Processing](https://www.synnada.ai/blog/running-window-query-in-stream-processing)
* **2023-08-05** [Blog: Aggregating Millions of Groups Fast in Apache Arrow DataFusion](https://www.influxdata.com/blog/aggregating-millions-groups-fast-apache-arrow-datafusion/) | [DataFusion Blog](https://arrow.apache.org/blog/2023/08/05/datafusion_fast_grouping/)
* **2023-07-28** [Blog: Sliding Window Hash Join (SWHJ)](https://www.synnada.ai/blog/sliding-window-hash-join-swhj)
* **2023-07-13** [Blog: Probabilistic Data Structures in Streaming: Count-Min Sketch](https://www.synnada.ai/blog/probabilistic-data-structures-in-streaming-count-min-sketch)
* **2023-05-25** [Video: D3L2: Discussing Rust, Ballista, Ray SQL, Data Fusion with Andy Grove](https://www.youtube.com/watch?v=NEL6DluUxgw)
* **2023-02-20** [Blog: General Purpose Stream Joins via Pruning Symmetric Hash Joins](https://www.synnada.ai/blog/general-purpose-stream-joins-via-pruning-symmetric-hash-joins)
* **2023-09-27** [Slides: MIT Database Group: Implementing InfluxDB IOx](https://docs.google.com/presentation/d/1_JXxapY2jksCOm5hePK8FIjO3buDzsrBBy0jUEpJR4A)
* **2023-06-02** [Talk: Dutch Seminar on Database System Design: Implementing InfluxDB IOx](https://dsdsd.da.cwi.nl/past_talks/post_talks/Andrew-Lamb/) - [Slides](https://docs.google.com/presentation/d/1XTsO2zsHkgBCF6C0YVwk0BnhZzLBrm39oeapOBb-s9A), [Recording](https://youtu.be/Y5K2Ik2oo-8)
* **2023-02-15** [Slides: Invited Talk at Optum Labs: Building a New Time Series Database](https://docs.google.com/presentation/d/1SzqgTtSKVqpuFUDdOHhRNC3mLmJ7oyVp0OyrYwHvgPA)
* **2023-01-01** [Blog: What I Want from DataFusion 2023](https://andygrove.io/2023/01/what-i-want-from-datafusion-2023/)
* **2022-12-07** [Blog: Querying Parquet with Millisecond Latency](https://www.influxdata.com/blog/querying-parquet-millisecond-latency/)
* **2022-06-27** [Talk: DataBricks Data+AI Summit: DataFusion and Arrow](https://www.databricks.com/dataaisummit/session/datafusion-and-arrow-supercharge-your-data-analytical-tool-rusty-query-engine) - [Slides](https://docs.google.com/presentation/d/1wLORMn23RD_sQ84W2w51s-Xysly5S8F5mGXzaeJ4QWY), [Recording](https://www.databricks.com/dataaisummit/session/datafusion-and-arrow-supercharge-your-data-analytical-tool-rusty-query-engine)
* **2022-05-23** [Video: The Data Thread 2022: Apache Arrow and DataFusion](https://www.youtube.com/watch?v=rb61lVH2vYc) - [Slides](https://docs.google.com/presentation/d/1Tkjfup5z_nsrBWIO7dXscEzC5toTQCXj0IsZeO3endc)
* **2021-03-10** [Video: InfluxData Tech Talk: Query Engine Design and Rust-Based DataFusion in Apache Arrow](https://www.youtube.com/watch?v=K6eCAVEk4kU) - [Slides](https://www.Slideshare.net/influxdata/influxdb-iox-tech-talks-query-engine-design-and-the-rustbased-datafusion-in-apache-arrow-244161934)

## 📅 Release Notes & Updates[#](#release-notes-updates "Link to this heading")

* **2026-04-02** [Apache DataFusion 53.0.0 Released](https://datafusion.apache.org/blog/2026/04/02/datafusion-53.0.0)
* **2026-03-18** [Apache DataFusion Comet 0.14.0 Release](https://datafusion.apache.org/blog/2026/03/18/datafusion-comet-0.14.0)
* **2026-01-30** [Apache DataFusion Comet 0.13.0 Release](https://datafusion.apache.org/blog/2026/01/30/datafusion-comet-0.13.0)
* **2026-01-12** [Apache DataFusion 52.0.0 Released](https://datafusion.apache.org/blog/2026/01/12/datafusion-52.0.0)
* **2025-12-04** [Apache DataFusion Comet 0.12.0 Release](https://datafusion.apache.org/blog/2025/12/04/datafusion-comet-0.12.0)
* **2025-11-25** [Apache DataFusion 51.0.0 Released](https://datafusion.apache.org/blog/2025/11/25/datafusion-51.0.0)
* **2025-10-21** [Apache DataFusion Comet 0.11.0 Release](https://datafusion.apache.org/blog/2025/10/21/datafusion-comet-0.11.0)
* **2025-09-29** [Apache DataFusion 50.0.0 Released](https://datafusion.apache.org/blog/2025/09/29/datafusion-50.0.0)
* **2025-09-16** [Apache DataFusion Comet 0.10.0 Release](https://datafusion.apache.org/blog/2025/09/16/datafusion-comet-0.10.0)
* **2025-07-28** [Apache DataFusion 49.0.0 Released](https://datafusion.apache.org/blog/2025/07/28/datafusion-49.0.0)
* **2025-07-16** [Apache DataFusion 48.0.0 Released](https://datafusion.apache.org/blog/2025/07/16/datafusion-48.0.0)
* **2025-07-11** [Apache DataFusion 47.0.0 Released](https://datafusion.apache.org/blog/2025/07/11/datafusion-47.0.0)
* **2025-07-01** [Apache DataFusion Comet 0.9.0 Release](https://datafusion.apache.org/blog/2025/07/01/datafusion-comet-0.9.0)
* **2025-05-06** [Apache DataFusion Comet 0.8.0 Release](https://datafusion.apache.org/blog/2025/05/06/datafusion-comet-0.8.0)
* **2025-03-30** [Apache DataFusion Python 46.0.0 Released](https://datafusion.apache.org/blog/2025/03/30/datafusion-python-46.0.0)
* **2025-03-24** [Apache DataFusion 46.0.0 Released](https://datafusion.apache.org/blog/2025/03/24/datafusion-46.0.0)
* **2025-03-20** [Apache DataFusion Comet 0.7.0 Release](https://datafusion.apache.org/blog/2025/03/20/datafusion-comet-0.7.0)
* **2025-02-20** [Apache DataFusion 45.0.0 Released](https://datafusion.apache.org/blog/2025/02/20/datafusion-45.0.0)
* **2025-02-17** [Apache DataFusion Comet 0.6.0 Release](https://datafusion.apache.org/blog/2025/02/17/datafusion-comet-0.6.0)
* **2025-02-02** [Apache DataFusion Ballista 43.0.0 Released](https://datafusion.apache.org/blog/2025/02/02/datafusion-ballista-43.0.0)
* **2025-01-17** [Apache DataFusion Comet 0.5.0 Release](https://datafusion.apache.org/blog/2025/01/17/datafusion-comet-0.5.0)

# 🌎 Community Events[#](#community-events "Link to this heading")

* **2026-07-22** [Denver Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/18428) - [RSVP](https://luma.com/jsu6faie)
* **2026-05-12** [New York City Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/20030) - [RSVP](https://luma.com/adhshv92)
* **2026-05-11** [San Francisco Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/21638) - [RSVP](https://luma.com/k3ointcl)
* **2026-04-23** [Seattle Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/13500) - [RSVP](https://luma.com/hxshbp0m)
* **2026-04-22** [Portland Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/19817) - [RSVP](https://luma.com/dsp3ud82)
* **2026-03-05** [Stockholm Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/18429) - [RSVP](https://luma.com/ctqtiqap), [Recording](https://youtu.be/9u4cNmL14Xs)
* **2026-02-19** [San Francisco Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/19859) - [RSVP](https://luma.com/p7r6fp2z), [Recording](https://www.youtube.com/playlist?list=PL42Ljm2tTt5peGUWMBN7WFkASq73j8PoU)
* **2025-11-12** [Boston Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/16703) - [Recording](https://youtu.be/wCAud478Dg8), [Slides](https://drive.google.com/file/d/18KGH_wGHkgdAfjy5sQVKFhnN1GyYXSzU)
* **2025-09-15** [New York City Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/16265) - [RSVP](https://lu.ma/qkcyycg0), [Recording](https://youtu.be/ElAiN_1fX_4)
* **2025-01-23** [Amsterdam Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/12988) - [Slides](https://github.com/apache/datafusion/discussions/12988)
* **2025-01-22** [Datadog Apache DataFusion Community Meeting](https://www.linkedin.com/posts/seshendranalla_apache-datafusion-community-meeting-2025-activity-7290384383201435648-8tqv) - [Recording](https://www.youtube.com/watch?v=ceTo2vUyRI0)
* **2025-01-15** [Boston Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/13165) - [Slides](https://docs.google.com/presentation/d/1_zBLHdqxPlhWuNK2oCA2d_hCpb6HWgHbVJBseiUXA80)
* **2024-12-18** [Chicago Apache DataFusion Meetup](https://lu.ma/eq5myc5i) - [Slides](https://github.com/apache/datafusion/discussions/12894), [Recording](https://www.youtube.com/playlist?list=PLrhIfEjaw9ilQEczOQlHyMznabtVRptyX)
* **2024-10-14** [Seattle Apache DataFusion Meetup](https://lu.ma/tnwl866b)
* **2024-09-27** [Belgrade Apache DataFusion Meetup](https://lu.ma/tmwuz4lg) - [Recap](https://github.com/apache/datafusion/discussions/11431#discussioncomment-10832070), [Slides](https://github.com/apache/datafusion/discussions/11431#discussioncomment-10826169), [Recording](https://www.youtube.com/playlist?list=PLrhIfEjaw9ilQEczOQlHyMznabtVRptyX)
* **2024-06-26** [New York City Apache DataFusion Meetup](https://lu.ma/2iwba0xm) - [Slides](https://docs.google.com/presentation/d/1dOLPAFPEMLhLv4NN6O9QSDIyyeiIySqAjky5cVgdWAE/edit#slide=id.g26bebde4fcc_3_7)
* **2024-06-25** [San Francisco Bay Area Apache DataFusion Meetup](https://lu.ma/6bphole2) - [Slides](https://docs.google.com/presentation/d/1Oz2yGllrWBkNGyiRMLr8qXTt4vmvtJWuI_weGThaZak/edit#slide=id.g26bebde4fcc_3_7), [Recording](https://www.youtube.com/playlist?list=PLrhIfEjaw9ilQEczOQlHyMznabtVRptyX)
* **2024-03-27** [Austin Apache DataFusion Meetup](https://github.com/apache/datafusion/discussions/8522) - [Slides](https://docs.google.com/presentation/d/1S51TK8waxHEJaxi_-uiSMrgQZ09m_hfaasPk5X5ExEY), [Recording](https://www.youtube.com/watch?v=q1N3pH3tFw8)

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/concepts-readings-events.md)

[Show Source](../_sources/user-guide/concepts-readings-events.md.txt)

---
# Information Schema[#](#information-schema "Link to this heading")

DataFusion supports showing metadata about the tables and views available. This information can be accessed using the
views of the ISO SQL `information_schema` schema or the DataFusion specific `SHOW TABLES` and `SHOW COLUMNS` commands.

## `SHOW TABLES`[#](#show-tables "Link to this heading")

To show tables in the DataFusion catalog, use the `SHOW TABLES` command or the
`information_schema.tables` view:

```
> show tables;
or
> select * from information_schema.tables;
+---------------+--------------------+------------+------------+
| table_catalog | table_schema       | table_name | table_type |
+---------------+--------------------+------------+------------+
| datafusion    | public             | t          | BASE TABLE |
| datafusion    | information_schema | tables     | VIEW       |
| datafusion    | information_schema | views      | VIEW       |
| datafusion    | information_schema | columns    | VIEW       |
+---------------+--------------------+------------+------------+
```

## `SHOW COLUMNS`[#](#show-columns "Link to this heading")

To show the schema of a table in DataFusion, use the `SHOW COLUMNS` command or
the `information_schema.columns` view.

```
> show columns from t;
or
> select table_catalog, table_schema, table_name, column_name, data_type, is_nullable from information_schema.columns;
+---------------+--------------+------------+-------------+-----------+-------------+
| table_catalog | table_schema | table_name | column_name | data_type | is_nullable |
+---------------+--------------+------------+-------------+-----------+-------------+
| datafusion    | public       | t          | Int64(1)    | Int64     | NO          |
+---------------+--------------+------------+-------------+-----------+-------------+
```

## `SHOW ALL` (configuration options)[#](#show-all-configuration-options "Link to this heading")

To show the current session configuration options, use the `SHOW ALL` command or
the `information_schema.df_settings` view:

```
select * from information_schema.df_settings;

+-------------------------------------------------+---------+
| name                                            | setting |
+-------------------------------------------------+---------+
| datafusion.execution.batch_size                 | 8192    |
| datafusion.execution.coalesce_batches           | true    |
| datafusion.execution.time_zone                  | UTC     |
| datafusion.explain.logical_plan_only            | false   |
| datafusion.explain.physical_plan_only           | false   |
...
| datafusion.optimizer.filter_null_join_keys      | false   |
| datafusion.optimizer.skip_failed_rules          | true    |
+-------------------------------------------------+---------+
```

## `SHOW FUNCTIONS`[#](#show-functions "Link to this heading")

To show the list of functions available, use the `SHOW FUNCTIONS` command or the

* `information_schema.information_schema.routines` view: functions and descriptions
* `information_schema.information_schema.parameters` view: parameters and descriptions

Syntax:

```
SHOW FUNCTIONS [ LIKE <pattern> ];
```

Example output

```
> show functions like '%datetrunc';
+---------------+-------------------------------------+-------------------------+-------------------------------------------------+---------------+-------------------------------------------------------+-----------------------------------+
| function_name | return_type                         | parameters              | parameter_types                                 | function_type | description                                           | syntax_example                    |
+---------------+-------------------------------------+-------------------------+-------------------------------------------------+---------------+-------------------------------------------------------+-----------------------------------+
| datetrunc     | Timestamp(Microsecond, Some("+TZ")) | [precision, expression] | [Utf8, Timestamp(Microsecond, Some("+TZ"))]     | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Nanosecond, None)         | [precision, expression] | [Utf8View, Timestamp(Nanosecond, None)]         | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Second, Some("+TZ"))      | [precision, expression] | [Utf8View, Timestamp(Second, Some("+TZ"))]      | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Microsecond, None)        | [precision, expression] | [Utf8View, Timestamp(Microsecond, None)]        | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Second, None)             | [precision, expression] | [Utf8View, Timestamp(Second, None)]             | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Microsecond, None)        | [precision, expression] | [Utf8, Timestamp(Microsecond, None)]            | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Second, None)             | [precision, expression] | [Utf8, Timestamp(Second, None)]                 | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Microsecond, Some("+TZ")) | [precision, expression] | [Utf8View, Timestamp(Microsecond, Some("+TZ"))] | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Nanosecond, Some("+TZ"))  | [precision, expression] | [Utf8, Timestamp(Nanosecond, Some("+TZ"))]      | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Millisecond, None)        | [precision, expression] | [Utf8, Timestamp(Millisecond, None)]            | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Millisecond, Some("+TZ")) | [precision, expression] | [Utf8, Timestamp(Millisecond, Some("+TZ"))]     | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Second, Some("+TZ"))      | [precision, expression] | [Utf8, Timestamp(Second, Some("+TZ"))]          | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Nanosecond, None)         | [precision, expression] | [Utf8, Timestamp(Nanosecond, None)]             | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Millisecond, None)        | [precision, expression] | [Utf8View, Timestamp(Millisecond, None)]        | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Millisecond, Some("+TZ")) | [precision, expression] | [Utf8View, Timestamp(Millisecond, Some("+TZ"))] | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
| datetrunc     | Timestamp(Nanosecond, Some("+TZ"))  | [precision, expression] | [Utf8View, Timestamp(Nanosecond, Some("+TZ"))]  | SCALAR        | Truncates a timestamp value to a specified precision. | date_trunc(precision, expression) |
+---------------+-------------------------------------+-------------------------+-------------------------------------------------+---------------+-------------------------------------------------------+-----------------------------------+
16 row(s) fetched.
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/information_schema.md)

[Show Source](../../_sources/user-guide/sql/information_schema.md.txt)

---
# Prepared Statements[#](#prepared-statements "Link to this heading")

The `PREPARE` statement allows for the creation and storage of a SQL statement with placeholder arguments.

The prepared statements can then be executed repeatedly in an efficient manner.

**SQL Example**

Create a prepared statement `greater_than` that selects all records where column “a” is greater than the parameter:

```
PREPARE greater_than(INT) AS SELECT * FROM example WHERE a > $1;
```

The prepared statement can then be executed with parameters as needed:

```
EXECUTE greater_than(20);
```

**Rust Example**

```
use datafusion::prelude::*;

#[tokio::main]
async fn main() -> datafusion::error::Result<()> {
  // Register the table
  let ctx = SessionContext::new();
  ctx.register_csv("example", "tests/data/example.csv", CsvReadOptions::new()).await?;

  // Create the prepared statement `greater_than`
  let prepare_sql = "PREPARE greater_than(INT) AS SELECT * FROM example WHERE a > $1";
  ctx.sql(prepare_sql).await?;

  // Execute the prepared statement `greater_than`
  let execute_sql = "EXECUTE greater_than(20)";
  let df = ctx.sql(execute_sql).await?;

  // Execute and print results
  df.show().await?;
  Ok(())
}
```

## Inferred Types[#](#inferred-types "Link to this heading")

If the parameter type is not specified, it can be inferred at execution time:

**SQL Example**

Create the prepared statement `greater_than`

```
PREPARE greater_than AS SELECT * FROM example WHERE a > $1;
```

Execute the prepared statement `greater_than`

```
EXECUTE greater_than(20);
```

**Rust Example**

```
    // Create the prepared statement `greater_than`
    let prepare_sql = "PREPARE greater_than AS SELECT * FROM example WHERE a > $1";
    ctx.sql(prepare_sql).await?;

    // Execute the prepared statement `greater_than`
    let execute_sql = "EXECUTE greater_than(20)";
    let df = ctx.sql(execute_sql).await?;
```

## Positional Arguments[#](#positional-arguments "Link to this heading")

In the case of multiple parameters, prepared statements can use positional arguments:

**SQL Example**

Create the prepared statement `greater_than`

```
PREPARE greater_than(INT, DOUBLE) AS SELECT * FROM example WHERE a > $1 AND b > $2;
```

Execute the prepared statement `greater_than`

```
EXECUTE greater_than(20, 23.3);
```

**Rust Example**

```
  // Create the prepared statement `greater_than`
  let prepare_sql = "PREPARE greater_than(INT, DOUBLE) AS SELECT * FROM example WHERE a > $1 AND b > $2";
  ctx.sql(prepare_sql).await?;

  // Execute the prepared statement `greater_than`
  let execute_sql = "EXECUTE greater_than(20, 23.3)";
  let df = ctx.sql(execute_sql).await?;
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/prepared_statements.md)

[Show Source](../../_sources/user-guide/sql/prepared_statements.md.txt)

---
# Special Functions[#](#special-functions "Link to this heading")

## Expansion Functions[#](#expansion-functions "Link to this heading")

* [unnest](#unnest)
* [unnest(struct)](#unnest-struct)

### `unnest`[#](#unnest "Link to this heading")

Expands an array or map into rows.

#### Arguments[#](#arguments "Link to this heading")

* **array**: Array expression to unnest.
  Can be a constant, column, or function, and any combination of array operators.

#### Examples[#](#examples "Link to this heading")

```
> select unnest(make_array(1, 2, 3, 4, 5)) as unnested;
+----------+
| unnested |
+----------+
| 1        |
| 2        |
| 3        |
| 4        |
| 5        |
+----------+
```

```
> select unnest(range(0, 10)) as unnested_range;
+----------------+
| unnested_range |
+----------------+
| 0              |
| 1              |
| 2              |
| 3              |
| 4              |
| 5              |
| 6              |
| 7              |
| 8              |
| 9              |
+----------------+
```

### `unnest (struct)`[#](#unnest-struct "Link to this heading")

Expand a struct fields into individual columns.
Each field of the struct will be prefixed with `__unnest_placeholder` and could be accessed via `"__unnest_placeholder(<struct>).<field>"`.

#### Arguments[#](#id1 "Link to this heading")

* **struct**: Object expression to unnest.
  Can be a constant, column, or function, and any combination of object operators.

#### Examples[#](#id2 "Link to this heading")

```
> create table foo as values ({a: 5, b: 'a string'}), ({a:6, b: 'another string'});

> create view foov as select column1 as struct_column from foo;

> select * from foov;
+---------------------------+
| struct_column             |
+---------------------------+
| {a: 5, b: a string}       |
| {a: 6, b: another string} |
+---------------------------+

> select unnest(struct_column) from foov;
+--------------------------------------------+--------------------------------------------+
| __unnest_placeholder(foov.struct_column).a | __unnest_placeholder(foov.struct_column).b |
+--------------------------------------------+--------------------------------------------+
| 5                                          | a string                                   |
| 6                                          | another string                             |
+--------------------------------------------+--------------------------------------------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/special_functions.md)

[Show Source](../../_sources/user-guide/sql/special_functions.md.txt)

---
# SQL Reference[#](#sql-reference "Link to this heading")

* [Data Types](data_types.html)
  * [Character Types](data_types.html#character-types)
  * [Numeric Types](data_types.html#numeric-types)
  * [Date/Time Types](data_types.html#date-time-types)
  * [Boolean Types](data_types.html#boolean-types)
  * [Binary Types](data_types.html#binary-types)
  * [Unsupported SQL Types](data_types.html#unsupported-sql-types)
* [Struct Type Coercion and Field Mapping](struct_coercion.html)
  * [Overview: Name-Based vs Positional Mapping](struct_coercion.html#overview-name-based-vs-positional-mapping)
  * [Coercion Paths Using Name-Based Matching](struct_coercion.html#coercion-paths-using-name-based-matching)
  * [NULL Handling for Missing Fields](struct_coercion.html#null-handling-for-missing-fields)
  * [Comparison and Ordering](struct_coercion.html#comparison-and-ordering)
  * [Migration Guide: From Positional to Name-Based Matching](struct_coercion.html#migration-guide-from-positional-to-name-based-matching)
  * [Best Practices](struct_coercion.html#best-practices)
  * [Error Messages and Troubleshooting](struct_coercion.html#error-messages-and-troubleshooting)
  * [Related Functions](struct_coercion.html#related-functions)
* [SELECT syntax](select.html)
  * [WITH clause](select.html#with-clause)
  * [SELECT clause](select.html#select-clause)
  * [FROM clause](select.html#from-clause)
  * [WHERE clause](select.html#where-clause)
  * [JOIN clause](select.html#join-clause)
  * [GROUP BY clause](select.html#group-by-clause)
  * [HAVING clause](select.html#having-clause)
  * [QUALIFY clause](select.html#qualify-clause)
  * [UNION clause](select.html#union-clause)
  * [ORDER BY clause](select.html#order-by-clause)
  * [LIMIT clause](select.html#limit-clause)
  * [EXCLUDE and EXCEPT clause](select.html#exclude-and-except-clause)
  * [Pipe operators](select.html#pipe-operators)
* [Subqueries](subqueries.html)
  * [Subquery operators](subqueries.html#subquery-operators)
  * [SELECT clause subqueries](subqueries.html#select-clause-subqueries)
  * [FROM clause subqueries](subqueries.html#from-clause-subqueries)
  * [WHERE clause subqueries](subqueries.html#where-clause-subqueries)
  * [HAVING clause subqueries](subqueries.html#having-clause-subqueries)
  * [Subquery categories](subqueries.html#subquery-categories)
* [DDL](ddl.html)
  * [CREATE DATABASE](ddl.html#create-database)
  * [CREATE SCHEMA](ddl.html#create-schema)
  * [CREATE EXTERNAL TABLE](ddl.html#create-external-table)
  * [CREATE TABLE](ddl.html#create-table)
  * [DROP TABLE](ddl.html#drop-table)
  * [CREATE VIEW](ddl.html#create-view)
  * [DROP VIEW](ddl.html#drop-view)
  * [DESCRIBE](ddl.html#describe)
* [DML](dml.html)
  * [COPY](dml.html#copy)
  * [INSERT](dml.html#insert)
* [EXPLAIN](explain.html)
  * [Syntax](explain.html#syntax)
  * [`EXPLAIN`](explain.html#id1)
  * [`EXPLAIN ANALYZE`](explain.html#explain-analyze)
* [Information Schema](information_schema.html)
  * [`SHOW TABLES`](information_schema.html#show-tables)
  * [`SHOW COLUMNS`](information_schema.html#show-columns)
  * [`SHOW ALL` (configuration options)](information_schema.html#show-all-configuration-options)
  * [`SHOW FUNCTIONS`](information_schema.html#show-functions)
* [Operators and Literals](operators.html)
  * [Numerical Operators](operators.html#numerical-operators)
  * [Comparison Operators](operators.html#comparison-operators)
  * [Logical Operators](operators.html#logical-operators)
  * [Bitwise Operators](operators.html#bitwise-operators)
  * [Other Operators](operators.html#other-operators)
  * [Literals](operators.html#literals)
* [Aggregate Functions](aggregate_functions.html)
  * [Filter clause](aggregate_functions.html#filter-clause)
  * [WITHIN GROUP / Ordered-set aggregates](aggregate_functions.html#within-group-ordered-set-aggregates)
  * [General Functions](aggregate_functions.html#general-functions)
  * [Statistical Functions](aggregate_functions.html#statistical-functions)
  * [Approximate Functions](aggregate_functions.html#approximate-functions)
* [Window Functions](window_functions.html)
  * [Syntax](window_functions.html#syntax)
  * [Filter clause for aggregate window functions](window_functions.html#filter-clause-for-aggregate-window-functions)
  * [Aggregate functions](window_functions.html#aggregate-functions)
  * [Ranking Functions](window_functions.html#ranking-functions)
  * [Analytical Functions](window_functions.html#analytical-functions)
* [Scalar Functions](scalar_functions.html)
  * [Math Functions](scalar_functions.html#math-functions)
  * [Conditional Functions](scalar_functions.html#conditional-functions)
  * [String Functions](scalar_functions.html#string-functions)
  * [Binary String Functions](scalar_functions.html#binary-string-functions)
  * [Regular Expression Functions](scalar_functions.html#regular-expression-functions)
  * [Time and Date Functions](scalar_functions.html#time-and-date-functions)
  * [Array Functions](scalar_functions.html#array-functions)
  * [Struct Functions](scalar_functions.html#struct-functions)
  * [Map Functions](scalar_functions.html#map-functions)
  * [Hashing Functions](scalar_functions.html#hashing-functions)
  * [Union Functions](scalar_functions.html#union-functions)
  * [Other Functions](scalar_functions.html#other-functions)
* [Special Functions](special_functions.html)
  * [Expansion Functions](special_functions.html#expansion-functions)
* [Format Options](format_options.html)
  * [Specifying Options and Order of Precedence](format_options.html#specifying-options-and-order-of-precedence)
* [Available Options](format_options.html#available-options)
  * [JSON Format Options](format_options.html#json-format-options)
  * [CSV Format Options](format_options.html#csv-format-options)
  * [Parquet Format Options](format_options.html#parquet-format-options)
* [Prepared Statements](prepared_statements.html)
  * [Inferred Types](prepared_statements.html#inferred-types)
  * [Positional Arguments](prepared_statements.html#positional-arguments)

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/index.rst)

[Show Source](../../_sources/user-guide/sql/index.rst.txt)

---
# Operators and Literals[#](#operators-and-literals "Link to this heading")

## Numerical Operators[#](#numerical-operators "Link to this heading")

* [+ (plus)](#op-plus)
* [- (minus)](#op-minus)
* [\* (multiply)](#op-multiply)
* [/ (divide)](#op-divide)
* [% (modulo)](#op-modulo)

### `+`[#](#op-plus "Link to this heading")

Addition

```
> SELECT 1 + 2;
+---------------------+
| Int64(1) + Int64(2) |
+---------------------+
| 3                   |
+---------------------+
```

### `-`[#](#op-minus "Link to this heading")

Subtraction

```
> SELECT 4 - 3;
+---------------------+
| Int64(4) - Int64(3) |
+---------------------+
| 1                   |
+---------------------+
```

### `*`[#](#op-multiply "Link to this heading")

Multiplication

```
> SELECT 2 * 3;
+---------------------+
| Int64(2) * Int64(3) |
+---------------------+
| 6                   |
+---------------------+
```

### `/`[#](#op-divide "Link to this heading")

Division (integer division truncates toward zero)

```
> SELECT 8 / 4;
+---------------------+
| Int64(8) / Int64(4) |
+---------------------+
| 2                   |
+---------------------+
```

### `%`[#](#op-modulo "Link to this heading")

Modulo (remainder)

```
> SELECT 7 % 3;
+---------------------+
| Int64(7) % Int64(3) |
+---------------------+
| 1                   |
+---------------------+
```

## Comparison Operators[#](#comparison-operators "Link to this heading")

* [= (equal)](#op-eq)
* [!= (not equal)](#op-neq)
* [< (less than)](#op-lt)
* [<= (less than or equal to)](#op-le)
* [> (greater than)](#op-gt)
* [>= (greater than or equal to)](#op-ge)
* [<=> (three-way comparison, alias for IS NOT DISTINCT FROM)](#op-spaceship)
* [IS DISTINCT FROM](#is-distinct-from)
* [IS NOT DISTINCT FROM](#is-not-distinct-from)
* [~ (regex match)](#op-re-match)
* [~\* (regex case-insensitive match)](#op-re-match-i)
* [!~ (not regex match)](#op-re-not-match)
* [!~\* (not regex case-insensitive match)](#op-re-not-match-i)

### `=`[#](#op-eq "Link to this heading")

Equal

```
> SELECT 1 = 1;
+---------------------+
| Int64(1) = Int64(1) |
+---------------------+
| true                |
+---------------------+
```

### `!=`[#](#op-neq "Link to this heading")

Not Equal

```
> SELECT 1 != 2;
+----------------------+
| Int64(1) != Int64(2) |
+----------------------+
| true                 |
+----------------------+
```

### `<`[#](#op-lt "Link to this heading")

Less Than

```
> SELECT 3 < 4;
+---------------------+
| Int64(3) < Int64(4) |
+---------------------+
| true                |
+---------------------+
```

### `<=`[#](#op-le "Link to this heading")

Less Than or Equal To

```
> SELECT 3 <= 3;
+----------------------+
| Int64(3) <= Int64(3) |
+----------------------+
| true                 |
+----------------------+
```

### `>`[#](#op-gt "Link to this heading")

Greater Than

```
> SELECT 6 > 5;
+---------------------+
| Int64(6) > Int64(5) |
+---------------------+
| true                |
+---------------------+
```

### `>=`[#](#op-ge "Link to this heading")

Greater Than or Equal To

```
> SELECT 5 >= 5;
+----------------------+
| Int64(5) >= Int64(5) |
+----------------------+
| true                 |
+----------------------+
```

### `<=>`[#](#op-spaceship "Link to this heading")

Three-way comparison operator. A NULL-safe operator that returns true if both operands are equal or both are NULL, false otherwise.

```
> SELECT NULL <=> NULL;
+--------------------------------+
| NULL IS NOT DISTINCT FROM NULL |
+--------------------------------+
| true                           |
+--------------------------------+
```

```
> SELECT 1 <=> NULL;
+------------------------------------+
| Int64(1) IS NOT DISTINCT FROM NULL |
+------------------------------------+
| false                              |
+------------------------------------+
```

```
> SELECT 1 <=> 2;
+----------------------------------------+
| Int64(1) IS NOT DISTINCT FROM Int64(2) |
+----------------------------------------+
| false                                  |
+----------------------------------------+
```

```
> SELECT 1 <=> 1;
+----------------------------------------+
| Int64(1) IS NOT DISTINCT FROM Int64(1) |
+----------------------------------------+
| true                                   |
+----------------------------------------+
```

### `IS DISTINCT FROM`[#](#is-distinct-from "Link to this heading")

Guarantees the result of a comparison is `true` or `false` and not an empty set

```
> SELECT 0 IS DISTINCT FROM NULL;
+--------------------------------+
| Int64(0) IS DISTINCT FROM NULL |
+--------------------------------+
| true                           |
+--------------------------------+
```

### `IS NOT DISTINCT FROM`[#](#is-not-distinct-from "Link to this heading")

The negation of `IS DISTINCT FROM`

```
> SELECT NULL IS NOT DISTINCT FROM NULL;
+--------------------------------+
| NULL IS NOT DISTINCT FROM NULL |
+--------------------------------+
| true                           |
+--------------------------------+
```

### `~`[#](#op-re-match "Link to this heading")

Regex Match

```
> SELECT 'datafusion' ~ '^datafusion(-cli)*';
+-------------------------------------------------+
| Utf8("datafusion") ~ Utf8("^datafusion(-cli)*") |
+-------------------------------------------------+
| true                                            |
+-------------------------------------------------+
```

### `~*`[#](#op-re-match-i "Link to this heading")

Regex Case-Insensitive Match

```
> SELECT 'datafusion' ~* '^DATAFUSION(-cli)*';
+--------------------------------------------------+
| Utf8("datafusion") ~* Utf8("^DATAFUSION(-cli)*") |
+--------------------------------------------------+
| true                                             |
+--------------------------------------------------+
```

### `!~`[#](#op-re-not-match "Link to this heading")

Not Regex Match

```
> SELECT 'datafusion' !~ '^DATAFUSION(-cli)*';
+--------------------------------------------------+
| Utf8("datafusion") !~ Utf8("^DATAFUSION(-cli)*") |
+--------------------------------------------------+
| true                                             |
+--------------------------------------------------+
```

### `!~*`[#](#op-re-not-match-i "Link to this heading")

Not Regex Case-Insensitive Match

```
> SELECT 'datafusion' !~* '^DATAFUSION(-cli)+';
+---------------------------------------------------+
| Utf8("datafusion") !~* Utf8("^DATAFUSION(-cli)+") |
+---------------------------------------------------+
| true                                              |
+---------------------------------------------------+
```

### `~~`[#](#id17 "Link to this heading")

Like Match

```
SELECT 'datafusion' ~~ 'dat_f%n';
+---------------------------------------+
| Utf8("datafusion") ~~ Utf8("dat_f%n") |
+---------------------------------------+
| true                                  |
+---------------------------------------+
```

### `~~*`[#](#id18 "Link to this heading")

Case-Insensitive Like Match

```
SELECT 'datafusion' ~~* 'Dat_F%n';
+----------------------------------------+
| Utf8("datafusion") ~~* Utf8("Dat_F%n") |
+----------------------------------------+
| true                                   |
+----------------------------------------+
```

### `!~~`[#](#id19 "Link to this heading")

Not Like Match

```
SELECT 'datafusion' !~~ 'Dat_F%n';
+----------------------------------------+
| Utf8("datafusion") !~~ Utf8("Dat_F%n") |
+----------------------------------------+
| true                                   |
+----------------------------------------+
```

### `!~~*`[#](#id20 "Link to this heading")

Not Case-Insensitive Like Match

```
SELECT 'datafusion' !~~* 'Dat%F_n';
+-----------------------------------------+
| Utf8("datafusion") !~~* Utf8("Dat%F_n") |
+-----------------------------------------+
| true                                    |
+-----------------------------------------+
```

## Logical Operators[#](#logical-operators "Link to this heading")

* [AND](#and)
* [OR](#or)

### `AND`[#](#and "Link to this heading")

Logical And

```
> SELECT true AND true;
+---------------------------------+
| Boolean(true) AND Boolean(true) |
+---------------------------------+
| true                            |
+---------------------------------+
```

### `OR`[#](#or "Link to this heading")

Logical Or

```
> SELECT false OR true;
+---------------------------------+
| Boolean(false) OR Boolean(true) |
+---------------------------------+
| true                            |
+---------------------------------+
```

## Bitwise Operators[#](#bitwise-operators "Link to this heading")

* [& (bitwise and)](#op-bit-and)
* [| (bitwise or)](#op-bit-or)
* [# (bitwise xor)](#op-bit-xor)
* [>> (bitwise shift right)](#op-shift-r)
* [<< (bitwise shift left)](#op-shift-l)

### `&`[#](#op-bit-and "Link to this heading")

Bitwise And

```
> SELECT 5 & 3;
+---------------------+
| Int64(5) & Int64(3) |
+---------------------+
| 1                   |
+---------------------+
```

### `|`[#](#op-bit-or "Link to this heading")

Bitwise Or

```
> SELECT 5 | 3;
+---------------------+
| Int64(5) | Int64(3) |
+---------------------+
| 7                   |
+---------------------+
```

### `#`[#](#op-bit-xor "Link to this heading")

Bitwise Xor (interchangeable with `^`)

```
> SELECT 5 # 3;
+---------------------+
| Int64(5) # Int64(3) |
+---------------------+
| 6                   |
+---------------------+
```

### `>>`[#](#op-shift-r "Link to this heading")

Bitwise Shift Right

```
> SELECT 5 >> 3;
+----------------------+
| Int64(5) >> Int64(3) |
+----------------------+
| 0                    |
+----------------------+
```

### `<<`[#](#op-shift-l "Link to this heading")

Bitwise Shift Left

```
> SELECT 5 << 3;
+----------------------+
| Int64(5) << Int64(3) |
+----------------------+
| 40                   |
+----------------------+
```

## Other Operators[#](#other-operators "Link to this heading")

* [|| (string concatenation)](#op-str-cat)
* [@> (array contains)](#op-arr-contains)
* [<@ (array is contained by)](#op-arr-contained-by)

### `||`[#](#op-str-cat "Link to this heading")

String Concatenation

```
> SELECT 'Hello, ' || 'DataFusion!';
+----------------------------------------+
| Utf8("Hello, ") || Utf8("DataFusion!") |
+----------------------------------------+
| Hello, DataFusion!                     |
+----------------------------------------+
```

### `@>`[#](#op-arr-contains "Link to this heading")

Array Contains

```
> SELECT make_array(1,2,3) @> make_array(1,3);
+-------------------------------------------------------------------------+
| make_array(Int64(1),Int64(2),Int64(3)) @> make_array(Int64(1),Int64(3)) |
+-------------------------------------------------------------------------+
| true                                                                    |
+-------------------------------------------------------------------------+
```

### `<@`[#](#op-arr-contained-by "Link to this heading")

Array Is Contained By

```
> SELECT make_array(1,3) <@ make_array(1,2,3);
+-------------------------------------------------------------------------+
| make_array(Int64(1),Int64(3)) <@ make_array(Int64(1),Int64(2),Int64(3)) |
+-------------------------------------------------------------------------+
| true                                                                    |
+-------------------------------------------------------------------------+
```

## Literals[#](#literals "Link to this heading")

Use single quotes for literal values. For example, the string `foo bar` is
referred to using `'foo bar'`

```
select 'foo';
```

### Escaping[#](#escaping "Link to this heading")

Unlike many other languages, SQL literals do not by default support C-style escape
sequences such as `\n` for newline. Instead all characters in a `'` string are treated
literally.

To escape `'` in SQL literals, use `''`:

```
> select 'it''s escaped';
+----------------------+
| Utf8("it's escaped") |
+----------------------+
| it's escaped         |
+----------------------+
1 row(s) fetched.
```

Strings such as `foo\nbar` mean `\` followed by `n` (not newline):

```
> select 'foo\nbar';
+------------------+
| Utf8("foo\nbar") |
+------------------+
| foo\nbar         |
+------------------+
1 row(s) fetched.
Elapsed 0.005 seconds.
```

To add escaped characters such as newline or tab, instead of `\n` you use the
`E` style strings. For example, to add the text with a newline

```
foo
bar
```

You can use `E'foo\nbar'`

```
> select E'foo\nbar';
+-----------------+
| Utf8("foo
bar") |
+-----------------+
| foo
bar         |
+-----------------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/operators.md)

[Show Source](../../_sources/user-guide/sql/operators.md.txt)

---
# Example Usage[#](#example-usage "Link to this heading")

In this example some simple processing is performed on the [`example.csv`](https://github.com/apache/datafusion/blob/main/datafusion/core/tests/data/example.csv) file.

Even [`more code examples`](https://github.com/apache/datafusion/tree/main/datafusion-examples) attached to the project.

## Add published DataFusion dependency[#](#add-published-datafusion-dependency "Link to this heading")

Find latest available Datafusion version on [DataFusion’s
crates.io](https://crates.io/crates/datafusion) page. Add the dependency to your `Cargo.toml` file:

```
datafusion = "53.0.0"
tokio = { version = "1.0", features = ["rt-multi-thread"] }
```

## Run a SQL query against data stored in a CSV[#](#run-a-sql-query-against-data-stored-in-a-csv "Link to this heading")

```
use datafusion::prelude::*;

#[tokio::main]
async fn main() -> datafusion::error::Result<()> {
  // register the table
  let ctx = SessionContext::new();
  ctx.register_csv("example", "tests/data/example.csv", CsvReadOptions::new()).await?;

  // create a plan to run a SQL query
  let df = ctx.sql("SELECT a, MIN(b) FROM example WHERE a <= b GROUP BY a LIMIT 100").await?;

  // execute and print results
  df.show().await?;
  Ok(())
}
```

See [the SQL API](../library-user-guide/using-the-sql-api.html) section of the
library guide for more information on the SQL API.

## Use the DataFrame API to process data stored in a CSV[#](#use-the-dataframe-api-to-process-data-stored-in-a-csv "Link to this heading")

```
use datafusion::prelude::*;
use datafusion::functions_aggregate::expr_fn::min;

#[tokio::main]
async fn main() -> datafusion::error::Result<()> {
  // create the dataframe
  let ctx = SessionContext::new();
  let df = ctx.read_csv("tests/data/example.csv", CsvReadOptions::new()).await?;

  let df = df.filter(col("a").lt_eq(col("b")))?
           .aggregate(vec![col("a")], vec![min(col("b"))])?
           .limit(0, Some(100))?;

  // execute and print results
  df.show().await?;
  Ok(())
}
```

## Output from both examples[#](#output-from-both-examples "Link to this heading")

```
+---+--------+
| a | MIN(b) |
+---+--------+
| 1 | 2      |
+---+--------+
```

## Arrow Versions[#](#arrow-versions "Link to this heading")

Many of DataFusion’s public APIs use types from the
[`arrow`](https://docs.rs/arrow/latest/arrow/) and [`parquet`](https://docs.rs/parquet/latest/parquet/) crates, so if you use
`arrow` in your project, the `arrow` version must match that used by
DataFusion. You can check the required version on [DataFusion’s
crates.io](https://crates.io/crates/datafusion) page.

The easiest way to ensure the versions match is to use the `arrow`
exported by DataFusion, for example:

```
use datafusion::arrow::datatypes::Schema;
```

For example, [DataFusion `26.0.0` dependencies](https://crates.io/crates/datafusion/26.0.0/dependencies) require `arrow`
`40.0.0`. If instead you used `arrow` `41.0.0` in your project you may
see errors such as:

```
mismatched types [E0308] expected `Schema`, found `arrow_schema::Schema` Note: `arrow_schema::Schema` and `Schema` have similar names, but are actually distinct types Note: `arrow_schema::Schema` is defined in crate `arrow_schema` Note: `Schema` is defined in crate `arrow_schema` Note: perhaps two different versions of crate `arrow_schema` are being used? Note: associated function defined here
```

Or calling `downcast_ref` on an `ArrayRef` may return `None`
unexpectedly.

## Identifiers and Capitalization[#](#identifiers-and-capitalization "Link to this heading")

Please be aware that all identifiers are effectively made lower-case in SQL, so if your csv file has capital letters (ex: `Name`) you must put your column name in double quotes or the examples won’t work.

To illustrate this behavior, consider the [`capitalized_example.csv`](../_downloads/3cce4d737d8c5814f5b50d859d21ba53/capitalized_example.csv) file:

## Run a SQL query against data stored in a CSV:[#](#id1 "Link to this heading")

```
use datafusion::prelude::*;

#[tokio::main]
async fn main() -> datafusion::error::Result<()> {
  // register the table
  let ctx = SessionContext::new();
  ctx.register_csv("example", "tests/data/capitalized_example.csv", CsvReadOptions::new()).await?;

  // create a plan to run a SQL query
  let df = ctx.sql("SELECT \"A\", MIN(b) FROM example WHERE \"A\" <= c GROUP BY \"A\" LIMIT 100").await?;

  // execute and print results
  df.show().await?;
  Ok(())
}
```

## Use the DataFrame API to process data stored in a CSV:[#](#id2 "Link to this heading")

```
use datafusion::prelude::*;
use datafusion::functions_aggregate::expr_fn::min;

#[tokio::main]
async fn main() -> datafusion::error::Result<()> {
  // create the dataframe
  let ctx = SessionContext::new();
  let df = ctx.read_csv("tests/data/capitalized_example.csv", CsvReadOptions::new()).await?;

  let df = df
      // col will parse the input string, hence requiring double quotes to maintain the capitalization
      .filter(col("\"A\"").lt_eq(col("c")))?
      // alternatively use ident to pass in an unqualified column name directly without parsing
      .aggregate(vec![ident("A")], vec![min(col("b"))])?
      .limit(0, Some(100))?;

  // execute and print results
  df.show().await?;
  Ok(())
}
```

## Output from both examples[#](#id3 "Link to this heading")

```
+---+--------+
| A | MIN(b) |
+---+--------+
| 2 | 1      |
| 1 | 2      |
+---+--------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/example-usage.md)

[Show Source](../_sources/user-guide/example-usage.md.txt)

---
# CLI Specific Functions[#](#cli-specific-functions "Link to this heading")

`datafusion-cli` comes with build-in functions that are not included in the
DataFusion SQL engine by default. These functions are:

## `parquet_metadata`[#](#parquet-metadata "Link to this heading")

The `parquet_metadata` table function can be used to inspect detailed metadata
about a parquet file such as statistics, sizes, and other information. This can
be helpful to understand how parquet files are structured.

For example, to see information about the `"WatchID"` column in the
`hits.parquet` file, you can use:

```
SELECT path_in_schema, row_group_id, row_group_num_rows, stats_min, stats_max, total_compressed_size
FROM parquet_metadata('hits.parquet')
WHERE path_in_schema = '"WatchID"'
LIMIT 3;

+----------------+--------------+--------------------+---------------------+---------------------+-----------------------+
| path_in_schema | row_group_id | row_group_num_rows | stats_min           | stats_max           | total_compressed_size |
+----------------+--------------+--------------------+---------------------+---------------------+-----------------------+
| "WatchID"      | 0            | 450560             | 4611687214012840539 | 9223369186199968220 | 3883759               |
| "WatchID"      | 1            | 612174             | 4611689135232456464 | 9223371478009085789 | 5176803               |
| "WatchID"      | 2            | 344064             | 4611692774829951781 | 9223363791697310021 | 3031680               |
+----------------+--------------+--------------------+---------------------+---------------------+-----------------------+
3 rows in set. Query took 0.053 seconds.
```

The returned table has the following columns for each row for each column chunk
in the file. Please refer to the [Parquet Documentation](https://parquet.apache.org/) for more information in
the meaning of these fields.

| column\_name | data\_type | Description |
| --- | --- | --- |
| filename | Utf8 | Name of the file |
| row\_group\_id | Int64 | Row group index the column chunk belongs to |
| row\_group\_num\_rows | Int64 | Count of rows stored in the row group |
| row\_group\_num\_columns | Int64 | Total number of columns in the row group (same for all row groups) |
| row\_group\_bytes | Int64 | Number of bytes used to store the row group (not including metadata) |
| column\_id | Int64 | ID of the column |
| file\_offset | Int64 | Offset within the file that this column chunk’s data begins |
| num\_values | Int64 | Total number of values in this column chunk |
| path\_in\_schema | Utf8 | “Path” (column name) of the column chunk in the schema |
| type | Utf8 | Parquet data type of the column chunk |
| stats\_min | Utf8 | The minimum value for this column chunk, if stored in the statistics, cast to a string |
| stats\_max | Utf8 | The maximum value for this column chunk, if stored in the statistics, cast to a string |
| stats\_null\_count | Int64 | Number of null values in this column chunk, if stored in the statistics |
| stats\_distinct\_count | Int64 | Number of distinct values in this column chunk, if stored in the statistics |
| stats\_min\_value | Utf8 | Same as `stats_min` |
| stats\_max\_value | Utf8 | Same as `stats_max` |
| compression | Utf8 | Block level compression (e.g. `SNAPPY`) used for this column chunk |
| encodings | Utf8 | All block level encodings (e.g. `[PLAIN_DICTIONARY, PLAIN, RLE]`) used for this column chunk |
| index\_page\_offset | Int64 | Offset in the file of the [`page index`](https://github.com/apache/parquet-format/blob/master/PageIndex.md), if any |
| dictionary\_page\_offset | Int64 | Offset in the file of the dictionary page, if any |
| data\_page\_offset | Int64 | Offset in the file of the first data page, if any |
| total\_compressed\_size | Int64 | Number of bytes the column chunk’s data after encoding and compression (what is stored in the file) |
| total\_uncompressed\_size | Int64 | Number of bytes the column chunk’s data after encoding |

## `metadata_cache`[#](#metadata-cache "Link to this heading")

The `metadata_cache` function shows information about the default File Metadata Cache that is used by the
[`ListingTable`](https://docs.rs/datafusion/latest/datafusion/datasource/listing/struct.ListingTable.html) implementation in DataFusion. This cache is used to speed up
reading metadata from files when scanning directories with many files.

For example, after creating a table with the [CREATE EXTERNAL TABLE](../sql/ddl.html#create-external-table)
command:

```
> create external table hits
  stored as parquet
  location 's3://clickhouse-public-datasets/hits_compatible/athena_partitioned/';
```

You can inspect the metadata cache by querying the `metadata_cache` function:

```
> select * from metadata_cache();
+----------------------------------------------------+---------------------+-----------------+---------------------------------------+---------+---------------------+------+------------------+
| path                                               | file_modified       | file_size_bytes | e_tag                                 | version | metadata_size_bytes | hits | extra            |
+----------------------------------------------------+---------------------+-----------------+---------------------------------------+---------+---------------------+------+------------------+
| hits_compatible/athena_partitioned/hits_61.parquet | 2022-07-03T15:40:34 | 117270944       | "5db11cad1ca0d80d748fc92c914b010a-6"  | NULL    | 212949              | 0    | page_index=false |
| hits_compatible/athena_partitioned/hits_32.parquet | 2022-07-03T15:37:17 | 94506004        | "2f7db49a9fe242179590b615b94a39d2-5"  | NULL    | 278157              | 0    | page_index=false |
| hits_compatible/athena_partitioned/hits_40.parquet | 2022-07-03T15:38:07 | 142508647       | "9e5852b45a469d5a05bf270a286eab8a-8"  | NULL    | 212917              | 0    | page_index=false |
| hits_compatible/athena_partitioned/hits_93.parquet | 2022-07-03T15:44:07 | 127987774       | "751100bf0dac7d489b9836abf3108b99-7"  | NULL    | 278318              | 0    | page_index=false |
| .                                                                                                                                                                                            |
+----------------------------------------------------+---------------------+-----------------+---------------------------------------+---------+---------------------+------+------------------+
```

Since `metadata_cache` is a normal table function, you can use it in most places you can use
a table reference.

For example, to get the total size consumed by the cached entries:

```
> select sum(metadata_size_bytes) from metadata_cache();
+-------------------------------------------+
| sum(metadata_cache().metadata_size_bytes) |
+-------------------------------------------+
| 22972345                                  |
+-------------------------------------------+
```

The columns of the returned table are:

| column\_name | data\_type | Description |
| --- | --- | --- |
| path | Utf8 | File path relative to the object store / filesystem root |
| file\_modified | Timestamp | Last modified time of the file |
| file\_size\_bytes | UInt64 | Size of the file in bytes |
| e\_tag | Utf8 | [Entity Tag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) (ETag) of the file if available |
| version | Utf8 | Version of the file if available (for object stores that support versioning) |
| metadata\_size\_bytes | UInt64 | Size of the cached metadata in memory (not its thrift encoded form) |
| hits | UInt64 | Number of times the cached metadata has been accessed |
| extra | Utf8 | Extra information about the cached metadata (e.g., if page index information is included) |

## `statistics_cache`[#](#statistics-cache "Link to this heading")

Similarly to the `metadata_cache`, the `statistics_cache` function can be used to show information
about the File Statistics Cache that is used by the [`ListingTable`](https://docs.rs/datafusion/latest/datafusion/datasource/listing/struct.ListingTable.html) implementation in DataFusion.
For the statistics to be collected, the config `datafusion.execution.collect_statistics` must be
enabled.

You can inspect the statistics cache by querying the `statistics_cache` function. For example:

```
> select * from statistics_cache();
+------------------+---------------------+-----------------+------------------------+---------+-----------------+-------------+--------------------+-----------------------+
| path             | file_modified       | file_size_bytes | e_tag                  | version | num_rows        | num_columns | table_size_bytes   | statistics_size_bytes |
+------------------+---------------------+-----------------+------------------------+---------+-----------------+-------------+--------------------+-----------------------+
| .../hits.parquet | 2022-06-25T22:22:22 | 14779976446     | 0-5e24d1ee16380-370f48 | NULL    | Exact(99997497) | 105         | Exact(36445943240) | 0                     |
+------------------+---------------------+-----------------+------------------------+---------+-----------------+-------------+--------------------+-----------------------+
```

The columns of the returned table are:

| column\_name | data\_type | Description |
| --- | --- | --- |
| path | Utf8 | File path relative to the object store / filesystem root |
| file\_modified | Timestamp | Last modified time of the file |
| file\_size\_bytes | UInt64 | Size of the file in bytes |
| e\_tag | Utf8 | [Entity Tag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) (ETag) of the file if available |
| version | Utf8 | Version of the file if available (for object stores that support versioning) |
| num\_rows | Utf8 | Number of rows in the table |
| num\_columns | UInt64 | Number of columns in the table |
| table\_size\_bytes | Utf8 | Size of the table, in bytes |
| statistics\_size\_bytes | UInt64 | Size of the cached statistics in memory |

## `list_files_cache`[#](#list-files-cache "Link to this heading")

The `list_files_cache` function shows information about the `ListFilesCache` that is used by the [`ListingTable`](https://docs.rs/datafusion/latest/datafusion/datasource/listing/struct.ListingTable.html) implementation in DataFusion. When creating a [`ListingTable`](https://docs.rs/datafusion/latest/datafusion/datasource/listing/struct.ListingTable.html), DataFusion lists the files in the table’s location and caches results in the `ListFilesCache`. Subsequent queries against the same table can reuse this cached information instead of re-listing the files. Cache entries are scoped to tables.

You can inspect the cache by querying the `list_files_cache` function. For example,

```
> set datafusion.runtime.list_files_cache_ttl = "30s";
> create external table overturemaps
stored as parquet
location 's3://overturemaps-us-west-2/release/2025-12-17.0/theme=base/type=infrastructure';
0 row(s) fetched.
> select table, path, metadata_size_bytes, expires_in, unnest(metadata_list)['file_size_bytes'] as file_size_bytes, unnest(metadata_list)['e_tag'] as e_tag from list_files_cache() limit 10;
+--------------+-----------------------------------------------------+---------------------+-----------------------------------+-----------------+---------------------------------------+
| table        | path                                                | metadata_size_bytes | expires_in                        | file_size_bytes | e_tag                                 |
+--------------+-----------------------------------------------------+---------------------+-----------------------------------+-----------------+---------------------------------------+
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 999055952       | "35fc8fbe8400960b54c66fbb408c48e8-60" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 975592768       | "8a16e10b722681cdc00242564b502965-59" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 1082925747      | "24cd13ddb5e0e438952d2499f5dabe06-65" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 1008425557      | "37663e31c7c64d4ef355882bcd47e361-61" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 1065561905      | "4e7c50d2d1b3c5ed7b82b4898f5ac332-64" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 1045655427      | "8fff7e6a72d375eba668727c55d4f103-63" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 1086822683      | "b67167d8022d778936c330a52a5f1922-65" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 1016732378      | "6d70857a0473ed9ed3fc6e149814168b-61" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 991363784       | "c9cafb42fcbb413f851691c895dd7c2b-60" |
| overturemaps | release/2025-12-17.0/theme=base/type=infrastructure | 2750                | 0 days 0 hours 0 mins 25.264 secs | 1032469715      | "7540252d0d67158297a67038a3365e0f-62" |
+--------------+-----------------------------------------------------+---------------------+-----------------------------------+-----------------+---------------------------------------+
```

The columns of the returned table are:

| column\_name | data\_type | Description |
| --- | --- | --- |
| table | Utf8 | Name of the table |
| path | Utf8 | File path relative to the object store / filesystem root |
| metadata\_size\_bytes | UInt64 | Size of the cached metadata in memory (not its thrift encoded form) |
| expires\_in | Duration(ms) | Last modified time of the file |
| metadata\_list | List(Struct) | List of metadatas, one for each file under the path. |

A metadata struct in the metadata\_list contains the following fields:

```
{
  "file_path": "release/2025-12-17.0/theme=base/type=infrastructure/part-00000-d556e455-e0c5-4940-b367-daff3287a952-c000.zstd.parquet",
  "file_modified": "2025-12-17T22:20:29",
  "file_size_bytes": 999055952,
  "e_tag": "35fc8fbe8400960b54c66fbb408c48e8-60",
  "version": null
}
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/cli/functions.md)

[Show Source](../../_sources/user-guide/cli/functions.md.txt)

---
# Configuration Settings[#](#configuration-settings "Link to this heading")

DataFusion configurations control various aspects of DataFusion planning and execution

## Setting Configuration Options[#](#setting-configuration-options "Link to this heading")

### Programmatically[#](#programmatically "Link to this heading")

You can set the options programmatically via the [`ConfigOptions`](https://docs.rs/datafusion/latest/datafusion/common/config/struct.ConfigOptions.html) object. For
example, to configure the `datafusion.execution.target_partitions` using the API:

```
use datafusion::common::config::ConfigOptions;
let mut config = ConfigOptions::new();
config.execution.target_partitions = 1;
```

### Via Environment Variables[#](#via-environment-variables "Link to this heading")

You can also set configuration options via environment variables using
[`ConfigOptions::from_env`](https://docs.rs/datafusion/latest/datafusion/common/config/struct.ConfigOptions.html#method.from_env), for example

```
DATAFUSION_EXECUTION_TARGET_PARTITIONS=1 ./your_program
```

### Via SQL[#](#via-sql "Link to this heading")

You can also set configuration options via SQL using the `SET` command. For
example, to configure `datafusion.execution.target_partitions`:

```
SET datafusion.execution.target_partitions = '1';
```

The following configuration settings are available:

| key | default | description |
| --- | --- | --- |
| datafusion.catalog.create\_default\_catalog\_and\_schema | true | Whether the default catalog and schema should be created automatically. |
| datafusion.catalog.default\_catalog | datafusion | The default catalog name - this impacts what SQL queries use if not specified |
| datafusion.catalog.default\_schema | public | The default schema name - this impacts what SQL queries use if not specified |
| datafusion.catalog.information\_schema | false | Should DataFusion provide access to `information_schema` virtual tables for displaying schema information |
| datafusion.catalog.location | NULL | Location scanned to load tables for `default` schema |
| datafusion.catalog.format | NULL | Type of `TableProvider` to use when loading `default` schema |
| datafusion.catalog.has\_header | true | Default value for `format.has_header` for `CREATE EXTERNAL TABLE` if not specified explicitly in the statement. |
| datafusion.catalog.newlines\_in\_values | false | Specifies whether newlines in (quoted) CSV values are supported. This is the default value for `format.newlines_in_values` for `CREATE EXTERNAL TABLE` if not specified explicitly in the statement. Parsing newlines in quoted values may be affected by execution behaviour such as parallel file scanning. Setting this to `true` ensures that newlines in values are parsed successfully, which may reduce performance. |
| datafusion.execution.batch\_size | 8192 | Default batch size while creating new batches, it’s especially useful for buffer-in-memory batches since creating tiny batches would result in too much metadata memory consumption |
| datafusion.execution.perfect\_hash\_join\_small\_build\_threshold | 1024 | A perfect hash join (see `HashJoinExec` for more details) will be considered if the range of keys (max - min) on the build side is < this threshold. This provides a fast path for joins with very small key ranges, bypassing the density check. Currently only supports cases where build\_side.num\_rows() < u32::MAX. Support for build\_side.num\_rows() >= u32::MAX will be added in the future. |
| datafusion.execution.perfect\_hash\_join\_min\_key\_density | 0.15 | The minimum required density of join keys on the build side to consider a perfect hash join (see `HashJoinExec` for more details). Density is calculated as: `(number of rows) / (max_key - min_key + 1)`. A perfect hash join may be used if the actual key density > this value. Currently only supports cases where build\_side.num\_rows() < u32::MAX. Support for build\_side.num\_rows() >= u32::MAX will be added in the future. |
| datafusion.execution.coalesce\_batches | true | When set to true, record batches will be examined between each operator and small batches will be coalesced into larger batches. This is helpful when there are highly selective filters or joins that could produce tiny output batches. The target batch size is determined by the configuration setting |
| datafusion.execution.collect\_statistics | true | Should DataFusion collect statistics when first creating a table. Has no effect after the table is created. Applies to the default `ListingTableProvider` in DataFusion. Defaults to true. |
| datafusion.execution.target\_partitions | 0 | Number of partitions for query execution. Increasing partitions can increase concurrency. Defaults to the number of CPU cores on the system |
| datafusion.execution.time\_zone | NULL | The default time zone Some functions, e.g. `now` return timestamps in this time zone |
| datafusion.execution.parquet.enable\_page\_index | true | (reading) If true, reads the Parquet data page level metadata (the Page Index), if present, to reduce the I/O and number of rows decoded. |
| datafusion.execution.parquet.pruning | true | (reading) If true, the parquet reader attempts to skip entire row groups based on the predicate in the query and the metadata (min/max values) stored in the parquet file |
| datafusion.execution.parquet.skip\_metadata | true | (reading) If true, the parquet reader skip the optional embedded metadata that may be in the file Schema. This setting can help avoid schema conflicts when querying multiple parquet files with schemas containing compatible types but different metadata |
| datafusion.execution.parquet.metadata\_size\_hint | 524288 | (reading) If specified, the parquet reader will try and fetch the last `size_hint` bytes of the parquet file optimistically. If not specified, two reads are required: One read to fetch the 8-byte parquet footer and another to fetch the metadata length encoded in the footer Default setting to 512 KiB, which should be sufficient for most parquet files, it can reduce one I/O operation per parquet file. If the metadata is larger than the hint, two reads will still be performed. |
| datafusion.execution.parquet.pushdown\_filters | false | (reading) If true, filter expressions are be applied during the parquet decoding operation to reduce the number of rows decoded. This optimization is sometimes called “late materialization”. |
| datafusion.execution.parquet.reorder\_filters | false | (reading) If true, filter expressions evaluated during the parquet decoding operation will be reordered heuristically to minimize the cost of evaluation. If false, the filters are applied in the same order as written in the query |
| datafusion.execution.parquet.force\_filter\_selections | false | (reading) Force the use of RowSelections for filter results, when pushdown\_filters is enabled. If false, the reader will automatically choose between a RowSelection and a Bitmap based on the number and pattern of selected rows. |
| datafusion.execution.parquet.schema\_force\_view\_types | true | (reading) If true, parquet reader will read columns of `Utf8/Utf8Large` with `Utf8View`, and `Binary/BinaryLarge` with `BinaryView`. |
| datafusion.execution.parquet.binary\_as\_string | false | (reading) If true, parquet reader will read columns of `Binary/LargeBinary` with `Utf8`, and `BinaryView` with `Utf8View`. Parquet files generated by some legacy writers do not correctly set the UTF8 flag for strings, causing string columns to be loaded as BLOB instead. |
| datafusion.execution.parquet.coerce\_int96 | NULL | (reading) If true, parquet reader will read columns of physical type int96 as originating from a different resolution than nanosecond. This is useful for reading data from systems like Spark which stores microsecond resolution timestamps in an int96 allowing it to write values with a larger date range than 64-bit timestamps with nanosecond resolution. |
| datafusion.execution.parquet.bloom\_filter\_on\_read | true | (reading) Use any available bloom filters when reading parquet files |
| datafusion.execution.parquet.max\_predicate\_cache\_size | NULL | (reading) The maximum predicate cache size, in bytes. When `pushdown_filters` is enabled, sets the maximum memory used to cache the results of predicate evaluation between filter evaluation and output generation. Decreasing this value will reduce memory usage, but may increase IO and CPU usage. None means use the default parquet reader setting. 0 means no caching. |
| datafusion.execution.parquet.data\_pagesize\_limit | 1048576 | (writing) Sets best effort maximum size of data page in bytes |
| datafusion.execution.parquet.write\_batch\_size | 1024 | (writing) Sets write\_batch\_size in rows |
| datafusion.execution.parquet.writer\_version | 1.0 | (writing) Sets parquet writer version valid values are “1.0” and “2.0” |
| datafusion.execution.parquet.skip\_arrow\_metadata | false | (writing) Skip encoding the embedded arrow metadata in the KV\_meta This is analogous to the `ArrowWriterOptions::with_skip_arrow_metadata`. Refer to <https://docs.rs/parquet/53.3.0/parquet/arrow/arrow_writer/struct.ArrowWriterOptions.html#method.with_skip_arrow_metadata> |
| datafusion.execution.parquet.compression | zstd(3) | (writing) Sets default parquet compression codec. Valid values are: uncompressed, snappy, gzip(level), brotli(level), lz4, zstd(level), and lz4\_raw. These values are not case sensitive. If NULL, uses default parquet writer setting Note that this default setting is not the same as the default parquet writer setting. |
| datafusion.execution.parquet.dictionary\_enabled | true | (writing) Sets if dictionary encoding is enabled. If NULL, uses default parquet writer setting |
| datafusion.execution.parquet.dictionary\_page\_size\_limit | 1048576 | (writing) Sets best effort maximum dictionary page size, in bytes |
| datafusion.execution.parquet.statistics\_enabled | page | (writing) Sets if statistics are enabled for any column Valid values are: “none”, “chunk”, and “page” These values are not case sensitive. If NULL, uses default parquet writer setting |
| datafusion.execution.parquet.max\_row\_group\_size | 1048576 | (writing) Target maximum number of rows in each row group (defaults to 1M rows). Writing larger row groups requires more memory to write, but can get better compression and be faster to read. |
| datafusion.execution.parquet.created\_by | datafusion version 53.0.0 | (writing) Sets “created by” property |
| datafusion.execution.parquet.column\_index\_truncate\_length | 64 | (writing) Sets column index truncate length |
| datafusion.execution.parquet.statistics\_truncate\_length | 64 | (writing) Sets statistics truncate length. If NULL, uses default parquet writer setting |
| datafusion.execution.parquet.data\_page\_row\_count\_limit | 20000 | (writing) Sets best effort maximum number of rows in data page |
| datafusion.execution.parquet.encoding | NULL | (writing) Sets default encoding for any column. Valid values are: plain, plain\_dictionary, rle, bit\_packed, delta\_binary\_packed, delta\_length\_byte\_array, delta\_byte\_array, rle\_dictionary, and byte\_stream\_split. These values are not case sensitive. If NULL, uses default parquet writer setting |
| datafusion.execution.parquet.bloom\_filter\_on\_write | false | (writing) Write bloom filters for all columns when creating parquet files |
| datafusion.execution.parquet.bloom\_filter\_fpp | NULL | (writing) Sets bloom filter false positive probability. If NULL, uses default parquet writer setting |
| datafusion.execution.parquet.bloom\_filter\_ndv | NULL | (writing) Sets bloom filter number of distinct values. If NULL, uses default parquet writer setting |
| datafusion.execution.parquet.allow\_single\_file\_parallelism | true | (writing) Controls whether DataFusion will attempt to speed up writing parquet files by serializing them in parallel. Each column in each row group in each output file are serialized in parallel leveraging a maximum possible core count of n\_files*n\_row\_groups*n\_columns. |
| datafusion.execution.parquet.maximum\_parallel\_row\_group\_writers | 1 | (writing) By default parallel parquet writer is tuned for minimum memory usage in a streaming execution plan. You may see a performance benefit when writing large parquet files by increasing maximum\_parallel\_row\_group\_writers and maximum\_buffered\_record\_batches\_per\_stream if your system has idle cores and can tolerate additional memory usage. Boosting these values is likely worthwhile when writing out already in-memory data, such as from a cached data frame. |
| datafusion.execution.parquet.maximum\_buffered\_record\_batches\_per\_stream | 2 | (writing) By default parallel parquet writer is tuned for minimum memory usage in a streaming execution plan. You may see a performance benefit when writing large parquet files by increasing maximum\_parallel\_row\_group\_writers and maximum\_buffered\_record\_batches\_per\_stream if your system has idle cores and can tolerate additional memory usage. Boosting these values is likely worthwhile when writing out already in-memory data, such as from a cached data frame. |
| datafusion.execution.parquet.use\_content\_defined\_chunking | NULL | (writing) EXPERIMENTAL: Enable content-defined chunking (CDC) when writing parquet files. When `Some`, CDC is enabled with the given options; when `None` (the default), CDC is disabled. When CDC is enabled, parallel writing is automatically disabled since the chunker state must persist across row groups. |
| datafusion.execution.planning\_concurrency | 0 | Fan-out during initial physical planning. This is mostly use to plan `UNION` children in parallel. Defaults to the number of CPU cores on the system |
| datafusion.execution.skip\_physical\_aggregate\_schema\_check | false | When set to true, skips verifying that the schema produced by planning the input of `LogicalPlan::Aggregate` exactly matches the schema of the input plan. When set to false, if the schema does not match exactly (including nullability and metadata), a planning error will be raised. This is used to workaround bugs in the planner that are now caught by the new schema verification step. |
| datafusion.execution.spill\_compression | uncompressed | Sets the compression codec used when spilling data to disk. Since datafusion writes spill files using the Arrow IPC Stream format, only codecs supported by the Arrow IPC Stream Writer are allowed. Valid values are: uncompressed, lz4\_frame, zstd. Note: lz4\_frame offers faster (de)compression, but typically results in larger spill files. In contrast, zstd achieves higher compression ratios at the cost of slower (de)compression speed. |
| datafusion.execution.sort\_spill\_reservation\_bytes | 10485760 | Specifies the reserved memory for each spillable sort operation to facilitate an in-memory merge. When a sort operation spills to disk, the in-memory data must be sorted and merged before being written to a file. This setting reserves a specific amount of memory for that in-memory sort/merge process. Note: This setting is irrelevant if the sort operation cannot spill (i.e., if there’s no `DiskManager` configured). |
| datafusion.execution.sort\_in\_place\_threshold\_bytes | 1048576 | When sorting, below what size should data be concatenated and sorted in a single RecordBatch rather than sorted in batches and merged. |
| datafusion.execution.sort\_pushdown\_buffer\_capacity | 1073741824 | Maximum buffer capacity (in bytes) per partition for BufferExec inserted during sort pushdown optimization. When PushdownSort eliminates a SortExec under SortPreservingMergeExec, a BufferExec is inserted to replace SortExec’s buffering role. This prevents I/O stalls by allowing the scan to run ahead of the merge. This uses strictly less memory than the SortExec it replaces (which buffers the entire partition). The buffer respects the global memory pool limit. Setting this to a large value is safe — actual memory usage is bounded by partition size and global memory limits. |
| datafusion.execution.max\_spill\_file\_size\_bytes | 134217728 | Maximum size in bytes for individual spill files before rotating to a new file. When operators spill data to disk (e.g., RepartitionExec), they write multiple batches to the same file until this size limit is reached, then rotate to a new file. This reduces syscall overhead compared to one-file-per-batch while preventing files from growing too large. A larger value reduces file creation overhead but may hold more disk space. A smaller value creates more files but allows finer-grained space reclamation as files can be deleted once fully consumed. Now only `RepartitionExec` supports this spill file rotation feature, other spilling operators may create spill files larger than the limit. Default: 128 MB |
| datafusion.execution.meta\_fetch\_concurrency | 32 | Number of files to read in parallel when inferring schema and statistics |
| datafusion.execution.minimum\_parallel\_output\_files | 4 | Guarantees a minimum level of output files running in parallel. RecordBatches will be distributed in round robin fashion to each parallel writer. Each writer is closed and a new file opened once soft\_max\_rows\_per\_output\_file is reached. |
| datafusion.execution.soft\_max\_rows\_per\_output\_file | 50000000 | Target number of rows in output files when writing multiple. This is a soft max, so it can be exceeded slightly. There also will be one file smaller than the limit if the total number of rows written is not roughly divisible by the soft max |
| datafusion.execution.max\_buffered\_batches\_per\_output\_file | 2 | This is the maximum number of RecordBatches buffered for each output file being worked. Higher values can potentially give faster write performance at the cost of higher peak memory consumption |
| datafusion.execution.listing\_table\_ignore\_subdirectory | true | Should sub directories be ignored when scanning directories for data files. Defaults to true (ignores subdirectories), consistent with Hive. Note that this setting does not affect reading partitioned tables (e.g. `/table/year=2021/month=01/data.parquet`). |
| datafusion.execution.listing\_table\_factory\_infer\_partitions | true | Should a `ListingTable` created through the `ListingTableFactory` infer table partitions from Hive compliant directories. Defaults to true (partition columns are inferred and will be represented in the table schema). |
| datafusion.execution.enable\_recursive\_ctes | true | Should DataFusion support recursive CTEs |
| datafusion.execution.split\_file\_groups\_by\_statistics | false | Attempt to eliminate sorts by packing & sorting files with non-overlapping statistics into the same file groups. Currently experimental |
| datafusion.execution.keep\_partition\_by\_columns | false | Should DataFusion keep the columns used for partition\_by in the output RecordBatches |
| datafusion.execution.skip\_partial\_aggregation\_probe\_ratio\_threshold | 0.8 | Aggregation ratio (number of distinct groups / number of input rows) threshold for skipping partial aggregation. If the value is greater then partial aggregation will skip aggregation for further input |
| datafusion.execution.skip\_partial\_aggregation\_probe\_rows\_threshold | 100000 | Number of input rows partial aggregation partition should process, before aggregation ratio check and trying to switch to skipping aggregation mode |
| datafusion.execution.use\_row\_number\_estimates\_to\_optimize\_partitioning | false | Should DataFusion use row number estimates at the input to decide whether increasing parallelism is beneficial or not. By default, only exact row numbers (not estimates) are used for this decision. Setting this flag to `true` will likely produce better plans. if the source of statistics is accurate. We plan to make this the default in the future. |
| datafusion.execution.enforce\_batch\_size\_in\_joins | false | Should DataFusion enforce batch size in joins or not. By default, DataFusion will not enforce batch size in joins. Enforcing batch size in joins can reduce memory usage when joining large tables with a highly-selective join filter, but is also slightly slower. |
| datafusion.execution.objectstore\_writer\_buffer\_size | 10485760 | Size (bytes) of data buffer DataFusion uses when writing output files. This affects the size of the data chunks that are uploaded to remote object stores (e.g. AWS S3). If very large (>= 100 GiB) output files are being written, it may be necessary to increase this size to avoid errors from the remote end point. |
| datafusion.execution.enable\_ansi\_mode | false | Whether to enable ANSI SQL mode. The flag is experimental and relevant only for DataFusion Spark built-in functions When `enable_ansi_mode` is set to `true`, the query engine follows ANSI SQL semantics for expressions, casting, and error handling. This means: - **Strict type coercion rules:** implicit casts between incompatible types are disallowed. - **Standard SQL arithmetic behavior:** operations such as division by zero, numeric overflow, or invalid casts raise runtime errors rather than returning `NULL` or adjusted values. - **Consistent ANSI behavior** for string concatenation, comparisons, and `NULL` handling. When `enable_ansi_mode` is `false` (the default), the engine uses a more permissive, non-ANSI mode designed for user convenience and backward compatibility. In this mode: - Implicit casts between types are allowed (e.g., string to integer when possible). - Arithmetic operations are more lenient — for example, `abs()` on the minimum representable integer value returns the input value instead of raising overflow. - Division by zero or invalid casts may return `NULL` instead of failing. # Default `false` — ANSI SQL mode is disabled by default. |
| datafusion.execution.hash\_join\_buffering\_capacity | 0 | How many bytes to buffer in the probe side of hash joins while the build side is concurrently being built. Without this, hash joins will wait until the full materialization of the build side before polling the probe side. This is useful in scenarios where the query is not completely CPU bounded, allowing to do some early work concurrently and reducing the latency of the query. Note that when hash join buffering is enabled, the probe side will start eagerly polling data, not giving time for the producer side of dynamic filters to produce any meaningful predicate. Queries with dynamic filters might see performance degradation. Disabled by default, set to a number greater than 0 for enabling it. |
| datafusion.optimizer.enable\_distinct\_aggregation\_soft\_limit | true | When set to true, the optimizer will push a limit operation into grouped aggregations which have no aggregate expressions, as a soft limit, emitting groups once the limit is reached, before all rows in the group are read. |
| datafusion.optimizer.enable\_round\_robin\_repartition | true | When set to true, the physical plan optimizer will try to add round robin repartitioning to increase parallelism to leverage more CPU cores |
| datafusion.optimizer.enable\_topk\_aggregation | true | When set to true, the optimizer will attempt to perform limit operations during aggregations, if possible |
| datafusion.optimizer.enable\_window\_limits | true | When set to true, the optimizer will attempt to push limit operations past window functions, if possible |
| datafusion.optimizer.enable\_window\_topn | false | When set to true, the optimizer will replace Filter(rn<=K) → Window(ROW\_NUMBER) → Sort patterns with a PartitionedTopKExec that maintains per-partition heaps, avoiding a full sort of the input. When the window partition key has low cardinality, enabling this optimization can improve performance. However, for high cardinality keys, it may cause regressions in both memory usage and runtime. |
| datafusion.optimizer.enable\_topk\_repartition | true | When set to true, the optimizer will push TopK (Sort with fetch) below hash repartition when the partition key is a prefix of the sort key, reducing data volume before the shuffle. |
| datafusion.optimizer.enable\_topk\_dynamic\_filter\_pushdown | true | When set to true, the optimizer will attempt to push down TopK dynamic filters into the file scan phase. |
| datafusion.optimizer.enable\_join\_dynamic\_filter\_pushdown | true | When set to true, the optimizer will attempt to push down Join dynamic filters into the file scan phase. |
| datafusion.optimizer.enable\_aggregate\_dynamic\_filter\_pushdown | true | When set to true, the optimizer will attempt to push down Aggregate dynamic filters into the file scan phase. |
| datafusion.optimizer.enable\_dynamic\_filter\_pushdown | true | When set to true attempts to push down dynamic filters generated by operators (TopK, Join & Aggregate) into the file scan phase. For example, for a query such as `SELECT * FROM t ORDER BY timestamp DESC LIMIT 10`, the optimizer will attempt to push down the current top 10 timestamps that the TopK operator references into the file scans. This means that if we already have 10 timestamps in the year 2025 any files that only have timestamps in the year 2024 can be skipped / pruned at various stages in the scan. The config will suppress `enable_join_dynamic_filter_pushdown`, `enable_topk_dynamic_filter_pushdown` & `enable_aggregate_dynamic_filter_pushdown` So if you disable `enable_topk_dynamic_filter_pushdown`, then enable `enable_dynamic_filter_pushdown`, the `enable_topk_dynamic_filter_pushdown` will be overridden. |
| datafusion.optimizer.filter\_null\_join\_keys | false | When set to true, the optimizer will insert filters before a join between a nullable and non-nullable column to filter out nulls on the nullable side. This filter can add additional overhead when the file format does not fully support predicate push down. |
| datafusion.optimizer.repartition\_aggregations | true | Should DataFusion repartition data using the aggregate keys to execute aggregates in parallel using the provided `target_partitions` level |
| datafusion.optimizer.repartition\_file\_min\_size | 10485760 | Minimum total files size in bytes to perform file scan repartitioning. |
| datafusion.optimizer.repartition\_joins | true | Should DataFusion repartition data using the join keys to execute joins in parallel using the provided `target_partitions` level |
| datafusion.optimizer.allow\_symmetric\_joins\_without\_pruning | true | Should DataFusion allow symmetric hash joins for unbounded data sources even when its inputs do not have any ordering or filtering If the flag is not enabled, the SymmetricHashJoin operator will be unable to prune its internal buffers, resulting in certain join types - such as Full, Left, LeftAnti, LeftSemi, Right, RightAnti, and RightSemi - being produced only at the end of the execution. This is not typical in stream processing. Additionally, without proper design for long runner execution, all types of joins may encounter out-of-memory errors. |
| datafusion.optimizer.repartition\_file\_scans | true | When set to `true`, datasource partitions will be repartitioned to achieve maximum parallelism. This applies to both in-memory partitions and FileSource’s file groups (1 group is 1 partition). For FileSources, only Parquet and CSV formats are currently supported. If set to `true` for a FileSource, all files will be repartitioned evenly (i.e., a single large file might be partitioned into smaller chunks) for parallel scanning. If set to `false` for a FileSource, different files will be read in parallel, but repartitioning won’t happen within a single file. If set to `true` for an in-memory source, all memtable’s partitions will have their batches repartitioned evenly to the desired number of `target_partitions`. Repartitioning can change the total number of partitions and batches per partition, but does not slice the initial record tables provided to the MemTable on creation. |
| datafusion.optimizer.preserve\_file\_partitions | 0 | Minimum number of distinct partition values required to group files by their Hive partition column values (enabling Hash partitioning declaration). How the option is used: - preserve\_file\_partitions=0: Disable it. - preserve\_file\_partitions=1: Always enable it. - preserve\_file\_partitions=N, actual file partitions=M: Only enable when M >= N. This threshold preserves I/O parallelism when file partitioning is below it. Note: This may reduce parallelism, rooting from the I/O level, if the number of distinct partitions is less than the target\_partitions. |
| datafusion.optimizer.repartition\_windows | true | Should DataFusion repartition data using the partitions keys to execute window functions in parallel using the provided `target_partitions` level |
| datafusion.optimizer.repartition\_sorts | true | Should DataFusion execute sorts in a per-partition fashion and merge afterwards instead of coalescing first and sorting globally. With this flag is enabled, plans in the form below `text "SortExec: [a@0 ASC]", " CoalescePartitionsExec", " RepartitionExec: partitioning=RoundRobinBatch(8), input_partitions=1",`  would turn into the plan below which performs better in multithreaded environments `text "SortPreservingMergeExec: [a@0 ASC]", " SortExec: [a@0 ASC]", " RepartitionExec: partitioning=RoundRobinBatch(8), input_partitions=1",` |
| datafusion.optimizer.subset\_repartition\_threshold | 4 | Partition count threshold for subset satisfaction optimization. When the current partition count is >= this threshold, DataFusion will skip repartitioning if the required partitioning expression is a subset of the current partition expression such as Hash(a) satisfies Hash(a, b). When the current partition count is < this threshold, DataFusion will repartition to increase parallelism even when subset satisfaction applies. Set to 0 to always repartition (disable subset satisfaction optimization). Set to a high value to always use subset satisfaction. Example (subset\_repartition\_threshold = 4): `text Hash([a]) satisfies Hash([a, b]) because (Hash([a, b]) is subset of Hash([a]) If current partitions (3) < threshold (4), repartition: AggregateExec: mode=FinalPartitioned, gby=[a, b], aggr=[SUM(x)] RepartitionExec: partitioning=Hash([a, b], 8), input_partitions=3 AggregateExec: mode=Partial, gby=[a, b], aggr=[SUM(x)] DataSourceExec: file_groups={...}, output_partitioning=Hash([a], 3) If current partitions (8) >= threshold (4), use subset satisfaction: AggregateExec: mode=SinglePartitioned, gby=[a, b], aggr=[SUM(x)] DataSourceExec: file_groups={...}, output_partitioning=Hash([a], 8)` |
| datafusion.optimizer.prefer\_existing\_sort | false | When true, DataFusion will opportunistically remove sorts when the data is already sorted, (i.e. setting `preserve_order` to true on `RepartitionExec` and using `SortPreservingMergeExec`) When false, DataFusion will maximize plan parallelism using `RepartitionExec` even if this requires subsequently resorting data using a `SortExec`. |
| datafusion.optimizer.skip\_failed\_rules | false | When set to true, the logical plan optimizer will produce warning messages if any optimization rules produce errors and then proceed to the next rule. When set to false, any rules that produce errors will cause the query to fail |
| datafusion.optimizer.max\_passes | 3 | Number of times that the optimizer will attempt to optimize the plan |
| datafusion.optimizer.top\_down\_join\_key\_reordering | true | When set to true, the physical plan optimizer will run a top down process to reorder the join keys |
| datafusion.optimizer.join\_reordering | true | When set to true, the physical plan optimizer may swap join inputs based on statistics. When set to false, statistics-driven join input reordering is disabled and the original join order in the query is used. |
| datafusion.optimizer.use\_statistics\_registry | false | When set to true, the physical plan optimizer uses the pluggable `StatisticsRegistry` for statistics propagation across operators. This enables more accurate cardinality estimates compared to each operator’s built-in `partition_statistics`. |
| datafusion.optimizer.prefer\_hash\_join | true | When set to true, the physical plan optimizer will prefer HashJoin over SortMergeJoin. HashJoin can work more efficiently than SortMergeJoin but consumes more memory |
| datafusion.optimizer.enable\_piecewise\_merge\_join | false | When set to true, piecewise merge join is enabled. PiecewiseMergeJoin is currently experimental. Physical planner will opt for PiecewiseMergeJoin when there is only one range filter. |
| datafusion.optimizer.hash\_join\_single\_partition\_threshold | 1048576 | The maximum estimated size in bytes for one input side of a HashJoin will be collected into a single partition |
| datafusion.optimizer.hash\_join\_single\_partition\_threshold\_rows | 131072 | The maximum estimated size in rows for one input side of a HashJoin will be collected into a single partition |
| datafusion.optimizer.hash\_join\_inlist\_pushdown\_max\_size | 131072 | Maximum size in bytes for the build side of a hash join to be pushed down as an InList expression for dynamic filtering. Build sides larger than this will use hash table lookups instead. Set to 0 to always use hash table lookups. InList pushdown can be more efficient for small build sides because it can result in better statistics pruning as well as use any bloom filters present on the scan side. InList expressions are also more transparent and easier to serialize over the network in distributed uses of DataFusion. On the other hand InList pushdown requires making a copy of the data and thus adds some overhead to the build side and uses more memory. This setting is per-partition, so we may end up using `hash_join_inlist_pushdown_max_size` \* `target_partitions` memory. The default is 128kB per partition. This should allow point lookup joins (e.g. joining on a unique primary key) to use InList pushdown in most cases but avoids excessive memory usage or overhead for larger joins. |
| datafusion.optimizer.hash\_join\_inlist\_pushdown\_max\_distinct\_values | 150 | Maximum number of distinct values (rows) in the build side of a hash join to be pushed down as an InList expression for dynamic filtering. Build sides with more rows than this will use hash table lookups instead. Set to 0 to always use hash table lookups. This provides an additional limit beyond `hash_join_inlist_pushdown_max_size` to prevent very large IN lists that might not provide much benefit over hash table lookups. This uses the deduplicated row count once the build side has been evaluated. The default is 150 values per partition. This is inspired by Trino’s `max-filter-keys-per-column` setting. See: <https://trino.io/docs/current/admin/dynamic-filtering.html#dynamic-filter-collection-thresholds> |
| datafusion.optimizer.default\_filter\_selectivity | 20 | The default filter selectivity used by Filter Statistics when an exact selectivity cannot be determined. Valid values are between 0 (no selectivity) and 100 (all rows are selected). |
| datafusion.optimizer.prefer\_existing\_union | false | When set to true, the optimizer will not attempt to convert Union to Interleave |
| datafusion.optimizer.expand\_views\_at\_output | false | When set to true, if the returned type is a view type then the output will be coerced to a non-view. Coerces `Utf8View` to `LargeUtf8`, and `BinaryView` to `LargeBinary`. |
| datafusion.optimizer.enable\_sort\_pushdown | true | Enable sort pushdown optimization. When enabled, attempts to push sort requirements down to data sources that can natively handle them (e.g., by reversing file/row group read order). Returns **inexact ordering**: Sort operator is kept for correctness, but optimized input enables early termination for TopK queries (ORDER BY … LIMIT N), providing significant speedup. Memory: No additional overhead (only changes read order). Future: Will add option to detect perfectly sorted data and eliminate Sort completely. Default: true |
| datafusion.optimizer.enable\_leaf\_expression\_pushdown | true | When set to true, the optimizer will extract leaf expressions (such as `get_field`) from filter/sort/join nodes into projections closer to the leaf table scans, and push those projections down towards the leaf nodes. |
| datafusion.explain.logical\_plan\_only | false | When set to true, the explain statement will only print logical plans |
| datafusion.explain.physical\_plan\_only | false | When set to true, the explain statement will only print physical plans |
| datafusion.explain.show\_statistics | false | When set to true, the explain statement will print operator statistics for physical plans |
| datafusion.explain.show\_sizes | true | When set to true, the explain statement will print the partition sizes |
| datafusion.explain.show\_schema | false | When set to true, the explain statement will print schema information |
| datafusion.explain.format | indent | Display format of explain. Default is “indent”. When set to “tree”, it will print the plan in a tree-rendered format. |
| datafusion.explain.tree\_maximum\_render\_width | 240 | (format=tree only) Maximum total width of the rendered tree. When set to 0, the tree will have no width limit. |
| datafusion.explain.analyze\_level | dev | Verbosity level for “EXPLAIN ANALYZE”. Default is “dev” “summary” shows common metrics for high-level insights. “dev” provides deep operator-level introspection for developers. |
| datafusion.explain.analyze\_categories | all | Which metric categories to include in “EXPLAIN ANALYZE” output. Comma-separated list of: “rows”, “bytes”, “timing”, “uncategorized”. Use “none” to show plan structure only, or “all” (default) to show everything. Metrics without a declared category are treated as “uncategorized”. |
| datafusion.sql\_parser.parse\_float\_as\_decimal | false | When set to true, SQL parser will parse float as decimal type |
| datafusion.sql\_parser.enable\_ident\_normalization | true | When set to true, SQL parser will normalize ident (convert ident to lowercase when not quoted) |
| datafusion.sql\_parser.enable\_options\_value\_normalization | false | When set to true, SQL parser will normalize options value (convert value to lowercase). Note that this option is ignored and will be removed in the future. All case-insensitive values are normalized automatically. |
| datafusion.sql\_parser.dialect | generic | Configure the SQL dialect used by DataFusion’s parser; supported values include: Generic, MySQL, PostgreSQL, Hive, SQLite, Snowflake, Redshift, MsSQL, ClickHouse, BigQuery, Ansi, DuckDB and Databricks. |
| datafusion.sql\_parser.support\_varchar\_with\_length | true | If true, permit lengths for `VARCHAR` such as `VARCHAR(20)`, but ignore the length. If false, error if a `VARCHAR` with a length is specified. The Arrow type system does not have a notion of maximum string length and thus DataFusion can not enforce such limits. |
| datafusion.sql\_parser.map\_string\_types\_to\_utf8view | true | If true, string types (VARCHAR, CHAR, Text, and String) are mapped to `Utf8View` during SQL planning. If false, they are mapped to `Utf8`. Default is true. |
| datafusion.sql\_parser.collect\_spans | false | When set to true, the source locations relative to the original SQL query (i.e. [`Span`](https://docs.rs/sqlparser/latest/sqlparser/tokenizer/struct.Span.html)) will be collected and recorded in the logical plan nodes. |
| datafusion.sql\_parser.recursion\_limit | 50 | Specifies the recursion depth limit when parsing complex SQL Queries |
| datafusion.sql\_parser.default\_null\_ordering | nulls\_max | Specifies the default null ordering for query results. There are 4 options: - `nulls_max`: Nulls appear last in ascending order. - `nulls_min`: Nulls appear first in ascending order. - `nulls_first`: Nulls always be first in any order. - `nulls_last`: Nulls always be last in any order. By default, `nulls_max` is used to follow Postgres’s behavior. postgres rule: <https://www.postgresql.org/docs/current/queries-order.html> |
| datafusion.sql\_parser.enable\_subquery\_sort\_elimination | true | When set to true, DataFusion may remove `ORDER BY` clauses from subqueries or CTEs during SQL planning when their ordering cannot affect the result, such as when no `LIMIT` or other order-sensitive operator depends on them. Disable this option to preserve explicit subquery ordering in the planned query. |
| datafusion.format.safe | true | If set to `true` any formatting errors will be written to the output instead of being converted into a [`std::fmt::Error`] |
| datafusion.format.null |  | Format string for nulls |
| datafusion.format.date\_format | %Y-%m-%d | Date format for date arrays |
| datafusion.format.datetime\_format | %Y-%m-%dT%H:%M:%S%.f | Format for DateTime arrays |
| datafusion.format.timestamp\_format | %Y-%m-%dT%H:%M:%S%.f | Timestamp format for timestamp arrays |
| datafusion.format.timestamp\_tz\_format | NULL | Timestamp format for timestamp with timezone arrays. When `None`, ISO 8601 format is used. |
| datafusion.format.time\_format | %H:%M:%S%.f | Time format for time arrays |
| datafusion.format.duration\_format | pretty | Duration format. Can be either `"pretty"` or `"ISO8601"` |
| datafusion.format.types\_info | false | Show types in visual representation batches |

You can also reset configuration options to default settings via SQL using the `RESET` command. For
example, to set and reset `datafusion.execution.batch_size`:

```
SET datafusion.execution.batch_size = '10000';

SHOW datafusion.execution.batch_size;
datafusion.execution.batch_size 10000

RESET datafusion.execution.batch_size;

SHOW datafusion.execution.batch_size;
datafusion.execution.batch_size 8192
```

# Runtime Configuration Settings[#](#runtime-configuration-settings "Link to this heading")

DataFusion runtime configurations can be set via SQL using the `SET` command.

For example, to configure `datafusion.runtime.memory_limit`:

```
SET datafusion.runtime.memory_limit = '2G';
```

The following runtime configuration settings are available:

| key | default | description |
| --- | --- | --- |
| datafusion.runtime.list\_files\_cache\_limit | 1M | Maximum memory to use for list files cache. Supports suffixes K (kilobytes), M (megabytes), and G (gigabytes). Example: ‘2G’ for 2 gigabytes. |
| datafusion.runtime.list\_files\_cache\_ttl | NULL | TTL (time-to-live) of the entries in the list file cache. Supports units m (minutes), and s (seconds). Example: ‘2m’ for 2 minutes. |
| datafusion.runtime.max\_temp\_directory\_size | 100G | Maximum temporary file directory size. Supports suffixes K (kilobytes), M (megabytes), and G (gigabytes). Example: ‘2G’ for 2 gigabytes. |
| datafusion.runtime.memory\_limit | NULL | Maximum memory limit for query execution. Supports suffixes K (kilobytes), M (megabytes), and G (gigabytes). Example: ‘2G’ for 2 gigabytes. |
| datafusion.runtime.metadata\_cache\_limit | 50M | Maximum memory to use for file metadata cache such as Parquet metadata. Supports suffixes K (kilobytes), M (megabytes), and G (gigabytes). Example: ‘2G’ for 2 gigabytes. |
| datafusion.runtime.temp\_directory | NULL | The path to the temporary file directory. |

# Tuning Guide[#](#tuning-guide "Link to this heading")

## Short Queries[#](#short-queries "Link to this heading")

By default DataFusion will attempt to maximize parallelism and use all cores –
For example, if you have 32 cores, each plan will split the data into 32
partitions. However, if your data is small, the overhead of splitting the data
to enable parallelization can dominate the actual computation.

You can find out how many cores are being used via the [`EXPLAIN`](sql/explain.html) command and look
at the number of partitions in the plan.

The `datafusion.optimizer.repartition_file_min_size` option controls the minimum file size the
[`ListingTable`](https://docs.rs/datafusion/latest/datafusion/datasource/listing/struct.ListingTable.html) provider will attempt to repartition. However, this
does not apply to user defined data sources and only works when DataFusion has accurate statistics.

If you know your data is small, you can set the `datafusion.execution.target_partitions`
option to a smaller number to reduce the overhead of repartitioning. For very small datasets (e.g. less
than 1MB), we recommend setting `target_partitions` to 1 to avoid repartitioning altogether.

```
SET datafusion.execution.target_partitions = '1';
```

## Memory-limited Queries[#](#memory-limited-queries "Link to this heading")

When executing a memory-consuming query under a tight memory limit, DataFusion
will spill intermediate results to disk.

When the [`FairSpillPool`](https://docs.rs/datafusion/latest/datafusion/execution/memory_pool/struct.FairSpillPool.html) is used, memory is divided evenly among partitions.
The higher the value of `datafusion.execution.target_partitions`, the less memory
is allocated to each partition, and the out-of-core execution path may trigger
more frequently, possibly slowing down execution.

Additionally, while spilling, data is read back in `datafusion.execution.batch_size` size batches.
The larger this value, the fewer spilled sorted runs can be merged. Decreasing this setting
can help reduce the number of subsequent spills required.

In conclusion, for queries under a very tight memory limit, it’s recommended to
set `target_partitions` and `batch_size` to smaller values.

```
-- Query still gets parallelized, but each partition will have more memory to use
SET datafusion.execution.target_partitions = 4;
-- Smaller than the default '8192', while still keep the benefit of vectorized execution
SET datafusion.execution.batch_size = 1024;
```

## Join Queries[#](#join-queries "Link to this heading")

Currently Apache Datafusion supports the following join algorithms:

* Nested Loop Join
* Sort Merge Join
* Hash Join
* Symmetric Hash Join
* Piecewise Merge Join (experimental)

The physical planner will choose the appropriate algorithm based on the statistics + join
condition of the two tables.

# Join Algorithm Optimizer Configurations[#](#join-algorithm-optimizer-configurations "Link to this heading")

You can modify join optimization behavior in your queries by setting specific configuration values.
Use the following command to update a configuration:

```
SET datafusion.optimizer.<configuration_name>;
```

Example

```
SET datafusion.optimizer.prefer_hash_join = false;
```

Adjusting the following configuration values influences how the optimizer selects the join algorithm
used to execute your SQL query:

## Join Optimizer Configurations[#](#join-optimizer-configurations "Link to this heading")

Adjusting the following configuration values influences how the optimizer selects the join algorithm
used to execute your SQL query.

### allow\_symmetric\_joins\_without\_pruning (bool, default = true)[#](#allow-symmetric-joins-without-pruning-bool-default-true "Link to this heading")

Controls whether symmetric hash joins are allowed for unbounded data sources even when their inputs
lack ordering or filtering.

* If disabled, the `SymmetricHashJoin` operator cannot prune its internal buffers to be produced only at the end of execution.

### prefer\_hash\_join (bool, default = true)[#](#prefer-hash-join-bool-default-true "Link to this heading")

Determines whether the optimizer prefers Hash Join over Sort Merge Join during physical plan selection.

* true: favors HashJoin for faster execution when sufficient memory is available.
* false: allows SortMergeJoin to be chosen when more memory-efficient execution is needed.

### enable\_piecewise\_merge\_join (bool, default = false)[#](#enable-piecewise-merge-join-bool-default-false "Link to this heading")

Enables the experimental Piecewise Merge Join algorithm.

* When enabled, the physical planner may select PiecewiseMergeJoin if there is exactly one range
  filter in the join condition.
* Piecewise Merge Join is faster than Nested Loop Join performance wise for single range filter
  except for cases where it is joining two large tables (num\_rows > 100,000) that are approximately
  equal in size.

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/configs.md)

[Show Source](../_sources/user-guide/configs.md.txt)

---
# DataFrame API[#](#dataframe-api "Link to this heading")

## DataFrame overview[#](#dataframe-overview "Link to this heading")

A DataFrame represents a logical set of rows with the same named columns,
similar to a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) or [Spark DataFrame](https://spark.apache.org/docs/latest/sql-programming-guide.html).

DataFrames are typically created by calling a method on [`SessionContext`](https://docs.rs/datafusion/latest/datafusion/execution/context/struct.SessionContext.html), such
as [`read_csv`](https://docs.rs/datafusion/latest/datafusion/execution/context/struct.SessionContext.html#method.read_csv), and can then be modified by calling the transformation methods,
such as [`filter`](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html#method.filter), [`select`](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html#method.select), [`aggregate`](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html#method.aggregate), and [`limit`](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html#method.limit) to build up a query
definition.

The query can be executed by calling the [`collect`](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html#method.collect) method.

DataFusion DataFrames use lazy evaluation, meaning that each transformation
creates a new plan but does not actually perform any immediate actions. This
approach allows for the overall plan to be optimized before execution. The plan
is evaluated (executed) when an action method is invoked, such as [`collect`](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html#method.collect).
See the [Library Users Guide](../library-user-guide/using-the-dataframe-api.html) for more details.

The DataFrame API is well documented in the [API reference on docs.rs](https://docs.rs/datafusion/latest/datafusion/dataframe/struct.DataFrame.html).
Please refer to the [Expressions Reference](expressions.html) for more information on
building logical expressions (`Expr`) to use with the DataFrame API.

## Example[#](#example "Link to this heading")

The DataFrame struct is part of DataFusion’s `prelude` and can be imported with
the following statement.

```
use datafusion::prelude::*;
```

Here is a minimal example showing the execution of a query using the DataFrame API.

Create DataFrame using macro API from in memory rows

```
use datafusion::prelude::*;
use datafusion::error::Result;

#[tokio::main]
async fn main() -> Result<()> {
    // Create a new dataframe with in-memory data using macro
    let df = dataframe!(
        "a" => [1, 2, 3],
        "b" => [true, true, false],
        "c" => [Some("foo"), Some("bar"), None]
    )?;
    df.show().await?;
    Ok(())
}
```

Create DataFrame from file or in memory rows using standard API

```
use datafusion::arrow::array::{Int32Array, RecordBatch, StringArray};
use datafusion::arrow::datatypes::{DataType, Field, Schema};
use datafusion::error::Result;
use datafusion::functions_aggregate::expr_fn::min;
use datafusion::prelude::*;
use std::sync::Arc;

#[tokio::main]
async fn main() -> Result<()> {
    // Read the data from a csv file
    let ctx = SessionContext::new();
    let df = ctx.read_csv("tests/data/example.csv", CsvReadOptions::new()).await?;
    let df = df.filter(col("a").lt_eq(col("b")))?
        .aggregate(vec![col("a")], vec![min(col("b"))])?
        .limit(0, Some(100))?;
    // Print results
    df.show().await?;

    // Create a new dataframe with in-memory data
    let schema = Schema::new(vec![
      Field::new("id", DataType::Int32, true),
      Field::new("name", DataType::Utf8, true),
    ]);
    let batch = RecordBatch::try_new(
      Arc::new(schema),
      vec![
          Arc::new(Int32Array::from(vec![1, 2, 3])),
          Arc::new(StringArray::from(vec!["foo", "bar", "baz"])),
      ],
    )?;
    let df = ctx.read_batch(batch)?;
    df.show().await?;

    Ok(())
}
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/dataframe.md)

[Show Source](../_sources/user-guide/dataframe.md.txt)

---
# DataFusion CLI[#](#datafusion-cli "Link to this heading")

* [Overview](overview.html)
* [Installation](installation.html)
  * [Install and run using Cargo](installation.html#install-and-run-using-cargo)
  * [Install and run using Homebrew (on MacOS)](installation.html#install-and-run-using-homebrew-on-macos)
  * [Run using Docker](installation.html#run-using-docker)
* [Usage](usage.html)
  * [Commands](usage.html#commands)
  * [Supported SQL](usage.html#supported-sql)
    * [`SHOW ALL [VERBOSE]`](usage.html#show-all-verbose)
    * [`SHOW <OPTION>>`](usage.html#show-option)
    * [`SET <OPTION> TO <VALUE>`](usage.html#set-option-to-value)
  * [Configuration Options](usage.html#configuration-options)
  * [Functions](usage.html#functions)
* [Local Files / Directories](datasources.html)
* [Remote Files / Directories](datasources.html#remote-files-directories)
* [`CREATE EXTERNAL TABLE`](datasources.html#create-external-table)
* [Formats](datasources.html#formats)
  * [Parquet](datasources.html#parquet)
    * [Parquet Specific Options](datasources.html#parquet-specific-options)
  * [CSV](datasources.html#csv)
* [Locations](datasources.html#locations)
  * [HTTP(s)](datasources.html#http-s)
  * [S3](datasources.html#s3)
  * [OSS](datasources.html#oss)
  * [COS](datasources.html#cos)
  * [GCS](datasources.html#gcs)
* [CLI Specific Functions](functions.html)
  * [`parquet_metadata`](functions.html#parquet-metadata)
  * [`metadata_cache`](functions.html#metadata-cache)
  * [`statistics_cache`](functions.html#statistics-cache)
  * [`list_files_cache`](functions.html#list-files-cache)

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/cli/index.rst)

[Show Source](../../_sources/user-guide/cli/index.rst.txt)

---
# Local Files / Directories[#](#local-files-directories "Link to this heading")

Files can be queried directly by enclosing the file, directory name
or a remote location in single `'` quotes as shown in the examples.

Create a CSV file to query.

```
$ echo "a,b" > data.csv
$ echo "1,2" >> data.csv
```

Query that single file (the CLI also supports parquet, compressed csv, avro, json and more)

```
$ datafusion-cli
DataFusion CLI v17.0.0
> select * from 'data.csv';
+---+---+
| a | b |
+---+---+
| 1 | 2 |
+---+---+
1 row in set. Query took 0.007 seconds.
```

You can also query directories of files with compatible schemas:

```
$ ls data_dir/
data.csv   data2.csv
```

```
$ datafusion-cli
DataFusion CLI v16.0.0
> select * from 'data_dir';
+---+---+
| a | b |
+---+---+
| 3 | 4 |
| 1 | 2 |
+---+---+
2 rows in set. Query took 0.007 seconds.
```

# Remote Files / Directories[#](#remote-files-directories "Link to this heading")

You can also query directly any remote location supported by DataFusion without
registering the location as a table.
For example, to read from a remote parquet file via HTTP(S) you can use the following:

```
select count(*) from 'https://datasets.clickhouse.com/hits_compatible/athena_partitioned/hits_1.parquet'
+----------+
| COUNT(*) |
+----------+
| 1000000  |
+----------+
1 row in set. Query took 0.595 seconds.
```

To read from an AWS S3 or GCS, use `s3` or `gs` as a protocol prefix. For
example, to read a file in an S3 bucket named `my-data-bucket` use the URL
`s3://my-data-bucket`and set the relevant access credentials as environmental
variables (e.g. for AWS S3 you can use `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`).

```
> select count(*) from 's3://altinity-clickhouse-data/nyc_taxi_rides/data/tripdata_parquet/';
+------------+
| count(*)   |
+------------+
| 1310903963 |
+------------+
```

See the [`CREATE EXTERNAL TABLE`](#create-external-table) section below for
additional configuration options.

# `CREATE EXTERNAL TABLE`[#](#create-external-table "Link to this heading")

It is also possible to create a table backed by files or remote locations via
`CREATE EXTERNAL TABLE` as shown below. Note that DataFusion does not support
wildcards (e.g. `*`) in file paths; instead, specify the directory path directly
to read all compatible files in that directory.

For example, to create a table `hits` backed by a local parquet file named `hits.parquet`:

```
CREATE EXTERNAL TABLE hits
STORED AS PARQUET
LOCATION 'hits.parquet';
```

To create a table `hits` backed by a remote parquet file via HTTP(S):

```
CREATE EXTERNAL TABLE hits
STORED AS PARQUET
LOCATION 'https://datasets.clickhouse.com/hits_compatible/athena_partitioned/hits_1.parquet';
```

In both cases, `hits` now can be queried as a regular table:

```
select count(*) from hits;
+----------+
| COUNT(*) |
+----------+
| 1000000  |
+----------+
1 row in set. Query took 0.344 seconds.
```

**Why Wildcards Are Not Supported**

Although wildcards (e.g., *.parquet or \*\*/*.parquet) may work for local
filesystems in some cases, they are not supported by DataFusion CLI. This
is because wildcards are not universally applicable across all storage backends
(e.g., S3, GCS). Instead, DataFusion expects the user to specify the directory
path, and it will automatically read all compatible files within that directory.

For example, the following usage is not supported:

```
CREATE EXTERNAL TABLE test (
    message TEXT,
    day DATE
)
STORED AS PARQUET
LOCATION 'gs://bucket/*.parquet';
```

Instead, you should use:

```
CREATE EXTERNAL TABLE test (
    message TEXT,
    day DATE
)
STORED AS PARQUET
LOCATION 'gs://bucket/my_table/';
```

When specifying a directory path that has a Hive compliant partition structure, by default, DataFusion CLI will
automatically parse and incorporate the Hive columns and their values into the table’s schema and data. Given the
following remote object paths:

```
gs://bucket/my_table/a=1/b=100/file1.parquet
gs://bucket/my_table/a=2/b=200/file2.parquet
```

`my_table` can be queried and filtered on the Hive columns:

```
CREATE EXTERNAL TABLE my_table
STORED AS PARQUET
LOCATION 'gs://bucket/my_table/';

SELECT count(*) FROM my_table WHERE b=200;
+----------+
| count(*) |
+----------+
| 1        |
+----------+
```

# Formats[#](#formats "Link to this heading")

## Parquet[#](#parquet "Link to this heading")

The schema information for parquet will be derived automatically.

Register a single file parquet datasource

```
CREATE EXTERNAL TABLE taxi
STORED AS PARQUET
LOCATION '/mnt/nyctaxi/tripdata.parquet';
```

Register a single folder parquet datasource. Note: All files inside must be valid
parquet files and have compatible schemas

Note

Paths must end in Slash `/`
:   The path must end in `/` otherwise DataFusion will treat the path as a file and not a directory

```
CREATE EXTERNAL TABLE taxi
STORED AS PARQUET
LOCATION '/mnt/nyctaxi/';
```

### Parquet Specific Options[#](#parquet-specific-options "Link to this heading")

You can specify additional options for parquet files using the `OPTIONS` clause.
For example, to read and write a parquet directory with encryption settings you could use:

```
CREATE EXTERNAL TABLE encrypted_parquet_table
(
double_field double,
float_field float
)
STORED AS PARQUET LOCATION 'pq/' OPTIONS (
    -- encryption
    'format.crypto.file_encryption.encrypt_footer' 'true',
    'format.crypto.file_encryption.footer_key_as_hex' '30313233343536373839303132333435',  -- b"0123456789012345"
    'format.crypto.file_encryption.column_key_as_hex::double_field' '31323334353637383930313233343530', -- b"1234567890123450"
    'format.crypto.file_encryption.column_key_as_hex::float_field' '31323334353637383930313233343531', -- b"1234567890123451"
    -- decryption
    'format.crypto.file_decryption.footer_key_as_hex' '30313233343536373839303132333435', -- b"0123456789012345"
    'format.crypto.file_decryption.column_key_as_hex::double_field' '31323334353637383930313233343530', -- b"1234567890123450"
    'format.crypto.file_decryption.column_key_as_hex::float_field' '31323334353637383930313233343531', -- b"1234567890123451"
);
```

Here the keys are specified in hexadecimal format because they are binary data. These can be encoded in SQL using:

```
select encode('0123456789012345', 'hex');
/*
+----------------------------------------------+
| encode(Utf8("0123456789012345"),Utf8("hex")) |
+----------------------------------------------+
| 30313233343536373839303132333435             |
+----------------------------------------------+
*/
```

For more details on the available options, refer to the Rust
[TableParquetOptions](https://docs.rs/datafusion/latest/datafusion/common/config/struct.TableParquetOptions.html)
documentation in DataFusion.

## CSV[#](#csv "Link to this heading")

DataFusion will infer the CSV schema automatically or you can provide it explicitly.

Register a single file csv datasource with a header row:

```
CREATE EXTERNAL TABLE test
STORED AS CSV
LOCATION '/path/to/aggregate_test_100.csv'
OPTIONS ('has_header' 'true');
```

Register a single file csv datasource with explicitly defined schema:

```
CREATE EXTERNAL TABLE test (
    c1  VARCHAR NOT NULL,
    c2  INT NOT NULL,
    c3  SMALLINT NOT NULL,
    c4  SMALLINT NOT NULL,
    c5  INT NOT NULL,
    c6  BIGINT NOT NULL,
    c7  SMALLINT NOT NULL,
    c8  INT NOT NULL,
    c9  BIGINT NOT NULL,
    c10 VARCHAR NOT NULL,
    c11 FLOAT NOT NULL,
    c12 DOUBLE NOT NULL,
    c13 VARCHAR NOT NULL
)
STORED AS CSV
LOCATION '/path/to/aggregate_test_100.csv';
```

# Locations[#](#locations "Link to this heading")

## HTTP(s)[#](#http-s "Link to this heading")

To read from a remote parquet file via HTTP(S):

```
CREATE EXTERNAL TABLE hits
STORED AS PARQUET
LOCATION 'https://datasets.clickhouse.com/hits_compatible/athena_partitioned/hits_1.parquet';
```

## S3[#](#s3 "Link to this heading")

DataFusion CLI supports configuring [AWS S3](https://aws.amazon.com/s3/) via the
`CREATE EXTERNAL TABLE` statement and standard AWS configuration methods (via the
[`aws-config`](https://docs.rs/aws-config/latest/aws_config/) AWS SDK crate).

To create an external table from a file in an S3 bucket with explicit
credentials:

```
CREATE EXTERNAL TABLE test
STORED AS PARQUET
OPTIONS(
    'aws.access_key_id' '******',
    'aws.secret_access_key' '******',
    'aws.region' 'us-east-2'
)
LOCATION 's3://bucket/path/file.parquet';
```

To create an external table using environment variables:

```
$ export AWS_DEFAULT_REGION=us-east-2
$ export AWS_SECRET_ACCESS_KEY=******
$ export AWS_ACCESS_KEY_ID=******

$ datafusion-cli
`datafusion-cli v21.0.0
> create CREATE TABLE test STORED AS PARQUET LOCATION 's3://bucket/path/file.parquet';
0 rows in set. Query took 0.374 seconds.
> select * from test;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
1 row in set. Query took 0.171 seconds.
```

To read from a public S3 bucket without signatures, use the
`aws.SKIP_SIGNATURE` option:

```
CREATE EXTERNAL TABLE nyc_taxi_rides
STORED AS PARQUET LOCATION 's3://altinity-clickhouse-data/nyc_taxi_rides/data/tripdata_parquet/'
OPTIONS(aws.SKIP_SIGNATURE true);
```

Credentials are taken in this order of precedence:

1. Explicitly specified in the `OPTIONS` clause of the `CREATE EXTERNAL TABLE` statement.
2. Determined by [`aws-config`](https://docs.rs/aws-config/latest/aws_config/) crate (standard environment variables such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as well as other AWS specific features).

If no credentials are specified, DataFusion CLI will use unsigned requests to S3,
which allows reading from public buckets.

Supported configuration options are:

| Environment Variable | Configuration Option | Description |
| --- | --- | --- |
| `AWS_ACCESS_KEY_ID` | `aws.access_key_id` |  |
| `AWS_SECRET_ACCESS_KEY` | `aws.secret_access_key` |  |
| `AWS_DEFAULT_REGION` | `aws.region` |  |
| `AWS_ENDPOINT` | `aws.endpoint` |  |
| `AWS_SESSION_TOKEN` | `aws.token` |  |
| `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` |  | See [IAM Roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) |
| `AWS_ALLOW_HTTP` |  | If “true”, permit HTTP connections without TLS |
| `AWS_SKIP_SIGNATURE` | `aws.skip_signature` | If “true”, does not sign requests |
|  | `aws.nosign` | Alias for `skip_signature` |

## OSS[#](#oss "Link to this heading")

[Alibaba cloud OSS](https://www.alibabacloud.com/product/object-storage-service) data sources must have connection credentials configured

```
CREATE EXTERNAL TABLE test
STORED AS PARQUET
OPTIONS(
    'aws.access_key_id' '******',
    'aws.secret_access_key' '******',
    'aws.oss.endpoint' 'https://bucket.oss-cn-hangzhou.aliyuncs.com'
)
LOCATION 'oss://bucket/path/file.parquet';
```

The supported OPTIONS are

* access\_key\_id
* secret\_access\_key
* endpoint

Note that the `endpoint` format of oss needs to be: `https://{bucket}.{oss-region-endpoint}`

## COS[#](#cos "Link to this heading")

[Tencent cloud COS](https://cloud.tencent.com/product/cos) data sources data sources must have connection credentials configured

```
CREATE EXTERNAL TABLE test
STORED AS PARQUET
OPTIONS(
    'aws.access_key_id' '******',
    'aws.secret_access_key' '******',
    'aws.cos.endpoint' 'https://cos.ap-singapore.myqcloud.com'
)
LOCATION 'cos://bucket/path/file.parquet';
```

The supported OPTIONS are:

* access\_key\_id
* secret\_access\_key
* endpoint

Note that the `endpoint` format of urls must be: `https://cos.{cos-region-endpoint}`

## GCS[#](#gcs "Link to this heading")

[Google Cloud Storage](https://cloud.google.com/storage) data sources must have connection credentials configured

For example, to create an external table from a file in a GCS bucket

```
CREATE EXTERNAL TABLE test
STORED AS PARQUET
OPTIONS(
    'gcp.service_account_path' '/tmp/gcs.json',
)
LOCATION 'gs://bucket/path/file.parquet';
```

It is also possible to specify the access information using environment variables:

```
$ export GOOGLE_SERVICE_ACCOUNT=/tmp/gcs.json

$ datafusion-cli
DataFusion CLI v21.0.0
> create external table test stored as parquet location 'gs://bucket/path/file.parquet';
0 rows in set. Query took 0.374 seconds.
> select * from test;
+----------+----------+
| column_1 | column_2 |
+----------+----------+
| 1        | 2        |
+----------+----------+
1 row in set. Query took 0.171 seconds.
```

Supported configuration options are:

| Environment Variable | Configuration Option | Description |
| --- | --- | --- |
| `GOOGLE_SERVICE_ACCOUNT` | `gcp.service_account_path` | location of service account file |
| `GOOGLE_SERVICE_ACCOUNT_PATH` | `gcp.service_account_path` | (alias) location of service account file |
| `SERVICE_ACCOUNT` | `gcp.service_account_path` | (alias) location of service account file |
| `GOOGLE_SERVICE_ACCOUNT_KEY` | `gcp.service_account_key` | JSON serialized service account key |
| `GOOGLE_APPLICATION_CREDENTIALS` | `gcp.application_credentials_path` | location of application credentials file |
| `GOOGLE_BUCKET` |  | bucket name |
| `GOOGLE_BUCKET_NAME` |  | (alias) bucket name |

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/cli/datasources.md)

[Show Source](../../_sources/user-guide/cli/datasources.md.txt)

---
# Data Types[#](#data-types "Link to this heading")

DataFusion uses Arrow, and thus the Arrow type system, for query
execution. The SQL types from
[sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs/blob/main/src/ast/data_type.rs#L27)
are mapped to [Arrow data types](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) according to the following table.
This mapping occurs when defining the schema in a `CREATE EXTERNAL TABLE` command or when performing a SQL `CAST` operation.

For background on extension types and custom metadata, see the
[Implementing User Defined Types and Custom Metadata in DataFusion](https://datafusion.apache.org/blog/2025/09/21/custom-types-using-metadata) blog.

You can see the corresponding Arrow type for any SQL expression using
the `arrow_typeof` function. For example:

```
select arrow_typeof(interval '1 month');
+---------------------------------------------------------------------+
| arrow_typeof(IntervalMonthDayNano("79228162514264337593543950336")) |
+---------------------------------------------------------------------+
| Interval(MonthDayNano)                                              |
+---------------------------------------------------------------------+
```

You can cast a SQL expression to a specific Arrow type using the `arrow_cast` function
For example, to cast the output of `now()` to a `Timestamp` with second precision:

```
select arrow_cast(now(), 'Timestamp(s)') as "now()";
+---------------------+
| now()               |
+---------------------+
| 2025-10-24T20:02:45 |
+---------------------+
```

The older syntax still works as well:

```
select arrow_cast(now(), 'Timestamp(Second, None)') as "now()";
+---------------------+
| now()               |
+---------------------+
| 2023-03-03T17:19:21 |
+---------------------+
```

## Character Types[#](#character-types "Link to this heading")

| SQL DataType | Arrow DataType |
| --- | --- |
| `CHAR` | `Utf8View` |
| `VARCHAR` | `Utf8View` |
| `TEXT` | `Utf8View` |
| `STRING` | `Utf8View` |

By default, string types are mapped to `Utf8View`. This can be configured using the `datafusion.sql_parser.map_string_types_to_utf8view` setting. When set to `false`, string types are mapped to `Utf8` instead.

## Numeric Types[#](#numeric-types "Link to this heading")

| SQL DataType | Arrow DataType |
| --- | --- |
| `TINYINT` | `Int8` |
| `SMALLINT` | `Int16` |
| `INT` or `INTEGER` | `Int32` |
| `BIGINT` | `Int64` |
| `TINYINT UNSIGNED` | `UInt8` |
| `SMALLINT UNSIGNED` | `UInt16` |
| `INT UNSIGNED` or `INTEGER UNSIGNED` | `UInt32` |
| `BIGINT UNSIGNED` | `UInt64` |
| `FLOAT` | `Float32` |
| `REAL` | `Float32` |
| `DOUBLE` | `Float64` |
| `DECIMAL(precision, scale)` where precision ≤ 38 | `Decimal128(precision, scale)` |
| `DECIMAL(precision, scale)` where precision > 38 | `Decimal256(precision, scale)` |

The maximum supported precision for `DECIMAL` types is 76.

## Date/Time Types[#](#date-time-types "Link to this heading")

| SQL DataType | Arrow DataType |
| --- | --- |
| `DATE` | `Date32` |
| `TIME` | `Time64(Nanosecond)` |
| `TIMESTAMP` | `Timestamp(Nanosecond, None)` |
| `INTERVAL` | `Interval(IntervalMonthDayNano)` |

## Boolean Types[#](#boolean-types "Link to this heading")

| SQL DataType | Arrow DataType |
| --- | --- |
| `BOOLEAN` | `Boolean` |

## Binary Types[#](#binary-types "Link to this heading")

| SQL DataType | Arrow DataType |
| --- | --- |
| `BYTEA` | `Binary` |

You can create binary literals using a hex string literal such as
`X'1234'` to create a `Binary` value of two bytes, `0x12` and `0x34`.

## Unsupported SQL Types[#](#unsupported-sql-types "Link to this heading")

| SQL Data Type | Arrow DataType |
| --- | --- |
| `UUID` | *Not yet supported* |
| `BLOB` | *Not yet supported* |
| `CLOB` | *Not yet supported* |
| `BINARY` | *Not yet supported* |
| `VARBINARY` | *Not yet supported* |
| `REGCLASS` | *Not yet supported* |
| `NVARCHAR` | *Not yet supported* |
| `CUSTOM` | *Not yet supported* |
| `ARRAY` | *Not yet supported* |
| `ENUM` | *Not yet supported* |
| `SET` | *Not yet supported* |
| `DATETIME` | *Not yet supported* |

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/data_types.md)

[Show Source](../../_sources/user-guide/sql/data_types.md.txt)

---
# Metrics[#](#metrics "Link to this heading")

DataFusion operators expose runtime metrics so you can understand where time is spent and how much data flows through the pipeline. See more in [EXPLAIN ANALYZE](sql/explain.html#explain-analyze).

## Common Metrics[#](#common-metrics "Link to this heading")

### BaselineMetrics[#](#baselinemetrics "Link to this heading")

`BaselineMetrics` are available in most physical operators to capture common measurements.

| Metric | Description |
| --- | --- |
| elapsed\_compute | CPU time the operator actively spends processing work. |
| output\_rows | Total number of rows the operator produces. |
| output\_bytes | Memory usage of all output batches. Note: This value may be overestimated. If multiple output `RecordBatch` instances share underlying memory buffers, their sizes will be counted multiple times. |
| output\_batches | Total number of output batches the operator produces. |

## Operator-specific Metrics[#](#operator-specific-metrics "Link to this heading")

### FilterExec[#](#filterexec "Link to this heading")

| Metric | Description |
| --- | --- |
| selectivity | Selectivity of the filter, calculated as output\_rows / input\_rows |

## TODO[#](#todo "Link to this heading")

Add metrics for the remaining operators

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/metrics.md)

[Show Source](../_sources/user-guide/metrics.md.txt)

---
# Crate Configuration[#](#crate-configuration "Link to this heading")

This section contains information on how to configure builds of DataFusion in
your Rust project. The [Configuration Settings](configs.html) section lists options that
control additional aspects DataFusion’s runtime behavior.

## Using the nightly DataFusion builds[#](#using-the-nightly-datafusion-builds "Link to this heading")

DataFusion changes are published to `crates.io` according to the [release schedule](https://github.com/apache/datafusion/blob/main/dev/release/README.md#release-process)

If you would like to use or test versions of the DataFusion code which are
merged but not yet published, you can use Cargo’s [support for adding
dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#specifying-dependencies) directly to a GitHub branch:

```
datafusion = { git = "https://github.com/apache/datafusion", branch = "main"}
```

Also it works on the package level

```
datafusion-common = { git = "https://github.com/apache/datafusion", branch = "main", package = "datafusion-common"}
```

And with features

```
datafusion = { git = "https://github.com/apache/datafusion", branch = "main", default-features = false, features = ["unicode_expressions"] }
```

More on [Cargo dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#specifying-dependencies)

## Optimizing Builds[#](#optimizing-builds "Link to this heading")

Here are several suggestions to get the Rust compler to produce faster code when
compiling DataFusion. Note that these changes may increase compile time and
binary size.

### Generate Code with CPU Specific Instructions[#](#generate-code-with-cpu-specific-instructions "Link to this heading")

By default, the Rust compiler produces code that runs on a wide range of CPUs,
but may not take advantage of all the features of your specific CPU (such as
certain [SIMD instructions](https://en.wikipedia.org/wiki/SIMD)). This is especially true for x86\_64 CPUs, where the
default target is `x86_64-unknown-linux-gnu`, which only guarantees support for
the `SSE2` instruction set. DataFusion can benefit from the more advanced
instructions in the `AVX2` and `AVX512` to speed up operations like filtering,
aggregation, and joins. To tell the Rust compiler to use these instructions, set
the `RUSTFLAGS` environment variable to specify a more specific target CPU.

We recommend setting `target-cpu` or at least `avx2`, or preferably at least
`native` (whatever the current CPU is). For example, to build and run DataFusion
with optimizations for your current CPU:

```
RUSTFLAGS='-C target-cpu=native' cargo run --release
```

### Enable Link Time Optimization / Single Codegen Unit[#](#enable-link-time-optimization-single-codegen-unit "Link to this heading")

You can potentially improve your performance by compiling DataFusion into a
single codegen unit which gives the Rust compiler more opportunity to optimize
across crate boundaries. To do so, modify your projects’ `Cargo.toml` to include
`lto = true` and `codegen-units = 1` as shown below. Beware that using a single
codegen unit *significantly* increases `--release` build times.

```
[profile.release]
lto = true
codegen-units = 1
```

### Profile Guided Optimization (PGO)[#](#profile-guided-optimization-pgo "Link to this heading")

Profile Guided Optimization can improve DataFusion performance by up to 25%. It works by compiling with instrumentation, running representative workloads to collect profile data, then recompiling with optimizations based on that data.

Build with instrumentation:

```
RUSTFLAGS="-C profile-generate=/tmp/pgo-data" cargo build --release
```

Run your workloads to collect profile data. Use benchmarks like TPCH or Clickbench, or your actual production queries:

```
./target/release/your-datafusion-app --benchmark
```

Rebuild using the collected profile:

```
RUSTFLAGS="-C profile-use=/tmp/pgo-data" cargo build --release
```

Tips:

* Use workloads that match your production patterns
* Run multiple iterations during profiling for better coverage
* Combine with LTO and CPU-specific optimizations for best results

See the [Rust compiler guide](https://rustc-dev-guide.rust-lang.org/building/optimized-build.html#profile-guided-optimization) for more details. Discussion and results in [issue #9507](https://github.com/apache/datafusion/issues/9507).

### Alternate Allocator: `snmalloc`[#](#alternate-allocator-snmalloc "Link to this heading")

You can also use [snmalloc-rs](https://crates.io/crates/snmalloc-rs) crate as
the memory allocator for DataFusion to improve performance. To do so, add the
dependency to your `Cargo.toml` as shown below.

```
[dependencies]
snmalloc-rs = "0.3"
```

Then, in `main.rs.` update the memory allocator with the below after your imports:

```
use datafusion::prelude::*;

#[global_allocator]
static ALLOC: snmalloc_rs::SnMalloc = snmalloc_rs::SnMalloc;

#[tokio::main]
async fn main() -> datafusion::error::Result<()> {
  Ok(())
}
```

## Enable Backtraces[#](#enable-backtraces "Link to this heading")

By default, Datafusion returns errors as a plain text message. You can enable more verbose details about the error,
such as backtraces by enabling the `backtrace` feature to your `Cargo.toml` file like this:

```
datafusion = { version = "53.0.0", features = ["backtrace"]}
```

Set environment [variables](https://doc.rust-lang.org/std/backtrace/index.html#environment-variables)

```
RUST_BACKTRACE=1 ./target/debug/datafusion-cli
DataFusion CLI v31.0.0
> select row_numer() over (partition by a order by a) from (select 1 a);
Error during planning: Invalid function 'row_numer'.
Did you mean 'ROW_NUMBER'?

backtrace:    0: std::backtrace_rs::backtrace::libunwind::trace
             at /rustc/5680fa18feaa87f3ff04063800aec256c3d4b4be/library/std/src/../../backtrace/src/backtrace/libunwind.rs:93:5
   1: std::backtrace_rs::backtrace::trace_unsynchronized
             at /rustc/5680fa18feaa87f3ff04063800aec256c3d4b4be/library/std/src/../../backtrace/src/backtrace/mod.rs:66:5
   2: std::backtrace::Backtrace::create
             at /rustc/5680fa18feaa87f3ff04063800aec256c3d4b4be/library/std/src/backtrace.rs:332:13
   3: std::backtrace::Backtrace::capture
             at /rustc/5680fa18feaa87f3ff04063800aec256c3d4b4be/library/std/src/backtrace.rs:298:9
   4: datafusion_common::error::DataFusionError::get_back_trace
             at /datafusion/datafusion/common/src/error.rs:436:30
   5: datafusion_sql::expr::function::<impl datafusion_sql::planner::SqlToRel<S>>::sql_function_to_expr
   ............
```

The backtraces are useful when debugging code. If there is a test in `datafusion/core/src/physical_planner.rs`

```
#[tokio::test]
async fn test_get_backtrace_for_failed_code() -> Result<()> {
    let ctx = SessionContext::new();

    let sql = "
    select row_numer() over (partition by a order by a) from (select 1 a);
    ";

    let _ = ctx.sql(sql).await?.collect().await?;

    Ok(())
}
```

To obtain a backtrace:

```
cargo build --features=backtrace
RUST_BACKTRACE=1 cargo test --features=backtrace --package datafusion --lib -- physical_planner::tests::test_get_backtrace_for_failed_code --exact --nocapture

running 1 test
Error: Plan("Invalid function 'row_numer'.\nDid you mean 'ROW_NUMBER'?\n\nbacktrace:    0: std::backtrace_rs::backtrace::libunwind::trace\n             at /rustc/129f3b9964af4d4a709d1383930ade12dfe7c081/library/std/src/../../backtrace/src/backtrace/libunwind.rs:105:5\n   1: std::backtrace_rs::backtrace::trace_unsynchronized\n...
```

Note: The backtrace wrapped into systems calls, so some steps on top of the backtrace can be ignored

To show the backtrace in a pretty-printed format use `eprintln!("{e}");`.

```
#[tokio::test]
async fn test_get_backtrace_for_failed_code() -> Result<()> {
    let ctx = SessionContext::new();

    let sql = "select row_numer() over (partition by a order by a) from (select 1 a);";

    let _ = match ctx.sql(sql).await {
        Ok(result) => result.show().await?,
        Err(e) => {
            eprintln!("{e}");
        }
    };

    Ok(())
}
```

Then run the test:

```
$ RUST_BACKTRACE=1 cargo test --features=backtrace --package datafusion --lib -- physical_planner::tests::test_get_backtrace_for_failed_code --exact --nocapture

running 1 test
Error during planning: Invalid function 'row_numer'.
Did you mean 'ROW_NUMBER'?

backtrace:    0: std::backtrace_rs::backtrace::libunwind::trace
             at /rustc/129f3b9964af4d4a709d1383930ade12dfe7c081/library/std/src/../../backtrace/src/backtrace/libunwind.rs:105:5
   1: std::backtrace_rs::backtrace::trace_unsynchronized
             at /rustc/129f3b9964af4d4a709d1383930ade12dfe7c081/library/std/src/../../backtrace/src/backtrace/mod.rs:66:5
   2: std::backtrace::Backtrace::create
             at /rustc/129f3b9964af4d4a709d1383930ade12dfe7c081/library/std/src/backtrace.rs:331:13
   3: std::backtrace::Backtrace::capture
   ...
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/crate-configuration.md)

[Show Source](../_sources/user-guide/crate-configuration.md.txt)

---
# Aggregate Functions[#](#aggregate-functions "Link to this heading")

Aggregate functions operate on a set of values to compute a single result.

## Filter clause[#](#filter-clause "Link to this heading")

Aggregate functions support the SQL `FILTER (WHERE ...)` clause to restrict which input rows contribute to the aggregate result.

```
function([exprs]) FILTER (WHERE condition)
```

Example:

```
SELECT
  sum(salary) FILTER (WHERE salary > 0) AS sum_positive_salaries,
  count(*)    FILTER (WHERE active)     AS active_count
FROM employees;
```

Note: When no rows pass the filter, `COUNT` returns `0` while `SUM`/`AVG`/`MIN`/`MAX` return `NULL`.

## WITHIN GROUP / Ordered-set aggregates[#](#within-group-ordered-set-aggregates "Link to this heading")

Some aggregate functions accept the SQL `WITHIN GROUP (ORDER BY ...)` clause to specify the ordering the
aggregate relies on. In DataFusion this is opt-in: only aggregate functions whose implementation returns
`true` from `AggregateUDFImpl::supports_within_group_clause()` accept the `WITHIN GROUP` clause. Attempting to
use `WITHIN GROUP` with a regular aggregate (for example, `SELECT SUM(x) WITHIN GROUP (ORDER BY x)`) will fail
during planning with an error: “WITHIN GROUP is only supported for ordered-set aggregate functions”.

Currently, the built-in aggregate functions that support `WITHIN GROUP` are:

* `percentile_cont` — exact percentile aggregate (also available as `percentile_cont(column, percentile)`)
* `approx_percentile_cont` — approximate percentile using the t-digest algorithm
* `approx_percentile_cont_with_weight` — approximate weighted percentile using the t-digest algorithm

Note: rank-like functions such as `rank()`, `dense_rank()`, and `percent_rank()` are window functions and
use the `OVER (...)` clause; they are not ordered-set aggregates that accept `WITHIN GROUP` in DataFusion.

Example (ordered-set aggregate):

```
percentile_cont(0.5) WITHIN GROUP (ORDER BY value)
```

Example (invalid usage — planner will error):

```
-- This will fail: SUM is not an ordered-set aggregate
SELECT SUM(x) WITHIN GROUP (ORDER BY x) FROM t;
```

## General Functions[#](#general-functions "Link to this heading")

* [array\_agg](#array-agg)
* [avg](#avg)
* [bit\_and](#bit-and)
* [bit\_or](#bit-or)
* [bit\_xor](#bit-xor)
* [bool\_and](#bool-and)
* [bool\_or](#bool-or)
* [count](#count)
* [first\_value](#first-value)
* [grouping](#grouping)
* [last\_value](#last-value)
* [max](#max)
* [mean](#mean)
* [median](#median)
* [min](#min)
* [percentile\_cont](#percentile-cont)
* [quantile\_cont](#quantile-cont)
* [string\_agg](#string-agg)
* [sum](#sum)
* [var](#var)
* [var\_pop](#var-pop)
* [var\_population](#var-population)
* [var\_samp](#var-samp)
* [var\_sample](#var-sample)

### `array_agg`[#](#array-agg "Link to this heading")

Returns an array created from the expression elements. If ordering is required, elements are inserted in the specified order.
This aggregation function can only mix DISTINCT and ORDER BY if the ordering expression is exactly the same as the argument expression.

```
array_agg(expression [ORDER BY expression])
```

#### Arguments[#](#arguments "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#example "Link to this heading")

```
> SELECT array_agg(column_name ORDER BY other_column) FROM table_name;
+-----------------------------------------------+
| array_agg(column_name ORDER BY other_column)  |
+-----------------------------------------------+
| [element1, element2, element3]                |
+-----------------------------------------------+
> SELECT array_agg(DISTINCT column_name ORDER BY column_name) FROM table_name;
+--------------------------------------------------------+
| array_agg(DISTINCT column_name ORDER BY column_name)  |
+--------------------------------------------------------+
| [element1, element2, element3]                         |
+--------------------------------------------------------+
```

### `avg`[#](#avg "Link to this heading")

Returns the average of numeric values in the specified column.

```
avg(expression)
```

#### Arguments[#](#id1 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id2 "Link to this heading")

```
> SELECT avg(column_name) FROM table_name;
+---------------------------+
| avg(column_name)           |
+---------------------------+
| 42.75                      |
+---------------------------+
```

#### Aliases[#](#aliases "Link to this heading")

* mean

### `bit_and`[#](#bit-and "Link to this heading")

Computes the bitwise AND of all non-null input values.

```
bit_and(expression)
```

#### Arguments[#](#id3 "Link to this heading")

* **expression**: Integer expression to operate on. Can be a constant, column, or function, and any combination of operators.

### `bit_or`[#](#bit-or "Link to this heading")

Computes the bitwise OR of all non-null input values.

```
bit_or(expression)
```

#### Arguments[#](#id4 "Link to this heading")

* **expression**: Integer expression to operate on. Can be a constant, column, or function, and any combination of operators.

### `bit_xor`[#](#bit-xor "Link to this heading")

Computes the bitwise exclusive OR of all non-null input values.

```
bit_xor(expression)
```

#### Arguments[#](#id5 "Link to this heading")

* **expression**: Integer expression to operate on. Can be a constant, column, or function, and any combination of operators.

### `bool_and`[#](#bool-and "Link to this heading")

Returns true if all non-null input values are true, otherwise false.

```
bool_and(expression)
```

#### Arguments[#](#id6 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id7 "Link to this heading")

```
> SELECT bool_and(column_name) FROM table_name;
+----------------------------+
| bool_and(column_name)       |
+----------------------------+
| true                        |
+----------------------------+
```

### `bool_or`[#](#bool-or "Link to this heading")

Returns true if all non-null input values are true, otherwise false.

```
bool_and(expression)
```

#### Arguments[#](#id8 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id9 "Link to this heading")

```
> SELECT bool_and(column_name) FROM table_name;
+----------------------------+
| bool_and(column_name)       |
+----------------------------+
| true                        |
+----------------------------+
```

### `count`[#](#count "Link to this heading")

Returns the number of non-null values in the specified column. To include null values in the total count, use `count(*)`.

```
count(expression)
```

#### Arguments[#](#id10 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id11 "Link to this heading")

```
> SELECT count(column_name) FROM table_name;
+-----------------------+
| count(column_name)     |
+-----------------------+
| 100                   |
+-----------------------+

> SELECT count(*) FROM table_name;
+------------------+
| count(*)         |
+------------------+
| 120              |
+------------------+
```

### `first_value`[#](#first-value "Link to this heading")

Returns the first element in an aggregation group according to the requested ordering. If no ordering is given, returns an arbitrary element from the group.

```
first_value(expression [ORDER BY expression])
```

#### Arguments[#](#id12 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id13 "Link to this heading")

```
> SELECT first_value(column_name ORDER BY other_column) FROM table_name;
+-----------------------------------------------+
| first_value(column_name ORDER BY other_column)|
+-----------------------------------------------+
| first_element                                 |
+-----------------------------------------------+
```

### `grouping`[#](#grouping "Link to this heading")

Returns 1 if the data is aggregated across the specified column, or 0 if it is not aggregated in the result set.

```
grouping(expression)
```

#### Arguments[#](#id14 "Link to this heading")

* **expression**: Expression to evaluate whether data is aggregated across the specified column. Can be a constant, column, or function.

#### Example[#](#id15 "Link to this heading")

```
> SELECT column_name, GROUPING(column_name) AS group_column
  FROM table_name
  GROUP BY GROUPING SETS ((column_name), ());
+-------------+-------------+
| column_name | group_column |
+-------------+-------------+
| value1      | 0           |
| value2      | 0           |
| NULL        | 1           |
+-------------+-------------+
```

### `last_value`[#](#last-value "Link to this heading")

Returns the last element in an aggregation group according to the requested ordering. If no ordering is given, returns an arbitrary element from the group.

```
last_value(expression [ORDER BY expression])
```

#### Arguments[#](#id16 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id17 "Link to this heading")

```
> SELECT last_value(column_name ORDER BY other_column) FROM table_name;
+-----------------------------------------------+
| last_value(column_name ORDER BY other_column) |
+-----------------------------------------------+
| last_element                                  |
+-----------------------------------------------+
```

### `max`[#](#max "Link to this heading")

Returns the maximum value in the specified column.

```
max(expression)
```

#### Arguments[#](#id18 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id19 "Link to this heading")

```
> SELECT max(column_name) FROM table_name;
+----------------------+
| max(column_name)      |
+----------------------+
| 150                  |
+----------------------+
```

### `mean`[#](#mean "Link to this heading")

*Alias of [avg](#avg).*

### `median`[#](#median "Link to this heading")

Returns the median value in the specified column.

```
median(expression)
```

#### Arguments[#](#id20 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id21 "Link to this heading")

```
> SELECT median(column_name) FROM table_name;
+----------------------+
| median(column_name)   |
+----------------------+
| 45.5                 |
+----------------------+
```

### `min`[#](#min "Link to this heading")

Returns the minimum value in the specified column.

```
min(expression)
```

#### Arguments[#](#id22 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id23 "Link to this heading")

```
> SELECT min(column_name) FROM table_name;
+----------------------+
| min(column_name)      |
+----------------------+
| 12                   |
+----------------------+
```

### `percentile_cont`[#](#percentile-cont "Link to this heading")

Returns the exact percentile of input values, interpolating between values if needed.

```
percentile_cont(percentile) WITHIN GROUP (ORDER BY expression)
```

#### Arguments[#](#id24 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **percentile**: Percentile to compute. Must be a float value between 0 and 1 (inclusive).

#### Example[#](#id25 "Link to this heading")

```
> SELECT percentile_cont(0.75) WITHIN GROUP (ORDER BY column_name) FROM table_name;
+----------------------------------------------------------+
| percentile_cont(0.75) WITHIN GROUP (ORDER BY column_name) |
+----------------------------------------------------------+
| 45.5                                                     |
+----------------------------------------------------------+
```

An alternate syntax is also supported:

```
> SELECT percentile_cont(column_name, 0.75) FROM table_name;
+---------------------------------------+
| percentile_cont(column_name, 0.75)    |
+---------------------------------------+
| 45.5                                  |
+---------------------------------------+
```

#### Aliases[#](#id26 "Link to this heading")

* quantile\_cont

### `quantile_cont`[#](#quantile-cont "Link to this heading")

*Alias of [percentile\_cont](#percentile-cont).*

### `string_agg`[#](#string-agg "Link to this heading")

Concatenates the values of string expressions and places separator values between them. If ordering is required, strings are concatenated in the specified order. This aggregation function can only mix DISTINCT and ORDER BY if the ordering expression is exactly the same as the first argument expression.

```
string_agg([DISTINCT] expression, delimiter [ORDER BY expression])
```

#### Arguments[#](#id27 "Link to this heading")

* **expression**: The string expression to concatenate. Can be a column or any valid string expression.
* **delimiter**: A literal string used as a separator between the concatenated values.

#### Example[#](#id28 "Link to this heading")

```
> SELECT string_agg(name, ', ') AS names_list
  FROM employee;
+--------------------------+
| names_list               |
+--------------------------+
| Alice, Bob, Bob, Charlie |
+--------------------------+
> SELECT string_agg(name, ', ' ORDER BY name DESC) AS names_list
  FROM employee;
+--------------------------+
| names_list               |
+--------------------------+
| Charlie, Bob, Bob, Alice |
+--------------------------+
> SELECT string_agg(DISTINCT name, ', ' ORDER BY name DESC) AS names_list
  FROM employee;
+--------------------------+
| names_list               |
+--------------------------+
| Charlie, Bob, Alice |
+--------------------------+
```

### `sum`[#](#sum "Link to this heading")

Returns the sum of all values in the specified column.

```
sum(expression)
```

#### Arguments[#](#id29 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id30 "Link to this heading")

```
> SELECT sum(column_name) FROM table_name;
+-----------------------+
| sum(column_name)       |
+-----------------------+
| 12345                 |
+-----------------------+
```

### `var`[#](#var "Link to this heading")

Returns the statistical sample variance of a set of numbers.

```
var(expression)
```

#### Arguments[#](#id31 "Link to this heading")

* **expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Aliases[#](#id32 "Link to this heading")

* var\_sample
* var\_samp

### `var_pop`[#](#var-pop "Link to this heading")

Returns the statistical population variance of a set of numbers.

```
var_pop(expression)
```

#### Arguments[#](#id33 "Link to this heading")

* **expression**: Numeric expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Aliases[#](#id34 "Link to this heading")

* var\_population

### `var_population`[#](#var-population "Link to this heading")

*Alias of [var\_pop](#var-pop).*

### `var_samp`[#](#var-samp "Link to this heading")

*Alias of [var](#var).*

### `var_sample`[#](#var-sample "Link to this heading")

*Alias of [var](#var).*

## Statistical Functions[#](#statistical-functions "Link to this heading")

* [corr](#corr)
* [covar](#covar)
* [covar\_pop](#covar-pop)
* [covar\_samp](#covar-samp)
* [nth\_value](#nth-value)
* [regr\_avgx](#regr-avgx)
* [regr\_avgy](#regr-avgy)
* [regr\_count](#regr-count)
* [regr\_intercept](#regr-intercept)
* [regr\_r2](#regr-r2)
* [regr\_slope](#regr-slope)
* [regr\_sxx](#regr-sxx)
* [regr\_sxy](#regr-sxy)
* [regr\_syy](#regr-syy)
* [stddev](#stddev)
* [stddev\_pop](#stddev-pop)
* [stddev\_samp](#stddev-samp)

### `corr`[#](#corr "Link to this heading")

Returns the coefficient of correlation between two numeric values.

```
corr(expression1, expression2)
```

#### Arguments[#](#id35 "Link to this heading")

* **expression1**: First expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression2**: Second expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id36 "Link to this heading")

```
> SELECT corr(column1, column2) FROM table_name;
+--------------------------------+
| corr(column1, column2)         |
+--------------------------------+
| 0.85                           |
+--------------------------------+
```

### `covar`[#](#covar "Link to this heading")

*Alias of [covar\_samp](#covar-samp).*

### `covar_pop`[#](#covar-pop "Link to this heading")

Returns the sample covariance of a set of number pairs.

```
covar_samp(expression1, expression2)
```

#### Arguments[#](#id37 "Link to this heading")

* **expression1**: First expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression2**: Second expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id38 "Link to this heading")

```
> SELECT covar_samp(column1, column2) FROM table_name;
+-----------------------------------+
| covar_samp(column1, column2)      |
+-----------------------------------+
| 8.25                              |
+-----------------------------------+
```

### `covar_samp`[#](#covar-samp "Link to this heading")

Returns the sample covariance of a set of number pairs.

```
covar_samp(expression1, expression2)
```

#### Arguments[#](#id39 "Link to this heading")

* **expression1**: First expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression2**: Second expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id40 "Link to this heading")

```
> SELECT covar_samp(column1, column2) FROM table_name;
+-----------------------------------+
| covar_samp(column1, column2)      |
+-----------------------------------+
| 8.25                              |
+-----------------------------------+
```

#### Aliases[#](#id41 "Link to this heading")

* covar

### `nth_value`[#](#nth-value "Link to this heading")

Returns the nth value in a group of values.

```
nth_value(expression, n ORDER BY expression)
```

#### Arguments[#](#id42 "Link to this heading")

* **expression**: The column or expression to retrieve the nth value from.
* **n**: The position (nth) of the value to retrieve, based on the ordering.

#### Example[#](#id43 "Link to this heading")

```
> SELECT dept_id, salary, NTH_VALUE(salary, 2) OVER (PARTITION BY dept_id ORDER BY salary ASC) AS second_salary_by_dept
  FROM employee;
+---------+--------+-------------------------+
| dept_id | salary | second_salary_by_dept   |
+---------+--------+-------------------------+
| 1       | 30000  | NULL                    |
| 1       | 40000  | 40000                   |
| 1       | 50000  | 40000                   |
| 2       | 35000  | NULL                    |
| 2       | 45000  | 45000                   |
+---------+--------+-------------------------+
```

### `regr_avgx`[#](#regr-avgx "Link to this heading")

Computes the average of the independent variable (input) expression\_x for the non-null paired data points.

```
regr_avgx(expression_y, expression_x)
```

#### Arguments[#](#id44 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id45 "Link to this heading")

```
create table daily_sales(day int, total_sales int) as values (1,100), (2,150), (3,200), (4,NULL), (5,250);
select * from daily_sales;
+-----+-------------+
| day | total_sales |
| --- | ----------- |
| 1   | 100         |
| 2   | 150         |
| 3   | 200         |
| 4   | NULL        |
| 5   | 250         |
+-----+-------------+

SELECT regr_avgx(total_sales, day) AS avg_day FROM daily_sales;
+----------+
| avg_day  |
+----------+
|   2.75   |
+----------+
```

### `regr_avgy`[#](#regr-avgy "Link to this heading")

Computes the average of the dependent variable (output) expression\_y for the non-null paired data points.

```
regr_avgy(expression_y, expression_x)
```

#### Arguments[#](#id46 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id47 "Link to this heading")

```
create table daily_temperature(day int, temperature int) as values (1,30), (2,32), (3, NULL), (4,35), (5,36);
select * from daily_temperature;
+-----+-------------+
| day | temperature |
| --- | ----------- |
| 1   | 30          |
| 2   | 32          |
| 3   | NULL        |
| 4   | 35          |
| 5   | 36          |
+-----+-------------+

-- temperature as Dependent Variable(Y), day as Independent Variable(X)
SELECT regr_avgy(temperature, day) AS avg_temperature FROM daily_temperature;
+-----------------+
| avg_temperature |
+-----------------+
| 33.25           |
+-----------------+
```

### `regr_count`[#](#regr-count "Link to this heading")

Counts the number of non-null paired data points.

```
regr_count(expression_y, expression_x)
```

#### Arguments[#](#id48 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id49 "Link to this heading")

```
create table daily_metrics(day int, user_signups int) as values (1,100), (2,120), (3, NULL), (4,110), (5,NULL);
select * from daily_metrics;
+-----+---------------+
| day | user_signups  |
| --- | ------------- |
| 1   | 100           |
| 2   | 120           |
| 3   | NULL          |
| 4   | 110           |
| 5   | NULL          |
+-----+---------------+

SELECT regr_count(user_signups, day) AS valid_pairs FROM daily_metrics;
+-------------+
| valid_pairs |
+-------------+
| 3           |
+-------------+
```

### `regr_intercept`[#](#regr-intercept "Link to this heading")

Computes the y-intercept of the linear regression line. For the equation (y = kx + b), this function returns b.

```
regr_intercept(expression_y, expression_x)
```

#### Arguments[#](#id50 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id51 "Link to this heading")

```
create table weekly_performance(week int, productivity_score int) as values (1,60), (2,65), (3, 70), (4,75), (5,80);
select * from weekly_performance;
+------+---------------------+
| week | productivity_score  |
| ---- | ------------------- |
| 1    | 60                  |
| 2    | 65                  |
| 3    | 70                  |
| 4    | 75                  |
| 5    | 80                  |
+------+---------------------+

SELECT regr_intercept(productivity_score, week) AS intercept FROM weekly_performance;
+----------+
|intercept|
|intercept |
+----------+
|  55      |
+----------+
```

### `regr_r2`[#](#regr-r2 "Link to this heading")

Computes the square of the correlation coefficient between the independent and dependent variables.

```
regr_r2(expression_y, expression_x)
```

#### Arguments[#](#id52 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id53 "Link to this heading")

```
create table weekly_performance(day int ,user_signups int) as values (1,60), (2,65), (3, 70), (4,75), (5,80);
select * from weekly_performance;
+-----+--------------+
| day | user_signups |
+-----+--------------+
| 1   | 60           |
| 2   | 65           |
| 3   | 70           |
| 4   | 75           |
| 5   | 80           |
+-----+--------------+

SELECT regr_r2(user_signups, day) AS r_squared FROM weekly_performance;
+---------+
|r_squared|
+---------+
| 1.0     |
+---------+
```

### `regr_slope`[#](#regr-slope "Link to this heading")

Returns the slope of the linear regression line for non-null pairs in aggregate columns. Given input column Y and X: regr\_slope(Y, X) returns the slope (k in Y = k\*X + b) using minimal RSS fitting.

```
regr_slope(expression_y, expression_x)
```

#### Arguments[#](#id54 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id55 "Link to this heading")

```
create table weekly_performance(day int, user_signups int) as values (1,60), (2,65), (3, 70), (4,75), (5,80);
select * from weekly_performance;
+-----+--------------+
| day | user_signups |
+-----+--------------+
| 1   | 60           |
| 2   | 65           |
| 3   | 70           |
| 4   | 75           |
| 5   | 80           |
+-----+--------------+

SELECT regr_slope(user_signups, day) AS slope FROM weekly_performance;
+--------+
| slope  |
+--------+
| 5.0    |
+--------+
```

### `regr_sxx`[#](#regr-sxx "Link to this heading")

Computes the sum of squares of the independent variable.

```
regr_sxx(expression_y, expression_x)
```

#### Arguments[#](#id56 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id57 "Link to this heading")

```
create table study_hours(student_id int, hours int, test_score int) as values (1,2,55), (2,4,65), (3,6,75), (4,8,85), (5,10,95);
select * from study_hours;
+------------+-------+------------+
| student_id | hours | test_score |
+------------+-------+------------+
| 1          | 2     | 55         |
| 2          | 4     | 65         |
| 3          | 6     | 75         |
| 4          | 8     | 85         |
| 5          | 10    | 95         |
+------------+-------+------------+

SELECT regr_sxx(test_score, hours) AS sxx FROM study_hours;
+------+
| sxx  |
+------+
| 40.0 |
+------+
```

### `regr_sxy`[#](#regr-sxy "Link to this heading")

Computes the sum of products of paired data points.

```
regr_sxy(expression_y, expression_x)
```

#### Arguments[#](#id58 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id59 "Link to this heading")

```
create table employee_productivity(week int, productivity_score int) as values(1,60), (2,65), (3,70);
select * from employee_productivity;
+------+--------------------+
| week | productivity_score |
+------+--------------------+
| 1    | 60                 |
| 2    | 65                 |
| 3    | 70                 |
+------+--------------------+

SELECT regr_sxy(productivity_score, week) AS sum_product_deviations FROM employee_productivity;
+------------------------+
| sum_product_deviations |
+------------------------+
|       10.0             |
+------------------------+
```

### `regr_syy`[#](#regr-syy "Link to this heading")

Computes the sum of squares of the dependent variable.

```
regr_syy(expression_y, expression_x)
```

#### Arguments[#](#id60 "Link to this heading")

* **expression\_y**: Dependent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **expression\_x**: Independent variable expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id61 "Link to this heading")

```
create table employee_productivity(week int, productivity_score int) as values (1,60), (2,65), (3,70);
select * from employee_productivity;
+------+--------------------+
| week | productivity_score |
+------+--------------------+
| 1    | 60                 |
| 2    | 65                 |
| 3    | 70                 |
+------+--------------------+

SELECT regr_syy(productivity_score, week) AS sum_squares_y FROM employee_productivity;
+---------------+
| sum_squares_y |
+---------------+
|    50.0       |
+---------------+
```

### `stddev`[#](#stddev "Link to this heading")

Returns the standard deviation of a set of numbers.

```
stddev(expression)
```

#### Arguments[#](#id62 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id63 "Link to this heading")

```
> SELECT stddev(column_name) FROM table_name;
+----------------------+
| stddev(column_name)   |
+----------------------+
| 12.34                |
+----------------------+
```

#### Aliases[#](#id64 "Link to this heading")

* stddev\_samp

### `stddev_pop`[#](#stddev-pop "Link to this heading")

Returns the population standard deviation of a set of numbers.

```
stddev_pop(expression)
```

#### Arguments[#](#id65 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id66 "Link to this heading")

```
> SELECT stddev_pop(column_name) FROM table_name;
+--------------------------+
| stddev_pop(column_name)   |
+--------------------------+
| 10.56                    |
+--------------------------+
```

### `stddev_samp`[#](#stddev-samp "Link to this heading")

*Alias of [stddev](#stddev).*

## Approximate Functions[#](#approximate-functions "Link to this heading")

* [approx\_distinct](#approx-distinct)
* [approx\_median](#approx-median)
* [approx\_percentile\_cont](#approx-percentile-cont)
* [approx\_percentile\_cont\_with\_weight](#approx-percentile-cont-with-weight)

### `approx_distinct`[#](#approx-distinct "Link to this heading")

Returns the approximate number of distinct input values calculated using the HyperLogLog algorithm.

```
approx_distinct(expression)
```

#### Arguments[#](#id67 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id68 "Link to this heading")

```
> SELECT approx_distinct(column_name) FROM table_name;
+-----------------------------------+
| approx_distinct(column_name)      |
+-----------------------------------+
| 42                                |
+-----------------------------------+
```

### `approx_median`[#](#approx-median "Link to this heading")

Returns the approximate median (50th percentile) of input values. It is an alias of `approx_percentile_cont(0.5) WITHIN GROUP (ORDER BY x)`.

```
approx_median(expression)
```

#### Arguments[#](#id69 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.

#### Example[#](#id70 "Link to this heading")

```
> SELECT approx_median(column_name) FROM table_name;
+-----------------------------------+
| approx_median(column_name)        |
+-----------------------------------+
| 23.5                              |
+-----------------------------------+
```

### `approx_percentile_cont`[#](#approx-percentile-cont "Link to this heading")

Returns the approximate percentile of input values using the t-digest algorithm.

```
approx_percentile_cont(percentile [, centroids]) WITHIN GROUP (ORDER BY expression)
```

#### Arguments[#](#id71 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **percentile**: Percentile to compute. Must be a float value between 0 and 1 (inclusive).
* **centroids**: Number of centroids to use in the t-digest algorithm. *Default is 100*. A higher number results in more accurate approximation but requires more memory.

#### Example[#](#id72 "Link to this heading")

```
> SELECT approx_percentile_cont(0.75) WITHIN GROUP (ORDER BY column_name) FROM table_name;
+------------------------------------------------------------------+
| approx_percentile_cont(0.75) WITHIN GROUP (ORDER BY column_name) |
+------------------------------------------------------------------+
| 65.0                                                             |
+------------------------------------------------------------------+
> SELECT approx_percentile_cont(0.75, 100) WITHIN GROUP (ORDER BY column_name) FROM table_name;
+-----------------------------------------------------------------------+
| approx_percentile_cont(0.75, 100) WITHIN GROUP (ORDER BY column_name) |
+-----------------------------------------------------------------------+
| 65.0                                                                  |
+-----------------------------------------------------------------------+
```

An alternate syntax is also supported:

```
> SELECT approx_percentile_cont(column_name, 0.75) FROM table_name;
+-----------------------------------------------+
| approx_percentile_cont(column_name, 0.75)     |
+-----------------------------------------------+
| 65.0                                          |
+-----------------------------------------------+

> SELECT approx_percentile_cont(column_name, 0.75, 100) FROM table_name;
+----------------------------------------------------------+
| approx_percentile_cont(column_name, 0.75, 100)           |
+----------------------------------------------------------+
| 65.0                                                     |
+----------------------------------------------------------+
```

### `approx_percentile_cont_with_weight`[#](#approx-percentile-cont-with-weight "Link to this heading")

Returns the weighted approximate percentile of input values using the t-digest algorithm.

```
approx_percentile_cont_with_weight(weight, percentile [, centroids]) WITHIN GROUP (ORDER BY expression)
```

#### Arguments[#](#id73 "Link to this heading")

* **expression**: The expression to operate on. Can be a constant, column, or function, and any combination of operators.
* **weight**: Expression to use as weight. Can be a constant, column, or function, and any combination of arithmetic operators.
* **percentile**: Percentile to compute. Must be a float value between 0 and 1 (inclusive).
* **centroids**: Number of centroids to use in the t-digest algorithm. *Default is 100*. A higher number results in more accurate approximation but requires more memory.

#### Example[#](#id74 "Link to this heading")

```
> SELECT approx_percentile_cont_with_weight(weight_column, 0.90) WITHIN GROUP (ORDER BY column_name) FROM table_name;
+---------------------------------------------------------------------------------------------+
| approx_percentile_cont_with_weight(weight_column, 0.90) WITHIN GROUP (ORDER BY column_name) |
+---------------------------------------------------------------------------------------------+
| 78.5                                                                                        |
+---------------------------------------------------------------------------------------------+
> SELECT approx_percentile_cont_with_weight(weight_column, 0.90, 100) WITHIN GROUP (ORDER BY column_name) FROM table_name;
+--------------------------------------------------------------------------------------------------+
| approx_percentile_cont_with_weight(weight_column, 0.90, 100) WITHIN GROUP (ORDER BY column_name) |
+--------------------------------------------------------------------------------------------------+
| 78.5                                                                                             |
+--------------------------------------------------------------------------------------------------+
```

An alternative syntax is also supported:

```
> SELECT approx_percentile_cont_with_weight(column_name, weight_column, 0.90) FROM table_name;
+--------------------------------------------------+
| approx_percentile_cont_with_weight(column_name, weight_column, 0.90) |
+--------------------------------------------------+
| 78.5                                             |
+--------------------------------------------------+
```

On this page

[Edit on GitHub](https://github.com/apache/arrow-datafusion/edit/main/docs/source/user-guide/sql/aggregate_functions.md)

[Show Source](../../_sources/user-guide/sql/aggregate_functions.md.txt)

---
