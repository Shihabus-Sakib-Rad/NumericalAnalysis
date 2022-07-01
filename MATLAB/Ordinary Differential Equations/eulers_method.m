f=@(x,y) 4*(exp(0.8*x))-0.5*y;
% (0, 2)
h=0.1; %step size

xfinal=4; %solve from x=[0,xfinal]


x(1)=0;
y(1)=2;

steps = ceil(xfinal/h)

for i=1:steps
    x(i+1)=x(i)+h;
    y(i+1)=y(i)+f(x(i),y(i))*h;
end
plot(x,y,'r')%red color
hold on