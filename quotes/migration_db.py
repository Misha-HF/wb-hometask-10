from quoteapp.models import Author, Quote
from models_mongodb import Quote as MongoQuote, Author as MongoAuthor
import connect


# Отримання даних з MongoDB та створення відповідних записів у PostgreSQL
mongo_authors = MongoAuthor.objects()
for mongo_author in mongo_authors:
    # Створимо автора в PostgreSQL
    Author.objects.get_or_create(fullname=mongo_author.fullname, born_date=mongo_author.born_date, born_location=mongo_author.born_location, description=mongo_author.description)

# Отримання даних з MongoDB та створення відповідних записів у PostgreSQL для моделі Quote
mongo_quotes = MongoQuote.objects()
for mongo_quote in mongo_quotes:
    # Знайдемо або створимо автора
    author = Author.objects.get(fullname=mongo_quote.author)
    Quote.objects.create(description=mongo_quote.quote, author=author)

print("success")