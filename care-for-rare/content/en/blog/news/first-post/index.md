---
title: Meet the winners of the TUM.ai Makeathon 2023
linkTitle: Meet the winners of the Makeathon 2023
description: >
  The TUM.ai Makeathon 2023 brought up many promising ideas for leveraging the diagnosis of rare diseases with AI. The team behind **AIME** stood out among
  many excellent projects.
resources:
  - src: "**.{png,jpg}"
    title: "Image #:counter"
    params:
      byline: "Photo: https://github.com/floriankri/aime_TUMai_Hackathon/tree/main"
---

<div class="row mt-5">
{{% alert title="Warning" %}}
This website is under construction. Please come back later!
{{% /alert %}}
</div>

Although the TUM.ai Makeathon has only been around for a short time, it has already become an institution among young AI developers. In the **2023** edition of the Makeathon
students were given a challenging task: to develop AI models to help diagnose rare pediatric diseases. The most convincing approach was presented
by the **AIME** team, which developed a neural network to classify synthetic disease data.

{{< imgproc sunset Fill "600x300" >}}
Fetch and scale an image in the upcoming Hugo 0.43.
{{< /imgproc >}}

The big challenge for the AIME team and the other contestants was to find solutions to deal with two distinctive characteristics of the *rare* disease data - its unlabelled nature and sparsity. The lack of labels meant that in many cases the students were unaware of the specific diseases the patients had, which was a barrier in to train effective AI models. In addition, the sparse nature of the data provided limited information for initial analysis. The students had to come up with a clever solution to these problems - and AIME certainly did.

The team behind AIME consisted of four talented students, who came up with a creative and well thought-out solution in just three days. The AIME team divided their development process into four iterations, resulting in an autoencoder architecture. The autoencoder architecture is based on a combination of an encoder and a fully connected neural network, which is a promising approach to classify rare diseases. Autoencoders, which are well-suited to unsupervised learning, proved effective in identifying patterns within unlabelled data - a common feature of rare disease datasets. Based on their final solution the AIME team outlined how their AI model could be improved and used in medical research.

The AIME team's pragmatic approach went beyond the scope of the competition, demonstrating the real-world applicability of their AI model in medical research. In just three days, the AIME team not only met the Makeathon's challenges but also provided a smart solution from which future approaches to AI assisted rare disease diagnosis could learn.

See their [GitHub repository](https://github.com/floriankri/aime_TUMai_Hackathon/tree/main) to learn more about AIME.
