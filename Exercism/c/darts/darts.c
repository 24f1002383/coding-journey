#include "darts.h"

uint8_t score(coordinate_t position)
{
    float distance = position.x * position.x +
                     position.y * position.y;

    if (distance <= 1.0F)
        return 10;
    else if (distance <= 25.0F)
        return 5;
    else if (distance <= 100.0F)
        return 1;
    else
        return 0;
}