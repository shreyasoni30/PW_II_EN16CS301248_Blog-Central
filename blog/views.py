from django.template.loader import get_template
from django.views import generic
from .models import Post
from .forms import CommentForm, ContactForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


class AboutView(generic.TemplateView):
    template_name = 'about.html'



def ContactView(request):
    template_name = 'contact.html'
    form = ContactForm()
    flag = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Contact Enquiry from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['shreya.barapatre.consultadd@gmail.com','shreya.s.consultadd@gmail.com']
            try:
                res = send_mail(subject=subject,message=message,from_email= sender, recipient_list=recipients)
                print(res)
                flag = 'Success'
            except BadHeaderError:
                return HttpResponse('Invalid Header found...')
    return render(request , template_name, {'form':form, 'flag':flag})



def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
