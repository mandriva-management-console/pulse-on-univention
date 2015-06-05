
#include <stdio.h>
#include <stddef.h>
#include <stdarg.h>
#include <errno.h>
#include <sys/types.h>   /* XXX for ssize_t on some platforms */

#ifdef _WIN32
#  include <Windows.h>
#  define snprintf _snprintf
typedef __int8 int8_t;
typedef __int16 int16_t;
typedef __int32 int32_t;
typedef __int64 int64_t;
typedef unsigned __int8 uint8_t;
typedef unsigned __int16 uint16_t;
typedef unsigned __int32 uint32_t;
typedef unsigned __int64 uint64_t;
typedef SSIZE_T ssize_t;
typedef unsigned char _Bool;
#else
#  include <stdint.h>
#endif

enum ee { EE1, EE2 };
int _cffi_e_enum_ee(char *out_error)
{
  if (EE1 != 0) {
    snprintf(out_error, 255,"%s has the real value %d, not %d",
            "EE1", (int)EE1, 0);
    return -1;
  }
  if (EE2 != 1) {
    snprintf(out_error, 255,"%s has the real value %d, not %d",
            "EE2", (int)EE2, 1);
    return -1;
  }
  if (EE3 != 2) {
    snprintf(out_error, 255,"%s has the real value %d, not %d",
            "EE3", (int)EE3, 2);
    return -1;
  }
  return 0;
}

