using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Optimization_Multi_Extreme
{
    public class Function
    {
        public double x;
        public double y;

        public Function(double x, double y)
        {
            this.x = x;
            this.y = y;
        }

        public void GetRestrictions(ref double[] restrictions)
        {
            restrictions = new double[] { Math.Pow(y - 5 * x, 2), Math.Pow(y + 0.01 * Math.Pow(x - 20, 2) - 37, 2), Math.Pow(x - 40, 2),
                Math.Pow(1 - x, 2), Math.Pow(y - 40, 2), Math.Pow(1 - y, 2)};
            for (int i = 0; i < restrictions.Length; i++)
            {
                if (restrictions[i] > 0)
                {
                    restrictions[i] = 0;
                }
            }
        }

        public double GetGradientAbs(double[] gradient_array)
        {
            double sum = Math.Sqrt(Math.Pow(gradient_array[0], 2) + Math.Pow(gradient_array[1], 2));
            return sum;
        }

        public double GetBarrierFunction(int parametre)
        {
            double[] restrictions = new double[6];
            GetRestrictions(ref restrictions);
            double function_value = Math.Cos(0.3 * x) * Math.Cos(0.25 * y - 7) - (1 / x);
            double barrier_function = 0;
            for (int i = 0; i < restrictions.Length; i++)
            {
                barrier_function += restrictions[i];
            }
            return function_value + parametre * barrier_function;
        }

        public double GetBarrierDerivativeX(int parametre)
        {
            double[] restrictions = new double[6];
            GetRestrictions(ref restrictions);
            double[] restrictions_derivitaves = new double[] { -10 * (y - 5 * x), 0.04 * (x - 20) * (y + 0.01 * Math.Pow(x - 20, 2) - 37),
                2 * (x - 40), -2 * (1 - x) };
            for (int i = 0; i < restrictions_derivitaves.Length; i++)
            {
                if(restrictions[i] == 0)
                {
                    restrictions_derivitaves[i] = 0;
                }
            }
            double barrier_derivatives_x = 0;
            for (int i = 0; i < restrictions_derivitaves.Length; i++)
            {
                barrier_derivatives_x += restrictions_derivitaves[i];
            }
            double function_derivative_x = -0.3 * Math.Sin(0.3 * x) * Math.Cos(0.25 * y - 7) - (1 / Math.Pow(x, 2));
            return function_derivative_x + parametre * barrier_derivatives_x;
        }
        
        public double GetBarrierDerivativeY(int parametre)
        {
            double[] restrictions = new double[6];
            GetRestrictions(ref restrictions);
            double[] restrictions_derivitaves = new double[] { 2 * (y - 5 * x), 2 * (y + 0.01 * Math.Pow(x - 20, 2) - 37), 2 * (y - 40), -2 * (1 - y) };
            for (int i = 0; i < restrictions_derivitaves.Length; i++)
            {
                if (i == 2 || i == 3)
                {
                    if(restrictions[i+2] == 0)
                    {
                        restrictions_derivitaves[i] = 0;
                    }
                }
                else
                {
                    if (restrictions[i] == 0)
                    {
                        restrictions_derivitaves[i] = 0;
                    }
                }
            }
            double barrier_derivatives_y = 0;
            for (int i = 0; i < restrictions_derivitaves.Length; i++)
            {
                barrier_derivatives_y += restrictions_derivitaves[i];
            }
            double function_derivative_y = -0.25 * Math.Sin(0.25 * y - 7) * Math.Cos(0.3 * x);
            return function_derivative_y + parametre * barrier_derivatives_y;
        }
    }

    public class GradientDescent
    {
        public void FindLocalMinimum(double epsylon, ref double x_start, ref double y_start, int parametre)
        {
            int iteration_descent = 0;
            double lambda = 5;
            double[] x_old = new double[2];
            double[] x_new = new double[2];
            while (true)
            {
                if (iteration_descent == 0)
                {
                    x_old[0] = x_start;
                    x_old[1] = y_start;
                }
                Function function = new Function(x_old[0], x_old[1]);
                double[] gradient = new double[] { function.GetBarrierDerivativeX(parametre), function.GetBarrierDerivativeY(parametre) };
                double gradient_abs = function.GetGradientAbs(gradient);
                if (gradient_abs < epsylon)
                {
                    break;
                }
                for (int i = 0; i < 2; i++)
                {
                    x_new[i] = x_old[i] - lambda * gradient[i];
                }
                for (int i = 0; i < 2; i++)
                {
                    x_old[i] = x_new[i];
                }
                iteration_descent++;
            }
            if (iteration_descent != 0)
            {
                x_start = x_new[0];
                y_start = x_new[1];
            }
            Console.WriteLine("Iterations =  " + iteration_descent);
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Epsylon for gradient descent: ");
            double epsylon = Convert.ToDouble(Console.ReadLine());
            Random random = new Random();
            Function minimization = new Function(15, 18);
            int parametre = 1;
            Console.WriteLine("Value in start point = " + minimization.GetBarrierFunction(parametre));
            GradientDescent gradientDescent = new GradientDescent();            
            while (parametre > epsylon)
            {
                gradientDescent.FindLocalMinimum(epsylon, ref minimization.x, ref minimization.y, parametre);
                Console.WriteLine("Value in point with x: " + minimization.x + ", y: " + minimization.y + " = " + minimization.GetBarrierFunction(parametre));
                parametre /= 10;
            }
        }
    }
}
