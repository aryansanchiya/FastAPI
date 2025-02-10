from fastapi import FastAPI, Body, Path, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id : int
    title : str
    author : str
    description : str
    rating : str
    published_year : int

    def __init__(self,id,title,author,description, rating, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year

class BookRequest(BaseModel):
    id : Optional[int] = Field(description="Default id is not needed!", default=None) 
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description : str = Field(min_length=1, max_length=100)
    rating : int = Field(gt=0, lt=6)
    published_year : int = Field(min_length=2000, max_length=2025)

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
        rating=4,
        published_year=2023
    ),
    Book(
        id=2,
        title="1984",
        author="George Orwell",
        description="A dystopian novel that delves into themes of government surveillance and totalitarianism.",
        rating=4,
        published_year=2020
    ),
    Book(
        id=3,
        title="Pride and Prejudice",
        author="Jane Austen",
        description="A classic romantic novel exploring love, reputation, and class in 19th-century England.",
        rating=4,
        published_year=2019
    ),
    Book(
        id=4,
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="A critique of the American Dream through the tragic story of Jay Gatsby and his unfulfilled love for Daisy Buchanan.",
        rating=4,
        published_year=2005
    ),
    Book(
        id=5,
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        description="A story of teenage rebellion and alienation, told by the iconic narrator Holden Caulfield.",
        rating=4.4,
        published_year=2002
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

@app.get("/get_book/{book_id}")
async def get_book(book_id:int = Path(gt=0)):       #Parameter Validation with Path
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.put("/update_book/")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.delete("/delete_book/{book_id}")
async def delete_book(book_id:int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

@app.get("/get_publish/{publish_year}")
async def get_publish_book(year:int):
    for book in BOOKS:
        if book.published_year == year:
            return book
            
def find_book_id(book:Book):
    # book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # print("IDD:",book.id)

    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    
    return book