from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum, Topic, Post
from .forms import TopicForm, PostForm

def forum_list(request):
    """
    Display a list of all forums.
    """
    forums = Forum.objects.all()
    return render(request, 'forum_list.html', {'forums': forums})

def topic_list(request, forum_id):
    """
    Display a list of topics for a specific forum.

    Parameters:
    forum_id (int): The ID of the forum whose topics are to be displayed.

    Returns:
    HttpResponse: Renders the 'topic_list.html' template with the forum and its topics.
    """
    forum = get_object_or_404(Forum, id=forum_id)
    topics = forum.topics.all()
    return render(request, 'topic_list.html', {'forum': forum, 'topics': topics})

def topic_detail(request, topic_id):
    """
    Display details for a specific topic and handle post creation.

    Parameters:
    topic_id (int): The ID of the topic to display.

    Returns:
    HttpResponse: Renders the 'topic_detail.html' template with the topic details and posts.
    """
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.posts.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = PostForm()

    return render(request, 'topic_detail.html', {'topic': topic, 'posts': posts, 'form': form})

@login_required
def new_topic(request, forum_id):
    """
    Create a new topic within a specific forum.

    Parameters:
    forum_id (int): The ID of the forum where the new topic will be created.

    Returns:
    HttpResponse: Renders the 'new_topic.html' template with the form for creating a new topic.
    """
    forum = get_object_or_404(Forum, pk=forum_id)
    
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.forum = forum
            topic.created_by = request.user
            topic.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = TopicForm()
    
    return render(request, 'new_topic.html', {'forum': forum, 'form': form})

@login_required
def edit_topic(request, topic_id):
    """
    Edit an existing topic.

    Parameters:
    topic_id (int): The ID of the topic to be edited.

    Returns:
    HttpResponse: Renders the 'edit_topic.html' template with the form for editing the topic.
    """
    topic = get_object_or_404(Topic, pk=topic_id)

    if request.user != topic.created_by and not request.user.is_staff:
        return redirect('topic_detail', topic_id=topic.id)
    
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = TopicForm(instance=topic)
    
    return render(request, 'edit_topic.html', {'topic': topic, 'form': form})

@login_required
def delete_topic(request, topic_id):
    """
    Delete an existing topic.

    Parameters:
    topic_id (int): The ID of the topic to be deleted.

    Returns:
    HttpResponse: Renders a confirmation page or redirects to the forum list after deletion.
    """
    topic = get_object_or_404(Topic, id=topic_id)

    if request.user != topic.created_by and not request.user.is_staff:
        return redirect('topic_detail', topic_id=topic_id)

    if request.method == 'POST':
        topic.delete()
        return redirect('forum_list')
    
    return render(request, 'confirm_delete.html', {'topic': topic})

@login_required
def edit_post(request, post_id):
    """
    Edit an existing post.

    Parameters:
    post_id (int): The ID of the post to be edited.

    Returns:
    HttpResponse: Renders the 'edit_post.html' template with the form for editing the post.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.created_by and not request.user.is_staff:
        return redirect('topic_detail', topic_id=post.topic.id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', topic_id=post.topic.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    """
    Delete an existing post.

    Parameters:
    post_id (int): The ID of the post to be deleted.

    Returns:
    HttpResponse: Renders a confirmation page or redirects to the topic detail page after deletion.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.created_by and not request.user.is_staff:
        return redirect('topic_detail', topic_id=post.topic.id)

    if request.method == 'POST':
        post.delete()
        return redirect('topic_detail', topic_id=post.topic.id)

    return render(request, 'confirm_delete.html', {'post': post})
