import json
from django.core.management.base import BaseCommand
from quotesapp.models import Author, Quote, Tag
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load data from JSON files'

    def handle(self, *args, **kwargs):
        # Загрузка авторов
        user = User.objects.get(id=1)
        
        with open('authors.json', encoding='utf-8') as authors_file:
            authors_data = json.load(authors_file)
            authors = [] 

            for author_data in authors_data:
                author = Author.objects.create(
                    full_name=author_data['fullname'],
                    born_date=author_data['born_date'],
                    born_location=author_data['born_location'],
                    description=author_data['description'],
                    user=user
                )
                authors.append(author)
                
                self.stdout.write(self.style.SUCCESS('Author added: %s' % author.full_name))
            
            
     # Загрузка цитат
        with open('quotes.json', encoding='utf-8') as quotes_file:
            quotes_data = json.load(quotes_file)
            
            for quote_data in quotes_data:
                # Найти автора по имени
                author = next((a for a in authors if a.full_name == quote_data['author']), None)
                
                if author: 
                    quote = Quote.objects.create(
                        quote=quote_data['quote'],
                        author=author,
                        user=user,
                        is_default=True
                    )

                    # Загрузка тегов
                    for tag_name in quote_data['tags']:
                        tag, created = Tag.objects.get_or_create(name=tag_name, user=user)
                        quote.tags.add(tag)

                    self.stdout.write(self.style.SUCCESS('Quote added: %s' % quote.quote))
                else:
                    self.stdout.write(self.style.ERROR('Author not found for quote: %s' % quote_data['quote']))