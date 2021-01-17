
from deepranking_get_distance import foo
import glob

model_path = './pre_trained_model/deepranking-v2-150000.h5'

foo(model_path, './img/Paris_2016-12-24_(32084381845).jpg',   './img/Paris_2016-12-24_(32084381845).jpg' )
foo(model_path, './img/Tour_Eiffel._Paris,_France.jpg',       './img/Torre_Eiffel_-_panoramio_(6).jpg' )
foo(model_path, './img/Tour_Eiffel._Paris,_France.jpg',       './img/1024px-The_Parthenon_in_Athens.jpg' )
foo(model_path, './img/Construction_tour_eiffel7.jpg',        './img/574px-Eiffel_-_panoramio_(115).jpg' )
foo(model_path, './img/Warwick_Castle_-_panoramio_(11).jpg',  './img/Warwick,_UK_-_panoramio_(37).jpg' )
foo(model_path, './img/Warwick_Castle_2015.jpg',              './img/Fundación_Joaquín_Díaz_-_Monasterio_de_Santa_María_de_Valbuena_-_San_Bernardo_(Valladolid).jpg' )
foo(model_path, './img/Warwick_Castle_(8918380584).jpg',      './img/Warwick_Castle_2015.jpg' )
foo(model_path, './img/Tour_Eiffel_(6172500991).jpg',         './img/Tour_Eiffel_vista_da_sotto.jpg' )

#for i in glob.glob('./in_et/*'):
#    for j in glob.glob('./in_images/*'):
#        foo('./deepranking-v2-150000.h5', i, j