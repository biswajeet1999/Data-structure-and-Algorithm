#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
typedef struct stack
{
    char a[50];
    int top;
}STACK;
STACK *createstack()
{
    STACK *stack=(STACK *)malloc(sizeof(STACK));
    stack->top=-1;
    return stack;
}
void push(STACK *s,char data)
{
    if(s->top==49)
        printf("Stack is full\n");
    else{
        s->a[++(s->top)]=data;
    }
}
char pop(STACK *s)
{
    if(s->top==-1)
        printf("Stack is empty\n");
    else{
        char x=s->a[s->top];
        (s->top)--;
        return x;
    }
}
int getvalue(STACK *s)
{
    int j,val1;
    char val[20];
    pop(s);   // first remove the semicolon just before the operator
    for(j=0;s->a[s->top]!=',';j++){
        val[j]=pop(s);
    }
    val[j]='\0';  val1=atoi(strrev(val));
    return val1;
}
char *convertstring(int x)
{
    char val[10];
    int i,r;
    for(i=0;x;i++){
        r=x%10;
        val[i]=48+r;
        x=x/10;
    }
    val[i]='\0';
    return (strrev(val));
}
void main()
{
    STACK *stack=createstack();
    char postfix[20],*val;
    int val1,val2,val3,i;
    printf("Enter postfix expression put \",\" between each term\n");
    fflush(stdin);
    scanf("%[^\n]s",postfix);
    push(stack,')');
    for(i=0;stack->a[stack->top]!=')';i++){
        if((postfix[i]>='0' && postfix[i]<='9') || postfix[i]==',')
            push(stack,postfix[i]);
        else if(postfix[i]=='+'){
            val1=getvalue(stack);
            printf("%d",val1);
            val2=getvalue(stack);
            val3=val2+val1;
            val=convertstring(val3);
            for(i=0;val[i]!='\0';i++)
            push(stack,val[i]);
            push(stack,',');
        }
        else if(postfix[i]=='-'){
           val1=getvalue(stack);
           val2=getvalue(stack);
           val3=val2-val1;
           val=convertstring(val3);
           for(i=0;val[i]!='\0';i++)
               push(stack,val[i]);
           push(stack,',');
        }
        else if(postfix[i]=='*'){
           val1=getvalue(stack);
           val2=getvalue(stack);
           val3=val2*val1;
           val=convertstring(val3);
           for(i=0;val[i]!='\0';i++)
               push(stack,val[i]);
           push(stack,',');
        }
        else if(postfix[i]=='/'){
           val1=getvalue(stack);
           val2=getvalue(stack);
           val3=val2/val1;
           val=convertstring(val3);
           for(i=0;val[i]!='\0';i++)
               push(stack,val[i]);
           push(stack,',');
        }
        else if(postfix[i]=='^'){
           val1=getvalue(stack);
           val2=getvalue(stack);
           val3=pow(val2,val1);
           val=convertstring(val3);
           for(i=0;val[i]!='\0';i++)
               push(stack,val[i]);
           push(stack,',');
        }
    }
   pop(stack);
   printf("VALUE IS : ");
   while(stack->a[stack->top]!=')'){
      printf("%c",pop(stack));
   }
   printf("\n\n");
}
