# Copyright (c) Facebook, Inc. and its affiliates.
from multimodelity.common.registry import registry
from multimodelity.datasets.builders.flickr30k.masked_dataset import MaskedFlickr30kDataset
from multimodelity.datasets.multimodelity_dataset_builder import multimodelityDatasetBuilder


@registry.register_builder("masked_flickr30k")
class MaskedFlickr30kBuilder(multimodelityDatasetBuilder):
    def __init__(
        self,
        dataset_name="masked_flickr30k",
        dataset_class=MaskedFlickr30kDataset,
        *args,
        **kwargs
    ):
        super().__init__(dataset_name, dataset_class, *args, **kwargs)

    @classmethod
    def config_path(cls):
        return "configs/datasets/flickr30k/masked.yaml"
