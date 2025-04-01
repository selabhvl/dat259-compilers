define i32 @max(i32 %l, i32 %r) {
entry:
  %cmp = icmp sgt i32 %l, %r
  %result = select i1 %cmp, i32 %l, i32 %r
  ret i32 %result
}

define i32 @max3(i32 %a, i32 %b, i32 %c) {
entry:
  %first = call i32 @max(i32 %a, i32 %b)
  %second = call i32 @max(i32 %first, i32 %c)
  ret i32 %second
}


define i32 @main(i32 %argc, ptr %argv) {
entry:
  %call = call i32 @max3(i32 23, i32 42, i32 69)
  ret i32 %call
}

