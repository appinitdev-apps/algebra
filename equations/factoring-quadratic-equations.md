## Factorization

When we introduced quadratic equations](../quadratic-equations/), we saw that they can be written in the following standard form:

$$ax^{2} + bx + c = 0 $$

We also saw that $(1)$ requires the coefficient $a$ to be nonzero, that its solutions can be obtained using the quadratic formula](../quadratic-formula/), and that their nature is determined by the discriminant $\Delta = b^2 - 4ac.$ In some cases, however, factoring provides a more direct way to find the solutions without using the quadratic formula. The aim is to express the left-hand side of $(1)$ as a product of linear factors and thus find its solutions. Specifically, when the discriminant is positive, we know that $(1)$ has two distinct real roots, $x_1$ and $x_2,$ for which the following identity holds:

$$ax^{2} + bx + c = a(x - x_1)(x - x_2) $$

When $\Delta = 0$ the roots coincide, and the factorization then reduces to $a(x - x_0)^2.$ When $\Delta < 0,$ the polynomial is irreducible over $\mathbb{R},$ has two complex conjugate roots](../quadratic-equations-with-complex-solutions/), and can be factored only over $\mathbb{C}.$ To illustrate how factoring works, we consider the quadratic polynomial](../polynomials/) associated with $(1)$:

$$P(x) = ax^2 + bx + c $$

Since we have required $a$ to be nonzero, we can factor out the leading coefficient and rewrite $(3)$ as follows:

$$P(x) = a\left(x^2 + \frac{b}{a}x + \frac{c}{a}\right) $$

Vieta's formulas, discussed in detail on their own page, relate the coefficients of the polynomial in parentheses to its roots as follows:

$$
\begin{aligned}
x_1 + x_2 &= -\frac{b}{a} \\
x_1x_2 &= \frac{c}{a}
\end{aligned}
$$

Substituting these expressions into $(4)$ gives:

$$
\begin{aligned}
P(x) &= a\left[x^2 - (x_1 + x_2)x + x_1x_2\right] \\
&= a\left(x^2 - x_1x - x_2x + x_1x_2\right) \\
&= a\left[x(x - x_1) - x_2(x - x_1)\right] \\
&= a(x - x_1)(x - x_2)
\end{aligned}
$$

This proves identity $(2).$ The roots of equation $(1)$ can now be found simply by setting each linear factor equal to zero, as follows:

$$ 
\begin{aligned}
x - x_1 = 0 &\implies x = x_1 \\
x - x_2 = 0 &\implies x = x_2
\end{aligned}
$$

> An alternative approach is the AC method](../factoring-polynomials-ac-method/), which allows us to factor the polynomial without explicitly calculating its discriminant.

## Finding the factors

We now examine the practical method for finding the factors of the left-hand side of $(1).$ The process is fairly simple, but it takes some practice. We can begin by looking directly for the constant terms of the linear factors, using the following identity:

$$a(x + r)(x + s) = a\left[x^2 + (r + s)x + rs\right] $$

Comparing the coefficients with those in $(1)$ gives two conditions that $r$ and $s$ must satisfy:

$$ 
\begin{aligned}
rs &= \frac{c}{a} \\
r + s &= \frac{b}{a}
\end{aligned}
$$

Our aim at this stage is to find $r$ and $s.$ We therefore draw up a table like the one in the following example to identify the row that satisfies both conditions in $(7).$ To factor the polynomial $x^2 - 5x + 6,$ we look for two numbers whose product is $6$ (that is, $c/a$) and whose sum is $-5$ (that is, $b/a$). We first list all pairs of integers whose product is $6$ in the columns headed $r$ and $s.$ In the column headed $r+s,$ we enter the sum of the two values in each row:

$$
\begin{array}{c|c|c|c}
r & s & rs & r+s \\
\\\\\hline
1 & 6 & 6 & 7 \\
2 & 3 & 6 & 5 \\
-1 & -6 & 6 & -7 \\
-2 & -3 & 6 & -5
\end{array}
$$

Keep in mind that the order of the rows does not matter, but working systematically helps us identify all possible candidates. The table makes it easy to see that the last row satisfies both conditions in $(7).$ Thus, setting $r = -2$ and $s = -3,$ we obtain the following factorization:

$$x^2 - 5x + 6 = (x - 2)(x - 3)$$

It follows from $(5)$ that the associated equation has solutions $x_1 = 2$ and $x_2 = 3,$ which are the same as those obtained by solving $x^2 - 5x + 6=0$ with the quadratic formula.

## Examples

The following examples provide practice in solving quadratic equations by factoring. In some of these cases, the quadratic formula would yield the solutions in fewer steps; here, however, factoring is used solely for instructional purposes.

[class="table-1 -right"]

|                      |                           |
| -------------------- | ------------------------- |
| $x^2 - 4x + 3 = 0$   | $x_1 = 1,$ $x_2 = 3$      |
| $2x^2 - 7x + 3 = 0$  | $x_1 = 3,$ $x_2 = 1/2$    |
| $x^2 - 6x + 9 = 0$   | $x_1 = x_2 = 3$           |
| $6x^2 + 13x - 8 = 0$ | $x_1 = 1/2,$ $x_2 = -8/3$ |


[/class]

Consider the first equation in the table and write out its associated polynomial:

$$x^{2} - 4x + 3$$

To factor it, we know that we need two numbers $r$ and $s$ satisfying the relations in $(7).$ In this case, their product must be $3$ and their sum $-4.$ We begin by identifying the pairs of integers whose product is $3:$

$$
\begin{array}{c|c|c|c}
r & s & rs & r+s \\
\\\\\hline
1 & 3 & 3 & 4 \\
-1 & -3 & 3 & -4
\end{array}
$$

We now check which row gives a sum of $-4.$ The sum in the first row is $4,$ so we discard that row. The second row is the one we need. The numbers satisfying $(7)$ are therefore $r = -1$ and $s = -3,$ and the polynomial factors as follows:

$$x^{2} - 4x + 3 = (x - 1)(x - 3)$$

By $(5),$ the equation associated with the polynomial therefore has solutions $x_1 = 1$ and $x_2 = 3.$

- - -

Consider the polynomial in the second equation:

$$2x^{2} - 7x + 3$$

Here $a = 2,$ so we factor out this coefficient as in $(4)$ to obtain:

$$2\left(x^2 - \frac{7}{2}x + \frac{3}{2}\right)$$

We now look for two numbers $r$ and $s$ whose product is $3/2$ and whose sum is $-7/2,$ and list candidate pairs in a table as before:

$$
\begin{array}{c|c|c|c}
r & s & rs & r+s \\
\\\\\hline
1 & 3/2 & 3/2 & 5/2 \\
3 & 1/2 & 3/2 & 7/2 \\
-1 & -3/2 & 3/2 & -5/2 \\
-3 & -1/2 & 3/2 & -7/2
\end{array}
$$

The last row satisfies both conditions in $(7),$ so setting $r = -3$ and $s = -1/2,$ we obtain:

$$2x^{2} - 7x + 3 = 2(x - 3)\left(x - \frac{1}{2}\right) = (x - 3)(2x - 1)$$

The associated equation therefore has solutions $x_1 = 3$ and $x_2 = 1/2.$

- - -

Next, consider the polynomial in the third equation:

$$x^{2} - 6x + 9$$

As in the preceding examples, we look for $r$ and $s$ whose product is $9$ and whose sum is $-6.$ We draw up a table as before:

$$
\begin{array}{c|c|c|c}
r & s & rs & r+s \\
\\\\\hline
1 & 9 & 9 & 10 \\
3 & 3 & 9 & 6 \\
-1 & -9 & 9 & -10 \\
-3 & -3 & 9 & -6
\end{array}
$$

The last row satisfies both conditions with $r = s = -3,$ so the factorization is:

$$x^{2} - 6x + 9 = (x - 3)^{2}$$

The equation therefore has a single root $x = 3$ of multiplicity two](../roots-of-a-polynomial/).

- - -

Next, consider the following polynomial equation](../polynomial-equations/):

$$6x^2 + 13x - 8 = 0$$

Factoring out the coefficient $6$ gives:

$$6x^2 + 13x - 8 = 6\left(x^2 + \frac{13}{6}x - \frac{4}{3}\right)$$

The constant terms of the factors must satisfy the following conditions:

$$rs = -\frac{4}{3}\qquad r+s = \frac{13}{6}$$

The product is negative, so the two numbers must have opposite signs. We draw up a table with some candidate pairs:

$$
\begin{array}{c|c|c|c}
r & s & rs & r+s \\
\\\\\hline
1/6 & -8 & -4/3 & -47/6 \\
-1/6 & 8 & -4/3 & 47/6 \\
1/3 & -4 & -4/3 & -11/3 \\
-1/2 & 8/3 & -4/3 & 13/6
\end{array}
$$

The row that satisfies both conditions in $(7)$ is the one with $r = -1/2$ and $s = 8/3.$ Carrying out the calculation gives:

$$
\begin{aligned}
6x^2 + 13x - 8 &= 6\left(x - \frac{1}{2}\right)\left(x + \frac{8}{3}\right) \\
&= (2x - 1)(3x + 8)
\end{aligned}
$$

The equation associated with the polynomial can therefore be written in factored form as follows:

$$(2x - 1)(3x + 8) = 0$$

By the zero-product property, at least one factor must be zero, so at least one of the following equations must hold:

$$
\begin{aligned}
2x - 1 &= 0 \\
3x + 8 &= 0
\end{aligned}
$$

Solving the two linear equations](../linear-equations/) gives the solutions $x_1 = 1/2$ and $x_2 = -8/3.$