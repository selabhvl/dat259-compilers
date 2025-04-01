; ModuleID = 'sums'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

declare i32 @rand()
declare i32 @printf(ptr, ...)
declare void @srand(i32)
declare i64 @time(ptr)

@.str = constant [40 x i8] c"Sum of 100,000 random variables: %.2lf\0A\00", align 1

define dso_local i32 @main() {
entry:
  %sum = alloca double, align 8
  %i = alloca i64, align 8
  %random_value = alloca i32, align 4
  %x = alloca i32, align 4
  store i64 0, ptr %sum, align 8
  store i64 0, ptr %i, align 4
  %call = call i64 @time(ptr null)
  %conv = trunc i64 %call to i32
  call void @srand(i32 %conv)
  br label %for.cond

for.cond:
  %0 = load i64, ptr %i, align 8
  %cmp = icmp slt i64 %0, 10000000
  br i1 %cmp, label %for.body, label %for.end

for.body:
  %call2 = call i32 @rand()
  store i32 %call2, ptr %random_value, align 4
  %1 = load i32, ptr %random_value, align 4
  %rem = srem i32 %1, 100
  store i32 %rem, ptr %x, align 4
  %2 = load i32, ptr %x, align 4
  %conv3 = sitofp i32 %2 to double
  %div = fdiv double %conv3, 1.000000e+02
  %3 = load double, ptr %sum, align 8
  %add = fadd double %3, %div
  store double %add, ptr %sum, align 8
  br label %for.inc

for.inc:
  %4 = load i64, ptr %i, align 8
  %inc = add nsw i64 %4, 1
  store i64 %inc, ptr %i, align 8
  br label %for.cond

for.end:
  %5 = load i64, ptr %sum, align 8
  %call1 = call i32 (ptr, ...) @printf(ptr @.str, i64 %5)
  ret i32 0
}
