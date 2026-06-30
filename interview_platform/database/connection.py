from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# MongoDB Connection URL
MONGO_URI = "mongodb://localhost:27017/"

# Database Name
DATABASE_NAME = "ai_interview_platform"

try:
    # Create MongoDB Client
    client = MongoClient(MONGO_URI)

    # Check Connection
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully")

    # Select Database
    db = client[DATABASE_NAME]

except ConnectionFailure:
    print("❌ MongoDB Connection Failed")


# ==============================
# Collections
# ==============================

users_collection = db["users"]

interview_collection = db["interviews"]

resume_collection = db["resumes"]

quiz_collection = db["quizzes"]

result_collection = db["results"]

coding_collection = db["coding_tests"]

history_collection = db["history"]

notification_collection = db["notifications"]