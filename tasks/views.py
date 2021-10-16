from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from tasks.models import Books
from tasks.serializers import BooksSerializer
from comments.serializers import CommentSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


    @action(methods=['post', ], serializer_class=CommentSerializer, detail=True)
    def comments(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        books = self.get_object()

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, books=books)
            return Response(serializer.data)

    @action(methods=['post', ], detail=True)
    def upvote(self, request, *args, **kwargs):
        books = self.get_object()
        books.upvotes_amount += 1
        books.save()
        serializer = self.get_serializer_class()(instance=books)
        return Response(serializer.data)

    @action(methods=['post', ], detail=True, permission_classes=[IsAdminUser, ])
    def drop_upvotes(self, request, *args, **kwargs):
        books = self.get_object()
        books.upvotes_amount = 0
        books.save()
        serializer = self.get_serializer_class()(instance=books)
        return Response(serializer.data)
    










# для отложеных задач  selery_bit

# import schedule
# import time

# def some_func():
#     print("I am just a lonely func")

# schedule.every().day.at("10:30").do(some_func)


# while True:
#     schedule.run_pending()
#     time.sleep(1)


# pip3 install openpyxl

# import openpyxl


# wb = openpyxl.load_workbook(filename = '1.xlsx')
# sheet = wb['Лист 1']
# sheet['A2'] = 'значение в ячейке'

# wb.save('1.xlsx')


# import telebot
# import schedule
# import time


# bot = telebot.TeleBot("")


# def standupp():
#     bot.send_message(номер_канала, "текст сообщения")


# schedule.every().day.at("20:18").do(standupp)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# bot.polling()


# import requests
# from bs4 import BeautifulSoup

# url = 'https://24.kg/'

# source = requests.get(url)
# main_text = source.text
# soup = BeautifulSoup(main_text, "html.parser")

# news = [zs.text for zs in soup.find_all('div', {'class': 'one'})]
# print(news[:10])
