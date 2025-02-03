from ..block import Block

class ConstructBlock(Block):
    def __init__(self, size:int):
        super().__init__(f'build{size}')
        self.size = size