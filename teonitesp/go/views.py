from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
# Create your views here.
from django.views.generic import ListView, DetailView
from go.models import Authors, Posts

from . import serializers
class AuthorsListView(ListView):
    model = Authors

class PostsListView(ListView):
    model = Posts

class PostDetalView(DetailView):
    model = Posts

    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(Posts, pk=self.kwargs.get("pk"))

class WordsCountApiView(APIView):


    def get(self, request, authorname=None):

        if not authorname:
            #If authorname is not given

            rows=self.counting_all()

            return Response({a[0]:a[1] for a in rows})

        else:
            #If authorname is given

            rows=self.counting_by_author(authorname)
            #checking for rows,  if is no rows it returns message
            if rows:
                return Response({a[0]:a[1] for a in rows})
            else:
                return Response({'message':'Author is not exist'})

    def counting_by_author(self, author):
        #checking for author
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT id_author
            FROM go_authors
            WHERE regexp_replace(lower(author), ' ','')=%s
            """,
            [author]
            )
            row=cursor.fetchone()
        #check that query returned row
        if row:

            with connection.cursor() as cursor:
                cursor.execute(
                """SELECT word, count(*) as many FROM
                (SELECT regexp_split_to_table(post,E'[\\\\.\\\\,\\\\;\\\\?\\\\!]?\\\s+') as word
                FROM go_posts WHERE id_author_id=%s)t
                GROUP BY word
                ORDER BY many DESC
                OFFSET 0
                LIMIT 10"""
                ,
                [str(row[0])]
                )
                rows = cursor.fetchall()

            return rows
        #if not functtion returning nothin

    def counting_all(self):
        with connection.cursor() as cursor:
            cursor.execute(
            """SELECT word, count(*) as many FROM
            (SELECT regexp_split_to_table(post,E'[\\\\.\\\\,\\\\;\\\\?\\\\!]?\\\s+') as word
            FROM go_posts)t
            GROUP BY word
            ORDER BY many DESC
            OFFSET 0
            LIMIT 10"""
            )
            rows = cursor.fetchall()

        return rows
