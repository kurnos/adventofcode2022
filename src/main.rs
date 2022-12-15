use std::fs;

mod day09;
mod day15;
mod point;

fn main() {
    println!("{}", day09::solve::<2>(fs::read_to_string("data/day09").unwrap()));
    println!("{}", day09::solve::<10>(fs::read_to_string("data/day09").unwrap()));
    println!("{:?}", day15::solve(&fs::read_to_string("data/day15").unwrap()))
}
