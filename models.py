from pydantic import BaseModel, Field
from typing import Optional ,List


class UserBase(BaseModel):
    # manadotory veriables (....) mee dot walin kiynne
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: int = Field(..., ge=18, le=100)
    role: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: str
    updated_at: str


class UserPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[str] = Field(None, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: Optional[int] = Field(None, ge=18, le=100)
    role: Optional[str] = None


class ProductBase(BaseModel):
    name : str = Field(..., min_length=3 , max_length=200)
    description : str = Field(..., min_length=3)
    price : int = Field(..., ge=0)
    category : str = Field(..., min_length=3 , max_length=100)
    in_stock : bool = True
    tags : List[str] = Field(default_factory=List)