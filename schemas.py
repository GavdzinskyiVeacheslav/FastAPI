from typing import List
from pydantic import BaseModel
from datetime import date

class Genre(BaseModel):
	name: str


class Book(BaseModel):
	title: str
	writer: str
	duration: str
	data: date
	summary: str
	genres: List[Genre]
	pages: int
