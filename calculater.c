#include <stdio.h>

int main(){
    char o;
    int x,y;

    while(1){
        printf("\n>> ");
        scanf("%d %c %d", &x, &o, &y);
        getchar();
        if (o == '+'){
            printf("\n%d", x + y);
        }
        else if(o == '-'){
            printf("\n%d", x-y);
        }
        else if (o == '*'){
            printf("\n%d", x*y);
        }
        else if (o =='/'){
            printf("\n%d", x/y);
        }
        else{
            printf("wrong format\n");
            break;
        }
    }
    return 0;
}