#include <stdlib.h>
#include <stdio.h>

typedef struct line{
    unsigned long len;
    char* data;
}line;

typedef struct lines{
    line **data;
    unsigned long len;
}lines;


void rain_memmove(char* dest,const char* src, unsigned long n){
    if(dest > src && dest-src < n){
        for (; n--; dest[n] = src[n]);
        return;
    }
    for (; n--; *(dest++) = *(src++));
    return;
}



void destroy_lines(lines* l){
    if(l == (void*)0) return;
    if(l->len == 0) goto free_lines;

    for(unsigned long it = (l->len - 1); it >= 0; it--){
        free(l->data[it]->data);
        free(l->data[it]);
    };
    
free_lines:
    free(l);
    return;
}




line* create_line(const char* from, unsigned long n){
    line* new_line = malloc(sizeof(line));
    new_line->len = n;
    new_line->data = malloc(n + 1);
    rain_memmove(new_line->data, from, n);
    new_line->data[n] = 0;
    return new_line;
}



lines* readlines(const char* path){
    FILE* file = fopen(path, "r");
    if(file == NULL) return NULL;
    fseek(file, 0, SEEK_END);
    unsigned long size = ftell(file);
    fseek(file, 0, SEEK_SET);
    char bytes[size];
    fread(bytes, 1, size, file);
    fclose(file);

    unsigned long head = 0;
    unsigned long tail = 0;
    unsigned long countLines = 0;
    for (unsigned int it = 0; it < size; it++) {
        if(bytes[it] == '\n'){
            countLines++;
        }
    }
    if(bytes[size-1]!= '\n') countLines++;

    lines *lns = malloc(sizeof(lines));
    lns->len = countLines;
    lns->data = malloc(sizeof(lines*)*countLines);
    unsigned long fr = 0;
    for (unsigned int it = 0; it < size; it++) {
        tail++;

        if(bytes[it] == '\n'){
            line *ln = create_line(&bytes[head], tail-1);
            head = it + 1;
            tail = 0;
            lns->data[fr++] = ln;
        }
    }
    if(bytes[size-1]!= '\n'){
        line *ln = create_line(&bytes[head], tail);
        lns->data[fr++] = ln;
    };

    return lns;
};


inline _Bool compare_line(const char* left, const char* right, unsigned int n){
    for (unsigned int it = 0; it < n; it++) {
        if(left[it] != right[it]){
            return 0;
        }
    }
    return 1;
}

inline unsigned long increase_score(unsigned long cycles, unsigned long reg, 
                                    unsigned int* crt){
    unsigned long result = 0;
 
    if(cycles == 20 || cycles%40 == 20){
        result = cycles * reg;
    }
    if(cycles%40 == 0){
        *crt = 0;
        putchar('\n');
    }

    return result;
}

inline void draw(unsigned int* crt, unsigned int* reg){
    int abs = (*reg) - (*crt);
    if(abs < 0) abs *= -1;

    if(abs <= 1){
        putchar('#');
    }
    else{
        putchar(' ');
    }
    *crt +=1;
}




void solvePuzzleOne(lines *lns)
{
    unsigned int reg     = 1;
    unsigned long cycles = 0;
    unsigned long score  = 0;
    unsigned int crt     = 0;


    for (unsigned long it = 0; it < lns->len ; it++) {
        //char c_value[100];
       
        if(compare_line(lns->data[it]->data, "noop", 4)){
            draw(&crt, &reg);
            score += increase_score(++cycles, reg, &crt);
        }
        else {
            //unsigned long copy = (lns->data[it]->len - 4);
            //rain_memmove(c_value,  &lns->data[it]->data[4], copy);
            //c_value[copy] = '\0';
            //int value = atoi(c_value);
            int value = atoi(&lns->data[it]->data[4]);
            draw(&crt, &reg);
            score += increase_score(++cycles, reg, &crt);
            draw(&crt, &reg);
            score += increase_score(++cycles, reg, &crt);
            reg += value;
        }
    }

    printf("%ld\n", score);

}




int main(int argc, char** argv)
{

    if(argc < 2){
        perror("you should pass a path to a file here");
        exit(0);
    }
    lines *lns = readlines(argv[1]);
    solvePuzzleOne(lns);
    destroy_lines(lns);
}