#include <iostream>

using namespace std;

//function declarations
double map(double val, double min, double max, double newMin,double newMax);
double weightedAverage(double *foo);
double aveOfAboveAverage(double *foo);

int main()
{

  double foo [5] = { 70, 72, 78, 90, 93 };
  cout<<weightedAverage(foo)<<"\n"<<aveOfAboveAverage(foo)<<"\n";

}

double map(double val, double min, double max, double newMin,double newMax)
{
  return  (val - min) / (min - max) * (newMax - newMin) + newMin;
}

double weightedAverage(double *foo)
{
  double max = foo[0];
  double min = foo[0];
  int size = sizeof(foo);

  for (int i = 1; i < size; i++){ // get min and max

      if(foo[i] < min)
        min = foo[i];

      if(foo[i] > max)
        max = foo[i];
  }

  double sum = 0;
  double count = 0;

  for(int i = 0; i < size; i++){
    double maped = map(foo[i], min, max, 0, 100);
    sum += foo[i] * maped;
    count += maped;
  }

  return sum/count;
}

double aveOfAboveAverage(double *foo)
{
  int size = sizeof(foo);
  double sum = 0;
  for(int i = 0; i < size; i++){
    sum += foo[i];
  }
  double average = sum /(size*1.0);

  sum = 0;
  double count = 0;
  for(int i = 0; i < size; i++){
    if(foo[i] > average){
      sum += foo[i];
      count += 1.0;
    }
  }
  return sum / count;
}
