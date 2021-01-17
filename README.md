# test_deepranking    

Inspired by [this article](https://medium.com/@akarshzingade/image-similarity-using-deep-ranking-c1bd83855978) and corresponded [git repo](https://github.com/akarshzingade/image-similarity-deep-ranking)


download pretrained model from [here](https://drive.google.com/file/d/1TmUKqp_TnzSP0TeAHIyTv8jG4KZeNqQP/view)


# Results

| 1st image     | 2nd image     | Distance  |
| ------------- |:-------------:| ---------:|
| ![ ./img/Paris_2016-12-24_(32084381845).jpg ]( ./img/Paris_2016-12-24_(32084381845).jpg ) | ![ ./img/Paris_2016-12-24_(32084381845).jpg ]( ./img/Paris_2016-12-24_(32084381845).jpg ) |  3.465798209097083e-07  |
| ![ ./img/Tour_Eiffel._Paris,_France.jpg ]( ./img/Tour_Eiffel._Paris,_France.jpg ) | ![ ./img/Torre_Eiffel_-_panoramio_(6).jpg ]( ./img/Torre_Eiffel_-_panoramio_(6).jpg ) |  0.38605431101038307  |
| ![ ./img/Tour_Eiffel._Paris,_France.jpg ]( ./img/Tour_Eiffel._Paris,_France.jpg ) | ![ ./img/1024px-The_Parthenon_in_Athens.jpg ]( ./img/1024px-The_Parthenon_in_Athens.jpg ) |  0.4606680812915227  |
| ![ ./img/Construction_tour_eiffel7.jpg ]( ./img/Construction_tour_eiffel7.jpg ) | ![ ./img/574px-Eiffel_-_panoramio_(115).jpg ]( ./img/574px-Eiffel_-_panoramio_(115).jpg ) |  0.6114139169167636  |
| ![ ./img/Warwick_Castle_-_panoramio_(11).jpg ]( ./img/Warwick_Castle_-_panoramio_(11).jpg ) | ![ ./img/Warwick,_UK_-_panoramio_(37).jpg ]( ./img/Warwick,_UK_-_panoramio_(37).jpg ) |  0.17693616835549186  |
| ![ ./img/Warwick_Castle_2015.jpg ]( ./img/Warwick_Castle_2015.jpg ) | ![ ./img/Fundación_Joaquín_Díaz_-_Monasterio_de_Santa_María_de_Valbuena_-_San_Bernardo_(Valladolid).jpg ]( ./img/Fundación_Joaquín_Díaz_-_Monasterio_de_Santa_María_de_Valbuena_-_San_Bernardo_(Valladolid).jpg ) |  0.668336033047218  |
| ![ ./img/Warwick_Castle_(8918380584).jpg ]( ./img/Warwick_Castle_(8918380584).jpg ) | ![ ./img/Warwick_Castle_2015.jpg ]( ./img/Warwick_Castle_2015.jpg ) |  0.8292099605550132  |
| ![ ./img/Tour_Eiffel_(6172500991).jpg ]( ./img/Tour_Eiffel_(6172500991).jpg ) | ![ ./img/Tour_Eiffel_vista_da_sotto.jpg ]( ./img/Tour_Eiffel_vista_da_sotto.jpg ) |  0.37081080262926935  |


Unfortunately distance Eiffel tower to form Parthenon less than one view of Eiffel tower to another.  
