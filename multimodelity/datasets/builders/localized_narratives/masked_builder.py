# Copyright (c) Facebook, Inc. and its affiliates.
from multimodelity.common.registry import registry
from multimodelity.datasets.builders.localized_narratives.masked_dataset import (
    MaskedLocalizedNarrativesDataset,
)
from multimodelity.datasets.multimodelity_dataset_builder import multimodelityDatasetBuilder


@registry.register_builder("masked_localized_narratives")
class MaskedLocalizedNarrativesBuilder(multimodelityDatasetBuilder):
    def __init__(
        self,
        dataset_name="masked_localized_narratives",
        dataset_class=MaskedLocalizedNarrativesDataset,
        *args,
        **kwargs
    ):
        super().__init__(dataset_name, dataset_class, *args, **kwargs)

    @classmethod
    def config_path(cls):
        return "configs/datasets/localized_narratives/masked.yaml"
