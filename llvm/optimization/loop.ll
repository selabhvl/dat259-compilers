define void @fun(i32 %y, i32 %z, i32 %n, ptr %a) {
entry:
  %y.addr = alloca i32
  %z.addr = alloca i32
  %n.addr = alloca i32
  %a.addr = alloca ptr
  %x = alloca i32
  %i = alloca i32
  store i32 %y, ptr %y.addr
  store i32 %z, ptr %z.addr
  store i32 %n, ptr %n.addr
  store ptr %a, ptr %a.addr
  store i32 0, ptr %i
  br label %while.cond

while.cond:
  %0 = load i32, ptr %i
  %1 = load i32, ptr %n.addr
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %while.body, label %while.end

while.body:
  %2 = load i32, ptr %y.addr
  %3 = load i32, ptr %z.addr
  %add = add nsw i32 %2, %3
  store i32 %add, ptr %x
  %4 = load i32, ptr %i
  %mul = mul nsw i32 6, %4
  %5 = load i32, ptr %x
  %6 = load i32, ptr %x
  %mul1 = mul nsw i32 %5, %6
  %add2 = add nsw i32 %mul, %mul1
  %7 = load ptr, ptr %a.addr
  %8 = load i32, ptr %i
  %idxprom = sext i32 %8 to i64
  %arrayidx = getelementptr i32, ptr %7, i64 %idxprom
  store i32 %add2, ptr %arrayidx
  %9 = load i32, ptr %i
  %inc = add nsw i32 %9, 1
  store i32 %inc, ptr %i
  br label %while.cond

while.end:
  ret void
}

