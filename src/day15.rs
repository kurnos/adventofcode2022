use crate::point::Point2;
use std::collections;

#[derive(Debug, Copy, Clone)]
struct Reading {
    center: Point2<i32>,
    radius: i32,
    diamond: Diamond,
}

#[derive(Debug, Copy, Clone)]
struct Diamond {
    a: [i32; 2],
    s: [i32; 2],
}

fn parse(line: &str) -> Option<Reading> {
    let (_, line) = line.split_at(12);
    let (x, line) = line.split_once(',')?;
    let (_, line) = line.split_at(3);
    let (y, line) = line.split_once(':')?;
    let (_, line) = line.split_at(24);
    let (bx, line) = line.split_once(',')?;
    let (_, by) = line.split_at(3);
    let c = Point2(x.parse().ok()?, y.parse().ok()?);
    let r = manhattan(c - Point2(bx.parse().ok()?, by.parse().ok()?));
    return Some(Reading {
        center: c,
        radius: r,
        diamond: Diamond {
            a: [c.1 + c.0 - r, c.1 + c.0 + r + 1],
            s: [c.1 - c.0 - r, c.1 - c.0 + r + 1],
        },
    });
}

fn manhattan(p: Point2<i32>) -> i32 {
    return p.0.abs() + p.1.abs();
}

impl Diamond {
    fn includes(self, rhs: Diamond) -> bool {
        self.a[0] <= rhs.a[0]
            && self.a[1] >= rhs.a[1]
            && self.s[0] <= rhs.s[0]
            && self.s[1] >= rhs.s[1]
    }
}

pub fn solve(data: &str) -> Option<(i32, i64)> {
    let readings = data.split('\n').map(parse).collect::<Option<Vec<_>>>()?;

    let bounds = readings
        .iter()
        .flat_map(|r| {
            let (d, dy) = (r.radius, (r.center.1 - 2000000).abs());
            if dy <= d {
                vec![r.center.0 - d + dy, r.center.0 + d - dy]
            } else {
                vec![]
            }
        })
        .collect::<Vec<_>>();
    let part1 = bounds.iter().max()? - bounds.iter().min()?;

    let ss = Vec::from_iter(collections::BTreeSet::from_iter(
        readings.iter().flat_map(|r| r.diamond.s),
    ));
    let aa = Vec::from_iter(collections::BTreeSet::from_iter(
        readings.iter().flat_map(|r| r.diamond.a),
    ));

    let limit = 4000000;
    let mut part2 = 0;
    'solved: for i in 0..ss.len() - 1 {
        for j in 0..aa.len() - 1 {
            let d = Diamond {
                a: [aa[j], aa[j + 1]],
                s: [ss[i], ss[i + 1]],
            };
            if !readings.iter().any(|r| r.diamond.includes(d)) {
                let p = Point2((d.a[0] - d.s[0]) / 2, (d.s[0] + d.a[0]) / 2);
                if 0 <= p.0 && p.0 <= limit && 0 <= p.1 && p.1 <= limit {
                    part2 = 4000000 * (p.0 as i64) + p.1 as i64;
                    break 'solved;
                }
            }
        }
    }

    Some((part1, part2))
}
