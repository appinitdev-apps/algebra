## Introduction

A system of three linear equations](../linear-equations/) in the unknowns $x,$ $y,$ and $z$ has the form:

$$
\begin{cases}
a_1x + b_1y + c_1z = d_1 \\
a_2x + b_2y + c_2z = d_2 \\
a_3x + b_3y + c_3z = d_3
\end{cases}
$$

All coefficients and constants are real numbers](../real-numbers/), and each equation has at least one nonzero coefficient among those of $x,$ $y,$ and $z.$ A solution is an ordered triple $(x,y,z)$ that satisfies all three equations. The entry on systems of linear equations](../systems-of-linear-equations/) has the definitions of consistency, dependence, and solution set. The focus here is elementary elimination in the three-variable case.

The solution set](../sets/) of one linear equation in three variables is a plane. The solutions of a system are the points common to its three planes. Their intersection has one of three forms:

+ One common point is one solution.
+ A common line or plane has infinitely many points, so the system has infinitely many solutions.
+ With no common point, the system has no solution.

The intersection is a line when the three equations leave one independent direction unconstrained. It is a plane when all three equations describe the same plane. The intersection can be empty because two planes are distinct and parallel, but parallelism is not required. Three planes may intersect in pairs and still have no point common to all three. Pairwise intersections are not sufficient for consistency.

## Elimination to two variables

Elementary elimination replaces an equation by the sum of itself and a multiple of another equation. The systems before and after the replacement have the same solution set because the operation is reversible. For equations denoted by $E_1,$ $E_2,$ and $E_3,$ an elimination has the form:

$$E_j \leftarrow E_j + kE_i$$

The following sequence reduces a three-variable system to a problem treated in systems of linear equations in two variables](../systems-of-linear-equations-in-two-variables/):

1. Choose one unknown to eliminate. A convenient choice has coefficients with small common multiples.
2. Use two different pairs of equations to obtain two equations without that unknown.
3. Solve the resulting two-variable system.
4. If the reduced system has one solution, substitute the two known values into an original equation and determine the remaining unknown.
5. Check the resulting ordered triple in all three original equations.

The two eliminations in the second step must remove the same unknown. Otherwise the result is not a system in a common pair of variables. These equation operations are scalar versions of the row operations in Gaussian elimination](../gaussian-elimination/), which is the systematic form of the same method for larger systems.

## A system with one solution

Consider the system:

$$
\begin{cases}
x + y + z = 4 \\
2x - y + z = 8 \\
x + 2y - z = -3
\end{cases}
$$

The coefficient of $x$ in the first equation is $1,$ so this equation is a convenient choice for both eliminations. Subtracting twice the first equation from the second eliminates $x$:

$$
\begin{aligned}
(2x - y + z) - 2(x + y + z) &= 8 - 2(4) \\
-3y - z &= 0
\end{aligned}
$$

Subtracting the first equation from the third gives a second equation in $y$ and $z$:

$$
\begin{aligned}
(x + 2y - z) - (x + y + z) &= -3 - 4 \\
y - 2z &= -7
\end{aligned}
$$

The first reduced equation is equivalent to $z=-3y.$ After this substitution, the second reduced equation has only $y$:

$$
\begin{aligned}
y - 2(-3y) &= -7 \\
7y &= -7 \\
y &= -1
\end{aligned}
$$

Since $y=-1,$ we have $z=3.$ After substitution into the first original equation, we have:

$$
\begin{aligned}
x + (-1) + 3 &= 4 \\
x &= 2
\end{aligned}
$$

The proposed triple satisfies every original equation:

$$
\begin{aligned}
2 + (-1) + 3 &= 4 \\
2(2) - (-1) + 3 &= 8 \\
2 + 2(-1) - 3 &= -3
\end{aligned}
$$

The system has the unique solution:

$$(x,y,z)=(2,-1,3)$$

## Contradictions and no solution

After elimination, we may have an equality whose variable terms cancel but whose constants do not. Consider the system:

$$
\begin{cases}
x + y + z = 2 \\
2x - y + z = 1 \\
3x + 2z = 5
\end{cases}
$$

Adding the first two equations gives $3x+2z=3,$ while the third requires $3x+2z=5.$ The same contradiction is obtained by subtracting the first and second equations from the third:

$$
\begin{aligned}
(3x + 2z) - (x + y + z) - (2x - y + z) &= 5 - 2 - 1 \\
0 &= 2
\end{aligned}
$$

No ordered triple can satisfy this contradiction, so the system is inconsistent. Every point common to the first two planes lies on the plane $3x+2z=3.$ That plane is parallel to the third plane, whose equation is $3x+2z=5,$ and the three planes have no common point.

## Identities and free variables

When elimination ends in an identity, one equation has no new condition. Consider:

$$
\begin{cases}
x + y + z = 2 \\
2x - y + 3z = 1 \\
3x + 4z = 3
\end{cases}
$$

The third equation is a linear combination](../linear-combinations/) of the first two, in this case their sum. For the second equation we have:

$$
\begin{aligned}
(2x - y + 3z) - 2(x + y + z) &= 1 - 2(2) \\
-3y + z &= -3
\end{aligned}
$$

For the third equation we have the same reduced equation:

$$
\begin{aligned}
(3x + 4z) - 3(x + y + z) &= 3 - 3(2) \\
-3y + z &= -3
\end{aligned}
$$

The two reduced equations are identical, so one unknown is free. Set $y=t,$ where $t \in \mathbb{R}.$ From the reduced equation and the first original equation we have:

$$
\begin{aligned}
z &= 3t - 3 \\
x &= 2 - y - z \\
  &= 5 - 4t
\end{aligned}
$$

Every solution has the form:

$$(x,y,z)=(5-4t,t,3t-3), \qquad t \in \mathbb{R}$$

Substitution verifies the parametrization for every real value of $t$:

$$
\begin{aligned}
(5 - 4t) + t + (3t - 3) &= 2 \\
2(5 - 4t) - t + 3(3t - 3) &= 1 \\
3(5 - 4t) + 4(3t - 3) &= 3
\end{aligned}
$$

The same line has the vector equation](../vector-and-parametric-equations-of-a-line/):

$$(x,y,z)=(5,0,-3)+t(-4,1,3), \qquad t \in \mathbb{R}$$

This is the line common to the three planes. An identity means that one condition is redundant, but the identity alone is not enough to classify the system. Another elimination may still produce a contradiction. If no contradiction occurs and at least one unknown remains free, the system has infinitely many solutions. The corresponding matrix criterion is the Rouché-Capelli theorem, stated in terms of matrix rank](../rank-of-a-matrix/).
