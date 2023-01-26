#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <time.h>

int main() {
    int sockfd, portno = 12345;
    struct sockaddr_in serv_addr;

    // create socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("Error opening socket");
        exit(1);
    }

    // configure server address
    memset((char *) &serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(portno);

    // bind socket to address
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
        perror("Error binding socket");
        exit(1);
    }

    // initialize random number generator
    srand(time(NULL));

    for (;;) {
        struct sockaddr_in cli_addr;
        socklen_t cli_len = sizeof(cli_addr);

        // generate random number
        int rand_num = rand() % 900 + 100;

        // send random number to client
        if (sendto(sockfd, &rand_num, sizeof(rand_num), 0, (struct sockaddr *) &cli_addr, cli_len) < 0) {
            perror("Error sending random number");
            exit(1);
        }

        printf("Sent random number %d to client\n", rand_num);
    }

    close(sockfd);
    return 0;
}
