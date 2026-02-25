# 变量
## 声明

`let` 声明变量
```rust
let i = 0;
```
`i`变量名 `0`值

```rust
let mut i = 0;
```
`i`变量名 `0`值 `mut`可改变

`let`默认声明的变量可以看成常理
`let`和变量名中间添加一个`mnt`让这个变量可以修改

## 类型
```rust
let a = 10       //i32 整数
let b = 3.14     //f64 浮点数
let c = true     //bool 布尔值
let d = "hello"  //&std 字符串切片
```

### 常见类型

- 整数: i32 i64 u32 usize
- 浮点数: f32 f64
- 布尔值: bool
- 字符: char
- 字符串切片: &str
- 字符串: String

### rust特性
同一个名称，可以重复使用`let`声明
```rust
let x = 5;
let x = x + 1;
let x = x / 2;
let x = "hello";
```

```rust
let a = 0
let mut a = "std"
let mut b = 0
let b = "str"
```


```rust
let mut a = 8;
s = "str";       //错误 这重类型已经固定好的了，不能修改类型
```

```rust
let mut a = 8;
let mut a = "str";   //完全可以
```

### 常量
`const` 必须写类型 不能使用`mut` 不能修改，只能调用
```rust
const ABC:u32 = 10;
```

错误实例
```rust
const mut A = 10       //不能使用mut, 没有添加类型
const mut B:u32 = 10   //不能使用mut
const C = 10           //没有添加类型
const D:&str = 10      //类型不匹配
const E:u32 = 10       //正确
const E:u32 = 60       //不能重复声明同一个名称
```
