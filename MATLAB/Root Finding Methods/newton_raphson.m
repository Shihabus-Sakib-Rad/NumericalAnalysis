f=input('Insert the function for which you want to know the root:');
df=input('Give the derivative of the function:');
xn=input('Give your first assumption of root , xn :');
error_limit=input('Give your error limit value:');
max_iteration=input('Give the maximum iteration value:');
iter = 0;
while (1)
iter = iter + 1;
xnold = xn;
xn = xnold - f(xnold)/df(xnold);
error = abs((xn - xnold)/xn) * 100;
if error <= error_limit || iter >= max_iteration,break,end
end
fprintf('The root is: %f',xn)
