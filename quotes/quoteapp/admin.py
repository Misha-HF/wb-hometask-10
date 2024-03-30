from django.contrib import admin
from .models import Author, Quote, AuthorReg, QuoteReg, QuoteRegField

# Register your models here.
admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(AuthorReg)
admin.site.register(QuoteReg)
admin.site.register(QuoteRegField)