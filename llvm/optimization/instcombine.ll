define i32 @double(i32 %in) {
    %result = mul i32 %in, 2
    ret i32 %result
}

define i32 @computation(i32 %n) {
    ; a := n + 5
    %x = add i32 %n, 5
    %a = alloca i32
    store i32 %x, ptr %a
    ; b := a - 3
    %b = alloca i32
    %y = load i32, ptr %a
    %z = sub i32 %y, 3
    store i32 %z, ptr %b
    ; return b;
    %result = load i32, ptr %b
    ret i32 %result
}

define double @half(double %n) {
    %result = fdiv double %n, 2.0
    ret double %result
}
