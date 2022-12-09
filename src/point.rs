#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub struct Point2<T> (pub T, pub T);

impl <T: std::ops::Mul<Output=T> + Copy> std::ops::Mul<T> for Point2<T> {
    type Output = Self;

    fn mul(self, rhs: T) -> Self::Output {
        Self(self.0 * rhs, self.1 * rhs)
    }
}

impl <T: std::ops::Div<Output=T> + Copy> std::ops::Div<T> for Point2<T> {
    type Output = Self;

    fn div(self, rhs: T) -> Self::Output {
        Self(self.0 / rhs, self.1 / rhs)
    }
}

impl <T: std::ops::Sub<Output=T>> std::ops::Sub for Point2<T> {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self::Output {
        Self(self.0 - rhs.0, self.1 - rhs.1)
    }
}

impl <T: std::ops::Add<Output=T>> std::ops::Add for Point2<T> {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self(self.0 + other.0, self.1 + other.1)
    }
}