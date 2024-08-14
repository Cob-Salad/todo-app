from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


from models import Todo, GetTodosResponse


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TODOS = [Todo(id=1, item="Teach Class"), Todo(id=2, item="Taxes"),]

@app.get("/todo")
async def get_todos() -> GetTodosResponse:
    return GetTodosResponse(data=TODOS) 

@app.post("/todo")
async def create_todo(a: Todo) -> None:
    return TODOS.append(a)

@app.put("/todo/{id}")
async def update_todo(id: int, updated_todo: Todo):
    for i, todo in enumerate(TODOS):
        if TODOS.id == id:
            TODOS[i] = updated_todo



@app.delete("/todo/{id}")
async def delete_todo(id: int):
    for i, todos in enumerate(TODOS):
        if todo.id == id:
            TODOS.pop(i)
