from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: int
    _name_: str

    # Automatically generate _tablename_
    @declared_attr
    def _tablename_(cls) -> str:
        return cls._name_.lower()
    