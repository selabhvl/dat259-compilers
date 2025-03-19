; ModuleID = 'factorial'
source_filename = "factorial"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

@prompt = constant [9 x i8] c"Inputt: \00"
@msg = constant [23 x i8] c"Fakultet av %d er: %d\0A\00"
@format = constant [3 x i8] c"%d\00"

declare i32 @printf(ptr, ...) 
declare i32 @scanf(ptr, ...) 

define i32 @factorial(i32 %n) {
entry:
  %cond = icmp eq i32 %n, 0
  br i1 %cond, label %base, label %recursive
base:
  ret i32 1
recursive:
  %prev_n = sub i32 %n, 1
  %prev_res = call i32  @factorial(i32 %prev_n)
  %result = mul i32 %n, %prev_res
  ret i32 %result

}
define i32 @main(i32 %argc, ptr %argv) {
entry:
  call i32 (ptr, ...) @printf(ptr @prompt)
  %local_var = alloca i32
  call i32 (ptr, ...) @scanf(ptr @format, ptr %local_var)
  %input = load i32, ptr %local_var
  %result = call i32 @factorial(i32 %input)
  call i32 (ptr, ...) @printf(ptr @msg, i32 %input, i32 %result)
  ret i32 %result
}
