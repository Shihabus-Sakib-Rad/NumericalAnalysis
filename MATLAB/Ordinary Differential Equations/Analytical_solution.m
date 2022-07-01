x=0:0.1:4;
y=(4/1.3)*(exp(0.8*x)-exp(-0.5*x))+2*(exp(-0.5*x));
plot(x,y,'g')%green color
xlabel('x')
ylabel('y')
hold on