from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Author, Quote, Tag
from .forms import QuoteForm, AuthorForm, TagForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def main(request):
    user_quotes = request.user.quotes.all()
    default_quotes = Quote.objects.filter(is_default=True)
    paginator = Paginator(quotes, 10) 

    page_number = request.GET.get('page')
    quotes = paginator.get_page(page_number)
    return render(request, 'quotesapp/index.html', {'user_quotes': user_quotes,
        'default_quotes': default_quotes,})


@login_required
def add_quote(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()
            form.save_m2m()
            
            choice_authors = Author.objects.filter(full_name__in=request.POST.getlist('authors'))
            for author in choice_authors.iterator():
                new_quote.author.add(author)
                
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_quote.html', {'form': form})
    
    form = QuoteForm()
    return render(request, 'quotesapp/add_quote.html', {'form': QuoteForm()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user
            new_author.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_author.html', {'form': form})
    
    return render(request, 'quotesapp/add_author.html', {'form': AuthorForm()})


@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save(commit=False)
            new_tag.user = request.user
            new_tag.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_tag.html', {'form': form})
    
    return render(request, 'quotesapp/add_tag.html', {'form': TagForm()})


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    quotes = tag.quotes.all()  # Retrieve all quotes related to this tag
    return render(request, 'quotesapp/tag_detail.html', {'tag': tag, 'quotes': quotes})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'quotesapp/about.html', {'author': author})


def top_tags():
    return Tag.objects.annotate(num_quotes=Count('quotes')).order_by('-num_quotes')[:10]



    

