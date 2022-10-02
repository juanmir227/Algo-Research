import os
from dotenv import load_dotenv

load_dotenv()
print(type(os.environ["PURESTAKE_API"]))
# usuario = env.prefix('path')
# usuario