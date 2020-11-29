# Copyright (c) Facebook, Inc. and its affiliates.
from multimodelity.common.registry import registry
from multimodelity.datasets.builders.coco2017.masked_dataset import MaskedCoco2017Dataset
from multimodelity.datasets.multimodelity_dataset_builder import multimodelityDatasetBuilder


@registry.register_builder("masked_coco2017")
class MaskedFlickr30kBuilder(multimodelityDatasetBuilder):
    def __init__(
        self,
        dataset_name="masked_coco2017",
        dataset_class=MaskedCoco2017Dataset,
        *args,
        **kwargs
    ):
        super().__init__(dataset_name, dataset_class, *args, **kwargs)

    @classmethod
    def config_path(cls):
        return "configs/datasets/coco2017/masked.yaml"
