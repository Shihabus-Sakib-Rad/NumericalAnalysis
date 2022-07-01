f=input('Insert the function for which you want to know root:');
x1=input('Give lower limit x1:');
x2=input('Give upper limit x2:');
error_limit=input('Give your error limit value:');
max_iteration=input('Give the maximum iteration value:');
iter =0;xs=x2;
while (1)
iter=iter+1;
xsold = xs;
xs = x2 - ((f(x2)*(x2-x1))/(f(x2)-f(x1)));
error = abs((xs - xsold)/xs) * 100;
if error <= error_limit || iter >= max_iteration,break,end
x1=x2; x2=xs;
end
fprintf('The root is %f',xs)
