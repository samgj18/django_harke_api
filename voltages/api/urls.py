from rest_framework import routers
from voltages.api.views import (
    DataViewSet, DataTestViewSet, DataViewSingleUser)


router = routers.DefaultRouter()
router.register(r'^all-data', DataViewSet)
router.register(r'^test-data', DataTestViewSet, base_name='testingdata')
router.register(r'^current-user', DataViewSingleUser, base_name='singledata')
urlpatterns = router.urls
