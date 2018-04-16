import django.dispatch

book_publised = django.dispatch.Signal(providing_args=["book", “author”])