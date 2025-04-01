; ModuleID = 'vector'
source_filename = "vector"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

@msg = constant [21 x i8] c"Last Element is: %d\0A\00" 
@stat_msg = constant [24 x i8] c"Size: %d, Capacity: %d\0A\00"
%Vector = type {
  ptr, ; 0 = memory pointer
  i64, ; 1 = size
  i64  ; 2 = capacity
}
@my_vec = global %Vector zeroinitializer

; taken from libc
declare i32 @printf(ptr, ...)
declare ptr @malloc(i64)
declare void @free(ptr)
declare ptr @memcpy(ptr, ptr, i64)


define void @init(ptr %vec) {
  %field.ptr = getelementptr %Vector, ptr %vec, i64 0
  %field.size = getelementptr %Vector, ptr %vec, i64 1
  %field.capacity = getelementptr %Vector, ptr %vec, i64 2
  store i64 0, ptr %field.size
  store i64 2, ptr %field.capacity
  %addr = call ptr (i64) @malloc(i64 2)
  store ptr %addr, ptr %field.ptr
  ret void
}

define void @add(ptr %vec, i8 %elem) {
  %field.ptr = getelementptr %Vector, ptr %vec, i64 0
  %field.size = getelementptr %Vector, ptr %vec, i64 1
  %field.capacity = getelementptr %Vector, ptr %vec, i64 2
  %size = load i64, ptr %field.size
  %capacity = load i64, ptr %field.capacity
  %is_space = icmp ult i64 %size, %capacity
  br i1 %is_space, label %not_full, label %full
not_full:
  %ptr = load ptr, ptr %field.ptr
  %slot = getelementptr i8, ptr %ptr, i64 %size
  store i8 %elem, ptr %slot
  %new_size = add i64 %size, 1
  store i64 %new_size, ptr %field.size
  ret void
full:
  %old_ptr = load ptr, ptr %field.ptr
  %new_cap = mul i64 %capacity, 2
  %new_ptr = call ptr (i64) @malloc(i64 %new_cap)
  call ptr (ptr, ptr, i64) @memcpy(ptr %new_ptr, ptr %old_ptr, i64 %capacity)
  store i64 %new_cap, ptr %field.capacity
  store ptr %new_ptr, ptr %field.ptr
  call void (ptr) @free(ptr %old_ptr)
  br label %not_full
}

define i8 @last(ptr %vec) {
  %field.ptr = getelementptr %Vector, ptr %vec, i64 0
  %field.size = getelementptr %Vector, ptr %vec, i64 1
  %size = load i64, ptr %field.size
  %last_idx = sub i64 %size, 1
  %ptr = load ptr, ptr %field.ptr
  %slot = getelementptr i8, ptr %ptr, i64 %last_idx
  %result = load i8, ptr %slot
  ret i8 %result
}

define void @stats(ptr %vec) {
  %field.size = getelementptr %Vector, ptr %vec, i64 1
  %field.cap = getelementptr %Vector, ptr %vec, i64 2
  %cap = load i64, ptr %field.cap
  %size = load i64, ptr %field.size
  call i32 (ptr, ...) @printf(ptr @stat_msg, i64 %size, i64 %cap)
  ret void
}

define void @deinit(ptr %vec) {
  %field.ptr = getelementptr %Vector, ptr %vec, i64 0
  %ptr = load ptr, ptr %field.ptr
  call void @free(ptr %ptr)
  ret void
}


define i32 @main(i32 %argc, ptr %argv) {
  call void (ptr) @init(ptr @my_vec)
  call void (ptr, i8) @add(ptr @my_vec, i8 23)
  call void (ptr, i8) @add(ptr @my_vec, i8 42)
  call void (ptr, i8) @add(ptr @my_vec, i8 69)
  call void (ptr, i8) @add(ptr @my_vec, i8 69)
  call void (ptr, i8) @add(ptr @my_vec, i8 1)
  %last = call i8 (ptr) @last(ptr @my_vec)
  call i32 (ptr, ...) @printf(ptr @msg, i8 %last)
  call void (ptr) @stats(ptr @my_vec)
  call void @deinit(ptr @my_vec)
  ret i32 0
}
