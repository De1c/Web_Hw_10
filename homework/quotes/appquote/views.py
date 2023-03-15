from collections import Counter

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote


def main(request):
    quotes = Quote.objects.all()
    all_tags = []
    most_popular_tag = []
    for el in quotes:
        for tag in el.show_quote_tags():
            all_tags.append(tag)
    top_tags = Counter(all_tags).most_common(10)
    for top in top_tags:
        most_popular_tag.append(top[0])
    paginator = Paginator(quotes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "appquote/index.html",
                  context={"quotes": quotes, "most_popular_tag": most_popular_tag, 'page_obj': page_obj})


@login_required
def addtag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='appquote:main')
        else:
            return render(request, 'appquote/addtag.html', {'form': form})

    return render(request, 'appquote/addtag.html', {'form': TagForm()})


@login_required
def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='appquote:main')
        else:
            return render(request, 'appquote/addauthor.html', {'form': form})

    return render(request, 'appquote/addauthor.html', {'form': AuthorForm()})


@login_required
def addqoute(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

                return redirect(to='appquote:main')
        else:
            return render(request, 'appquote/addquote.html', {"tags": tags, "authors": authors, 'form': form})

    return render(request, 'appquote/addquote.html', {"tags": tags, "authors": authors, 'form': QuoteForm()})


def author_page(request, fullname):
    authors = get_object_or_404(Author, fullname=fullname)

    return render(request, "appquote/author.html", {"author": authors})


def tag_page(request, tag):
    tags = get_object_or_404(Tag, name=tag)
    quotes = Quote.objects.all()
    return render(request, "appquote/tag.html", {"tag": tags, "quotes": quotes})