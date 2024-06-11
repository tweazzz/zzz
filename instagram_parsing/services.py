import requests
from bs4 import BeautifulSoup
import json
import instaloader
from django.utils import timezone
from .models import InstagramPost
from admin_app.models import School_SocialMedia
from itertools import islice



def update_instagram_posts():
    schools_with_instagram = School_SocialMedia.objects.filter(type=School_SocialMedia.INSTAGRAM)

    for school_social in schools_with_instagram:
        account_url = school_social.account_name.rstrip('/').split('/')[-1]
        posts = fetch_instagram_posts(account_url, max_posts=10)
        school = school_social.school

        current_posts = InstagramPost.objects.filter(school=school)
        current_post_ids = set(current_posts.values_list('post_id', flat=True))

        fetched_post_ids = set(post['post_id'] for post in posts)

        posts_to_delete = current_posts.exclude(post_id__in=fetched_post_ids)
        posts_to_delete.delete()

        for post in posts:
            InstagramPost.objects.update_or_create(
                post_id=post['post_id'],
                school=school,
                defaults={
                    'image_url': post['image_url'],
                    'caption': post['caption'],
                    'created_at': post['created_at'],
                    'post_url': post['post_url'],
                    'video_url': post['video_url'],
                }
            )


def fetch_instagram_posts(account_name, max_posts=10):
    L = instaloader.Instaloader()


    try:
        profile = instaloader.Profile.from_username(L.context, account_name)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Account {account_name} does not exist.")
        return []
    except Exception as e:
        print(f"Error fetching data for account {account_name}: {e}")
        return []

    post_data = []
    for post in islice(profile.get_posts(), max_posts):
        post_data.append({
            'post_id': post.shortcode,
            'image_url': post.url,
            'caption': post.caption,
            'created_at': timezone.datetime.fromtimestamp(post.date_utc.timestamp()),
            'post_url': f"https://www.instagram.com/p/{post.shortcode}/",
            'video_url': post.video_url if post.is_video else None
        })

    return post_data