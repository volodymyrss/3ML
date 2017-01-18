import collections


from threeML.plugins.FermiGBMTTELike import FermiGBMTTELike
from astromodels.core.parameter import Parameter

from gbm_drm_gen import DRMGenTTE








class BALROGLike(FermiGBMTTELike):

    def __init__(self,name, tte_file, trigdata_file, cspec_file, background_selections, source_intervals, trigger_time=None,
                 poly_order=-1, matrix_type=2, unbinned=True, verbose=True):



                 # Here we create a DRMGenerator object for this GRB. We must extract the detector name
                 # from the input TTE file to feed to the generator

                 super(BALROGLike, self).__init__(name,
                                                  tte_file,
                                                  background_selections,
                                                  source_intervals,
                                                 # rsp_file,
                                                  trigger_time,
                                                  poly_order,
                                                  unbinned,
                                                  verbose)


                 # now we add on the nuisance parameters by updating from the original correction
                 # factor and adding ra, dec into the mix.

                 self._location_ra = Parameter("ra" % name, 1.0, min_value=0, max_value=360, delta=0.05,
                                                      free=True, desc="right accession for  %s" % name)

                 self._location_dec = Parameter("dec" % name, 1.0, min_value=0, max_value=360, delta=0.05,
                                               free=True, desc="declination for  %s" % name)

                 nuisance_parameters = collections.OrderedDict()

                 nuisance_parameters[self._nuisance_parameter.name] = self._nuisance_parameter
                 nuisance_parameters[self._location_dec.name] = self._location_dec
                 nuisance_parameters[self._location_ra.name] = self._location_ra

                 self.update_nuisance_parameters(nuisance_parameters)

    def get_folded_model(self):


        # Here we update the GBM drm parameters which creates and new DRM for that location



        super(BALROGLike, self).get_folded_model()