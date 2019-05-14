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
     
        public double GetFunctionValue()
        {
            return Math.Cos(0.3 * x) * Math.Cos(0.25 * y - 7) - (1 / x);
        }

        public double GetDerivativeX()
        {
            return -0.3 * Math.Sin(0.3 * x) * Math.Cos(0.25 * y - 7) - (1 / Math.Pow(x, 2));
        }

        public double GetDerivativeY()
        {
            return -0.25 * Math.Sin(0.25 * y - 7) * Math.Cos(0.3 * x);
        }

        public double GetGradientAbs(double[] gradient_array)
        {
            double sum = Math.Sqrt(Math.Pow(gradient_array[0], 2) + Math.Pow(gradient_array[1], 2));
            return sum;
        }

        public double GetBarrierFunction(double function_value, double x, double y, int iteration_number)
        {
            double parametre = Math.Pow(2, iteration_number - 1);
            double restrinction_1 = Math.Pow(y - 5 * x, 2);
            double restrinction_2 = Math.Pow(y + 0.01 * Math.Pow(x - 20, 2) - 37, 2);
            double restrinction_3 = Math.Pow(x - 40, 2);
            double restrinction_4 = Math.Pow(1 - x, 2);
            double restrinction_5 = Math.Pow(y - 40, 2);
            double restrinction_6 = Math.Pow(1 - y, 2);
            double barrier_function = restrinction_1 + restrinction_2 + restrinction_3 + restrinction_4 + restrinction_5 + restrinction_6;
            return function_value + parametre * barrier_function;
        }
}

    class Program
    {
        public void GradientDescent(double epsylon, ref double x_start, ref double y_start)
        {
            int iteration_descent = 0;
            double lambda = 0.01;
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
                double[] gradient = new double[] { function.GetDerivativeX(), function.GetDerivativeY() };
                double gradient_abs = function.GetGradientAbs(gradient);
                if (gradient_abs < epsylon)
                {
                    break;
                }
                for(int i = 0; i < 2; i++)
                {
                    x_new[i] = x_old[i] - lambda * gradient[i];
                }
                for (int i = 0; i < 2; i++)
                {
                    x_old[i] = x_new[i];
                }
                iteration_descent++;
            }
            x_start = x_new[0];
            y_start = x_new[1];
        }


        static void Main(string[] args)
        {
            Console.Write("Epsylon for gradient descent: ");
            double epsylon = Convert.ToDouble(Console.ReadLine());
            Random random = new Random();
            Function minimization = new Function(1, 1);
            
        }
    }
}
