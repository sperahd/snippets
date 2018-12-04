#include <cstdio>
#include <cstdlib>
#include <cstring>

void swap(char *a, char *b)
{
    char *temp = a;
    a = b;
    b = temp;
}

void move_spaces(char *str)
{
    int i = 0, num_spaces = 0, num_chars = 0;
    for ((i = strlen(str) - 1); i >= 0; i--)
    {
        num_chars++; 
        if(str[i] == ' ')
        {
            printf("HERE 1\n");
            num_spaces++;
        }
        else
        {
            printf("HERE 2\n");
            if (num_spaces > 0)
            {
                printf("HERE 3\n");
                char temp;
                temp    = str[i];
                str[i]  = str[i+num_spaces];
                str[i+num_spaces]  = temp;
            }
        }
        if (num_chars + num_spaces >= strlen(str))
        {
            printf("HERE\n");
            str[i] = ' ';
        }
    }
    printf("String with moved spaces: %s  %d\n", str, strlen(str));
}

void moveSpaceInFront(char str[]) 
{ 
     // Keep copying non-space characters 
     int i = strlen(str);
     for (int j=i; j >= 0; j--) 
     {
         if (str[j] != ' ') 
             str[i--] = str[j]; 
     }
     // Move spaces to be beginning 
     while (i >= 0) 
         str[i--] = ' '; 
    printf("String with moved spaces: %s  %d\n", str, strlen(str));
} 

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("USAGE: %s <string to be processed>\n", argv[0]);
        exit(-1);
    }
    
    char str[1024];
    snprintf(str, 1024, "%s", argv[1]);
    printf("String without moved spaces: %s  %d\n", str, strlen(str));
    //move_spaces(str);
    moveSpaceInFront(str);
}
