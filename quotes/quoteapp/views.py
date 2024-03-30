from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# from .forms import QuoteForm, AuthorForm
from .models import Quote, Author, QuoteReg, AuthorReg, QuoteRegField
from .forms import AuthorForm, QuoteForm
# Create your views here.
def main(request):
    # quotes = Quote.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    quotes = Quote.objects.all()
    quotes_added = QuoteReg.objects.all()
    return render(request, 'quoteapp/index.html', {"quotes": quotes, "quotes_added": quotes_added})
# quotes = Quote.objects.filter(user=request.user).all() if request.user.is_authenticated else []
def author(request, quote_author):
    try:
        author = Author.objects.get(fullname=quote_author)
    except Author.DoesNotExist:
        # Якщо об'єкт `Author` не знайдено, шукати в моделі `AuthorReg`
        author = get_object_or_404(AuthorReg, fullname=quote_author)
    return render(request, 'quoteapp/author.html', {"author": author})


def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author_reg = form.save(commit=False)
            # tag.user = request.user
            author_reg.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/addauthor.html', {'form': form})

    return render(request, 'quoteapp/addauthor.html', {'form': AuthorForm()})

def addquote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            add_quote = form.save(commit=False)
            # tag.user = request.user
            add_quote.save()
            author = AuthorReg.objects.get(fullname=QuoteRegField.author)
            QuoteReg.objects.get_or_create(description=QuoteRegField.description, author=author)
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/addquote.html', {'form': form})

    return render(request, 'quoteapp/addquote.html', {'form': QuoteForm()})