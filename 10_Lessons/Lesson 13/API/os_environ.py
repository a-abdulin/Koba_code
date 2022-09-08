import os
os.environ['USER'] = 'Alice'
print(os.environ.get('USER'))

import dotenv

dotenv.load_dotenv()