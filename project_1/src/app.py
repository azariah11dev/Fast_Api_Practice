from fastapi import FastAPI

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
    }
}

@app.get("/")
def read_root():
    return {"message" : "Hello World"}

@app.get("/post/{id}")
def get_post(id:int):
    post = posts.get(id)
    if post:
        return post
    else:
        return {"error" : "post not found"}