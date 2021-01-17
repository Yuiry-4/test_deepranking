
from deepranking_get_distance import foo
import glob

model_path = './pre_trained_model/deepranking-v2-150000.h5'

foo(model_path, './in_et/Paris_2016-12-24_(32084381845).jpg', './in_et/Paris_2016-12-24_(32084381845).jpg' )
foo(model_path, './in_et/Tour_Eiffel._Paris,_France.jpg', './in_et/Torre_Eiffel_-_panoramio_(6).jpg' )
foo(model_path, './in_et/Tour_Eiffel._Paris,_France.jpg', './in_images_2/1024px-The_Parthenon_in_Athens.jpg' )
foo(model_path, './in_images/Construction_tour_eiffel7.jpg', './in_images/574px-Eiffel_-_panoramio_(115).jpg' )
foo(model_path, './in_wc/Warwick_Castle_-_panoramio_(11).jpg', './in_wc/Warwick,_UK_-_panoramio_(37).jpg' )
foo(model_path, './in_wc/Warwick_Castle_2015.jpg', './in_images_2/Fundación_Joaquín_Díaz_-_Monasterio_de_Santa_María_de_Valbuena_-_San_Bernardo_(Valladolid).jpg' )
foo(model_path, './in_wc/Warwick_Castle_(8918380584).jpg', './in_wc/Warwick_Castle_2015.jpg' )
foo(model_path, './in_et/Tour_Eiffel_(6172500991).jpg', './in_et/Tour_Eiffel_vista_da_sotto.jpg' )

#for i in glob.glob('./in_et/*'):
#    for j in glob.glob('./in_images/*'):
#        foo('./deepranking-v2-150000.h5', i, j)