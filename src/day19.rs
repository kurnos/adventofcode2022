use std::{ops::{Add, Sub, Mul}, collections::BTreeSet, cmp::max};
use regex::Regex;

#[derive(Debug, Copy, Clone, Eq, PartialEq, PartialOrd, Ord)]
struct Mats(u8,u8,u8,u8);

impl Mats {
    fn ge(self, rhs: Self) -> bool {
        self.0 >= rhs.0 && self.1 >= rhs.1 && self.2 >= rhs.2 && self.3 >= rhs.3
    }
}

impl Add for Mats {
    type Output=Mats;

    fn add(self, rhs: Self) -> Self::Output {
        Mats(self.0+rhs.0, self.1+rhs.1, self.2+rhs.2, self.3+rhs.3)
    }
}

impl Sub for Mats {
    type Output=Mats;

    fn sub(self, rhs: Self) -> Self::Output {
        Mats(self.0-rhs.0, self.1-rhs.1, self.2-rhs.2, self.3-rhs.3)
    }
}

impl Mul<u8> for Mats {
    type Output=Mats;

    fn mul(self, rhs: u8) -> Self::Output {
        Mats(self.0*rhs, self.1*rhs, self.2*rhs, self.3*rhs)
    }
}

#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Debug)]
struct State {
    t: u8,
    res: Mats,
    prod: Mats,
}

fn parse(line: &str) -> Option<[(Mats, Mats); 4]> {
    let re = Regex::new(r"^Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$").ok()?;
    let c = re.captures(line)?;

    Some([
        (Mats(1,0,0,0), Mats(c.get(1)?.as_str().parse().ok()?,0,0,0)),
        (Mats(0,1,0,0), Mats(c.get(2)?.as_str().parse().ok()?,0,0,0)),
        (Mats(0,0,1,0), Mats(c.get(3)?.as_str().parse().ok()?,c.get(4)?.as_str().parse().ok()?,0,0)),
        (Mats(0,0,0,1), Mats(c.get(5)?.as_str().parse().ok()?,0,c.get(6)?.as_str().parse().ok()?,0)),
    ])
}

fn run(bp: [(Mats, Mats);4], n: u8) -> u8 {
    let mut max_c = Mats(0,0,0,0);
    for (_, cost) in bp {
        max_c.0 = max(max_c.0, cost.0);
        max_c.1 = max(max_c.1, cost.1);
        max_c.2 = max(max_c.2, cost.2);
    }

    let mut visited: BTreeSet<State> = BTreeSet::new();
    let mut queue = vec![
        State{ t: 0, res: Mats(0,0,0,0), prod: Mats(1,0,0,0) }
    ];

    let mut best = 0;

    while let Some(s) = queue.pop() {
        if s.t == n {
            if s.res.3 > best {
                best = s.res.3;
            }
            continue
        }

        for &(prod, cost) in bp.iter() {
            let x = s.prod + prod;
            if x.0 > max_c.0 || x.1 > max_c.1 || x.2 > max_c.2 {
                continue
            }

            let mut new_s = s;
            while new_s.t < n {
                if new_s.res.ge(cost) {
                    new_s = State{
                        t: new_s.t + 1,
                        res: new_s.res + new_s.prod - cost,
                        prod: new_s.prod + prod,
                    };
                    if visited.insert(new_s) {
                        queue.push(new_s)
                    }
                    break
                }
                new_s = State{
                    t: new_s.t + 1,
                    res: new_s.res + new_s.prod,
                    prod: new_s.prod,
                };
            }
        }
    }
    println!("visited {}", visited.len());
    best
}


pub fn solve(data: &str) -> Option<(u16, u16)> {
    let blueprints = data.split('\n').map(parse).collect::<Option<Vec<_>>>()?;

    let part1 = blueprints.iter().enumerate().map(|(t, &bp)| {
        (t+1) as u16 * run(bp, 24) as u16
    }).sum();

    let part2 = run(blueprints[0], 32) as u16 * run(blueprints[1], 32) as u16 * run(blueprints[2], 32) as u16;

    return Some((part1, part2))
}