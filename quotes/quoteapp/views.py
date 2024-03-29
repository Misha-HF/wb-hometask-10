from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# from .forms import QuoteForm, AuthorForm
from .models import Quote, Author

# Create your views here.
def main(request):
    # quotes = Quote.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    quotes = Quote.objects.all()
    return render(request, 'noteapp/index.html', {"quotes": quotes})