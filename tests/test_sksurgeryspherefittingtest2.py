# coding=utf-8

"""scikit-surgery-sphere-fitting-test2 tests"""

import numpy
from sksurgeryspherefittingtest2.algorithms import sphere_fitting # pylint: disable=line-too-long

def test_fit_sphere_least_squares():
    """
    test_fit_sphere_least_square
    """
    x_centre = 1.0
    y_centre = 167.0
    z_centre = 200.0

    radius = 7.5

    #some arrays to fit data to
    x_values=numpy.ndarray(shape=(1000,),dtype=float )
    y_values=numpy.ndarray(shape=(1000,),dtype=float )
    z_values=numpy.ndarray(shape=(1000,),dtype=float )

    #fill the arrays with points uniformly spread on
    #a sphere centred at x,y,z with radius radius
    for i in range(1000):
        #make a random vector
        x_var=numpy.random.uniform(-1.0, 1.0)
        y_var=numpy.random.uniform(-1.0, 1.0)
        z_var=numpy.random.uniform(-1.0, 1.0)

        #scale it to length radius
        length=numpy.sqrt( (x_var)**2 + (y_var)**2 + (z_var)**2 )
        factor = radius / length

        x_values[i] = x_var*factor + x_centre
        y_values[i] = y_var*factor + y_centre
        z_values[i] = z_var*factor + z_centre

    parameters = [0.0, 0.0, 0.0, 0.0]
    result = sphere_fitting.fit_sphere_least_squares (x_values,
                                                        y_values,
                                                        z_values,
                                                        parameters)

    numpy.testing.assert_approx_equal(result[0][0], x_centre, significant=10)
