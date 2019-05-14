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
    }

    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            Function minimization = new Function(1, 1);
            double[] gradient = new double[] {minimization.GetDerivativeX(), minimization.GetDerivativeY()};
        }
    }
}
