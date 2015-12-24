from child import Child
from uuid import uuid4

child = Child(str(uuid4()),"http://localhost:8000")
child.start()