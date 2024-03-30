from django.core.management.base import BaseCommand
from quoteapp.models import Author, Quote, AuthorReg, QuoteRegField, QuoteReg
from models_mongodb import Quote as MongoQuote, Author as MongoAuthor
import connect


class Command(BaseCommand):
    help = "Migrate data from MongoDB to PostgreSQL"
    def handle(self, *args, **options):
        # mongo_authors = MongoAuthor.objects()
        # for mongo_author in mongo_authors:
        #     Author.objects.get_or_create(
        #         fullname=mongo_author.fullname,
        #         born_date=mongo_author.born_date,
        #         born_location=mongo_author.born_location,
        #         description=mongo_author.description
        #     )
        # mongo_quotes = MongoQuote.objects()
        # for mongo_quote in mongo_quotes:
        #     author = Author.objects.get(fullname=mongo_quote.author)
        #     Quote.objects.get_or_create(description=mongo_quote.quote, author=author)
        print("Migration completed successfully")
        AuthorReg.objects.all().delete()
        QuoteReg.objects.all().delete()
        QuoteRegField.objects.all().delete()
    
