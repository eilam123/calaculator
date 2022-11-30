class Token:

    def __init__(self, value, Type=None):
        if Type == 'PLUS':
            self.type = 'PLUS'
        elif Type == 'MINUS':
            self.type = 'MINUS'
        elif Type == 'MUL':
            self.type = 'MUL'
        elif Type == 'DIV':
            self.type = 'DIV'
        self.value = value
