#include "resistor_color.h"

unsigned int color_code(resistor_band_t color)
{
    return (unsigned int)color;
}
const resistor_band_t *colors(void)
{
    static const resistor_band_t all_colors[RESISTOR_BAND_LIMIT] = {
        BLACK,
        BROWN,
        RED,
        ORANGE,
        YELLOW,
        GREEN,
        BLUE,
        VIOLET,
        GREY,
        WHITE
    };
    return all_colors;
}