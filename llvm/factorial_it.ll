; ModuleID = 'factorial'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

@prompt = constant [9 x i8] c"Inputt: \00"
@msg = constant [23 x i8] c"Fakultet av %d er: %d\0A\00"
@format = constant [3 x i8] c"%d\00"

declare i32 @printf(ptr, ...) 
declare i32 @scanf(ptr, ...) 

define i32 @factorial(i32 %n) {
entry:
  %result = alloca i32
  %i = alloca i32
  store i32 1, ptr %result 
  store i32 1, ptr %i
  %too_smll =  icmp slt i32 %n, 2
  br i1 %too_smll, label %fin, label %check
check:
  %current = load i32, ptr %i
  %cond = icmp sgt i32 %current, %n
  br i1 %cond, label %fin, label %body
body:
  %current_i = load i32, ptr %i
  %current_res = load i32, ptr %result 
  %next_i = add i32 %current_i, 1
  %next_res = mul i32 %current_res, %current_i
  store i32 %next_i, ptr %i
  store i32 %next_res, ptr %result
  br label %check
fin:
  %result_val = load i32, ptr %result
  ret i32 %result_val
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
