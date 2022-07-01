f=input('give the input function. example:to give f(x)=2x+5, write this way: @(x)2*x-5 \n')
xmax=input('give the value of xmax\n')
xmin=input('give the value of xmin \n')
n=input('give the value of number of division n \n')
x=linspace(xmin,xmax,n);
y=f(x);
fprintf('There must be a root in between the two column values of x \n')
for k=1:length(x)-1
    if sign(y(k))~=sign(y(k+1))
        fprintf('%f          %f \n',[x(k);x(k+1)])
    end
end