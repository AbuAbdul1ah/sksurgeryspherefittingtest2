# coding=utf-8

"""scikit-surgery-sphere-fitting tests"""

from sksurgeryspherefittingtest2.ui.sksurgeryspherefittingtest2_demo import run_demo # pylint: disable=line-too-long

def test_fit_sphere_least_sqs_demo():
    """
    test the run demo entry point
    """
    model_name = 'data/CT_Level_1.vtp'
    output_name = 'out_temp.vtp'

    run_demo(model_name, output_name)