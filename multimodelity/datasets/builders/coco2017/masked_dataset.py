# Copyright (c) Facebook, Inc. and its affiliates.

from multimodelity.common.typings import multimodelityDatasetConfigType
from multimodelity.datasets.builders.localized_narratives.masked_dataset import (
    MaskedLocalizedNarrativesDatasetMixin,
)
from multimodelity.datasets.multimodelity_dataset import multimodelityDataset


class MaskedCoco2017Dataset(MaskedLocalizedNarrativesDatasetMixin, multimodelityDataset):
    def __init__(
        self,
        config: multimodelityDatasetConfigType,
        dataset_type: str,
        index: int,
        *args,
        **kwargs,
    ):
        super().__init__(
            "masked_coco2017", config, dataset_type, index, *args, **kwargs
        )
