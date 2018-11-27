#include <iostream>
#include <vector>

std::vector<std::string> split(std::string s, std::string delim)
{
    size_t pos = 0;
    std::string token;
    std::vector<std::string> v;

    while ((pos = s.find(delim)) != std::string::npos) 
    {
        token = s.substr(0, pos);
        v.push_back(token);
        s.erase(0, pos + delim.length());
    }
    v.push_back(s);
    return v;
}

int main()
{
    std::string s = "foo:";
    std::string delim = ":";
    std::vector<std::string> v;
    v = split(s, delim);
    int i = 0;
    for(auto it = v.begin(); it != v.end(); it++)
    {
        std::cout << i << ": " << *it << std::endl;
    }
}
