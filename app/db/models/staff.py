from sqlalchemy import column, integer,string
from app.db.session import Base

class staff(Base):
    __tablename__ = "staff"
    id = column(integer, primary_key=True, index=True)
    first_name = column(string)
    email = column(string)
    password = column(string)
    phone = column(string)
    address = column(string)
    role = column(string)
    status = column(string)
    created_at = column(string)
    updated_at = column(string)
    deleted_at = column(string)
    created_by = column(string)
    updated_by = column(string)
    deleted_by = column(string)
    def __repr__(self):
        return f"<staff(name={self.name}, email={self.email}, password={self.password}, phone={self.phone}, address={self.address}, role={self.role}, status={self.status}, created_at={self.created_at}, updated_at={self.updated_at}, deleted_at={self.deleted_at}, created_by={self.created_by}, updated_by={self.updated_by}, deleted_by={self.deleted_by})>"