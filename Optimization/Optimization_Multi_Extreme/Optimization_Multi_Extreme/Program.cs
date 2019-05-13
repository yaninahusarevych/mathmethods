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
        public double lambda_1;
        public double lambda_2;
        public double lambda_3;
        public double lambda_4;
        public double lambda_5;
        public double lambda_6;

        /* public void SetLambdaValue()
        {
            if((y - 5 * x) != 0)
            {
                lambda_1 = 0;
            }
            if ((y + 0.01 * Math.Pow(x - 20, 2) - 37) != 0)
            {
                lambda_2 = 0;
            }
            if ((x - 40) != 0)
            {
                lambda_3 = 0;
            }
            if ((1 - x) != 0)
            {
                lambda_4 = 0;
            }
            if ((y - 40) != 0)
            {
                lambda_5 = 0;
            }
            if ((1 - y) != 0)
            {
                lambda_6 = 0;
            }
        }*/

        public double GetFunctionValue()
        {
            return Math.Cos(0.3 * x) * Math.Cos(0.25 * y - 7) - (1 / x);
        }

        public double GetDerivativeX()
        {
            //SetLambdaValue();
            return -0.3 * Math.Sin(0.3 * x) * Math.Cos(0.25 * y - 7) - (1 / Math.Pow(x, 2)) - 5 * lambda_1 * x + 
                0.02 * lambda_2 * (x - 20) + lambda_3 - lambda_4;
        }

        public double GetDerivativeY()
        {
            //SetLambdaValue();
            return -0.25 * Math.Sin(0.25 * y - 7) * Math.Cos(0.3 * x) + lambda_1 + lambda_2 + lambda_5 - lambda_6;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            Function minimization = new Function
            {
                x = 1, //Convert.ToDouble(random.Next(1, 40)),
                y = 1 //Convert.ToDouble(random.Next(1, 40))
            };

            Console.WriteLine("lambda_4 = " + minimization.lambda_4);
            double first_restrinction = minimization.GetDerivativeX();
            double second_restriction = minimization.GetDerivativeY();
            if (first_restrinction == 0 && second_restriction == 0)
            {
                Console.WriteLine("Point with coordinates: x = " + minimization.x + ", y = " + minimization.y + 
                    " can be optimal solution for minimization problem");
            }
            else
            {
                Console.WriteLine("Point with coordinates: x = " + minimization.x + ", y = " + minimization.y +
                   " cannot be optimal solution for minimization problem");
            }
        }
    }
}
