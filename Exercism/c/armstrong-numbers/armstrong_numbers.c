#include "armstrong_numbers.h"
#include <math.h>

bool is_armstrong_number(int number)
{
    int original = number;
    int digits = 0;
    int sum = 0;

    int temp = number;

    // Count digits
    do {
        digits++;
        temp /= 10;
    } while (temp != 0);

    // Calculate Armstrong sum
    temp = number;

    do {
        int digit = temp % 10;
        sum += (int)pow(digit, digits);
        temp /= 10;
    } while (temp != 0);

    return sum == original;
}