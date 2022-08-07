from .step import Step
from ...model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        print('in search terms')
        terms = inputs['terms']
        founds = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if terms in caption:
                    time = captions[caption]
                    found = Found(yt, caption, time)
                    founds.append(found)
        print(len(founds))
        data = founds
        return data





