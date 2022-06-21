import base64
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from itertools import chain
from myapp.models import Profile, Post, likePost, Follower
import random


# Create your views here.
@login_required(login_url='signup')
def index(request):
    user_object= User.objects.get(username= request.user.username)
    user_profile= Profile.objects.get(user= user_object)

    user_following_list= []
    feed= []

    user_following= Follower.objects.filter(follower= request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists= Post.objects.filter(user= usernames)
        feed.append(feed_lists)

    current_post= Post.objects.filter(user= request.user.username)
    feed.append(current_post)

    feed_list= list(chain(*feed))

    #user suggestions
    all_users= User.objects.all()
    user_following_all= []

    for user in user_following:
        user_list= User.objects.get(username= user.user)
        user_following_all.append(user_list)

    new_suggestion_list= [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user= User.objects.filter(username= request.user.username)

    final_suggestion_list= [x for x in list(new_suggestion_list) if (x not in list(current_user))]
    random.shuffle(final_suggestion_list)

    username_profile= []
    username_profile_list= []

    for users in final_suggestion_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists= Profile.objects.filter(id_user= ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list= list(chain(*username_profile_list))
    
    context= {
        'posts': feed_list,
        'user_object': user_object,
        'user_profile': user_profile,
        'suggestions_username_profile_list': suggestions_username_profile_list[:3]
    }
    return render(request, 'index.html', context)

def signup(request):
# for signup 
    if request.method == 'POST':
        username_s = request.POST['username_s']
        email= request.POST['email']
        password_s= request.POST["password_s"]
        password_2_s= request.POST['password_2_s']

        
        if password_s == password_2_s:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('login')
            elif User.objects.filter(username= username_s).exists():
                messages.info(request, 'Username already taken.')
                redirect ('login')

            else:
                user= User.objects.create_user(username= username_s, email= email, password= password_s)
                user.save();

                user_login= auth.authenticate(username= username_s, password= password_s)
                auth.login(request,  user_login)
                
                user_model = User.objects.get(username = username_s)
                new_profile = Profile.objects.create(user= user_model, id_user= user_model.id)
                new_profile.save();
                return redirect('/settings')
        else:
            messages.info(request, 'Passwords not matching.')
            return redirect('login')
    else:
        return render(request, 'login.html')  

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        
        user= auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signup')
    else:
        return redirect('signup')

@login_required(login_url='signup')
def search(request):
    user_object= User.objects.get(username= request.user.username)
    user_profile= Profile.objects.get(user= user_object)

    if request.method== 'POST':
        username= request.POST['username']
        username_object= User.objects.filter(username__icontains= username)

        username_profile= []
        username_profile_list= []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists= Profile.objects.filter(id_user= ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))

    context= {
        'user_object': user_object,
        'user_profile': user_profile,
        'username_profile_list': username_profile_list
    }

    return render(request, 'search.html', context)

@login_required(login_url='signup')
def settings(request):
    user_profile= Profile.objects.get(user= request.user)

    if request.method== 'POST':

        if request.FILES.get('profile-image')== None:
            image= user_profile.profilePic
            bio= request.POST['bio']
            location= request.POST['location']

            user_profile.profilePic= image
            user_profile.bio= bio
            user_profile.location= location
            user_profile.save();

        if request.FILES.get('profile-image')!= None:
            image= request.FILES.get('profile-image')
            bio= request.POST['bio']
            location= request.POST['location']

            user_profile.profilePic= image
            user_profile.bio= bio
            user_profile.location= location
            user_profile.save();
        
        return redirect('settings')

    context={
       'user_profile': user_profile
    }
    return render(request, 'account.html', context)

@login_required(login_url='signup')
def profile(request, pk):
    user_object= User.objects.get(username= pk)
    user_profile= Profile.objects.get(user= user_object)
    user_posts= Post.objects.filter(user= pk)
    user_post_number= len(user_posts)
    current_user= User.objects.get(username= request.user.username)
    current_user_profile= Profile.objects.get(user= current_user)

    follower= request.user.username
    user= pk

    if Follower.objects.filter(follower= follower, user= user).first():
        btnTxt= 'Unfollow'

    else:
        btnTxt= 'Follow'

    user_followers= len(Follower.objects.filter(user= pk))
    user_following= len(Follower.objects.filter(follower= pk))

    context= {
        'user_followers': user_followers,
        'user_following': user_following,
        'btnTxt': btnTxt,
        'current_user': current_user,
        'current_user_profile': current_user_profile,
        'user_post_number': user_post_number,
        'user_posts': user_posts,
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='signup')
def upload(request):
    if request.method== 'POST':
        user= request.user.username
        image= request.FILES.get('image')
        caption= request.POST['caption']

        new_post= Post.objects.create(user= user, image= image, caption= caption)
        new_post.save();

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signup')
def like_post(request):
    username= request.user.username
    post_id= request.GET.get('post_id')

    post= Post.objects.get(id= post_id)

    like_filter= likePost.objects.filter(post_id= post_id, username= username).first()

    if like_filter is None:
        new_like= likePost.objects.create(post_id= post_id, username= username)
        new_like.save();
        post.likies_no= post.likies_no+1
        post.save();
        return redirect('/')

    else:
        like_filter.delete();
        post.likies_no= post.likies_no-1
        post.save();
        return redirect('/')

@login_required(login_url='signup')
def like_post_via_profile(request):
    username= request.user.username
    post_id= request.GET.get('post_id')

    post= Post.objects.get(id= post_id)

    like_filter= likePost.objects.filter(post_id= post_id, username= username).first()

    if like_filter is None:
        new_like= likePost.objects.create(post_id= post_id, username= username)
        new_like.save();
        post.likies_no= post.likies_no+1
        post.save();
        return redirect('/profile/'+username)

    else:
        like_filter.delete();
        post.likies_no= post.likies_no-1
        post.save();
        return redirect('/profile/'+username)

@login_required(login_url='signup')
def post_upload_via_profile(request):
    if request.method== 'POST':
        user= request.user.username
        image= request.FILES.get('image_upload')
        caption= request.POST['caption']

        new_post= Post.objects.create(user= user, image= image, caption= caption)
        new_post.save();

        return redirect('/profile/'+user)
    else:
        return redirect('/profile/'+user)

@login_required(login_url='signup')   
def follow(request):
    if request.method== 'POST':
        follower= request.POST['follower']
        user= request.POST['user']

        if Follower.objects.filter(follower= follower, user= user).first():
            delete_follower= Follower.objects.get(follower= follower, user= user)
            delete_follower.delete();
            return redirect('/profile/'+user)
        
        else:
            new_folloewr= Follower.objects.create(follower= follower, user= user)
            new_folloewr.save();
            return redirect('/profile/'+user)

    else:
        return redirect('/')

@login_required(login_url='signup')
def logout(request):
     auth.logout(request)
     return redirect('signup')