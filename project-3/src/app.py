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
    11: {
        "title": "API testing",
        "content": "Using Postman to test endpoints and understand request flows.",
        "location": "Raleigh, NC"
    },
    12: {
        "title": "Calisthenics progress",
        "content": "Noticing better control and strength after staying consistent.",
        "location": "San Diego, CA"
    },
    13: {
        "title": "Refactoring code",
        "content": "Cleaned up some endpoints and improved readability.",
        "location": "Portland, OR"
    },
    14: {
        "title": "Weekend reflection",
        "content": "Taking time to review goals and plan the next week.",
        "location": "Nashville, TN"
    },
    15: {
        "title": "Learning authentication",
        "content": "Exploring JWTs and password hashing in FastAPI.",
        "location": "Remote"
    },
    16: {
        "title": "Side project update",
        "content": "Made steady progress on a small backend project today.",
        "location": "Los Angeles, CA"
    },
    17: {
        "title": "Debugging session",
        "content": "Tracked down a tricky bug related to request validation.",
        "location": "Phoenix, AZ"
    },
    18: {
        "title": "Staying consistent",
        "content": "Showing up every day, even when progress feels slow.",
        "location": "Columbus, OH"
    },
    19: {
        "title": "API documentation",
        "content": "Writing clear docs to make endpoints easier to understand.",
        "location": "Madison, WI"
    },
    20: {
        "title": "Wrapping up the day",
        "content": "Reviewed what I learned and planned tasks for tomorrow.",
        "location": "Remote"
    }
}

@app.get("/")
def read_root():
    return {"message" : "Welcome to Project-3"}

@app.get("/post/{id}")
def get_post(id:int):
    post = posts.get(id)
    if post:
        return post
    else:
        return {"message":"That is not in the database"}