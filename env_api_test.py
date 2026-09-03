from dotenv import load_dotenv
import os
load_dotenv()
a=os.getenv("MY_API_KEY")
print(a) 