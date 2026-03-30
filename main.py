from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
import os
load_dotenv()

db = SQLDatabase.from_uri(os.getenv("POSTGRES_CONN_STRING"))

print(f"Dialect ?? is: {db.dialect}")
print(f"The results of a run is: {db.run("SELECT * FROM users;")}")
