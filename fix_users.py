import os
import argilla as rg
from dotenv import load_dotenv
load_dotenv()
rg.init(api_url=os.getenv("ARGILLA_URL"), api_key="argilla.apikey", workspace="argilla")

# create new workspace
rg.Workspace.create("sml")

# create new user
user = rg.User.create(
    username=os.getenv("OWNER_USERNAME"),
    first_name="Argilla",
    last_name="Admin",
    password=os.getenv("OWNER_PASSWORD"),
    role="owner",
    workspaces=["sml"]
)

# remove default user
default_user = rg.User.from_name("argilla")
default_user.delete()



