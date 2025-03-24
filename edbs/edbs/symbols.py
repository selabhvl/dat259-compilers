from typing import Literal

EDBS_TYP = Literal["streng", "tal", "hugseliste"]

ALL_TYPES = {'streng', 'tal', 'hugseliste'}

class EDBSException(Exception):

    def __init__(self, errmsg: str):
        super.__init__(errmsg)
        self.msg = errmsg

class UndefinedVarRef(EDBSException):
    def __init__(self, name: str):
        super().__init__(f"FEIL! Stedfortreter med namn '{name}' finnast ikkje")
        self.name = name

class UndefinedModuleRef(EDBSException):
    def __init__(self, name: str):
        super().__init__(f"FEIL! Modul med namn '{name}' finnast ikkje")
        self.name = name

class VarAlreadyDefined(EDBSException):
    def __init__(self, name: str):
        super().__init__(f"FEIL! Stedfortreter med namn '{name}' finnast alt!")
        self.name = name

class UnsoundTypes(EDBSException):
    def __init__(self, name: str, expected: set[EDBS_TYP], actual: set[EDBS_TYP]):
        super().__init__(f"FEIL! Stedfortreter {name} har feil type! Det forventes å være {expected} mens den er {actual}")
        self.name = name
        self.expected = expected
        self.actual = actual


class Hugseliste:

    def __init__(self, size: int, current_idx: int, keys: list, values: list):
        self.size = size
        self.current_idx = current_idx
        self.keys = keys
        self.values = values

    def next(self):
        self.current_idx += 1

    def current(self):
        return self.values[self.current_idx]

    def reset(self, idx: int):
        self.current_idx = idx

    def find(self, key):
        return self.keys.index(key)


class Var:

    def __init__(self, name: str, admissible_types: set[EDBS_TYP] = ALL_TYPES):
        self.name = name
        self.admissible_types = admissible_types

    def is_type_determined(self) -> bool:
        return len(self.admissible_types) == 1

    def get_type(self) -> EDBS_TYP:
        assert self.is_type_determined()
        return self.admissible_types.__iter__().__next__()


class Module:

    def __init__(self, formal_params, result, body):
        self.formal_params = formal_params
        self.result = result
        self.body = body


class SymbolTable:

    def __init__(self, next = None):
        self.storage = {}
        self.types = {}
        self.modules = {}
        self.next = next

    def add_var(self, name: str, value: float):
        if name in self.storage:
            raise VarAlreadyDefined(name)
        self.storage[name] = value

    def get_var(self, name: str):
        if name not in self.storage:
            if self.next is not None:
                return self.next.get_var(name)
            else:
                raise UndefinedVarRef(name)
        return self.storage[name]

    def mutate_var(self, name: str, value):
        if self.next is not None:
            self.next.mutate_var(name, value)
        else:
            self.storage[name] = value

    def is_defined(self, name: str):
        result = name in self.storage
        if not result and self.next is not None:
            return self.next.is_defined(name)
        return result

    def register_var_name(self, name: str):
        self.types[name] = {"streng", "tal", "hugseliste"}
