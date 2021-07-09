from .users import router as user_routers 
from .courses import router as course_routers 


routers = [
    user_routers,
    course_routers,
]