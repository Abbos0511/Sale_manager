from app.views import *
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'qiuck_panel', QuickPanelView, basename='quick_panel')
