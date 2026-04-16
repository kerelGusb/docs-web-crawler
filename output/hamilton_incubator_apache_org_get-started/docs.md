# Get Started[¶](#get-started "Link to this heading")

Welcome to Apache Hamilton’s documentation!

## www.tryhamilton.dev[¶](#www-tryhamilton-dev "Link to this heading")

Before diving in, we highly recommend you try Apache Hamilton in your browser at <https://www.tryhamilton.dev>.
It allows you to:

> 1. run python in the browser, so you can get a feel for the basics of Apache Hamilton *without installing anything!*
> 2. it includes various examples that you can run and modify.
>
> 3. it represents an easy hands-on introduction to Apache Hamilton that should get you comfortable with the framework and its basic capabilities.

## Get started with Apache Hamilton locally[¶](#get-started-with-apache-hamilton-locally "Link to this heading")

The following section of the docs will teach you how to install Apache Hamilton and get started with your own project.

* [Why use Apache Hamilton?](why-hamilton/)
  * [Comparison to Other Frameworks](why-hamilton/#comparison-to-other-frameworks)
    * [Orchestration Systems](why-hamilton/#orchestration-systems)
    * [Feature Stores](why-hamilton/#feature-stores)
    * [Data Science Ecosystems/ML platforms](why-hamilton/#data-science-ecosystems-ml-platforms)
    * [Registries / Experiment Tracking](why-hamilton/#registries-experiment-tracking)
    * [Python Dataframe/manipulation Libraries](why-hamilton/#python-dataframe-manipulation-libraries)
    * [Python “big data” systems](why-hamilton/#python-big-data-systems)
* [Install](install/)
  * [Installing with pip](install/#installing-with-pip)
  * [Installing with conda](install/#installing-with-conda)
  * [Installing from source](install/#installing-from-source)
* [Your First Dataflow](your-first-dataflow/)
  * [Write transformation functions](your-first-dataflow/#write-transformation-functions)
  * [Run your dataflow](your-first-dataflow/#run-your-dataflow)
* [Learning Resources](learning-resources/)
  * [📒 User Guide Documentation](learning-resources/#user-guide-documentation)
  * [📚 Reference Documentation](learning-resources/#reference-documentation)
  * [🌐 Ecosystem & Integrations](learning-resources/#ecosystem-integrations)
  * [✍ tryhamilton.dev](learning-resources/#tryhamilton-dev)
  * [👋 Slack](learning-resources/#slack)
  * [📣 Talks & Videos](learning-resources/#talks-videos)
  * [📰 External Blogs](learning-resources/#external-blogs)
  * [🎙 Podcasts](learning-resources/#podcasts)
* [Contributing](contributing/)
* [License](license/)

---
# License[¶](#license "Link to this heading")

Apache Hamilton is released under the [Apache 2.0 License](https://github.com/apache/hamilton/blob/main/LICENSE).

---
# Why use Apache Hamilton?[¶](#why-use-apache-hamilton "Link to this heading")

There are many choices for building dataflows/pipelines/workflows/ETLs.
Let’s compare Apache Hamilton to some of the other options to help answer this question.

## Comparison to Other Frameworks[¶](#comparison-to-other-frameworks "Link to this heading")

There are a lot of frameworks out there, especially in the pipeline space. This section should help you figure out when to
use Apache Hamilton with another framework, or in place of a framework, or when to use another framework altogether.

Let’s go over some groups of “competitive” or “complimentary” products. For a basic overview,
see the product matrix on the [homepage](../../).

### Orchestration Systems[¶](#orchestration-systems "Link to this heading")

Examples include:

* [Airflow](https://airflow.apache.org/)
* [Metaflow](https://github.com/Netflix/metaflow)
* [Luigi](https://github.com/spotify/luigi)
* [dbt](https://www.getdbt.com/)

Apache Hamilton is not, in itself a macro, i.e. high level, task orchestration system. While it does orchestrate functions,
and the DAG abstraction is very powerful, it does not provision compute,
or schedule long-running jobs. Apache Hamilton works well in conjunction with these macro systems.
Apache Hamilton provides the capabilities of fine-grained lineage, highly readable code, and self-documenting pipelines,
which many of these systems lack.

Apache Hamilton can be used within any python orchestration system in the following ways:

1. *Hamilton DAGs can be called within orchestration system tasks.*
   See the [Apache Hamilton + Airflow example](https://blog.dagworks.io/p/supercharge-your-airflow-dag-with). The integration is generally trivial – all you have to do
   is call out to the hamilton library within your task. If your orchestrator supports python, then you’re good to go. Some pseudocode (if your orchestrator handles scripts like airflow):

   ```
   #my_task.py
   import hamilton
   import my_transformations
   dr = hamilton.driver.Driver({}, my_functions)
   output = dr.execute(['final_var'], inputs=...)
   do_something_with(output)
   ```
2. *Hamilton DAGs can be broken up to run as components within an orchestration system.*
   With the ability to include [overrides](../../concepts/driver/),
   you can run the DAG on each task, overloading the outputs of the last task + any static inputs/configuration, and pass it into the next task. This is more
   of a manual/power-user feature. Some pseudocode:

   ```
   #my_task.py
   import hamilton
   import my_functions
   prior_inputs = load_relevant_task_results()
   desired_outputs = ['final_var_1', 'final_var_2']
   inputs = my_inputs
   dr = hamilton.driver.Driver({}, my_functions)
   output = dr.execute(
      desired_outputs,
      inputs=inputs,
      overrides=prior_inputs)
   save_for_later(output)
   ```

### Feature Stores[¶](#feature-stores "Link to this heading")

Examples include:

* [Hopsworks](https://www.hopsworks.ai/)
* [Feast](https://feast.dev/)
* [Tecton](https://tecton.ai/)

One can think of Apache Hamilton as a being your “feature definition store”, where “store” is code + git. While it does
not provide all the capabilities of a standard feature store, it provides a source of truth for the code that
generated the features, and can be run in a portable method. *So*, if your desire is just to be able to run the same
code in different environments, and have an online/offline store of features, you can use hamilton both to save the
features offline, and generate features online on the fly.

See the [feature engineering example](../../how-tos/use-for-feature-engineering/) for more possibilities, as
well as [blogs on the feature topic](https://blog.dagworks.io/?sort=search&amp;search=features).

Note that in small cases, you probably don’t need a true feature store – recomputing derived features in an ETL
and online can be very efficient, as long as you have some database to look values up (or have them passed in).

Also note that joins and aggregations can get tricky. We often recommend using our “polymorphic function
definition” i.e. functions decorated with `@config.when`, to either load up the non-online-friendly features
from a feature store or do an external lookup to simulate an online join.

We expect Apache Hamilton to play a prominent role in the way feature stores work in the future.

### Data Science Ecosystems/ML platforms[¶](#data-science-ecosystems-ml-platforms "Link to this heading")

Examples include:

* [Kedro](https://kedro.org/)
* [Domino Data Labs](https://www.dominodatalab.com/)
* [Dataiku](https://www.dataiku.com/)
* [SageMaker](https://aws.amazon.com/sagemaker/)
* [Google Cloud Vertex AI Platform](https://cloud.google.com/vertex-ai)
* etc.

We’ve kind of grouped a whole suite of platforms into the same bucket here. These
tend to have a lot of capabilities all related to ML. Apache Hamilton can be used in conjunction with these
platforms in a variety of ways. For example, you can use Apache Hamilton to generate features for a model
that you train in one of these platforms. Or you can use Apache Hamilton to generate a model using the
platform’s compute, and then save the model to the platform’s registry.

### Registries / Experiment Tracking[¶](#registries-experiment-tracking "Link to this heading")

Examples include:

* [MLflow](https://mlflow.org/)
* [Weights and Biases](https://wandb.ai/site)
* [DVC](https://dvc.org/)

Most pipelines have a “reverse ETL problem” – they need to get the results of the pipeline into a some
sort of datastore or registry. Apache Hamilton can be used in conjunction with these tools as the glue code
that helps everything work together. For example, you can use Apache Hamilton to generate a model
and then store metrics computed by Apache Hamilton to one of these “destinations”.

There are three main ways to integrate with these tools:

* inside a function that Apache Hamilton orchestrates
* outside Apache Hamilton (e.g. in a script that calls Apache Hamilton)
* using “materializers” (see [materializers](../../reference/io/)) (see [this blog](https://blog.dagworks.io/p/separate-data-io-from-transformation)).

See this [ML reference post](https://blog.dagworks.io/p/from-dev-to-prod-a-ml-pipeline-reference) for examples of how to use Apache Hamilton with these tools.

### Python Dataframe/manipulation Libraries[¶](#python-dataframe-manipulation-libraries "Link to this heading")

Examples include:

* [pandas](https://pandas.pydata.org/)
* [dask](https://www.dask.org/)
* [modin](https://github.com/modin-project/modin)
* [polars](https://www.pola.rs/)
* [duckdb](https://duckdb.org/)

Apache Hamilton works with any python dataframe/manipulation oriented libraries.
See our [examples folder](https://github.com/apache/hamilton/tree/main/examples)
to see how to use Apache Hamilton with these libraries.

### Python “big data” systems[¶](#python-big-data-systems "Link to this heading")

The following systems are ones that you would resort to using when wanting to scale up your data processing.

Examples include:

* [dask](https://www.dask.org/)
* [ray](https://ray.io/)
* [pyspark](https://spark.apache.org/docs/latest/api/python/)
* [pandas-on-spark](https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/index.html)

These all provide capabilities to either (a) express and execute computation over datasets in python or (b)
parallelize it. Often both. Apache Hamilton has a variety of integrations with these systems. The basics is that Apache Hamilton
can make use of these systems to execute the DAG using the [GraphAdapter](../../reference/graph-adapters/) abstraction and [Lifecycle Hooks](../../reference/lifecycle-hooks/).

See our [examples folder](https://github.com/apache/hamilton/tree/main/examples)
to see how to use Apache Hamilton with these systems.

---
# Learning Resources[¶](#learning-resources "Link to this heading")

Several channels are available to get started with Apache Hamilton, learn advanced usage, and participate in the latest feature development.

## 📒 User Guide Documentation[¶](#user-guide-documentation "Link to this heading")

The [user guide](../../concepts/) gives a complete overview of Apache Hamilton’s features.

## 📚 Reference Documentation[¶](#reference-documentation "Link to this heading")

The [reference documentation](../../reference/dataflows/) details Apache Hamilton’s public API.

## 🌐 Ecosystem & Integrations[¶](#ecosystem-integrations "Link to this heading")

The [ecosystem page](../../ecosystem/) lists all built-in integrations (pandas, Polars, Spark, etc.) and external community resources. Find reusable dataflows, blog posts, and video tutorials there.

## ✍ tryhamilton.dev[¶](#tryhamilton-dev "Link to this heading")

The [tryhamilton.dev](https://tryhamilton.dev) website provides interactive tutorials in-browser to learn specific Apache Hamilton concepts.

## 👋 Slack[¶](#slack "Link to this heading")

The [Slack channel](https://join.slack.com/t/hamilton-opensource/shared_invite/zt-2niepkra8-DGKGf_tTYhXuJWBTXtIs4g) is the ideal place to ask questions, request features, and give feedback.

## 📣 Talks & Videos[¶](#talks-videos "Link to this heading")

See the [ecosystem page](../../ecosystem/) for links to video content and conference talks.

* 2024-02    Apache Hamilton Meet-up for February

  * [Recording](https://www.youtube.com/watch?v=ks672Lm0CJo.)
  * [Slides](https://github.com/skrawcz/talks/files/14351139/Apache Hamilton.February.2024.Meetup.pdf)
* 2023-12    Why you should build your GenAI/LLM apps using Apache Hamilton. [AICamp End of Year in SF](https://www.aicamp.ai/event/eventdetails/W2023121217)

  * [Recording](https://youtu.be/IwWixrjhkZU?si=DVa72Zr4iD-hibS5&amp;t=7602)
  * [Slides](https://github.com/skrawcz/talks/files/13666470/Why.you.should.build.your.GenAI\_LLM.apps.using.Apache Hamilton.pdf)
* 2023-12    Bridging Classic ML Pipelines with the World of LLMs. [PyData Global](https://global2023.pydata.org/cfp/talk/3REDA9/)

  * [Slides](https://github.com/skrawcz/talks/files/13666479/Bridging.Classic.ML.Pipelines.with.the.World.of.LLMs.1.pdf)
* 2023-11    Apache Hamilton: Natively bringing software engineering best practices to python data transformations. [Scale by the Bay](https://www.scale.bythebay.io/).

  * [Recording](https://www.youtube.com/watch?v=gK4-6X0h7PU)
  * [Slides](https://github.com/skrawcz/talks/files/13969784/Scale.By.The.Bay.-.Hamilton_.Natively.bringing.SWE.best.practices.to.python.data.transformations.pdf)
* 2023-09    Apache Hamilton: Natively bringing software engineering best practices to python data transformations. [Bay Area Python Interest Group (BAYPIGgies)](https://www.meetup.com/baypiggies/events/296283989/)

  * [Slides](https://github.com/skrawcz/talks/files/12785978/BayPIGgies\_.Apache Hamilton.Talk.pdf)
* 2023-08    dbt + Apache Hamilton: Enabling you to maintain complex Python within dbt models. [MDSFest’23](https://www.mdsfest.com/)

  * [Recording](https://www.youtube.com/watch?v=ZM-kM8DqlaQ&amp;list=PLdVpUmZrh0QpDi07ENp3FD5aTFuTTtWnP)
  * [Slides](https://github.com/skrawcz/talks/files/12431755/dbt.%2B.Hamilton_.Enabling.you.to.maintain.complex.python.within.dbt.models.pdf)
* 2023-06    Apache Hamilton: an OS tool to add to your LLM App toolbelt. LLM Avalanche.

  * [Slides](https://github.com/skrawcz/talks/files/11899349/Hamilton_.an.OS.tool.to.add.to.your.LLM.App.toolbelt.pdf)
* 2023-06    Feature Engineering with Apache Hamilton: Portability & Lineage. [Budapest ML Forum June 2023](https://budapestml.hu/2023/en/)

  * [Slides](https://github.com/skrawcz/talks/files/11690901/Stefan_Krawczyk_BudapestTalkJune2023_FeatureEngineeringwith.Hamilton_Portability.Lineage.pdf)
* 2023-06    British Cycling Data Platform in Python. Manchester PyData Meetup

  * [Slides](https://github.com/skrawcz/talks/files/11899331/PyData.British.Cycling.7.June.2023.pdf)
  * Co-presented with Peter Robinson, and Murray Tait.
* 2023-04    Lightweight Lineage with Apache Hamilton. PyData Seattle

  * [Slides](https://github.com/skrawcz/talks/files/11399972/PyData-Seattl-Lightning-Talk-2023-Lighweight-Lineage-with-Apache Hamilton.pdf)
* 2023-01    Apache Hamilton: Natively bringing software engineering best practices to python data transformations. AI Camp Meetup San Jose

  * [Slides](https://github.com/skrawcz/talks/files/10830349/Hamilton_.Natively.bringing.software.engineering.best.practices.to.python.data.transformations.-.January.2023.pdf)
* 2022-10    Apache Hamilton: an open source, declarative, micro-framework for clean & robust feature transform code in Python. Feature Store Summit

  * [Event](https://www.featurestoresummit.com/)
  * [Slides](https://github.com/skrawcz/talks/files/9759661/FS.Summit.2022.-.Apache Hamilton.pdf)
* 2022-09    Apache Hamilton: enabling software engineering best practices for data transformations via generalized dataflow graphs. DEco - First International Workshop on Data Ecosystems

  * [Event](https://dbis.rwth-aachen.de/DEco22/)
  * [Slides](https://github.com/skrawcz/talks/files/9550914/Submitted.-.DEco.2022_.Hamilton_.enabling.software.engineering.best.practices.for.data.transformations.via.generalized.dataflow.graphs.1.pdf)
* 2022-09    Apache Hamilton: a modular open source declarative paradigm for high level modeling of dataflows. CDMS - First International Workshop on Composable Data Management Systems

  * [Event](https://cdmsworkshop.github.io/2022/)
  * [Slides](https://github.com/skrawcz/talks/files/9550939/CDMS.2022.-.Hamilton_.a.modular.open.source.declarative.paradigm.for.high.level.modeling.of.dataflows.1.pdf)
  * [Paper](https://cdmsworkshop.github.io/2022/Proceedings/ShortPapers/Paper6_StefanKrawczyk.pdf)
* 2022-08    Apache Hamilton: A Python Micro-Framework for tidy scalable Pandas. Scalable Pandas Meetup

  * [Recording](https://www.youtube.com/watch?v=m_rjCzxQj4c&amp;ab_channel=Ponder)
  * [Slides](https://github.com/skrawcz/talks/files/9428705/Apache Hamilton.%40.Ponder.Pandas.meetup.pdf)
* 2022-08    Scalable feature engineering with Apache Hamilton on Ray. Ray Summit

  * [Slides](https://github.com/skrawcz/talks/files/9411082/Submitted.Slides.-.Ray.Summit\_.Scalable.feature.engineering.with.Apache Hamilton.on.Ray.pdf)
* 2022-07    Apache Hamilton: A Python Micro-Framework for Data / Feature Engineering. MLOPsWorld Bay Area

  * [Slides](https://github.com/skrawcz/talks/files/9213924/Hamilton_.A.Python.Micro-Framework.for.Data._.Feature.Engineering.pdf)
* 2022-05    Apache Hamilton: a python micro-framework for data / feature engineering at Stitch Fix. AICamp

  * [Recording](https://www.youtube.com/watch?v=PDGIt37dov8)
  * [Slides](https://github.com/skrawcz/talks/files/8691633/AICamp.Apache Hamilton.Presentation.pdf)
* 2022-02    [Open Source] Apache Hamilton, a micro framework for creating dataframes, and its application at Stitch Fix. Apply(Meetup)

  * [Event](https://www.applyconf.com/agenda/open-source-hamilton-a-micro-framework-for-creating-dataframes-and-its-application-at-stitch-fix/).
  * [Recording](https://www.youtube.com/watch?v=CHfrT5OVjlM)
  * [Slides](https://github.com/skrawcz/talks/blob/main/Public%20ApplyConf2022%20-%20%5BOpen%20Source%5D%20Hamilton%2C%20a%20micro%20framework%20for%20creating%20dataframes%2C%20and%20its%20application%20at%20Stitch%20Fix.pdf)
* 2021-12    Apache Hamilton an open source micro framework for creating dataframes. SF Python Meetup

  * [Recording](https://www.youtube.com/watch?v=_XUYfwougz4)
  * [Slides](https://github.com/skrawcz/talks/files/8944605/Python.Meetup.Dec.2021.-.Hamilton_.an.open.source.micro.framework.for.creating.dataframes.pdf)

## 📰 External Blogs[¶](#external-blogs "Link to this heading")

For external resources including blogs, see the [ecosystem page](../../ecosystem/). Here are some notable blog posts about Apache Hamilton:

* 2024-03    [RAG: ingestion and chunking using Apache Hamilton and scaling to Ray, Dask, or PySpark](https://blog.dagworks.io/p/rag-ingestion-and-chunking-using)
* 2024-02    [A command line tool to improve your development workflow](https://blog.dagworks.io/p/a-command-line-tool-to-improve-your)
* 2024-02    [Monthly Meetup Recap and office hours](https://blog.dagworks.io/p/monthly-hamilton-meetup-and-office)
* 2024-02    [Using IPython Jupyter Magic commands to improve the notebook experience](https://blog.dagworks.io/p/using-ipython-jupyter-magic-commands)
* 2024-02    [Building a lightweight experiment manager](https://blog.dagworks.io/p/building-a-lightweight-experiment)
* 2024-01    [Customizing Apache Hamilton’s Execution with the new Lifecycle API](https://blog.dagworks.io/p/customizing-hamiltons-execution-with)
* 2024-01    [How well-structured should your data code be?](https://blog.dagworks.io/p/how-well-structured-should-your-data)
* 2024-01    [From Dev to Prod: a ML Pipeline Reference Post](https://blog.dagworks.io/p/from-dev-to-prod-a-ml-pipeline-reference)
* 2023-12    [Winning over hearts and minds at work: ADKAR my favorite change management approach](https://blog.dagworks.io/p/winning-hearts-and-minds-at-work)
* 2023-11    [🚀 We’re launching the Apache Hamilton Dataflow Hub!](https://blog.dagworks.io/p/were-launching-the-hamilton-dataflow)
* 2023-10    [Separate data I/O from transformation – your future self will thank you.](https://blog.dagworks.io/p/separate-data-io-from-transformation)
* 2023-09    [Retrieval augmented generation (RAG) with Streamlit, FastAPI, Weaviate, and Apache Hamilton!](https://blog.dagworks.io/p/retrieval-augmented-generation-reference-arch)
* 2023-09    [LLMOps: Production prompt engineering patterns with Apache Hamilton](https://blog.dagworks.io/p/llmops-production-prompt-engineering)
* 2023-09    [Feature Engineering with Apache Hamilton](https://blog.dagworks.io/p/feature-engineering-with-hamilton)
* 2023-08    [Expressing PySpark Transformations Declaratively with Apache Hamilton](https://blog.dagworks.io/p/expressing-pyspark-transformations)
* 2023-08    [Containerized PDF Summarizer with FastAPI and Apache Hamilton](https://blog.dagworks.io/p/containerized-pdf-summarizer-with)
* 2023-08    [Dynamic DAGs: Counting Stars with Apache Hamilton](https://blog.dagworks.io/p/counting-stars-with-hamilton)
* 2023-08    [Featurization: Integrating Apache Hamilton with Feast](https://blog.dagworks.io/p/featurization-integrating-hamilton)
* 2023-07    [Simplify Prefect Workflow Creation and Maintenance with Apache Hamilton](https://blog.dagworks.io/p/simplify-prefect-workflow-creation)
* 2023-07    [Building a maintainable and modular LLM application stack with Apache Hamilton](https://blog.dagworks.io/p/building-a-maintainable-and-modular)
* 2023-06    [Simplify Airflow DAG Creation and Maintenance with Apache Hamilton](https://blog.dagworks.io/p/supercharge-your-airflow-dag-with)
* 2023-05    [Lineage + Apache Hamilton in 10 minutes](https://blog.dagworks.io/p/lineage-hamilton-in-10-minutes-c2b8a944e2e6)
* 2022-11    [Apache Hamilton + DBT in 5 minutes](https://blog.dagworks.io/p/hamilton-dbt-in-5-minutes-62e4cb63f08f)
* 2022-07    [Tidy production pandas with Apache Hamilton](https://towardsdatascience.com/tidy-production-pandas-with-hamilton-3b759a2bf562)
* 2022-06    [Developing Scalable Feature Engineering DAGs with Metaflow & Apache Hamilton](https://outerbounds.com/blog/developing-scalable-feature-engineering-dags)
* 2022-05    [Apache Hamilton backstory and intro post on TDS](https://towardsdatascience.com/functions-dags-introducing-hamilton-a-microframework-for-dataframe-generation-more-8e34b84efc1d)
* 2022-05    [Apache Hamilton + Pandas in five minutes](https://towardsdatascience.com/how-to-use-hamilton-with-pandas-in-5-minutes-89f63e5af8f5)
* 2022-05    [Iterating with Apache Hamilton in a Notebook](https://towardsdatascience.com/how-to-use-hamilton-with-pandas-in-5-minutes-89f63e5af8f5)

## 🎙 Podcasts[¶](#podcasts "Link to this heading")

* 2024-03    [Apache Hamilton mention in Real Python, about ipython magic command post](https://realpython.com/podcasts/rpp/196/)
* 2023-06    [Exploring the Intersection of DAGs, ML Code, and Complex Code Bases: An Elegant Solution Unveiled with Stefan Krawczyk of DAGWorks](https://datastackshow.com/podcast/exploring-the-intersection-of-dags-ml-code-and-complex-code-bases-an-elegant-solution-unveiled-with-stefan-krawczyk-of-dagworks/)
* 2022-08    [S01 E08 - MLOps Week 8: The MLOps Mindset with Stefan Krawczyk](https://rss.com/podcasts/mlops-weekly/571949/)
* 2022-04    [MLOps dla 100 data scientistów](https://nieliniowy.pl/mlops-dla-100-data-scientistow-stefan-krawczyk-stitch-fix/) (in Polish)
* 2021-09    [Aggressively Helpful Platform teams](https://www.youtube.com/watch?v=az8lXG9v4uo)

---
Installing hamilton is easy!

# Install[¶](#install "Link to this heading")

Apache Hamilton is a lightweight framework with a variety of extensions/plugins. To get started, you’ll need the following:

* `python >= 3.10`
* `pip`

For help with python/pip/managing virtual environments see the [python docs](https://docs.python.org/3/tutorial/venv.html/).

## Installing with pip[¶](#installing-with-pip "Link to this heading")

Apache Hamilton is published on [pypi](https://pypi.org/project/sf-hamilton/) under `sf-hamilton`. To install, run:

`pip install sf-hamilton`

To use the DAG visualization functionality, instead install with

`pip install sf-hamilton[visualization]`

*Note: for visualization you may additionally need to install graphviz externally – see*
[graphviz](https://graphviz.org/download/) *for instructions on the correct way for your
operating system.*

## Installing with conda[¶](#installing-with-conda "Link to this heading")

Apache Hamilton is also available on conda if you prefer:

`conda install -c hamilton-opensource sf-hamilton`

## Installing from source[¶](#installing-from-source "Link to this heading")

You can also download the code and run it from the source.

```
git clone https://github.com/apache/hamilton.git
cd hamilton
pip install -e .
```

---
# Your First Dataflow[¶](#your-first-dataflow "Link to this heading")

Let’s get started with a dataflow that computes statistics on a time-series of marketing spend.

We’re jumping in head-first. If you want to start with an overview, skip ahead to
[Concepts](../../concepts/).

Note

You can follow along in the [examples directory](https://github.com/apache/hamilton/tree/main/examples/hello_world)
of the [hamilton repo](https://github.com/apache/hamilton/). We highly recommend forking the repo and playing
around with the code to get comfortable.

## Write transformation functions[¶](#write-transformation-functions "Link to this heading")

Create a file `my_functions.py` and add the following two functions:

```
import pandas as pd

def avg_3wk_spend(spend: pd.Series) -> pd.Series:
    """Rolling 3 week average spend."""
    return spend.rolling(3).mean()

def acquisition_cost(avg_3wk_spend: pd.Series, signups: pd.Series) -> pd.Series:
    """The cost per signup in relation to a rolling average of spend."""
    return avg_3wk_spend / signups
```

An astute observer might ask the following questions:

1. **Why do the parameter names clash with the function names?** This is core to how hamilton works. It utilizes dependency injection to create a DAG of computation. Parameter names tell the framework where your function gets its data.
2. **OK, if the parameter names determine the source of the data, why have we not defined defined `spend` or `signups` as functions?** This is OK, as we will provide this data as an input when we actually want to materialize our functions. The DAG doesn’t have to be complete when it is compiled.
3. **Why is there no main line to call these functions?** Good observation. In fact, we never will call them (directly)! This is one of the core principles of Apache Hamilton. You write individual transforms and the rest is handled by the framework. More on that next.
4. **The functions all output pandas series. What if I don’t want to use series?** You don’t have to! Apache Hamilton is not opinionated on the data type you use. The following are all perfectly valid as well (and we support dask/spark/ray/other distributed frameworks).

Let’s add a few more functions to our `my_functions.py` file:

```
def spend_mean(spend: pd.Series) -> float:
    """Shows function creating a scalar. In this case it computes the mean of the entire column."""
    return spend.mean()

def spend_zero_mean(spend: pd.Series, spend_mean: float) -> pd.Series:
    """Shows function that takes a scalar. In this case to zero mean spend."""
    return spend - spend_mean

def spend_std_dev(spend: pd.Series) -> float:
    """Function that computes the standard deviation of the spend column."""
    return spend.std()

def spend_zero_mean_unit_variance(spend_zero_mean: pd.Series, spend_std_dev: float) -> pd.Series:
    """Function showing one way to make spend have zero mean and unit variance."""
    return spend_zero_mean / spend_std_dev
```

Let’s give these functions a spin!

## Run your dataflow[¶](#run-your-dataflow "Link to this heading")

To actually run the dataflow, we’ll need to write [a driver](../../concepts/driver/). Create a`my_script.py` with the following contents:

```
import logging
import sys

import pandas as pd

# We add this to speed up running things if you have a lot in your python environment.
from hamilton import registry; registry.disable_autoload()
from hamilton import driver, base
import my_functions  # we import the module here!


logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout)

if __name__ == '__main__':
    # Instantiate a common spine for your pipeline
    index = pd.date_range("2022-01-01", periods=6, freq="w")
    initial_columns = {  # load from actuals or wherever -- this is our initial data we use as input.
        # Note: these do not have to be all series, they could be scalar inputs.
        'signups': pd.Series([1, 10, 50, 100, 200, 400], index=index),
        'spend': pd.Series([10, 10, 20, 40, 40, 50], index=index),
    }
    dr = (
      driver.Builder()
        .with_config({})  # we don't have any configuration or invariant data for this example.
        .with_modules(my_functions)  # we need to tell hamilton where to load function definitions from
        .with_adapters(base.PandasDataFrameResult())  # we want a pandas dataframe as output
        .build()
    )
    # we need to specify what we want in the final dataframe (these could be function pointers).
    output_columns = [
        'spend',
        'signups',
        'avg_3wk_spend',
        'acquisition_cost',
    ]
    # let's create the dataframe!
    df = dr.execute(output_columns, inputs=initial_columns)
    # `pip install sf-hamilton[visualization]` earlier you can also do
    # dr.visualize_execution(output_columns,'./my_dag.png', {})
    print(df)
```

Run the script with the following command:

`python my_script.py`

And you should see the following output:

```
            spend  signups  avg_3wk_spend  acquisition_cost
2022-01-02     10        1            NaN            10.000
2022-01-09     10       10            NaN             1.000
2022-01-16     20       50      13.333333             0.400
2022-01-23     40      100      23.333333             0.400
2022-01-30     40      200      33.333333             0.200
2022-02-06     50      400      43.333333             0.125
```

Not only is your spend to signup ratio decreasing exponentially (your product is going viral!), but you’ve also
successfully run your first Apache Hamilton Dataflow. Kudos!

See, wasn’t that quick and easy?

Note: if you’re ever like “why are things taking a while to execute?”, then you might have too much
in your python environment and Apache Hamilton is auto-loading all the extensions. You can disable this by
setting the environment variable `HAMILTON_AUTOLOAD_EXTENSIONS=0` or programmatically via
`from hamilton import registry; registry.disable_autoload()` - for more see [Extension autoloading](../../how-tos/extensions-autoloading/).

---
# Contributing[¶](#contributing "Link to this heading")

We are open contributions big and small. See our [contributing guidelines](https://github.com/apache/hamilton/blob/main/CONTRIBUTING.md).

We also operate under a [Code of Conduct](https://www.apache.org/foundation/policies/conduct.html), and
expect contributors to do the same.

---
