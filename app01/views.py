from django.shortcuts import render
from app01.models import *
from django.core.paginator import Paginator ,EmptyPage
# Create your views here.
def index(request):
   # # 批量添加数据
   #  book_list = []
   #  for i in range(100):
   #      book = Book(title="book_%s" % i, price=i * i)
   #      book_list.append(book)
   #  Book.objects.bulk_create(book_list)
    bool_lish=Book.objects.all()
    #分页器
    paginator = Paginator(bool_lish ,3) #每页显示的条数
    print (paginator.count)#显示总条数
    print (paginator.num_pages) #显示总页数
    print(paginator.page_range) #页码的列表
    current_page_num = int(request.GET.get("page", 1)) #浏览器返回的页数
    if paginator.num_pages >11:
       if current_page_num -5 <1:
            page_range= range(1,12)
       elif current_page_num + 5 >paginator.num_pages:
           page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
       else:
           page_range = range(current_page_num -5, current_page_num + 6)
    else:
       page_range = paginator.page_range
    try:
        page1=paginator.page(current_page_num) #跳转的第几页
            # 拿数据的第一种方法
        print(page1.object_list)
            # for i in page1:
            #     print (i) # 查看别页数http://127.0.0.1:8000/index/?page=3 后面加参数
    except  EmptyPage as e:
       page1 = paginator.page(1)
    return render(request ,"index.html",locals())
