from rest_framework import routers
from voltages.api.views import (
    DataViewSet, DataTestViewSet, DataViewSingleUser, DataViewSingleActivity)


router = routers.DefaultRouter()
router.register(r'^all-data', DataViewSet, base_name='alldata')
router.register(r'^test-data', DataTestViewSet, base_name='testingdata')
router.register(
    r'^current-user', DataViewSingleUser, base_name='singledata')
router.register(r'activities', DataViewSingleActivity,
                base_name='singleactivity')
urlpatterns = router.urls
