from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CustomLoginView,LogoutView,registerPage, registerPage

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name='login'),
    path('register/',registerPage.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('createtask/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',DeleteView.as_view(),name='task-delete'),
] 
