# Copyright (c) Facebook, Inc. and its affiliates.
from multimodelity.common.registry import registry
from multimodelity.datasets.builders.okvqa.dataset import OKVQADataset
from multimodelity.datasets.multimodelity_dataset_builder import multimodelityDatasetBuilder


@registry.register_builder("okvqa")
class OKVQABuilder(multimodelityDatasetBuilder):
    def __init__(
        self, dataset_name="okvqa", dataset_class=OKVQADataset, *args, **kwargs
    ):
        super().__init__(dataset_name, dataset_class, *args, **kwargs)

    @classmethod
    def config_path(cls):
        return "configs/datasets/okvqa/defaults.yaml"
