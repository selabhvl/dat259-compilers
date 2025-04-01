; ModuleID = 'to_opt.c'
source_filename = "to_opt.c"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128-Fn32"
target triple = "arm64-apple-macosx15.0.0"

@.str = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

define void @foo() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 42, ptr %1, align 4
  %3 = load i32, ptr %1, align 4
  %4 = mul nsw i32 2, %3
  store i32 %4, ptr %2, align 4
  %5 = load i32, ptr %2, align 4
  %6 = call i32 (ptr, ...) @printf(ptr noundef @.str, i32 noundef %5)
  ret void
}

declare i32 @printf(ptr , ...) #1

define i32 @main()  {
  %1 = alloca i32, align 4
  store i32 0, ptr %1, align 4
  call void @foo()
  ret i32 0
}


