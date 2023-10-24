class UserInput:
    def __enter__(self) -> None:
        pass
        
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def input(self, prompt):
        value = self.inputs[self.index]
        self.index += 1
        return value
    
    def __exit__(self, inputs, prompt, mock_user):
        pass