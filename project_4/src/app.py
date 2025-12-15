from fastapi import FastAPI, HTTPException
from src.schemas import Create_Post

app = FastAPI()

posts = {
    1: {
        "title": "Check out my new car",
        "content": "Just picked up a new car and wanted to share some details and photos.",
        "location": "John Doe, PA"
    },
    2: {
        "title": "Morning workout complete",
        "content": "Finished a bodyweight workout focused on core strength and mobility.",
        "location": "Austin, TX"
    },
    3: {
        "title": "Building with FastAPI",
        "content": "Practicing API development and learning authentication basics.",
        "location": "San Francisco, CA"
    },
    4: {
        "title": "Weekend hike",
        "content": "Went hiking today and enjoyed some amazing views and fresh air.",
        "location": "Boulder, CO"
    },
    5: {
        "title": "Learning Python",
        "content": "Spent the afternoon improving my Python skills and writing cleaner code.",
        "location": "Seattle, WA"
    },
    6: {
        "title": "Homemade dinner",
        "content": "Tried a new recipe tonight and it turned out great.",
        "location": "Brooklyn, NY"
    },
    7: {
        "title": "Late-night coding",
        "content": "Debugging a FastAPI endpoint and learning how request validation works.",
        "location": "Chicago, IL"
    },
    8: {
        "title": "First pull-up milestone",
        "content": "Hit a personal record on pull-ups today. Small wins add up.",
        "location": "Denver, CO"
    },
    9: {
        "title": "Project planning",
        "content": "Mapping out features and thinking about how to structure the backend.",
        "location": "Remote"
    },
    10: {
        "title": "Reading about finance",
        "content": "Learning more about investing and long-term wealth strategies.",
        "location": "Boston, MA"
    },
}

@app.get("/")
def read_root(limit:int=None):
    if limit is not None:
        return {key: posts[key] for key in sorted(posts.keys())[:limit]}
    return {"message": "Welcome to Project-4"}

@app.get("/{id}")
def post_id(id:int):
    post = posts.get(id)
    if post:
        return post
    else:
        raise HTTPException (status_code=404, detail="The post is not in the database")
    
@app.post("/")
def create_post(post:Create_Post) -> Create_Post:
    new_post = {"title": post.title, "content":post.content}
    posts[max(posts.keys()) + 1] = new_post
    return new_post