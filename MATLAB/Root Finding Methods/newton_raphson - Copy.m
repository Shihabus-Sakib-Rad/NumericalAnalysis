f=@(x) x^3 - 2*x -5;
df=@(x) 3*x^2 - 2;
xn=2;
error_limit=0.01;
max_iteration=100;
iter = 0;
while (1)
iter = iter + 1;
xnold = xn;
xn = xnold - f(xnold)/df(xnold);
error = abs((xn - xnold)/xn) * 100;
if error <= error_limit || iter >= max_iteration,break,end
end
fprintf('The root is: %f',xn)
