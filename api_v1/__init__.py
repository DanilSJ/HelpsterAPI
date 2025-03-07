from fastapi import APIRouter

from .users.views import router as users_router
from .blogs.views import router as blogs_router
from .articles.views import router as articles_router

router = APIRouter()
router.include_router(router=users_router, prefix="/users")
router.include_router(router=blogs_router, prefix="/blogs")
router.include_router(router=articles_router, prefix="/articles")
