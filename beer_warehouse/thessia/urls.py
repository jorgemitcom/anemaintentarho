from django.conf.urls import url
from thessia.views import first_view, thessia_list_view, thessia_detail_view, all_thessia_list_view, thessia_interactive_game_view, thessia_first_test_view, thessia_second_test_view, thessia_third_test_view


urlpatterns = [
    url(r'^$', first_view, name='first-view'),
    url(r'^list/$', thessia_list_view, name='thessia-list-view'),
    url(r'^cuentos/$', all_thessia_list_view, name='all-thessia-list-view'),
    url(r'^juego/$', thessia_interactive_game_view, name='thessia-interactive-game-view'),
    url(r'^pruebaUno/$', thessia_first_test_view, name='thessia-first-test-view'),
    url(r'^pruebaDos/$', thessia_second_test_view, name='thessia-second-test-view'),
    url(r'^pruebaTres/$', thessia_third_test_view, name='thessia-third-test-view'),
    url(r'^detail/(?P<id>\d+)/$', thessia_detail_view, name='thessia-detail-view'),
]