#include "pid.h"
#include <stdio.h>

int main() {

    PID pid = PID(0.1, 100, -100, 0.1, 0.01, 0.5);
    FILE *fp;
    if((fp=fopen("data.csv","w"))==NULL)
    {
        printf("Could not open the data file\n");
        return 1;
    }
    double val = 20;
    fprintf(fp,"t,output,error\n");
    for (int i = 0; i < 100; i++) {
        double inc = pid.calculate(0, val);
        printf("val:%7.3f inc:%7.3f\n", val, inc);
        fprintf(fp,"%d,%7.3f,%7.3f\n",i,val,inc);
        val += inc;
    }
    fclose(fp);

    return 0;


    
}
