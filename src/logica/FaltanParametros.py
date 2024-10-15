class FaltanParametros(Exception):
    def __init__(self, message="Faltan parámetros para realizar la operación"):
        self.message = message
        super().__init__(self.message)
