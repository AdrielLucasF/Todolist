from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet, TagViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)
router.register(r'tags', TagViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = router.urls
