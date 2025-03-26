from __future__ import annotations
from typing import Literal, Any

EDBS_TYP = Literal["streng", "tal", "hugseliste"]

ALL_TYPES = {'streng', 'tal', 'hugseliste'}

class EDBSException(Exception):

    def __init__(self, errmsg: str, line: int, col: int):
        msg = f"FEIL! {errmsg} (i linje {line} kolonne {col})"
        super().__init__(msg)
        self.msg = msg
        self.line = line
        self.col = col

class UndefinedVarRef(EDBSException):
    def __init__(self, name: str, line: int, col: int):
        super().__init__(f"Stedfortreter med namn '{name}' finnast ikkje", line, col)
        self.name = name


class UndefinedModuleRef(EDBSException):
    def __init__(self, name: str, line: int, col: int):
        super().__init__(f"Modul med namn '{name}' finnast ikkje", line, col)
        self.name = name

class VarAlreadyDefined(EDBSException):
    def __init__(self, name: str, line: int, col: int):
        super().__init__(f"Stedfortreter med namn '{name}' finnast alt!", line, col)
        self.name = name

class UnsoundTypes(EDBSException):
    def __init__(self, name: str, expected: set[EDBS_TYP], actual: set[EDBS_TYP], line: int, col: int):
        super().__init__(f"Stedfortreter {name} har feil type! Det forventes å være {expected} mens den er {actual}", line, col)
        self.name = name
        self.expected = expected
        self.actual = actual

class ModuleCallParameterListMismatch(EDBSException):
    def __init__(self, module_name, expected: int, actual: int, line: int, col: int):
        super().__init__(f"Kall av modul med namd {module_name} ble gjort med feil tal av parametre! Det forventes å {expected} stykk mens det er {actual}", line, col)
        self.module_name = module_name
        self.expected = expected
        self.actual = actual
        
class UnsupportedFeature(EDBSException):
    
    def __init__(self, feature_name: str, line: int, col: int):
        super().__init__(f"Funksjonalitet '{feature_name}' er ikkje støtta enda", line, col)

class Hugseliste:

    def __init__(self, size: int, current_idx: int, keys: list[Val], values: list[Val]):
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

    def find(self, key: Val):
        return self.keys.index(key)


Val = str | float | Hugseliste


class Var:

    def __init__(self, name: str, initial_value: Val | None = None, admissible_types: set[EDBS_TYP] = ALL_TYPES, is_constant: bool = True):
        self.name = name
        self.admissible_types = admissible_types
        self.is_constant = is_constant
        self.value = initial_value

    def is_type_determined(self) -> bool:
        return len(self.admissible_types) == 1

    def get_type(self) -> EDBS_TYP:
        assert self.is_type_determined()
        return self.admissible_types.__iter__().__next__()

    def get_val(self) -> Val | None:
        return self.value

    def narrow_and_type(self, expected_types: set[EDBS_TYP], line: int, col: int):
        result_types = expected_types.intersection(self.admissible_types)
        if len(result_types) == 0:
            raise UnsoundTypes(self.name, expected_types, self.admissible_types, line, col)
        else:
            self.admissible_types = result_types
            return result_types

    def __repr__(self):
        if self.is_type_determined():
            return f"«{self.name}» er «{self.get_type()}» {'[konstant]' if self.is_constant else ''} {'og har fast verdi: «' + str(self.value) + "»" if self.value is not None else ''} "
        else:
            return f"«{self.name}» har uviss type (Kandidater = {self.admissible_types}) {'[konstant]' if self.is_constant else ''}"


class Module:

    def __init__(self, formal_params: list[str], result: str, line:int, col:int, body: Any):
        self.formal_param_names = formal_params
        self.result_param_name = result
        self.body = body
        self.symbols = SymbolTable()
        for v in formal_params:
            self.symbols.add_var(v, line, col)




class SymbolTable:

    def __init__(self, next: SymbolTable | None = None):
        self.storage = {}
        self.modules = {}
        self.next = next

    def __repr__(self):
        result = f"{len(self.storage.keys())} Stedfortreter (variabler):\n - "
        result += "\n - ".join([str(x) for x in self.storage.values()])
        if self.next is not None:
            result += "\nInnvikla kontekst: "
            result += self.next.__repr__()
        return result

    def get_module(self, name: str, line: int, col: int) -> Module:
        if name not in self.modules:
            raise UndefinedModuleRef(name, line, col)
        return self.modules[name]

    def add_var(self, name: str, line: int, col: int, value: Val | None = None) -> Var:
        if name in self.storage:
            raise VarAlreadyDefined(name, line, col)

        if isinstance(value, str):
            types = {'streng'}
        elif isinstance(value, float):
            types = {'tal'}
        elif isinstance(value, Hugseliste):
            types = {'hugseliste'}
        else:
            types = ALL_TYPES
        result = Var(name, initial_value=value, admissible_types=types)
        self.storage[name] = result
        return result

    def get_var(self, name: str, line: int, col: int) -> Var:
        if name not in self.storage:
            if self.next is not None:
                return self.next.get_var(name, line, col)
            else:
                raise UndefinedVarRef(name, line, col)
        return self.storage[name]

    def mutate_var(self, name: str, line: int, col:int, value: Val | None = None, typing: set[EDBS_TYP] = ALL_TYPES):
        if self.next is not None:
            return self.next.mutate_var(name, line, col, value=value)
        else:
            if name not in self.storage:
                self.storage[name] = Var(name)
            var = self.storage[name]
            var.is_constant = False
            var.value = value
            var.narrow_and_type(typing, line, col)
            return var


    def is_defined(self, name: str):
        result = name in self.storage
        if not result and self.next is not None:
            return self.next.is_defined(name)
        return result


