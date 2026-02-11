First, notice the chain of x^2 on the top-right diagonal, where x is an odd natural number.

Next, notice we can divide each concentric square into 4 equal sides ending in a number on the diagonal. (This works for all squares except the center) Since we know the beginning and end of these, we can split into 4 parts.

$$
1^2 + \frac{k}{4}(3^2-1^2): k=1,2,3,4
\\
3^2 + \frac{k}{4}(5^2-3^2): k=1,2,3,4
\\
x^2 + \frac{k}{4}((x+2)^2-x^2): k=1,2,3,4
$$

We find total sum of diagonals of concentric square. I did it in Wolfram to save myself from writing out the algebra.

$$
\sum_{k=1}^{4}x^2 + \frac{k}{4}((x+2)^2 - x^2)=4x^2+10x+10
$$

We can denote $x$ as the $j$th odd natural number.
$$
x=2j-1 \implies 4x^2+10x+10 = 16j^2 + 4j + 4
$$

Remember that $x^2$ represents the last digit of the previous square. So if our spiral is size $s$, we use $x=s-2$ to calculate the final square. This is the $\frac{s-1}{2}$th odd natural number.

We sum over all odd natural numbers from indices 1 to $\frac{s-1}{2}$

$$
\sum_{j=1}^{\frac{s-1}{2}}16j^2+4j+4=\frac{1}{6}(4s^3+3s^2+8s-15)
$$

Remember that this does not include the center at "1", so we add that and find our total!

$$
total = \frac{1}{6}(4s^3+3s^2+8s-9)
$$

Calculate for $s=5$ and $s=1001$.

$$
s=5 \implies total=\frac{1}{6}(4(5)^3+3(5)^2+8(5)-9) = 101
\\
s=1001 \implies total = \frac{1}{6}(4(1001)^3+3(1001)^2+8(1001)-9) = 669171001
$$