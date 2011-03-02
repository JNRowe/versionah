/*
**  test.c -- Version Information for shtool_output_test (syntax: C/C++)
**  [automatically generated and maintained by GNU shtool]
*/

#ifdef _TEST_C_AS_HEADER_

#ifndef _TEST_C_
#define _TEST_C_

#define VERSION 0x102203

typedef struct {
    const int   v_hex;
    const char *v_short;
    const char *v_long;
    const char *v_tex;
    const char *v_gnu;
    const char *v_web;
    const char *v_sccs;
    const char *v_rcs;
} version_t;

extern version_t version;

#endif /* _TEST_C_ */

#else /* _TEST_C_AS_HEADER_ */

#define _TEST_C_AS_HEADER_
#include "test.c"
#undef  _TEST_C_AS_HEADER_

version_t version = {
    0x102203,
    "1.2.3",
    "1.2.3 (02-Mar-2011)",
    "This is shtool_output_test, Version 1.2.3 (02-Mar-2011)",
    "shtool_output_test 1.2.3 (02-Mar-2011)",
    "shtool_output_test/1.2.3",
    "@(#)shtool_output_test 1.2.3 (02-Mar-2011)",
    "$Id: shtool_output_test 1.2.3 (02-Mar-2011) $"
};

#endif /* _TEST_C_AS_HEADER_ */

