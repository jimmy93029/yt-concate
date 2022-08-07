from .step import Step
from ...model.yt import Yt


class InitializeYt(Step):
    def process(self, data, inputs, utils):
        return [Yt(url) for url in data]


