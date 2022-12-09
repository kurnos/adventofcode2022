use std::{collections::HashSet, iter};

use crate::point::Point2;

type P = Point2<i32>;

fn advance_head(head: P, dir: char) -> P {
    match dir {
        'U' => head + Point2(0, -1),
        'D' => head + Point2(0, 1),
        'L' => head + Point2(-1, 0),
        'R' => head + Point2(1, 0),
        _ => panic!(),
    }
}

fn advance_tail(head: P, tail: P) -> P {
    let d = tail - head;
    match (d.0.abs(), d.1.abs()) {
        (0, 2) | (2, 0) | (2, 2) => tail - d / 2,
        (2, 1) => Point2(tail.0 - d.0 / 2, tail.1 - d.1),
        (1, 2) => Point2(tail.0 - d.0, tail.1 - d.1 / 2),
        _ => tail,
    }
}

pub fn solve<const N: usize>(s: String) -> usize {
    s.lines()
        .map(|line| {
            (
                line.chars().next().unwrap(),
                line[2..].parse::<usize>().unwrap(),
            )
        })
        .flat_map(|(dir, count)| iter::repeat(dir).take(count))
        .scan([Point2(0, 0); N], |rope, d| {
            rope[0] = advance_head(rope[0], d);
            for i in 1usize..N {
                rope[i] = advance_tail(rope[i - 1], rope[i])
            }
            Some(rope[N - 1])
        })
        .collect::<HashSet<_>>()
        .len()
}
