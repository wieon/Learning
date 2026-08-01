#include <stdio.h>

char Grade_convertion( int score ) {
    if (score >= 90)  return 'A';
    else if (score >= 80 && score < 90)  return 'B';
    else if (score >= 70 && score < 80)  return 'C';
    else if (score >= 60 && score < 70)  return 'D';
    else  return 'E';
}

int main() {
    int score, N, i, A, B, C, D, E;
    char grade;

    A = 0; B = 0; C = 0; D = 0; E = 0;
    scanf("%d", &N);
    for (i=0; i<N; i++) {
        scanf("%d", &score);
        grade = Grade_convertion(score);
        switch (grade) {
            case 'A': A++; break;
            case 'B': B++; break;
            case 'C': C++; break;
            case 'D': D++; break;
            case 'E': E++; break;
        }
    }   
    printf("%d %d %d %d %d", A, B, C, D, E);

    return 0;
}