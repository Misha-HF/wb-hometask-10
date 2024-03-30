from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest

# from .forms import QuoteForm, AuthorForm
from .models import Quote, Author, QuoteReg, AuthorReg, QuoteRegField
from .forms import AuthorForm, QuoteForm
# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    quotes_added = QuoteReg.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'quoteapp/index.html', {"quotes": quotes, "quotes_added": quotes_added})



def author(request, quote_author):
    try:
        author = Author.objects.get(fullname=quote_author)
    except Author.DoesNotExist:
        # Якщо об'єкт `Author` не знайдено, шукати в моделі `AuthorReg`
        author = get_object_or_404(AuthorReg, fullname=quote_author)
    return render(request, 'quoteapp/author.html', {"author": author})


@login_required
def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author_reg = form.save(commit=False)
            author_reg.user = request.user
            author_reg.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/addauthor.html', {'form': form})

    return render(request, 'quoteapp/addauthor.html', {'form': AuthorForm()})


@login_required
def addquote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            add_quote = form.save(commit=False)
            add_quote.user = request.user  # Додайте користувача до цитати
            add_quote.save()
            author_name = form.cleaned_data['author']  # Отримати ім'я автора з форми
            # Спробувати знайти автора в таблиці Author
            try:
                author = Author.objects.get(fullname=author_name)
                author_type = 'Author'
            except Author.DoesNotExist:
                # Якщо автор не знайдений в таблиці Author, спробуємо знайти в таблиці AuthorReg
                try:
                    author = AuthorReg.objects.get(fullname=author_name, user=request.user)
                    author_type = 'AuthorReg'
                except AuthorReg.DoesNotExist:
                    # Якщо автор не знайдений в обох таблицях, повертаємо помилку
                    return HttpResponseBadRequest("Author not found")
            # Створити новий об'єкт QuoteReg з описом цитати та об'єктом автора
            if author_type == 'Author':
                author_reg = AuthorReg.objects.get_or_create(fullname=author.fullname, user=request.user)[0]
                QuoteReg.objects.create(description=add_quote.description, author=author_reg, user=request.user)
            else:
                QuoteReg.objects.create(description=add_quote.description, author=author, user=request.user)
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/addquote.html', {'form': form})

    return render(request, 'quoteapp/addquote.html', {'form': QuoteForm()})



# def addquote(request):
#     if request.method == 'POST':
#         form = QuoteForm(request.POST)
#         if form.is_valid():
#             add_quote = form.save(commit=False)
#             # tag.user = request.user
#             add_quote.save()
#             author_name = form.cleaned_data['author']  # Отримати ім'я автора з форми
#             # Спробувати знайти автора в таблиці Author
#             try:
#                 author = Author.objects.get(fullname=author_name)
#             except Author.DoesNotExist:
#                 # Якщо автор не знайдений в таблиці Author, спробуємо знайти в таблиці AuthorReg
#                 try:
#                     author = AuthorReg.objects.get(fullname=author_name)
#                 except AuthorReg.DoesNotExist:
#                     # Якщо автор не знайдений в обох таблицях, повертаємо помилку
#                     return HttpResponseBadRequest("Author not found")
#             # Створити новий об'єкт QuoteReg з описом цитати та об'єктом автора
#             QuoteReg.objects.create(description=add_quote.description, author=author)
#             return redirect(to='quoteapp:main')
#         else:
#             return render(request, 'quoteapp/addquote.html', {'form': form})

#     return render(request, 'quoteapp/addquote.html', {'form': QuoteForm()})

