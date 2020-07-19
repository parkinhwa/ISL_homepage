import math
from django.shortcuts import render, get_object_or_404, redirect
from .models import DjangoBoard
# from .forms import NewDjangoBoard
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def board(request):
    boards = DjangoBoard.objects
    
    board_list = DjangoBoard.objects.all().order_by('-id')
    # 게시판 모든 글들을 대상으로 한다.
    num = 5
    paginator = Paginator(board_list, num)
    # 게시판 객체 num 개를 한 페이지로 자른다.
    board_page = request.GET.get('page')
    # request된 페이지를 변수에 담는다.
    post = paginator.get_page(board_page) 
    # request된 페이지를 얻어온 뒤 post에 저장

    page_numbers_range = 5
    #화면에 보여줄 페이지 번호 갯수
    max_index = len(paginator.page_range)
    current_page = int(board_page) if board_page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]    
    
    return render(request, 'board.html', {'boards':boards, 'post':post,'page_range':page_range,'board_list':board_list})


# def create(request):
#     # 새로운 데이터 블로그 글 저장하는 역할 == POST
#     if request.method == 'POST':
#         # 입력된 블로그 글들을 저장
#         djangoBoard = DjangoBoard(request.POST)
#         if djangoBoard.is_valid:
#             djangoboard = DjangoBoard()
#             djangoboard.subject = request.GET['title']
#             djangoboard.memo = request.GET['body']
#             djangoboard.name = request.user
#             djangoboard.created_date = timezone.datetime.now()
#             djangoboard.save()
#             return redirect('/detail/')
#         #글쓰기 페이지를 띄워주는 역할 == GET
#         else:
#             # 단순히 입력받을 수 있는 form을 띄워줘라
#             form = NewDjangoBoard()
#             return render(request, 'write.html',{'form':form})
#     #    입력된 블로그 글들을 저장해라
#     #    글쓰기 페이지를 띄워주는 역할 == GET(!=POST)

def create(request):
    djangoboard = DjangoBoard()
    djangoboard.subject = request.GET['title']
    djangoboard.memo = request.GET['body']
    djangoboard.name = request.user
    djangoboard.created_date = timezone.datetime.now()
    djangoboard.save()
    return redirect('/board/')

def update(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    if request.method == "POST":
        # 수정할 게시판의 글 객체 가져오기
        board_detail.subject = request.POST['edit_title']
        board_detail.memo = request.POST['edit_body']
        board_detail.created_date = timezone.datetime.now()
        board_detail.save()
        return redirect('board')
    else:
        return render(request, 'edit.html',{'board':board_detail} )
    #해당하는 게시판의 글 객체 pk에 맞는 입력공간
    
    


def delete(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    board_detail.delete()
    return redirect('board')

def detail(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    return render(request, 'detail.html',{'board':board_detail})

def write(request):
    return render(request,'write.html')

def edit(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    return render(request, 'edit.html',{'board':board_detail} )
