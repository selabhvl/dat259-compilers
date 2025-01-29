```
pb get foobar () =
  case (get "www.helloworld.no/") of
    response@{ status: 200, body } => response
    _ => { status: 404 }
 
fib (/?n: number) =
  case n of
    1 => 1
    2 => 1
    _ => fib (n - 1) + fib (n - 2)
 
map (/?f: a -> b) =
  map' /?xs: [a] =
    case xs of
      [] => []
      [y, ...ys] => f y : map f ys
```
