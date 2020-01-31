class StraalException(Exception):
    _REGISTRY = {}

    def __init_subclass__(cls, code: int, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._register_straal_exc(code)

    @classmethod
    def _register_straal_exc(cls, code: int):
        if code in cls._REGISTRY:
            raise RuntimeError(f"Duplicate straal_exc entry for {code}")

        cls._REGISTRY[code] = cls


class ReferenceAlreadyExists(StraalException, code=12005):
    ...


class ReferenceTooLong(StraalException, code=12006):
    ...
