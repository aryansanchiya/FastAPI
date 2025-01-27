from fastapi import FastAPI

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