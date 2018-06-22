#include <iostream>

using namespace std;

//function declarations
double map(double val, double min, double max, double newMin,double newMax);
double weightedAverage(double *foo);
double aveOfAboveAverage(double *foo);

int main()
{

  double foo [715]= {28.711,27.792,28.178,28.268,28.313,28.450,28.631,28.353,28.295,28.221,28.586,28.024,28.336,28.298,28.683,27.972,28.248,28.537,28.573,28.238,29.127,28.777,28.629,28.172,29.070,28.718,28.894,28.509,28.883,29.076,29.687,29.163,28.942,28.618,28.332,28.134,28.541,28.517,28.394,27.982,28.318,28.092,28.151,27.914,28.753,28.156,27.861,28.261,28.118,28.198,28.582,28.528,28.359,28.837,28.618,28.730,28.610,28.814,28.605,28.558,28.881,28.605,29.019,29.005,28.513,28.605,28.482,28.154,28.428,28.766,27.946,28.048,28.248,28.450,28.387,28.199,28.340,28.594,28.128,28.421,28.544,28.256,28.321,28.073,28.986,28.410,28.445,28.408,28.728,28.530,28.778,28.326,29.035,28.677,28.639,28.351,28.483,28.116,28.430,28.237,28.430,28.173,28.300,28.519,28.179,28.303,28.405,28.049,28.329,28.246,28.347,28.466,28.346,28.247,28.304,28.378,28.597,28.835,28.656,28.480,28.723,28.828,28.500,28.428,28.796,28.528,28.297,29.030,28.163,28.340,28.719,28.336,28.268,28.561,28.439,28.254,28.607,28.734,28.199,28.376,28.440,28.248,28.730,27.926,28.361,28.278,28.256,28.490,28.253,28.898,28.563,28.491,28.593,28.432,28.962,28.417,28.746,28.817,28.917,27.554,28.126,28.112,28.473,27.955,28.466,28.365,28.968,28.291,29.580,28.335,28.803,28.610,28.409,28.281,28.132,28.303,28.803,28.246,28.443,28.710,28.649,28.723,28.537,28.532,28.564,28.493,28.667,28.686,28.746,28.565,28.278,28.197,28.489,28.339,28.295,28.444,28.610,28.566,28.497,28.802,29.183,31.090,29.365,29.834,28.763,28.843,28.320,28.427,28.594,28.279,28.641,28.140,28.629,28.230,28.950,28.392,27.980,28.579,28.349,28.584,28.453,28.300,28.852,27.232,28.490,28.364,28.630,28.244,28.633,28.023,28.703,28.247,31.642,29.572,31.352,30.034,29.809,28.667,28.683,28.642,28.605,28.316,28.433,28.311,28.448,28.444,28.483,28.168,28.580,28.403,28.510,28.438,28.743,28.800,27.995,27.913,28.091,28.460,28.598,28.515,28.313,28.996,28.813,30.302,30.533,32.592,32.362,32.093,31.328,31.273,29.314,29.422,28.126,28.591,28.517,28.460,28.644,28.192,28.679,28.554,28.485,28.324,28.714,28.284,28.549,28.354,28.739,27.168,28.536,28.275,28.361,27.955,28.948,28.448,30.536,28.965,32.884,31.879,32.682,32.094,32.728,31.286,30.920,29.814,29.226,28.593,28.639,28.303,28.674,28.808,28.445,28.596,28.308,28.363,28.237,28.585,28.762,28.420,27.634,28.341,28.595,28.757,28.668,28.844,28.724,29.482,29.526,32.560,32.332,33.558,32.878,32.994,32.587,32.664,32.080,32.187,30.319,30.384,29.259,28.561,28.347,28.620,28.371,28.259,28.591,28.458,28.779,28.458,28.650,28.496,28.577,28.159,28.835,28.330,28.219,28.480,29.530,28.753,32.294,30.412,34.299,33.225,33.583,33.175,32.902,32.848,32.213,31.967,31.870,30.751,29.610,29.090,28.328,28.461,27.930,28.636,28.181,28.437,28.476,28.707,28.600,28.479,28.681,28.493,28.450,28.323,28.205,28.425,28.945,31.092,30.841,33.522,33.628,34.564,34.155,33.856,33.454,32.664,32.621,32.372,32.219,31.654,31.181,28.926,28.945,28.697,28.535,28.474,28.354,28.337,28.338,28.403,28.487,28.216,28.645,28.384,28.889,28.420,28.804,28.235,30.758,29.189,32.667,32.258,33.935,34.054,33.947,34.386,33.459,33.366,32.776,32.502,31.703,32.534,29.363,30.553,28.741,28.703,28.474,28.123,28.522,28.465,28.276,28.435,28.844,28.666,28.557,28.458,28.412,28.779,28.618,28.839,29.437,31.981,32.515,32.602,33.633,33.339,34.348,33.200,33.460,32.708,33.297,32.716,32.441,30.769,30.583,28.879,28.901,28.662,28.751,28.224,28.455,28.549,28.551,28.501,28.674,28.491,28.816,28.358,28.403,28.379,29.006,28.929,31.579,30.135,32.674,32.781,32.740,33.364,32.741,33.703,32.951,33.035,32.577,32.681,31.359,32.508,28.893,29.271,28.502,28.813,28.726,28.176,28.417,28.281,28.839,28.308,28.837,28.441,28.693,28.851,28.266,28.880,28.759,28.696,30.103,30.616,32.329,31.805,32.560,32.485,32.963,32.454,32.587,32.690,32.781,31.630,32.408,29.459,29.431,28.422,28.536,28.365,28.849,28.236,28.187,28.445,28.597,29.407,29.227,29.049,28.880,29.072,28.191,28.259,28.706,28.992,29.507,30.442,30.965,32.244,31.855,32.250,32.388,32.312,32.607,32.854,31.842,32.680,30.104,31.065,28.447,28.621,28.679,28.344,28.156,28.447,28.570,28.667,29.436,28.698,30.319,29.718,28.776,28.963,28.429,28.555,28.570,28.395,29.163,28.748,29.828,29.420,31.671,30.793,32.379,31.911,32.265,32.313,32.592,30.116,31.175,28.890,29.218,28.496,28.587,28.648,28.508,28.310,28.957,28.748,29.226,31.269,31.199,32.328,31.547,29.811,28.888,28.137,28.285,28.463,28.483,28.557,28.797,29.704,29.399,30.460,30.472,31.603,31.694,31.990,30.547,32.004,28.930,29.626,28.220,28.473,28.552,28.220,28.351,28.694,29.062,28.703,30.867,29.831,32.820,32.548,32.478,32.176,28.473,28.493,28.264,28.442,28.662,28.390,28.372,28.661,29.225,28.774,29.797,29.597,30.999,30.204,31.244,29.254,29.575,28.162,28.510,28.532,28.530,28.600,28.449,28.428,28.642,29.765,30.602,32.329,32.418,34.008,34.239,32.016,28.925,28.322,28.395,28.078,28.614,28.183,28.452,28.517,28.848,28.593,28.970,29.005,29.060,30.394,28.891,30.257,28.808,28.746,28.235,28.295,28.682,28.561,28.342,28.250,29.916,28.593,31.676,31.333,33.850,33.254,32.702,33.224,28.516,28.235,28.317,28.028,28.465,28.464,28.845,28.247,28.642,28.392,28.464,28.436,28.858,28.573,28.979,28.471,29.039,28.500,28.832,28.364,28.280,28.374,28.837,28.830,29.056,31.258,31.946,32.501,33.101,33.231,32.988,30.287,28.260,28.161,28.310,28.257,28.417,28.346,28.377,28.301,28.276,28.101,28.675,28.288,28.494,28.615,28.389,28.926,28.616,28.512,27.969,28.178,28.515,28.392,28.549,28.412,31.642,30.166,32.618,32.614,33.084,32.530,31.086,32.028};
  cout<<weightedAverage(foo)<<"\n"<<aveOfAboveAverage(foo)<<"\n";
}

double map(double val, double min, double max, double newMin,double newMax)
{
  return -1 * ((val - min) / (min - max) * (newMax - newMin) + newMin);
}

double weightedAverage(double *foo)
{
  double max = foo[0];
  double min = foo[0];
  int size = sizeof(foo) + 1;

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
  int size = sizeof(foo) + 1;
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
