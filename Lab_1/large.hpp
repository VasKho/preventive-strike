#ifndef _LARGE_H_
#define _LARGE_H_
#include <iostream>
#include <string>
#include <string.h>
#include <vector>


class Large
{
private:
    enum Sign {POSITIVE, NEGATIVE};
    Sign sign;
    std::vector<int> number;
    short compare_absolutes(const Large&) const;
    Large& str_to_large(const std::string&);
    Large get_absolute() const;
public:
    Large(const std::string& = "0");
    Large(const Large&);
    Large& operator=(const Large&);
    friend std::ostream& operator<<(std::ostream&, const Large&);
    friend std::istream& operator>>(std::istream&, Large&);
    friend bool operator==(const Large&, const Large&);
    friend bool operator==(const Large&, const int&);
    friend bool operator!=(const Large&, const Large&);
    friend bool operator!=(const Large&, const int&);
    friend bool operator>(const Large&, const Large&);
    friend bool operator>(const Large&, const int&);
    friend bool operator>=(const Large&, const Large&);
    friend bool operator>=(const Large&, const int&);
    friend bool operator<(const Large&, const Large&);
    friend bool operator<(const Large&, const int&);
    friend bool operator<=(const Large&, const Large&);
    friend bool operator<=(const Large&, const int&);
    friend Large operator+(const Large&, const Large&);
    friend Large operator+(const Large&, const int&);
    friend Large operator-(const Large&, const Large&);
    friend Large operator-(const Large&, const int&);
    friend Large operator*(const Large&, const Large&);
    friend Large operator*(const Large&, const int&);
    friend Large operator/(const Large&, const Large&);
    friend Large operator/(const Large&, const int&);
    Large operator+=(const Large&);
    Large operator+=(const int&);
    Large operator-=(const Large&);
    Large operator-=(const int&);
    Large operator*=(const Large&);
    Large operator*=(const int&);
    Large operator/=(const Large&);
    Large operator/=(const int&);
    Large& operator++();
    Large operator++(int);
    Large& operator--();
    Large operator--(int);
    operator int() const;
};
#endif
