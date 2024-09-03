from django.urls import path
from .views import index , detailed_task , todo_by_status ,Todo_list_Category,Createtodo , createCategory ,update_task ,delete_task
from . import views


urlpatterns = [
    path('',index , name="home"),

    
    path('todos/status/<str:st>' , todo_by_status , name ="status"),
    path('tasks/<str:status>/', views.tasks_by_status, name='tasks_by_status'),
    path('tasks/category/<int:category_id>/', views.tasks_by_category, name='tasks_by_category'),

    path('detailed/<int:id>' , detailed_task , name ="detail"),
    path('todo/delete/<int:id>' , delete_task , name ="delete-task"),
    path('todo/update/<int:id>' , update_task , name ="update-task"),
    
    path('todo/category/<int:id>' , Todo_list_Category , name="cattodo" ),

    path('todo/create' , Createtodo , name="createtodo"),
    path('todo/create', Createtodo, name="createtodo"),
     path('todo/update/<int:task_id>/', Createtodo, name="updatetodo"),

    path('categopry/create' , createCategory , name='createcategory' ),

    
   
    
    path('register/', views.register_user, name='register'),    

    

    
 ]