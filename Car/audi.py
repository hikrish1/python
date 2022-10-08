class Audi:
    def __init__(self):
        self.models = ['q7', 'a3', 'a6', 'a8']
        def outmodels(self):
            print('These are the avalable models for audi ')
            for model in self.models:
               print('\t%s ' % model)