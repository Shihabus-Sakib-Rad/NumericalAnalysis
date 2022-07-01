h=0.1; %step size
xfinal=4; %solve from x=[0,xfinal]
x(1)=0;y(1)=2;
%define the RHS of the ODE
f=@(x,y)4*(exp(0.8*x))-0.5*y;
%write the loop for solving RK4
for i=1:ceil(xfinal/h) %ceil function rounds up a number towards infinity
    %update x
    x(i+1)=x(i)+h;
    %update y
    k1=f(x(i),      y(i));
    k2=f(x(i)+0.5*h,y(i)+0.5*k1*h);
    k3=f(x(i)+0.5*h,y(i)+0.5*k2*h);
    k4=f(x(i)+    h,y(i)+    k3*h);
    y(i+1)=y(i)+(h/6)*(k1+2*k2+2*k3+k4);
end
plot(x,y,'m')%magenta color


    
    
    
