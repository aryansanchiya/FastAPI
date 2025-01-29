from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id : int
    title : str
    author : str
    description : str
    rating : str

    def __init__(self,id,title,author,description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id : Optional[int] = Field(description="Default id is not needed!", default=None) 
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description : str = Field(min_length=1, max_length=100)
    rating : int = Field(gt=0, lt=6)

    # model_config = {
    #     "json_schema_extra": {
    #         "example" : {
    #             "title" : "A new book",
    #             "author" : "Add Author",
    #             "description" : "Add Description",
    #             "rating" : "Add Book Rating"
    #         }
    #     }
    # }

BOOKS = [
    Book(
        id=1,
        title="To Kill a Mockingbird",
        author="Harper Lee",
        description="A novel about the serious issues of rape and racial inequality, told through the eyes of a young girl.",
        rating=4
    ),
    Book(
        id=2,
        title="1984",
        author="George Orwell",
        description="A dystopian novel that delves into themes of government surveillance and totalitarianism.",
        rating=4
    ),
    Book(
        id=3,
        title="Pride and Prejudice",
        author="Jane Austen",
        description="A classic romantic novel exploring love, reputation, and class in 19th-century England.",
        rating=4
    ),
    Book(
        id=4,
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="A critique of the American Dream through the tragic story of Jay Gatsby and his unfulfilled love for Daisy Buchanan.",
        rating=4
    ),
    Book(
        id=5,
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        description="A story of teenage rebellion and alienation, told by the iconic narrator Holden Caulfield.",
        rating=4.4
    )
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create_book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(new_book)
    BOOKS.append(find_book_id(new_book))


def find_book_id(book:Book):
    # book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # print("IDD:",book.id)

    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    
    return book