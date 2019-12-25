from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.workIndex, name='work-index'),
    path('worksearched/', views.workSearched, name='work-searched'),
    path('findjobs/', views.workFindjobs, name='work-find-jobs'),
    path('findjobs2/', views.workFindjobs2, name='work-find-jobs2'),
    path('workjob/', views.workJob, name='work-job'),
    #path('workjob/<int:id>', views.workJob, name='work-job'),
    #path('hello/', views.hello),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    #path('task/<int:id>', views.taskView, name='work-view'),
    #path('newtask/', views.newTask, name='new-task'),
    #path('edittask/<int:id>', views.editTask, name='edit-task'),
    #path('deletetask/<int:id>', views.deleteTask, name='delete-task'),
    #path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    
    #path('fatura/', views.faturaTask, name='fatura-task'),