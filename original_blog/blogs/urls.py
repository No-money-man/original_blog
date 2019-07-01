from django.urls import path
from . import views

app_name='blogs'
urlpatterns=[
    path('', views.home, name='home'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('new_form/', views.new_form, name='new_form'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('form_detail/<int:blog_id>/', views.form_detail, name='form_detail'),
    path('form_delete/<int:blog_id>/', views.form_delete, name='form_delete'),
    # 第一引数の'detail/<int:blog_id>/'ではURLを指定しています。intは、ここに何かしらの数字が入ることを示しています。トップページからのリンクで、変数blog_idには数字が代入された状態で情報を受け取っているので、ここにはその数字が自動的に入力されることになります。また、ここに入った数字は変数blog_idに代入されてViewに渡されます。これで、URLhttp://127.0.0.1:8000/detail/1のページではid=1の記事の詳細ページを表示する準備をしています。ただし、まだViewやHTMLファイルを作っていないので、現段階でこのURLにアクセスしてもエラーが出ます。
    # 第二引数は、１つ上のpathと同様のことをしています。このURLでは、views.pyファイルのdetail関数が処理されることを意味しています。
    # 第三引数は、このURLにdetailという名前をつけています。名前をつけることで、<a href="{% url 'blogs:detail' blog_id=blog.id %}">記事を読む</a>のリンクをクリックした時にこのpathに飛ぶようになります。
]
