class Params:

    def __init__(self, arg1, arg2, operation):
        self.arg1 = arg1
        self.arg2 = arg2
        self.operation = operation
        pass

    def get_request_body(self):
        return {'arg1': self.arg1, 'arg2': self.arg2, 'operation': self.operation}
