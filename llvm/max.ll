; ModuleID = 'max'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128-Fn32"
target triple = "arm64-apple-macosx15.0.0"

define i32 @max(i32 %a, i32 %b) {
  %c = icmp sgt i32 %a, %b
  br i1 %c, label %left_bigger, label %right_bigger
left_bigger:
  ret i32 %a
right_bigger: 
  ret i32 %b
}

define i32 @main(i32  %0, ptr %1) {
  %result = call i32 @max(i32 13, i32 17)
  ret i32 %result
}

