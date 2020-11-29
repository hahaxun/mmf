# Copyright (c) Facebook, Inc. and its affiliates.
from multimodelity.common.registry import Registry
from multimodelity.datasets.builders.stvqa.dataset import STVQADataset
from multimodelity.datasets.builders.textvqa.builder import TextVQABuilder


@Registry.register_builder("stvqa")
class STVQABuilder(TextVQABuilder):
    def __init__(self):
        super().__init__()
        self.dataset_name = "stvqa"
        self.set_dataset_class(STVQADataset)

    @classmethod
    def config_path(cls):
        return "configs/datasets/stvqa/defaults.yaml"
