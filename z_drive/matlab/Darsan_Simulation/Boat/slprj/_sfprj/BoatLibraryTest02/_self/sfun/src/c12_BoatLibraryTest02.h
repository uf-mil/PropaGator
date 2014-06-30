#ifndef __c12_BoatLibraryTest02_h__
#define __c12_BoatLibraryTest02_h__

/* Include files */
#include "sfc_sf.h"
#include "sfc_mex.h"
#include "rtwtypes.h"
#include "multiword_types.h"

/* Type Definitions */
#ifndef typedef_SFc12_BoatLibraryTest02InstanceStruct
#define typedef_SFc12_BoatLibraryTest02InstanceStruct

typedef struct {
  SimStruct *S;
  ChartInfoStruct chartInfo;
  uint32_T chartNumber;
  uint32_T instanceNumber;
  int32_T c12_sfEvent;
  boolean_T c12_isStable;
  boolean_T c12_doneDoubleBufferReInit;
  uint8_T c12_is_active_c12_BoatLibraryTest02;
} SFc12_BoatLibraryTest02InstanceStruct;

#endif                                 /*typedef_SFc12_BoatLibraryTest02InstanceStruct*/

/* Named Constants */

/* Variable Declarations */

/* Variable Definitions */

/* Function Declarations */
extern const mxArray *sf_c12_BoatLibraryTest02_get_eml_resolved_functions_info
  (void);

/* Function Definitions */
extern void sf_c12_BoatLibraryTest02_get_check_sum(mxArray *plhs[]);
extern void c12_BoatLibraryTest02_method_dispatcher(SimStruct *S, int_T method,
  void *data);

#endif
