from django.shortcuts import render, get_object_or_404, redirect
from .models import DjangoBoard
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def board(request):
    boards = DjangoBoard.objects

    board_list = DjangoBoard.objects.all()
    paginator = Paginator(board_list, 2)
    board_page = request.GET.get('page')
    board_page_post = paginator.get_page(board_page)
    return render(request, 'board.html', {'boards':boards, 'board_page_post':board_page_post})


def create(request):
    djangoboard = DjangoBoard()
    djangoboard.subject = request.GET['title']
    djangoboard.memo = request.GET['body']
    djangoboard.created_date = timezone.datetime.now()
    djangoboard.save()
    return redirect('/board/')

def detail(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    return render(request, 'detail.html',{'board':board_detail})

def write(request):
    return render(request,'write.html')