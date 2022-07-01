f=input('insert the function for which you want to know the root:');
%%Example: To insert f(x)=2x+5, write this way: @(x)2*x+5. This line is not a part of the programme%%
xl=input('give lower limit xl:');
xu=input('give upper limit xu:');
error_limit=input('give your error limit value in %:');
max_iteration=input('give the maximum iteration value:');
iter = 0; xf = xl;
while (1)
iter=iter+1;
xfold = xf;
xf = xu-(f(xu)*(xl-xu))/(f(xl)-f(xu));
error = abs((xf - xfold)/xf) * 100;
test = f(xl)*f(xf);
if test < 0
xu = xf;
elseif test > 0
xl = xf;
else
error = 0;
end
if error <= error_limit || iter >= max_iteration,break,end
end
fprintf('The root is %f',xf)
