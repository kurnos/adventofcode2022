use std::fs;

mod day09;
mod point;

fn main() {
    println!("{}", day09::solve::<2>(fs::read_to_string("data/day09").unwrap()));
    println!("{}", day09::solve::<10>(fs::read_to_string("data/day09").unwrap()));
}
