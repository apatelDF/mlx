#include <iostream>

using namespace std;

int main()
{

  double foo [5] = { 70, 72, 78, 90, 93 };
  double max = foo[0];
  double min = foo[0];
  int size = foo.size();

  for (int i = 1; i < size); i++){ // get min and max

      if(foo[i] < min)
        min = foo[i];

      if(foo[i] > max)
        max = foo[i];
  }

  double sum = 0;
  double count = 0;

  for(int i = 0; i < size, i++){
    maped = map(foo[i], min, max, 0, 100);
    sum += foo[i] * maped;
    count += maped;
  }

  double average = sum/count

  cout<<average<<"\n";

}

double map(double val, double min, double max, double newMin,double newMax)
{
  return  (val - min) / (min - max) * (newMax - newMin) + newMin;
}
