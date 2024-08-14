from pydantic import BaseModel



class Todo(BaseModel):
    id: int
    item: str

class GetTodosResponse(BaseModel):
    data: list[Todo]

class UpdateTodoRequest(BaseModel):
    item: str
