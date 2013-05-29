from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^hide_site_selection.css$', views.hide_site_selection_css, name='hide_site_selection_css'),
)