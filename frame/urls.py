from django.urls import path
from  rest_framework.routers import DefaultRouter
from .views import PollViewSet,ChoiceList,CreateVote,UserCreate,LoginView
router=DefaultRouter()
router.register('polls',PollViewSet,basename='polls')

urlpatterns=[
    path("users/", UserCreate.as_view(), name="user_create"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    #path("login/", views.obtain_auth_token, name="login"),
    path("login/", LoginView.as_view(), name="login"),
#
]
urlpatterns +=router.urls

#"token": "0bd6881a76ff4fb9a1851e90fe0260c433a7c1f5"
    #"token": "0bd6881a76ff4fb9a1851e90fe0260c433a7c1f5"