---
title: Infrastructure setup
weight: 1
---

Here you can find an overview of the infrastructure setup comprised of Local Developer Environment, Feature Cloud, and on-premise server at the clinic.

The developer use their local environment to build their machine learning applications and provide them to the user at the clinic via the feature cloud app store, allowing the user at the clinic to securely retrieve the machine learning application and run them on their data locally. 

This setup ensure that data resides on the clinic system and infrastructure at all times. 

{{% imgproc infrastructure-setup Fit "1000x500" %}}
{{% /imgproc %}}

Developers obtain mock data from Neo4j in their local environment. The mock data mimics the <a href="../../for-developers/graph-data-model/" class="link-underline-primary">data model</a> on the clinic side.

Developers in the local environment follow the <a href="https://github.com/careforrare/PersonalizedMedicine)" class="link-underline-primary">prepared template</a> to build their machine learning applications and test them with the mock data. They can then upload their machine learning applications to the feature cloud app store.

The user at the clinic can select their machine learning application of interest from feature cloud app store and download them to their local environment via the pull process. They can then securely execute the machine learning application on their data in their local environment. 

Depending on the performance of the application, the user at the clinic can choose to update the machine learning application residing on the feature cloud app store.