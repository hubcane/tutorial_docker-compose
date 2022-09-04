from django.http import Http404
from django.shortcuts import render, redirect
from .models import Board
from tag.models import Tag
from .forms import Boardform
from fcuser.models import Fcuser
from django.core.paginator import Paginator

# Create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시물을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board':board})

def board_write(request):
    if not request.session.get('user'):
        print('user not found')
        return redirect('/fcuser/login')

    if request.method == 'POST':
        form = Boardform(request.POST)
        if form.is_valid():

            user_id = request.session.get('user')

            tags = form.cleaned_data['tags'].split(', ')

            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            for tag in tags:
                if not tag: continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = Boardform()
        return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})