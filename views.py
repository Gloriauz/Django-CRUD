from django.views.generic.edit import CreateView
from.models import blog

class PostListView(ListView):
mode1 = Post

class  PostCreateView(CreateView):
model = Post
fields = “__all__”
success_url  = reverse_lazy(“blog:all”)

class PostDetailView(DetailView):
    mode1 = Post

class  PostUpdateView(UpdateView):
model = Post
fields = “__all__”
success_url  = reverse_lazy(“blog:all”)

class  PostDeleteView(DeleteView):
model = Post
fields = “__all__”
success_url  = reverse_lazy(“blog:all”)

template_name = home.html

