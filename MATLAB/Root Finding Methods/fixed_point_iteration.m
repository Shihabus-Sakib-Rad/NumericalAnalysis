clear
clear all
clc
f=input('insert the function for which you want to know the root:');
g=@(x)f(x)+x;
error_limit=input('give your error limit value in %:');
max_iteration=input('give the maximum iteration value:');
iter = 0;
xp=input('insert the first guess of the root, xp:');
while (1)
iter=iter+1;
xpold = xp;
xp = g(xpold);
error = abs((xp - xpold)/xp) * 100;
if error <= error_limit || iter >= max_iteration,break,end
end
fprintf('The root is %f',xp)