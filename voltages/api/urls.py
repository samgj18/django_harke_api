from rest_framework import routers
from voltages.api.views import (
    DataViewSet, DataTestViewSet, DataViewSingleUser, DataVerifyTestViewSet)


router = routers.DefaultRouter()
router.register(r'^all-data', DataViewSet, base_name='alldata')
router.register(r'^train-data', DataTestViewSet, base_name='traindata')
router.register(
    r'^current-user', DataViewSingleUser, base_name='singledata')
router.register(
    r'^test-data', DataVerifyTestViewSet, base_name='testdata')

urlpatterns = router.urls
