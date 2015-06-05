
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


        struct foo_s { struct { int a; short b; }; union { char c, d; }; };
    
static void _cffi_check_struct_foo_s(struct foo_s *p)
{
  /* only to generate compile-time warnings or errors */
  (void)((p->a) << 1);
  { char *tmp = &p->b; (void)tmp; }
  { char *tmp = &p->c; (void)tmp; }
  { char *tmp = &p->d; (void)tmp; }
}
ssize_t _cffi_layout_struct_foo_s(ssize_t i)
{
  struct _cffi_aligncheck { char x; struct foo_s y; };
  static ssize_t nums[] = {
    sizeof(struct foo_s),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct foo_s, a),
    sizeof(((struct foo_s *)0)->a),
    offsetof(struct foo_s, b),
    sizeof(((struct foo_s *)0)->b),
    offsetof(struct foo_s, c),
    sizeof(((struct foo_s *)0)->c),
    offsetof(struct foo_s, d),
    sizeof(((struct foo_s *)0)->d),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_foo_s(0);
}

