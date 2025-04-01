
; ModuleID = 'strings'
source_filename = "strings"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

@msg = constant [27 x i8] c"Value at '%d' (%p) is: %d\0A\00" 

; taken from libc
declare i32 @printf(ptr, ...)
declare ptr @malloc(i64)
declare void @free(ptr)
declare ptr @memcpy(ptr, ptr, i64)




define i32 @main(i32 %argc, ptr %argv) {
  %mem = call ptr (i64) @malloc(i64 4)

  %idx1 = getelementptr i8, ptr %mem, i64 0
  %idx2 = getelementptr i8, ptr %mem, i64 1
  %idx3 = getelementptr i8, ptr %mem, i64 2
  %idx4 = getelementptr i8, ptr %mem, i64 4

  store i8 42, ptr %idx1
  store i8 23, ptr %idx2
  store i8 69, ptr %idx3
  store i8 1, ptr %idx4

  %val1 = load i8, ptr %idx1
  %val2 = load i8, ptr %idx2
  %val3 = load i8, ptr %idx3
  %val4 = load i8, ptr %idx4

  call i32 (ptr, ...) @printf(ptr @msg, i64 0, ptr %idx1, i8 %val1)
  call i32 (ptr, ...) @printf(ptr @msg, i64 1, ptr %idx2, i8 %val2)
  call i32 (ptr, ...) @printf(ptr @msg, i64 2, ptr %idx3, i8 %val3)
  call i32 (ptr, ...) @printf(ptr @msg, i64 3, ptr %idx4, i8 %val4)

  call void (ptr) @free(ptr %mem)
  ret i32 0
}
