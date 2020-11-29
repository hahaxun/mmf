---
id: quickstart
title: Quickstart
sidebar_label: Quickstart
---

In this quickstart guide, we are going to train the [M4C](https://github.com/facebookresearch/multimodelity/tree/master/projects/m4c) model on the TextVQA dataset. TextVQA requires models to read and reason about text in images to answer questions about them. `M4C` is a recent SOTA model on TextVQA which consists of a multimodal transformer architecture accompanied by a rich representation for text in images.

To train other models or understand more about multimodelity, follow Next Steps at the bottom of this tutorial.

## Installation

Install multimodelity following the [installation documentation](https://multimodelity.sh/docs/getting_started/installation).

## Getting Data

Datasets and required files will be downloaded automatically when we run training. For more details about custom datasets and other advanced setups for datasets check the [dataset documentation](https://multimodelity.sh/docs/tutorials/dataset).

## Training

We can start training by running the following command:

```bash
multimodelity_run config=projects/m4c/configs/textvqa/defaults.yaml \
    datasets=textvqa \
    model=m4c \
    run_type=train_val
```

The hyperparameters for training and for the experiment are in the experiment config `projects/m4c/configs/textvqa/defaults.yaml`. We can also set config params using command line args:

```bash
multimodelity_run config=projects/m4c/configs/textvqa/defaults.yaml \
    datasets=textvqa \
    model=m4c \
    run_type=train_val \
    training.batch_size=32 \
    training.max_updates=44000 \
```

where `training.batch_size=32` will set batch size to 32 and `training.max_updates=44000` will set max iterations to 44000 for the training.

Similarly, log interval, checkpoint interval and validation interval can all be set as:

```bash
multimodelity_run config=projects/m4c/configs/textvqa/defaults.yaml \
    datasets=textvqa \
    model=m4c \
    run_type=train_val \
    training.batch_size=32 \
    training.max_updates=44000 \
    training.log_interval=10 \
    training.checkpoint_interval=100 \
    training.evaluation_interval=1000
```

This will show training logs every 10 iterations, checkpoint models every 100 iterations and run validation every 1000 iterations. More about configurations and how we set them can be found [here](https://multimodelity.sh/docs/notes/configuration).

## Inference

For running inference or generating predictions, we can specify a pretrained model using its zoo key and then run the following command:

```bash
multimodelity_predict config=projects/m4c/configs/textvqa/defaults.yaml \
    datasets=textvqa \
    model=m4c \
    run_type=test \
    checkpoint.resume_zoo=m4c.textvqa.defaults
```

For running inference on the `val` set, use `run_type=val` and rest of the arguments stay the same. `checkpoint.resume_zoo` is loading a pretrained model from model zoo. To learn more about checkpoints and pretraining/finetuning models check this [tutorial](https://multimodelity.sh/docs/tutorials/checkpointing).

These commands should be enough to get you started with training and performing inference using multimodelity.

## Citation

If you use multimodelity in your work or use any models published in multimodelity, please cite:

```text
@misc{singh2020multimodelity,
  author =       {Singh, Amanpreet and Goswami, Vedanuj and Natarajan, Vivek and Jiang, Yu and Chen, Xinlei and Shah, Meet and
                 Rohrbach, Marcus and Batra, Dhruv and Parikh, Devi},
  title =        {multimodelity: A multimodal framework for vision and language research},
  howpublished = {\url{https://github.com/facebookresearch/multimodelity}},
  year =         {2020}
}
```

## Next steps

To dive deeper into multimodelity, explore the following topics next:

- [Concepts and Terminology](https://multimodelity.sh/docs/notes/concepts)
- [Model Zoo of multimodelity](https://multimodelity.sh/docs/notes/model_zoo)
- [Dataset Zoo of multimodelity](https://multimodelity.sh/docs/notes/dataset_zoo)
- [Projects available in multimodelity](https://multimodelity.sh/docs/notes/projects)
- [FAQs](https://multimodelity.sh/docs/getting_started/faqs)
