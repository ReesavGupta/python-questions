from collections import Counter, defaultdict

posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]},
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120},
}

def most_popular_tags(posts):
    all_tags = []
    for post in posts:
        all_tags.extend(post['tags'])
    tag_counts = Counter(all_tags)
    print("Most Popular Tags:")
    for tag, count in tag_counts.most_common():
        print(f"{tag}: {count}")
    print()

def user_engagement(posts):
    likes_per_user = defaultdict(int)
    for post in posts:
        likes_per_user[post['user']] += post['likes']
    print("User Engagement (Total Likes):")
    for user, likes in likes_per_user.items():
        print(f"{user}: {likes} likes")
    print()
    return likes_per_user

def top_posts_by_likes(posts):
    sorted_posts = sorted(posts, key=lambda x: x['likes'], reverse=True)
    print("Top Posts by Likes:")
    for post in sorted_posts:
        print(f"Post ID {post['id']} by {post['user']}: {post['likes']} likes")
    print()

def user_activity_summary(posts, users):
    post_count = defaultdict(int)
    total_likes = defaultdict(int)

    for post in posts:
        user = post['user']
        post_count[user] += 1
        total_likes[user] += post['likes']

    print("User Activity Summary:")
    for user in users:
        print(f"{user}:")
        print(f"  Posts: {post_count[user]}")
        print(f"  Total Likes: {total_likes[user]}")
        print(f"  Followers: {users[user]['followers']}")
        print(f"  Following: {users[user]['following']}")
    print()


if __name__ == "__main__":
    most_popular_tags(posts)
    engagement = user_engagement(posts)
    top_posts_by_likes(posts)
    user_activity_summary(posts, users)
