class Singleton:
    _unique_instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._unique_instance:
            cls._unique_instance = super(Singleton, cls).__new__(cls)
        return cls._unique_instance

    def getValue(self) -> str:
        return self._unique_instance

    def setValue(self, value: str):
        self._unique_instance = value
