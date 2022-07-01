f =@(x) 2*x +5;
xl = -5;
xu = 5;
error_limit = 0.01;
max_iteration = 100;
iter = 0; xb = xl;

while (1)
    iter = iter + 1;
    xbold = xb;
    xb = (xl + xu) / 2;
    error = abs((xb - xbold) / xb) * 100;
    test = f(xl) * f(xb);

    if test < 0
        xu = xb;
    elseif test > 0
        xl = xb;
    else
        error = 0;
    end

    if error <= error_limit || iter >= max_iteration, break, end
end

fprintf('The root is %f', xb)
